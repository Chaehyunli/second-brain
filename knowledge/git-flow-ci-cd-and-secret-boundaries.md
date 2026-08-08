---
schema_version: 1
id: knowledge-git-flow-ci-cd-and-secret-boundaries
title: Git 흐름·CI/CD·비밀 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-14 Git 이해 및 활용/7-14 Git & AI코딩 & 환경구성 — 강의 정리.md
  - notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# Git 흐름·CI/CD·비밀 경계

## 변경을 안전하게 흘리는 질문
코드 변경은 어떤 검증을 거쳐 어느 환경으로 승격되고, 비밀값은 어느 경계에 남아야 하는가?

## 변경 생명주기
GitHub Flow의 브랜치·PR·검토·테스트는 변경 단위를 분리한다. `main` production과 PR preview의 구분은 배포 대상과 검증 시점을 분리한다.

## 품질·배포·비밀의 연결
lint/test gate는 코드 품질을, 환경 승격은 배포 위험을, 비밀값 분리는 운영 자격증명 노출을 다룬다. 하나의 설정 파일이나 CI 성공만으로 세 경계가 모두 검증되지는 않는다.

## 배포 토폴로지와의 관계
Workers·Pages·VPS 배치 같은 실행 위치는 [[knowledge/resilient-deployment-and-data-infrastructure]]에서, 사용자 인증 자산과 운영 비밀의 차이는 [[knowledge/authentication-state-and-authorization-boundaries]]에서 보완한다.

## 롤백·감사와 불확실성
실패 시 되돌릴 기준, 누가 비밀에 접근하는지, 어떤 검증이 통과했는지 기록한다. 공급자별 권한·secret 처리 방식은 이 기록만으로 일반화하지 않고 공식 설정을 확인한다.

## 근거
- [[notion/SKALA/7-14 Git 이해 및 활용/7-14 Git & AI코딩 & 환경구성 — 강의 정리]]
- [[notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD]]
