---
title: "[네트워크] IPv4 vs IPv6"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "NETWORK"
published: 2026-05-11
source_url: https://ch010104.tistory.com/273
archive_method: Tistory sitemap + HTML content extraction
---

# [네트워크] IPv4 vs IPv6

> 원문: https://ch010104.tistory.com/273

## 본문

1. 차세대 인터넷 프로토콜: IPv6 1.1 등장 동기 및 헤더 구조    주소 고갈 해결: 32비트(2^32)의 IPv4 주소를 128비트(2^128)로 확장하여 무한에 가까운 주소 공간 확보. 고정 길이 헤더 (40바이트): 가변적이었던 IPv4와 달리 헤더를 고정하여 라우터의 하드웨어 처리 속도를 비약적으로 향상. 주요 필드 분석:  Priority: 데이터의 우선순위 식별. Flow Label: 실시간 스트리밍 등 동일 '흐름' 패킷 식별. Next Header: 상위 프로토콜(TCP/UDP) 혹은 확장 헤더 식별. Hop Limit: 라우터를 거칠 때마다 감소하는 수치(TTL).    1.2 IPv4-IPv6 과도기 기술: 터널링(Tunneling)    IPv6 패킷이 IPv4 전용 구간을 통과하기 위해 사용하는 핵심 기술입니다.  동작 원리: IPv6 데이터그램 전체를 IPv4 패킷의 페이로드로 캡슐화("Packet within a packet"). 주소 변화 사례 (A에서 F로 전송 시):  터널 진입 전: [Src: A, Dest: F] (순수 IPv6) 터널 내부 (B-E 구간): 겉면에 [Src: B, Dest: E]라는 IPv4 헤더를 덧씌움. 내부에는 여전히 [Src: A, Dest: F] 정보 유지. 터널 탈출 후: 겉면의 IPv4 헤더를 제거하고 원래의 [Src: A, Dest: F] 패킷으로 목적지 도달.    2. 일반화된 전달과 OpenFlow 실전 사례 전통적인 라우팅(목적지 기반)을 넘어, 패킷의 모든 계층 정보를 이용한 제어가 가능해졌습니다. 2.1 "Match + Action"의 구체적 구현 사례 OpenFlow 규칙을 통해 장비의 정체성을 소프트웨어로 결정합니다.       계층 3 라우팅 예시: * Match: IP Dst = 51.6.0.8  Action: forward(port 6)   방화벽(Firewall) 예시:  특정 서비스 차단: TCP d-port = 22 (SSH) -> Action: drop 특정 호스트 차단: IP Src = 128.119.1.1 -> Action: drop   계층 2 스위칭 예시:  Match: MAC dst = 22:A7:23:11:E1:02 Action: forward(port 3)    2.2 네트워크 전체 오케스트레이션 (Network-wide Orchestration)    중앙 컨트롤러가 여러 스위치를 동시에 조종하여 특정 경로를 강제하는 사례입니다.  시나리오: 호스트 h5/h6의 트래픽을 s1을 거쳐 s2로 보내도록 설정. 스위치별 규칙 배포:  s3: 10.3 대역에서 오는 패킷을 s1 방향(port 3)으로 전송. s1: s3에서 온 패킷을 s2 방향(port 4)으로 단순 토스. s2: 최종 목적지 IP(.3 또는 .4)에 따라 각 호스트 h3, h4로 배달.    3. 인터넷의 아키텍처와 설계 철학 3.1 종단 간 원칙 (End-to-End Argument)    Saltzer 등의 논리 (1981): "특정 기능의 완벽한 구현은 결국 양 끝단의 애플리케이션만이 보장할 수 있다." 신뢰성 전송 비교:  End-to-End: 라우터는 전달만, 재전송 등은 호스트(TCP)가 담당. (인터넷의 선택) Hop-by-hop: 모든 라우터가 에러 체크. (과도한 부하로 현대 인터넷에 부적합)    3.2 Narrow Waist (모래시계 모델)  하위의 다양한 물리 매체(WiFi, 5G 등)와 상위의 수만 가지 앱(Web, 게임 등) 사이를 IP라는 단 하나의 프로토콜이 이어주는 구조. 이 단순함이 인터넷의 폭발적 확장을 가능케 함.  3.3 지능의 위치 변화 (Intelligence Location)  과거 (전화망): 네트워크 중심부(교환기)가 매우 똑똑하고 전화기는 멍청함. 인터넷 초기: 네트워크 내부는 단순한 전달(벽돌)만 수행, 지능은 끝단(PC)에 집중. 현대: SDN의 등장으로 네트워크 내부도 프로그래밍 가능해졌으며(똑똑해짐), 끝단의 인프라도 거대해짐(Post-2005 모델).  4. 미들박스(Middleboxes)와 SDN의 역할  미들박스: NAT, 방화벽, 로드밸런서 등 라우팅 이외의 특수 기능을 수행하는 장치. SDN의 의의: 과거에는 각 미들박스를 하드웨어로 따로 구매해야 했으나, 이제는 OpenFlow의 "Match + Action" 추상화를 통해 일반 스위치 위에서 소프트웨어로 모든 미들박스 기능을 통합 구현 가능.
