# Media archive

This directory holds local, permanent copies of videos and podcast episodes that
are referenced (via external links) from `index.md` and `_posts/`. The goal is
to survive link rot / platform shutdowns for talks and podcast appearances that
matter for the historical record.

- `videos/` — conference talks and other YouTube videos, as `<youtube-id>.mp4`
  (720p, h264/aac) plus a small `<youtube-id>.info.json` with title/description/
  upload date/duration metadata.
- `podcasts/` — podcast episode audio, as `<slug>.mp3`.
- `manifest.json` — the authoritative index of everything archived (or attempted),
  including original source URL, archived file path, and status.

Files in `videos/*.mp4` and `podcasts/*.mp3` are tracked with **Git LFS** (see
`.gitattributes`). Run `git lfs install` once per clone before working with them.

In the source Markdown, each archived item has an `([archived](...))` link
immediately after its original external link, e.g.:

```md
[2019](https://youtu.be/y5Z5a6QdA-M) ([archived](/archive/videos/y5Z5a6QdA-M.mp4))
```

## Known gaps (as of 2026-10-05)

These three podcast appearances referenced in `index.md` could **not** be
automatically archived and need manual follow-up:

1. **Code and the Coding Coders who Code it — Episode 53** (`podcast.drbragg.dev`):
   the episode page's embedded player points to the wrong Buzzsprout episode
   ("Episode 8 - RailsConf Home Edition Podcast Panel"), which looks like a bug
   on the show's site. Need to contact the host or find the correct enclosure
   URL from the show's RSS feed.
2. **The Ruby Blend** (`radiopublic.com`): RadioPublic has shut down and the
   domain no longer resolves. Need to find this episode via the show's
   current RSS feed/host or the Wayback Machine.
3. **Ruby Rogues — RR 461** (`devchat.tv`): the site did not respond (DNS/connect
   timeout) when attempted. Retry later, or locate the episode via the
   Top End Devs / devchat.tv RSS feed.

See `manifest.json` for the full machine-readable status of every item.

For the general process to repeat this archiving exercise in the future
(e.g. after writing new posts with new talk/podcast links), see
`../ARCHIVING.md` at the repo root.
