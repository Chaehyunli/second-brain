---
title: "[네트워크] TCP 혼잡 제어 및 전송"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-04-20
source_url: https://ch010104.tistory.com/264
---

# [네트워크] TCP 혼잡 제어 및 전송

## 원문

https://ch010104.tistory.com/264

## 핵심 요약

- **핵심 변수 정의** — MSS (Maximum Segment Size): TCP 패킷 하나가 실어 나를 수 있는 순수 데이터의 최대 크기.
- **전송 속도 공식** — TCP는 매 왕복 시간(RTT)마다 cwnd만큼의 데이터를 네트워크 파이프에 채우려 노력합니다.
- **① Slow Start (슬로우 스타트)** — 동작: cwnd = 1 MSS에서 시작하여 매 RTT마다 cwnd를 2배씩 증가시킵니다 (지수적 증가).
- **② Congestion Avoidance (혼잡 회피 - AIMD)** — 조건: cwnd >= ssthresh 일 때 진입.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
- [[blog/NETWORK/네트워크- BGP와 SDN|[네트워크] BGP와 SDN]]
