#!/usr/bin/env python3
"""Archive media referenced by the site; see ARCHIVING.md."""

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit, urlunsplit

URL = re.compile(r"""https?://[^\s<>"'()[\]`]+""")
MARKDOWN_LINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^\s)]+)\)")
IFRAME = re.compile(r"<iframe\b.*?</iframe>", re.DOTALL | re.IGNORECASE)
METADATA_FIELDS = (
    "title", "description", "upload_date", "duration", "webpage_url",
    "channel", "view_count",
)
GAPS_START = "<!-- automated-media-gaps:start -->"
GAPS_END = "<!-- automated-media-gaps:end -->"
MAX_BYTES = 250 * 1024 * 1024


class ArchiveError(Exception):
    pass


def canonical_url(url):
    parts = urlsplit(html.unescape(url))
    host = (parts.hostname or "").lower().removeprefix("www.")
    path = parts.path.rstrip("/")
    if host in {"youtube.com", "m.youtube.com", "youtube-nocookie.com", "youtu.be"}:
        if host == "youtu.be":
            video_id = path.lstrip("/")
        elif path == "/watch":
            video_id = parse_qs(parts.query).get("v", [""])[0]
        else:
            video_id = path.split("/")[-1] if path.startswith(("/embed/", "/shorts/", "/live/")) else ""
        if re.fullmatch(r"[-\w]{11}", video_id, flags=re.ASCII):
            return f"https://www.youtube.com/watch?v={video_id}"
    # Keep meaningful query parameters (some episode pages use ?id=...).
    query = "&".join(
        pair for pair in parts.query.split("&")
        if pair and not pair.lower().startswith(("utm_", "si=", "fbclid="))
    )
    return urlunsplit(("https", host, path, query, ""))


def media_kind(url, line, podcast_hosts):
    parts = urlsplit(url)
    if re.fullmatch(r"https://www\.youtube\.com/watch\?v=[-\w]{11}", url, flags=re.ASCII):
        return "videos"
    if (
        parts.hostname in podcast_hosts
        or re.search(r"/(podcast|podcasts|episodes|pods)/", parts.path)
        or parts.path.lower().endswith((".mp3", ".m4a"))
    ):
        return "podcasts"
    if parts.hostname in {"vimeo.com", "player.vimeo.com"}:
        return "videos"
    # Conference landing pages may embed recordings, but homepages and event
    # listings are not individual recordings.
    if (
        "I've spoken at" in line
        and parts.path
        and parts.hostname not in {"meetup.com", "www.meetup.com"}
        and not parts.path.endswith("/talks")
    ):
        return "videos"
    return None


def discover(root, manifest):
    podcast_hosts = {
        urlsplit(canonical_url(item["source_url"])).hostname
        for item in manifest["podcasts"]
    }
    found = {}
    for path in [root / "index.md", *sorted((root / "_posts").rglob("*.md"))]:
        for line in path.read_text().splitlines():
            titles = {canonical_url(url): title for title, url in MARKDOWN_LINK.findall(line)}
            for match in URL.finditer(line):
                source = canonical_url(match.group().rstrip(".,;"))
                kind = media_kind(source, line, podcast_hosts)
                if kind:
                    found.setdefault(source, {
                        "kind": kind,
                        "source_url": source,
                        "title": titles.get(source, unquote(urlsplit(source).path).split("/")[-1]),
                    })
    return list(found.values())


def item_slug(candidate):
    url = candidate["source_url"]
    if url.startswith("https://www.youtube.com/watch?v="):
        return parse_qs(urlsplit(url).query)["v"][0]
    parts = urlsplit(url)
    label = re.sub(r"[^a-z0-9]+", "-", f"{parts.hostname}-{unquote(parts.path)}".lower()).strip("-")
    return f"{label[:90]}-{hashlib.sha256(url.encode()).hexdigest()[:8]}"


def run_command(command, timeout):
    try:
        result = subprocess.run(
            command, check=True, text=True, capture_output=True, timeout=timeout,
        )
    except subprocess.CalledProcessError as error:
        raise ArchiveError((error.stderr or error.stdout or str(error))[-1500:].strip()) from error
    except subprocess.TimeoutExpired as error:
        raise ArchiveError(f"Command timed out after {timeout} seconds") from error
    return result.stdout


def verify_episode(candidate, metadata):
    if metadata.get("_type") in {"playlist", "multi_video"} or metadata.get("entries"):
        raise ArchiveError("Source resolves to multiple recordings; select the episode manually")
    title = metadata.get("title", "")
    if not title:
        raise ArchiveError("Source did not provide a recording title")
    if candidate["kind"] != "podcasts":
        return
    # Do not trust an arbitrary embedded player: the episode title must agree
    # with the source URL, including an explicit episode number when present.
    source_path = unquote(urlsplit(candidate["source_url"]).path).lower()
    words = set(re.findall(r"[a-z]{4,}", source_path)) - {
        "podcast", "podcasts", "episodes", "episode", "with", "html",
    }
    title_words = set(re.findall(r"[a-z]{4,}", title.lower()))
    numbers = re.findall(r"(?:episode[-_/ ]*|/)(\d{1,4})(?:[-_/]|$)", source_path)
    if (
        len(words & title_words) < min(2, len(words))
        or (not words and not numbers)
        or any(number not in re.findall(r"\d+", title) for number in numbers)
    ):
        raise ArchiveError(f"Embedded title does not confidently match the episode URL: {title}")


