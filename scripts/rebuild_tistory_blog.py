#!/usr/bin/env python3
"""Rebuild the Tistory archive as concise, category-organized Obsidian notes."""
from __future__ import annotations

import concurrent.futures
import html
import re
import shutil
import subprocess
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://ch010104.tistory.com"
SITEMAP = f"{BASE}/sitemap.xml"
VAULT = Path("/root/wiki")
STAGING = Path("/tmp/wiki-blog-rebuild")
TARGET = VAULT / "blog"
UA = "Mozilla/5.0 (compatible; SecondBrainArchive/2.0)"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def fetch(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", "--retry", "2", "--max-time", "30", "-A", UA, url],
        check=True, capture_output=True,
    )
    return result.stdout.decode("utf-8", "replace")


def meta(source: str, key: str) -> str:
    for pattern in (
        rf'<meta[^>]+(?:property|name)=["\']{re.escape(key)}["\'][^>]+content=["\']([^"\']*)',
        rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:property|name)=["\']{re.escape(key)}["\']',
    ):
        hit = re.search(pattern, source, re.I)
        if hit:
            return html.unescape(hit.group(1)).strip()
    return ""


def text_only(fragment: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(fragment))).strip()


def category_of(source: str, title: str = "") -> str:
    entry = re.search(r'window\.T\.entryInfo\s*=\s*\{.*?"categoryLabel"\s*:\s*"((?:\\.|[^"\\])*)"', source, re.DOTALL)
    if entry:
        return bytes(entry.group(1), 'utf-8').decode('unicode_escape') if '\\' in entry.group(1) else entry.group(1)
    visible = re.search(r'<strong[^>]+class=["\'][^"\']*\btit_category\b[^"\']*["\'][^>]*>.*?<a[^>]*>(.*?)</a>', source, re.I | re.S)
    if visible:
        value = text_only(visible.group(1))
        if value:
            return value
    hit = re.search(r'<p[^>]+class=["\']category["\'][^>]*>(.*?)</p>', source, re.I | re.S)
    if hit:
        value = text_only(hit.group(1))
        if value:
            return value
    if title.startswith("[STUDYING]"):
        return "STUDYING"
    if re.match(r"^\[(?:스프링|모든 개발자를 위한 HTTP 웹 기본 지식)", title):
        return "INFLEARN"
    return "카테고리 없음"


def tags_of(source: str) -> list[str]:
    section = re.search(r'<div[^>]+class=["\'][^"\']*\bbox-tag\b[^"\']*["\'][^>]*>(.*?)</div>', source, re.I | re.S)
    if not section:
        return []
    tags = [text_only(v) for v in re.findall(r'<a[^>]*rel=["\']tag["\'][^>]*>(.*?)</a>', section.group(1), re.I | re.S)]
    return list(dict.fromkeys(tag for tag in tags if tag and len(tag) <= 50))


