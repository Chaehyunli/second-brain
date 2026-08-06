# Knowledge Wiki Layer Implementation Plan

> **For Hermes:** Use the existing Vault transaction contract; implement in small, verified commits rather than restructuring the existing source archives.

**Goal:** Preserve the current source-governed Vault while adding (1) cross-source concept notes, (2) a visible Inbox → review → canonical workflow, and (3) a scheduled knowledge-health audit.

**Architecture:** Keep `blog/`, `notion/SKALA/`, `notion/Information/`, `entities/`, and `raw/` as authoritative source or evidence collections. Add a separate, curated `knowledge/` layer for reusable concepts and decisions that link back to those sources. Treat `inbox/` as the only intake/staging area for unreviewed web captures and AI drafts; do not route already-approved Notion/Tistory mirrors through it.

**Tech stack:** Markdown, Obsidian wikilinks, Python standard library, existing Vault scripts, Git/GitHub, Hermes cron.

---

## Design decisions

### Do not flatten or migrate current folders
The LLM-Wiki article's `raw/` and `wiki/` layout is a useful operating model, but moving the existing archive into it would lose useful source semantics and would create unnecessary filename/link churn.

Use this target model instead:

```text
raw/                 immutable evidence and source manifests
inbox/               unreviewed captures and AI drafts only
blog/                canonical Tistory archive
notion/SKALA/        canonical learning-note mirror
notion/Information/  canonical Notion mirror
entities/            verified projects, experience, awards
knowledge/           curated cross-source concepts and decisions
```

### Concept notes are not source mirrors
A `knowledge/` note must explain one reusable concept, decision pattern, or practical relationship. It must link to the originating SKALA/blog/entity notes and distinguish source facts from the curated interpretation. Do not create one concept note per source note automatically.

### Inbox promotion is explicit
An Inbox item begins as `review_status: pending`. Automation may capture, classify, suggest links, and surface it in a review report, but may not silently mark it verified, delete it, or move it to `knowledge/` / `entities/`.

### Health checks report before changing
The weekly health job is read-only by default. It produces a report with candidates and evidence; it does not rewrite links, merge notes, change source metadata, or delete files. Any repair becomes a separate, reviewed transaction.

---

## Phase 1 — Add the cross-source `knowledge/` layer

### Task 1: Define the concept-note contract

**Objective:** Add one clear contract for the curated layer without changing existing source-note contracts.

**Files:**
- Modify: `SCHEMA.md`
- Modify: `agent.md` (therefore align the compatibility entry points as already required)
- Create: `knowledge/README.md`

**Implementation:**
1. Add a `knowledge-note` metadata contract with:
   ```yaml
   schema_version: 1
   id: knowledge-<stable-slug>
   title:
   type: knowledge-note
   status: draft # draft | verified | needs-review | superseded
   created:
   updated:
   tags: []
   sources: []
   checked_at:
   ```
2. Define required sections: `## 핵심`, `## 연결된 근거`, `## 적용 기준`, `## 주의점 또는 한계`.
3. Require at least two resolved links: one source/evidence note and one genuinely related concept or entity note. Allow a single link only for an explicitly marked seed note.
4. State that canonical source notes remain immutable under their existing source policies; concept notes must never overwrite or relabel their provenance.

**Verification:**
- Confirm `agent.md`, `AGENTS.md`, and `CLAUDE.md` remain byte-identical where the existing compatibility contract requires it.
- Run `python3 scripts/validate_vault_contract.py --strict`.

### Task 2: Create a deliberately small seed set

**Objective:** Demonstrate the layer with 3–5 high-value notes, not a bulk AI-generated encyclopedia.

**Initial candidate set:**
- Vue application composition: Router + Pinia + Axios + Element Plus
- Source-driven technical learning: SKALA 기준본 → public blog derivative
- Evidence-grounded portfolio narrative: problem → role → decision → verification

**Files:**
- Create: `knowledge/vue-application-composition.md`
- Create: `knowledge/source-to-public-technical-writing.md`
- Create: `knowledge/evidence-grounded-portfolio-narrative.md`
- Modify: `knowledge/README.md`
- Modify: `index.md` only if its existing index convention permits a Knowledge entry point

**Implementation:**
1. Read the linked canonical sources first; do not infer from filenames alone.
2. Write only the common, reusable abstraction and visibly link each source.
3. Add one explicit “not implied”/limitation statement when a source supports a narrow context only.
4. Link the three seed notes from `knowledge/README.md`; do not add a second global index yet.

**Verification:**
- Validate every explicit wiki link resolves.
- Run the Vault contract validator on staged files.
- Review the notes manually for duplicated source-body text; they should add synthesis, not copy archives.

### Task 3: Add a conservative concept-candidate report

