---
schema_version: 1
id: knowledge-transaction-boundary-and-execution-context
title: 트랜잭션 경계와 실행 컨텍스트
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation, java, spring-boot]
sources:
  - blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md
  - blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해.md
  - blog/INFLEARN/스프링 DB 2편 - 데이터 접근 활용 기술- 3. 데이터 접근 기술 - 테스트.md
---

# 트랜잭션 경계와 실행 컨텍스트

## 보장하려는 것
원자성은 애너테이션 이름이 아니라 실제 DB 작업이 같은 실행 컨텍스트에서 commit·rollback 경계에 묶일 때 확인된다.

## 경계가 실제로 놓이는 곳
선언형 `@Transactional`, `TransactionTemplate`, 테스트 롤백은 목적과 동작 위치가 다르다. 스레드·스케줄러·리액티브와 블로킹 경계를 넘으면 기대한 ThreadLocal 전파가 끊길 수 있다.

## 증상에서 원인으로
부분 반영, 롤백 누락, 테스트와 운영의 차이는 DB 작업의 실행 위치·드라이버·라이브러리 혼용을 먼저 확인해 진단한다.

## 테스트로 확인할 것
테스트 profile, 실제 DB, 롤백, 실행 로그를 확인한다. 블로킹 작업 격리는 [[knowledge/blocking-work-in-async-systems]]에서, 같은 접근 계층의 성능 문제는 [[knowledge/query-planning-index-and-pagination]]에서 분리해 다룬다.

## 스택별 불확실성
버전·드라이버·프레임워크가 달라지면 구체 동작도 달라진다. 이 노트는 실제 실행 검증을 대신하지 않는다.

## 근거
- [[blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해]]
- [[blog/INFLEARN/스프링 DB 2편 - 데이터 접근 활용 기술- 3. 데이터 접근 기술 - 테스트]]
