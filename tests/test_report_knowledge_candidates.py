from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from report_knowledge_candidates import build_candidates


class KnowledgeCandidateTests(unittest.TestCase):
    def make_vault(self, files: dict[str, str]) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return root

    def test_explicit_shared_tag_across_source_domains_creates_review_candidate(self):
        root = self.make_vault({
            "blog/vue.md": "---\ntitle: Vue\ntags: [vue, frontend]\nsource_url: https://blog.example/vue\n---\n# Vue\n",
            "notion/SKALA/day4.md": "---\ntitle: Day4\ntags: [vue, frontend]\nnotion_page_id: page-4\nsource_url: https://notion.example/day4\n---\n# Day4\n",
        })
        candidates = build_candidates(root)
        candidate = next(item for item in candidates if item["tag"] == "vue")
        self.assertEqual(candidate["review_required"], True)
        self.assertEqual(set(candidate["domains"]), {"blog", "notion/SKALA"})

    def test_same_tag_in_one_domain_does_not_create_candidate(self):
        root = self.make_vault({
            "blog/a.md": "---\ntags: [vue]\nsource_url: https://a.example\n---\n",
            "blog/b.md": "---\ntags: [vue]\nsource_url: https://b.example\n---\n",
        })
        self.assertEqual(build_candidates(root), [])

    def test_missing_provenance_is_reported_but_not_used_as_evidence(self):
        root = self.make_vault({
            "blog/a.md": "---\ntags: [vue]\n---\n",
            "notion/SKALA/b.md": "---\ntags: [vue]\nsource_url: https://b.example\n---\n",
        })
        candidates = build_candidates(root)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["evidence_paths"], ["notion/SKALA/b.md"])
        self.assertEqual(candidates[0]["missing_provenance_paths"], ["blog/a.md"])
    def test_multiline_sources_are_recognized_as_provenance(self):
        root = self.make_vault({
            "blog/a.md": "---\ntags: [vue]\nsource_url: https://a.example\n---\n",
            "entities/b.md": "---\ntags: [vue]\nsources:\n  - raw/proof.md\n---\n",
        })
        candidate = next(item for item in build_candidates(root) if item["tag"] == "vue")
        self.assertEqual(candidate["missing_provenance_paths"], [])
    def test_existing_knowledge_tag_suppresses_repeated_candidate(self):
        root = self.make_vault({
            "blog/a.md": "---\ntags: [vue]\nsource_url: https://a.example\n---\n",
            "notion/SKALA/b.md": "---\ntags: [vue]\nsource_url: https://b.example\n---\n",
            "knowledge/vue.md": "---\ntype: knowledge-note\ntags: [vue]\nsources: [blog/a.md, notion/SKALA/b.md]\n---\n",
        })
        self.assertEqual(build_candidates(root), [])


if __name__ == "__main__":
    unittest.main()