**Objective:** Let automation suggest cross-source concepts without automatically creating speculative knowledge notes.

### Operating owner: Hermes Knowledge Curator

The `knowledge/` layer needs an explicit owner; it must not be a folder that is created once and then forgotten. The owner is a dedicated **Hermes/Codex scheduled curator job** running on the VPS, not Obsidian itself.

- **Daily, after Tistory → SKALA → Information sync:** read source deltas and refresh a candidate queue. It never rewrites source archives and remains silent when there is no actionable candidate.
- **Weekly:** review the candidate queue and health report. It may make only safe, evidence-preserving updates to an existing `knowledge/` note (append a dated, source-linked section; refresh `checked_at`; repair an explicit link). It must create a new note, merge concepts, revise an interpretation, or promote Inbox material only when the user has approved that category of automation or has explicitly reviewed the candidate.
- **Human role:** approve ambiguous interpretation, portfolio claims, personal takeaways, and Inbox promotion. The curator reports exactly which source notes support every proposed or completed update.

This separates continuous maintenance from editorial judgement: the agent maintains freshness and traceability; the user retains authority over meaning and personal conclusions.

**Files:**
- Create: `scripts/report_knowledge_candidates.py`
- Create: `tests/test_report_knowledge_candidates.py`
- Create: `reports/knowledge/README.md` (report output contract; generated reports themselves remain ignored or untracked according to the decided policy)

**Implementation:**
1. Read frontmatter/title/tags and resolved wikilinks from source notes.
2. Produce candidates only when at least two distinct source domains share explicit tags or direct declared relationships.
3. Include candidate title, source paths, source URLs/IDs, overlap evidence, and a `review_required: true` marker.
4. Do not create or edit `knowledge/*.md`.

**Tests:**
- Same keyword in unrelated notes must not produce a candidate.
- Two explicit related sources must produce one review candidate.
- Fenced code and URLs must not be interpreted as wikilinks.
- A source with missing provenance is reported, not treated as verified evidence.

---

## Phase 2 — Make Inbox a visible intake and review workflow

### Task 4: Add Inbox manifest and review queue generation

**Objective:** Make incoming material discoverable without changing the current safety rule that automation cannot silently promote it.

**Files:**
- Create: `scripts/build_inbox_review_queue.py`
- Create: `tests/test_build_inbox_review_queue.py`
- Create: `inbox/REVIEW_QUEUE.md` as generated, non-canonical output (or add it to `.gitignore` if the user prefers it never be versioned)
- Modify: `inbox/README.md`

**Implementation:**
1. Parse all Inbox Markdown frontmatter.
2. Require `captured_at`, `review_status`, `agent_generated`, and source provenance.
3. Group queue items by `pending`, `needs-source`, `needs-classification`, and `ready-for-review`.
4. Flag missing required metadata; never repair it automatically.
5. List likely related notes only as suggestions with evidence, never as automatic links.

**Tests:**
- Pending note appears in the queue.
- Verified item does not appear as pending.
- Missing source URL is flagged.
- Duplicate canonical URL is flagged for human review, not deleted.

### Task 5: Define human-approved promotion commands

**Objective:** Make “review then promote” predictable and reversible.

**Files:**
- Create: `scripts/promote_inbox_note.py`
- Create: `tests/test_promote_inbox_note.py`
- Modify: `inbox/README.md`
- Modify: `SCHEMA.md`

**Implementation:**
1. Require an explicit target type (`knowledge-note`, `research-note`, or another existing canonical type) and destination path.
2. Require `--approve` plus a review note; no default promotion action.
3. Preserve source URL, capture time, and review history in frontmatter.
4. Refuse promotion if the target path already exists, required fields are absent, or the Git tree is dirty.
5. Use the Vault lock, stage only affected files, validate, commit, and push as a single transaction.

**Tests:**
- Missing `--approve` refuses with no file changes.
- Existing destination refuses safely.
- Successful promotion preserves original source metadata.
- Dirty tree refuses before mutation.

### Task 6: Add a low-noise Inbox reminder

**Objective:** Surface reviewable material without creating daily noise.

**Automation behavior:**
- Run daily at KST 00:15, after the Tistory (00:00), SKALA (00:05), and Information (00:10) source synchronization jobs.
- Deliver only when one or more pending items have existed for at least 7 days, or when new items require source/classification review.
- Otherwise return `[SILENT]`.

**Files/configuration:**
- Create: `/root/.hermes/scripts/inbox_review_reminder.sh` or a read-only Python script outside the Vault as appropriate.
- Create one Hermes cron job with `/root/wiki` workdir and no Git mutation.

**Verification:**
- Empty Inbox generates no delivery.
- One stale pending fixture generates a concise report with source links.

---

## Phase 3 — Introduce a scheduled knowledge health check

