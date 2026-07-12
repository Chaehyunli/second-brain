---
title: Backend Portfolio Narrative
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [career, backend, project, architecture, performance, quality]
sources: [raw/sources/employment-zip-2026-07-10.md]
confidence: high
---

# Backend portfolio narrative

## Core message

**서비스 요구를 기술 문제로 분해하고, 설계 선택·검증 수치까지 책임지는 백엔드 개발자.** 프로젝트마다 서로 다른 문제를 해결했지만, 공통적으로 요구사항과 운영 제약을 먼저 파악한 뒤 구조를 선택하고, 테스트·성능 지표로 결과를 확인했다.

## Proof pillars

| Pillar                   | Evidence                                             | Portfolio proof                                |
| ------------------------ | ---------------------------------------------------- | ---------------------------------------------- |
| Performance/search       | [[entities/projects/searchive]]                      | 태그 정규화와 배치 검색으로 250ms→10ms         |
| Real-time data integrity | [[entities/projects/petner]]                         | Redis 세션, STOMP, Soft Delete, 페이징         |
| Security/authorization   | [[entities/projects/clubmoa]]                        | 리소스 단위 RBAC·세션 방식 선택                |
| Data/ML integration      | [[entities/projects/nosogong]]                       | 10,000 합성 데이터, R² 0.9964, RMSE 0.22       |
| AI service reliability   | [[entities/projects/masil]]                          | WebFlux/R2DBC, SSE, 일정·예약 상태, 429 복원력 |
| Production quality       | [[entities/experiences/pramt-technology-internship]] | 20만 LOC 전환, 약 8,000 테스트 케이스          |

## Writing rules for Notion portfolio

1. 프로젝트마다 `문제 맥락 → 본인의 판단 → 구현 범위 → 검증 결과` 순서로 쓴다.
2. 팀 프로젝트는 “전체 서비스”와 “내가 설계·구현한 범위”를 분리한다.
3. 수치는 원본 근거가 있는 값만 사용한다. `250ms→10ms`, `10,000건`, `R² 0.9964`, `RMSE 0.22`, `약 8,000개`, `20만 LOC`가 현재 확인된 수치다.
4. AI 도구 활용은 보조 수단으로만 표현하고, 문제 정의·설계·테스트·기술 판단의 소유권을 명시한다.
5. PETNER 기간은 사용자 확인과 기존 포트폴리오 표기를 기준으로 **2025-08~2025-10**으로 확정했으며, 이력서의 2024년 표기는 오기다.

## Portfolio order

1. [[entities/experiences/pramt-technology-internship]] — 실무 품질 검증
2. [[entities/projects/searchive]] — 개인 프로젝트 성능 개선
3. [[entities/projects/petner]] — 실시간·정합성·팀 협업
4. [[entities/projects/nosogong]] — ML/백엔드 통합
5. [[entities/projects/clubmoa]] — 보안·권한 설계

## Next evidence to obtain

- GitHub 저장소별 README·커밋·배포 링크로 구현 범위와 코드 수준 증빙 강화.
- Searchive의 실제 벤치마크 조건/데이터 규모 정리.
- PETNER의 진행 기간에 대한 GitHub 타임라인·대회 제출물 교차 근거 보강.
- Masil Capstone 디자인 전시회 은상 관련 상장·결과 공지·행사 정보 중 공개 가능한 근거 확보.
- 인턴 산출물 중 공개 가능한 테스트 설계 예시를 익명화해 보강.
