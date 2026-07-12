---
title: "[네트워크] rdt 3.0 과 TCP"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CSS", "Network"]
category: "NETWORK"
published: 2026-04-13
source_url: https://ch010104.tistory.com/260
---

# [네트워크] rdt 3.0 과 TCP

## 원문

https://ch010104.tistory.com/260

## 핵심 요약

- **1. rdt 3.0 (Stop-and-Wait)의 성능과 한계** — 신뢰성 있는 데이터 전송을 보장하는 rdt 3.0은 전송 후 대기(Stop-and-Wait) 방식을 사용합니다.
- **주요 개념** — 이용률 (U_{sender}): 송신자가 전체 시간 중 실제로 데이터를 전송하는 시간의 비율.
- **계산 예시 (1 Gbps 링크, 15ms 편도 지연, 8000비트 패킷)** — 전송 지연 계산: D_trans = {8,000}{10^9} = 8\mu s = 0.008ms
- **2. 파이프라이닝 (Pipelining): 효율성 극대화** — Stop-and-Wait의 낮은 이용률을 해결하기 위해 등장한 개념입니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- TCP 연결과 3-Way Handshake|[네트워크] TCP 연결과 3-Way Handshake]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
- [[blog/NETWORK/네트워크- TCP 혼잡 제어 및 전송|[네트워크] TCP 혼잡 제어 및 전송]]
