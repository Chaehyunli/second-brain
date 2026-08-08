---
schema_version: 1
id: knowledge-context-engineering-and-tool-grounding
title: Context Engineering과 도구 근거화
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md
  - notion/SKALA/7-15 기타/7-15 AI 에이전틱 패턴의 진화 — Prompt·Context·Harness.md
  - notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md
---

# Context Engineering과 도구 근거화

## 설계 질문
답변이나 다음 행동에 필요한 정보만, 어떤 우선순위와 검증 경계로 모델에 제공할 것인가?

## 입력을 구성하는 요소
evidence, memory, tool 결과, instruction, 출력 형식은 역할이 다르다. Context engineering은 이를 모두 늘리는 일이 아니라 관련성·최신성·출처·길이 예산으로 고르는 일이다.

## 도구 결과를 근거로 바꾸는 흐름
호출 → 결과 해석 → 원본과 연결 → 검증 가능한 응답의 순서를 둔다. 원문에 없는 지시나 도구 출력의 해석을 사실처럼 승격하지 않는다.

## 점진적 공개와 하네스
필요할 때만 세부 정보를 열어 context를 관리한다. 이 선택은 [[knowledge/agent-harness-and-bounded-loops]]의 tool·state·검증 루프 안에서 실행되며, [[knowledge/rag-retrieval-and-data-boundaries]]의 retrieval 결과도 하나의 근거 입력이다.

## 실패 패턴과 범위
과도한 컨텍스트, 출처 없는 요약, 결과의 무비판적 사용은 정확성을 보장하지 않는다. 긴 prompt만으로 확률적 오류를 없앨 수 없으며 고위험 행동은 별도 검증·승인 경계가 필요하다.

## 근거
- [[notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering]]
- [[notion/SKALA/7-15 기타/7-15 AI 에이전틱 패턴의 진화 — Prompt·Context·Harness]]
- Information 원본은 frontmatter `sources` 경로로 추적한다.
