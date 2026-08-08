---
schema_version: 1
id: knowledge-request-response-and-server-events
title: 요청·응답과 서버 주도 이벤트
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/SPRING BOOT/Spring Boot- 10. Redis Pub-Sub 기반 실시간 알림 시스템.md
  - blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조.md
  - entities/projects/masil.md
---

# 요청·응답과 서버 주도 이벤트

## 통신 요구를 가르는 질문
누가 전송을 시작하는지, 연결을 얼마나 유지하는지, 전달 실패 뒤 무엇을 보장할지가 채널 선택의 기준이다.

## 요청·응답 계약
일반 HTTP API는 클라이언트가 요청을 시작하고 DTO·세션 등으로 응답을 처리한다. 이 계약은 사용자별 상태와 오류 응답을 명시하기에 적합하다.

## 서버 주도 전달 모델
Redis Pub/Sub와 SSE는 알림·스트리밍 전달에 쓰일 수 있다. Masil의 FastAPI AI 응답은 SSE로 흐르며 일정·예약 컨텍스트와 연결된다.

## 연결 수명과 권한
재연결, 전달 보장, 사용자별 채널, 관측 지표를 설계한다. 인증·인가 경계는 [[knowledge/authentication-state-and-authorization-boundaries]]와 함께 검토하고, 지속 연결에서의 블로킹 작업은 [[knowledge/blocking-work-in-async-systems]]와 분리해 본다.

## 선택의 한계
SSE·WebSocket·Pub/Sub 중 하나가 보편적으로 우월하다고 말하지 않는다. 요구되는 양방향성·내구성·운영 조건을 실제 서비스별로 확인한다.

## 근거
- [[blog/SPRING BOOT/Spring Boot- 10. Redis Pub-Sub 기반 실시간 알림 시스템]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조]]
- [[entities/projects/masil]]
