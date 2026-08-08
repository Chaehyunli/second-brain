---
schema_version: 1
id: knowledge-blocking-work-in-async-systems
title: 비동기 시스템의 블로킹 작업 격리
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/OS/운영체제- 쓰레드(Thread) 란.md
  - blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리.md
  - blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md
---

# 비동기 시스템의 블로킹 작업 격리

## 관찰할 실패 신호
이벤트 루프에서 동기 DB·파일·외부 호출이 길게 점유되면 지연이 함께 늘고, 스레드 전환 뒤 트랜잭션·진단 정보가 사라질 수 있다.

## 실행 모델과 자원 경계
스레드는 자원을 공유하지만 전환 비용을 가진다. `boundedElastic` 같은 별도 스케줄러는 동기 Postgres/JPA 작업을 이벤트 루프에서 분리하는 수단이지, connection pool·대기열의 한계를 없애는 수단은 아니다.

## 격리 패턴
블로킹 작업의 위치를 먼저 식별하고, 전용 풀·큐·스케줄러로 옮긴다. 이어서 풀 크기, DB 연결 수, backpressure를 같은 부하 가정에서 맞춘다.

## 컨텍스트 단절 진단
WebFlux에서 ThreadLocal 기반 트랜잭션은 스레드 이동과 함께 기대대로 전파되지 않을 수 있다. 이 실행 의미론은 [[knowledge/transaction-boundary-and-execution-context]]에서 원자성·테스트 경계와 함께 확인한다.

## 부하 검증과 불확실성
격리 전후의 지연, 대기열, 연결 풀 포화, 오류율을 실제 실행으로 비교한다. 스케줄러 이름만으로 처리량이나 트랜잭션 전파를 보장한다고 결론내리지 않는다.

## 근거
- [[blog/OS/운영체제- 쓰레드(Thread) 란]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리]]
