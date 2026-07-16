---
title: "[네트워크] 네트워크 계층(Network Layer) 의 구조"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "카테고리 없음"
published: 2026-04-27
source_url: https://ch010104.tistory.com/266
---

# [네트워크] 네트워크 계층(Network Layer) 의 구조

## 원문

https://ch010104.tistory.com/266

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

제어 평면 (Control Plane - 지도를 그리는 뇌): 라우팅 알고리즘(OSPF, BGP 등)을 실행하여 패킷이 목적지까지 가는 최적의 경로를 계산합니다. (밀리초 단위의 소프트웨어 처리)

데이터 평면 (Data Plane - 실제 운전하는 손발): 제어 평면이 만든 지도를 보고, 입력 포트로 들어온 패킷을 출력 포트로 빠르게 전달하는 포워딩을 수행합니다. (나노초 단위의 하드웨어 처리)

## 원문 기반 개념 정리

### 1. 네트워크 계층의 구조: 제어 평면 vs 데이터 평면

네트워크 계층은 두 가지 핵심 기능으로 나뉩니다.

제어 평면 (Control Plane - 지도를 그리는 뇌): 라우팅 알고리즘(OSPF, BGP 등)을 실행하여 패킷이 목적지까지 가는 최적의 경로를 계산합니다. (밀리초 단위의 소프트웨어 처리)

데이터 평면 (Data Plane - 실제 운전하는 손발): 제어 평면이 만든 지도를 보고, 입력 포트로 들어온 패킷을 출력 포트로 빠르게 전달하는 포워딩을 수행합니다. (나노초 단위의 하드웨어 처리)

### 2. 서비스 모델 및 QoS (Quality of Service)

네트워크 아키텍처별로 품질을 보장하는 방식이 다릅니다.

### 상세 설명:

CBR (Constant Bit Rate): 일정한 전송률을 유지하며 실시간 방송 등에 적합.

VBR (Variable Bit Rate): 데이터 양이 변해도 평균 속도와 타이밍을 보장.

ABR (Available Bit Rate): 남는 자원을 쓰되, 최소 대역폭은 보장.

UBR (Unspecified Bit Rate): 보장 없이 남는 공간만 사용.

### 3. Best-Effort 모델의 성공 배경 (Reflections)

왜 아무것도 보장하지 않는 "최선형" 모델이 복잡한 ATM을 이기고 승리했을까요?

메커니즘의 단순함: 라우터가 복잡한 상태를 관리할 필요가 없어 전 세계적인 배포가 쉬웠습니다.

충분한 대역폭 증설 (Over-provisioning): 정교한 제어 기술을 만드는 대신, 광케이블을 더 깔아 파이프 자체를 굵게 만들어 혼잡을 해결했습니다.

분산 서비스 (CDN/Cloud): 데이터를 사용자 근처 서버에 두어 네트워크 지연 문제를 물리적 거리 단축으로 극복했습니다.

탄력적 서비스 (Elastic Services): TCP와 같은 프로토콜이 혼잡 시 스스로 속도를 조절하여 전체 망의 붕괴를 막았습니다.

### 4. 입력 포트 및 포워딩 기술

### ① 분산 스위칭 (Decentralized Switching)

중앙 CPU의 개입 없이 각 포트가 독립적으로 포워딩을 결정합니다. "Match plus Action" 원칙에 따라 헤더 정보를 보고 행동을 결정합니다.

Destination-based: 오직 목적지 IP 주소만 보고 전달 (전통적).

Generalized: IP, 포트 번호 등 다양한 헤더 필드 조합을 보고 전달 (SDN/현대적).

### ② 최장 일치 접두어 매칭 (Longest Prefix Matching)

목적지 IP 주소와 가장 길게 일치하는 테이블 항목을 선택합니다.

예시: 11001000 00010111 00011000... 이라는 주소가 들어왔을 때, 21비트 일치 항목보다 더 구체적인 24비트 일치 항목을 선택하여 정확한 경로를 찾습니다.

TCAM (Ternary Content Addressable Memory): 0, 1 외에 'X(Don't Care)'를 지원하는 특수 메모리로, 테이블 크기와 상관없이 단 한 번의 동작으로 매칭 결과를 찾아냅니다.

### 5. 스위칭 패브릭 (Switching Fabrics)

라우터 내부에서 패킷이 이동하는 고속도로의 종류입니다.

메모리 (Memory): CPU가 직접 시스템 메모리에 썼다가 읽음. 2번의 버스 통과(Crossing)가 발생하여 매우 느림.

버스 (Bus): 공용 도로 하나를 공유. 버스 경합(Contention) 때문에 한 번에 하나만 이동 가능.

인터커넥션 네트워크 (Crossbar): 격자형 회로로 여러 경로를 동시에 연결.

Scaling: 100Tbps급 성능을 위해 여러 개의 Fabric Plane을 병렬로 연결하고, 패킷을 고정 크기의 **셀(Cell)**로 쪼개서 병렬 처리합니다.

### 6. 큐잉 및 성능 병목 (Queuing & Loss)

### ① 입력 포트: HOL Blocking

현상: 큐 맨 앞의 패킷이 막히면, 자기가 갈 길은 뚫려 있는데도 뒤에 있는 패킷들이 나가지 못하고 갇히는 현상입니다.

### ② 출력 포트: 버퍼 오버플로우

Buffering: 패브릭에서 쏟아지는 데이터가 링크 전송 속도($R$)보다 빠를 때 발생합니다.

삭제 정책 (Drop Policy): 버퍼가 꽉 차면 패킷을 버립니다(Tail drop 등).

스케줄링 (Scheduling): 우선순위를 따져 누구를 먼저 보낼지 결정합니다. 이것이 QoS와 망 중립성 논쟁의 핵심 지점입니다.

## 관련 글

- [[blog/카테고리 없음/index|카테고리 없음]]
- [[blog/NETWORK/네트워크- TCP 혼잡 제어 및 전송|[네트워크] TCP 혼잡 제어 및 전송]]
- [[blog/NETWORK/네트워크- 버퍼 관리, 스케줄링 및 정책|[네트워크] 버퍼 관리, 스케줄링 및 정책]]
- [[blog/NETWORK/네트워크- TCP 연결과 3-Way Handshake|[네트워크] TCP 연결과 3-Way Handshake]]
