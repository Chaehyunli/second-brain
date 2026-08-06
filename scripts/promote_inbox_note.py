#!/usr/bin/env python3
"""Explicit, review-gated Inbox promotion. It never runs autonomously."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


class PromotionError(RuntimeError):
    pass


def promote_note(root: Path, source: Path, destination: Path, approve: bool, review_note: str) -> Path:
    if not approve:
        raise PromotionError("--approve is required; Inbox notes are never promoted implicitly")
    if not review_note.strip():
        raise PromotionError("--review-note is required")
    source_path = root / source
    destination_path = root / destination
    if not source_path.is_file():
        raise PromotionError(f"source note not found: {source}")
    if destination_path.exists():
        raise PromotionError(f"destination already exists: {destination}")
    if not source_path.as_posix().startswith((root / "inbox").as_posix() + "/"):
        raise PromotionError("source must be inside inbox/")
    text = source_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise PromotionError("source note requires frontmatter")
    metadata_end = text.find("\n---\n", 4)
    if metadata_end == -1:
        raise PromotionError("source note frontmatter is incomplete")
    metadata = text[4:metadata_end]
    if "source_url:" not in metadata and "sources:" not in metadata:
        raise PromotionError("source provenance is required")
    additions = f"\nreview_status: approved\nreview_note: {review_note.strip()}\npromoted_from: {source.as_posix()}"
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_text("---\n" + metadata + additions + text[metadata_end:], encoding="utf-8")
    source_path.unlink()
    return destination_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--approve", action="store_true")
    parser.add_argument("--review-note", default="")
    args = parser.parse_args()
    root = args.root.resolve()
    if subprocess.run(["git", "status", "--porcelain"], cwd=root, capture_output=True, text=True).stdout.strip():
        raise SystemExit("refusing promotion: Vault worktree is not clean")
    try:
        promoted = promote_note(root, args.source, args.destination, args.approve, args.review_note)
    except PromotionError as error:
        raise SystemExit(str(error)) from error
    print(promoted.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
