# Personal Career Wiki Log

> Chronological record of actions. `raw/` source artifacts remain immutable after ingestion.

## [2026-07-10] create | Personal Career Wiki initialized

- Domain: 임채현의 백엔드 개발자 포트폴리오와 검증된 기술·경험 지식.
- Created: `SCHEMA.md`, `index.md`, `raw/sources/employment-zip-2026-07-10.md`.
- Privacy rule established: no address, contact details, birth date, credential IDs, or secrets in agent-owned pages.

## [2026-07-10] ingest | 취업.zip portfolio evidence

- Extracted and cross-checked resume, career description, prior portfolio, detailed project records, internship record, and credential evidence.
- Created profile, project, experience, and portfolio-narrative pages.
- PETNER period was later confirmed as 2025-08~2025-10; the 2024 resume entry is a typo.

## [2026-07-10] ingest | Masil GitHub code evidence

- Inspected `Masil2026/Capstone-backend`, `Capstone-ai`, and `Capstone-deploy` main branches.
- Recorded WebFlux/R2DBC transition, itinerary snapshots, FastAPI SSE flow, reservation/cancel safeguards, and 429 rate-limit handling.

## [2026-07-10] update | Masil Capstone 디자인 전시회 은상

- Recorded user-confirmed award: Masil project, Capstone 디자인 전시회, 26개 팀 중 은상.
- Evidence remains `confidence: medium` until an award certificate or official announcement is archived.

## [2026-07-11] correction | VIBE CODING award attribution

- The 2025 Cursor AI 기반 VIBE CODING 실전활용 경진대회 장려상 is connected to PETNER.
- PETNER period is confirmed as 2025-08~2025-10.

## [2026-07-12] enrich | Career evidence split and detailed entity notes

- Split traceability manifests by source for internship, Searchive, PETNER/VIBE CODING, 동아리모아, 노소공, and career description.
- Rewrote profile, portfolio narrative, five project notes, internship note, and two award notes with problem context, personal contribution, technical decisions, verified outcomes, caveats, and wikilinks.
- Preserved evidence boundaries: Masil award remains user-confirmed; Searchive and 노소공 metrics retain their measurement conditions.

## [2026-07-12] archive | Technical blog to Obsidian

- Archived `https://ch010104.tistory.com/` posts as one Markdown note per post under `blog/`.
- Each note preserves source URL, category, publication date when available, and extracted body; `blog/index.md` groups them by category.

## [2026-07-12] correction | Technical blog archive quality and graph structure

- Rebuilt all 297 posts as concise `핵심 요약` notes; removed raw continuous body extraction and formula/noise fragments.
- Kept every original Tistory URL in a visible `원문` section and in `source_url` frontmatter.
- Moved notes into 25 category folders, replaced numeric filenames with title-based filenames, and made the top-level blog index point only to category indexes.
- Added tag/category-based related-post links (up to three per post) instead of one all-post hub node.

## [2026-07-13] update | Project code and UI evidence

- Reviewed Searchive backend `main` commits for embedding model initialization locking, KeyBERT latency reduction, and document-summary fallback context for AI responses; linked the implementation evidence to the Searchive project note.
- Added traceable UI-flow evidence to Masil, PETNER, 동아리모아, and 노소공 notes. Each entry records whether it is an original mobile panel, local fixture rendering, or mock-only UI verification so interface evidence is not presented as production backend validation.

## [2026-08-06] build | Knowledge curator and review workflow

- Added a source-preserving `knowledge/` layer with initial cross-source notes for Vue application composition, source-to-public technical writing, and evidence-grounded portfolio narrative.
- Added candidate discovery, Inbox review queue, explicit approval-only promotion, and read-only health-audit tools with unit tests.
- Registered daily Knowledge Curator candidate discovery and weekly health-check/safe-update cron roles; source mirrors remain authoritative and automatic interpretation/promotion stays prohibited.

## [2026-08-08] refactor | Adaptive Knowledge and Python evidence map

- Reframed all existing Knowledge notes by their evidence-fit archetype rather than a fixed project-oriented body template; retained stable IDs, source lists, and explicit scope/uncertainty.
- Updated the Knowledge schema, curator policy, navigation map, and index with the adaptive minimum invariants: topic, source-backed evidence, meaningful relation, and scope/uncertainty.
- Added the source-backed Python analysis/service-boundary note from SKALA Day1/Day2 and the Masil, 노소공, Searchive, and profile evidence paths; it keeps synthetic-data, analysis, and operational claims distinct.