def download(candidate, root, slug, remaining):
    source = candidate["source_url"]
    metadata = json.loads(run_command([
        "yt-dlp", "--ignore-config", "--js-runtimes", "node",
        "--no-playlist", "--socket-timeout", "30",
        "--retries", "2", "--dump-single-json", "--skip-download", "--", source,
    ], 120))
    verify_episode(candidate, metadata)
    kind = candidate["kind"]
    extension = "mp4" if kind == "videos" else "mp3"
    relative = Path("archive") / kind / f"{slug}.{extension}"
    destination = root / relative
    if destination.exists():
        raise ArchiveError(f"Refusing to overwrite an unindexed archive file: {relative}")
    with tempfile.TemporaryDirectory(prefix="archive-media-") as directory:
        output = Path(directory) / f"media.{extension}"
        command = [
            "yt-dlp", "--ignore-config", "--js-runtimes", "node", "--no-playlist",
            "--socket-timeout", "30", "--retries", "2", "--fragment-retries", "2",
            "--max-filesize", str(remaining),
            "--output", str(Path(directory) / "media.%(ext)s"),
        ]
        if kind == "videos":
            command += [
                "--format", "bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720][ext=mp4]",
                "--merge-output-format", "mp4",
            ]
        else:
            command += ["--format", "bestaudio/best", "--extract-audio", "--audio-format", "mp3"]
        run_command([*command, "--", source], 900)
        if not output.is_file() or output.stat().st_size == 0:
            raise ArchiveError("Download produced no media (possibly over the size limit)")
        size = output.stat().st_size
        if size > remaining:
            raise ArchiveError(f"Recording exceeds the remaining per-run budget ({remaining} bytes)")
        streams = json.loads(run_command([
            "ffprobe", "-v", "error", "-show_streams", "-of", "json", str(output),
        ], 30))["streams"]
        required = "video" if kind == "videos" else "audio"
        if not any(stream.get("codec_type") == required for stream in streams):
            raise ArchiveError(f"Downloaded file has no {required} stream")
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Temporary files can live on a different filesystem.
        shutil.copyfile(output, destination)
    if kind == "videos":
        destination.with_suffix(".info.json").write_text(
            json.dumps({key: metadata.get(key) for key in METADATA_FIELDS}, indent=2) + "\n"
        )
    return relative.as_posix(), size, metadata["title"]


def add_post_links(root, archived):
    def archive_for(url):
        return archived.get(canonical_url(url))

    for path in sorted((root / "_posts").rglob("*.md")):
        original = path.read_text()

        def link(match):
            file = archive_for(match[2])
            if not file or original[match.end():].startswith(f" ([archived](/{file}))"):
                return match[0]
            return f"{match[0]} ([archived](/{file}))"

        content = MARKDOWN_LINK.sub(link, original)

        def iframe(match):
            sources = re.findall(r'\bsrc=["\']([^"\']+)["\']', match[0], re.IGNORECASE)
            for source in sources:
                file = archive_for(source)
                if file and f"](/{file})" not in content:
                    return f"{match[0]}\n\n[Archived recording](/{file})"
            return match[0]

        content = IFRAME.sub(iframe, content)
        if content != original:
            path.write_text(content)


def update_gaps(root, manifest):
    gaps = [
        item for kind in ("videos", "podcasts") for item in manifest[kind]
        if not item.get("file")
    ]
    path = root / "archive/README.md"
    content = path.read_text()
    if not gaps and GAPS_START not in content:
        return
    lines = [
        GAPS_START, "### Automated follow-up", "",
        "See each manifest entry's `notes` for download errors and manual follow-up details.", "",
    ]
    lines += [
        f"- <{item['source_url']}>: `{item['status']}`."
        for item in gaps
    ] or ["No outstanding automated gaps."]
    section = "\n".join([*lines, GAPS_END])
    if GAPS_START in content:
        start = content.index(GAPS_START)
        end = content.index(GAPS_END, start) + len(GAPS_END)
        content = content[:start] + section + content[end:]
    else:
        content += "\n" + section + "\n"
    path.write_text(content)


def archive(root, dry_run=False):
    path = root / "archive/manifest.json"
    original = path.read_text()
    manifest = json.loads(original)
    indexed = {
        canonical_url(item["source_url"]): item
        for kind in ("videos", "podcasts") for item in manifest[kind]
    }
    candidates = discover(root, manifest)
    if dry_run:
        for candidate in candidates:
            item = indexed.get(candidate["source_url"])
            if not item or not item.get("file"):
                print(f"{candidate['kind']}: {candidate['source_url']}")
        return
    remaining = MAX_BYTES
    for candidate in candidates:
        source = candidate["source_url"]
        item = indexed.get(source)
        if item and item.get("file"):
            if not (root / item["file"]).is_file():
                raise ArchiveError(f"Manifest references a missing file: {item['file']}")
            continue
        if item is None:
            item = {
                "slug": item_slug(candidate), "title": candidate["title"],
                "source_url": source, "file": None, "status": "needs-manual-check",
            }
            manifest[candidate["kind"]].append(item)
            indexed[source] = item
        if remaining <= 0:
            item.update(status="deferred", notes="Per-run 250 MB budget exhausted; retry next run.")
            continue
        try:
            file, size, title = download(candidate, root, item["slug"], remaining)
        except ArchiveError as error:
            print(f"::warning::{source}: {error}")
            item.update(status="needs-manual-check", notes=str(error))
        else:
            remaining -= size
            item.update(file=file, status="archived", title=title)
            item.pop("notes", None)
            print(f"Archived {source} ({size} bytes)")
    add_post_links(root, {
        source: item["file"] for source, item in indexed.items() if item.get("file")
    })
    update_gaps(root, manifest)
    if manifest != json.loads(original):
        manifest["generated_at"] = date.today().isoformat()
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="List pending sources without network requests or writes")
    args = parser.parse_args()
    archive(Path(__file__).resolve().parents[1], dry_run=args.dry_run)


if __name__ == "__main__":
    main()
