#!/usr/bin/env python3
"""Render selected PDF pages as opaque PNG assets for visual Notion notes."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def parse_pages(value: str) -> list[int]:
    pages: set[int] = set()
    for part in value.split(","):
        item = part.strip()
        if not item:
            continue
        if "-" in item:
            start_text, end_text = item.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start < 1 or end < start:
                raise ValueError(f"invalid page range: {item}")
            pages.update(range(start, end + 1))
        else:
            page = int(item)
            if page < 1:
                raise ValueError(f"invalid page: {item}")
            pages.add(page)
    if not pages:
        raise ValueError("at least one page is required")
    return sorted(pages)


def render_pages(pdf: Path, pages: list[int], output_dir: Path, dpi: int) -> list[Path]:
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    if not shutil.which("pdftocairo"):
        raise RuntimeError("pdftocairo is required; install poppler-utils")

    output_dir.mkdir(parents=True, exist_ok=True)
    assets: list[Path] = []
    for page in pages:
        target = output_dir / f"page-{page:03d}"
        asset = target.with_suffix(".png")
        subprocess.run(
            [
                "pdftocairo",
                "-png",
                "-singlefile",
                "-r",
                str(dpi),
                "-f",
                str(page),
                "-l",
                str(page),
                str(pdf),
                str(target),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        if not asset.is_file() or asset.stat().st_size == 0:
            raise RuntimeError(f"PDF page {page} did not render")
        assets.append(asset)
    return assets


def write_manifest(pdf: Path, pages: list[int], assets: list[Path], output_dir: Path, dpi: int) -> Path:
    manifest = output_dir / "manifest.json"
    payload = {
        "source_pdf": str(pdf.resolve()),
        "dpi": dpi,
        "background": "opaque white",
        "assets": [
            {"page": page, "path": str(asset.resolve()), "status": "needs_visual_review"}
            for page, asset in zip(pages, assets, strict=True)
        ],
    }
    manifest.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", required=True, help="1-based pages, for example: 1,3-5")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--dpi", type=int, default=180)
    args = parser.parse_args()
    if args.dpi < 72:
        parser.error("--dpi must be at least 72")

    try:
        pages = parse_pages(args.pages)
        assets = render_pages(args.pdf, pages, args.output_dir, args.dpi)
        manifest = write_manifest(args.pdf, pages, assets, args.output_dir, args.dpi)
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        parser.error(str(exc))

    print(f"rendered={len(assets)} manifest={manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
