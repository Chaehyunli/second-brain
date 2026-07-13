---
title: "[클라우드 컴퓨터링] MapReduce 데이터 관리"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cloud", "hadoop", "mapreduce"]
category: "CLAUD COMPUTERING"
published: 2025-10-16
source_url: https://ch010104.tistory.com/163
---

# [클라우드 컴퓨터링] MapReduce 데이터 관리

## 원문

https://ch010104.tistory.com/163

## 핵심 요약

- **MapReduce 데이터 지역성 최적화 (Data Locality Optimization)** — 개념: 대용량 데이터를 계산이 필요한 곳으로 옮기는 대신, 계산 프로그램(코드)을 데이터가 저장된 곳으로 보내 처리하는 방식.
- **Hadoop 1.x 실행 구조 및 흐름** — Master: 메타데이터를 관리하는 Namenode와 어플리케이션 작업을 관리하는 JobTracker로 구성.
- **MapReduce 데이터 처리 단위** — MapReduce Job: 입력 데이터, MapReduce 프로그램, 설정 정보로 구성된 작업의 기본 단위.
- **Map Task와 Reduce Task의 특징** — 출력 데이터: 중간 결과물은 HDFS가 아닌 로컬 디스크에 저장됨.

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- Haddop의 데이터 처리를 위한 MapReduce|[클라우드 컴퓨터링] Haddop의 데이터 처리를 위한 MapReduce]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce 데이터 흐름과 API|[클라우드 컴퓨터링] MapReduce 데이터 흐름과 API]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce vs. 병렬 데이터베이스|[클라우드 컴퓨터링] MapReduce vs. 병렬 데이터베이스]]
