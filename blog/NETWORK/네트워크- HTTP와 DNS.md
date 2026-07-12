---
title: "[네트워크] HTTP와 DNS"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-03-31
source_url: https://ch010104.tistory.com/247
---

# [네트워크] HTTP와 DNS

## 원문

https://ch010104.tistory.com/247

## 핵심 요약

- **웹 캐시 (Proxy Server)의 목적** — 응답 시간 단축: 클라이언트와 물리적으로 가까운 곳에 데이터를 두어 객체 전송 속도를 높입니다.
- **조건부 GET (Conditional GET)** — 캐시에 저장된 데이터가 최신인지(Up-to-date) 확인하는 메커니즘입니다.
- **HTTP/1.1의 한계: HOL 블로킹** — FCFS(First-Come-First-Served) 스케줄링: 서버는 요청받은 순서대로 응답해야 합니다.
- **HTTP/2 (2015년 도입)** — 목적: 다중 객체 요청 시 지연 시간 최소화.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- 전송 계층(Transport Layer)과 TCP-UDP|[네트워크] 전송 계층(Transport Layer)과 TCP/UDP]]
- [[blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers|[네트워크] 쿠키 (Cookies)와 Proxy Servers]]
- [[blog/NETWORK/네트워크- UDP 프로토콜과 RDT|[네트워크] UDP 프로토콜과 RDT]]
