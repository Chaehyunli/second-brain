from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_knowledge_health import audit_health


class KnowledgeHealthTests(unittest.TestCase):
    def make_vault(self, files: dict[str, str]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def test_reports_missing_knowledge_link_and_inbox_source_gap(self):
        root = self.make_vault({
            "knowledge/example.md": "# Example\n[[missing-note]]\n",
            "inbox/pending.md": "---\nreview_status: pending\ncaptured_at: 2026-08-01\nagent_generated: true\n---\n",
        })
        report = audit_health(root)
        self.assertIn("knowledge/example.md", report["action_required"]["broken_wikilinks"])
        self.assertEqual(report["warnings"]["inbox_missing_provenance"], ["inbox/pending.md"])

    def test_healthy_knowledge_link_has_no_action_required_items(self):
        root = self.make_vault({
            "knowledge/a.md": "# A\n[[knowledge/b]]\n",
            "knowledge/b.md": "# B\n",
        })
        report = audit_health(root)
        self.assertEqual(report["action_required"]["broken_wikilinks"], [])


if __name__ == "__main__":
    unittest.main()
