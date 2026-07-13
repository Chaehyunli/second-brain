---
title: Masil
created: 2026-07-10
updated: 2026-07-13
type: entity
tags: [project, backend, java, spring-boot, webflux, r2dbc, python, fastapi, ai-agent, sse, redis, postgresql, testing, reliability, infrastructure]
sources: [raw/sources/masil-github-2026-07-10.md, raw/sources/user-confirmed-masil-award-2026-07-10.md, raw/sources/project-ui-evidence-2026-07-13.md]
confidence: high
---

# Masil — AI 여행 일정 에이전트

## 한눈에 보기

명지대학교 자연캠퍼스 가이드와 사용자 맞춤형 여행 일정을 설계하는 AI 에이전트 프로젝트. Spring Boot WebFlux 백엔드와 FastAPI AI 서비스를 분리하고, 일정·대화·예약 상태를 하나의 사용자 흐름으로 연결했다.

## 확인된 구현과 설계

### 반응형 데이터 접근 전환

Spring Boot 3.5 WebFlux 환경에서 PostgreSQL 접근을 JPA에서 **R2DBC**로 전환했다. 단순 드라이버 교체가 아니라 Reactive Redis, JSON 변환기, 지연 평가 오류, 테스트까지 함께 보완해 비동기 스택의 계약을 맞췄다.

### 일정 변경을 추적 가능한 상태로 관리

일정 목록·상세·수정, 수정 이력, 아이템 상태 변경 API를 구현했다. 기본 정보와 day plan 변경 전 스냅샷을 `itinerary_logs`에 저장해, AI 요청이나 사용자의 수정으로 일정이 바뀌어도 변경 전후를 추적할 수 있게 했다.

### AI 응답을 업무 상태와 연결

FastAPI AI API는 SSE로 응답하고 `chat`, `itinerary`, `change`, `reservation`, `cancel` 요청을 분류한다. 컨텍스트·현재 일정·예약 정보를 로드해 처리 흐름에 반영한다. 취소 대상이 모호하면 모델 호출로 성급히 처리하지 않고 후보 목록과 사용자 확인을 먼저 요구해 잘못된 취소를 줄였다.

### 외부 모델 API 실패를 사용자 흐름에서 격리

`app/services/agents/_base.py`에 Token Bucket 요청 조절과 429 감지, exponential backoff+jitter 재시도를 구현·테스트했다. 이는 “AI가 답하면 성공”이 아니라, 제한 응답에도 일정·예약 상태를 무너뜨리지 않는 서비스 계약을 다룬 사례다.

## 제품 흐름 UI 근거 (2026-07-13)

사용자 제공 모바일 앱 패널을 기능별로 분리한 UI 기록을 확인했다. 홈의 AI 여행 플래너 진입 → 자연어 대화에서 일정·항공·숙소 후보 제안 → 예약 상태 조회 → Day별 일정 편집 → 여행 당일 진행률·길 안내 흐름으로 연결된다. 실제 Android/iOS 기기에 직접 접근하지 못한 환경이므로, 이 기록은 웹 화면을 임의 재현한 결과가 아니라 원본 모바일 UI 패널을 근거로 한다.

## 코드 근거

- `ItineraryController.java` — 사용자별 일정 조회·PATCH·수정 이력과 JWT 주체 처리
- `ItineraryLog.java`, Flyway migration V7 — 일정 변경 전 스냅샷
- `aiMessageController.py` — internal token 검증, `StreamingResponse`, 컨텍스트 로드·요청 분류·예약/취소 처리
- `app/services/agents/_base.py` — Token Bucket, 429 대응, backoff+jitter
- GitHub inspection 기준 사용자 식별자와 연결된 커밋: backend 118개, AI service 173개

## 수상

[[entities/awards/masil-capstone-silver]] — Capstone 디자인 전시회 26개 팀 중 은상. 이 결과는 사용자 확인 기반이며, 공식 결과 공지·상장·주최 정보가 확보되면 근거 수준을 추가로 높인다.

## 관련 노트

- [[entities/lim-chae-hyun]] — Java·Python 이중 백엔드와 AI 서비스 신뢰성 역량
- [[entities/projects/searchive]] — AI 기능을 데이터 품질·성능과 함께 설계한 비교 사례
- [[concepts/backend-portfolio-narrative]] — 상태·신뢰성 중심의 포트폴리오 서사
