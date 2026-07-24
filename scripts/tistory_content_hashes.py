#!/usr/bin/env python3
"""Stable, central SHA-256 state for archived Tistory post title/body content."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

MANIFEST_VERSION = 1


def normalized_title(title: str) -> str:
    return " ".join(title.split())


def normalized_blocks(blocks: Iterable[tuple[str, str]]) -> list[list[str]]:
    return [[kind, " ".join(value.split())] for kind, value in blocks]


def content_hash(title: str, blocks: Iterable[tuple[str, str]]) -> str:
    payload = {
        "title": normalized_title(title),
        "blocks": normalized_blocks(blocks),
    }
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def load_manifest(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("version") != MANIFEST_VERSION:
        raise ValueError(f"unsupported manifest version: {raw.get('version')!r}")
    posts = raw.get("posts")
    if not isinstance(posts, dict) or not all(isinstance(url, str) and isinstance(value, str) for url, value in posts.items()):
        raise ValueError("invalid manifest posts")
    return dict(sorted(posts.items()))


def save_manifest(path: Path, posts: dict[str, str]) -> None:
    payload = {"version": MANIFEST_VERSION, "posts": dict(sorted(posts.items()))}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def changed_urls(previous: dict[str, str], observed: dict[str, str]) -> tuple[list[str], list[str]]:
    changed = sorted(url for url, value in observed.items() if url in previous and previous[url] != value)
    added = sorted(url for url in observed if url not in previous)
    return changed, added
