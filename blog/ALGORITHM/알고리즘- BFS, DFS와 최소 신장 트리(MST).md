---
title: "[알고리즘] BFS, DFS와 최소 신장 트리(MST)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Algorithm", "BFS", "dfs", "mst"]
category: "ALGORITHM"
published: 2025-10-13
source_url: https://ch010104.tistory.com/157
---

# [알고리즘] BFS, DFS와 최소 신장 트리(MST)

## 원문

https://ch010104.tistory.com/157

## 노트 유형

`guide`

## 적용 목적과 전제조건

시작 정점 s에서 도달 가능한 모든 정점을 방문하는 탐색 기법.

시작점으로부터의 거리가 가까운 순서대로 정점을 탐색하며, 가중치 없는 그래프에서 최단 경로를 찾는 데 사용됨.

## 구현 절차·검증·주의점

### 너비 우선 탐색 (BFS, Breadth-First Search)

개요

시작 정점 s에서 도달 가능한 모든 정점을 방문하는 탐색 기법.

시작점으로부터의 거리가 가까운 순서대로 정점을 탐색하며, 가중치 없는 그래프에서 최단 경로를 찾는 데 사용됨.

주요 자료구조

큐 (Queue): 다음에 방문할 정점을 선입선출(FIFO) 방식으로 관리.

color[u]: 정점의 방문 상태 표시 (white: 미발견, gray: 발견되었으나 미처리, black: 처리 완료).

d[u]: 시작점 s로부터의 최단 거리 저장.

pred[u]: 최단 경로 트리에서 부모 정점을 가리킴.

알고리즘 코드

```text
BFS(G,s) {
    // 모든 정점 u에 대해 초기화 수행
    for each u in V {
        color[u] = white       // 방문 상태: 미발견(white)
        d[u] = infinity        // 거리: 무한대
        pred[u] = null         // 부모 노드: 없음
    }
    // 시작 정점 s 초기화
    color[s] = gray            // 방문 상태: 발견(gray)
    d[s] = 0                   // 시작점이므로 거리는 0

    Q = {s}                    // 큐에 시작 정점 s 추가
    while (Q is nonempty) {    // 큐가 비어있지 않은 동안 반복
        u = Q.Dequeue()        // 큐에서 정점 u를 꺼냄
        // u에 인접한 모든 정점 v를 확인
        for each v in Adj[u] {
            // v가 아직 발견되지 않았다면
            if (color[v] == white) {
                color[v] = gray    // 방문 상태: 발견(gray)
                d[v] = d[u] + 1    // 거리 설정 (u의 거리 + 1)
                pred[v] = u        // 부모 노드를 u로 설정
                Q.Enqueue(v)       // 큐에 v 추가
            }
        }
        color[u] = black           // u의 모든 인접 정점 확인 후 처리 완료(black)
    }
}
```

BFS 트리와 간선

pred 포인터는 시작점을 루트로 하는 너비 우선 탐색 트리(BFS 트리)를 형성.

그래프의 간선은 트리 간선(tree edge)과 교차 간선(cross edge)으로 분류됨.

시간 복잡도 분석

초기화에 Θ(V) 시간 소요.

각 정점은 큐에 한 번만 들어가고 나오므로, while 루프는 최대 V번 실행됨.

모든 정점의 인접 리스트를 한 번씩만 순회하므로, for 루프의 총 반복 횟수는 ∑u∈V​deg(u)=2E (무방향 그래프 기준).

총 실행 시간: Θ(V+E).

### 깊이 우선 탐색 (DFS, Depth-First Search)

개요

가능한 한 깊이 들어가는 경로를 우선적으로 탐색하는 기법.

막다른 길에 도달하면 되돌아와서 다른 경로를 시도하는 재귀적 방식.

주요 자료구조

color[u]: BFS와 동일하게 정점의 방문 상태 관리.

pred[u]: DFS 트리에서 부모 정점을 가리킴.

d[u] (발견 시각): 정점 u를 처음 발견(회색으로 변경)한 시각을 기록하는 타임스탬프.

f[u] (완료 시각): 정점 u의 모든 인접 정점 탐색이 끝난(검은색으로 변경) 시각을 기록하는 타임스탬프.

알고리즘 코드

```text
// 메인 DFS 프로그램
DFS(G) {
    // 모든 정점 u에 대해 초기화
    for each u in V {
        color[u] = white;
        pred[u] = null;
    }
    time = 0; // 타임스탬프 초기화

    // 모든 정점을 순회하며
    for each u in V {
        // 아직 발견되지 않은 정점 u에서 새로운 탐색 시작
        if (color[u] == white) {
            DFSVisit(u);
        }
    }
}

// u에서 재귀적으로 탐색 시작
DFSVisit(u) {
    color[u] = gray;           // u를 발견된 것으로 표시
    d[u] = ++time;             // 발견 시각 기록

    // u에 인접한 모든 정점 v에 대해
    for each v in Adj(u) {
        // v가 아직 발견되지 않았다면
        if (color[v] == white) {
            pred[v] = u;       // 부모 포인터 설정
            DFSVisit(v);       // 재귀적으로 방문
        }
    }
    color[u] = black;          // u에 대한 처리가 완료됨
    f[u] = ++time;             // 완료 시각 기록
}
```

DFS 트리와 간선 분류

pred 포인터는 깊이 우선 탐색 숲(forest)을 형성.

트리 간선 (Tree edges): DFS 숲을 구성하는 간선.

역 간선 (Back edges): 정점 u에서 조상 정점 v로 향하는 간선.(이 Back edges를 이용해서 사이클을 감지)

