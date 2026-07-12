---
title: "[알고리즘] 이진 탐색 트리(Binary Search Tree)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "이진 검색 트리", "자료구조", "트리 순회"]
category: "ALGORITHM"
published: 2025-09-25
source_url: https://ch010104.tistory.com/145
---

# [알고리즘] 이진 탐색 트리(Binary Search Tree)

## 원문

https://ch010104.tistory.com/145

## 핵심 요약

- **1. 이진 탐색 트리(BST)란 무엇일까요?** — 이진 탐색 트리(BST)는 이름에서 알 수 있듯이 '검색'에 특화된 '이진 트리'
- **2. 핵심 연산: 검색, 삽입, 삭제** — - 특정 값을 찾을 때, 루트 노드부터 시작하여 찾는 값과 현재 노드의 값을 비교
- **3. 트리 순회(Traversal) 방법** — - 트리의 모든 노드를 한 번씩 방문하는 것을 '순회'라고 함
- **4. 깊이 우선 탐색(DFS) vs. 너비 우선 탐색(BFS)** — 깊이 우선 탐색 (Depth-First Search, DFS)

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/ALGORITHM/알고리즘- 백트래킹을 이용한 순열-조합 및 알고리즘 성능 분석(Big-O, Omega, Theta)|[알고리즘] 백트래킹을 이용한 순열/조합 및 알고리즘 성능 분석(Big-O, Omega, Theta)]]
- [[blog/ALGORITHM/알고리즘- 그래프 알고리즘 소개|[알고리즘] 그래프 알고리즘 소개]]
- [[blog/ALGORITHM/알고리즘- 재귀란- (일반 재귀 vs 꼬리 재귀)|[알고리즘] 재귀란? (일반 재귀 vs 꼬리 재귀)]]
