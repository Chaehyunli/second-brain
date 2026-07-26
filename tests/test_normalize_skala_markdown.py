from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from normalize_skala_markdown import normalize_markdown


class NormalizeSkalaMarkdownTests(unittest.TestCase):
    def test_converts_notion_xml_table_to_github_markdown_table(self):
        source = """<table header-row=\"true\">\n<tr>\n<td>구분</td>\n<td>예시</td>\n</tr>\n<tr>\n<td>**유선**</td>\n<td>광케이블 | LAN</td>\n</tr>\n</table>\n"""
        result = normalize_markdown(source)
        self.assertEqual(result, "| 구분 | 예시 |\n| --- | --- |\n| **유선** | 광케이블 \\| LAN |\n")

    def test_removes_stray_language_marker_before_matching_fence(self):
        self.assertEqual(normalize_markdown("html\n```html\n<div>예시</div>\n```\n"), "```html\n<div>예시</div>\n```\n")

    def test_wraps_unfenced_html_example_in_html_fence(self):
        source = "설명\n<div class=\"card\">\n  <p>내용</p>\n</div>\n다음 설명\n"
        self.assertIn("```html\n<div class=\"card\">\n  <p>내용</p>\n</div>\n```", normalize_markdown(source))

    def test_preserves_html_already_inside_code_fence(self):
        source = "```html\n<table>\n<tr><td>x</td></tr>\n</table>\n```\n"
        self.assertEqual(normalize_markdown(source), source)


if __name__ == "__main__":
    unittest.main()
