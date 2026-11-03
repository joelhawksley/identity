import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "archive_media", Path(__file__).resolve().parents[1] / "archive_media.py",
)
media = importlib.util.module_from_spec(spec)
spec.loader.exec_module(media)


class ArchiveMediaTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "_posts").mkdir()
        (self.root / "archive").mkdir()
        (self.root / "index.md").write_text("")
        (self.root / "archive/README.md").write_text("# Media archive\n")
        self.manifest = {"generated_at": "2026-01-01", "videos": [], "podcasts": []}
        self.save_manifest()

    def save_manifest(self):
        (self.root / "archive/manifest.json").write_text(json.dumps(self.manifest))

    def load_manifest(self):
        return json.loads((self.root / "archive/manifest.json").read_text())

    def test_youtube_variants_dedupe(self):
        variants = [
            "https://youtu.be/y5Z5a6QdA-M?t=10",
            "http://youtube.com/watch?v=y5Z5a6QdA-M&feature=share",
            "https://www.youtube-nocookie.com/embed/y5Z5a6QdA-M?si=123",
            "https://m.youtube.com/shorts/y5Z5a6QdA-M",
            "https://youtube.com/live/y5Z5a6QdA-M",
        ]
        (self.root / "index.md").write_text("\n".join(variants))
        found = media.discover(self.root, self.manifest)
        self.assertEqual(len(found), 1)
        self.assertEqual(media.item_slug(found[0]), "y5Z5a6QdA-M")

    def test_discovers_podcasts_and_talk_pages_not_unrelated_links(self):
        (self.root / "index.md").write_text(
            "I've spoken at [Talk](https://brightonruby.com/2022/my-talk/) "
            "[Meetup](https://www.meetup.com/group/events/123) "
            "[Conference](https://rubyconf.org/).\n"
            "[Episode](https://new.example/episodes/new-episode)\n"
            "[Interview](https://example.com/pods/interview)\n"
            "[Product](https://amazon.com/product)\n"
        )
        self.assertEqual(
            [item["kind"] for item in media.discover(self.root, self.manifest)],
            ["videos", "podcasts", "podcasts"],
        )

    def test_preserves_meaningful_query_parameters(self):
        self.assertNotEqual(
            media.canonical_url("https://example.com/episode?id=1"),
            media.canonical_url("https://example.com/episode?id=2"),
        )
        self.assertEqual(
            media.canonical_url("http://www.example.com/episode/?utm_source=x&id=1#player"),
            "https://example.com/episode?id=1",
        )

    def test_autolink_titles_and_invalid_youtube_links(self):
        source = "https://example.com/pods/erin-meyer"
        (self.root / "index.md").write_text(
            f"[{source}]({source}).\n"
            "https://youtube.com/watch\nhttps://youtube.com/watch?v=invalid",
        )
        found = media.discover(self.root, self.manifest)
        self.assertEqual([item["source_url"] for item in found], [source])

    def test_checks_episode_title_and_number(self):
        candidate = {
            "kind": "podcasts",
            "source_url": "https://podcast.example/episodes/episode-53-joel-hawksley",
        }
        media.verify_episode(candidate, {"title": "Episode 53 - Joel Hawksley"})
        with self.assertRaises(media.ArchiveError):
            media.verify_episode(candidate, {"title": "Episode 8 - Joel Hawksley"})
        with self.assertRaises(media.ArchiveError):
            media.verify_episode(candidate, {"title": "Episode 53 - Someone Else"})
        with self.assertRaises(media.ArchiveError):
            media.verify_episode(candidate, {"_type": "playlist", "title": "Joel Hawksley"})

    def test_success_updates_manifest_posts_and_leaves_index_unchanged(self):
        index = "[Talk](https://youtu.be/y5Z5a6QdA-M)"
        (self.root / "index.md").write_text(index)
        post = self.root / "_posts/talk.md"
        post.write_text(index)

        def download(candidate, root, slug, remaining):
            file = f"archive/videos/{slug}.mp4"
            (root / file).parent.mkdir(exist_ok=True)
            (root / file).write_bytes(b"media")
            return file, 5, "A talk"

        with patch.object(media, "download", side_effect=download) as mocked:
            media.archive(self.root)
            first = (self.root / "archive/manifest.json").read_bytes()
            media.archive(self.root)
        self.assertEqual(mocked.call_count, 1)
        self.assertEqual((self.root / "archive/manifest.json").read_bytes(), first)
        self.assertEqual((self.root / "index.md").read_text(), index)
        self.assertEqual(post.read_text().count("[archived]"), 1)
        self.assertEqual(self.load_manifest()["videos"][0]["status"], "archived")

    def test_iframe_gets_one_backup_link(self):
        post = self.root / "_posts/talk.md"
        post.write_text('<iframe src="https://youtube.com/embed/y5Z5a6QdA-M"></iframe>')
        archived = {
            "https://www.youtube.com/watch?v=y5Z5a6QdA-M": "archive/videos/y5Z5a6QdA-M.mp4",
        }
        media.add_post_links(self.root, archived)
        media.add_post_links(self.root, archived)
        self.assertEqual(post.read_text().count("[Archived recording]"), 1)

    def test_failure_is_recorded_and_retried_without_duplicate_entries(self):
        (self.root / "index.md").write_text("https://youtu.be/y5Z5a6QdA-M")
        with patch.object(media, "download", side_effect=media.ArchiveError("HTTP 403")):
            media.archive(self.root)
            media.archive(self.root)
        entries = self.load_manifest()["videos"]
        self.assertEqual(len(entries), 1)
        self.assertIsNone(entries[0]["file"])
        self.assertEqual(entries[0]["notes"], "HTTP 403")
        self.assertIn("needs-manual-check", (self.root / "archive/README.md").read_text())

    def test_budget_defers_remaining_media(self):
        (self.root / "index.md").write_text(
            "https://youtu.be/y5Z5a6QdA-M\nhttps://youtu.be/YVYRus_2KZM",
        )
        with patch.object(media, "download", return_value=("archive/videos/first.mp4", media.MAX_BYTES, "Talk")) as mocked:
            media.archive(self.root)
        self.assertEqual(mocked.call_count, 1)
        self.assertEqual(self.load_manifest()["videos"][1]["status"], "deferred")

    def test_download_rejects_oversized_file(self):
        candidate = {"source_url": "https://youtu.be/y5Z5a6QdA-M", "kind": "videos"}

        def command(args, timeout):
            if "--dump-single-json" in args:
                return '{"title": "Talk"}'
            template = args[args.index("--output") + 1]
            Path(template.replace("%(ext)s", "mp4")).write_bytes(b"123456")
            return ""

        with patch.object(media, "run_command", side_effect=command):
            with self.assertRaisesRegex(media.ArchiveError, "budget"):
                media.download(candidate, self.root, "y5Z5a6QdA-M", 5)
        self.assertFalse((self.root / "archive/videos/y5Z5a6QdA-M.mp4").exists())

    def test_download_persists_only_valid_media_and_trimmed_metadata(self):
        candidate = {"source_url": "https://youtu.be/y5Z5a6QdA-M", "kind": "videos"}

        def command(args, timeout):
            if "--dump-single-json" in args:
                return '{"title": "Talk", "formats": ["large data"], "duration": 42}'
            if args[0] == "ffprobe":
                return '{"streams": [{"codec_type": "video"}, {"codec_type": "audio"}]}'
            template = args[args.index("--output") + 1]
            Path(template.replace("%(ext)s", "mp4")).write_bytes(b"12345")
            return ""

        with patch.object(media, "run_command", side_effect=command):
            file, size, title = media.download(candidate, self.root, "y5Z5a6QdA-M", 5)
        self.assertEqual(size, 5)
        self.assertEqual(title, "Talk")
        self.assertEqual((self.root / file).read_bytes(), b"12345")
        metadata = json.loads((self.root / file).with_suffix(".info.json").read_text())
        self.assertEqual(set(metadata), set(media.METADATA_FIELDS))
        self.assertEqual(metadata["duration"], 42)

    def test_download_rejects_wrong_stream_type(self):
        candidate = {"source_url": "https://youtu.be/y5Z5a6QdA-M", "kind": "videos"}

        def command(args, timeout):
            if "--dump-single-json" in args:
                return '{"title": "Talk"}'
            if args[0] == "ffprobe":
                return '{"streams": [{"codec_type": "audio"}]}'
            template = args[args.index("--output") + 1]
            Path(template.replace("%(ext)s", "mp4")).write_bytes(b"12345")
            return ""

        with patch.object(media, "run_command", side_effect=command):
            with self.assertRaisesRegex(media.ArchiveError, "no video stream"):
                media.download(candidate, self.root, "y5Z5a6QdA-M", 5)
        self.assertFalse((self.root / "archive/videos/y5Z5a6QdA-M.mp4").exists())

    def test_missing_indexed_file_fails(self):
        self.manifest["videos"].append({
            "source_url": "https://youtu.be/y5Z5a6QdA-M",
            "file": "archive/videos/missing.mp4",
        })
        self.save_manifest()
        (self.root / "index.md").write_text("https://youtu.be/y5Z5a6QdA-M")
        with self.assertRaisesRegex(media.ArchiveError, "missing file"):
            media.archive(self.root)

    def test_dry_run_does_not_download_or_write(self):
        (self.root / "index.md").write_text("https://youtu.be/y5Z5a6QdA-M")
        before = (self.root / "archive/manifest.json").read_bytes()
        with patch.object(media, "download") as mocked:
            media.archive(self.root, dry_run=True)
        mocked.assert_not_called()
        self.assertEqual((self.root / "archive/manifest.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
