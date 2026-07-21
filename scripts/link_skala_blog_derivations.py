#!/usr/bin/env python3
"""Create explicit Obsidian links between a SKALA canonical note and a derived blog post."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

NOTION_ID_RE = re.compile(
    r"https?://(?:app\.notion\.com/p/|(?:www\.)?notion\.so/(?:[^\"'<>/]+/)?)([0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}|[0-9a-f]{32})",
    re.I,
)
SOURCE_MARKER_RE = re.compile(r"(?:학습\s*원본|SKALA\s*원문)", re.I)


def normalize_notion_id(value: str) -> str:
    raw = value.strip().lower().replace("-", "")
    if not re.fullmatch(r"[0-9a-f]{32}", raw):
        raise ValueError(f"invalid Notion page ID: {value}")
    return f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"


def extract_notion_page_id(html: str) -> str | None:
    marker = SOURCE_MARKER_RE.search(html)
    if not marker:
        return None
    match = NOTION_ID_RE.search(html, marker.end())
    return normalize_notion_id(match.group(1)) if match else None


def note_target(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).with_suffix("").as_posix()


def find_skala_note(skala_root: Path, notion_page_id: str) -> Path | None:
    wanted = normalize_notion_id(notion_page_id)
    for note in skala_root.rglob("*.md"):
        match = re.search(r'^notion_page_id:\s*"?([^"\n]+)', note.read_text(encoding="utf-8"), re.M)
        if not match:
            continue
        try:
            candidate_id = normalize_notion_id(match.group(1))
        except ValueError:
            continue
        if candidate_id == wanted:
            return note
    return None


def append_section(path: Path, heading: str, link: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if link in text:
        return False
    suffix = "" if text.endswith("\n") else "\n"
    path.write_text(f"{text}{suffix}\n## {heading}\n\n- {link}\n", encoding="utf-8")
    return True


def link_pair(blog: Path, skala: Path, *, blog_target: str, skala_target: str) -> tuple[bool, bool]:
    blog_changed = append_section(
        blog,
        "학습 기준본",
        f"[[{skala_target}|SKALA 상세 학습 노트]]",
    )
    skala_changed = append_section(
        skala,
        "공개 게시물",
        f"[[{blog_target}|공개 블로그 글]]",
    )
    return blog_changed, skala_changed


def link_blog_from_source(blog: Path, source_html: str, root: Path) -> bool:
    notion_page_id = extract_notion_page_id(source_html)
    if not notion_page_id:
        return False
    skala = find_skala_note(root / "notion/SKALA", notion_page_id)
    if not skala:
        return False
    blog_changed, skala_changed = link_pair(
        blog,
        skala,
        blog_target=note_target(blog, root),
        skala_target=note_target(skala, root),
    )
    return blog_changed or skala_changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("/root/wiki"))
    parser.add_argument("--blog-note", type=Path, required=True)
    parser.add_argument("--notion-page-id", required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    blog = args.blog_note if args.blog_note.is_absolute() else root / args.blog_note
    skala = find_skala_note(root / "notion/SKALA", args.notion_page_id)
    if not blog.is_file():
        raise SystemExit(f"blog note not found: {blog}")
    if not skala:
        raise SystemExit(f"SKALA note not found for Notion page: {args.notion_page_id}")

    blog_changed, skala_changed = link_pair(
        blog,
        skala,
        blog_target=note_target(blog, root),
        skala_target=note_target(skala, root),
    )
    print(f"linked blog_changed={blog_changed} skala_changed={skala_changed}")


if __name__ == "__main__":
    main()
