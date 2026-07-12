---
title: "[알고리즘] 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "ALGORITHM"
published: 2025-10-16
source_url: https://ch010104.tistory.com/161
archive_method: Tistory sitemap + HTML content extraction
---

# [알고리즘] 최소 신장 트리 (MST) - 크루스칼 (Kruskal) & 프림 (Prim) 알고리즘

> 원문: https://ch010104.tistory.com/161

## 본문

최소 신장 트리 (MST) 정의 및 핵심 개념  정의: 주어진 연결된, 무방향 가중치 그래프에서 모든 정점을 연결하는 간선들의 가중치 합이 최소가 되는 트리를 찾는 문제.  목표: 모든 정점을 연결하면서 사이클이 없는 부분집합 T⊆E 를 찾아, 총 가중치 w(T)=∑(u,v)∈T​w(u,v) 를 최소화하는 것.  Generic-MST 알고리즘:  초기화: 간선 집합 A를 공집합으로 시작.  반복: A가 신장 트리를 형성할 때까지 다음을 반복.  Safe Edge 추가: A에 대해 안전한(safe) 간선 $(u,v)$를 찾아 A에 추가.    Safe Edge: MST의 일부가 될 수 있는 간선으로, 그래프를 두 개의 집합 S와 V-S로 나누는 '컷(cut)'을 가로지르는 간선 중 가장 가중치가 낮은 '경량 간선(light edge)'은 안전한 간선임.    크루스칼 (Kruskal) 알고리즘    핵심 아이디어: 사이클을 형성하지 않는 선에서, 가중치가 가장 낮은 간선을 순서대로 선택하여 트리를 구성.  알고리즘 순서:  A를 공집합으로 초기화.  그래프의 모든 정점 v에 대해 MAKE-SET(v) 연산을 수행하여 각 정점이 자신만의 집합에 속하도록 함.  그래프의 모든 간선을 가중치에 따라 비내림차순(오름차순)으로 정렬.  정렬된 간선 리스트에서 간선 (u, v)를 순서대로 하나씩 확인.  만약 FIND-SET(u)가 FIND-SET(v)와 다르면 (즉, 두 정점이 서로 다른 집합에 속해 사이클을 만들지 않으면),   간선 (u, v)를 A에 추가.  UNION(u, v) 연산을 수행하여 두 정점이 속한 집합을 합침.    최종적으로 A를 반환.    사이클 탐지 (Disjoint Set Union):  Find-Set: 특정 원소가 속한 집합의 대표 원(예: 트리의 루트)을 찾음. 두 정점의 대표 원이 같으면 사이클이 형성된다고 판단.  Union: 두 집합을 하나의 집합으로 합침.  경로 압축 (Path Compression): Find-Set 연산 시 트리의 높이를 줄여 시간 복잡도를 개선하는 기법.    시간 복잡도  간선 정렬에 O(ElogE).  Find-Set 및 Union 연산에 약 O(E).  따라서 전체 시간 복잡도는 $O(E \log E)$이며, 이는 $O(E \log V)$와 같음.        프림 (Prim) 알고리즘    핵심 아이디어: 임의의 시작 정점에서부터 트리를 점진적으로 확장해 나가는 방식. 현재 트리에 속한 정점 집합과 속하지 않은 정점 집합을 연결하는 간선 중 가중치가 가장 낮은 것을 선택.  알고리즘 순서:  모든 정점 u에 대해 u.key를 무한대(∞)로, 부모 u.π를 NIL로 초기화. u.key는 해당 정점을 트리에 연결하는 데 필요한 최소 비용.  시작 정점 r의 r.key를 0으로 설정.  모든 정점을 최소 우선순위 큐 Q에 삽입. Q는 key 값이 가장 작은 정점을 우선적으로 추출.   Q가 비어있지 않은 동안 다음을 반복.   Q에서 key 값이 가장 작은 정점 u를 추출 (EXTRACT-MIN(Q)).  u에 인접한 각 정점 v에 대해 다음을 수행.  만약 v가 아직 Q에 있고, 간선 w(u,v)의 가중치가 v.key보다 작다면,   v.π를 u로 갱신.  v.key를 w(u,v) 값으로 갱신.  우선순위 큐 Q에서 v의 key 값을 갱신 (DECREASE-KEY).        시간 복잡도:  이진 힙을 우선순위 큐로 사용할 경우, 초기화에 O(V), EXTRACT-MIN 연산에 총 O(VlogV), DECREASE-KEY 연산에 총 $O(E \log V)$가 소요되어 전체 시간 복잡도는 $O(E \log V)$임.  피보나치 힙을 사용할 경우, $O(E + V \log V)$로 개선 가능
