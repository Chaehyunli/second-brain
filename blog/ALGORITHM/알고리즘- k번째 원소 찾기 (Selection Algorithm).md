---
title: "[알고리즘] k번째 원소 찾기 (Selection Algorithm)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Algorithm", "Sort"]
category: "ALGORITHM"
published: 2025-09-18
source_url: https://ch010104.tistory.com/132
---

# [알고리즘] k번째 원소 찾기 (Selection Algorithm)

## 원문

https://ch010104.tistory.com/132

## 핵심 요약

- 주어진 데이터 묶음에서 특정 순서에 있는 값을 찾아야 할 때가 많음
- **1. 무작위 분할을 이용한 선택 (Randomized-Select)** — 퀵 정렬(Quick Sort)과 유사한 아이디어를 사용하지만, 더 효율적으로 동작
- **2. 결정론적 선택 (Deterministic-Select) - "중간값들의 중간값"** — "항상 좋은" 피벗을 고르는 결정론적 방법이 고안
- **결론** — 선택 알고리즘은 특정 순위의 데이터를 효율적으로 찾는 강력한 도구

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort|[알고리즘] 정렬 알고리즘이란?(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Merge Sort, Heap Sort, Quick Sort)|[알고리즘] 정렬 알고리즘이란?(Merge Sort, Heap Sort, Quick Sort)]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Insertion Sort, Bubble Sort)|[알고리즘] 정렬 알고리즘이란?(Insertion Sort, Bubble Sort)]]
