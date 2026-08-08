---
schema_version: 1
id: knowledge-legacy-characterization-and-team-reproducibility
title: 레거시 특성화 테스트와 팀 재현성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - entities/experiences/pramt-technology-internship.md
  - entities/projects/petner.md
  - raw/sources/petner-vibe-coding-detail-2026-03-08.md
---

# 레거시 특성화 테스트와 팀 재현성

## 핵심
불완전한 명세에서는 관찰한 상태·버튼 경로·업무 규칙을 특성화 테스트로 만들고, 마이그레이션·로컬 의존성·프로토콜 테스트 환경을 재현 가능하게 유지해야 한다.

## 연결된 근거
- [[entities/experiences/pramt-technology-internship.md]]
- [[entities/projects/petner.md]]
- [[raw/sources/petner-vibe-coding-detail-2026-03-08.md]]

## 적용 기준
인턴십의 legacy 분석·결함 분류·테스트 복구와 PETNER의 Flyway·Docker Compose·STOMP 테스트 환경을 연결한다.

## 주의점 또는 한계
프로젝트별 테스트 수·품질 결과는 각각의 측정 범위에 한정해 해석한다.
