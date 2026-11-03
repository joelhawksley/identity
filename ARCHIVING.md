# Archiving videos and podcasts (repeatable process)

This repo keeps local, Git-LFS-backed copies of externally-hosted videos and
podcast episodes referenced in `index.md` and `_posts/`, so they survive link
rot, platform shutdowns, and takedowns. This document is the reusable
procedure for refreshing that archive — e.g. after adding new talks or
podcast appearances to `index.md`.

## Scheduled archiving

The **Archive media** GitHub Actions workflow runs every Monday at 08:00 UTC
and can also be started from the Actions tab with **Run workflow**. The workflow
must be on the default branch for its schedule to run. In repository settings,
under **Actions → General → Workflow permissions**, enable **Allow GitHub Actions
to create and approve pull requests**. The workflow uses `GITHUB_TOKEN` with
contents and pull request write permissions; no additional secret is needed.
It opens pull requests but never approves or merges them.

Each run scans `index.md` and `_posts/**/*.md` for YouTube links (including
embeds), Vimeo links, likely podcast episode links, known podcast hosts, and
individual talk pages in the index's speaking list. It does not search the web
for appearances that aren't linked from the site. Podcast discovery recognizes
`/podcast/`, `/podcasts/`, `/episodes/`, `/pods/`, and direct MP3/M4A links;
other URL patterns on new hosts need manual inventory.

The archiver skips files already indexed in the manifest, tries `yt-dlp` for
new or unresolved sources, caps videos at 720p, and limits newly archived media
to **250 MiB per run**. Individual downloads have a 15-minute timeout. Files
over the remaining budget are not committed; temporary downloads can exceed
that budget while downloading or merging. The workflow avoids downloading
existing LFS objects, but new uploads still consume the account's LFS quota.

Successful downloads update the manifest and post backup links, leaving
`index.md` untouched. Failed downloads and podcast players whose titles cannot
be confidently matched to the episode URL are recorded in the manifest and an
automated follow-up section in `archive/README.md`. RSS recovery remains a
manual step below; the workflow never guesses at a replacement episode.

Changes are proposed in a single pull request from an
`automation/archive-media-*` branch. While that pull request remains open,
subsequent runs skip work to avoid duplicate downloads and LFS uploads. Merge
or close it to allow another refresh. Runs with no changes open no pull request.
Failures appear in Actions logs; unresolved sources produce warnings and are
retried on subsequent refreshes.

To preview pending sources locally without downloading or changing files:

```bash
python3 scripts/archive_media.py --dry-run
```

To run a refresh locally, install the prerequisites below plus Node.js 22+
for YouTube's JavaScript challenges, then run `python3 scripts/archive_media.py`.
The workflow installs `yt-dlp[default]` (including its challenge solver) and
Node.js. Run the archiver's offline tests with:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_archive_media.py'
```

## Prerequisites

```bash
brew install yt-dlp git-lfs ffmpeg
git lfs install --local
```

`.gitattributes` already tracks `archive/videos/*.mp4` and
`archive/podcasts/*.mp3` via LFS — no setup needed beyond having `git-lfs`
installed.

## 1. Inventory links

Find every external video/podcast URL in the site content:

```bash
# YouTube links
grep -oE 'https?://(www\.)?(youtube\.com|youtu\.be)[^) "<>]*' index.md _posts/*.md

# Likely podcast links (adjust the exclude list for known non-media domains)
grep -oE 'https?://[^) "<>]*' index.md _posts/*.md \
  | grep -viE 'youtube|youtu\.be|github\.com|meetup\.com|instagram'
```

Dedupe YouTube URLs by the 11-character video ID (the same video is often
linked via both `youtu.be/<id>` and `youtube.com/watch?v=<id>`, sometimes with
extra query params like `&t=` or `?si=`).

## 2. Download videos

```bash
yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" \
  --merge-output-format mp4 \
  --write-info-json \
  -o "archive/videos/<id>.%(ext)s" \
  "https://www.youtube.com/watch?v=<id>"
```

720p keeps individual files in the tens-to-low-hundreds of MB instead of
several hundred MB at 1080p — important since GitHub's free Git LFS quota is
1GB storage/bandwidth per account. Go lower (480p) or higher (1080p) depending
on quota/budget; this is a deliberate tradeoff each time, not a fixed rule.

After downloading, trim each `.info.json` down to the essential fields (title,
description, upload_date, duration, webpage_url, channel, view_count) — the
raw file can be many MB of formats/comments data that isn't useful for an
archival record.

## 3. Resolve and download podcast episodes

Podcast episode pages are usually *not* direct audio files, so each needs
manual resolution:

1. Try `yt-dlp --simulate -j <url>` first — it resolves many embeds (Acast,
   Simplecast, Buzzsprout iframes, Transistor) automatically.
2. If that 404s or times out, check if the show has moved/renamed its feed,
   and search the show's RSS feed for an episode title match:
   ```bash
   curl -s "<show-rss-url>" -o /tmp/show.rss
   python3 -c "...parse <item> blocks, match by title, read <enclosure url=...>..."
   ```
3. If a page embeds a player pointing to an mp3, double check the mp3 slug
   actually matches the expected episode (sites occasionally embed the wrong
   episode — verify episode numbers/titles match before trusting it).
4. Download confirmed mp3 URLs directly with `curl -L -o archive/podcasts/<slug>.mp3 <url>`.
5. If a site/domain is completely unreachable (DNS failure, timeout), don't
   guess — log it as a manual follow-up item instead of skipping silently.

## 4. Update `archive/manifest.json`

Record every item (archived or not) with: slug/id, title, original source URL,
archived file path (or `null`), and a status string. Use clear status values
like `archived`, `needs-manual-check`, or `unreachable` so gaps are visible
at a glance.

## 5. Link archived copies from posts

In `_posts/*.md`, add an `([archived](/archive/...))` link
immediately after each original external link (site-root-relative path, since
posts live at varying directory depths):

```md
[2019](https://youtu.be/y5Z5a6QdA-M) ([archived](/archive/videos/y5Z5a6QdA-M.mp4))
```

For HTML `<iframe>` embeds, add a plain sentence/link below the embed instead.

Leave the original external link in place — the archived copy is a backup,
not a replacement, so the live/canonical source is still the first click.

Do not modify `index.md` when archiving media. Its appearances are indexed in
`archive/manifest.json` instead.

## 6. Document gaps

Anything that couldn't be auto-resolved goes in `archive/README.md` under
"Known gaps," with enough detail (URL, what went wrong, suspected fix) that a
future session can pick it up without re-doing the investigation.

## 7. Commit

Commit the new `archive/videos/*.mp4` and `archive/podcasts/*.mp3` (LFS
pointers), the trimmed `.info.json` files, the updated `manifest.json`, and
the content changes together, with a descriptive message. Double-check
`git lfs status` shows the binaries as LFS objects before pushing, and expect
the push itself to take a while / use LFS bandwidth quota.
