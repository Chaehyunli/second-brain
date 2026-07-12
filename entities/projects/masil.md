---
title: Masil
created: 2026-07-10
updated: 2026-07-10
type: entity
tags:
  [
    project,
    backend,
    java,
    spring-boot,
    webflux,
    r2dbc,
    python,
    fastapi,
    ai-agent,
    sse,
    redis,
    postgresql,
    testing,
    reliability,
  ]
sources:
  [
    raw/sources/masil-github-2026-07-10.md,
    raw/sources/user-confirmed-masil-award-2026-07-10.md,
  ]
confidence: high
---

# Masil — AI travel itinerary agent

## Overview

명지대학교 자연캠퍼스 가이드와 사용자 맞춤형 여행 일정을 설계하는 AI 에이전트 프로젝트. Spring Boot WebFlux 백엔드와 FastAPI AI 서버를 분리하고, 일정·대화·예약 상태를 연결하는 구조를 구현했다.

## Verified contribution

- Spring Boot 3.5 WebFlux 기반에서 PostgreSQL 접근을 JPA에서 **R2DBC**로 전환하고, Reactive Redis·JSON 변환기·지연 평가 오류·테스트까지 함께 보완했다.
- 일정 목록·상세·수정·수정 이력·아이템 상태 변경 API를 구현했다. 기본 정보와 day plan 변경 전 스냅샷을 `itinerary_logs`에 보존해 변경을 추적한다.
- FastAPI AI API를 SSE로 제공하고, 요청을 `chat`, `itinerary`, `change`, `reservation`, `cancel`로 분류해 컨텍스트·현재 일정·예약 정보를 처리 흐름에 연결했다.
- 취소 요청에서 사용자가 대상을 명확히 선택하지 않았을 경우 후보 목록/확인 흐름을 우선 처리해, 모호한 LLM 호출이나 잘못된 취소를 줄이도록 설계했다.
- 429 대응을 위해 Token Bucket 기반 요청 조절과 지수 backoff+jitter 재시도를 구현하고 테스트했다.
- Clerk JWT, Flyway, Swagger, 배포용 컨테이너 구성을 포함한 운영 기반을 코드와 문서에서 확인했다.

## Evidence in current code

- `ItineraryController.java`: 사용자별 일정 조회, PATCH, 수정 이력 API와 JWT 주체 처리
- `ItineraryLog.java` 및 Flyway migration V7: 일정 변경 전 스냅샷 저장
- `aiMessageController.py`: internal token 검증, `StreamingResponse`, 컨텍스트 로드·요청 분류·예약/취소 처리
- `app/services/agents/_base.py`: Token Bucket, 429 감지, exponential backoff+jitter

## Award

[[entities/awards/masil-capstone-silver]] — Capstone 디자인 전시회 26개 팀 중 은상 수상. 수상 사실은 사용자 확인에 근거하며, 행사 세부 증빙은 추가 확보가 필요하다.

## Portfolio narrative

**AI 기능을 단순 응답 생성에 그치지 않고, 일정의 변경 이력·예약/취소 상태·인증·스트리밍 계약·모델 API 실패 대응까지 연결한 백엔드 설계 경험**으로 설명한다.

## Related

[[entities/lim-chae-hyun]]의 Java·Python 양쪽 백엔드와 비동기 전환 역량을 입증한다. [[concepts/backend-portfolio-narrative]]에서 AI 기능의 신뢰성·상태 관리 사례로 활용한다.
