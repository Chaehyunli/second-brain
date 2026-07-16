#!/usr/bin/env python3
"""Validate SKALA Notion→Obsidian identities without rewriting frozen notes."""

from __future__ import annotations

import re
import sys
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


def main() -> int:
    errors: list[str] = []
    legacy: list[str] = []
    seen_ids: dict[str, Path] = {}

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
        if page_id in seen_ids:
            errors.append(f"duplicate notion_page_id {page_id}: {seen_ids[page_id]} and {rel}")
        else:
            seen_ids[page_id] = rel

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

    if errors:
        print("[SKALA sync validation] failed")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"[SKALA sync validation] ok: {len(seen_ids)} unique note identities")
    if legacy:
        print(f"legacy frozen notes without source hash/timestamp: {len(legacy)}")
        print("\n".join(f"- {item}" for item in legacy))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
