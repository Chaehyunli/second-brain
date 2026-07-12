---
title: "[네트워크] BGP와 인터넷 AS 라우팅"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-05-20
source_url: https://ch010104.tistory.com/275
---

# [네트워크] BGP와 인터넷 AS 라우팅

## 원문

https://ch010104.tistory.com/275

## 핵심 요약

- **1. BGP의 개요 및 핵심 역할** — 인터넷은 수만 개의 독립적인 네트워크 영역인 AS(Autonomous System, 자율 시스템)들의 거대한 결합체입니다.
- **🔑 BGP가 각 AS에 제공하는 이중 핵심 기능** — eBGP (external BGP): 인접한 다른 외부 AS로부터 서브넷 도달 가능성(Reachability) 정보를 획득합니다.
- **2. BGP의 기본 동작 및 세션 구성** — BGP는 신뢰성 있는 정보 교환을 위해 네트워크 계층 프로토콜임에도 불구하고 전송 계층의 TCP 위에서 동작합니다.
- **3. BGP 경로 속성과 정책 기반 라우팅** — BGP에서 단순히 하나의 경로를 수신하는 것은 '목적지 주소'만을 얻는 것을 의미하지 않습니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- BGP와 SDN|[네트워크] BGP와 SDN]]
- [[blog/NETWORK/네트워크- 링크 계층(CRC)과 다중 접속 프로토콜|[네트워크] 링크 계층(CRC)과 다중 접속 프로토콜]]
- [[blog/NETWORK/네트워크- MAC 주소와 ARP|[네트워크] MAC 주소와 ARP]]
