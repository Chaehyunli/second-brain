#!/usr/bin/env python3
"""Synchronize new and changed Tistory posts using one compact hash manifest."""
from __future__ import annotations

import concurrent.futures
import re
import subprocess
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from archive_note_images import append_image_section
from archive_tistory_images import safe_slug
from relocate_note_images import relocate_note
from enrich_tistory_blog_bodies import (
    body_blocks,
    classify_post,
    fetch,
    literalize_html_tags_in_markdown,
    render_note,
    split_note,
)
from rebuild_tistory_blog import category_of, meta, quote, safe_name, tags_of
from sync_new_tistory_posts import (
    ROOT,
    rebuild_category_index,
    rebuild_root_index,
    replace_front_value,
    make_post,
)
from tistory_content_hashes import changed_urls, content_hash, load_manifest, save_manifest

BLOG = ROOT / "blog"
MANIFEST = ROOT / "scripts" / "tistory_content_hashes.json"
URL_RE = re.compile(r"^source_url:\s*(https://ch010104\.tistory\.com/\d+)\s*$", re.M)


@dataclass(frozen=True)
class Snapshot:
    url: str
    title: str
    category: str
    published: str
    tags: list[str]
    blocks: list[tuple[str, str]]
    digest: str


def snapshot(url: str) -> Snapshot:
    source = fetch(url)
    title = re.sub(r"\s*::\s*소소한 지식 저장소\s*$", "", meta(source, "og:title")).strip()
    blocks = body_blocks(source)
    return Snapshot(
        url=url,
        title=title,
        category=category_of(source, title),
        published=meta(source, "article:published_time")[:10] or date.today().isoformat(),
        tags=["blog", "technical-writing", *tags_of(source)],
        blocks=blocks,
        digest=content_hash(title, blocks),
    )


def render_changed_note(
    original: str,
    *,
    title: str,
    category: str,
    tags: list[str],
    published: str,
    blocks: list[tuple[str, str]],
) -> str:
    frontmatter, old_body = split_note(original)
    current_category = re.search(r'^category:\s*"(.*)"\s*$', frontmatter, re.M)
    category = current_category.group(1) if current_category else category
    for key, value in (
        ("title", f'"{quote(title)}"'),
        ("updated", date.today().isoformat()),
    ):
        frontmatter = replace_front_value(frontmatter, key, value)
    note_type = classify_post(title, category, blocks)
    return literalize_html_tags_in_markdown(render_note(frontmatter, old_body, title, note_type, blocks))


def update_title_only(original: str, title: str) -> str:
    """Repair local title drift without rewriting the archived body or metadata."""
    frontmatter, body = split_note(original)
    frontmatter = replace_front_value(frontmatter, "title", f'"{quote(title)}"')
    body, replacements = re.subn(r"^# .+$", f"# {title}", body, count=1, flags=re.MULTILINE)
    if replacements != 1:
        raise ValueError("archived note is missing a single H1 title")
    return f"{frontmatter}{body}"


def rename_note_to_title(path: Path, title: str, blog_root: Path = BLOG, vault_root: Path = ROOT) -> Path:
    """Rename an archive note from its canonical title and repair explicit inbound wikilinks."""
    target = path.with_name(f"{safe_name(title)}.md")
    if target == path:
        return path
    if target.exists():
        raise FileExistsError(f"title-derived path already exists: {target}")
    old_link = f"blog/{path.relative_to(blog_root).with_suffix('').as_posix()}"
    new_link = f"blog/{target.relative_to(blog_root).with_suffix('').as_posix()}"
    path.rename(target)
    link_pattern = re.compile(rf"\[\[{re.escape(old_link)}(?=\| |\||\]\])")
    for candidate in vault_root.rglob("*.md"):
        text = candidate.read_text(encoding="utf-8")
        updated = link_pattern.sub(f"[[{new_link}", text)
        if updated != text:
            candidate.write_text(updated, encoding="utf-8")
    return target


def title_drift_urls(local: dict[str, Path], observed: dict[str, Snapshot]) -> list[str]:
    """Find local notes whose displayed title does not match the live source."""
    drifted: list[str] = []
    for url, path in local.items():
        item = observed.get(url)
        if item is None:
            continue
        text = path.read_text(encoding="utf-8")
        expected_frontmatter = f'title: "{quote(item.title)}"'
        expected_h1 = f"# {item.title}"
        if expected_frontmatter not in text or expected_h1 not in text:
            drifted.append(url)
    return sorted(drifted)


