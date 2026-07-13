---
title: "[네트워크] BGP와 SDN"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "CS", "Network"]
category: "NETWORK"
published: 2026-05-27
source_url: https://ch010104.tistory.com/278
---

# [네트워크] BGP와 SDN

## 원문

https://ch010104.tistory.com/278

## 핵심 요약

- **1) BGP의 정의 및 역할** — 인터넷의 GPS: 독립적인 네트워크 자치 시스템인 AS(Autonomous System)와 AS 사이에서 데이터를 목적지까지 보내기 위한 최적의 경로를 설정해 주는 대규모 외관문 라우팅 프로토콜(EGP)입니다.
- **2) BGP 최적 경로 선택 메커니즘 (Route Selection)** — BGP 라우터가 동일 목적지로 가는 다중 경로를 학습했을 때, 다음 우선순위에 따라 단 하나의 '최적 경로'를 도출해 냅니다.
- **1) 기존 Per-Router Control (분산형 제어 방식)** — Monolithic & Distributed: 각각의 개별 라우터 장비 내부에 Data Plane(하드웨어)과 Control Plane(경로 계산용 소프트웨어)이 일체형으로 통합되어 돌아가는 폐쇄적 수직 구조입니다.
- **2) 왜 SDN(소프트웨어 정의 네트워킹)인가? (중앙 집중화의 이점)** — 전통 방식(수직 계통): 전용 하드웨어, 전용 OS, 전용 앱이 묶여 팔리던 옛날의 IBM 메인프레임과 같습니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- BGP와 인터넷 AS 라우팅|[네트워크] BGP와 인터넷 AS 라우팅]]
- [[blog/NETWORK/네트워크- 링크 계층(CRC)과 다중 접속 프로토콜|[네트워크] 링크 계층(CRC)과 다중 접속 프로토콜]]
- [[blog/NETWORK/네트워크- MAC 주소와 ARP|[네트워크] MAC 주소와 ARP]]