class Blocks(HTMLParser):
    """Keep only readable headings, paragraphs, and list items; ignore code/media."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, str]] = []
        self.kind: str | None = None
        self.buf: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "pre", "code", "table"}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4", "p", "li", "blockquote"}:
            self.finish()
            self.kind = "heading" if tag.startswith("h") else "text"
        elif tag == "br" and self.kind:
            self.buf.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "pre", "code", "table"}:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4", "p", "li", "blockquote"}:
            self.finish()

    def handle_data(self, data: str) -> None:
        if not self.skip and self.kind:
            self.buf.append(data)

    def finish(self) -> None:
        if self.kind:
            value = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if value:
                self.blocks.append((self.kind, value))
        self.kind = None
        self.buf = []


def body_blocks(source: str) -> list[tuple[str, str]]:
    start = source.find('<div class="tt_article_useless_p_margin')
    end = source.find('<div class="container_postbtn', start) if start >= 0 else -1
    if start < 0 or end <= start:
        return []
    fragment = source[source.find(">", start) + 1:end]
    parser = Blocks()
    parser.feed(fragment)
    parser.finish()
    return parser.blocks


def useful(text: str) -> bool:
    text = text.strip()
    if len(text) < 25 or len(text) > 360:
        return False
    if re.fullmatch(r"[\d\s.,\[\](){}:+*/=\-]+", text):
        return False
    if any(marker in text.lower() for marker in ("package ", "import ", "public class", "<script", "http://localhost")):
        return False
    return len(re.findall(r"[가-힣A-Za-z]", text)) >= 12


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|(?<=다\.)\s+", text)
    return [p.strip() for p in parts if useful(p.strip())]


def summarize(blocks: list[tuple[str, str]]) -> list[str]:
    # ponytail: deterministic extractive summary; replace with an LLM only if editorial rewriting is required.
    selected: list[str] = []
    seen: set[str] = set()
    used_headings: set[str] = set()
    heading = ""
    for kind, value in blocks:
        if kind == "heading":
            heading = value[:60]
            continue
        if heading in used_headings:
            continue
        for sentence in sentences(value):
            normalized = re.sub(r"\W+", "", sentence).lower()
            heading_normalized = re.sub(r"\W+", "", heading).lower()
            if normalized in seen or (heading_normalized and normalized.startswith(heading_normalized) and len(normalized) <= len(heading_normalized) + 12):
                continue
            seen.add(normalized)
            prefix = f"**{heading}** — " if heading else ""
            selected.append(prefix + sentence[:260])
            used_headings.add(heading)
            break
        if len(selected) >= 4:
            break
    if not selected:
        for _, value in blocks:
            clean = re.sub(r"\s+", " ", value).strip()
            if useful(clean):
                selected.append(clean[:260])
            if len(selected) >= 3:
                break
    return selected[:4]


def safe_name(value: str) -> str:
    value = unicodedata.normalize("NFC", value).strip()
    value = re.sub(r'[<>:"/\\|?*\[\]\x00-\x1f]', "-", value)
    return re.sub(r"\s+", " ", value).strip(" .-")[:150] or "제목 없는 글"


def quote(value: str) -> str:
    return value.replace('"', "'").replace("\n", " ")


def wiki(path: Path, label: str | None = None) -> str:
    stem = "blog/" + path.with_suffix("").as_posix()
    return f"[[{stem}|{label}]]" if label else f"[[{stem}]]"


def parse_one(url: str) -> dict:
    source = fetch(url)
    post_id = int(url.rsplit("/", 1)[1])
    title = re.sub(r"\s*::\s*소소한 지식 저장소\s*$", "", meta(source, "og:title")).strip() or f"글 {post_id}"
    published = meta(source, "article:published_time")[:10] or "발행일 미확인"
    blocks = body_blocks(source)
    return {
        "id": post_id, "url": url, "title": title, "category": category_of(source),
        "published": published, "tags": tags_of(source), "summary": summarize(blocks),
    }


def related(records: list[dict]) -> None:
    for record in records:
        tagset = {tag.lower() for tag in record["tags"]}
        def score(other: dict) -> tuple[int, int, int]:
            overlap = len(tagset & {tag.lower() for tag in other["tags"]})
            same_category = int(record["category"] == other["category"])
            # Nearby publication dates provide a stable tie-breaker within a topic series.
            return (overlap * 4 + same_category, overlap, -abs(record["id"] - other["id"]))
        options = [other for other in records if other is not record and score(other)[0] > 0]
        options.sort(key=score, reverse=True)
        record["related"] = options[:3]


def main() -> None:
    sitemap = fetch(SITEMAP)
    root = ET.fromstring(sitemap)
    urls = sorted({(node.text or "").strip() for node in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc") if re.fullmatch(r"https://ch010104\.tistory\.com/\d+", (node.text or "").strip())}, key=lambda u: int(u.rsplit("/", 1)[1]))
    assert len(urls) >= 297, f"unexpected sitemap count: {len(urls)}"

    records: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(parse_one, url): url for url in urls}
        for n, future in enumerate(concurrent.futures.as_completed(futures), 1):
            records.append(future.result())
            if n % 30 == 0:
                print(f"fetched={n}/{len(urls)}", flush=True)
    records.sort(key=lambda item: item["id"])
    related(records)

    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    by_category: dict[str, list[dict]] = defaultdict(list)
    used_paths: set[Path] = set()
    for record in records:
        directory = STAGING / safe_name(record["category"])
        directory.mkdir(parents=True, exist_ok=True)
        filename = safe_name(record["title"])
        path = directory / f"{filename}.md"
        if path in used_paths:
            path = directory / f"{filename} ({record['id']}).md"
        used_paths.add(path)
        record["path"] = path.relative_to(STAGING)
        record["category_index"] = directory.relative_to(STAGING) / "index.md"
        by_category[record["category"]].append(record)

    for record in records:
        tags = ["blog", "technical-writing", *record["tags"]]
        links = [wiki(record["category_index"], record["category"])]
        links.extend(wiki(other["path"], other["title"]) for other in record["related"])
        summary_lines = "\n".join(f"- {line}" for line in record["summary"]) or "- 본문에서 핵심 문장을 자동 추출하지 못했습니다. 원문 링크에서 확인하세요."
        related_lines = "\n".join(f"- {link}" for link in links)
        content = f'''---
title: "{quote(record['title'])}"
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
type: blog-post
tags: [{', '.join('"' + quote(tag) + '"' for tag in tags)}]
category: "{quote(record['category'])}"
published: {record['published']}
source_url: {record['url']}
---

# {record['title']}

## 원문

{record['url']}

## 핵심 요약

{summary_lines}

## 관련 글

{related_lines}
'''
        (STAGING / record["path"]).write_text(content, encoding="utf-8")

    for category, items in by_category.items():
        items.sort(key=lambda item: (item["published"], item["id"]), reverse=True)
        lines = [
            "---", f'title: "{quote(category)}"', f"created: {date.today().isoformat()}",
            f"updated: {date.today().isoformat()}", "type: blog-category", "tags: [blog, technical-writing]",
            "---", "", f"# {category}", "", f"> 글 {len(items)}개 · 카테고리 기반 탐색", "", "## 글", "",
        ]
        for item in items:
            lines.append(f"- {wiki(item['path'], item['title'])} — {item['published']}")
        (STAGING / items[0]["category_index"]).write_text("\n".join(lines) + "\n", encoding="utf-8")

    category_links = []
    for category, items in sorted(by_category.items(), key=lambda pair: pair[0]):
        category_links.append(f"- {wiki(items[0]['category_index'], category)} — {len(items)}개")
    (STAGING / "index.md").write_text("\n".join([
        "---", "title: 기술 블로그", f"created: {date.today().isoformat()}", f"updated: {date.today().isoformat()}",
        "type: index", "tags: [blog, technical-writing]", f"source_url: {BASE}/", "---", "", "# 기술 블로그", "",
        f"> 원본: {BASE}/", "> 글은 카테고리 폴더에 저장하고, 각 노트는 태그·카테고리 기반 관련 글만 연결합니다.",
        "", "## 카테고리", "", *category_links, "",
    ]), encoding="utf-8")

    notes = [path for path in STAGING.rglob("*.md") if path.name != "index.md"]
    assert len(notes) == len(records), (len(notes), len(records))
    assert not any(re.search(r"^\d+-", path.name) for path in notes), "numeric filename prefix remains"
    assert all("## 원문\n\nhttps://ch010104.tistory.com/" in path.read_text(encoding="utf-8") for path in notes)
    assert all("[0.0102" not in path.read_text(encoding="utf-8") for path in notes)
    assert all("## 핵심 요약\n\n- " in path.read_text(encoding="utf-8") for path in notes)
    # ponytail: blocks legacy NumPy-style [[1, 2], [3, 4]] data from becoming Obsidian graph nodes.
    assert not any(re.search(r"\[\[[0-9][0-9, .\[\]-]*\]\]", path.read_text(encoding="utf-8")) for path in notes)
    assert len(list(STAGING.iterdir())) == len(by_category) + 1

    backup = Path("/tmp/wiki-blog-previous")
    if backup.exists():
        shutil.rmtree(backup)
    if TARGET.exists():
        TARGET.rename(backup)
    STAGING.rename(TARGET)
    shutil.rmtree(backup)
    print(f"DONE posts={len(records)} categories={len(by_category)} related_links={sum(len(r['related']) for r in records)}")


if __name__ == "__main__":
    main()
