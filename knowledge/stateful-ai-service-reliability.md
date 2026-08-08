---
schema_version: 1
id: knowledge-stateful-ai-service-reliability
title: 상태를 가진 AI 서비스의 신뢰성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation, fastapi, backend]
sources:
  - entities/projects/masil.md
  - raw/sources/masil-github-2026-07-10.md
  - knowledge/llm-reliability-and-human-oversight.md
---

# 상태를 가진 AI 서비스의 신뢰성

## 핵심
AI 통합은 답변 생성만이 아니라 예약·취소처럼 실제 업무 상태를 바꾸는 흐름의 계약, 모호한 요청 차단, rate limit·재시도·이력 보존을 함께 설계해야 한다.

## 연결된 근거
- [[entities/projects/masil.md]]
- [[raw/sources/masil-github-2026-07-10.md]]
- [[knowledge/llm-reliability-and-human-oversight.md]]

## 적용 기준
Masil의 SSE·상태 전이·모호 취소 차단·429 회복력과 LLM 사용 경계 원칙을 연결한다.

## 주의점 또는 한계
구현 근거는 운영 가용성·실사용 효과를 자동 증명하지 않는다.
