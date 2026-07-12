---
title: "[네트워크] RDT (Reliable Data Transfer) 프로토콜"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-04-08
source_url: https://ch010104.tistory.com/257
---

# [네트워크] RDT (Reliable Data Transfer) 프로토콜

## 원문

https://ch010104.tistory.com/257

## 핵심 요약

- **1. rdt 2.1: 시퀀스 번호의 도입 (비트 오류 및 응답 오류 해결)** — image_cdfe45.png(송신자)와 image_ce549e.png(수신자)를 통해 확인할 수 있는 단계입니다.
- **핵심 문제 해결** — 문제: rdt 2.0에서는 ACK/NAK 자체가 깨질 경우 송신자가 재전송을 해야 하는데, 수신자는 이게 '새 데이터'인지 '중복 데이터'인지 구분할 수 없었습니다.
- **FSM 주요 로직** — 패킷을 보낼 때 0 또는 1 번호를 부여합니다.
- **3. rdt 3.0: 타이머의 도입 (패킷 유실 해결)** — image_ce76c6.png부터 image_d86f6a.png까지 설명하는 완성형 단계입니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- TCP 혼잡 제어 및 전송|[네트워크] TCP 혼잡 제어 및 전송]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
- [[blog/NETWORK/네트워크- 네트워크 애플리케이션의 원리 및 서비스|[네트워크] 네트워크 애플리케이션의 원리 및 서비스]]
