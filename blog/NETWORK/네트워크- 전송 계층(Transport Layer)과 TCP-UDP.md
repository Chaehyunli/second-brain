---
title: "[네트워크] 전송 계층(Transport Layer)과 TCP/UDP"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-01
source_url: https://ch010104.tistory.com/251
---

# [네트워크] 전송 계층(Transport Layer)과 TCP/UDP

## 원문

https://ch010104.tistory.com/251

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

프로세스 간 통신: 전송 계층은 서로 다른 호스트에서 실행되는 애플리케이션 프로세스 간의 논리적 통신(Logical Communication)을 제공합니다.

학습 목표: 다중화(Multiplexing)와 역다중화(Demultiplexing)의 원리 이해.

## 원문 기반 학습 정리

### 1. 전송 계층(Transport Layer) 개요

### 전송 계층의 역할과 목표

프로세스 간 통신: 전송 계층은 서로 다른 호스트에서 실행되는 애플리케이션 프로세스 간의 논리적 통신(Logical Communication)을 제공합니다.

학습 목표: 다중화(Multiplexing)와 역다중화(Demultiplexing)의 원리 이해.

신뢰적인 데이터 전송(Reliable Data Transfer)의 원리.

흐름 제어(Flow Control)와 혼잡 제어(Congestion Control).

인터넷 프로토콜인 UDP(비연결형)와 TCP(연결 지향형) 학습.

### 전송 계층 vs 네트워크 계층

네트워크 계층: 호스트 간(Host-to-Host)의 논리적 통신을 담당합니다. (예: 우편 배달 서비스 자체가 도시 간 편지를 옮기는 것)

전송 계층: 프로세스 간(Process-to-Process)의 논리적 통신을 담당합니다. 네트워크 계층의 서비스를 이용하며 이를 강화(Reliability 추가 등)합니다.

가족 비유(Household Analogy):

집(Host): 앤(Ann)의 집과 빌(Bill)의 집.

아이들(Process): 각 집에 사는 12명의 아이들.

편지(App Message): 봉투에 든 편지.

앤과 빌(Transport Protocol): 아이들의 편지를 모아서 우체부에게 주거나, 받은 편지를 각 아이들에게 나누어 주는 역할.

우편 서비스(Network Layer): 집과 집 사이를 이동하는 서비스.

### 전송 계층의 동작

송신자(Sender): 애플리케이션 메시지를 수신하여 이를 세그먼트(Segment) 단위로 쪼개고, 전송 계층 헤더를 붙여 네트워크 계층(IP)으로 전달합니다.

수신자(Receiver): IP로부터 세그먼트를 받아 헤더를 확인하고, 메시지를 재조립하여 소켓(Socket)을 통해 해당 애플리케이션으로 전달합니다.

### 주요 인터넷 전송 프로토콜

TCP (Transmission Control Protocol): 신뢰적이고 순차적인 전달, 혼잡 제어, 흐름 제어, 연결 설정(Handshake)을 제공합니다.

UDP (User Datagram Protocol): 비신뢰적이고 순서가 보장되지 않는 전달. IP의 기능을 최소한으로 확장한 형태입니다.

제공하지 않는 서비스: 지연 시간 보장(Delay guarantees), 대역폭 보장(Bandwidth guarantees)은 두 프로토콜 모두 제공하지 않습니다.

### 2. 다중화 및 역다중화

### 기본 개념

다중화(Multiplexing, 송신측): 여러 소켓에서 나오는 데이터를 모아, 각 데이터에 헤더 정보를 추가하여 하위 계층으로 보내는 과정입니다.

역다중화(Demultiplexing, 수신측): 전송 계층 헤더 정보를 확인하여 받은 세그먼트를 올바른 소켓으로 전달하는 과정입니다.

소켓(Socket): 애플리케이션 프로세스와 전송 계층 사이의 문(Door) 역할을 하며, 각 소켓은 고유한 식별자를 가집니다.

### 역다중화의 작동 방식

호스트가 IP 데이터그램을 받으면, 그 안에는 소스 포트 번호(Source Port)와 목적지 포트 번호(Destination Port)가 포함된 전송 계층 세그먼트가 들어 있습니다.

호스트는 IP 주소와 포트 번호를 조합하여 데이터를 전달할 소켓을 찾습니다.

### 비연결형 역다중화 (UDP)

UDP 소켓은 (목적지 IP 주소, 목적지 포트 번호)로만 식별됩니다.

따라서 소스(출발지) IP나 포트 번호가 다르더라도, 목적지 IP와 포트 번호가 같다면 동일한 UDP 소켓으로 전달됩니다.

서버 응답 시 "누구에게 보낼지" 알기 위해 세그먼트 헤더에 소스 포트 번호를 포함합니다.

### 연결 지향형 역다중화 (TCP

TCP 소켓은 4-튜플(4-tuple)에 의해 식별됩니다:

Source IP address

Source port number

Destination IP address

Destination port number

핵심 차이점: 목적지 IP와 포트 번호가 같더라도, 출발지 IP나 포트 번호 중 하나라도 다르면 서로 다른 TCP 소켓으로 안내됩니다.

웹 서버(예: Apache)는 각 연결된 클라이언트마다 별도의 소켓을 생성하여 관리합니다.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- HTTP와 DNS|[네트워크] HTTP와 DNS]]
- [[blog/NETWORK/네트워크- UDP 프로토콜과 RDT|[네트워크] UDP 프로토콜과 RDT]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
