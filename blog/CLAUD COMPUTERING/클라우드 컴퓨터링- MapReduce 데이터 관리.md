---
title: "[클라우드 컴퓨터링] MapReduce 데이터 관리"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "cloud", "hadoop", "mapreduce"]
category: "CLAUD COMPUTERING"
published: 2025-10-16
source_url: https://ch010104.tistory.com/163
---

# [클라우드 컴퓨터링] MapReduce 데이터 관리

## 원문

https://ch010104.tistory.com/163

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

개념: 대용량 데이터를 계산이 필요한 곳으로 옮기는 대신, 계산 프로그램(코드)을 데이터가 저장된 곳으로 보내 처리하는 방식.

목표: 상대적으로 부족한 자원인 네트워크 대역폭 사용을 최소화.

## 원문 기반 개념 정리

### MapReduce 데이터 지역성 최적화 (Data Locality Optimization)

개념: 대용량 데이터를 계산이 필요한 곳으로 옮기는 대신, 계산 프로그램(코드)을 데이터가 저장된 곳으로 보내 처리하는 방식.

목표: 상대적으로 부족한 자원인 네트워크 대역폭 사용을 최소화.

스케줄링 우선순위: Master는 데이터의 위치를 고려하여 Map Task를 스케줄링함.

1순위 (Data-Local): 데이터 블록이 위치한 노드(Node)와 동일한 노드에서 Map Task를 실행.

2순위 (Rack-Local): 1순위가 불가능할 경우, 데이터 블록과 동일한 랙(Rack)에 있는 다른 노드에서 Task를 실행.

3순위 (Off-Rack): 1, 2순위가 모두 불가능하면, 데이터 블록과 다른 랙에 있는 노드에서 Task를 실행.

### Hadoop 1.x 실행 구조 및 흐름

구성 요소:

Master: 메타데이터를 관리하는 Namenode와 어플리케이션 작업을 관리하는 JobTracker로 구성.

Slave Node: 실제 데이터 블록을 저장하는 datanode daemon과 실제 Task를 수행하는 tasktracker로 구성.

작업 제출 및 실행 과정:

작업 요청 (1-4단계): 사용자가 MapReduce program을 실행하면 JobClient가 JobTracker에게 새로운 Job ID를 받고 작업을 제출.

작업 초기화 (5단계): JobTracker가 작업을 초기화.

입력 데이터 정보 검색 (6단계): JobTracker는 HDFS의 Namenode와 통신하여 처리할 데이터가 어떻게 조각(Input Split)나서 어디에 저장되어 있는지 정보를 가져옴.

Task 할당 (7단계): TaskTracker는 주기적으로 JobTracker에게 하트비트(heartbeat)를 보내 자신의 상태를 알리고, JobTracker는 가장 적합한 TaskTracker에게 Task를 할당.

Task 수행 (8-10단계): 할당받은 TaskTracker는 HDFS에서 필요한 리소스(프로그램 등)를 가져와 별도의 child JVM 공간에서 실제 Map 또는 Reduce 작업을 실행.

### MapReduce 데이터 처리 단위

MapReduce Job: 입력 데이터, MapReduce 프로그램, 설정 정보로 구성된 작업의 기본 단위.

Input Split: MapReduce Job의 입력 데이터를 고정된 크기로 나눈 조각으로, 각 Input Split마다 하나의 Map Task가 할당됨.

최적의 Input Split 크기: HDFS 블록 크기(예: 64MB)와 동일하게 설정하는 것이 가장 효율적.

이유: HDFS 블록은 하나의 노드에 저장되는 것을 보장하는 가장 큰 데이터 단위이기 때문. 만약 Split이 여러 블록에 걸쳐 있으면, 다른 노드에 있는 데이터를 네트워크를 통해 전송해야 하므로 데이터 지역성의 이점이 사라짐.

주의: Split 크기가 너무 작으면, 수많은 Task를 생성하고 관리하는 오버헤드가 실제 데이터 처리 시간보다 커질 수 있음.

### Map Task와 Reduce Task의 특징

Map Task:

출력 데이터: 중간 결과물은 HDFS가 아닌 로컬 디스크에 저장됨. HDFS에 복제본과 함께 저장하는 것은 과도한 오버헤드이기 때문.

장애 복구: Task 실패 시, HDFS에 원본 데이터가 안전하게 보관되어 있으므로 다른 노드에서 Task를 재실행하면 됨.

Reduce Task:

데이터 지역성: Map Task의 정렬된 결과물들을 네트워크를 통해 가져와야 하므로 데이터 지역성의 이점을 누릴 수 없음.

출력 데이터: 최종 결과물은 영구적으로 보존되어야 하므로 안정성을 위해 HDFS에 저장됨.

개수 결정: Map Task의 개수는 입력 데이터의 크기에 따라 자동 결정되지만, Reduce Task의 개수는 사용자가 직접 지정함.

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- Haddop의 데이터 처리를 위한 MapReduce|[클라우드 컴퓨터링] Haddop의 데이터 처리를 위한 MapReduce]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce 데이터 흐름과 API|[클라우드 컴퓨터링] MapReduce 데이터 흐름과 API]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce vs. 병렬 데이터베이스|[클라우드 컴퓨터링] MapReduce vs. 병렬 데이터베이스]]
