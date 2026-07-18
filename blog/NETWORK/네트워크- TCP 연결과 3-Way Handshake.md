---
title: "[네트워크] TCP 연결과 3-Way Handshake"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Network"]
category: "NETWORK"
published: 2026-04-15
source_url: https://ch010104.tistory.com/262
---

# [네트워크] TCP 연결과 3-Way Handshake

## 원문

https://ch010104.tistory.com/262

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

개념: 클라이언트의 요청(req_conn)에 서버가 응답(acc_conn)하면 즉시 연결되는 방식.

가변 지연(Variable delays) 및 패킷 재전송으로 인해, 클라이언트는 이미 포기한 "과거의 요청 패킷(Stale packet)"이 뒤늦게 서버에 도착할 수 있음.

## 원문 기반 개념 정리

### 1. TCP 연결 설정 (Connection Establishment)

### 1.1 2-Way Handshake의 한계

개념: 클라이언트의 요청(req_conn)에 서버가 응답(acc_conn)하면 즉시 연결되는 방식.

문제점:

가변 지연(Variable delays) 및 패킷 재전송으로 인해, 클라이언트는 이미 포기한 "과거의 요청 패킷(Stale packet)"이 뒤늦게 서버에 도착할 수 있음.

서버는 이를 새로운 요청으로 오해하여 자원을 할당하지만, 클라이언트는 응답하지 않음 -> 자원 낭비(Half-Open Connection) 발생.

### 1.2 3-Way Handshake (표준 방식)

목적: 양방향 신뢰성 확보 및 초기 순서 번호(Seq #) 동기화.

단계별 과정:

SYN (Step 1): 클라이언트가 임의의 번호 x를 생성해 전송. (SYNbit=1, Seq=x)

상태: 클라이언트 SYN_SENT

SYN-ACK (Step 2): 서버가 자신의 번호 y를 생성하고 클라이언트의 $x$를 확인. (SYNbit=1, Seq=y, ACKbit=1, ACKnum=x+1)

상태: 서버 SYN_RCVD

ACK (Step 3): 클라이언트가 서버의 y를 확인. (ACKbit=1, ACKnum=y+1)

상태: 클라이언트/서버 모두 ESTABLISHED (연결 완료)

코드 레벨:

Client: connect() 호출 시 위 과정이 내부적으로 실행됨.

Server: listen() 상태에서 대기하다가 accept()가 리턴되는 시점이 Step 3 완료 후임.

### 2. TCP 데이터 전송 메커니즘

### 2.1 ACK 생성 규칙 (RFC 5681)

수신측은 네트워크 부하를 줄이기 위해 전략적으로 ACK를 보냅니다.

### 2.2 Seq #와 ACK #의 상호작용 (Telnet 예시)

Seq #: 내가 보내는 데이터의 첫 번째 바이트 번호.

ACK #: 상대방으로부터 받고 싶은 다음 바이트 번호 (상대방이 보낸 Seq + 데이터 크기).

피기배킹(Piggybacking): 수신 확인(ACK) 패킷에 실제 데이터(Data)를 실어서 한 번에 보내는 기술.

예: Seq=42, ACK=79, data='C' -> 나는 42번부터 보내고, 너의 78번까지 잘 받았으니 79번을 다오.

### 3. 흐름 제어 (Flow Control)

### 3.1 목적 및 개념

목적: 송신측 전송 속도가 수신측 처리 속도보다 빠를 때 발생하는 수신 버퍼 오버플로우 방지.

원리: 수신측이 송신측을 제어함.

### 3.2 rwnd (Receive Window) 관리

RcvBuffer: OS가 소켓에 할당한 전체 버퍼 크기 (기본 약 4096 bytes).

rwnd (수신 윈도우): 버퍼 중 현재 비어 있어 추가 수용 가능한 공간.

수식: rwnd = RcvBuffer - [LastByteRcvd - LastByteRead]

광고(Advertising): 수신측은 모든 ACK 패킷 헤더의 window size 필드에 현재 rwnd 값을 담아 보냄. 송신측은 확인 응답 받지 못한 데이터의 합이 rwnd를 넘지 않도록 제한함.

### 4. 연결 종료 (Connection Termination)

### 4.1 4-Way Handshake 과정

한쪽이 닫아도 반대쪽은 보낼 게 남을 수 있어 4단계로 진행됩니다.

FIN (Client): 클라이언트가 close() 호출. "보낼 거 끝났다." (FIN_WAIT_1)

ACK (Server): 서버가 확인 응답. (CLOSE_WAIT). 클라이언트는 서버가 닫기를 기다림 (FIN_WAIT_2).

FIN (Server): 서버도 보낼 거 다 보내면 종료 선언. (LAST_ACK)

ACK (Client): 클라이언트의 최종 확인. 서버는 즉시 CLOSED. 클라이언트는 TIME_WAIT 진입.

### 4.2 TIME_WAIT 상태의 이유

최종 ACK 유실 대비: 클라이언트의 마지막 ACK가 사라지면 서버는 FIN을 재전송함. 이를 처리하기 위해 기다림.

지연 패킷 방지: 네트워크를 떠돌던 이전 연결의 패킷이 새로운 연결(같은 포트 번호)에 섞여 들어가는 현상 차단.

대기 시간: 보통 $2 \times MSL$ (Maximum Segment Lifetime) 동안 유지.

### 5. 핵심 용어 및 필드 비교

FINbit vs Seq:

FINbit: 1비트 플래그. 패킷의 '종류'가 종료 신호임을 표시 (Yes/No).

Seq: 32비트 숫자. 데이터의 '순서'를 나타내는 값. (종료 시 FIN 신호도 1바이트를 소비한 것으로 간주하여 번호를 부여함).

상태 요약:

LISTEN: 서버가 요청 대기 중.

ESTABLISHED: 연결 완료, 데이터 전송 중.

TIME_WAIT: 종료 후 유실 패킷 처리를 위한 대기 시간.

## 관련 글

- [[blog/NETWORK/index|NETWORK]]
- [[blog/NETWORK/네트워크- rdt 3.0 과 TCP|[네트워크] rdt 3.0 과 TCP]]
- [[blog/NETWORK/네트워크- TCP 혼잡 제어 및 전송|[네트워크] TCP 혼잡 제어 및 전송]]
- [[blog/NETWORK/네트워크- 네트워크 계층(Network Layer) 의 구조|[네트워크] 네트워크 계층(Network Layer) 의 구조]]