### Task 7: Build a read-only health auditor

**Objective:** Replace ad-hoc inspection with an explicit weekly report that distinguishes source freshness, graph quality, and review backlog.

**Files:**
- Create: `scripts/audit_knowledge_health.py`
- Create: `tests/test_audit_knowledge_health.py`
- Create: `reports/knowledge-health/README.md`

**Audit checks:**
1. **Source freshness:** last successful Tistory, SKALA, and Information cron outputs; compare with tracked source IDs/hashes where each source contract supports it.
2. **Synchronization health:** identify job errors, lock contention, auth failures, and a scheduler `ok` result without evidence of a source check.
3. **Link health:** unresolved explicit wikilinks, numeric phantom links, and source/knowledge notes with no meaningful connection.
4. **Metadata health:** partial provenance, duplicate stable source IDs, missing source URLs, and stale Inbox review items.
5. **Knowledge-layer coverage:** concept candidates based on explicit relationships only; never title similarity alone.

**Output contract:**
- Markdown report with `healthy`, `warning`, and `action-required` sections.
- Each issue contains a concrete path, source/job evidence, and recommended next action.
- No source file modifications.

**Tests:**
- Healthy fixture returns zero action-required items.
- Broken wiki link is reported with its source path.
- A failed cron output is reported even if the scheduler’s stored status says `ok`.
- A fresh source note with a valid ID is not flagged as stale.

### Task 8: Schedule a weekly report-only audit

**Objective:** Provide the article’s “health check” capability without autonomous rewrites.

**Configuration:**
- Create a weekly Hermes cron job, KST Sunday 00:20 (UTC cron expression: `20 15 * * 6`).
- Keep `/root/wiki` as the shared workdir; the existing Vault lock serializes any unexpected overlap with the 00:15 daily curator candidate pass.
- Read-only terminal/file toolset.
- Deliver a report only for warnings/action-required items; return `[SILENT]` when healthy.

**Verification:**
- Run it manually once with the current Vault.
- Confirm it does not change `git status`.
- Confirm the report distinguishes “source current” from “cron last ran.”

---

## Phase 4 — Integrate without weakening current safeguards

### Task 9: Update the human-facing Vault map

**Files:**
- Modify: `README.md`
- Modify: `index.md`
- Modify: `log.md`

**Implementation:**
1. Add a short diagram of the five roles: source archives, raw evidence, inbox, knowledge layer, and Git history.
2. Add only top-level entry points; do not turn the root index into a complete file listing.
3. Record the new workflow in `log.md` after real implementation, not during planning.

### Task 10: Final end-to-end verification

**Checklist:**
1. Add a synthetic Inbox fixture; verify it appears in review queue.
2. Attempt promotion without approval; verify safe refusal.
3. Promote an approved fixture in a temporary test repository; verify source metadata preservation and Git validation.
4. Run concept-candidate report; verify it suggests but does not write knowledge notes.
5. Run health audit; verify no source Markdown changes.
6. Run existing Tistory, SKALA, and Information sync jobs in no-change mode; verify all remain silent and clean.
7. Verify `git status --short --branch` is clean and `HEAD == origin/main`.

---

## Commit plan

Use small Korean, concrete commits:

1. `정책: 지식 레이어와 Inbox 승격 계약 추가`
2. `문서: 지식 노트 기준본 3건 추가`
3. `기능: Inbox 검토 대기열 생성 추가`
4. `기능: 승인 기반 Inbox 승격 도구 추가`
5. `기능: 지식 건강검진 감사 도구 추가`
6. `자동화: 주간 지식 건강검진 훅 추가`
7. `문서: Second Brain 지식 운영 흐름 안내 보완`

All Vault-mutating commits must run through `scripts/vault_sync_lock.sh`, pass `python3 scripts/validate_vault_contract.py --changed-from-index --strict`, and use KST commit timestamps.

---

## Risks and guardrails

- **Over-linking / hallucinated connections:** Require source-backed links and show candidates for review before creating concept notes.
- **Archive corruption:** Treat blog and Notion mirrors as canonical source records; the new layer only links to them.
- **Automation noise:** Inbox reminders and health reports must be silent when healthy.
- **Hidden job failure:** Audit actual cron output and source identity, not status labels alone.
- **Scope creep:** Start with exactly three seed knowledge notes and one weekly read-only audit; do not bulk-convert the archive.
- **Private data:** Preserve the existing no-secrets/no-PII policy in all generated reports and notes.

## Recommended implementation order

1. Phase 1 contract + three seed notes.
2. Phase 3 read-only health auditor, because it improves visibility without modifying knowledge.
3. Phase 2 Inbox queue, then explicit promotion command.
4. Only after one week of reports, tune candidate thresholds or reminder frequency.
