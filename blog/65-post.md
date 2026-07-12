---
title: "[운영체제] 임계 구역 문제 란??"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "OS"
published: 2025-04-30
source_url: https://ch010104.tistory.com/65
archive_method: Tistory sitemap + HTML content extraction
---

# [운영체제] 임계 구역 문제 란??

> 원문: https://ch010104.tistory.com/65

## 본문

1. 임계 구역(Critical Section) 이란?  임계 구역: 여러 프로세스가 공유 데이터를 접근하는 코드 영역 각 프로세스는 자신만의 임계 구역을 가지고 있으며, 동시에 여러 프로세스가 이 구역을 실행하면 안 됨 반드시 **시간적으로 상호 배타적(Mutual Exclusive)**으로 실행되어야 함  🔁 프로세스 Pi의 구조   repeat entry section // 진입: 임계 구역에 들어가기 위한 요청 critical section // 임계 구역 exit section // 종료: 임계 구역을 벗어났음을 알림 remainder section // 나머지 코드 until false    2. 임계 구역 문제의 세 가지 요구 조건  임계 구역 문제를 해결하기 위해서는 아래 세 가지 조건을 반드시 만족해야 함.       조건 설명   1. 상호 배제 (Mutual Exclusion) 한 번에 하나의 프로세스만 임계 구역에 들어갈 수 있어야 함   2. 진행 (Progress) 임계 구역에 아무도 없고 진입을 원하는 프로세스가 있을 경우, 이들 중 하나가 반드시 들어가야 함 (무한정 대기 금지)   3. 한계 대기 (Bounded Waiting) 어떤 프로세스도 무한히 기다리게 해서는 안 됨. 즉, 유한한 횟수 안에 임계 구역에 들어가야 함       3. 임계 구역 해결 기법 1) 피터슨(Peterson) 알고리즘  두 개의 프로세스만 허용되는 상황에서 사용 flag[]: 임계 구역에 들어갈 준비 상태 표시 turn: 누가 다음 차례인지 명시   // Pi의 코드 do { flag[i] = true; turn = j; while (flag[j] && turn == j); // 대기 // 임계 구역 flag[i] = false; // 잔류 구역 } while (true);   특징: 단순한 공유 변수만으로 동기화를 구현하며, 세 가지 요구 조건 모두 만족   2) 세마포어(Semaphore)  정수 변수 S와 두 개의 원자적 연산으로 구성됨 연산 종류:  wait(S) 또는 P(S) signal(S) 또는 V(S)      wait(S) { while (S <= 0); // 대기 S--; } signal(S) { S++; }     세마포어 종류      종류 설명   Binary 세마포어 (Mutex) 0 또는 1만 가짐. 상호 배제를 위한 간단한 락으로 사용   Counting 세마포어 0 이상 정수 사용. 동시에 N개의 프로세스가 접근 가능      예시: 공유 자원 접근 보호   Semaphore s = 1; wait(s); // 임계 구역 signal(s);    ⚠️ 세마포어 문제점: 교착 상태(Deadlock) 발생 가능   // P0 wait(S); wait(Q); // ... signal(S); signal(Q); // P1 wait(Q); wait(S); // ... signal(Q); signal(S);   이와 같이 서로 자원을 점유한 채 상대방의 signal을 기다리면 무한 대기가 발생   3) 모니터(Monitor)  고급 언어 수준에서 제공되는 동기화 기법 클래스와 유사한 구조지만, 한 번에 하나의 프로세스만 진입 가능 프로그래머가 직접 락(lock)을 관리할 필요 없음  문법 예시   monitor MonitorName { shared variables procedure P1(...) { ... } procedure P2(...) { ... } Initialization code { ... } }    장점: 코드의 안전성과 가독성이 높으며, 병행 제어를 자동으로 처리해줌
