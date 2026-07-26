#!/usr/bin/env python3
"""Normalize Notion-exported Markdown for GitHub and Obsidian rendering."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

TABLE_RE = re.compile(r'<table\b[^>]*>(?P<body>.*?)</table>', re.IGNORECASE | re.DOTALL)
ROW_RE = re.compile(r'<tr\b[^>]*>(?P<body>.*?)</tr>', re.IGNORECASE | re.DOTALL)
CELL_RE = re.compile(r'<td\b[^>]*>(?P<body>.*?)</td>', re.IGNORECASE | re.DOTALL)
FENCE_RE = re.compile(r'^```.*$', re.MULTILINE)
LANGUAGE_MARKER_RE = re.compile(r'(?m)^(?P<lang>html|css|javascript|js)\s*\n(?=```(?P=lang)\b)')
HTML_OPEN_RE = re.compile(r'^\s*<(?P<tag>html|head|body|div|span|p|h[1-6]|ul|ol|li|form|section|article)\b[^>]*>', re.IGNORECASE)


def cell_text(value: str) -> str:
    value = re.sub(r'\s*\n\s*', '<br>', value.strip())
    return value.replace('|', r'\|')


def render_table(match: re.Match[str]) -> str:
    rows = [
        [cell_text(cell) for cell in CELL_RE.findall(row)]
        for row in ROW_RE.findall(match.group('body'))
    ]
    rows = [row for row in rows if row]
    if not rows:
        return match.group(0)
    width = max(len(row) for row in rows)
    rows = [row + [''] * (width - len(row)) for row in rows]
    header, data = rows[0], rows[1:]
    lines = [
        '| ' + ' | '.join(header) + ' |',
        '| ' + ' | '.join(['---'] * width) + ' |',
        *['| ' + ' | '.join(row) + ' |' for row in data],
    ]
    return '\n'.join(lines)


def fence_raw_html_examples(value: str) -> str:
    lines = value.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        match = HTML_OPEN_RE.match(lines[index])
        if not match:
            output.append(lines[index])
            index += 1
            continue
        tag = match.group('tag')
        block = [lines[index]]
        index += 1
        closing = re.compile(rf'</{re.escape(tag)}>\s*$', re.IGNORECASE)
        while index < len(lines):
            block.append(lines[index])
            if closing.search(lines[index]):
                index += 1
                break
            index += 1
        output.extend(['```html\n', *block])
        if not block[-1].endswith('\n'):
            output.append('\n')
        output.append('```\n')
    return ''.join(output)


def normalize_outside_fences(value: str) -> str:
    value = TABLE_RE.sub(render_table, value)
    value = LANGUAGE_MARKER_RE.sub('', value)
    return fence_raw_html_examples(value)


def normalize_markdown(markdown: str) -> str:
    chunks: list[str] = []
    current: list[str] = []
    fenced = False
    for line in markdown.splitlines(keepends=True):
        if line.lstrip().startswith('```'):
            if not fenced:
                chunks.append(normalize_outside_fences(''.join(current)))
                current = [line]
                fenced = True
            else:
                current.append(line)
                chunks.append(''.join(current))
                current = []
                fenced = False
            continue
        current.append(line)
    chunks.append(''.join(current) if fenced else normalize_outside_fences(''.join(current)))
    return LANGUAGE_MARKER_RE.sub('', ''.join(chunks))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=Path)
    parser.add_argument('--root', type=Path, default=Path('notion/SKALA'))
    args = parser.parse_args()
    paths = [args.path] if args.path else sorted(args.root.rglob('*.md'))
    changed = 0
    for path in paths:
        original = path.read_text(encoding='utf-8')
        normalized = normalize_markdown(original)
        if normalized != original:
            path.write_text(normalized, encoding='utf-8')
            changed += 1
    print(f'changed={changed}')


if __name__ == '__main__':
    main()
