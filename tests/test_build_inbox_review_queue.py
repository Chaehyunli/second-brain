from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_inbox_review_queue import build_queue


class InboxReviewQueueTests(unittest.TestCase):
    def make_vault(self, files: dict[str, str]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def test_pending_note_with_source_is_ready_for_review(self):
        root = self.make_vault({
            "inbox/item.md": "---\ntitle: Item\ntype: research-note\ncaptured_at: 2026-08-01\nreview_status: pending\nagent_generated: true\nsource_url: https://example.com\n---\n",
        })
        queue = build_queue(root)
        self.assertEqual(queue["ready_for_review"], ["inbox/item.md"])
        self.assertEqual(queue["needs_source"], [])

    def test_pending_note_without_source_is_needs_source(self):
        root = self.make_vault({
            "inbox/item.md": "---\ntitle: Item\ncaptured_at: 2026-08-01\nreview_status: pending\nagent_generated: true\n---\n",
        })
        queue = build_queue(root)
        self.assertEqual(queue["needs_source"], ["inbox/item.md"])

    def test_reviewed_note_is_not_pending(self):
        root = self.make_vault({
            "inbox/item.md": "---\ntitle: Item\ncaptured_at: 2026-08-01\nreview_status: verified\nagent_generated: true\nsource_url: https://example.com\n---\n",
        })
        self.assertEqual(build_queue(root)["ready_for_review"], [])


if __name__ == "__main__":
    unittest.main()
