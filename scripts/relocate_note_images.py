#!/usr/bin/env python3
"""Move archived image embeds from a collector section into matching note headings."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from archive_note_images import eligible_note


IMAGE_RE = re.compile(r"!\[([^]]*)\]\((assets/[^)]+)\)")
COLLECTOR_RE = re.compile(r"^## 핵심 이미지\n\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)


@dataclass(frozen=True)
class RelocationResult:
    content: str
    placed: int
    unmatched: int


def find_heading_for_context(content: str, context: str) -> re.Match[str] | None:
    exact = re.search(rf"(?m)^#+\s+{re.escape(context)}\s*$", content)
    if exact or not re.fullmatch(r"원문 이미지 \d+", context):
        return exact
    metadata = {"원문", "노트 유형", "원문·출처", "연결", "관련 글"}
    for heading in re.finditer(r"(?m)^##\s+(.+?)\s*$", content):
        if heading.group(1).strip() not in metadata:
            return heading
    return None


def relocate_images(content: str, contexts: dict[str, str]) -> RelocationResult:
    """Relocate collector embeds directly below their exact Markdown headings."""
    collector = COLLECTOR_RE.search(content)
    if not collector:
        return RelocationResult(content, 0, 0)

    images = [(alt, path) for alt, path in IMAGE_RE.findall(collector.group("body"))]
    without_collector = content[:collector.start()] + content[collector.end():]
    groups: dict[str, list[tuple[str, str]]] = {}
    unmatched: list[tuple[str, str]] = []
    for alt, path in images:
        context = contexts.get(path)
        if context:
            groups.setdefault(context, []).append((alt, path))
        else:
            unmatched.append((alt, path))

    placements: list[tuple[int, list[tuple[str, str]]]] = []
    for context, entries in groups.items():
        heading = find_heading_for_context(without_collector, context)
        if heading:
            placements.append((heading.end(), entries))
        else:
            unmatched.extend(entries)

    placed = 0
    for offset, entries in sorted(placements, reverse=True):
        embeds = "\n\n".join(f"![{alt}]({path})" for alt, path in entries)
        before = without_collector[:offset].rstrip("\n")
        following = without_collector[offset:]
        without_collector = (
            before
            + "\n\n"
            + embeds
            + "\n\n"
            + following.lstrip("\n")
        )
        placed += len(entries)

    if unmatched:
        collector_text = "## 핵심 이미지\n\n" + "\n\n".join(
            f"![{alt}]({path})" for alt, path in unmatched
        ) + "\n\n"
        related_marker = "## 관련 글\n"
        if related_marker in without_collector:
            without_collector = without_collector.replace(related_marker, collector_text + related_marker, 1)
        else:
            without_collector = without_collector.rstrip() + "\n\n" + collector_text

    return RelocationResult(without_collector.rstrip() + "\n", placed, len(unmatched))


def contexts_from_manifest(note: Path) -> dict[str, str]:
    contexts: dict[str, str] = {}
    for manifest in note.parent.glob("assets/*/SOURCE.txt"):
        text = manifest.read_text(encoding="utf-8")
        for match in re.finditer(r"^- file: (?P<file>.+)\n  context: (?P<context>.+)$", text, re.MULTILINE):
            relative = (manifest.parent.relative_to(note.parent) / match.group("file")).as_posix()
            contexts[relative] = match.group("context")
        placement = re.search(r"^placement_context: (?P<context>.+)$", text, re.MULTILINE)
        if placement:
            for image in manifest.parent.glob("*.webp"):
                relative = image.relative_to(note.parent).as_posix()
                contexts[relative] = placement.group("context")
    return contexts


def relocate_note(note: Path, *, dry_run: bool = False) -> RelocationResult:
    if not eligible_note(note):
        return RelocationResult(note.read_text(encoding="utf-8"), 0, 0)
    result = relocate_images(note.read_text(encoding="utf-8"), contexts_from_manifest(note))
    if result.content != note.read_text(encoding="utf-8") and not dry_run:
        note.write_text(result.content, encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    notes = [p for p in Path("blog").rglob("*.md") if p.name != "index.md"]
    notes.extend(Path("notion/Information").glob("*.md"))
    moved = unmatched = changed = 0
    for note in notes:
        if not eligible_note(note):
            continue
        before = note.read_text(encoding="utf-8")
        result = relocate_note(note, dry_run=args.dry_run)
        if result.content != before:
            changed += 1
        moved += result.placed
        unmatched += result.unmatched
    print(f"notes_changed={changed} images_placed={moved} images_unmatched={unmatched}")


if __name__ == "__main__":
    main()
