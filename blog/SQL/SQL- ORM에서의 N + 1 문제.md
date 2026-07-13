---
title: "[SQL] ORM에서의 N + 1 문제"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "SQL"]
category: "SQL"
published: 2026-06-25
source_url: https://ch010104.tistory.com/286
---

# [SQL] ORM에서의 N + 1 문제

## 원문

https://ch010104.tistory.com/286

## 핵심 요약

- **💻 2. 실무 기본 세팅: 엔티티 설계 (LAZY)** — 실무의 대원칙은 모든 연관 관계를 LAZY(지연 로딩)로 설정하는 것입니다.
- **🚨 3. N+1 문제의 발생 (Before)** — 모든 연관 관계를 LAZY로 잘 막았지만, 전체 게시글을 조회한 뒤 각 게시글의 댓글을 읽어오는 로직을 실행할 때 $N+1$ 문제가 터집니다.
- **❌ 실제 실행되는 SQL 로그 (N+1 발생)** — 게시글이 총 3개(ID: 10, 11, 12)가 있다고 가정하면, DB에 총 4번(1 + 3)의 요청이 날아갑니다.
- **🛠️ 4. 해결책 1: Fetch Join (페이징이 필요 없을 때)** — SQL의 JOIN을 사용하여 처음부터 게시글과 댓글을 한 방에 긁어옵니다.

## 관련 글

- [[blog/SQL/index|SQL]]
- [[blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX|[SQL] MySql의 인덱스 설정 - BTREE INDEX]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜젝션과 Serializability|[데이터베이스 설계] 트랜젝션과 Serializability]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
