---
title: "[네트워크] IPv4 vs IPv6"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-05-11
source_url: https://ch010104.tistory.com/273
---

# [네트워크] IPv4 vs IPv6

## 원문

https://ch010104.tistory.com/273

## 핵심 요약

- **1.1 등장 동기 및 헤더 구조** — 주소 고갈 해결: 32비트(2^32)의 IPv4 주소를 128비트(2^128)로 확장하여 무한에 가까운 주소 공간 확보.
- **1.2 IPv4-IPv6 과도기 기술: 터널링(Tunneling)** — IPv6 패킷이 IPv4 전용 구간을 통과하기 위해 사용하는 핵심 기술입니다.
- **2. 일반화된 전달과 OpenFlow 실전 사례** — 전통적인 라우팅(목적지 기반)을 넘어, 패킷의 모든 계층 정보를 이용한 제어가 가능해졌습니다.
- **2.1 "Match + Action"의 구체적 구현 사례** — OpenFlow 규칙을 통해 장비의 정체성을 소프트웨어로 결정합니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- 라우팅 알고리즘 - 다익스트라|[네트워크] 라우팅 알고리즘 - 다익스트라]]
- [[blog/NETWORK/네트워크- DHCP와 NAT|[네트워크] DHCP와 NAT]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
