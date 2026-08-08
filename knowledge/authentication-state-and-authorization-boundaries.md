---
schema_version: 1
id: knowledge-authentication-state-and-authorization-boundaries
title: 인증 상태와 권한 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md
  - blog/기타/기타- Vue SPA 인증 상태 관리와 보안(Pinia · localStorage · Session · JWT · Cookie · CSRF · XSS).md
  - entities/projects/clubmoa.md
---

# 인증 상태와 권한 경계

## 핵심
HTTP의 인증 전달, UI의 반응형 상태, 서버의 세션·권한 관계는 서로 다른 책임이다. 권한은 전역 역할 이름보다 사용자·리소스·역할의 관계와 변경·철회 요구로 모델링한다.

## 연결된 근거
- [[blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md]]
- [[blog/기타/기타- Vue SPA 인증 상태 관리와 보안(Pinia · localStorage · Session · JWT · Cookie · CSRF · XSS).md]]
- [[entities/projects/clubmoa.md]]

## 적용 기준
쿠키/세션의 전달 구조, Pinia·localStorage의 UI·복원 역할, Clubmoa의 리소스 범위 RBAC와 세션 선택 근거를 연결한다.

## 주의점 또는 한계
토큰 위치·cookie flag·CSRF/XSS 대응은 제품별 위협 모델과 공식 보안 지침을 추가 확인해야 한다.
