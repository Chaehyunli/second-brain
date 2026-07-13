---
title: "[클라우드 컴퓨터링] Haddop의 데이터 처리를 위한 MapReduce"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cloud", "hadoop", "mapreduce"]
category: "CLAUD COMPUTERING"
published: 2025-10-14
source_url: https://ch010104.tistory.com/160
---

# [클라우드 컴퓨터링] Haddop의 데이터 처리를 위한 MapReduce

## 원문

https://ch010104.tistory.com/160

## 핵심 요약

- **1. Hadoop의 개념과 구조** — Hadoop = 대규모 데이터를 저장(HDFS) + 처리(MapReduce) 하는 오픈소스 프레임워크
- **2. MapReduce의 등장 배경** — Google은 과거 수백 개의 맞춤형 분산 계산 프로그램을 사용
- **3. MapReduce의 개념적 모델** — 입력 데이터를 한 줄씩 읽어 (key, value) 형태의 중간 결과 생성
- **4. 예시 – WordCount** — Map: 입력 문장 → (단어, 1) 쌍 출력

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce 데이터 관리|[클라우드 컴퓨터링] MapReduce 데이터 관리]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce 데이터 흐름과 API|[클라우드 컴퓨터링] MapReduce 데이터 흐름과 API]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- MapReduce vs. 병렬 데이터베이스|[클라우드 컴퓨터링] MapReduce vs. 병렬 데이터베이스]]