def restore_local_images(note: Path) -> int:
    """Reinsert already archived local images using their recorded source context."""
    manifest = note.parent / "assets" / safe_slug(note.stem) / "SOURCE.txt"
    if not manifest.exists():
        return 0
    entries = [
        (f"assets/{manifest.parent.name}/{match.group('file')}", match.group("context"))
        for match in re.finditer(r"^- file: (?P<file>.+)\n  context: (?P<context>.+)$", manifest.read_text(encoding="utf-8"), re.MULTILINE)
        if (manifest.parent / match.group("file")).is_file()
    ]
    if not entries:
        return 0
    append_image_section(note, entries)
    return relocate_note(note).placed


def local_notes() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in BLOG.rglob("*.md"):
        if path.name == "index.md":
            continue
        match = URL_RE.search(path.read_text(encoding="utf-8"))
        if match:
            found[match.group(1)] = path
    return found


def remote_urls() -> list[str]:
    sitemap = subprocess.run(
        ["curl", "-fsSL", "--max-time", "30", "https://ch010104.tistory.com/sitemap.xml"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return sorted(set(re.findall(r"https://ch010104\.tistory\.com/\d+", sitemap)), key=lambda url: int(url.rsplit("/", 1)[1]))


def collect(urls: list[str]) -> tuple[dict[str, Snapshot], list[str]]:
    snapshots: dict[str, Snapshot] = {}
    errors: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(snapshot, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                snapshots[url] = future.result()
            except Exception as exc:
                errors.append(f"{url}: {type(exc).__name__}: {exc}")
    return snapshots, sorted(errors)


def plan_updates(
    previous: dict[str, str],
    observed: dict[str, str],
    local: dict[str, Path],
) -> tuple[list[str], list[str], list[str]]:
    changed, added = changed_urls(previous, observed)
    new = [url for url in added if url not in local]
    baseline = [url for url in added if url in local]
    return changed, new, baseline


def main() -> None:
    urls = remote_urls()
    observed, errors = collect(urls)
    if errors:
        for error in errors:
            print(f"WARN {error}")
    if not observed:
        raise SystemExit("no Tistory posts could be fetched; manifest unchanged")

    previous = load_manifest(MANIFEST)
    observed_hashes = {url: item.digest for url, item in observed.items()}
    if not previous:
        save_manifest(MANIFEST, observed_hashes)
        print(f"baseline={len(observed_hashes)} changed=0 added=0 errors={len(errors)}")
        return

    notes = local_notes()
    changed, added, baseline = plan_updates(previous, observed_hashes, notes)
    title_drift = [url for url in title_drift_urls(notes, observed) if url not in changed]
    updated = 0
    title_fixed = 0
    filename_fixed = 0
    added_categories: set[str] = set()
    reindex_categories: set[str] = set()
    for url in changed:
        path = notes.get(url)
        if path is None:
            errors.append(f"{url}: archived note not found")
            continue
        item = observed[url]
        path.write_text(render_changed_note(
            path.read_text(encoding="utf-8"),
            title=item.title,
            category=item.category,
            tags=item.tags,
            published=item.published,
            blocks=item.blocks,
        ), encoding="utf-8")
        restore_local_images(path)
        renamed = rename_note_to_title(path, item.title)
        if renamed != path:
            filename_fixed += 1
        category_match = re.search(r'^category:\s*"(.*)"\s*$', renamed.read_text(encoding="utf-8"), re.M)
        if category_match:
            reindex_categories.add(category_match.group(1))
        updated += 1
    for url in title_drift:
        path = notes[url]
        path.write_text(update_title_only(path.read_text(encoding="utf-8"), observed[url].title), encoding="utf-8")
        title_fixed += 1
        renamed = rename_note_to_title(path, observed[url].title)
        if renamed != path:
            filename_fixed += 1
        category_match = re.search(r'^category:\s*"(.*)"\s*$', renamed.read_text(encoding="utf-8"), re.M)
        if category_match:
            reindex_categories.add(category_match.group(1))
    for url in added:
        category, _ = make_post(url)
        added_categories.add(category)
    for category in sorted(added_categories | reindex_categories):
        rebuild_category_index(category)
    if added_categories:
        rebuild_root_index()

    successful = set(observed_hashes) - {error.split(":", 1)[0] for error in errors}
    merged = {**previous, **{url: observed_hashes[url] for url in successful}}
    if merged != previous:
        save_manifest(MANIFEST, merged)
    print(f"baseline={len(baseline)} changed={updated} title_fixed={title_fixed} filename_fixed={filename_fixed} added={len(added)} errors={len(errors)}")


if __name__ == "__main__":
    main()
