---
schema_version: 1
id: knowledge-llm-reliability-and-human-oversight
title: LLM 신뢰성 경계와 사람 검토
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-21 LLM과 Transformer 아키텍처_Day1/7-21 LLM과 Transformer 아키텍처 — Day1 핵심 정리.md
  - notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering.md
  - notion/Information/2026-08-04 — AI 시대의 사람 중심 혁신 | 기술·지역·산업을 연결하는 기준.md
---

# LLM 신뢰성 경계와 사람 검토

## 위험을 판단하는 질문
확률적 생성 결과가 정보 제공을 넘어 추천·상태 변경으로 이어질 때, 어떤 통제를 누구에게 맡길 것인가?

## 모델 특성과 통제 강도
환각·비결정성은 더 긴 prompt만으로 사라지지 않는다. 저위험 정보, 중위험 추천, 고위험 상태 변경은 같은 자동화 정책을 쓰지 않는다.

## 결정론적 검증과 승인
형식·권한·상태 전이를 모델 밖에서 검사하고, 되돌리기 어려운 행동에는 사람 확인 또는 명시적 승인 단계를 둔다.

## 실행 경계의 구현 관계
[[knowledge/agent-harness-and-bounded-loops]]는 권한·재시도·검증·복구를 시스템 루프에 배치하는 방법을, [[knowledge/stateful-ai-service-reliability]]는 예약·취소 흐름에서 모호성을 먼저 차단한 사례를 다룬다.

## 운영에서 남길 신호
오류, 승인 거절, override, 복구 가능성을 기록해 정책이 실제 위험을 줄이는지 본다.

## 범위와 근거
도메인별 법·운영 요구는 별도 결정한다.
- [[notion/SKALA/7-21 LLM과 Transformer 아키텍처_Day1/7-21 LLM과 Transformer 아키텍처 — Day1 핵심 정리]]
- [[notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering]]
- Information 원본은 frontmatter `sources` 경로로 추적한다.
