---
title: PETNER
created: 2026-07-10
updated: 2026-07-11
type: entity
tags:
  [
    project,
    backend,
    java,
    spring-boot,
    database,
    search,
    security,
    testing,
    infrastructure,
    award,
  ]
sources: [raw/sources/employment-zip-2026-07-10.md]
confidence: high
contested: false
---

# PETNER — Real-time pet adoption platform

## Overview

Spring Boot·React 기반의 유기견 입양 플랫폼 팀 프로젝트. 백엔드 3명·프론트엔드 1명 구성에서 백엔드 개발자로 참여했으며, ERD/API 명세와 핵심 도메인 구현에 기여했다.

## Verified contribution

- 채팅방 생성·재입장·나가기·메시지 전송·이전 메시지 페이징 등 채팅 API를 설계·구현했다.
- Spring WebSocket/STOMP와 Redis 세션으로 연결 상태에서도 사용자 식별을 유지했고, Soft Delete로 참여자별 메시지 조회 범위를 분리했다.
- Dogs, DogApplies, 즐겨찾기 등 핵심 도메인 API를 구현하고 N+1 조회를 Fetch Join으로 개선했다.
- Flyway로 DB 스키마 동기화를 자동화하고, Docker Compose로 PostgreSQL·Redis·OpenSearch 개발 환경을 표준화했다.
- 라이선스·배포 조건을 비교해 Elasticsearch 대신 OpenSearch를 선택했고, 카카오 OAuth 인증을 구현했다.
- JUnit 5/Mockito 단위 테스트와 Spring Boot 통합 테스트, 단일 HTML STOMP 테스트 페이지로 주요 흐름을 검증했다.

## Award

[[entities/awards/vibe-coding-encouragement-award]] — PETNER 프로젝트로 2025 Cursor AI 기반 VIBE CODING 실전활용 경진대회에서 장려상을 수상했다. 심사 피드백으로 기술 설계·구현 완성도가 높았다는 기록이 있다.

## Confirmed timeline

프로젝트 기간은 **2025-08~2025-10**이다. 사용자 확인과 기존 포트폴리오의 프로젝트 기간 표기를 기준으로 확정했으며, 이력서의 2024년 표기는 오기였다.

## Related

[[entities/lim-chae-hyun]]의 실시간 시스템·기술 의사결정 역량을 입증한다. [[concepts/backend-portfolio-narrative]]에서는 정합성과 테스트 전략 사례로 활용한다.
