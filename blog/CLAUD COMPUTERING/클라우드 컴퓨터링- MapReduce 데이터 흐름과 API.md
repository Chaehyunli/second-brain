---
title: "[클라우드 컴퓨터링] MapReduce 데이터 흐름과 API"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cloud", "mapreduce"]
category: "CLAUD COMPUTERING"
published: 2025-10-21
source_url: https://ch010104.tistory.com/168
---

# [클라우드 컴퓨터링] MapReduce 데이터 흐름과 API

## 원문

https://ch010104.tistory.com/168

## 핵심 요약

- **MapReduce 데이터 흐름** — 단일 리듀스 태스크(Single Reduce Task)
- **MapReduce API** — setup(): 태스크 시작 시 1회 호출됨.
- **작업(Job) 및 매퍼(Mapper) 구성** — 입력 데이터의 총 크기와 HDFS 블록 크기에 따라 결정되는 입력 스플릿(Input Split)의 개수에 의해 정해짐.
- **작업(Job) 분석 및 실행** — Hadoop MapReduce 프로그램은 하나의 Job임.

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce 데이터 관리|[클라우드 컴퓨터링] MapReduce 데이터 관리]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- Haddop의 데이터 처리를 위한 MapReduce|[클라우드 컴퓨터링] Haddop의 데이터 처리를 위한 MapReduce]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce vs. 병렬 데이터베이스|[클라우드 컴퓨터링] MapReduce vs. 병렬 데이터베이스]]
