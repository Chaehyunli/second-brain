---
schema_version: 1
id: knowledge-git-flow-ci-cd-and-secret-boundaries
title: Git 흐름·CI/CD·비밀 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-14 Git 이해 및 활용/7-14 Git & AI코딩 & 환경구성 — 강의 정리.md
  - notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# Git 흐름·CI/CD·비밀 경계

## 핵심
브랜치·PR·테스트 게이트·preview와 production 분리·secret isolation은 배포 속도와 변경 안전성을 함께 관리하는 흐름이다.

## 연결된 근거
- [[notion/SKALA/7-14 Git 이해 및 활용/7-14 Git & AI코딩 & 환경구성 — 강의 정리.md]]
- [[notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리.md]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md]]

## 적용 기준
GitHub Flow·lint/test gate, main production·PR preview, 비밀값을 코드/클라이언트에서 분리하는 근거를 연결한다.

## 주의점 또는 한계
CI/CD 공급자와 비밀 관리 방식은 조직 권한·서비스별 제약에 맞춰 추가 확인한다.
