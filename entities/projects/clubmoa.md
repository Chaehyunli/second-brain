---
title: 동아리모아
created: 2026-07-10
updated: 2026-07-10
type: entity
tags: [project, backend, java, spring-boot, database, security, architecture]
sources: [raw/sources/employment-zip-2026-07-10.md]
confidence: high
---

# 동아리모아 — Club application and management platform

## Overview

2025-01~2025-03 진행한 동아리 지원·운영 플랫폼 팀 프로젝트. React·Spring Boot·MySQL 기반에서 백엔드와 권한 설계를 담당했다.

## Key decisions and implementation

- 사용자·동아리·지원서·역할 관계를 모델링하고, 지원서 작성/조회/수정/삭제와 관리자 승인·구성원 운영 흐름을 구현했다.
- 로그인, 강제 탈퇴, 권한 변경 같은 즉시 통제 요구를 분석해 JWT 대신 Redis 기반 세션 인증과 Spring Security를 선택했다.
- 사용자-동아리-역할 관계를 별도 스키마로 두고, 동아리별 회장 여부를 확인하는 커스텀 인가를 구현했다. 회장만 임원 권한을 위임하도록 제어했다.
- 지원 승인과 역할 부여를 트랜잭션으로 묶어 일관성을 확보했고, GCS에 첨부 파일을 저장하는 연동을 구현했다.
- 리소스별 RBAC, 메서드 단위 인가, 표현식 기반 검증을 결합했다.

## Portfolio role

[[entities/lim-chae-hyun]]의 인증·인가 설계 역량을 가장 명확하게 보여주는 초기 프로젝트다. [[concepts/backend-portfolio-narrative]]에서는 기술 선택의 기준을 설명하는 사례로 활용한다.
