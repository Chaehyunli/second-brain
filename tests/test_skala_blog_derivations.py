import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from link_skala_blog_derivations import extract_notion_page_id, find_skala_note, link_blog_from_source, link_pair


class SkalaBlogDerivationTests(unittest.TestCase):
    def test_extracts_notion_page_id_from_public_learning_source_link(self):
        html = '''<p>학습 원본: <a href="https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5">SKALA</a></p>'''

        self.assertEqual(
            extract_notion_page_id(html),
            "3a41d84b-f68e-8163-bfa0-d4f8af36e3d5",
        )

    def test_ignores_an_unlabeled_notion_link_to_avoid_false_derivations(self):
        html = '''<p>추가 참고: <a href="https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5">다른 노트</a></p>'''

        self.assertIsNone(extract_notion_page_id(html))

    def test_finder_ignores_local_only_identity_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.md").write_text("---\nnotion_page_id: local-skala-index\n---\n", encoding="utf-8")
            target = root / "note.md"
            target.write_text("---\nnotion_page_id: 3a41d84b-f68e-8163-bfa0-d4f8af36e3d5\n---\n", encoding="utf-8")

            self.assertEqual(find_skala_note(root, "3a41d84b-f68e-8163-bfa0-d4f8af36e3d5"), target)

    def test_links_only_when_source_contains_explicit_marker_and_matching_skala_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            blog = root / "blog" / "STUDYING" / "post.md"
            skala = root / "notion" / "SKALA" / "day" / "note.md"
            blog.parent.mkdir(parents=True)
            skala.parent.mkdir(parents=True)
            blog.write_text("# Blog\n", encoding="utf-8")
            skala.write_text("---\nnotion_page_id: 3a41d84b-f68e-8163-bfa0-d4f8af36e3d5\n---\n# SKALA\n", encoding="utf-8")

            result = link_blog_from_source(
                blog,
                '<p>학습 원본: https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5</p>',
                root,
            )

            self.assertTrue(result)
            self.assertIn("[[notion/SKALA/day/note|SKALA 상세 학습 노트]]", blog.read_text(encoding="utf-8"))

    def test_link_pair_appends_one_visible_wikilink_to_each_note_idempotently(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            blog = root / "blog.md"
            skala = root / "skala.md"
            blog.write_text("---\ntitle: blog\n---\n\n# Blog\n", encoding="utf-8")
            skala.write_text("---\nnotion_page_id: id\n---\n\n# SKALA\n", encoding="utf-8")

            link_pair(blog, skala, blog_target="blog/STUDYING/post", skala_target="notion/SKALA/day/note")
            link_pair(blog, skala, blog_target="blog/STUDYING/post", skala_target="notion/SKALA/day/note")

            self.assertEqual(blog.read_text(encoding="utf-8").count("[[notion/SKALA/day/note|SKALA 상세 학습 노트]]"), 1)
            self.assertEqual(skala.read_text(encoding="utf-8").count("[[blog/STUDYING/post|공개 블로그 글]]"), 1)


if __name__ == "__main__":
    unittest.main()
