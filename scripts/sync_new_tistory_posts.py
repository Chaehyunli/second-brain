#!/usr/bin/env python3
"""Append only newly discovered Tistory posts; never rewrite archived notes."""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

from enrich_tistory_blog_bodies import body_blocks, classify_post, fetch, render_note
from rebuild_tistory_blog import category_of, meta, quote, safe_name, tags_of

ROOT = Path("/root/wiki")
BLOG = ROOT / "blog"
URL_RE = re.compile(r"^source_url: (https://ch010104\.tistory\.com/\d+)$", re.M)


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\n.*?\n---\n*", text, re.S)
    if not match:
        raise ValueError("frontmatter missing")
    return match.group(0)


def prop(text: str, key: str) -> str:
    match = re.search(rf'^{re.escape(key)}: "?([^"\n]+)"?$', text, re.M)
    return match.group(1).strip() if match else ""


def replace_front_value(front: str, key: str, value: str) -> str:
    return re.sub(rf"^{re.escape(key)}: .*?$", f"{key}: {value}", front, flags=re.M)


def existing_urls() -> set[str]:
    return {match.group(1) for path in BLOG.rglob("*.md") for match in URL_RE.finditer(path.read_text(encoding="utf-8"))}


def make_post(url: str) -> tuple[str, Path]:
    source = fetch(url)
    title = re.sub(r"\s*::\s*소소한 지식 저장소\s*$", "", meta(source, "og:title")).strip()
    published = meta(source, "article:published_time")[:10] or date.today().isoformat()
    category = category_of(source)
    blocks = body_blocks(source)
    note_type = classify_post(title, category, blocks)
    category_dir = BLOG / safe_name(category)
    category_dir.mkdir(parents=True, exist_ok=True)
    path = category_dir / f"{safe_name(title)}.md"
    if path.exists():
        raise FileExistsError(path)
    tags = ["blog", "technical-writing", *tags_of(source)]
    tag_line = "tags: [" + ", ".join('"' + quote(tag) + '"' for tag in tags) + "]"
    front = "\n".join([
        "---", f'title: "{quote(title)}"', f"created: {date.today().isoformat()}",
        f"updated: {date.today().isoformat()}", "type: blog-post", tag_line,
        f'category: "{quote(category)}"', f"published: {published}", f"source_url: {url}", "---", "",
    ])
    old_body = f"## 관련 글\n\n- [[blog/{safe_name(category)}/index|{category}]]\n"
    path.write_text(render_note(front, old_body, title, note_type, blocks), encoding="utf-8")
    return category, path


def rebuild_category_index(category: str) -> None:
    directory = BLOG / safe_name(category)
    notes = []
    for path in directory.glob("*.md"):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        notes.append((prop(text, "published"), prop(text, "title"), path))
    notes.sort(key=lambda item: (item[0], item[2].name), reverse=True)
    index = directory / "index.md"
    if index.exists():
        front = frontmatter(index.read_text(encoding="utf-8"))
        front = replace_front_value(front, "updated", date.today().isoformat())
    else:
        front = "\n".join(["---", f'title: "{quote(category)}"', f"created: {date.today().isoformat()}", f"updated: {date.today().isoformat()}", "type: blog-category", "tags: [blog, technical-writing]", "---", ""])
    lines = [front.rstrip(), "", f"# {category}", "", f"> 글 {len(notes)}개 · 카테고리 기반 탐색", "", "## 글", ""]
    for published, title, path in notes:
        lines.append(f"- [[blog/{path.relative_to(BLOG).with_suffix('').as_posix()}|{title}]] — {published}")
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")


def rebuild_root_index() -> None:
    index = BLOG / "index.md"
    old = index.read_text(encoding="utf-8")
    front = replace_front_value(frontmatter(old), "updated", date.today().isoformat())
    categories = []
    for directory in sorted(path for path in BLOG.iterdir() if path.is_dir()):
        count = len([path for path in directory.glob("*.md") if path.name != "index.md"])
        if count:
            categories.append((directory.name, count))
    lines = [front.rstrip(), "", "# 기술 블로그", "", "> 원본: https://ch010104.tistory.com/", "> 글은 카테고리 폴더에 저장하고, 각 노트는 태그·카테고리 기반 관련 글만 연결합니다.", "", "## 카테고리", ""]
    lines.extend(f"- [[blog/{name}/index|{name}]] — {count}개" for name, count in categories)
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    args = parser.parse_args()
    known = existing_urls()
    if duplicates := sorted(set(args.urls) & known):
        raise SystemExit(f"already archived: {duplicates}")
    categories = set()
    for url in args.urls:
        category, _ = make_post(url)
        categories.add(category)
    for category in categories:
        rebuild_category_index(category)
    rebuild_root_index()
    print(f"DONE added={len(args.urls)} categories={','.join(sorted(categories))}")


if __name__ == "__main__":
    main()
