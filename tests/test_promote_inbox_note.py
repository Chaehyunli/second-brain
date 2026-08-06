from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from promote_inbox_note import PromotionError, promote_note


class InboxPromotionTests(unittest.TestCase):
    def make_vault(self, files: dict[str, str]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def source_note(self) -> str:
        return "---\ntitle: Candidate\ntype: research-note\ncaptured_at: 2026-08-01\nreview_status: pending\nagent_generated: true\nsource_url: https://example.com\n---\n# Candidate\n"

    def test_refuses_without_explicit_approval(self):
        root = self.make_vault({"inbox/item.md": self.source_note()})
        with self.assertRaises(PromotionError):
            promote_note(root, Path("inbox/item.md"), Path("knowledge/item.md"), False, "reviewed")
        self.assertTrue((root / "inbox/item.md").exists())
        self.assertFalse((root / "knowledge/item.md").exists())

    def test_approved_promotion_preserves_provenance_and_review_history(self):
        root = self.make_vault({"inbox/item.md": self.source_note()})
        destination = promote_note(root, Path("inbox/item.md"), Path("knowledge/item.md"), True, "source and claims reviewed")
        rendered = destination.read_text(encoding="utf-8")
        self.assertIn("source_url: https://example.com", rendered)
        self.assertIn("review_status: approved", rendered)
        self.assertIn("review_note: source and claims reviewed", rendered)
        self.assertFalse((root / "inbox/item.md").exists())


if __name__ == "__main__":
    unittest.main()