순방향 간선 (Forward edges): 정점 u에서 자손 정점 v로 향하는 비-트리 간선.

교차 간선 (Cross edges): 서로 다른 트리에 속하거나, 같은 트리 내에서 조상-자손 관계가 아닌 두 정점을 잇는 간선.

시간 복잡도 분석

DFSVisit()는 각 정점에 대해 정확히 한 번만 호출됨.

DFSVisit(u) 내의 루프는 outdeg(u)에 비례하는 시간이 걸림.

모든 정점에 대해 합산하면 ∑u∈V​outdeg(u)=E (방향 그래프 기준).

총 실행 시간: Θ(V+E).

### DFS의 속성 및 응용

괄호 보조정리 (Parenthesis Lemma)

DFS 탐색에서 두 정점 u, v의 발견/완료 시간 구간 $[d[u], f[u\]\]$와 $[d[v], f[v\]\]$는 다음 관계 중 하나만 가짐.

한 구간이 다른 구간을 완전히 포함 (조상-자손 관계).

두 구간이 서로 완전히 분리됨 (그 외 관계).

사이클 탐지

방향 그래프 G에서 DFS 수행 시 역 간선(back edge)이 발견되면 그래프에 사이클이 존재함.

역 간선이 없다면 그래프는 사이클이 없는 DAG(유향 비순환 그래프)임.

위상 정렬 (Topological Sort)

DAG의 정점들을 선형으로 나열하는 방법으로, 모든 간선 (u, v)에 대해 u가 v보다 앞에 오도록 정렬.

DFS를 수행한 후, 완료 시각(finish time)의 내림차순으로 정점을 정렬하면 위상 정렬 결과를 얻을 수 있음.

실행 시간은 DFS와 동일하게 Θ(V+E).

위상 정렬 알고리즘 코드

```text
TopSort(G) {
    // 모든 정점 u에 대해 초기화
    for each (u in V) {
        color[u] = white;
    }
    L = new linked_list; // 정렬 결과를 저장할 빈 연결 리스트

    // 발견되지 않은 정점에서 탐색 시작
    for each (u in V) {
        if (color[u] == white) {
            TopVisit(u);
        }
    }
    return L; // 최종 순서 제공
}

TopVisit(u) {
    color[u] = gray; // u 방문 표시

    // 인접한 정점 v에 대해
    for each (v in Adj(u)) {
        if (color[v] == white) {
            TopVisit(v);
        }
    }
    // u가 완료되면 리스트의 맨 앞에 추가
    Append u to the front of L;
}
```

### 최소 신장 트리 (MST, Minimum Spanning Tree)

개요

신장 트리 (Spanning Tree): 연결된 무방향 그래프의 모든 정점을 포함하면서 사이클이 없는 부분 그래프(트리).

최소 신장 트리 (MST): 간선들의 가중치 합이 최소가 되는 신장 트리.

일반적인 탐욕적 접근법

MST를 구성할 간선 집합 A를 유지하며, A에 추가해도 MST의 일부가 될 수 있는 **안전한 간선(safe edge)**을 반복적으로 추가.

MST 보조정리(MST Lemma): 정점 집합을 두 그룹 S와 V-S로 나누는 컷(cut)을 생각할 때, 이 컷을 가로지르는 가장 가중치가 작은 간선(경량 간선, light edge)은 항상 안전함.

크루스칼 알고리즘 (Kruskal's Algorithm)

모든 간선을 가중치의 오름차순으로 정렬.

정렬된 순서대로 간선을 하나씩 확인하며, 현재까지 선택된 간선 집합에 추가했을 때 사이클을 형성하지 않는 경우에만 해당 간선을 MST에 추가.

Union-Find 자료구조: 간선 추가 시 사이클 형성 여부를 효율적으로 확인하는 데 사용됨

Find-Set(u) != Find-Set(v)는 두 정점이 아직 같은 컴포넌트에 속하지 않음을 의미.

크루스칼 알고리즘 코드

```text
Kruskal(G=(V,E), w) {
    A = {}; // MST 간선 집합을 비움

    // 각 정점을 자신만의 집합(컴포넌트)으로 초기화
    for each (u in V) {
        Create_Set(u);
    }

    // 모든 간선을 가중치 오름차순으로 정렬
    Sort E in increasing order by weight w;

    // 정렬된 간선을 하나씩 순회
    for each ((u,v) from the sorted list) {
        // u와 v가 서로 다른 컴포넌트에 속해 있다면 (사이클을 형성하지 않는다면)
        if (Find_Set(u) != Find_Set(v)) {
            Add (u,v) to A;    // 간선을 A에 추가
            Union(u, v);       // 두 컴포넌트를 하나로 합침
        }
    }
    return A;
}
```

크루스칼 알고리즘 분석

간선 정렬 시간: Θ(ElogE).

for 루프는 E번 반복.

Union-Find 연산 시간: 각 연산은 O(logV).

총 실행 시간은 정렬 시간에 의해 지배되며, Θ(ElogE) 또는 $\Theta(E \log V)$로 표현 가능 (일반적으로 E가 V2보다 작으므로 logE는 O(logV)).

## 관련 글

- [[blog/ALGORITHM/index|ALGORITHM]]
- [[blog/BACKJOON/백준(Python)- BFS vs DFS|[백준(Python)] BFS vs DFS]]
- [[blog/ALGORITHM/알고리즘- 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘|[알고리즘] 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘]]
- [[blog/ALGORITHM/알고리즘- 그래프 알고리즘 소개|[알고리즘] 그래프 알고리즘 소개]]
