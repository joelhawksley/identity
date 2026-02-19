"""
Extract songs from a church live stream and upload as a private YouTube video.

1. Downloads live streams from the church YouTube channel
2. Uses audio analysis to detect music segments (hymns/songs)
3. Extracts and concatenates those segments
4. Uploads the result as a private video

Tracks processed streams in processed_streams.json to avoid re-processing.
On each run, processes all unprocessed streams from the last 6 months.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import librosa
import numpy as np
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


CHANNEL_URL = os.environ.get(
    "YOUTUBE_CHANNEL_URL",
    "https://www.youtube.com/@christtheservantlutheranch5318",
)
MIN_MUSIC_DURATION = 60  # Ignore music segments shorter than 60 seconds
MERGE_GAP = 10  # Merge music segments separated by less than 10 seconds
PADDING = 2  # Add 2 seconds of padding around each segment

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
]


# ---------------------------------------------------------------------------
# Already-uploaded detection (via YouTube API)
# ---------------------------------------------------------------------------

def get_uploaded_titles(youtube) -> set[str]:
    """
    Fetch titles of all videos on the authenticated user's channel.

    Returns a set of titles for quick lookup.
    """
    print("Fetching existing uploads from your YouTube channel...")

    # Get the authenticated user's upload playlist
    channels = youtube.channels().list(part="contentDetails", mine=True).execute()
    if not channels.get("items"):
        print("WARNING: Could not fetch channel info. Assuming no prior uploads.")
        return set()

    uploads_playlist = (
        channels["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    )

    titles = set()
    next_page = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=next_page,
        )
        response = request.execute()

        for item in response.get("items", []):
            titles.add(item["snippet"]["title"])

        next_page = response.get("nextPageToken")
        if not next_page:
            break

    print(f"Found {len(titles)} existing uploads")
    return titles


# ---------------------------------------------------------------------------
# Step 1: Find and download live streams
# ---------------------------------------------------------------------------

def get_recent_livestreams(channel_url: str, months: int = 6) -> list[tuple[str, str, str]]:
    """
    Return a list of (video_id, title, upload_date) for live streams
    from the last `months` months, oldest first.
    """
    print(f"Fetching live streams from the last {months} months...")
    cutoff = datetime.now() - timedelta(days=months * 30)
    cutoff_str = cutoff.strftime("%Y%m%d")

    result = subprocess.run(
        [
            "yt-dlp",
            "--flat-playlist",
            "--print", "%(id)s\t%(title)s\t%(upload_date)s",
            "--dateafter", cutoff_str,
            f"{channel_url}/streams",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.strip().splitlines()
    if not lines:
        print("No live streams found on the channel.")
        return []

    streams = []
    for line in lines:
        parts = line.split("\t", 2)
        if len(parts) >= 2:
            video_id = parts[0]
            title = parts[1]
            upload_date = parts[2] if len(parts) == 3 else "unknown"
            streams.append((video_id, title, upload_date))

    # Reverse so oldest is first (catch up in chronological order)
    streams.reverse()
    print(f"Found {len(streams)} live streams in the last {months} months")
    return streams


def download_video(url: str, output_path: str) -> str:
    """Download video and return the path to the downloaded file."""
    print("Downloading video...")
    subprocess.run(
        [
            "yt-dlp",
            "-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "--merge-output-format", "mp4",
            "-o", output_path,
            url,
        ],
        check=True,
    )
    print(f"Downloaded to {output_path}")
    return output_path


# ---------------------------------------------------------------------------
# Step 2: Detect music segments using inaSpeechSegmenter
# ---------------------------------------------------------------------------

def extract_audio(video_path: str, audio_path: str) -> str:
    """Extract audio from video as WAV for analysis."""
    print("Extracting audio for analysis...")
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", video_path,
            "-ac", "1",          # mono
            "-ar", "22050",      # 22kHz sample rate (librosa default)
            "-vn",               # no video
            audio_path,
        ],
        check=True,
        capture_output=True,
    )
    return audio_path


def detect_music_segments(video_path: str) -> list[tuple[float, float]]:
    """
    Analyze audio to find music segments using librosa spectral features.

    Designed for church services: distinguishes congregational hymns (with
    organ/piano accompaniment) from spoken word (sermon, readings, liturgy).

    Uses multiple features with strict thresholds and majority-vote smoothing
    to avoid false positives from tonal speech.

    Returns a list of (start, end) tuples in seconds.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = os.path.join(tmpdir, "audio.wav")
        extract_audio(video_path, audio_path)

        print("Analyzing audio for music segments...")
        y, sr = librosa.load(audio_path, sr=22050)

    # Analyze in 3-second windows with 1-second hop for more context
    win_sec = 3.0
    hop_sec = 1.0
    win_samples = int(win_sec * sr)
    hop_samples = int(hop_sec * sr)

    scores = []  # float scores per window (higher = more likely music)
    timestamps = []

    for start_sample in range(0, len(y) - win_samples, hop_samples):
        window = y[start_sample : start_sample + win_samples]
        t = start_sample / sr
        timestamps.append(t)

        # Skip silence
        rms = np.sqrt(np.mean(window**2))
        if rms < 0.005:
            scores.append(0.0)
            continue

        # --- Feature 1: Spectral flatness ---
        # Closer to 0 = tonal (music), closer to 1 = noise-like
        # Speech is typically 0.02-0.15, music with instruments < 0.05
        flatness = np.mean(librosa.feature.spectral_flatness(y=window))

        # --- Feature 2: Harmonic-to-percussive ratio ---
        # Singing + instruments = high harmonic content
        harmonic, percussive = librosa.effects.hpss(window)
        h_energy = np.sum(harmonic**2)
        p_energy = np.sum(percussive**2)
        harmonic_ratio = h_energy / (h_energy + p_energy + 1e-10)

        # --- Feature 3: Chroma concentration ---
        # Music has energy concentrated in specific pitch classes;
        # speech is more spread across the chromagram
        chroma = librosa.feature.chroma_stft(y=window, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)  # 12 pitch classes
        chroma_std = np.std(chroma_mean)  # High = concentrated pitches

        # --- Feature 4: Spectral contrast ---
        # Music (especially with instruments) has higher spectral contrast
        contrast = librosa.feature.spectral_contrast(y=window, sr=sr)
        mean_contrast = np.mean(contrast)

        # --- Feature 5: Tempo regularity ---
        # Music has a steady beat; speech does not
        onset_env = librosa.onset.onset_strength(y=window, sr=sr)
        if len(onset_env) > 1:
            ac = np.correlate(onset_env - np.mean(onset_env),
                              onset_env - np.mean(onset_env), mode='full')
            ac = ac[len(ac)//2:]  # positive lags only
            if ac[0] > 0:
                ac = ac / ac[0]
                # Look for a strong peak in autocorrelation (indicates tempo)
                tempo_regularity = np.max(ac[2:]) if len(ac) > 2 else 0
            else:
                tempo_regularity = 0
        else:
            tempo_regularity = 0

        # --- Weighted scoring ---
        score = 0.0

        # Low spectral flatness = tonal (strong indicator)
        if flatness < 0.03:
            score += 2.0
        elif flatness < 0.06:
            score += 1.0

        # High harmonic ratio
        if harmonic_ratio > 0.7:
            score += 2.0
        elif harmonic_ratio > 0.6:
            score += 1.0

        # Strong chroma concentration (pitched instruments/singing)
        if chroma_std > 0.08:
            score += 1.5
        elif chroma_std > 0.05:
            score += 0.5

        # High spectral contrast (instruments)
        if mean_contrast > 25:
            score += 1.0

        # Regular tempo
        if tempo_regularity > 0.3:
            score += 1.0

        # Penalize features typical of speech
        # Speech has moderate flatness and lower harmonic ratio
        if flatness > 0.06 and harmonic_ratio < 0.65:
            score -= 2.0

        scores.append(score)

    # --- Smoothing: majority vote over a sliding window ---
    # This eliminates isolated false positives/negatives
    smooth_window = 15  # 15-second smoothing window
    threshold = 3.5     # Require strong evidence of music
    smoothed = []
    for i in range(len(scores)):
        window_start = max(0, i - smooth_window // 2)
        window_end = min(len(scores), i + smooth_window // 2 + 1)
        window_scores = scores[window_start:window_end]
        avg_score = np.mean(window_scores)
        smoothed.append(avg_score >= threshold)

    # Convert boolean array to segments
    music_segments = []
    in_segment = False
    seg_start = 0.0

    for i, (t, m) in enumerate(zip(timestamps, smoothed)):
        if m and not in_segment:
            seg_start = t
            in_segment = True
        elif not m and in_segment:
            music_segments.append((seg_start, t))
            in_segment = False

    if in_segment:
        music_segments.append((seg_start, timestamps[-1] + hop_sec))

    print(f"Found {len(music_segments)} raw music segments")

    # Merge nearby segments
    merged = merge_segments(music_segments, gap=MERGE_GAP)
    print(f"After merging nearby segments: {len(merged)} segments")

    # Filter out short segments (hymns are typically 2-5 minutes)
    filtered = [(s, e) for s, e in merged if (e - s) >= MIN_MUSIC_DURATION]
    print(f"After filtering short segments (<{MIN_MUSIC_DURATION}s): {len(filtered)} segments")

    for i, (start, end) in enumerate(filtered):
        duration = end - start
        print(f"  Song {i+1}: {format_time(start)} - {format_time(end)} ({duration:.0f}s)")

    return filtered


def merge_segments(
    segments: list[tuple[float, float]], gap: float
) -> list[tuple[float, float]]:
    """Merge segments that are within `gap` seconds of each other."""
    if not segments:
        return []

    merged = [segments[0]]
    for start, end in segments[1:]:
        prev_start, prev_end = merged[-1]
        if start - prev_end <= gap:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))
    return merged


def format_time(seconds: float) -> str:
    """Format seconds as HH:MM:SS."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


# ---------------------------------------------------------------------------
# Step 3: Extract and concatenate song segments
# ---------------------------------------------------------------------------

def extract_songs(
    video_path: str, segments: list[tuple[float, float]], output_path: str
) -> str:
    """Extract music segments from the video and concatenate them."""
    if not segments:
        print("No music segments found!")
        sys.exit(1)

    print("Extracting and concatenating song segments...")

    with tempfile.TemporaryDirectory() as tmpdir:
        segment_files = []
        for i, (start, end) in enumerate(segments):
            # Add padding
            padded_start = max(0, start - PADDING)
            padded_end = end + PADDING

            seg_path = os.path.join(tmpdir, f"segment_{i:03d}.mp4")
            segment_files.append(seg_path)

            subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-ss", str(padded_start),
                    "-to", str(padded_end),
                    "-i", video_path,
                    "-c", "copy",
                    "-avoid_negative_ts", "make_zero",
                    seg_path,
                ],
                check=True,
                capture_output=True,
            )

        # Create concat file list
        concat_list = os.path.join(tmpdir, "concat.txt")
        with open(concat_list, "w") as f:
            for seg_path in segment_files:
                f.write(f"file '{seg_path}'\n")

        # Concatenate all segments
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", concat_list,
                "-c", "copy",
                output_path,
            ],
            check=True,
            capture_output=True,
        )

    print(f"Songs extracted to {output_path}")
    return output_path


# ---------------------------------------------------------------------------
# Step 4: Upload to YouTube as a private video
# ---------------------------------------------------------------------------

def get_youtube_service():
    """Authenticate and return a YouTube API service object."""
    creds = None
    token_path = Path("token.json")
    client_secret_path = Path("client_secret.json")

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
            # Save refreshed token
            with open(token_path, "w") as f:
                f.write(creds.to_json())
        else:
            print("ERROR: No valid OAuth token found.")
            print("Run this script locally first to generate token.json")
            sys.exit(1)

    return build("youtube", "v3", credentials=creds)


def upload_to_youtube(video_path: str, title: str, description: str) -> str:
    """Upload video to YouTube as private and return the video ID."""
    print(f"Uploading to YouTube: {title}")
    youtube = get_youtube_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["worship", "hymns", "lutheran", "church"],
            "categoryId": "22",  # People & Blogs
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        video_path,
        mimetype="video/mp4",
        resumable=True,
        chunksize=10 * 1024 * 1024,  # 10 MB chunks
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  Upload progress: {int(status.progress() * 100)}%")

    video_id = response["id"]
    print(f"Upload complete! Video ID: {video_id}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    return video_id


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_stream(
    video_id: str, title: str, workdir: str, debug: bool
) -> bool:
    """Process a single stream. Returns True if successful."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"\n{'='*60}")
    print(f"Processing: {title}")
    print(f"URL: {url}")
    print(f"{'='*60}")

    try:
        raw_video = os.path.join(workdir, f"{video_id}.mp4")
        download_video(url, raw_video)

        segments = detect_music_segments(raw_video)

        songs_video = os.path.join(workdir, f"{video_id}_songs.mp4")
        extract_songs(raw_video, segments, songs_video)

        if debug:
            output_file = f"songs_debug_{video_id}.mp4"
            shutil.copy2(songs_video, output_file)
            print(f"Debug mode: saved to {output_file} (skipping upload)")
        else:
            today = datetime.now().strftime("%B %d, %Y")
            upload_title = f"Worship Songs - {title}"
            upload_description = (
                f"Songs extracted from: {title}\n"
                f"Source: {url}\n"
                f"Extracted on: {today}\n"
            )
            upload_to_youtube(songs_video, upload_title, upload_description)

        # Clean up downloaded files to save disk space
        for f in [raw_video, songs_video]:
            if os.path.exists(f):
                os.remove(f)

        return True

    except Exception as e:
        print(f"ERROR processing {video_id}: {e}")
        return False


def make_upload_title(stream_title: str) -> str:
    """Generate the upload title for a given stream title."""
    return f"Worship Songs - {stream_title}"


def main():
    parser = argparse.ArgumentParser(description="Extract worship songs from church live streams.")
    parser.add_argument("--debug", action="store_true", help="Skip YouTube upload; save output to current directory")
    parser.add_argument("--months", type=int, default=6, help="How many months back to check (default: 6)")
    args = parser.parse_args()

    # Fetch all streams from the last N months
    streams = get_recent_livestreams(CHANNEL_URL, months=args.months)
    if not streams:
        return

    # Check which have already been uploaded (by matching title)
    if args.debug:
        uploaded_titles = set()
        print("Debug mode: skipping uploaded-title check")
    else:
        youtube = get_youtube_service()
        uploaded_titles = get_uploaded_titles(youtube)

    to_process = [
        (vid, title, date)
        for vid, title, date in streams
        if make_upload_title(title) not in uploaded_titles
    ]

    if not to_process:
        print("All recent streams have already been processed.")
        return

    print(f"\n{len(to_process)} stream(s) to process ({len(streams) - len(to_process)} already done)")

    with tempfile.TemporaryDirectory() as workdir:
        for video_id, title, upload_date in to_process:
            success = process_stream(video_id, title, workdir, args.debug)
            if success:
                print(f"Successfully processed {video_id}.")
            else:
                print(f"Skipping {video_id} due to error.")

    print(f"\nDone! Processed {len(to_process)} stream(s).")


if __name__ == "__main__":
    main()
