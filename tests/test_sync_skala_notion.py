import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from sync_skala_notion import (  # noqa: E402
    is_scope_excluded,
    remove_temporary_signed_url_lines,
    safe_component,
    safe_error_reason,
)


class SyncSkalaNotionPureHelperTests(unittest.TestCase):
    def test_safe_component_removes_brackets_and_windows_unsafe_characters(self):
        self.assertEqual(safe_component("[7/20] 데이터: 분석?"), "7-20 데이터- 분석-")

    def test_scope_exclusion_applies_exact_administrative_and_editing_rules(self):
        self.assertTrue(is_scope_excluded("[7/14] OT", in_padlet=False))
        self.assertTrue(is_scope_excluded("수료증 안내", in_padlet=False))
        self.assertTrue(is_scope_excluded("학습 내용 (수정중)", in_padlet=True))
        self.assertFalse(is_scope_excluded("실습 자료", in_padlet=True))

    def test_scope_exclusion_rejects_non_instructional_root_announcements(self):
        self.assertTrue(is_scope_excluded("종합 실습 .env(절대 동기화 금지)", in_padlet=False))
        self.assertTrue(is_scope_excluded("[8/25] 취업 캠프", in_padlet=False))
        self.assertTrue(is_scope_excluded("2026 금융 AI Challenge | 2026-07-13 ~ 2026-09-07 10:00 KST", in_padlet=False))

    def test_safe_error_reason_does_not_echo_untrusted_command_output(self):
        self.assertEqual(safe_error_reason(RuntimeError("ntn exit 1: secret markdown body")), "Notion API 호출 실패")

    def test_removes_only_lines_containing_temporary_signed_urls(self):
        source = "보존\n![img](https://s3.example/x?X-Amz-Signature=abc)\n계속\n[안정](https://example.com/a)\n"
        self.assertEqual(
            remove_temporary_signed_url_lines(source),
            "보존\n계속\n[안정](https://example.com/a)\n",
        )


if __name__ == "__main__":
    unittest.main()
