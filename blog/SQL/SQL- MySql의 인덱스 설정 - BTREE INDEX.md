---
title: "[SQL] MySql의 인덱스 설정 - BTREE INDEX"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Database", "springboot"]
category: "SQL"
published: 2025-04-03
source_url: https://ch010104.tistory.com/41
---

# [SQL] MySql의 인덱스 설정 - BTREE INDEX

## 원문

https://ch010104.tistory.com/41

## 핵심 요약

- **1. 인덱스란?** — 인덱스(Index)는 데이터베이스에서 원하는 데이터를 빠르게 찾기 위해 사용하는 자료구조
- **2. B-Tree 인덱스와 조회 방식 비교** — 📌 인덱스가 없는 경우 (Full Table Scan)
- **3. 인덱스를 사용할 수 없는 경우: LIKE '%abc%'** — %가 앞에 있으면 MySQL이 B-Tree 인덱스를 사용할 수 없음
- **4. MySQL에서 인덱스 설정 & 사용 확인 방법** — key에 인덱스 이름이 보이면 실제 사용 중!!!

## 관련 글

- [[blog/SQL/index|SQL]]
- [[blog/SQL/SQL- ORM에서의 N + 1 문제|[SQL] ORM에서의 N + 1 문제]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장|[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장]]
- [[blog/DOCKER/Docker- Docker를 사용해서 Spring boot + React 배포하기 ( 1 )|[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )]]
