---
title: "[백준(Python)] 파이썬 자료형 - List, Deque, Heap, Dictionary, Set"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "BACKJOON"
published: 2026-03-12
source_url: https://ch010104.tistory.com/217
---

# [백준(Python)] 파이썬 자료형 - List, Deque, Heap, Dictionary, Set

## 원문

https://ch010104.tistory.com/217

## 노트 유형

`guide`

## 적용 목적과 전제조건

특징: 순서가 있고 수정 가능함. pop()을 쓰면 스택처럼 뒤에서부터 뺄 수 있음.

시간 복잡도: 맨 뒤 삽입/삭제는 O(1), 중간 삽입/삭제는 O(N)

## 구현 절차·검증·주의점

### 1. 리스트 (List) - 가장 기본

가장 많이 쓰이며, 스택(Stack) 기능을 포함.

특징: 순서가 있고 수정 가능함. pop()을 쓰면 스택처럼 뒤에서부터 뺄 수 있음.

시간 복잡도: 맨 뒤 삽입/삭제는 O(1), 중간 삽입/삭제는 O(N)

import: 필요 없음.

```text
# 선언 및 초기화
arr = [1, 2, 3]
graph = [0] * 10 # 크기가 10인 0으로 채워진 리스트 (자주 쓰임)

# 추가 및 삭제
arr.append(4)    # 맨 뒤 추가 [1, 2, 3, 4]
arr.pop()        # 맨 뒤 삭제 [1, 2, 3]

# 슬라이싱 (부분 추출)
print(arr[0:2])  # [1, 2]
```

### 2. 덱 (Deque) - BFS 필수템

큐(Queue)를 구현할 때 리스트(pop(0))를 쓰면 O(N)이라 느려짐

반드시 deque를 써야 O(1)로 해결

특징: 양방향에서 삽입/삭제 가능.

import: from collections import deque

```text
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)      # 오른쪽 추가
queue.appendleft(0)  # 왼쪽 추가
queue.popleft()      # 왼쪽에서 꺼내기 (BFS의 핵심)
queue.pop()          # 오른쪽에서 꺼내기
```

### 3. 힙 (Heap) - 우선순위 큐

다익스트라(최단거리) 알고리즘이나 상위 K번째 요소를 찾을 때 필수

특징: 항상 가장 작은 값(최솟값)이 맨 앞에 옴 (최소 힙).

import: import heapq

```text
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

# 가장 작은 값 꺼내기
print(heapq.heappop(heap)) # 1 (자동으로 정렬되어 나옴)

# 최대 힙을 만들고 싶을 땐 값을 음수로 바꿔서 넣음
# heapq.heappush(heap, -value)
```

### 4. 딕셔너리 (Dictionary) - 해시 맵

특정 데이터를 키(Key)값으로 빠르게 조회해야 할 때 씁니다.

특징: Key-Value 쌍. 중복된 데이터를 세거나 카테고리별 분류 시 유용.

시간 복잡도: 삽입/조회 O(1).

import: 필요 없음 (단, defaultdict나 Counter는 collections에서 가져옴).

```text
# 기본 딕셔너리
info = {"name": "python", "level": 5}

# Counter (리스트 요소 개수 세기)
from collections import Counter
counts = Counter([1, 1, 2, 2, 2, 3])
print(counts) # Counter({2: 3, 1: 2, 3: 1}) - 2가 3개 있다는 뜻
```

### 5. 집합 (Set)

중복을 허용하지 않고, 특정 원소가 있는지 확인할 때 매우 빠릅니다.

특징: 순서 없음, 중복 불가능.

시간 복잡도: 조회( in ) O(1). 리스트의 O(N)보다 압도적으로 빠름.

import: 필요 없음.

```text
s = set([1, 2, 2, 3, 3, 3])
print(s) # {1, 2, 3} (중복 자동 제거)

if 2 in s: # 조회 속도가 매우 빠름
    print("존재함")
```

## 관련 글

- [[blog/BACKJOON/index|BACKJOON]]
- [[blog/BACKJOON/백준(Python)- BFS vs DFS|[백준(Python)] BFS vs DFS]]
- [[blog/BACKJOON/백준(Python)- Input()|[백준(Python)] Input()]]
- [[blog/BACKJOON/백준(Python)- while - else, for - else 문|[백준(Python)] while - else, for - else 문]]
