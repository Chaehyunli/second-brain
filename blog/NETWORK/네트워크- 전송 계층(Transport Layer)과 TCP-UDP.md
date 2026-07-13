---
title: "[네트워크] 전송 계층(Transport Layer)과 TCP/UDP"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-01
source_url: https://ch010104.tistory.com/251
---

# [네트워크] 전송 계층(Transport Layer)과 TCP/UDP

## 원문

https://ch010104.tistory.com/251

## 핵심 요약

- **전송 계층의 역할과 목표** — 프로세스 간 통신: 전송 계층은 서로 다른 호스트에서 실행되는 애플리케이션 프로세스 간의 논리적 통신(Logical Communication)을 제공합니다.
- **전송 계층 vs 네트워크 계층** — 네트워크 계층: 호스트 간(Host-to-Host)의 논리적 통신을 담당합니다.
- **전송 계층의 동작** — 송신자(Sender): 애플리케이션 메시지를 수신하여 이를 세그먼트(Segment) 단위로 쪼개고, 전송 계층 헤더를 붙여 네트워크 계층(IP)으로 전달합니다.
- **주요 인터넷 전송 프로토콜** — TCP (Transmission Control Protocol): 신뢰적이고 순차적인 전달, 혼잡 제어, 흐름 제어, 연결 설정(Handshake)을 제공합니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- HTTP와 DNS|[네트워크] HTTP와 DNS]]
- [[blog/NETWORK/네트워크- UDP 프로토콜과 RDT|[네트워크] UDP 프로토콜과 RDT]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
