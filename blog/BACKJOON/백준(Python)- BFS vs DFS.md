---
title: "[백준(Python)] BFS vs DFS"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "BFS", "dfs", "Pthon"]
category: "BACKJOON"
published: 2026-03-12
source_url: https://ch010104.tistory.com/216
---

# [백준(Python)] BFS vs DFS

## 원문

https://ch010104.tistory.com/216

## 핵심 요약

- **1. BFS (너비 우선 탐색) - 큐(Queue) 활용** — BFS는 시작 노드에서 가까운 노드부터 차례대로 탐색합니다.
- **2. DFS (깊이 우선 탐색) - 재귀(Recursion) 활용** — DFS는 한 방향으로 갈 수 있을 때까지 깊게 가다가, 막히면 다시 돌아와서 다른 길을 찾습니다.
- **3. 전체 실행 예시 (그래프 구성)** — 아래와 같은 연결 상태를 가진 그래프가 있다고 가정해 보겠습니다.
- **💡 핵심 요약** — BFS (Queue): "내 주변부터 다 확인하고 다음으로 넘어가자!" → 최단 경로 찾기에 유리

## 관련 글

- [[blog/BACKJOON/index|BACKJOON]]
- [[blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST)|[알고리즘] BFS, DFS와 최소 신장 트리(MST)]]
- [[blog/BACKJOON/백준(Python)- Input()|[백준(Python)] Input()]]
- [[blog/BACKJOON/백준(Python)- 파이썬 자료형 - List, Deque, Heap, Dictionary, Set|[백준(Python)] 파이썬 자료형 - List, Deque, Heap, Dictionary, Set]]
