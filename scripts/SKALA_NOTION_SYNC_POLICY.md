# SKALA Notion → Obsidian daily sync policy

- Source root: Notion `SKALA` page `39d1d84b-f68e-80f3-89b7-e70a6c911bf9`.
- Scope: recursively discover and sync all descendant pages. Do not follow pages outside this ancestor tree.
- Destination: `notion/SKALA/` in this Vault. One Notion page maps to one Markdown note with `notion_page_id`, source URL, title, sync timestamp, and `content_sha256` in frontmatter.
- Preserve the page's meaningful Markdown content and original Notion URL. Do not archive temporary signed image URLs as durable evidence; retain stable text and page references.
- Extract only the Notion `<content>` region, remove temporary signed-image URLs, normalize whitespace, then calculate `content_sha256` from that source text. Compare this source hash before writing: update only newly discovered or changed pages. A missing hash is a one-time baseline migration. Never delete a local note merely because a remote page is unavailable or removed.
- Rebuild `notion/SKALA/index.md` with links to the synced notes.
- Safety: stop before writing or committing if `git status --porcelain` reports unrelated local changes. Do not use reset or force push.
- Commit every changed page separately and use its exact Notion title: `노션: SKALA - <페이지 제목> 업데이트`. If only the hub/index changes, use `노션: SKALA - SKALA 인덱스 업데이트`.
- Push each successful commit to `origin/main`. If no page changed, make no commit and return no user-facing report.
