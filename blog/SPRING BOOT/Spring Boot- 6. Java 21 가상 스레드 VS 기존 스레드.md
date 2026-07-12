---
title: "[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/200
---

# [Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드

## 원문

https://ch010104.tistory.com/200

## 핵심 요약

- **등장 배경: 기존 스레드의 한계** — 기존의 Java 스레드(Platform Thread)는 OS 스레드와 1:1로 매핑됩니다.
- **가상 스레드(Virtual Thread)란?** — JVM이 관리하는 경량 논리 단위로, OS 스레드와 직접 연결되지 않습니다.
- **주요 특징 요약** — 특징 기존 스레드 (Platform) 가상 스레드 (Virtual)
- **2. Java 코드 비교 (직접 사용할 때)** — 기존에는 스레드를 아껴 쓰기 위해 **풀링(Pooling)**을 했지만, 가상 스레드는 작업당 하나씩(Per-task) 던지는 것이 핵심입니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
