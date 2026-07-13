---
title: "[네트워크] MAC 주소와 ARP"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-06-03
source_url: https://ch010104.tistory.com/283
---

# [네트워크] MAC 주소와 ARP

## 원문

https://ch010104.tistory.com/283

## 핵심 요약

- **1. 두 가지 네트워크 주소 체계 비교 (IP vs MAC)** — 네트워크 기기들은 통신을 위해 두 가지 대표적인 주소(논리 주소와 물리 주소)를 가집니다.
- **2. 프로토콜 계층과 데이터 포장 (캡슐화/역캡슐화)** — 데이터가 전송될 때는 프로토콜 스택 상단에서 하단으로 내려오며 포장지(헤더)가 붙고, 수신할 때는 반대로 올라가며 해체됩니다.
- **3. ARP (Address Resolution Protocol)의 역할과 동작** — ARP는 "상대방의 IP 주소는 알지만, MAC 주소를 모를 때" 이를 해결해 주는 통역사 역할을 수행합니다.
- **3.1 ARP 테이블 (ARP Table)** — 각 기기(호스트, 라우터)는 매번 주소를 물어보는 비효율을 줄이기 위해 < IP 주소 ; MAC 주소 ; TTL > 정보를 메모리에 표 형태로 저장해 둡니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- 링크 계층(CRC)과 다중 접속 프로토콜|[네트워크] 링크 계층(CRC)과 다중 접속 프로토콜]]
- [[blog/NETWORK/네트워크- BGP와 SDN|[네트워크] BGP와 SDN]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
