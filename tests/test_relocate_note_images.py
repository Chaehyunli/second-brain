import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from relocate_note_images import contexts_from_manifest, relocate_images


class RelocateNoteImagesTest(unittest.TestCase):
    def test_moves_images_to_their_exact_heading_and_removes_collector_section(self):
        source = """# Docker

### 📥 1. 다운로드

설명입니다.

### 🔍 2. 확인

설명입니다.

## 핵심 이미지

![다운로드](assets/a.webp)

![다운로드](assets/b.webp)

![확인](assets/c.webp)

## 관련 글

- [[hub]]
"""
        contexts = {
            "assets/a.webp": "📥 1. 다운로드",
            "assets/b.webp": "📥 1. 다운로드",
            "assets/c.webp": "🔍 2. 확인",
        }
        result = relocate_images(source, contexts)
        self.assertNotIn("## 핵심 이미지", result.content)
        self.assertIn("### 📥 1. 다운로드\n\n![다운로드](assets/a.webp)\n\n![다운로드](assets/b.webp)\n\n설명입니다.", result.content)
        self.assertIn("### 🔍 2. 확인\n\n![확인](assets/c.webp)\n\n설명입니다.", result.content)
        self.assertEqual(result.placed, 3)
        self.assertEqual(result.unmatched, 0)

    def test_keeps_unmatched_image_in_collector_section(self):
        source = """# Note

### Present

Text.

## 핵심 이미지

![Present](assets/p.webp)

![Missing](assets/m.webp)

## 관련 글

- [[hub]]
"""
        result = relocate_images(source, {
            "assets/p.webp": "Present",
            "assets/m.webp": "Missing",
        })
        self.assertIn("### Present\n\n![Present](assets/p.webp)\n\nText.", result.content)
        self.assertIn("## 핵심 이미지\n\n![Missing](assets/m.webp)\n\n## 관련 글", result.content)
        self.assertEqual(result.placed, 1)
        self.assertEqual(result.unmatched, 1)

    def test_places_generic_source_image_at_first_semantic_section(self):
        source = """# Note

## 원문

Link.

## 노트 유형

`guide`

## 핵심 개념

Text.

## 핵심 이미지

![원문 이미지 1](assets/a.webp)
"""
        result = relocate_images(source, {"assets/a.webp": "원문 이미지 1"})
        self.assertIn("## 핵심 개념\n\n![원문 이미지 1](assets/a.webp)\n\nText.", result.content)
        self.assertTrue(result.content.endswith("Text.\n"))
        self.assertFalse(result.content.endswith("Text.\n\n"))
        self.assertEqual((result.placed, result.unmatched), (1, 0))

    def test_reads_explicit_placement_context_for_single_asset_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            note = Path(tmp) / "note.md"
            asset_dir = Path(tmp) / "assets" / "note"
            asset_dir.mkdir(parents=True)
            (asset_dir / "01.webp").write_bytes(b"image")
            (asset_dir / "SOURCE.txt").write_text("placement_context: 원문·출처\n", encoding="utf-8")
            self.assertEqual(contexts_from_manifest(note), {"assets/note/01.webp": "원문·출처"})

    def test_returns_unchanged_when_no_collector_section(self):
        source = "# Note\n\nText.\n"
        result = relocate_images(source, {"assets/a.webp": "Note"})
        self.assertEqual(result.content, source)
        self.assertEqual(result.placed, 0)


if __name__ == "__main__":
    unittest.main()
