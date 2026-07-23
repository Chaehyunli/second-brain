#!/usr/bin/env python3
"""Enrich existing Tistory Markdown note bodies without changing paths or frontmatter."""
from __future__ import annotations

import argparse
import concurrent.futures
import html
import re
import subprocess
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://ch010104.tistory.com"
VAULT = Path("/root/wiki")
BLOG = VAULT / "blog"
UA = "Mozilla/5.0 (compatible; SecondBrainArchive/3.0)"


class RichBlocks(HTMLParser):
    """Extract readable source structure, including instructional code blocks."""

    TEXT_TAGS = {"h1", "h2", "h3", "h4", "p", "li", "blockquote"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, str]] = []
        self.kind: str | None = None
        self.buf: list[str] = []
        self.skip_depth = 0
        self.code_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.finish()
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "pre":
            self.finish()
            self.kind = "code"
            self.code_depth = 1
            return
        if self.code_depth:
            if tag == "code":
                return
            return
        if tag in self.TEXT_TAGS:
            self.finish()
            self.kind = "heading" if tag.startswith("h") else "text"
        elif tag == "br" and self.kind:
            self.buf.append("\n" if self.kind == "code" else " ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"}:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == "pre" and self.code_depth:
            self.code_depth = 0
            self.finish()
            return
        if self.code_depth:
            return
        if tag in self.TEXT_TAGS:
            self.finish()

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and self.kind:
            self.buf.append(data)

    def finish(self) -> None:
        if not self.kind:
            return
        if self.kind == "code":
            value = "".join(self.buf).strip("\n")
        else:
            value = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if value:
            self.blocks.append((self.kind, value))
        self.kind = None
        self.buf = []


def fetch(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", "--retry", "2", "--max-time", "30", "-A", UA, url],
        check=True, capture_output=True,
    )
    return result.stdout.decode("utf-8", "replace")


def body_blocks(source: str) -> list[tuple[str, str]]:
    start = source.find('<div class="tt_article_useless_p_margin')
    end = source.find('<div class="container_postbtn', start) if start >= 0 else -1
    if start < 0 or end <= start:
        return []
    fragment = source[source.find(">", start) + 1:end]
    parser = RichBlocks()
    parser.feed(fragment)
    parser.finish()
    return parser.blocks


def classify_post(title: str, category: str, blocks: list[tuple[str, str]]) -> str:
    # Course-category membership is stronger evidence than incidental words such as
    # "문제" in an explanatory lesson.
    if category == "INFLEARN":
        return "tutorial"
    title_text = f"{title} {category}"
    if re.search(r"오류|에러|문제 해결|트러블|권한|충돌|실패|버그|exception|error|cors", title_text, re.I):
        return "troubleshooting"
    if re.search(r"프로젝트|구현기|개발기|회고|포트폴리오|서비스", title_text, re.I):
        return "project"
    text = title_text + " " + " ".join(value for kind, value in blocks[:12] if kind != "code")
    low = text.lower()
    if re.search(r"강의|실습|학습 목표|커리큘럼", text, re.I):
        return "tutorial"
    if re.search(r"vs\.?|비교|차이|개념|이해|소개|분포|원리|란\??", low, re.I):
        return "concept"
    return "guide"


def code_language(code: str) -> str:
    lowered = code.lower()
    if "public class" in lowered or "springframework" in lowered or "@springboot" in lowered or "jdbctemplate" in lowered:
        return "java"
    if "def " in lowered or "import numpy" in lowered or "import pandas" in lowered:
        return "python"
    if "select " in lowered or "insert into" in lowered or "create table" in lowered:
        return "sql"
    if "{" in code and ("const " in lowered or "function " in lowered or "=>" in code):
        return "typescript"
    if "<" in code and "/>" in code:
        return "html"
    if "docker" in lowered or "kubectl" in lowered:
        return "bash"
    return "text"


HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>\n]*>")


def literalize_html_tags(value: str) -> str:
    """Keep source HTML examples as Markdown code instead of live renderer nodes."""
    return HTML_TAG_RE.sub(lambda match: f"`{match.group(0)}`", value)


def literalize_html_tags_in_markdown(markdown: str) -> str:
    """Quote literal HTML examples while preserving fenced code blocks verbatim."""
    fenced = False
    output: list[str] = []
    for line in markdown.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            output.append(line)
            continue
        if fenced:
            output.append(line)
            continue
        parts = re.split(r"(`[^`]*`)", line)
        output.append("".join(
            part if index % 2 else literalize_html_tags(part)
            for index, part in enumerate(parts)
        ))
    return "".join(output)


def opening_texts(blocks: list[tuple[str, str]], limit: int = 2) -> list[str]:
    found: list[str] = []
    for kind, value in blocks:
        if kind != "text" or len(value) < 35:
            continue
        found.append(literalize_html_tags(value[:700]))
        if len(found) == limit:
            break
    return found


