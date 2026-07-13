---
title: "[알고리즘] A* (A-Star) 알고리즘과 Greedy (탐욕) 알고리즘"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Algorithm"]
category: "ALGORITHM"
published: 2025-11-03
source_url: https://ch010104.tistory.com/176
---

# [알고리즘] A* (A-Star) 알고리즘과 Greedy (탐욕) 알고리즘

## 원문

https://ch010104.tistory.com/176

## 핵심 요약

- **A* (A-Star) 알고리즘 (vs. 다익스트라)** — A* 알고리즘은 다익스트라(Dijkstra) 알고리즘을 기반으로 하지만, **휴리스틱(heuristic, 추정치)**을 사용하여 훨씬 효율적으로 최단 경로를 탐색하는 알고리즘
- **💡 Greedy (탐욕) 알고리즘** — - 탐욕 알고리즘은 매 순간(local) 가장 좋아 보이는 선택을 반복함으로써, 전체적으로도 최적의 해(global optimum)를 찾으려는 접근 방식

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- DynamicProgramming과 AllPairShortestPathAlgorithm|[알고리즘] DynamicProgramming과 AllPairShortestPathAlgorithm]]
- [[blog/ALGORITHM/알고리즘- Shortest Path 알고리즘(Bellman-Ford & DIJKSTRA 알고리즘)|[알고리즘] Shortest Path 알고리즘(Bellman-Ford & DIJKSTRA 알고리즘)]]
- [[blog/ALGORITHM/알고리즘- 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘|[알고리즘] 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘]]
