from pathlib import Path
import sys
import subprocess
import tempfile
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_vault_contract import audit_markdown, context_files_match, staged_markdown_paths


class VaultContractTests(unittest.TestCase):
    def make_vault(self, files: dict[str, str]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def test_audit_resolves_existing_wikilink(self):
        root = self.make_vault({
            "index.md": "# Index\n",
            "notes/a.md": "[[index]]\n",
        })
        self.assertEqual(audit_markdown(root, [root / "notes/a.md"]), [])

    def test_audit_rejects_missing_and_numeric_wikilinks(self):
        root = self.make_vault({
            "notes/a.md": "[[missing-note]]\n[[100]]\n",
        })
        issues = audit_markdown(root, [root / "notes/a.md"])
        self.assertEqual({issue.kind for issue in issues}, {"missing_wikilink", "numeric_wikilink"})

    def test_audit_ignores_code_fence_examples(self):
        root = self.make_vault({
            "notes/a.md": "```text\n[[100]]\n[[not-a-real-note]]\n```\n",
        })
        self.assertEqual(audit_markdown(root, [root / "notes/a.md"]), [])

    def test_audit_ignores_single_bracket_source_titles_and_escaped_arrays(self):
        root = self.make_vault({
            "notes/a.md": "원본: [[7/21] 실습](https://example.com)\n\\\\[[[10, 20, 30]\\\\]]\n",
        })
        self.assertEqual(audit_markdown(root, [root / "notes/a.md"]), [])

    def test_context_files_must_be_exact_copies(self):
        root = self.make_vault({
            "AGENTS.md": "rules\n",
            "CLAUDE.md": "rules\n",
            "agent.md": "different\n",
        })
        self.assertFalse(context_files_match(root))

    def test_staged_paths_keep_unicode_filenames(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            note = root / "notes" / "한글 노트.md"
            note.parent.mkdir()
            note.write_text("# note\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            self.assertEqual(staged_markdown_paths(root), [note])

    def test_vault_lock_refuses_a_second_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            lock = root / ".git" / "hermes-vault-sync.lock"
            holder = subprocess.Popen(["flock", str(lock), "sleep", "2"])
            self.addCleanup(holder.wait)
            time.sleep(0.1)
            script = Path(__file__).resolve().parents[1] / "scripts" / "vault_sync_lock.sh"
            result = subprocess.run([str(script), "true"], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 75)


if __name__ == "__main__":
    unittest.main()
