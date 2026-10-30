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

In posts, archived items have an `([archived](...))` link immediately after
their original external link, e.g.:

```md
[2019](https://youtu.be/y5Z5a6QdA-M) ([archived](/archive/videos/y5Z5a6QdA-M.mp4))
```

`index.md` intentionally keeps its original links without archive links. Use
`manifest.json` to find archived copies of appearances listed there.

## Recovered podcast appearances

- **Code and the Coding Coders who Code it — Episode 53 - Joel Hawksley**
  ([archived audio](podcasts/drbragg-episode-53.mp3)): recovered from the
  [Buzzsprout RSS feed](https://feeds.buzzsprout.com/1927628.rss), published
  July 2, 2025. The page's player selects the correct episode; only its Twitter
  player metadata points to Episode 8. After initial HTTP 403 responses, a
  browser-style request succeeded:

  ```bash
  curl --fail --location \
    --referer 'https://www.buzzsprout.com/' --user-agent 'Mozilla/5.0' \
    'https://www.buzzsprout.com/1927628/episodes/17437317-episode-53-joel-hawksley.mp3?client_source=small_player' \
    -o archive/podcasts/drbragg-episode-53.mp3
  ```

- **The Ruby Blend — Episode 9: ViewComponent at GitHub with Joel Hawksley**
  ([archived audio](podcasts/radiopublic-ruby-blend.mp3)): recovered from the
  [Transistor RSS archive](https://feeds.transistor.fm/the-ruby-blend), published
  April 16, 2020.
- **Ruby Rogues — RR 461: Rethinking the View Layer with Components with Joel Hawksley**
  ([archived audio](podcasts/devchat-ruby-rogues-461.mp3)): recovered from the
  [Spreaker RSS feed](https://www.spreaker.com/show/6102073/episodes/feed), published
  June 9, 2020.

All three downloads were matched against their RSS episode titles and audio title tags.
The manifest records the feed and enclosure URLs so the recovery is repeatable.

The Ruby Rogues source contains a malformed MP3 packet, but decoding continues
through the end (50:16). The RSS enclosure, direct host URL, and official API
download all returned identical bytes; the archive preserves those bytes rather
than editing the recording.

## Known gaps (as of 2026-10-30)

None of the three previously missing podcast recordings remain unarchived.
The Ruby Rogues source-quality issue is documented above.

See `manifest.json` for the full machine-readable status of every item.

For the general process to repeat this archiving exercise in the future
(e.g. after writing new posts with new talk/podcast links), see
`../ARCHIVING.md` at the repo root.
