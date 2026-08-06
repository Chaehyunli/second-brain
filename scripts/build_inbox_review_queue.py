#!/usr/bin/env python3
"""Build a non-mutating review queue for Inbox notes."""
from __future__ import annotations

import argparse
from pathlib import Path
from report_knowledge_candidates import parse_frontmatter


def build_queue(root: Path) -> dict[str, list[str]]:
    queue = {"ready_for_review": [], "needs_source": [], "needs_classification": []}
    inbox = root / "inbox"
    if not inbox.exists():
        return queue
    for path in sorted(inbox.rglob("*.md")):
        if path.name in {"README.md", "REVIEW_QUEUE.md"}:
            continue
        metadata = parse_frontmatter(path.read_text(encoding="utf-8"))
        relative = path.relative_to(root).as_posix()
        if metadata.get("review_status") != "pending":
            continue
        if not metadata.get("source_url") and not metadata.get("sources"):
            queue["needs_source"].append(relative)
        elif not metadata.get("type"):
            queue["needs_classification"].append(relative)
        else:
            queue["ready_for_review"].append(relative)
    return queue


def render_queue(queue: dict[str, list[str]]) -> str:
    labels = {
        "ready_for_review": "검토 가능",
        "needs_source": "출처 필요",
        "needs_classification": "분류 필요",
    }
    lines = ["# Inbox Review Queue", "", "> 생성 시각 기준 검토 대기 목록입니다. 이 파일은 승격·삭제를 수행하지 않습니다.", ""]
    for key in ("ready_for_review", "needs_source", "needs_classification"):
        lines.append(f"## {labels[key]}")
        if queue[key]:
            lines.extend(f"- [[{path[:-3]}]]" for path in queue[key])
        else:
            lines.append("- 없음")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("inbox/REVIEW_QUEUE.md"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_queue(build_queue(root)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
