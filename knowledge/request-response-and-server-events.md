---
schema_version: 1
id: knowledge-request-response-and-server-events
title: 요청·응답과 서버 주도 이벤트
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/SPRING BOOT/Spring Boot- 10. Redis Pub-Sub 기반 실시간 알림 시스템.md
  - blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조.md
  - entities/projects/masil.md
---

# 요청·응답과 서버 주도 이벤트

## 핵심
일반 웹 API는 클라이언트가 시작하는 요청·응답이고, 알림·스트리밍은 서버에서 클라이언트로 지속 전달할 채널과 연결 상태 정책이 필요하다.

## 연결된 근거
- [[blog/SPRING BOOT/Spring Boot- 10. Redis Pub-Sub 기반 실시간 알림 시스템.md]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조.md]]
- [[entities/projects/masil.md]]

## 적용 기준
SSE·Redis Pub/Sub의 알림 구조, DTO·세션 기반 요청 처리, Masil의 SSE AI 요청 흐름을 연결한다.

## 주의점 또는 한계
SSE·WebSocket·Pub/Sub 선택은 전달 보장·재연결·권한·운영 관측 요구를 기준으로 별도 설계해야 한다.
