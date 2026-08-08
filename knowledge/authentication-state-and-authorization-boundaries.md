---
schema_version: 1
id: knowledge-authentication-state-and-authorization-boundaries
title: 인증 상태와 권한 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md
  - blog/기타/기타- Vue SPA 인증 상태 관리와 보안(Pinia · localStorage · Session · JWT · Cookie · CSRF · XSS).md
  - entities/projects/clubmoa.md
---

# 인증 상태와 권한 경계

## 보호하려는 것
인증 전달, 화면의 로그인 표시, 리소스에 대한 허용 여부는 모두 “로그인”으로 묶을 수 있지만 보호 대상과 실패 방식이 다르다.

## 브라우저·UI·서버의 책임
쿠키·세션은 HTTP 요청에서 인증 상태를 전달한다. Pinia·localStorage는 화면 상태와 복원을 돕지만 서버 권한 판단을 대신하지 않는다. 서버는 요청 주체와 대상 리소스의 관계를 다시 확인한다.

## 권한 관계를 정하는 방법
Clubmoa 기록의 사용자–동아리–역할 관계처럼 권한은 전역 역할명보다 리소스 범위와 철회 요구를 포함해 모델링한다. 세션 선택은 즉시 차단 요구 같은 운영 조건과 연결된다.

## 경계를 넘을 때의 위험
공유 캐시·클라이언트 저장소에 민감한 상태를 넓게 두면 노출 범위가 달라진다. 인증된 요청과 장기 연결 채널의 권한은 [[knowledge/request-response-and-server-events]]와 함께 같은 주체 확인 원칙으로 검토한다.

## 검증 질문과 한계
권한 변경 뒤 즉시 차단되는지, 서버가 리소스별 인가를 수행하는지 확인한다. cookie flag, CSRF/XSS 대응, 토큰 보관 방식은 이 출처만으로 제품별 정답을 정하지 않으며 위협 모델과 공식 보안 지침이 필요하다.

## 확인한 근거
- [[blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers]]
- [[blog/기타/기타- Vue SPA 인증 상태 관리와 보안(Pinia · localStorage · Session · JWT · Cookie · CSRF · XSS)]]
- [[entities/projects/clubmoa]]
