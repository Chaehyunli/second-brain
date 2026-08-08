---
schema_version: 1
id: knowledge-legacy-characterization-and-team-reproducibility
title: 레거시 특성화 테스트와 팀 재현성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - entities/experiences/pramt-technology-internship.md
  - entities/projects/petner.md
  - raw/sources/petner-vibe-coding-detail-2026-03-08.md
---

# 레거시 특성화 테스트와 팀 재현성

## 사용할 때
명세가 불완전하고 기존 동작을 바꾸기 전 현재 행동을 확인해야 할 때 쓰는 작업 절차다.

## 동작을 복원하는 순서
관찰한 상태, 버튼 경로, 업무 규칙을 먼저 기록하고 특성화 테스트로 고정한다. 인턴십 기록의 legacy 분석·결함 분류는 이 순서가 추측보다 관찰 가능한 행동을 우선함을 보여 준다.

## 팀이 같은 환경에서 확인하는 방법
PETNER의 Flyway, Docker Compose, STOMP 테스트 환경처럼 마이그레이션·로컬 의존성·프로토콜 테스트 조건을 함께 재현한다. 테스트만 저장하고 실행 환경을 잃으면 팀 검증은 끊긴다.

## 결과를 전달하는 형식
결함은 재현 경로·기대와 실제·범위로 나누어 전달한다. 이런 흔적은 [[knowledge/evidence-grounded-portfolio-narrative]]에서 말하는 검증 가능한 주장 근거가 될 수 있다.

## 측정 경계
프로젝트별 테스트 수나 품질 결과를 다른 시스템의 일반 품질 보장으로 확장하지 않는다.

## 근거
- [[entities/experiences/pramt-technology-internship]]
- [[entities/projects/petner]]
- [[raw/sources/petner-vibe-coding-detail-2026-03-08]]
