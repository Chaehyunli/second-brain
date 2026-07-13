---
title: "[네트워크] 링크 계층(CRC)과 다중 접속 프로토콜"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-06-01
source_url: https://ch010104.tistory.com/281
---

# [네트워크] 링크 계층(CRC)과 다중 접속 프로토콜

## 원문

https://ch010104.tistory.com/281

## 핵심 요약

- **1) 기본 용어 정리 (Terminology)** — 노드 (Nodes): 네트워크에 연결되어 전송을 수행하는 호스트(PC, 노트북, 스마트폰 등)와 라우터(Routers).
- **2) 네트워크 계층 vs 링크 계층 (교통수단 비유)** — 핵심 메시지: 3계층(네트워크)이 출발지부터 목적지까지의 전체 경로(End-to-End)를 책임진다면, 2계층(링크)은 물리적으로 바로 맞닿아 있는 인접 노드(Hop-by-Hop)로 데이터를 안전하게 건네주는 구체적인 수송 책임을 집니다.
- **1) 제공 서비스 (Link Layer Services)** — 프레이밍 및 링크 접근 (Framing, Link Access): 데이터그램에 헤더와 트레일러를 추가하여 프레임을 구성합니다.
- **2) 링크 계층의 구현 위치 (Implementation)** — 구현 하드웨어: 링크 계층은 소프트웨어 중심의 상위 계층과 달리 주로 네트워크 인터페이스 카드(NIC, 랜카드) 또는 메인보드 내 통신 칩셋에 구현됩니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- MAC 주소와 ARP|[네트워크] MAC 주소와 ARP]]
- [[blog/NETWORK/네트워크- BGP와 SDN|[네트워크] BGP와 SDN]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
