#!/usr/bin/env python3
"""Validate changed Markdown links and agent-context file consistency."""
from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

CONTEXT_FILES = ("AGENTS.md", "CLAUDE.md", "agent.md")
WIKILINK_RE = re.compile(r"(?<![!\\\\])\[\[([^\]|#]+?)(?:\]\]|\|)")
NUMERIC_TARGET_RE = re.compile(r"^\d+(?:-\d+)?$")


@dataclass(frozen=True)
class Issue:
    kind: str
    path: Path
    target: str


def without_fenced_code(text: str) -> str:
    parts = text.split("```")
    return "".join(part for index, part in enumerate(parts) if index % 2 == 0)


def markdown_paths(root: Path) -> list[Path]:
    return [path for path in root.rglob("*.md") if ".git" not in path.parts and ".obsidian" not in path.parts]


def resolves(root: Path, target: str, notes: list[Path]) -> bool:
    target = target.strip().removesuffix(".md")
    if "/" in target:
        candidate = root / f"{target}.md"
        return candidate in notes
    return any(path.stem == target for path in notes)


def audit_markdown(root: Path, paths: list[Path] | None = None) -> list[Issue]:
    root = root.resolve()
    notes = markdown_paths(root)
    selected = paths or notes
    issues: list[Issue] = []
    for path in selected:
        path = path.resolve()
        if path.name in CONTEXT_FILES or path.name == "README.md":
            continue
        text = without_fenced_code(path.read_text(encoding="utf-8"))
        for raw_target in WIKILINK_RE.findall(text):
            target = raw_target.strip()
            if NUMERIC_TARGET_RE.fullmatch(target):
                issues.append(Issue("numeric_wikilink", path, target))
            elif not resolves(root, target, notes):
                issues.append(Issue("missing_wikilink", path, target))
    return issues


def context_files_match(root: Path) -> bool:
    paths = [root / name for name in CONTEXT_FILES]
    return all(path.is_file() for path in paths) and len({path.read_bytes() for path in paths}) == 1


def staged_markdown_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z", "--", "*.md"],
        cwd=root, check=True, capture_output=True,
    )
    return [root / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", action="append", default=[])
    parser.add_argument("--changed-from-index", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    root = Path.cwd()
    paths = [root / value for value in args.path]
    if args.changed_from_index:
        paths.extend(staged_markdown_paths(root))
    if not paths:
        paths = markdown_paths(root)
    issues = audit_markdown(root, paths)
    if not context_files_match(root):
        issues.append(Issue("context_files_drift", root, ", ".join(CONTEXT_FILES)))
    for issue in issues:
        print(f"{issue.kind}: {issue.path.relative_to(root)}: {issue.target}")
    print(f"checked={len(paths)} issues={len(issues)}")
    return 1 if args.strict and issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
