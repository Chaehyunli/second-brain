---
schema_version: 1
id: knowledge-llm-reliability-and-human-oversight
title: LLM 신뢰성 경계와 사람 검토
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-21 LLM과 Transformer 아키텍처_Day1/7-21 LLM과 Transformer 아키텍처 — Day1 핵심 정리.md
  - notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md
  - notion/Information/2026-08-04 — AI 시대의 사람 중심 혁신 | 기술·지역·산업을 연결하는 기준.md
---

# LLM 신뢰성 경계와 사람 검토

## 핵심
확률적 생성의 환각·비결정성은 더 긴 프롬프트로 사라지지 않는다. 고위험 행동에는 deterministic check·근거·사람 승인·되돌릴 수 있는 경계가 필요하다.

## 연결된 근거
- [[notion/SKALA/7-21 LLM과 Transformer 아키텍처_Day1/7-21 LLM과 Transformer 아키텍처 — Day1 핵심 정리.md]]
- [[notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md]]
- `notion/Information/2026-08-04 — AI 시대의 사람 중심 혁신 | 기술·지역·산업을 연결하는 기준.md` — 파일명에 `|`가 있어 wiki link 별칭 구문과 충돌하므로 frontmatter `sources`를 정본 경로로 사용

## 적용 기준
LLM 한계·검증 요구, context/tool grounding, Information의 인간 책임·운영 기준을 연결한다.

## 주의점 또는 한계
위험 수준과 승인 정책은 도메인별 법적·운영 요구에 따라 별도로 정해야 한다.
