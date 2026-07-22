#!/usr/bin/env python3
"""Shared, safe primitives for archiving selected source images beside Markdown notes."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image


class _TistoryImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.heading = "원문 이미지"
        self._heading_parts: list[str] | None = None
        self.items: list[ImageCandidate] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4"}:
            self._heading_parts = []
        if tag != "img":
            return
        data = dict(attrs)
        url = data.get("data-src") or data.get("src")
        if not url:
            return
        def number(key: str) -> int:
            try:
                return int(data.get(key) or 0)
            except ValueError:
                return 0
        self.items.append(ImageCandidate(url, number("width"), number("height"), self.heading, len(self.items)))

    def handle_data(self, data: str) -> None:
        if self._heading_parts is not None:
            self._heading_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"h1", "h2", "h3", "h4"} and self._heading_parts is not None:
            value = " ".join("".join(self._heading_parts).split())
            if value:
                self.heading = value
            self._heading_parts = None


def extract_tistory_candidates(source: str) -> list[ImageCandidate]:
    start = source.find('<div class="tt_article_useless_p_margin')
    end = source.find('<div class="container_postbtn', start) if start >= 0 else -1
    if start < 0 or end <= start:
        return []
    fragment = source[source.find(">", start) + 1:end]
    parser = _TistoryImageParser()
    parser.feed(fragment)
    return parser.items


@dataclass(frozen=True)
class ImageCandidate:
    url: str
    width: int
    height: int
    caption: str
    index: int


def archive_image_bytes(data: bytes, output: Path, max_width: int = 1600) -> tuple[str, int, int]:
    with Image.open(BytesIO(data)) as source:
        image = source.convert("RGBA") if source.mode in {"RGBA", "LA"} else source.convert("RGB")
        if image.width > max_width:
            height = round(image.height * max_width / image.width)
            image = image.resize((max_width, height), Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        image.save(output, format="WEBP", quality=88, method=6)
    return hashlib.sha256(data).hexdigest(), image.width, image.height


def eligible_note(path: Path) -> bool:
    parts = path.as_posix().split("/")
    if "SKALA" in parts or "STUDYING" in parts:
        return False
    return "[STUDYING]" not in path.name


def select_candidates(candidates: list[ImageCandidate], cap: int = 3) -> list[ImageCandidate]:
    chosen: list[ImageCandidate] = []
    seen: set[str] = set()
    for candidate in candidates:
        suffix = Path(urlparse(candidate.url).path).suffix.lower()
        if candidate.width < 240 or candidate.height < 100:
            continue
        if suffix not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            continue
        if candidate.url in seen:
            continue
        seen.add(candidate.url)
        chosen.append(candidate)
        if len(chosen) == cap:
            break
    return chosen


def append_image_section(note: Path, entries: list[tuple[str, str]]) -> bool:
    text = note.read_text(encoding="utf-8")
    if "\n## 핵심 이미지\n" in text:
        return False
    section = "## 핵심 이미지\n\n" + "\n\n".join(
        f"![{caption}]({relative_path})" for relative_path, caption in entries
    )
    marker = "## 관련 글\n"
    if marker in text:
        text = text.replace(marker, section + "\n\n" + marker, 1)
    else:
        text = text.rstrip() + "\n\n" + section + "\n"
    note.write_text(text, encoding="utf-8")
    return True
