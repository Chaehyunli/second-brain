from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_new_tistory_posts as sync


class TistoryCategoryIndexTests(unittest.TestCase):
    def test_empty_category_index_has_no_extra_blank_line_at_eof(self):
        original_blog = sync.BLOG
        try:
            with tempfile.TemporaryDirectory() as tmp:
                sync.BLOG = Path(tmp) / "blog"
                (sync.BLOG / "빈 카테고리").mkdir(parents=True)
                sync.rebuild_category_index("빈 카테고리")
                text = (sync.BLOG / "빈 카테고리" / "index.md").read_text(encoding="utf-8")
                self.assertTrue(text.endswith("## 글\n"))
                self.assertFalse(text.endswith("## 글\n\n"))
        finally:
            sync.BLOG = original_blog


if __name__ == "__main__":
    unittest.main()
