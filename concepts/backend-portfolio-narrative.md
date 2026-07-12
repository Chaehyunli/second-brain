---
title: Backend Portfolio Narrative
created: 2026-07-10
updated: 2026-07-12
type: concept
tags: [career, backend, project, architecture, performance, quality, reliability]
sources: [raw/sources/career-description-2026-03-24.md, raw/sources/pramt-internship-detail-2026-03-08.md, raw/sources/searchive-detail-2026-03-08.md, raw/sources/petner-vibe-coding-detail-2026-03-08.md]
confidence: high
---

# Backend Portfolio Narrative

## 핵심 메시지

**서비스 요구를 기술 문제로 분해하고, 설계 선택·구현 범위·검증 결과까지 책임지는 백엔드 개발자.** 공통점은 기술 자체를 먼저 고르는 것이 아니라, 데이터 정합성·운영 제약·응답 지연·콜드 스타트·명세 부재 같은 제약을 먼저 드러내고 그에 맞는 구조를 선택했다는 점이다.

## 증거 축

| 축 | 대표 근거 | 포트폴리오에서 말할 수 있는 결과 |
| --- | --- | --- |
| 성능·검색 | [[entities/projects/searchive]] | 태그 정규화·배치 검색으로 키워드 5개 예시 250ms→10ms, 5회→1회 왕복 |
| 실시간 정합성 | [[entities/projects/petner]] | Redis 세션·STOMP·Soft Delete·페이징과 전용 테스트 환경 |
| 보안·인가 | [[entities/projects/clubmoa]] | 운영 시나리오를 기준으로 Redis 세션·리소스 단위 RBAC 선택 |
| 데이터·ML 통합 | [[entities/projects/nosogong]] | 10,000건 합성 데이터, XGBoost API 연동, R² 0.9964/RMSE 0.22 |
| AI 서비스 신뢰성 | [[entities/projects/masil]] | WebFlux/R2DBC, SSE, 일정 변경 이력, 모호한 취소 차단, 429 복원력 |
| 실무 품질 | [[entities/experiences/pramt-technology-internship]] | 20만 LOC 전환에서 약 8,000 테스트와 결함 원인 범위화 |

## 작성 규칙

1. **문제 맥락을 먼저 쓴다.** 예: “검색이 느렸다”보다 “키워드 M개와 태그 N개 전수 비교가 O(N×M)이었다.”
2. **개인 기여와 서비스 전체를 분리한다.** 팀 프로젝트에서는 담당 도메인, 판단, 직접 구현을 명확히 한다.
3. **수치는 조건을 붙인다.** Searchive 250ms→10ms는 키워드 5개 예시, 노소공 모델 지표는 합성 데이터 테스트셋이라는 한계를 함께 적는다.
4. **기술 선택의 대안을 남긴다.** JWT 대신 Redis 세션, Elasticsearch 대신 OpenSearch, Pygame 직접 이식 대신 웹 재구현처럼 ‘왜’를 보인다.
5. **AI는 결과가 아니라 도구다.** AI 도구 사용 여부보다 요구를 명세·상태 모델·테스트·복원력으로 구체화한 결과를 증거로 쓴다.

## 권장 제시 순서

1. [[entities/experiences/pramt-technology-internship]] — 실무 품질·레거시 분석·협업
2. [[entities/projects/searchive]] — 개인 프로젝트 성능 개선
3. [[entities/projects/petner]] — 실시간 시스템·팀 표준화·수상
4. [[entities/projects/masil]] — AI 서비스의 상태·신뢰성
5. [[entities/projects/nosogong]] — 콜드 스타트와 ML/백엔드 통합
6. [[entities/projects/clubmoa]] — 인증·인가 설계의 출발점

## 보강할 증거

- Masil 수상의 공식 결과 공지 또는 상장.
- Searchive 성능 측정의 데이터 규모·환경·반복 횟수.
- 인턴 경험에서 공개 가능한 익명화 테스트 설계 예시.
- PETNER 저장소 커밋/배포/대회 제출물의 교차 근거.
