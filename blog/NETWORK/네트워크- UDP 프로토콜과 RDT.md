---
title: "[네트워크] UDP 프로토콜과 RDT"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-06
source_url: https://ch010104.tistory.com/255
---

# [네트워크] UDP 프로토콜과 RDT

## 원문

https://ch010104.tistory.com/255

## 노트 유형

`guide`

## 적용 목적과 전제조건

UDP는 복잡한 제어 없이 데이터를 빠르게 던지는 "비연결형" 프로토콜입니다.

비연결성 (Connectionless): 송수신자 간 핸드셰이킹 없이 즉각 전송.

## 구현 절차·검증·주의점

### 1. UDP (User Datagram Protocol): 최소한의 전송 서비스

UDP는 복잡한 제어 없이 데이터를 빠르게 던지는 "비연결형" 프로토콜입니다.

### - 주요 특징

비연결성 (Connectionless): 송수신자 간 핸드셰이킹 없이 즉각 전송.

최선 노력 원칙 (Best-effort): 전송은 시도하나 손실, 순서 바뀜을 책임지지 않음.

오버헤드 최소화: 헤더가 단 8바이트로 매우 가벼움.

비정체 제어: 네트워크 상황에 상관없이 애플리케이션이 원하는 속도로 전송 가능.

### - 실제 활용 사례

스트리밍 & 게임: 실시간성이 중요하며 약간의 데이터 손실을 감수할 수 있는 서비스.

DNS (Domain Name System): 짧은 요청/응답 구조에 적합하며 빠른 응답이 생명.

SNMP (Network Management): 네트워크 장애 상황에서도 장비 상태를 모니터링하기 위해 가벼운 UDP 사용.

HTTP/3: 속도를 위해 UDP(QUIC)를 쓰되, 필요한 신뢰성은 앱 계층에서 직접 구현.

### 2. 에러 검출의 핵심: 인터넷 체크섬 (Checksum)

데이터가 전송 중 변형(Bit flip)되었는지 확인하는 수학적 장치입니다.

### - 계산 단계 (송신측)

16비트 분할: 데이터를 16비트 정수들의 나열로 취급.

1의 보수 합 (1's complement sum): 모든 값을 더함.

Wraparound 처리: 덧셈 중 왼쪽 끝(MSB)에서 넘친 '1(Carry)'을 버리지 않고 다시 맨 오른쪽(LSB)에 더함.

비트 반전 (Inversion): 합산 결과의 모든 비트를 뒤집어(0↔1) 체크섬 필드에 저장.

### - 검증 단계 (수신측)

수신한 [데이터 합 + 체크섬]을 계산.

결과가 모든 비트가 1 (1111 1111 1111 1111)이면 정상. 하나라도 0이면 에러로 판단.

### 3. RDT (Reliable Data Transfer)의 인터페이스

애플리케이션과 네트워크 사이에서 신뢰성을 확보하기 위한 약속된 명령어들입니다.

rdt_send(): 애플리케이션이 데이터를 보낼 때 호출.

udt_send(): 신뢰할 수 없는 채널로 패킷을 전송.

rdt_rcv(): 패킷이 수신측에 도착했을 때 호출.

deliver_data(): 검증 완료된 데이터를 상위 앱으로 전달.

### 4. RDT의 단계별 발전 (Evolution)

### 1) rdt 1.0: 완벽한 채널

에러도, 손실도 없는 이상적인 환경.

동작: 단순히 데이터를 패킷화하여 보내고, 받아서 올림.

### 2) rdt 2.0: 비트 에러 발생 (ACK/NAK 도입)

메커니즘: 인간의 대화처럼 피드백(Feedback) 도입.

ACK: 잘 받았음 확인.

NAK: 에러 발생, 재전송 요청.

한계: ACK/NAK 신호 자체가 깨질 경우, 송신자는 패킷을 재전송하게 되고 수신자는 중복 패킷 문제를 겪음.

이를 해결하기 위해 패킷에 순서 번호라는 식별자를 넣어서 만든게 rdt 2.1임

### 3) rdt 2.1: 중복 문제 해결 (Sequence Number)

해결책: 패킷에 순서 번호(Sequence Number)를 부여.

1비트 번호: Stop-and-Wait 방식이므로 0번과 1번만 번갈아 써도 중복 판별 가능.

수신자는 번호를 보고 이미 받은 거라면 데이터는 버리고 ACK만 다시 전송함.

### 5. 에러 수정 철학 비교

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- RDT (Reliable Data Transfer) 프로토콜|[네트워크] RDT (Reliable Data Transfer) 프로토콜]]
- [[blog/NETWORK/네트워크- 전송 계층(Transport Layer)과 TCP-UDP|[네트워크] 전송 계층(Transport Layer)과 TCP/UDP]]
- [[blog/NETWORK/네트워크- rdt 3.0 과 TCP|[네트워크] rdt 3.0 과 TCP]]
