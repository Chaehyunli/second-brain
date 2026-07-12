---
title: "[네트워크] UDP 프로토콜과 RDT"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-06
source_url: https://ch010104.tistory.com/255
---

# [네트워크] UDP 프로토콜과 RDT

## 원문

https://ch010104.tistory.com/255

## 핵심 요약

- **1. UDP (User Datagram Protocol): 최소한의 전송 서비스** — UDP는 복잡한 제어 없이 데이터를 빠르게 던지는 "비연결형" 프로토콜입니다.
- **- 주요 특징** — 비연결성 (Connectionless): 송수신자 간 핸드셰이킹 없이 즉각 전송.
- **- 실제 활용 사례** — 스트리밍 & 게임: 실시간성이 중요하며 약간의 데이터 손실을 감수할 수 있는 서비스.
- **2. 에러 검출의 핵심: 인터넷 체크섬 (Checksum)** — 데이터가 전송 중 변형(Bit flip)되었는지 확인하는 수학적 장치입니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
- [[blog/NETWORK/네트워크- 전송 계층(Transport Layer)과 TCP-UDP|[네트워크] 전송 계층(Transport Layer)과 TCP/UDP]]
- [[blog/NETWORK/네트워크- rdt 3.0 과 TCP|[네트워크] rdt 3.0 과 TCP]]
