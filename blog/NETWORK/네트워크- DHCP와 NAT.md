---
title: "[네트워크] DHCP와 NAT"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-05-06
source_url: https://ch010104.tistory.com/271
---

# [네트워크] DHCP와 NAT

## 원문

https://ch010104.tistory.com/271

## 핵심 요약

- **1. DHCP (Dynamic Host Configuration Protocol)** — DHCP는 호스트가 네트워크에 접속할 때 자동으로 통신에 필요한 설정 정보를 할당받는 프로토콜입니다.
- **1.1 할당되는 주요 정보** — 서브넷 마스크 (Subnet Mask): 네트워크 부분과 호스트 부분을 구분.
- **1.2 동작 과정 (UDP/IP 기반)** — Discovery (클라이언트 → 서버): 클라이언트가 브로드캐스트(FF:FF:FF:FF:FF:FF)를 통해 서버를 찾음.
- **2. IP 주소 체계와 서브네팅 (Subnetting)** — IP 주소는 유한한 자원이며, 이를 효율적으로 나누어 쓰는 것이 중요합니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- 네트워크와 서브넷|[네트워크] 네트워크와 서브넷]]
- [[blog/NETWORK/네트워크- IPv4 vs IPv6|[네트워크] IPv4 vs IPv6]]
- [[blog/NETWORK/네트워크- 버퍼 관리, 스케줄링 및 정책|[네트워크] 버퍼 관리, 스케줄링 및 정책]]
