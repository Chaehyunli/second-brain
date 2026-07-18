---
title: "[백준(Python)] BFS vs DFS"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "BFS", "dfs", "Pthon"]
category: "BACKJOON"
published: 2026-03-12
source_url: https://ch010104.tistory.com/216
---

# [백준(Python)] BFS vs DFS

## 원문

https://ch010104.tistory.com/216

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

BFS는 시작 노드에서 가까운 노드부터 차례대로 탐색합니다. 파이썬에서는 collections.deque를 사용하는 것이 속도면에서 가장 효율적입니다.

DFS는 한 방향으로 갈 수 있을 때까지 깊게 가다가, 막히면 다시 돌아와서 다른 길을 찾습니다.

## 원문 기반 개념 정리

### 1. BFS (너비 우선 탐색) - 큐(Queue) 활용

BFS는 시작 노드에서 가까운 노드부터 차례대로 탐색합니다. 파이썬에서는 collections.deque를 사용하는 것이 속도면에서 가장 효율적입니다.

```python
from collections import deque

def bfs(graph, start, visited):
    # 1. 시작 노드를 큐에 넣고 방문 처리
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 2. 큐에서 하나의 원소를 뽑아 출력 (가장 먼저 들어온 것)
        v = queue.popleft()
        print(v, end=' ')

        # 3. 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 큐에 추가
                visited[i] = True # 방문 처리
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 2. DFS (깊이 우선 탐색) - 재귀(Recursion) 활용

DFS는 한 방향으로 갈 수 있을 때까지 깊게 가다가, 막히면 다시 돌아와서 다른 길을 찾습니다.

```python
def dfs(graph, v, visited):
    # 1. 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 2. 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            # 방문하지 않은 인접 노드가 있다면 바로 파고들기
            dfs(graph, i, visited)
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 3. 전체 실행 예시 (그래프 구성)

아래와 같은 연결 상태를 가진 그래프가 있다고 가정해 보겠습니다.

```text
# 각 노드가 연결된 정보를 리스트로 표현 (2차원 리스트)
# 0번 노드는 비워두고 1번 노드부터 사용합니다.
graph = [
    [],
    [2, 3, 8],  # 1번 노드와 연결된 노드들
    [1, 7],     # 2번 노드와 연결된 노드들
    [1, 4, 5],  # 3번 노드와 연결된 노드들
    [3, 5],     # 4번 노드와 연결된 노드들
    [3, 4],     # 5번 노드와 연결된 노드들
    [7],        # 6번 노드와 연결된 노드들
    [2, 6, 8],  # 7번 노드와 연결된 노드들
    [1, 7]      # 8번 노드와 연결된 노드들
]

# 각 노드가 방문된 정보를 리스트로 표현 (기본값 False)
visited_bfs = [False] * 9
visited_dfs = [False] * 9

print("BFS 탐색 결과:", end=' ')
bfs(graph, 1, visited_bfs)
# 출력: 1 2 3 8 7 4 5 6 (가까운 곳부터 넓게 탐색)

print("\nDFS 탐색 결과:", end=' ')
dfs(graph, 1, visited_dfs)
# 출력: 1 2 7 6 8 3 4 5 (한 놈만 끝까지 패며 탐색)
```

### 💡 핵심 요약

BFS (Queue): "내 주변부터 다 확인하고 다음으로 넘어가자!" → 최단 경로 찾기에 유리

DFS (Stack/Recursion): "일단 끝까지 가보고 아니면 돌아오자!" → 모든 노드를 방문해야 하거나, 경로의 특징을 저장해야 할 때 유리

## 관련 글

- [[blog/BACKJOON/index|BACKJOON]]
- [[blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST)|[알고리즘] BFS, DFS와 최소 신장 트리(MST)]]
- [[blog/BACKJOON/백준(Python)- Input()|[백준(Python)] Input()]]
- [[blog/BACKJOON/백준(Python)- 파이썬 자료형 - List, Deque, Heap, Dictionary, Set|[백준(Python)] 파이썬 자료형 - List, Deque, Heap, Dictionary, Set]]
