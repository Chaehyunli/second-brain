---
schema_version: 1
id: knowledge-transaction-boundary-and-execution-context
title: 트랜잭션 경계와 실행 컨텍스트
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation, java, spring-boot]
sources:
  - blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md
  - blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해.md
  - blog/INFLEARN/스프링 DB 2편 - 데이터 접근 활용 기술- 3. 데이터 접근 기술 - 테스트.md
---

# 트랜잭션 경계와 실행 컨텍스트

## 핵심
트랜잭션 원자성은 애너테이션 이름만으로 보장되지 않는다. 실제 DB 작업이 실행되는 스레드·스케줄러·테스트 경계에 맞춰 트랜잭션 범위를 잡아야 한다.

## 연결된 근거
- [[blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리.md]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해.md]]
- [[blog/INFLEARN/스프링 DB 2편 - 데이터 접근 활용 기술- 3. 데이터 접근 기술 - 테스트.md]]

## 적용 기준
선언형 트랜잭션·`TransactionTemplate`·테스트 롤백은 각각 실행 컨텍스트와 검증 목적이 다르다.

## 주의점 또는 한계
구체 프레임워크 동작은 버전·드라이버·리액티브/블로킹 경계에 따라 달라지므로 실제 실행 로그와 테스트로 확인한다.
