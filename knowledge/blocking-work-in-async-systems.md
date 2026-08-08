---
schema_version: 1
id: knowledge-blocking-work-in-async-systems
title: 비동기 시스템의 블로킹 작업 격리
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/OS/운영체제- 쓰레드(Thread) 란.md
  - blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리.md
  - blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md
---

# 비동기 시스템의 블로킹 작업 격리

## 핵심
동시성은 스레드 수를 늘리는 문제가 아니다. 블로킹 I/O와 희소 자원을 이벤트 루프에서 분리하고, 전환 뒤 컨텍스트 보존을 검증해야 한다.

## 연결된 근거
- [[blog/OS/운영체제- 쓰레드(Thread) 란.md]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리.md]]
- [[blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md]]

## 적용 기준
스레드의 자원 공유·전환 비용과 Postgres/JPA 작업의 `boundedElastic` 분리, ThreadLocal 트랜잭션의 제약을 근거로 한다.

## 주의점 또는 한계
스케줄러 선택만으로 처리량이 보장되지는 않으며 connection pool·backpressure·관측 지표를 함께 검증해야 한다.
