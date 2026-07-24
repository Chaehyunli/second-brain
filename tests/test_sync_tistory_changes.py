from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_tistory_changes as sync


class SyncTistoryChangesTests(unittest.TestCase):
    def test_rebuilds_changed_note_with_new_title_and_preserves_related_links(self):
        original = """---
title: \"이전 제목\"
created: 2026-01-01
updated: 2026-01-01
type: blog-post
tags: [\"blog\"]
category: \"OLD\"
published: 2026-01-01
source_url: https://ch010104.tistory.com/1
---

# 이전 제목

## 구현 절차·검증·주의점

이전 본문

## 관련 글

- [[blog/OLD/index|OLD]]
"""
        result = sync.render_changed_note(
            original,
            title="새 제목",
            category="NEW",
            tags=["blog", "technical-writing"],
            published="2026-01-01",
            blocks=[("heading", "새 섹션"), ("text", "새 본문에서 <h2>는 예시 태그입니다.")],
        )
        self.assertIn('title: "새 제목"', result)
        self.assertIn('category: "NEW"', result)
        self.assertIn("# 새 제목", result)
        self.assertIn("### 새 섹션", result)
        self.assertIn("`<h2>`", result)
        self.assertIn("[[blog/OLD/index|OLD]]", result)
        self.assertNotIn("이전 본문", result)
    def test_treats_missing_manifest_entry_for_an_existing_note_as_baseline_only(self):
        changed, new, baseline = sync.plan_updates(
            previous={},
            observed={"https://ch010104.tistory.com/1": "a" * 64},
            local={"https://ch010104.tistory.com/1": Path("blog/OLD/existing.md")},
        )
        self.assertEqual((changed, new, baseline), ([], [], ["https://ch010104.tistory.com/1"]))


if __name__ == "__main__":
    unittest.main()
