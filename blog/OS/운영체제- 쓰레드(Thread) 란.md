---
title: "[운영체제] 쓰레드(Thread) 란??"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CS", "OS"]
category: "OS"
published: 2025-04-07
source_url: https://ch010104.tistory.com/46
---

# [운영체제] 쓰레드(Thread) 란??

## 원문

https://ch010104.tistory.com/46

## 핵심 요약

- **1. 쓰레드란?** — **쓰레드(Thread)**는 CPU를 사용하는 최소 실행 단위이며, 프로세스 내에서 실행되는 작업 흐름
- **3. 단일 쓰레드 vs 다중 쓰레드** — Thread를 생성할 때마다, OS에 TCB를 생성함.
- **4. 쓰레드의 메모리 구조( 다중 쓰레드 )** — 쓰레드는 code, data, heap, open files를 공유
- **5. 쓰레드의 장점** — 빠른 응답성: 한 작업이 block되도 다른 작업은 계속 가능

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- CPU 스케줄링 이란|[운영체제] CPU 스케줄링 이란??]]
- [[blog/OS/운영체제- 프로세스 종료와 통신|[운영체제] 프로세스 종료와 통신]]
- [[blog/OS/운영체제- CPU 스케줄링 알고리즘 이란|[운영체제] CPU 스케줄링 알고리즘 이란??]]
