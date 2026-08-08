---
schema_version: 1
id: knowledge-stateful-ai-service-reliability
title: 상태를 가진 AI 서비스의 신뢰성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation, fastapi, backend]
sources:
  - entities/projects/masil.md
  - raw/sources/masil-github-2026-07-10.md
  - knowledge/llm-reliability-and-human-oversight.md
---

# 상태를 가진 AI 서비스의 신뢰성

## 사례의 질문
AI가 답변을 넘어 일정·예약·취소 같은 업무 상태를 바꿀 때, 잘못된 실행과 외부 모델 실패를 어떻게 흐름 밖으로 격리하는가?

## 상태 모델과 추적성
Masil은 일정 목록·수정·수정 이력과 변경 전 스냅샷을 `itinerary_logs`에 남긴다. AI 요청과 사용자 수정이 같은 상태를 바꿔도 변경 전후를 추적하려는 구조다.

## 모호한 요청의 처리
AI API는 SSE로 응답하고 chat, itinerary, change, reservation, cancel 흐름을 분류한다. 취소 대상이 모호하면 모델 호출로 곧바로 처리하지 않고 후보와 사용자 확인을 요구한다.

## 외부 실패의 격리
Token Bucket, 429 감지, exponential backoff+jitter는 제한 응답이 일정·예약 상태를 무너뜨리지 않도록 하는 구현 근거다.

## 일반 원칙과 사례의 경계
[[knowledge/llm-reliability-and-human-oversight]]의 승인·결정론적 검증 원칙이 이 사례에 연결된다. 그러나 구현 기록은 운영 가용성·실사용 효과를 자동으로 증명하지 않는다.

## 근거
- [[entities/projects/masil]]
- [[raw/sources/masil-github-2026-07-10]]
- [[knowledge/llm-reliability-and-human-oversight]]
