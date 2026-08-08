---
schema_version: 1
id: knowledge-evidence-grounded-portfolio-narrative
title: 근거 기반 포트폴리오 서사
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [career, portfolio, evidence, backend]
sources:
  - concepts/backend-portfolio-narrative.md
  - entities/lim-chae-hyun.md
  - entities/projects/petner.md
---

# 근거 기반 포트폴리오 서사

## 주장 단위
포트폴리오 문장은 기술 목록이 아니라 문제 맥락, 내가 내린 판단, 구현 범위, 검증 결과, 한계를 함께 가진 하나의 주장이다.

## 서사의 연결 규칙
[[concepts/backend-portfolio-narrative]]의 순서처럼 제약과 대안을 먼저 두고 선택·구현을 잇는다. [[entities/lim-chae-hyun]]의 역량 지도는 사례를 찾는 출발점이지, 프로젝트의 세부 성과를 자동으로 증명하는 근거는 아니다.

## 필요한 증거의 모양
수치에는 데이터 규모·환경·반복 조건을, 역할에는 팀 결과와 개인 구현 범위를 붙인다. PETNER처럼 팀 프로젝트에서는 서비스 전체 기능과 나의 설계·검증 범위를 분리한다.

## 공개 가능한 범위
비공개 코드, 고객 정보, 자격 식별값은 공개 서사에 넣지 않는다. 근거가 부족하면 멋있게 보이도록 추정하지 않고 추가 확인 필요 상태로 남긴다.

## 다른 지식 노트와의 관계
[[knowledge/performance-investigation-and-measurement-boundaries]]는 성능 수치의 측정 범위를, [[knowledge/legacy-characterization-and-team-reproducibility]]는 재현 가능한 검증 흔적을 제공한다. 이 노트는 그 기술 내용을 반복하지 않고 주장 가능 조건을 정한다.

## 출처와 한계
- [[concepts/backend-portfolio-narrative]]
- [[entities/lim-chae-hyun]]
- [[entities/projects/petner]]
