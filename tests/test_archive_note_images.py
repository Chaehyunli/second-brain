import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from archive_tistory_images import archive_note
from archive_note_images import (
    ImageCandidate,
    append_image_section,
    archive_image_bytes,
    eligible_note,
    extract_tistory_candidates,
    select_candidates,
)


class ArchiveNoteImagesTest(unittest.TestCase):
    def test_eligibility_excludes_skala_and_studying_only(self):
        self.assertFalse(eligible_note(Path("notion/SKALA/day/note.md")))
        self.assertFalse(eligible_note(Path("blog/STUDYING/[STUDYING] transformer.md")))
        self.assertFalse(eligible_note(Path("blog/STUDYING/STUDYING- transformer.md")))
        self.assertTrue(eligible_note(Path("notion/Information/hot-issue.md")))
        self.assertTrue(eligible_note(Path("blog/DOCKER/docker-network.md")))

    def test_extract_tistory_candidates_keeps_article_images_with_nearest_heading(self):
        source = '''before<div class="tt_article_useless_p_margin"><h2>배포 흐름</h2><img src="https://cdn.example/flow.png" width="1280" height="720"><img src="https://cdn.example/hidden.png" width="0" height="0"></div><div class="container_postbtn">after</div>'''
        candidates = extract_tistory_candidates(source)
        self.assertEqual(len(candidates), 2)
        self.assertEqual(candidates[0], ImageCandidate("https://cdn.example/flow.png", 1280, 720, "배포 흐름", 0))

    def test_selection_keeps_unique_visible_raster_candidates_up_to_cap(self):
        candidates = [
            ImageCandidate("https://example.test/a.png", 0, 0, "hidden", 0),
            ImageCandidate("https://example.test/a.png", 1200, 500, "architecture", 1),
            ImageCandidate("https://example.test/a.png", 1200, 500, "duplicate", 2),
            ImageCandidate("https://example.test/tiny.png", 150, 80, "tiny icon", 3),
            ImageCandidate("https://example.test/b.svg", 1000, 600, "svg", 4),
            ImageCandidate("https://example.test/c.webp", 1000, 600, "flow", 4),
            ImageCandidate("https://example.test/d.jpg", 900, 600, "extra", 5),
        ]
        chosen = select_candidates(candidates, cap=2)
        self.assertEqual([item.url for item in chosen], [
            "https://example.test/a.png",
            "https://example.test/c.webp",
        ])

    def test_archive_image_bytes_writes_bounded_webp(self):
        source = BytesIO()
        Image.new("RGB", (2400, 1200), "white").save(source, format="PNG")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "diagram.webp"
            digest, width, height = archive_image_bytes(source.getvalue(), output)
            with Image.open(output) as saved:
                self.assertEqual(saved.format, "WEBP")
                self.assertEqual(saved.size, (1600, 800))
        self.assertEqual(len(digest), 64)
        self.assertEqual((width, height), (1600, 800))

    def test_archive_note_skips_previously_archived_note_without_fetching_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            note = Path(tmp) / "note.md"
            note.write_text("---\nsource_url: https://example.test\n---\n\n## 핵심 이미지\n\n![x](assets/x.webp)\n", encoding="utf-8")
            self.assertEqual(archive_note(note, "http://127.0.0.1:1/not-available"), (0, []))

    def test_append_image_section_preserves_frontmatter_and_is_idempotent(self):
        original = "---\ntitle: Keep exactly\nsource_url: https://example.test/post\n---\n\n# Body\n\nText.\n\n## 관련 글\n\n- [[hub]]\n"
        with tempfile.TemporaryDirectory() as tmp:
            note = Path(tmp) / "note.md"
            note.write_text(original, encoding="utf-8")
            entries = [("assets/post/01-flow.webp", "처리 흐름")]
            append_image_section(note, entries)
            once = note.read_text(encoding="utf-8")
            append_image_section(note, entries)
            twice = note.read_text(encoding="utf-8")

        self.assertTrue(once.startswith("---\ntitle: Keep exactly\nsource_url: https://example.test/post\n---\n"))
        self.assertIn("## 핵심 이미지\n\n![처리 흐름](assets/post/01-flow.webp)\n\n## 관련 글", once)
        self.assertEqual(once, twice)

    def test_append_image_section_without_related_section_has_single_final_newline(self):
        with tempfile.TemporaryDirectory() as tmp:
            note = Path(tmp) / "note.md"
            note.write_text("# Body\n", encoding="utf-8")
            append_image_section(note, [("assets/a.webp", "A")])
            result = note.read_text(encoding="utf-8")
        self.assertTrue(result.endswith("![A](assets/a.webp)\n"))
        self.assertFalse(result.endswith("![A](assets/a.webp)\n\n"))


if __name__ == "__main__":
    unittest.main()
