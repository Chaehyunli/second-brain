---
title: Cursor AI 기반 VIBE CODING 실전활용 경진대회 장려상
created: 2026-07-11
updated: 2026-07-12
type: entity
tags: [award, career, project, backend]
sources: [raw/sources/petner-vibe-coding-detail-2026-03-08.md, raw/sources/career-description-2026-03-24.md]
confidence: high
---

# Cursor AI 기반 VIBE CODING 실전활용 경진대회 장려상

## 수상 기록

임채현은 **2025 Cursor AI 기반 VIBE CODING 실전활용 경진대회**에서 [[entities/projects/petner]] 프로젝트로 장려상을 수상했다. 프로젝트 수행 기간은 2025-08~2025-10이다.

## 평가 맥락과 프로젝트 근거

PETNER는 Spring Boot·React 기반 유기견 입양 플랫폼으로, OpenSearch 검색, WebSocket/STOMP 실시간 채팅, Redis 세션·캐시, Flyway 마이그레이션, OAuth 인증을 포함했다. 경진대회 원본 기록에는 기능 구현뿐 아니라 기술적 완성도와 실전 활용 역량을 평가받는 상황이 명시돼 있다.

본인이 맡은 범위는 ERD·API 명세 기준 정렬, 채팅·유기견·입양 신청·즐겨찾기 핵심 도메인 구현, 개발 환경·스키마 표준화, 테스트였다. 구체적으로 채팅 도메인 API 10개, 즐겨찾기 API 5개를 포함해 주요 흐름을 구현했다.

## 심사 피드백

원본 기록에는 기술 설계와 시스템 구현 완성도가 매우 높았다는 심사위원 피드백이 담겨 있다. 포트폴리오에서는 이 표현만 독립적으로 과장하기보다, 아래처럼 구현 근거와 함께 사용한다.

- Redis 세션을 이용한 WebSocket 사용자 식별
- Soft Delete·페이징을 통한 채팅 데이터 보존·조회 정책
- Flyway와 Docker Compose를 통한 팀 개발 표준화
- 라이선스·배포 조건을 고려한 OpenSearch 선택
- 단위·통합 테스트와 STOMP 전용 테스트 페이지

## AI 도구 활용의 위치

Cursor·Claude를 개발 생산성 향상을 위한 도구로 활용했다는 기록이 있다. 다만 수상과 프로젝트의 핵심 증거는 도구 사용 그 자체가 아니라, 요구를 ERD/API·상태 정책·테스트로 구체화하고 실제 기술 제약을 해결한 설계·구현 결과에 둔다.

## 관련 노트

- [[entities/projects/petner]] — 구현 범위와 기술 판단
- [[entities/lim-chae-hyun]] — 수상·기술 역량 요약
- [[concepts/backend-portfolio-narrative]] — 수상을 구현 근거로 설명하는 방식
