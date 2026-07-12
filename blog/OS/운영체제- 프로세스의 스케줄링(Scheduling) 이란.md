---
title: "[운영체제] 프로세스의 스케줄링(Scheduling) 이란?"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CS", "OS"]
category: "OS"
published: 2025-03-31
source_url: https://ch010104.tistory.com/33
---

# [운영체제] 프로세스의 스케줄링(Scheduling) 이란?

## 원문

https://ch010104.tistory.com/33

## 핵심 요약

- **1️⃣ 문맥 교환 (Context Switch)** — CPU가 현재 프로세스의 상태(CPU 레지스터 값 등)를 PCB에 저장하고, 다른 프로세스의 PCB 정보를 불러와 레지스터에 적재하는 과정
- **2️⃣ 프로세스 스케줄링** — 목적: CPU를 최대한 쉬지 않게 활용하기 위함
- **3️⃣ 스케줄링 큐 (Scheduling Queue)** — 운영체제는 스케줄링을 위해 PCB를 큐(Queue)로 관리함.
- **4️⃣ 프로세스 상태와 큐 이동** — 새 프로세스 → Ready Queue로 - 프로세스가 생성되면 Ready 상태가 되어 ready queue에 들어감.

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- 프로세스의 상태(Process State) 란|[운영체제] 프로세스의 상태(Process State) 란?]]
- [[blog/OS/운영체제- 프로세스 종료와 통신|[운영체제] 프로세스 종료와 통신]]
- [[blog/OS/운영체제- 프로세스(Process) 란|[운영체제] 프로세스(Process) 란?]]
