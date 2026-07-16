#!/usr/bin/env python3
"""Validate SKALA Notion→Obsidian identities without rewriting frozen notes."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "notion" / "SKALA"
REQUIRED = {"title", "notion_page_id", "source_url"}
PROVENANCE = {"synced_at", "content_sha256"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter missing")
    try:
        block = text.split("---", 2)[1]
    except IndexError as exc:
        raise ValueError("frontmatter unterminated") from exc
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def first_git_upload_time(path: Path) -> int | None:
    """Return the first commit timestamp that introduced a note to this Vault."""
    vault = ROOT.parents[1]
    try:
        relative_path = path.relative_to(vault)
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%ct", "--reverse", "--", str(relative_path)],
            cwd=vault,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    timestamps = result.stdout.split()
    return int(timestamps[0]) if timestamps else None


def main() -> int:
    errors: list[str] = []
    legacy: list[str] = []
    paths_by_id: dict[str, list[Path]] = {}
    resolved_duplicates: list[tuple[str, Path, list[Path]]] = []

    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        try:
            meta = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        missing = REQUIRED - meta.keys()
        if missing:
            errors.append(f"{rel}: required metadata missing: {', '.join(sorted(missing))}")
            continue

        page_id = meta["notion_page_id"]
        paths_by_id.setdefault(page_id, []).append(path)

        provenance_missing = PROVENANCE - meta.keys()
        if provenance_missing == PROVENANCE:
            # Existing notes are immutable after their first Git commit. They
            # may predate provenance fields; report but never fail or rewrite.
            legacy.append(str(rel))
        elif provenance_missing:
            errors.append(
                f"{rel}: partial provenance metadata missing: {', '.join(sorted(provenance_missing))}"
            )
        elif not SHA256.fullmatch(meta["content_sha256"]):
            errors.append(f"{rel}: content_sha256 is not a 64-character lowercase SHA-256")

    for page_id, paths in paths_by_id.items():
        if len(paths) == 1:
            continue
        dated_paths: list[tuple[int, Path]] = []
        for path in paths:
            upload_time = first_git_upload_time(path)
            if upload_time is None:
                errors.append(f"duplicate notion_page_id {page_id}: Git upload time unavailable")
                break
            dated_paths.append((upload_time, path))
        else:
            latest_time = max(timestamp for timestamp, _ in dated_paths)
            latest_paths = [path for timestamp, path in dated_paths if timestamp == latest_time]
            if len(latest_paths) != 1:
                errors.append(f"duplicate notion_page_id {page_id}: latest Git upload time is tied")
                continue
            canonical = latest_paths[0]
            ignored = [path for _, path in dated_paths if path != canonical]
            resolved_duplicates.append((page_id, canonical, ignored))

    if errors:
        print("[SKALA sync validation] failed")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"[SKALA sync validation] ok: {len(paths_by_id)} unique note identities")
    for page_id, canonical, ignored in resolved_duplicates:
        ignored_paths = ", ".join(str(path.relative_to(ROOT)) for path in ignored)
        print(f"duplicate {page_id}: use later Git upload {canonical.relative_to(ROOT)}; ignore {ignored_paths}")
    if legacy:
        print(f"legacy frozen notes without source hash/timestamp: {len(legacy)}")
        print("\n".join(f"- {item}" for item in legacy))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
