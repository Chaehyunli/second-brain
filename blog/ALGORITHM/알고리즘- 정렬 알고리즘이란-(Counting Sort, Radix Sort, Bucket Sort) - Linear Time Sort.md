---
title: "[알고리즘] 정렬 알고리즘이란?(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Algorithm", "Sort"]
category: "ALGORITHM"
published: 2025-09-15
source_url: https://ch010104.tistory.com/127
---

# [알고리즘] 정렬 알고리즘이란?(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort

## 원문

https://ch010104.tistory.com/127

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

정리 8.1: 모든 비교 기반 정렬 알고리즘은 최악의 경우 Ω(n lg n)번의 비교가 필요

완전 이진 트리에서 n!개의 리프 노드를 갖기 위해서는 높이가 최소 ⌈lg(n!)⌉ ≈ n lg n

## 원문 기반 개념 정리

### 비교 기반 정렬의 한계

주요 비교 기반 정렬 알고리즘들과 시간복잡도

비교 기반 정렬의 이론적 하한선

정리 8.1: 모든 비교 기반 정렬 알고리즘은 최악의 경우 Ω(n lg n)번의 비교가 필요

증명의 핵심 아이디어:

결정 트리(Decision Tree)를 사용한 분석

n개 원소의 가능한 순열은 n!개

완전 이진 트리에서 n!개의 리프 노드를 갖기 위해서는 높이가 최소 ⌈lg(n!)⌉ ≈ n lg n

따라서 최악의 경우 Ω(n lg n)번의 비교가 필요

### Linear Time Sorting

비교 기반 정렬의 한계를 넘어서려면 비교가 아닌 다른 방식을 사용해야 Gㅏㅁ

특정 제약 조건 하에서 O(n) 시간에 정렬이 가능한 알고리즘들이 있음

1. Counting Sort

조건

입력 원소들이 0부터 k까지의 정수 범위에 있을 때

k = O(n)인 경우 O(n) 시간에 정렬 가능

알고리즘 과정

```text
COUNTING-SORT(A, n, k)
1. B[1:n]과 C[0:k] 배열 생성
2. for i = 0 to k: C[i] = 0
3. for j = 1 to n: C[A[j]] = C[A[j]] + 1
4. for i = 1 to k: C[i] = C[i] + C[i-1]
5. for j = n downto 1:
   B[C[A[j]]] = A[j]
   C[A[j]] = C[A[j]] - 1
```

핵심 특징

Stable Sort: 동일한 값을 가진 원소들의 상대적 순서가 유지됨

시간복잡도: Θ(k + n)

Counting Sort는 unstable sort임

2. Radix Sort

기본 아이디어

d자리 숫자들을 각 자릿수별로 정렬

중요: 가장 낮은 자릿수부터 시작 (LSD: Least Significant Digit first)

예시 (3자리 숫자)

```text
초기: 329, 457, 657, 839, 436, 720, 355

1의 자리로 정렬: 720, 355, 436, 457, 657, 329, 839
10의 자리로 정렬: 720, 329, 436, 839, 355, 457, 657
100의 자리로 정렬: 329, 355, 436, 457, 657, 720, 839
```

알고리즘

```text
RADIX-SORT(A, n, d)
1. for i = 1 to d
2.   use stable sort to sort array A[1:n] on digit i
```

시간복잡도

Θ(d(n + k)) where k는 각 자릿수의 범위

10진수의 경우: Θ(d(n + 10)) = Θ(d·n)

3. Bucket Sort

조건

n개의 숫자가 [0, 1) 구간에서 균등 분포(uniform distribution)를 따른다고 가정

기본 아이디어

[0, 1) 구간을 n개의 동일한 크기 버킷으로 분할: [0, 1/n), [1/n, 2/n), ..., [(n-1)/n, 1)

각 원소를 해당 버킷에 삽입

각 버킷을 개별적으로 정렬 (보통 Insertion Sort 사용)

버킷들을 순서대로 연결

알고리즘

```text
BUCKET-SORT(A, n)
1. B[0:n-1] 버킷 배열 생성
2. for i = 0 to n-1: B[i]를 빈 리스트로 초기화
3. for i = 1 to n: A[i]를 리스트 B[⌊n·A[i]⌋]에 삽입
4. for i = 0 to n-1: 리스트 B[i]를 insertion sort로 정렬
5. 리스트들을 B[0], B[1], ..., B[n-1] 순서로 연결
```

시간복잡도

평균의 경우: Θ(n)

최악의 경우: Θ(n²) (모든 원소가 한 버킷에 들어가는 경우)

이론적 근거

균등 분포 가정 하에서 각 버킷에 들어가는 원소의 기댓값은: E[n²ᵢ] = 2 - 1/n ≈ 2 (상수)

정리

Linear Time Sorting 알고리즘들은 각각 특정한 조건 하에서 O(n) 성능을 달성할 수 있음

Counting Sort: 정수 범위가 제한적일 때

Radix Sort: 고정된 자릿수를 가진 데이터일 때

Bucket Sort: 데이터가 균등 분포를 따를 때

이들은 비교 기반 정렬의 Ω(n lg n) 하한선을 넘어서는 강력한 도구들이지만, 각각의 제약 조건을 만족해야 함

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- k번째 원소 찾기 (Selection Algorithm)|[알고리즘] k번째 원소 찾기 (Selection Algorithm)]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Merge Sort, Heap Sort, Quick Sort)|[알고리즘] 정렬 알고리즘이란?(Merge Sort, Heap Sort, Quick Sort)]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Insertion Sort, Bubble Sort)|[알고리즘] 정렬 알고리즘이란?(Insertion Sort, Bubble Sort)]]
