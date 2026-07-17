---
title: "[운영체제] CPU 스케줄링 이란??"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "CS", "OS"]
category: "OS"
published: 2025-04-09
source_url: https://ch010104.tistory.com/51
---

# [운영체제] CPU 스케줄링 이란??

## 원문

https://ch010104.tistory.com/51

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

**준비 큐(Ready Queue)**에 있는 프로세스들 중에서, CPU를 어떤 순서로 할당할지 결정하는 과정 - 준비 큐: 메모리에서 프로세스가 생성되면, OS 내에 PCB가 생성됨. 프로세스가 준비 상태이면 PCB가 준비 큐에 존재함.

운영체제 내 **단기 스케줄러(CPU Scheduler)**가 담당

## 원문 기반 개념 정리

### 1. CPU 스케줄링 개요

1) CPU 스케줄링이란?

**준비 큐(Ready Queue)**에 있는 프로세스들 중에서, CPU를 어떤 순서로 할당할지 결정하는 과정 - 준비 큐: 메모리에서 프로세스가 생성되면, OS 내에 PCB가 생성됨. 프로세스가 준비 상태이면 PCB가 준비 큐에 존재함.

운영체제 내 **단기 스케줄러(CPU Scheduler)**가 담당

2) CPU 스케줄링 알고리즘

다양한 **스케줄링 정책(Policy)**이 존재하며, 시스템의 특성과 요구사항에 따라 적절한 알고리즘을 선택해야 함.

### 2. CPU 스케줄링이 일어나는 시점

📌

비선점: 프로세스가 자발적으로 CPU를 내려놓음(반환)

선점: 운영체제나 외부 이벤트가 CPU를 강제로 회수(빼앗김)

### 3. CPU 스케줄링 평가 기준

운영체제는 CPU 스케줄러를 통해 아래 목표들을 달성하려고 함. 하지만 모든 목표를 동시에 만족시키기는 어렵기 때문에, 상황과 시스템에 맞는 우선순위를 정해야 함.

⚠️ 용어 주의!

대기 시간(Waiting Time): → 프로세스가 Ready 상태에서 CPU를 기다린 시간만 포함 → **I/O를 기다리는 대기 상태(Blocked/Waiting)**는 포함되지 않음!

### 4. 스케줄링 목표 예시

스케줄러는 아래의 5가지 목표를 만족해야함.

CPU 이용률을 최대화

처리량을 최대화

반환시간을 최소화

대기시간을 최소화

응답시간을 최소화

하지만, 이 5가지를 모두 충족하는 것은 불가능 -> 응용 분야에 따라서 적절한 목표를 결정해 선택

### 5. 스케줄링 알고리즘의 종류

FCFS (First-Come First-Served)

SJF (Shortest Job First)

RR (Round Robin)

MQ (Multi-level Queue)

MFQ (Multi-level Feedback Queue)

HRN (Highest Response-rate Next)

스케줄러의 종류는 위와 같이 있다.

각각의 자세한 내용음 다음 글에서 알아보겠다.

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- 쓰레드(Thread) 란|[운영체제] 쓰레드(Thread) 란??]]
- [[blog/OS/운영체제- CPU 스케줄링 알고리즘 이란|[운영체제] CPU 스케줄링 알고리즘 이란??]]
- [[blog/OS/운영체제- 프로세스의 동기화( 생산자 - 소비자 )란|[운영체제] 프로세스의 동기화( 생산자 - 소비자 )란?]]
