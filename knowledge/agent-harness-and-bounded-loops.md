---
schema_version: 1
id: knowledge-agent-harness-and-bounded-loops
title: Agent Harness와 제한된 자율 루프
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-15 기타/7-15 Agent Harness 핵심 구조 — LangChain.md
  - notion/SKALA/7-15 기타/7-15 OpenCode로 보는 코딩 에이전트 내부 구조.md
  - notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md
---

# Agent Harness와 제한된 자율 루프

## 핵심
에이전트 신뢰성은 모델 프롬프트만이 아니라 context·tools·state·권한·독립 검증·재시도 경계를 가진 harness와 discovery→execution→verification 루프에서 나온다.

## 연결된 근거
- [[notion/SKALA/7-15 기타/7-15 Agent Harness 핵심 구조 — LangChain.md]]
- [[notion/SKALA/7-15 기타/7-15 OpenCode로 보는 코딩 에이전트 내부 구조.md]]
- `notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md` — 파일명에 `|`가 있어 wiki link 별칭 구문과 충돌하므로 frontmatter `sources`를 정본 경로로 사용

## 적용 기준
SKALA의 tool loop·filesystem state·sandbox·log/test 검증과 Information의 루프 제약·회복 구조를 연결한다.

## 주의점 또는 한계
특정 제품의 내부 구현·권한 모델은 공식 문서 없이 일반 사실로 확정하지 않는다.
