---
title: "[네트워크] TCP 연결과 3-Way Handshake"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-15
source_url: https://ch010104.tistory.com/262
---

# [네트워크] TCP 연결과 3-Way Handshake

## 원문

https://ch010104.tistory.com/262

## 핵심 요약

- **1.1 2-Way Handshake의 한계** — 개념: 클라이언트의 요청(req_conn)에 서버가 응답(acc_conn)하면 즉시 연결되는 방식.
- **1.2 3-Way Handshake (표준 방식)** — 목적: 양방향 신뢰성 확보 및 초기 순서 번호(Seq #) 동기화.
- **2.1 ACK 생성 규칙 (RFC 5681)** — 수신측은 네트워크 부하를 줄이기 위해 전략적으로 ACK를 보냅니다.
- **2.2 Seq #와 ACK #의 상호작용 (Telnet 예시)** — Seq #: 내가 보내는 데이터의 첫 번째 바이트 번호.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- rdt 3.0 과 TCP|[네트워크] rdt 3.0 과 TCP]]
- [[blog/NETWORK/네트워크- TCP 혼잡 제어 및 전송|[네트워크] TCP 혼잡 제어 및 전송]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
