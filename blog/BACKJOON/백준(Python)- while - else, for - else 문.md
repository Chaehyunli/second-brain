---
title: "[백준(Python)] while - else, for - else 문"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Python"]
category: "BACKJOON"
published: 2026-03-17
source_url: https://ch010104.tistory.com/230
---

# [백준(Python)] while - else, for - else 문

## 원문

https://ch010104.tistory.com/230

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

조건식이 False가 되어 반복문이 정상적으로 종료될 때 else 블록이 실행

리스트나 범위(range)를 끝까지 다 훑었을 때 else 블록이 실행

## 원문 기반 개념 정리

핵심 원리: break를 만나면 else는 실행되지 않음

### 1. while - else 문

조건식이 False가 되어 반복문이 정상적으로 종료될 때 else 블록이 실행

사용 예시: 설탕 배달 문제 (정확한 봉지 구성 찾기)

```text
n = int(input()) # 예: 7
count = 0

while n >= 0:
    if n % 5 == 0:
        print(count + n // 5)
        break  # <--- 성공! 여기서 탈출하면 else는 무시됨
    n -= 3
    count += 1
else:
    # n이 0보다 작아질 때까지 break를 못 만난 경우
    print("-1 (정확하게 나눌 수 없습니다)")
```

### 2. for - else 문

리스트나 범위(range)를 끝까지 다 훑었을 때 else 블록이 실행

사용 예시: 소수(Prime Number) 판별

```text
num = 13

for i in range(2, num):
    if num % i == 0:
        print(f"{num}은(는) 소수가 아닙니다.")
        break  # <--- 나누어떨어지는 수를 찾으면 탈출 (else 실행 안 함)
else:
    # 2부터 num-1까지 한 번도 나누어떨어지지 않은 경우
    print(f"{num}은(는) 소수입니다!")
```

### 3. 한눈에 비교하는 실행 흐름

## 관련 글

- [[blog/BACKJOON/index|BACKJOON]]
- [[blog/BACKJOON/백준(Python)- Input()|[백준(Python)] Input()]]
- [[blog/PYTHON/Python- Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트|[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트]]
- [[blog/CODINGTEST/코딩테스트- 현대오토 2026-04-05 회고|[코딩테스트] 현대오토 2026-04-05 회고]]
