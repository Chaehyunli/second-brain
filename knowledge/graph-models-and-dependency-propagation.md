---
schema_version: 1
id: knowledge-graph-models-and-dependency-propagation
title: 그래프와 의존성 전파 모델
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST).md
  - blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient).md
---

# 그래프와 의존성 전파 모델

## 공통 표현
그래프는 노드·간선으로 연결과 의존성을 표현한다. 그러나 어떤 상태를, 어느 방향으로, 왜 전파하는지는 문제마다 다르다.

## 탐색 그래프
BFS/DFS는 방문 여부·거리·부모 같은 탐색 상태를 갱신해 연결된 정점이나 경로를 찾는다.

## 계산 그래프
자동미분은 연산과 입력의 의존성을 따라 gradient를 역방향으로 전파한다. 목적은 경로 탐색이 아니라 학습을 위한 미분값 계산이다.

## 비교로 얻는 선택 기준
둘은 연결 구조와 상태 전파라는 표현을 공유하지만 알고리즘·방향·종료 조건이 다르다. 탐색 문제에는 그래프 traversal을, 미분 계산에는 chain rule 기반 계산 그래프를 선택한다.

## 비유의 한계와 근거
“그래프”라는 말만으로 구현 세부나 성능 특성을 동일시하지 않는다.
- [[blog/ALGORITHM/알고리즘- BFS, DFS와 최소 신장 트리(MST)]]
- [[blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient)]]
