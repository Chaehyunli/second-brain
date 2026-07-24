from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import tistory_content_hashes as hashes


class TistoryContentHashTests(unittest.TestCase):
    def test_same_normalized_title_and_blocks_have_same_hash(self):
        first = hashes.content_hash(
            "글 제목",
            [("heading", "개요"), ("text", "본문입니다.")],
        )
        second = hashes.content_hash(
            " 글 제목 ",
            [("heading", "개요"), ("text", "본문입니다.")],
        )
        self.assertEqual(first, second)

    def test_title_or_body_change_has_a_different_hash(self):
        original = hashes.content_hash("글 제목", [("text", "첫 본문")])
        self.assertNotEqual(original, hashes.content_hash("바뀐 제목", [("text", "첫 본문")]))
        self.assertNotEqual(original, hashes.content_hash("글 제목", [("text", "바뀐 본문")]))

    def test_manifest_round_trip_is_sorted_and_compact(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tistory_content_hashes.json"
            hashes.save_manifest(path, {
                "https://ch010104.tistory.com/2": "b" * 64,
                "https://ch010104.tistory.com/1": "a" * 64,
            })
            self.assertEqual(hashes.load_manifest(path), {
                "https://ch010104.tistory.com/1": "a" * 64,
                "https://ch010104.tistory.com/2": "b" * 64,
            })
            text = path.read_text(encoding="utf-8")
            self.assertLess(text.index('"https://ch010104.tistory.com/1"'), text.index('"https://ch010104.tistory.com/2"'))
            self.assertNotIn("title", text)
            self.assertNotIn("body", text)

    def test_diff_reports_only_new_and_changed_urls(self):
        prior = {
            "https://ch010104.tistory.com/1": "a" * 64,
            "https://ch010104.tistory.com/2": "b" * 64,
        }
        observed = {
            "https://ch010104.tistory.com/1": "a" * 64,
            "https://ch010104.tistory.com/2": "c" * 64,
            "https://ch010104.tistory.com/3": "d" * 64,
        }
        self.assertEqual(
            hashes.changed_urls(prior, observed),
            (["https://ch010104.tistory.com/2"], ["https://ch010104.tistory.com/3"]),
        )


if __name__ == "__main__":
    unittest.main()
