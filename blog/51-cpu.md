---
title: "[운영체제] CPU 스케줄링 이란??"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "OS"
published: 2025-04-09
source_url: https://ch010104.tistory.com/51
archive_method: Tistory sitemap + HTML content extraction
---

# [운영체제] CPU 스케줄링 이란??

> 원문: https://ch010104.tistory.com/51

## 본문

1. CPU 스케줄링 개요 1) CPU 스케줄링이란?  **준비 큐(Ready Queue)**에 있는 프로세스들 중에서, CPU를 어떤 순서로 할당할지 결정하는 과정- 준비 큐: 메모리에서 프로세스가 생성되면, OS 내에 PCB가 생성됨.  프로세스가 준비 상태이면 PCB가 준비 큐에 존재함.     운영체제 내 **단기 스케줄러(CPU Scheduler)**가 담당  2) CPU 스케줄링 알고리즘  다양한 **스케줄링 정책(Policy)**이 존재하며, 시스템의 특성과 요구사항에 따라 적절한 알고리즘을 선택해야 함.   2. CPU 스케줄링이 일어나는 시점     전이  상황 설명 선점 여부   ① 실행 → 대기 입출력 요청, 자식 프로세스 종료 대기 ❌ 비선점   ② 실행 → 준비 타이머 인터럽트 발생 등 ✅ 선점   ③ 대기 → 준비 입출력 종료 등 외부 이벤트 발생(입출력 종료 인터럽트) ✅ 선점   ④ 실행 → 종료 프로세스 종료 ❌ 비선점       📌  비선점: 프로세스가 자발적으로 CPU를 내려놓음(반환) 선점: 운영체제나 외부 이벤트가 CPU를 강제로 회수(빼앗김)   3. CPU 스케줄링 평가 기준 운영체제는 CPU 스케줄러를 통해 아래 목표들을 달성하려고 함.하지만 모든 목표를 동시에 만족시키기는 어렵기 때문에, 상황과 시스템에 맞는 우선순위를 정해야 함.     기준 설명   ① CPU 사용률 (Utilization) CPU가 실제로 사용된 비율 (0~100%) - CPU 사용시간 / 단위 시간   ② 처리량 (Throughput) 단위 시간당 완료된 프로세스 수 - 완료 프로세스 수/ 단위시간   ③ 반환 시간 (Turnaround Time) 프로세스가 도착해서 완전히 종료되기까지 걸린 총 시간   ④ 대기 시간 (Waiting Time) **Ready 상태(준비 큐)**에서 CPU를 기다린 총 시간 - 대기 상태와 상관 x   ⑤ 응답 시간 (Response Time) 요청 후 처음으로 실행(응답)이 시작될 때까지 걸린 시간     ⚠️ 용어 주의!  대기 시간(Waiting Time):→ 프로세스가 Ready 상태에서 CPU를 기다린 시간만 포함→ **I/O를 기다리는 대기 상태(Blocked/Waiting)**는 포함되지 않음!   4. 스케줄링 목표 예시 스케줄러는 아래의 5가지 목표를 만족해야함.  CPU 이용률을 최대화 처리량을 최대화 반환시간을 최소화 대기시간을 최소화 응답시간을 최소화  하지만, 이 5가지를 모두 충족하는 것은 불가능 -> 응용 분야에 따라서 적절한 목표를 결정해 선택     상황 중요한 목표   대화형 시스템 (채팅, 터미널 등) 평균 응답 시간 최소화   실시간 시스템 응답 시간의 일관성 (변동폭 최소화)   일괄 처리 시스템 높은 CPU 사용률, 많은 처리량       5. 스케줄링 알고리즘의 종류  FCFS (First-Come First-Served) SJF (Shortest Job First) RR (Round Robin) MQ (Multi-level Queue) MFQ (Multi-level Feedback Queue) HRN (Highest Response-rate Next)  스케줄러의 종류는 위와 같이 있다. 각각의 자세한 내용음 다음 글에서 알아보겠다.
