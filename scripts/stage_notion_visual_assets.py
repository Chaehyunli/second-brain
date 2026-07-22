#!/usr/bin/env python3
"""Stage rendered visual-note PNGs in Notion through the official ntn CLI."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def load_assets(manifest_path: Path) -> list[tuple[int, Path]]:
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    assets: list[tuple[int, Path]] = []
    for entry in payload.get("assets", []):
        page = entry.get("page")
        path = Path(entry.get("path", ""))
        if not isinstance(page, int) or not path.is_file():
            raise ValueError(f"invalid asset entry: {entry}")
        assets.append((page, path))
    if not assets:
        raise ValueError("manifest has no usable assets")
    return assets


def upload_asset(path: Path) -> dict[str, object]:
    try:
        result = subprocess.run(
            [
                "ntn",
                "files",
                "create",
                "--filename",
                path.name,
                "--content-type",
                "image/png",
                "--json",
            ],
            input=path.read_bytes(),
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(detail or f"ntn exited with status {exc.returncode}") from exc
    payload = json.loads(result.stdout)
    if not isinstance(payload, dict) or not payload.get("id"):
        raise RuntimeError("ntn returned no file upload ID")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()

    try:
        assets = load_assets(args.manifest)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.dry_run:
        for page, path in assets:
            print(f"page={page} asset={path.name} status=ready")
        print(f"ready={len(assets)}")
        return 0

    if not shutil.which("ntn"):
        parser.error("ntn is required; install it before uploading")

    uploads: list[dict[str, object]] = []
    try:
        for page, path in assets:
            upload = upload_asset(path)
            uploads.append({"page": page, "path": str(path.resolve()), "file_upload": upload})
    except (OSError, RuntimeError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        parser.error(f"Notion upload failed: {exc}")

    receipt = args.receipt or args.manifest.with_name("notion_uploads.json")
    receipt.write_text(json.dumps({"uploads": uploads}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"uploaded={len(uploads)} receipt={receipt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
