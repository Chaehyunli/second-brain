---
title: "[운영체제] 프로세서(Processor)의 모드? 메모리(Memory) 란?"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "CS", "OS"]
category: "OS"
published: 2025-03-12
source_url: https://ch010104.tistory.com/13
---

# [운영체제] 프로세서(Processor)의 모드? 메모리(Memory) 란?

## 원문

https://ch010104.tistory.com/13

## 핵심 요약

- **1. 프로세서 모드(Processor Mode)란?** — 프로세서의 권한 수준(privilege level)을 설정하는 개념으로, 실행할 수 있는 명령어의 종류를 제한함.
- **① 사용자 모드(User Mode)** — 제한된 명령어만 실행 가능 (예: I/O 접근, 특정 메모리 접근 불가).
- **② 커널 모드(Kernel Mode, Supervisor Mode, Privilege Mode)** — 운영체제(OS)와 같은 중요한 소프트웨어가 실행될 때 사용됨.
- **2) 프로세서 모드를 사용하는 이유** — 사용자 프로그램이 운영체제의 중요한 데이터 및 코드 영역을 변경하는 것을 방지.

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- 저장장치(Storage) 란- 캐싱(Cashng) 이란- 인터럽트(Interrupt) 란|[운영체제] 저장장치(Storage) 란? 캐싱(Cashng) 이란? 인터럽트(Interrupt) 란?]]
- [[blog/OS/운영체제- 운영체제(OS, Operating System)란|[운영체제] 운영체제(OS, Operating System)란?]]
- [[blog/OS/운영체제- 시스템 호출(System Call)과 운영체제|[운영체제] 시스템 호출(System Call)과 운영체제]]
