---
title: "[알고리즘] Shortest Path 알고리즘(Bellman-Ford & DIJKSTRA 알고리즘)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Algorithm"]
category: "ALGORITHM"
published: 2025-10-20
source_url: https://ch010104.tistory.com/166
---

# [알고리즘] Shortest Path 알고리즘(Bellman-Ford & DIJKSTRA 알고리즘)

## 원문

https://ch010104.tistory.com/166

## 핵심 요약

- **1. 최단 경로 문제 (Shortest Paths)** — 문제: 가중치가 있는 유향 그래프 $G=(V,E)$에서 1, 한 정점 $u$에서 다른 정점 $v$로 가는 가장 가중치가 낮은 (가장 빠른) 경로를 찾는 문제
- **2. 최단 경로의 속성** — 최적 부분 구조 (Optimal Substructure)
- **3. Relaxation (완화)** — Relaxation은 $v$로 가는 현재까지의 최단 경로 추정치($v.d$)를 $u$를 거쳐 가는 더 짧은 경로가 있는지 확인하고, 있다면 갱신하는 핵심 연산
- **4. 벨만-포드 (Bellman-Ford) 알고리즘** — - 음수 가중치 간선이 있어도 작동하며 58, 음수 가중치 사이클을 탐지할 수 있음

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘|[알고리즘] 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘]]
- [[blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST)|[알고리즘] BFS, DFS와 최소 신장 트리(MST)]]
- [[blog/ALGORITHM/알고리즘- A- (A-Star) 알고리즘과 Greedy (탐욕) 알고리즘|[알고리즘] A* (A-Star) 알고리즘과 Greedy (탐욕) 알고리즘]]
