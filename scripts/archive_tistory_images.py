#!/usr/bin/env python3
"""Archive up to three visible, substantive images from each eligible Tistory note.

SKALA and [STUDYING] are intentionally out of scope; this command operates only
on existing blog notes with a Tistory canonical source URL.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

from archive_note_images import (
    ImageCandidate,
    append_image_section,
    archive_image_bytes,
    eligible_note,
    extract_tistory_candidates,
    select_candidates,
)

ROOT = Path("/root/wiki")
URL_RE = re.compile(r"^source_url: (https://ch010104\.tistory\.com/\d+)$", re.M)
UA = "Mozilla/5.0 (compatible; SecondBrainImageArchive/1.0)"
MAX_DOWNLOAD_BYTES = 10 * 1024 * 1024


def fetch_page(url: str) -> str:
    with urlopen(Request(url, headers={"User-Agent": UA}), timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def fetch(url: str, *, referer: str | None = None) -> tuple[bytes, str]:
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        content_type = response.headers.get("Content-Type", "")
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_DOWNLOAD_BYTES:
            raise ValueError("source image exceeds 10 MiB")
        data = response.read(MAX_DOWNLOAD_BYTES + 1)
    if len(data) > MAX_DOWNLOAD_BYTES:
        raise ValueError("source image exceeds 10 MiB")
    if not content_type.startswith("image/"):
        raise ValueError(f"unexpected content type: {content_type}")
    return data, content_type


def safe_slug(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9가-힣._-]+", "-", text).strip(".-")
    return slug[:72] or "source"


def image_source_path(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def archive_note(note: Path, source_page: str, *, dry_run: bool = False) -> tuple[int, list[str]]:
    if "\n## 핵심 이미지\n" in note.read_text(encoding="utf-8"):
        return 0, []
    source_html = fetch_page(source_page)
    candidates = select_candidates(extract_tistory_candidates(source_html))
    if not candidates:
        return 0, []
    asset_dir = note.parent / "assets" / safe_slug(note.stem)
    entries: list[tuple[str, str]] = []
    manifest: list[str] = [f"source_page: {source_page}", "", "selected_images:"]
    errors: list[str] = []
    for ordinal, candidate in enumerate(candidates, 1):
        try:
            data, content_type = fetch(candidate.url, referer=source_page)
            filename = f"{ordinal:02d}-{safe_slug(candidate.caption)}.webp"
            destination = asset_dir / filename
            if not dry_run:
                sha256, width, height = archive_image_bytes(data, destination)
            else:
                sha256, width, height = "dry-run", candidate.width, candidate.height
            label = candidate.caption if candidate.caption != "원문 이미지" else f"원문 이미지 {ordinal}"
            entries.append((f"assets/{asset_dir.name}/{filename}", label))
            manifest.extend([
                f"- file: {filename}",
                f"  context: {label}",
                f"  source_image_path: {image_source_path(candidate.url)}",
                f"  source_content_type: {content_type}",
                f"  source_sha256: {sha256}",
                f"  archived_dimensions: {width}x{height}",
            ])
        except Exception as exc:
            errors.append(f"{candidate.index}: {type(exc).__name__}: {exc}")
    if not entries or dry_run:
        return len(entries), errors
    asset_dir.mkdir(parents=True, exist_ok=True)
    (asset_dir / "SOURCE.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    append_image_section(note, entries)
    return len(entries), errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    results: list[tuple[Path, int, list[str]]] = []
    notes = []
    for note in sorted((ROOT / "blog").rglob("*.md")):
        if note.name == "index.md" or not eligible_note(note):
            continue
        match = URL_RE.search(note.read_text(encoding="utf-8"))
        if match:
            notes.append((note, match.group(1)))
    if args.limit is not None:
        notes = notes[: args.limit]
    def one(item: tuple[Path, str]) -> tuple[Path, int, list[str]]:
        note, source_page = item
        try:
            count, errors = archive_note(note, source_page, dry_run=args.dry_run)
            return note, count, errors
        except Exception as exc:
            return note, 0, [f"source: {type(exc).__name__}: {exc}"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        results.extend(executor.map(one, notes))
    changed = sum(1 for _, count, _ in results if count)
    images = sum(count for _, count, _ in results)
    errors = sum(len(items) for _, _, items in results)
    print(f"notes={len(results)} changed={changed} images={images} image_errors={errors}")
    for note, _, items in results:
        for error in items:
            print(f"WARN {note.relative_to(ROOT)}: {error}")


if __name__ == "__main__":
    main()