def render_source_structure(blocks: list[tuple[str, str]]) -> str:
    lines: list[str] = []
    for kind, value in blocks:
        if kind == "heading":
            clean = literalize_html_tags(value.lstrip("# ").strip())
            if clean:
                lines.extend([f"### {clean}", ""])
        elif kind == "code":
            clipped = value[:8000]
            clipped = "\n".join(line.rstrip() for line in clipped.splitlines()).strip()
            lines.extend([f"```{code_language(clipped)}", clipped, "```", ""])
            if len(value) > len(clipped):
                lines.extend(["> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.", ""])
        else:
            if value:
                # Blog prose can contain NumPy-like [[...]] values; make them literal so
                # Obsidian never turns source data into phantom graph links.
                literal = literalize_html_tags(value).replace("[[", r"\[\[").replace("]]", r"\]\]")
                lines.extend([literal, ""])
    return "\n".join(lines).strip()


def related_section(old_body: str) -> str:
    marker = "## 관련 글"
    pos = old_body.find(marker)
    return old_body[pos:].strip() if pos >= 0 else ""


def template_sections(note_type: str, blocks: list[tuple[str, str]]) -> tuple[str, str]:
    if note_type == "tutorial":
        return "## 학습 목표 및 맥락", "## 원문 기반 학습 정리"
    if note_type == "troubleshooting":
        return "## 문제·재현 맥락", "## 원인·해결 근거"
    if note_type == "project":
        return "## 배경·목표·적용 맥락", "## 구현·의사결정·결과"
    if note_type == "concept":
        return "## 핵심 개념과 선택 맥락", "## 원문 기반 개념 정리"
    return "## 적용 목적과 전제조건", "## 구현 절차·검증·주의점"


def split_note(text: str) -> tuple[str, str]:
    match = re.match(r"\A(---\n.*?\n---\n*)(.*)\Z", text, re.S)
    if not match:
        raise ValueError("YAML frontmatter is required")
    return match.group(1), match.group(2)


def render_note(frontmatter: str, old_body: str, title: str, note_type: str, blocks: list[tuple[str, str]]) -> str:
    intro_heading, detail_heading = template_sections(note_type, blocks)
    intro = "\n\n".join(opening_texts(blocks)) or "원문에서 추출한 학습·구현 내용을 구조화했습니다."
    intro = intro.replace("[[", r"\[\[").replace("]]", r"\]\]")
    detail = render_source_structure(blocks) or "원문 본문을 구조적으로 추출하지 못했습니다. 원문 링크를 확인하세요."
    related = related_section(old_body)
    original_url = source_url(frontmatter)
    sections = [
        f"# {title}",
        f"## 원문\n\n{original_url}" if original_url else "",
        f"## 노트 유형\n\n`{note_type}`",
        f"{intro_heading}\n\n{intro}",
        f"{detail_heading}\n\n{detail}",
    ]
    if related:
        sections.append(related)
    return frontmatter + "\n\n".join(sections).strip() + "\n"


def source_url(text: str) -> str:
    match = re.search(r"^source_url:\s*(https://ch010104\.tistory\.com/\d+)\s*$", text, re.M)
    return match.group(1) if match else ""


def title_of(frontmatter: str, fallback: str) -> str:
    match = re.search(r'^title:\s*"(.*)"\s*$', frontmatter, re.M)
    return html.unescape(match.group(1)) if match else fallback


def enrich_one(path: Path) -> tuple[str, str]:
    original = path.read_text(encoding="utf-8")
    frontmatter, old_body = split_note(original)
    url = source_url(frontmatter)
    if not url:
        return "skipped", str(path)
    source = fetch(url)
    blocks = body_blocks(source)
    category_match = re.search(r'^category:\s*"(.*)"\s*$', frontmatter, re.M)
    category = category_match.group(1) if category_match else ""
    title = title_of(frontmatter, path.stem)
    note_type = classify_post(title, category, blocks)
    rendered = render_note(frontmatter, old_body, title, note_type, blocks)
    if rendered != original:
        path.write_text(rendered, encoding="utf-8")
        return note_type, str(path)
    return "unchanged", str(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write enriched bodies")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    paths = sorted(path for path in BLOG.rglob("*.md") if path.name != "index.md")
    if args.limit:
        paths = paths[:args.limit]
    if not args.apply:
        print(f"DRY_RUN posts={len(paths)}; use --apply to update bodies")
        return
    results: Counter[str] = Counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for kind, path in pool.map(enrich_one, paths):
            results[kind] += 1
            print(f"{kind}: {path}", flush=True)
    print("DONE " + " ".join(f"{kind}={count}" for kind, count in sorted(results.items())))


if __name__ == "__main__":
    main()
