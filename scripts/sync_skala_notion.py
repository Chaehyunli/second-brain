#!/usr/bin/env python3
"""Deterministically mirror new, complete SKALA Notion learning leaves.

The script deliberately keeps Notion JSON in a private run directory and emits
only concise operational outcomes. Existing page IDs are immutable.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

ROOT_ID = "39d1d84b-f68e-80f3-89b7-e70a6c911bf9"
ADMIN_WORDS = (
    "attendance", "출결", "출석", "모바일", "보안서약", "일정", "스케줄", "캠퍼스",
    "식사", "운영", "수당", "수료", "연락처", "certificate", "contact", "allowance",
)
SIGNED_URL_RE = re.compile(r"(?:X-Amz-(?:Algorithm|Credential|Date|Expires|Security-Token|Signature)|[?&](?:signature|expires|token)=)", re.I)
UNSAFE_COMPONENT_RE = re.compile(r'[\\/:*?"<>|]')
NOTION_ID_RE = re.compile(r"^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$", re.I)
CONTENT_RE = re.compile(r"<content\b[^>]*>(.*?)</content>", re.I | re.S)


@dataclass(frozen=True)
class Leaf:
    page_id: str
    title: str
    parents: tuple[str, ...]
    in_padlet: bool


def safe_component(title: str) -> str:
    """Map a Notion hierarchy title to a portable Vault component."""
    value = title.replace("[", "").replace("]", "")
    value = UNSAFE_COMPONENT_RE.sub("-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value or "untitled"


def is_scope_excluded(title: str, *, in_padlet: bool) -> bool:
    lower = title.casefold()
    if "(수정중)" in title:
        return True
    if in_padlet:
        return False
    return title == "[7/14] OT" or any(word in lower for word in ADMIN_WORDS)


def remove_temporary_signed_url_lines(markdown: str) -> str:
    """Discard only lines whose URL is demonstrably ephemeral signed media."""
    return "".join(line for line in markdown.splitlines(keepends=True) if not SIGNED_URL_RE.search(line))


def normalize_id(value: str) -> str:
    raw = value.replace("-", "").lower()
    if not re.fullmatch(r"[0-9a-f]{32}", raw):
        raise ValueError("invalid Notion page ID")
    return f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"


def ntn_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update({"HOME": "/var/lib/hermes", "HERMES_HOME": "/root/.hermes", "NOTION_KEYRING": "0"})
    return env


def call_ntn_json(path: str, output: Path, *, query: Iterable[str] = ()) -> dict[str, Any]:
    """Call ntn without a shell and retain its JSON only in the run directory."""
    command = ["ntn", "api", path, *query]
    with output.open("wb") as handle:
        result = subprocess.run(command, env=ntn_env(), stdout=handle, stderr=subprocess.PIPE, check=False)
    if result.returncode:
        raise RuntimeError(f"ntn exit {result.returncode}")
    try:
        return json.loads(output.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError("invalid Notion JSON") from exc


def child_pages(page_id: str, run_dir: Path) -> list[tuple[str, str]]:
    cursor: str | None = None
    children: list[tuple[str, str]] = []
    page = 0
    while True:
        query = ["page_size==100"]
        if cursor:
            query.append(f"start_cursor=={cursor}")
        payload = call_ntn_json(f"v1/blocks/{page_id}/children", run_dir / f"children-{page_id}-{page}.json", query=query)
        for item in payload.get("results", []):
            if item.get("type") == "child_page":
                child = item.get("child_page", {})
                child_id = item.get("id", "")
                title = child.get("title", "")
                if NOTION_ID_RE.fullmatch(child_id) and isinstance(title, str) and title.strip():
                    children.append((normalize_id(child_id), title.strip()))
        if not payload.get("has_more"):
            return children
        cursor = payload.get("next_cursor")
        if not isinstance(cursor, str) or not cursor:
            raise RuntimeError("child pagination cursor missing")
        page += 1


def discover_leaves(run_dir: Path) -> list[Leaf]:
    leaves: list[Leaf] = []

    def walk(page_id: str, parents: tuple[str, ...], in_padlet: bool) -> None:
        children = child_pages(page_id, run_dir)
        if not children:
            if parents:
                leaves.append(Leaf(page_id, parents[-1], parents[:-1], in_padlet))
            return
        for child_id, title in children:
            walk(child_id, (*parents, title), in_padlet or title == "Padlet")

    walk(ROOT_ID, (), False)
    return leaves


def existing_page_ids(skala_root: Path) -> set[str]:
    result: set[str] = set()
    for note in skala_root.rglob("*.md"):
        match = re.search(r'^notion_page_id:\s*"?([^"\n]+)', note.read_text(encoding="utf-8"), re.M)
        if not match:
            continue
        try:
            result.add(normalize_id(match.group(1)))
        except ValueError:
            continue
    return result


def retained_markdown(payload: dict[str, Any]) -> str:
    if payload.get("truncated") is not False or payload.get("unknown_block_ids") != []:
        raise ValueError("source incomplete")
    markdown = payload.get("markdown")
    if not isinstance(markdown, str):
        raise ValueError("markdown missing")
    match = CONTENT_RE.search(markdown)
    body = match.group(1) if match else markdown
    if body.startswith("---\n"):
        parts = body.split("---", 2)
        if len(parts) == 3:
            body = parts[2].lstrip("\n")
    body = remove_temporary_signed_url_lines(body).strip()
    if not body:
        raise ValueError("empty learning source")
    return body + "\n"


def note_path(vault: Path, leaf: Leaf) -> Path:
    parent_parts = [safe_component(title) for title in leaf.parents]
    date_match = next((re.match(r"\[?(\d{1,2})/(\d{1,2})\]?", title) for title in leaf.parents), None)
    filename = safe_component(leaf.title)
    if date_match and not re.match(r"\d{1,2}-\d{1,2}\b", filename):
        filename = f"{date_match.group(1)}-{date_match.group(2)} {filename}"
    return vault / "notion" / "SKALA" / Path(*parent_parts) / f"{filename}.md"


def source_url(page_id: str) -> str:
    return f"https://app.notion.com/p/{page_id.replace('-', '')}"


def render_note(leaf: Leaf, body: str) -> str:
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    stamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return (
        f'---\ntitle: "{leaf.title.replace(chr(34), chr(39))}"\n'
        f'notion_page_id: "{leaf.page_id}"\nsource_url: "{source_url(leaf.page_id)}"\n'
        f'content_sha256: "{digest}"\nsynced_at: "{stamp}"\n---\n\n'
        f"# {leaf.title}\n\n## 원문\n\n[Notion 원문]({source_url(leaf.page_id)})\n\n"
        f"{body}\n## 연결\n\n- [[notion/SKALA/index|SKALA 학습 노트]]\n"
    )


def append_index(index: Path, leaf: Leaf, note: Path, vault: Path) -> None:
    target = note.relative_to(vault).with_suffix("").as_posix()
    link = f"[[{target}]]"
    text = index.read_text(encoding="utf-8")
    if link in text:
        return
    heading = leaf.parents[-1] if leaf.parents else leaf.title
    suffix = "" if text.endswith("\n") else "\n"
    index.write_text(f"{text}{suffix}\n## {heading}\n\n- {link}\n", encoding="utf-8")


def clean_worktree(vault: Path) -> bool:
    result = subprocess.run(["git", "status", "--porcelain"], cwd=vault, text=True, capture_output=True, check=True)
    return not result.stdout.strip()


def locked(vault: Path, args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(vault / "scripts/vault_sync_lock.sh"), *args], cwd=vault, text=True, capture_output=True, env=env, check=False)


def concise(leaf: Leaf, reason: str) -> None:
    print(f"SKALA 오류: {leaf.title} | {leaf.page_id} | {reason}")


def write_manifest(run_dir: Path, *, reason: str, leaf: Leaf | None = None) -> None:
    data: dict[str, str] = {"reason": reason}
    if leaf:
        data.update({"title": leaf.title, "page_id": leaf.page_id})
    (run_dir / "manifest.json").write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")


def commit_leaf(vault: Path, leaf: Leaf, paths: list[Path]) -> str:
    relative = [str(path.relative_to(vault)) for path in paths]
    env = os.environ.copy()
    env["COMMIT_MESSAGE"] = f"노션: SKALA - {leaf.title} 업데이트"
    script = (
        'git add -- "$@" && python3 scripts/validate_vault_contract.py --changed-from-index --strict '
        '&& git commit -m "$COMMIT_MESSAGE" && git push origin main'
    )
    result = locked(vault, ["bash", "-c", script, "sync-skala", *relative], env=env)
    if result.returncode:
        raise RuntimeError("git transaction failed")
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=vault, text=True, capture_output=True, check=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    vault = args.vault.resolve()
    run_dir = Path(tempfile.mkdtemp(prefix="skala-sync-", dir="/var/lib/hermes/tmp"))
    run_dir.chmod(0o700)
    failed = False
    try:
        if not clean_worktree(vault):
            print("SKALA 보류: Vault 작업 트리가 깨끗하지 않습니다.")
            return 2
        pull = locked(vault, ["git", "pull", "--ff-only", "origin", "main"])
        if pull.returncode or not clean_worktree(vault):
            print("SKALA 보류: Vault 동기화 또는 작업 트리 확인에 실패했습니다.")
            return 2
        validation = subprocess.run([sys.executable, "scripts/validate_skala_sync.py"], cwd=vault, capture_output=True, text=True)
        if validation.returncode:
            print("SKALA 보류: 기존 SKALA ID 검증 실패")
            return 2
        known = existing_page_ids(vault / "notion" / "SKALA")
        for leaf in discover_leaves(run_dir):
            if leaf.page_id in known or is_scope_excluded(leaf.title, in_padlet=leaf.in_padlet):
                continue
            try:
                payload = call_ntn_json(f"v1/pages/{leaf.page_id}/markdown", run_dir / f"page-{leaf.page_id}.json")
                body = retained_markdown(payload)
            except (RuntimeError, ValueError) as exc:
                failed = True
                concise(leaf, str(exc))
                write_manifest(run_dir, reason=str(exc), leaf=leaf)
                continue
            note = note_path(vault, leaf)
            if note.exists():
                failed = True
                concise(leaf, "destination already exists")
                write_manifest(run_dir, reason="destination already exists", leaf=leaf)
                continue
            note.parent.mkdir(parents=True, exist_ok=True)
            note.write_text(render_note(leaf, body), encoding="utf-8")
            normalized = subprocess.run([sys.executable, "scripts/normalize_skala_markdown.py", "--path", str(note)], cwd=vault, capture_output=True, text=True)
            if normalized.returncode:
                note.unlink(missing_ok=True)
                failed = True
                concise(leaf, "markdown normalization failed")
                write_manifest(run_dir, reason="markdown normalization failed", leaf=leaf)
                continue
            index = vault / "notion/SKALA/index.md"
            index_before = index.read_text(encoding="utf-8")
            append_index(index, leaf, note, vault)
            check = subprocess.run([sys.executable, "scripts/validate_skala_sync.py"], cwd=vault, capture_output=True, text=True)
            if check.returncode:
                note.unlink(missing_ok=True)
                index.write_text(index_before, encoding="utf-8")
                failed = True
                concise(leaf, "SKALA validation failed")
                write_manifest(run_dir, reason="SKALA validation failed", leaf=leaf)
                continue
            try:
                sha = commit_leaf(vault, leaf, [note, index])
            except RuntimeError as exc:
                failed = True
                concise(leaf, str(exc))
                write_manifest(run_dir, reason=str(exc), leaf=leaf)
                return 2
            print(f"SKALA 동기화: {leaf.title} | {sha}")
            known.add(leaf.page_id)
        return 1 if failed else 0
    finally:
        if not failed:
            shutil.rmtree(run_dir)


if __name__ == "__main__":
    raise SystemExit(main())
