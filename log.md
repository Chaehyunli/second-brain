# Personal Career Wiki Log

> Chronological record of actions. `raw/` source artifacts remain immutable after ingestion.

## [2026-07-10] create | Personal Career Wiki initialized

- Domain: 임채현의 백엔드 개발자 포트폴리오와 검증된 기술·경험 지식.
- Created: `SCHEMA.md`, `index.md`, `raw/sources/employment-zip-2026-07-10.md`.
- Privacy rule established: no address, contact details, birth date, credential IDs, or secrets in agent-owned pages.

## [2026-07-10] ingest | 취업.zip portfolio evidence

- Extracted and cross-checked resume, career description, prior portfolio, detailed project records, internship record, and credential evidence.
- Created profile, project, experience, and portfolio-narrative pages.
- Flagged PETNER period discrepancy for review rather than silently selecting an unsupported date.

## [2026-07-10] ingest | Masil GitHub code evidence and PETNER timeline correction

- Inspected `Masil2026/Capstone-backend`, `Capstone-ai`, and `Capstone-deploy` main branches; recorded the source manifest and created the Masil project entity.
- Confirmed the Masil narrative from current code: WebFlux/R2DBC transition, itinerary snapshots, FastAPI SSE flow, reservation/cancel safeguards, and 429 rate-limit handling.
- Updated PETNER timeline to 2025-08~2025-10 from user confirmation and the existing portfolio PDF; marked the earlier 2024 resume entry as a typo.

## [2026-07-10] lint | Career wiki integrity and coverage audit

- Structural checks: 8 agent-owned pages, 2 raw manifests; no broken wikilinks, no index omissions, no missing required frontmatter, no oversized pages, and no low-confidence or contested pages.
- Fixed: registered Masil technology tags in `SCHEMA.md` and linked Masil from the profile and portfolio narrative, resolving its orphan status.
- Review required: both raw manifest body hashes do not match their stored `sha256` values; raw files were left untouched under the immutability policy.
- Coverage gaps: the current raw manifests aggregate multiple portfolio extracts, so individual claims are not traceable to a specific original file; no archived source currently substantiates the Masil Capstone exhibition silver award.
- Updated: `SCHEMA.md`, `entities/lim-chae-hyun.md`, `concepts/backend-portfolio-narrative.md`.

## [2026-07-10] update | Masil Capstone 디자인 전시회 은상

- Recorded user-confirmed award: Masil project, Capstone 디자인 전시회, 26개 팀 중 은상.
- Created `raw/sources/user-confirmed-masil-award-2026-07-10.md` and `entities/awards/masil-capstone-silver.md`.
- Updated the Masil project page, profile, index, and portfolio narrative follow-up evidence list.
- Evidence status: user-confirmed; award page remains `confidence: medium` until an award certificate or official announcement is archived.

## [2026-07-11] correction | VIBE CODING award relationship

- User corrected the prior correction: the 2025 Cursor AI 기반 VIBE CODING 실전활용 경진대회 장려상 is connected to PETNER.
- Restored the PETNER `award` tag and its award section; updated the VIBE CODING award entity, profile, and index to link the award to PETNER.
- Rebuilt the HERMES child knowledge-graph page with detailed project→capability, project→award, credentials, internship, confidence, and evidence views.

## [2026-07-11] update | Award attribution and credential coverage correction

- User correction: the Capstone 디자인 전시회 은상 and “Masil 전시회 은상” are one award; future visualizations must show one Masil award node only.
- Removed the VIBE CODING 장려상 attribution and `award` tag from `entities/projects/petner.md`; the profile retains the competition record without a PETNER relation.
- Created verified credential pages for 정보처리기사 (2025-12-24) and SQL 개발자(SQLD, 2025-09-19), excluding credential IDs and other sensitive fields.
- Created `entities/awards/vibe-coding-encouragement-award.md` to retain the VIBE CODING 장려상 as a personal award with no PETNER association.
- Updated: `SCHEMA.md`, `index.md`, `entities/lim-chae-hyun.md`, `entities/projects/petner.md`.
