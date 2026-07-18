---
title: "[알고리즘] 재귀란? (일반 재귀 vs 꼬리 재귀)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Algorithm"]
category: "ALGORITHM"
published: 2025-09-22
source_url: https://ch010104.tistory.com/135
---

# [알고리즘] 재귀란? (일반 재귀 vs 꼬리 재귀)

## 원문

https://ch010104.tistory.com/135

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

큰 문제를 동일한 구조의 더 작은 문제로 나누고, 가장 작은 단위의 문제(종료 조건)에 도달했을 때부터 차례대로 답을 구해 전체 문제의 답을 찾아가는 방식

만약 종료 조건이 없다면 함수는 무한히 자기 자신을 호출하게 되어 '스택 오버플로(Stack Overflow)' 오류를 발생

## 원문 기반 개념 정리

### 재귀(Recursion)란 무엇일까?

큰 문제를 동일한 구조의 더 작은 문제로 나누고, 가장 작은 단위의 문제(종료 조건)에 도달했을 때부터 차례대로 답을 구해 전체 문제의 답을 찾아가는 방식

가장 중요한 것은 종료 조건(Base Case)

만약 종료 조건이 없다면 함수는 무한히 자기 자신을 호출하게 되어 '스택 오버플로(Stack Overflow)' 오류를 발생

재귀는 어디에 사용될까? (재귀의 응용)

정렬: 퀵 소트(Quick Sort), 병합 정렬(Merge Sort)

탐색: 이진 탐색(Binary Search)

수학적 계산: 팩토리얼(Factorial), 피보나치 수열(Fibonacci)

트리/그래프 탐색: 깊이 우선 탐색(DFS), 트리 순회(Tree Traversal)

분할 정복: 하노이의 탑(Hanoi Tower), 카라츠바 곱셈(Karatsuba Multiplication)

### 일반 재귀의 문제점과 '꼬리 재귀(Tail Recursion)'

일반적인 재귀 함수는 리소스를 많이 차지하는 단점

함수가 호출될 때마다 해당 함수의 상태(지역 변수, 반환 주소 등)가 스택(Stack) 메모리에 계속해서 쌓이기 때문

예를 들어 factorial(10)을 호출하면 factorial(9), factorial(8)... 순서로 스택에 쌓이고, factorial(1)이 1을 반환한 후에야 쌓였던 스택들이 차례로 반환

이러한 문제를 해결하기 위해 꼬리 재귀(Tail Recursion) 개념이 등장

꼬리 재귀란?: - 함수의 가장 마지막 동작이 자기 자신을 호출하는 형태의 재귀 - 핵심 특징: 재귀 호출 이후에 어떠한 추가 연산도 수행하지 않음

장점: - 컴파일러가 '꼬리 호출 최적화(Tail Call Optimization, TCO)'를 통해 스택 프레임을 재사용하도록 코드를 최적화 - 꼬리 재귀는 반복문과 동일한 성능을 낼 수 있음

예제로 비교하기: Factorial

1. 일반 재귀 (Standard Recursion)

- 재귀 호출 이후 n * 연산이 남아있음

```text
long long factorial (int n) {
    if (n==0) return 1;
    return n * factorial (n-1); [cite: 59]
}
```

호출 스택 (factorial(3)):

factorial(3) → 3 * factorial(2)

factorial(2) → 2 * factorial(1)

factorial(1) = 1

2. 꼬리 재귀 (Tail Recursion)

- 함수의 마지막 동작이 오직 자기 자신을 호출하는 것

- 중간 결괏값을 누산기(accumulator,acc)를 통해 전달

```text
long long factorial_tail(int n, long long acc) {
    if (n==0) return acc; [cite: 77]
    return factorial_tail(n-1, acc * n); [cite: 78]
}
```

동작 방식 (f_tail(3, 1)):

f_tail(3, 1) → f_tail(2, 3) → f_tail(1, 6) → 6

컴파일러가 TCO를 지원하면, 새로운 스택을 쌓지 않고 하나의 스택 프레임만 유지하며 동작

3. 반복문 (Iteration)

- 가장 일반적인 구현 방식

```text
long long factorial_iter (int n) {
    long long res = 1; [cite: 93, 94]
    for (int i=1; i<=n; i++) res *= i; [cite: 95, 96]
    return res; [cite: 97]
}
```

성능 비교 및 결론

- 이론적으로 꼬리 재귀는 컴파일러 최적화가 적용될 경우 반복문과 같은 성능을 보임

- 이를 통해 재귀의 단점인 스택 오버플로를 방지할 수 있음

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- k번째 원소 찾기 (Selection Algorithm)|[알고리즘] k번째 원소 찾기 (Selection Algorithm)]]
- [[blog/ALGORITHM/알고리즘- 정렬 알고리즘이란-(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort|[알고리즘] 정렬 알고리즘이란?(Counting Sort, Radix Sort, Bucket Sort) - Linear Time Sort]]
- [[blog/ALGORITHM/알고리즘- 백트래킹을 이용한 순열-조합 및 알고리즘 성능 분석(Big-O, Omega, Theta)|[알고리즘] 백트래킹을 이용한 순열/조합 및 알고리즘 성능 분석(Big-O, Omega, Theta)]]
