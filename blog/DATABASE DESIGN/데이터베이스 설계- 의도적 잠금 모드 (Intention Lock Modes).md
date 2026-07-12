---
title: "[데이터베이스 설계] 의도적 잠금 모드 (Intention Lock Modes)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing"]
category: "DATABASE DESIGN"
published: 2025-11-19
source_url: https://ch010104.tistory.com/191
---

# [데이터베이스 설계] 의도적 잠금 모드 (Intention Lock Modes)

## 원문

https://ch010104.tistory.com/191

## 핵심 요약

- **1. 의도적 잠금 모드 (Intention Lock Modes)** — 다중 입도(Multiple Granularity)에서의 잠금 모드
- **2. 잠금 호환성 행렬 (Compatibility Matrix)** — S 잠금은 일관된 뷰를 보장해야 하는데, IX는 하위 노드 수정을 암시하므로 충돌 발생
- **3. 다중 입도 잠금 예시** — 트랜잭션 T_21, T_22, T_23, T_24의 잠금 수행 예시
- **4. 다중 입도 잠금 규약 (Rules)** — 노드 Q에 S 또는 IS 잠금을 하려면, 부모 노드는 IX 또는 IS 상태여야 함

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 회복 시스템(Recovery System)|[데이터베이스 설계] 회복 시스템(Recovery System)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜잭션 복구 및 데이터 접근|[데이터베이스 설계] 트랜잭션 복구 및 데이터 접근]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 동시성 제어|[데이터베이스 설계] 동시성 제어]]
