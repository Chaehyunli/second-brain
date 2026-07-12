---
title: "[운영체제] 프로세스의 상태(Process State) 란?"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CS", "OS"]
category: "OS"
published: 2025-03-26
source_url: https://ch010104.tistory.com/27
---

# [운영체제] 프로세스의 상태(Process State) 란?

## 원문

https://ch010104.tistory.com/27

## 핵심 요약

- **1. 다중 프로그래밍 (Multiprogramming)** — 정의: 여러 작업을 메모리에 동시에 올려두고, CPU가 놀지 않도록 다른 작업을 실행하는 기법 - 예를 들어, CPU가 입출력 장치 작업(프린터기 복사)을 하고 있다고 하면, 이는 매우 오래 걸리는 작업이기 때문에 해당 프로세스를 Waiting 상태로 돌림(이후, CPU가 입출력 완료 인터럽트를 받게 되면 다시 Ready 상태로 전환).
- **2. 시분할 시스템 (Timesharing) / 멀티태스킹 (Multitasking)** — 정의: 여러 프로세스(또는 사용자)가 CPU 시간을 분할해서 번갈아 사용하는 방식
- **3. 프로세스 상태 (Process States)** — 한순간에 CPU는 오직 하나의 프로세스만 실행할 수 있음
- **4. 프로세스 상태 변화 예시( I/O 요청 발생 )** — PID=1이 CPU에서 실행 중 (Running)

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- 프로세스(Process) 란|[운영체제] 프로세스(Process) 란?]]
- [[blog/OS/운영체제- 사용자 인터페이스와 운영체제|[운영체제] 사용자 인터페이스와 운영체제]]
- [[blog/OS/운영체제- 프로세스의 스케줄링(Scheduling) 이란|[운영체제] 프로세스의 스케줄링(Scheduling) 이란?]]
