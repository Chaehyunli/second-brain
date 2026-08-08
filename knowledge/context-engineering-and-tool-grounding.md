---
schema_version: 1
id: knowledge-context-engineering-and-tool-grounding
title: Context Engineering과 도구 근거화
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md
  - notion/SKALA/7-15 기타/7-15 AI 에이전틱 패턴의 진화 — Prompt·Context·Harness.md
  - notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md
---

# Context Engineering과 도구 근거화

## 핵심
Context engineering은 문장형 prompt 작성보다 evidence·memory·tool 결과·출력 형식을 필요한 순간에 선택하고 검증 가능한 범위로 제공하는 작업이다.

## 연결된 근거
- [[notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md]]
- [[notion/SKALA/7-15 기타/7-15 AI 에이전틱 패턴의 진화 — Prompt·Context·Harness.md]]
- `notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md` — 파일명에 `|`가 있어 wiki link 별칭 구문과 충돌하므로 frontmatter `sources`를 정본 경로로 사용

## 적용 기준
progressive disclosure, tool grounding, verification을 prompt/context/harness 계층으로 분리한 근거를 연결한다.

## 주의점 또는 한계
컨텍스트가 많다고 정확성이 보장되지는 않으므로 출처 우선순위·길이 제한·독립 검증을 함께 둔다.
