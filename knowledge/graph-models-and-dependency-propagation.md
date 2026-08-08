---
schema_version: 1
id: knowledge-graph-models-and-dependency-propagation
title: 그래프와 의존성 전파 모델
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST).md
  - blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient).md
---

# 그래프와 의존성 전파 모델

## 핵심
그래프는 노드·간선으로 연결과 의존성을 명시하고, 탐색에서는 방문·거리·부모 상태를, 계산 그래프에서는 연산 의존성 위의 gradient를 전파한다.

## 연결된 근거
- [[blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST).md]]
- [[blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient).md]]

## 적용 기준
BFS/DFS의 topology traversal과 자동미분의 computation graph를 공통 표현 관점에서 연결한다.

## 주의점 또는 한계
두 영역은 목적과 알고리즘이 다르므로 그래프라는 표현의 공통성 이상으로 구현 세부를 동일시하지 않는다.
