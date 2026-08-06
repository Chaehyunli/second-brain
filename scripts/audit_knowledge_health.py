#!/usr/bin/env python3
"""Read-only health audit for curated knowledge and Inbox provenance."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from report_knowledge_candidates import parse_frontmatter

LINK_RE = re.compile(r"(?<!\!)\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def existing_note(root: Path, target: str) -> bool:
    target = target.strip()
    if not target:
        return True
    direct = root / (target if target.endswith(".md") else target + ".md")
    if direct.is_file():
        return True
    return any(path.stem == target for path in root.rglob("*.md"))


def links_outside_fences(text: str) -> list[str]:
    pieces = re.split(r"```.*?```", text, flags=re.DOTALL)
    return [match.group(1).strip() for piece in pieces for match in LINK_RE.finditer(piece)]


def audit_health(root: Path) -> dict[str, dict[str, list[str]]]:
    broken: list[str] = []
    inbox_missing: list[str] = []
    stale_pending: list[str] = []
    knowledge_without_sources: list[str] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        if relative.startswith(".git/") or relative.startswith(".hermes/"):
            continue
        text = path.read_text(encoding="utf-8")
        if relative.startswith("knowledge/") and path.name != "README.md":
            if any(not existing_note(root, target) for target in links_outside_fences(text)):
                broken.append(relative)
            metadata = parse_frontmatter(text)
            if not metadata.get("sources") and not metadata.get("source_url"):
                knowledge_without_sources.append(relative)
        if relative.startswith("inbox/") and path.name not in {"README.md", "REVIEW_QUEUE.md"}:
            metadata = parse_frontmatter(text)
            if metadata.get("review_status") == "pending":
                if not metadata.get("source_url") and not metadata.get("sources"):
                    inbox_missing.append(relative)
                if metadata.get("captured_at"):
                    stale_pending.append(relative)
    return {
        "action_required": {"broken_wikilinks": broken},
        "warnings": {
            "inbox_missing_provenance": inbox_missing,
            "pending_inbox": stale_pending,
            "knowledge_missing_sources": knowledge_without_sources,
        },
    }


def render(report: dict[str, dict[str, list[str]]]) -> str:
    lines = ["# Knowledge Health Report", ""]
    for severity, label in (("action_required", "조치 필요"), ("warnings", "주의")):
        lines.append(f"## {label}")
        section = report[severity]
        if not any(section.values()):
            lines.append("- 없음")
        for key, paths in section.items():
            if paths:
                lines.append(f"### {key}")
                lines.extend(f"- `{path}`" for path in paths)
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = audit_health(args.root.resolve())
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else render(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
