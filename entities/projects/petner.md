---
title: PETNER
created: 2026-07-10
updated: 2026-07-12
type: entity
tags: [project, backend, java, spring-boot, database, search, security, testing, infrastructure, award, redis]
sources: [raw/sources/petner-vibe-coding-detail-2026-03-08.md, raw/sources/career-description-2026-03-24.md]
confidence: high
contested: false
---

# PETNER — 실시간 유기견 입양 플랫폼

## 한눈에 보기

- **기간:** 2025-08~2025-10
- **구성:** 백엔드 3명·프런트엔드 1명 팀 프로젝트
- **기술:** Spring Boot (Java 17), React, PostgreSQL, Redis, Flyway, OpenSearch 2.11.0, Google Cloud Storage, WebSocket/STOMP, JUnit 5
- **역할:** ERD·API 명세 기준 정렬, 채팅·유기견·입양 신청·즐겨찾기 핵심 도메인 구현, 스키마·개발 환경 표준화, 테스트

## 서비스와 구현 범위

유기견 정보·입양 신청·커뮤니티·상담을 연결하는 서비스다. 본인은 팀의 ERD와 API 명세 설계를 주도해 개발 인터페이스를 정렬하고, 4개 도메인 총 27개 API 구현에 참여했다.

- **채팅:** 채팅방 생성/재입장/나가기/메시지 전송/이전 메시지 페이징 등 10개 API
- **즐겨찾기:** 추가·제거·내 목록 페이징·여부 조회 등 5개 API
- **도메인:** Dogs, DogApplies, 즐겨찾기 핵심 로직과 신청 상태 변경 정책

## 핵심 기술 판단

### 실시간 채팅의 사용자 식별과 데이터 보존

Spring WebSocket과 STOMP로 1:1 실시간 채팅을 구현하고, Redis 세션을 사용해 연결 상태에서도 사용자 식별과 세션 관리를 이어갔다. 메시지는 PostgreSQL에 영속화하고 과거 내역은 페이징 조회했다.

초기 물리 삭제는 FK 제약 위반과 데이터 유실 위험을 만들었다. 참여자 이탈 정책과 참조 무결성을 모두 만족시키기 위해 Soft Delete로 전환하고, 참여자별 메시지 조회 범위를 분리했다.

### 팀 개발의 환경·스키마 표준화

Flyway migration을 버전 관리하고 Docker Compose로 PostgreSQL·Redis·OpenSearch를 컨테이너화했다. 팀원은 애플리케이션 실행만으로 최신 스키마와 동일한 개발 환경에 맞출 수 있어, 환경 차이로 생기는 오류를 줄이는 기반이 됐다.

### 라이선스와 운영 제약을 포함한 검색 선택

OpenSearch와 Elasticsearch를 비교해 Apache 2.0 라이선스, 재배포·운영 제약을 기준으로 OpenSearch를 선택했다. 기술 기능만이 아니라 배포·사용 조건까지 포함해 선택한 사례다.

### 인증·테스트·성능

- 자체 토큰 설계를 급히 완성하는 대신 카카오 OAuth를 적용해 로그인 신뢰성을 확보하고 핵심 기능 개발에 집중했다.
- JUnit 5·Mockito 단위 테스트와 Spring Boot 통합 테스트로 서비스 로직·엔드포인트를 검증했다.
- STOMP는 REST 도구만으로 흐름 검증이 어려워, 단일 HTML 테스트 페이지로 연결·구독·발행·수신 전 과정을 확인했다.
- 유기견 목록 API의 N+1 문제를 Fetch Join으로 개선해 쿼리 횟수를 `1 + 2N`에서 1회로 줄였다.

## 수상

[[entities/awards/vibe-coding-encouragement-award]] — PETNER로 2025 Cursor AI 기반 VIBE CODING 실전활용 경진대회 장려상 수상. 원본 기록에는 기술 설계와 시스템 구현 완성도에 대한 심사 피드백이 포함돼 있다.

## 포트폴리오 핵심 문장

**실시간 기능을 단순 WebSocket 연결로 끝내지 않고 Redis 세션 기반 사용자 식별, Soft Delete 기반 보존 정책, 페이징 조회, 스키마/환경 표준화와 전용 STOMP 테스트 환경까지 연결해 정합성과 검증 가능성을 설계했다.**

## 관련 노트

- [[entities/lim-chae-hyun]] — 실시간·정합성·기술 의사결정 역량
- [[entities/awards/vibe-coding-encouragement-award]] — 수상 근거와 심사 피드백
- [[entities/experiences/pramt-technology-internship]] — 테스트·품질 검증 관점
- [[concepts/backend-portfolio-narrative]] — 포트폴리오 서술 기준
