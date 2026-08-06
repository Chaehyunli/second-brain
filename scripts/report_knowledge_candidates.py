#!/usr/bin/env python3
"""Report evidence-backed, cross-domain candidates for curated knowledge notes."""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

SOURCE_ROOTS = ("blog", "notion/SKALA", "notion/Information", "entities")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    values: dict[str, Any] = {}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if ":" not in line or line.startswith((" ", "\t", "-")):
            index += 1
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if not value:
            items: list[str] = []
            lookahead = index + 1
            while lookahead < len(lines) and lines[lookahead].startswith((" ", "\t")):
                candidate = lines[lookahead].strip()
                if candidate.startswith("- "):
                    items.append(candidate[2:].strip().strip('"').strip("'"))
                lookahead += 1
            values[key] = items
            index = lookahead
            continue
        if value.startswith("[") and value.endswith("]"):
            values[key] = [item.strip().strip('"').strip("'") for item in value[1:-1].split(",") if item.strip()]
        else:
            values[key] = value
        index += 1
    return values


def source_domain(path: Path, root: Path) -> str | None:
    relative = path.relative_to(root).as_posix()
    for source_root in SOURCE_ROOTS:
        if relative == source_root or relative.startswith(source_root + "/"):
            return source_root
    return None


def build_candidates(root: Path) -> list[dict[str, Any]]:
    tag_notes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    covered_tags: set[str] = set()
    knowledge_root = root / "knowledge"
    if knowledge_root.exists():
        for path in knowledge_root.rglob("*.md"):
            metadata = parse_frontmatter(path.read_text(encoding="utf-8"))
            if metadata.get("type") == "knowledge-note":
                covered_tags.update(str(tag).strip() for tag in metadata.get("tags", []) if str(tag).strip())
    for path in sorted(root.rglob("*.md")):
        domain = source_domain(path, root)
        if domain is None:
            continue
        metadata = parse_frontmatter(path.read_text(encoding="utf-8"))
        tags = metadata.get("tags", [])
        if not isinstance(tags, list):
            continue
        provenance = metadata.get("source_url") or metadata.get("sources") or metadata.get("notion_page_id")
        record = {
            "path": path.relative_to(root).as_posix(),
            "domain": domain,
            "has_provenance": bool(provenance),
        }
        for tag in sorted({str(tag).strip() for tag in tags if str(tag).strip()}):
            tag_notes[tag].append(record)

    candidates: list[dict[str, Any]] = []
    for tag, notes in sorted(tag_notes.items()):
        if tag in covered_tags:
            continue
        domains = sorted({note["domain"] for note in notes})
        if len(domains) < 2:
            continue
        evidence = sorted(note["path"] for note in notes if note["has_provenance"])
        missing = sorted(note["path"] for note in notes if not note["has_provenance"])
        if not evidence:
            continue
        candidates.append({
            "tag": tag,
            "domains": domains,
            "evidence_paths": evidence,
            "missing_provenance_paths": missing,
            "review_required": True,
        })
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, help="write JSON report to this path")
    args = parser.parse_args()
    candidates = build_candidates(args.root.resolve())
    payload = {"candidate_count": len(candidates), "candidates": candidates}
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
