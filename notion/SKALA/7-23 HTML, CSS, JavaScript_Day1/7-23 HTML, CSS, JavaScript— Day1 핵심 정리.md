---
title: "[7/23] HTML, CSS, JavaScript— Day1 핵심 정리"
notion_page_id: "3a61d84b-f68e-804c-957b-fb4c37f43860"
source_url: https://app.notion.com/p/3a61d84bf68e804c957bfb4c37f43860
synced_at: "2026-07-25T15:07:17.778891+00:00"
content_sha256: "fa26af9cecf1d351bac5c18ddffbd6503f0176ffcae68c0fe082af3102464e47"
---

# [7/23] HTML, CSS, JavaScript— Day1 핵심 정리

> 원본: [[7/23] HTML, CSS, JavaScript— Day1 핵심 정리](https://app.notion.com/p/3a61d84bf68e804c957bfb4c37f43860)

[[notion/SKALA/index|SKALA 학습 노트]]

<file src="file://%7B%22source%22%3A%22attachment%3Acae4b6ff-0deb-450b-8f10-e38ecdc0db88%3A1)_Full-stack_Engineering_2.HTMLCSSJavaScript_%E1%84%80%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A9_0720.pdf%22%2C%22permissionRecord%22%3A%7B%22table%22%3A%22block%22%2C%22id%22%3A%223a61d84b-f68e-80a8-9806-c1654dbc0920%22%2C%22spaceId%22%3A%22ee81d84b-f68e-815c-b261-00039e7d544f%22%7D%7D"></file>
## 인터넷의 물리적 구성 (Physical Infrastructure)
인터넷은 크게 **종단 시스템 · 전송 매체 · 네트워크 장비** 세 요소로 구성됨.
#### 종단 시스템 (End Systems)
- 네트워크의 가장자리(Edge)에 위치해 프로토콜을 직접 실행하고 데이터를 **생성·소비**하는 단말 기기임.
- **Client**: 서비스를 요청하는 쪽 (스마트폰, PC 등 — 웹 브라우저로 요청)
- **Server**: 요청에 응답해 서비스를 제공하는 고성능 컴퓨터 (Web/DB Server 등)
- 각 종단 시스템은 **고유 IP 주소**를 식별자로 할당받아 애플리케이션 프로세스를 구동함.
#### 전송 매체 (Transmission Media)
데이터 신호가 **물리 계층 위에서 이동하는 채널**을 제공하는 매체임.
<table header-row="true">
<tr>
<td>구분</td>
<td>예시</td>
</tr>
<tr>
<td>**유선**</td>
<td>광케이블, Ethernet(LAN선), 해저 광케이블</td>
</tr>
<tr>
<td>**무선**</td>
<td>Wi-Fi, 5G/LTE, 위성통신</td>
</tr>
</table>
---
### 네트워크 장비 (Network Equipment)
**패킷(Packet)의 헤더 정보를 파싱**해 최적 경로를 정하고 다음 목적지로 포워딩(Forwarding)하는 노드 장비임.
- **Router**: 서로 다른 네트워크를 연결하고, 패킷의 경로를 배정(**라우팅**)하는 장치
- **Switch**: 하나의 네트워크 안에서 여러 기기를 유선 연결하고 데이터를 분배하는 장치
---
#### 프로토콜과 계층 구조 (Protocol & Layers)

인터넷에서 데이터를 주고받기 위한 **규칙·약속**을 네트워크 기능별로 계층(Layer)으로 나눠 정의한 것임.
- **OSI 7 Layers**: 학술적·이론적 모델 표준 (네트워크 구조 이해용)
- **TCP/IP 4 Layers**: 실무적 모델로, 인터넷의 사실상 표준임
#### TCP/IP 4계층 역할
- **Network Access Layer**: 물리적 케이블·랜카드로 데이터를 **비트(0,1)** 단위로 전달
- **Internet Layer**: 최적 경로를 찾고 **IP 주소**를 부여
- **Transport Layer**: 데이터를 목적지까지 **안전·정확하게** 전달
- **Application Layer**: 사용자가 쓰는 앱과 직접 상호작용
#### OSI ↔ TCP/IP 계층 대응 & PDU
<table header-row="true">
<tr>
<td>OSI 7계층</td>
<td>TCP/IP 4계층</td>
<td>주요 프로토콜</td>
<td>PDU(데이터 단위)</td>
</tr>
<tr>
<td>응용 / 표현 / 세션</td>
<td>Application</td>
<td>HTTP, FTP, DNS, DHCP</td>
<td>Data/Message</td>
</tr>
<tr>
<td>전송(Transport)</td>
<td>Transport</td>
<td>TCP, UDP</td>
<td>Segment(TCP) / Datagram(UDP)</td>
</tr>
<tr>
<td>네트워크(Network)</td>
<td>Internet</td>
<td>IP, ICMP</td>
<td>Packet</td>
</tr>
<tr>
<td>데이터 링크</td>
<td>Network Access</td>
<td>Ethernet, ATM</td>
<td>Frame</td>
</tr>
<tr>
<td>물리(Physical)</td>
<td>Network Access</td>
<td>—</td>
<td>Bit</td>
</tr>
</table>
- **PDU(Protocol Data Unit)**: 각 계층에서 다루는 데이터 단위의 이름. 계층을 내려갈수록 헤더가 붙으며 이름이 바뀜 (Message → Segment → Packet → Frame → Bit).
- OSI의 상위 3계층(응용·표현·세션)이 TCP/IP에서는 **Application 하나로 통합**됨.
---
### TCP/IP 하위 계층 정리 (Network Access + Internet Layer)
TCP/IP 4계층 중 **하위 두 계층**으로, 실제 물리적 전송과 네트워크 간 경로 배정을 담당함.
#### 1) 네트워크 액세스 계층 (Network Access Layer)
- OSI의 **물리 + 데이터 링크 계층**을 통합한 계층. 매체(광케이블·LAN선·무선)로 데이터를 **전기 신호**로 변환해 실제 전송함.
- **데이터 단위: Frame**
- 핵심 Protocol: **Ethernet**(유선 규격), **Wi-Fi / IEEE 802.11**(무선 규격)
#### MAC (Media Access Control) Address
- **하드웨어 고유의 물리적 식별자**로, 하드웨어에 영구 기록되어 \<u\>변경되지 않음\</u\>.
- **48비트(6바이트)** = 16진수 12자리 표기 (예: `8C-B0-E9-D8-30-A8`)
- 확인: Windows `ipconfig /all`, macOS `ifconfig` → **"물리적 주소"** 항목
#### 2) 인터넷 계층 (Internet Layer)
- 논리적 주소(IP)를 사용해 서로 다른 네트워크 간 통신을 가능하게 함.
- **데이터 단위: Packet**
- 핵심 Protocol: **IP**(주소 부여·경로 지정), **ICMP**(오류·상태 메시지 전달)
#### IP Address — 인터넷에서 각 장치를 식별하는 고유 주소
<table header-row="true">
<tr>
<td>구분</td>
<td>IPv4</td>
<td>IPv6</td>
</tr>
<tr>
<td>표기</td>
<td>`192.168.0.1` (점 3개로 나뉜 숫자 4개)</td>
<td>`2001:0db8:...:7334`</td>
</tr>
<tr>
<td>주소 수</td>
<td>약 **43억 개** → \<u\>거의 고갈\</u\></td>
<td>사실상 무한대 (고갈 걱정 X)</td>
</tr>
<tr>
<td>등장 이유</td>
<td>—</td>
<td>IPv4 주소 부족 해결</td>
</tr>
</table>
#### 공인 IP vs 사설 IP
- **Public IP**: 전 세계 인터넷 망(WAN)에서 \<u\>유일무이\</u\>하게 식별되는 주소
- **Private IP**: 폐쇄된 내부 네트워크(LAN) **안에서만** 쓰이는 주소 (예: `172.16.20.59`)
- **NAT (Network Address Translation)**: 하나의 공인 IP ↔ 여러 사설 IP를 상호 **변환**하는 기술
#### 두 계층의 식별자 비교 (핵심)
<table header-row="true">
<tr>
<td></td>
<td>MAC 주소</td>
<td>IP 주소</td>
</tr>
<tr>
<td>계층</td>
<td>Network Access</td>
<td>Internet</td>
</tr>
<tr>
<td>성격</td>
<td>**물리적**(하드웨어 고정)</td>
<td>**논리적**(네트워크 따라 가변)</td>
</tr>
<tr>
<td>역할</td>
<td>같은 네트워크 내 장치 식별</td>
<td>서로 다른 네트워크 간 통신·경로 지정</td>
</tr>
</table>
---
### 전송 계층 (Transport Layer)
데이터 전송의 **신뢰성**을 담당하는 계층임. **데이터 단위: Segment**, 핵심 Protocol은 **TCP · UDP**임.
#### TCP vs UDP 비교
<table header-row="true">
<tr>
<td>구분</td>
<td>**TCP** (Transmission Control)</td>
<td>**UDP** (User Datagram)</td>
</tr>
<tr>
<td>방식</td>
<td>**연결 지향** (전송 전 **3-Way Handshake**로 연결 확립)</td>
<td>**비연결형** (연결 없이 일방적으로 던짐)</td>
</tr>
<tr>
<td>신뢰성</td>
<td>\<u\>높음\</u\> — 유실 시 재전송, 순서 보장</td>
<td>\<u\>낮음\</u\> — 유실·순서 뒤바뀜 미보정</td>
</tr>
<tr>
<td>속도</td>
<td>느림, 오버헤드 큼</td>
<td>**매우 빠름**, 헤더 가벼움</td>
</tr>
<tr>
<td>용도</td>
<td>신뢰성이 중요한 서비스 — 웹(HTTP), 파일 전송(FTP), 이메일(SMTP)</td>
<td>실시간성이 중요한 서비스 — 실시간 스트리밍, 온라인 게임</td>
</tr>
</table>
- 핵심 트레이드오프: **신뢰성(TCP) ↔ 속도(UDP)**. 약간의 손실이 허용되고 실시간성이 중요하면 UDP를 씀.
#### 포트/연결 현황 확인
- **Windows**: `netstat -an`
- **macOS**: `lsof -i TCP -P -n`
- → 프로토콜·로컬 주소·외부 주소·상태(LISTENING 등)가 출력됨.
---
### 웹 접속 전체 흐름 (Web Connection Workflow)

브라우저에 URL을 입력한 순간부터 페이지가 화면에 뜨기까지의 순서를 정리한 것임.
#### 접속 단계 (순서)
1. **DNS 조회** — 브라우저가 DNS 서버에 도메인의 **IP 주소를 문의** (예: `www.example.com` → `93.184.216.34`)
2. **TCP 3-Way Handshake** — 클라이언트와 서버가 신뢰할 수 있는 통신 통로를 수립
	- **SYN**(연결요청) → **SYN+ACK**(수락응답+연결요청) → **ACK**(연결확립) 의 3단계
3. **HTTP 요청/응답** — 통로가 수립되면 브라우저가 **HTTP 요청(GET)** 전송 → 서버가 **HTML/CSS/JS** 응답
4. **렌더링 & 표시** — 브라우저가 받은 HTML/CSS/JS를 렌더링해 **웹 페이지를 화면에 표시**
#### 흐름 요약
`URL 입력 → DNS(IP 조회) → TCP 연결(Handshake) → HTTP 요청/응답 → 렌더링 → 페이지 표시`
---
#### WWW (World Wide Web)
인터넷 상에서 **웹 페이지를 통해 정보를 주고받는 서비스**의 한 형태임. 웹 페이지는 **HTML로 작성**되고 웹 브라우저로 열람함.
#### WEB의 3대 개념
<table header-row="true">
<tr>
<td>질문</td>
<td>요소</td>
<td>의미</td>
</tr>
<tr>
<td>**어떻게**</td>
<td>HTTP (HyperText Transfer Protocol)</td>
<td>데이터를 주고받는 통신 규약</td>
</tr>
<tr>
<td>**어디로**</td>
<td>URL (Uniform Resource Locator)</td>
<td>자원의 위치(주소)</td>
</tr>
<tr>
<td>**무엇을**</td>
<td>HTML (HyperText Markup Language)</td>
<td>웹 페이지를 구성하는 문서 언어</td>
</tr>
</table>
#### Internet vs WWW (핵심 구분)
<table header-row="true">
<tr>
<td>구분</td>
<td>인터넷 (Internet)</td>
<td>웹 (WWW)</td>
</tr>
<tr>
<td>정의</td>
<td>전 세계 컴퓨터를 연결한 **물리적 통신망(인프라)**</td>
<td>인터넷 위에서 정보를 공유하는 **정보 공간(서비스)**</td>
</tr>
<tr>
<td>구성 요소</td>
<td>케이블·라우터·스위치·컴퓨터 (**하드웨어**)</td>
<td>HTML·HTTP·URL·브라우저 (**소프트웨어**)</td>
</tr>
<tr>
<td>TCP/IP 기준 계층</td>
<td>하위 계층 (인터넷·전송 계층 중심)</td>
<td>**최상위 응용 계층**</td>
</tr>
<tr>
<td>포함 관계</td>
<td>전체 인프라 (모든 서비스의 기반)</td>
<td>인프라 위 \<u\>수많은 서비스 중 하나\</u\></td>
</tr>
</table>
#### WWW — Client와 Server
웹은 요청하는 **Client**와 응답하는 **Server**의 상호작용으로 동작함.
#### Client
- 웹 페이지를 **요청하는** 사용자의 컴퓨터·장치
- 대표 클라이언트 소프트웨어는 **웹 브라우저** (Chrome, Edge, Safari 등)
#### Server
- 클라이언트의 요청을 받아 처리하고 데이터를 **제공하는** 컴퓨터
- 웹 서버는 **HTML·이미지·CSS·JavaScript** 등을 저장했다가 클라이언트에 전달
#### 대표 웹 서버
<table header-row="true">
<tr>
<td>Web Server</td>
<td>특징</td>
</tr>
<tr>
<td>**Apache**</td>
<td>오픈소스, \<u\>모든 OS에서 동작\</u\> (1995, Apache SW Foundation)</td>
</tr>
<tr>
<td>**Nginx**</td>
<td>오픈소스+상용, 모든 OS 동작. **빠른 속도·가벼운 리소스**, 이벤트 기반 **비동기** 처리</td>
</tr>
<tr>
<td>**Microsoft IIS**</td>
<td>Windows 전용, Windows 생태계에 최적화 (1995, Microsoft)</td>
</tr>
</table>
---
#### URL (Uniform Resource Locator)

네트워크 상에서 **자원(리소스)의 위치와 접근 방법**을 나타내는 주소 규약임. 통신 프로토콜, 서버 위치(도메인/IP), 포트, 경로, 파일명, 쿼리 등이 결합된 구조로 이뤄짐.
#### URL 구성 요소
예시: `http://www.codns.com:80/codns/codns.jsp?id=1`
<table header-row="true">
<tr>
<td>구성</td>
<td>예시</td>
<td>의미</td>
</tr>
<tr>
<td>**통신 프로토콜**</td>
<td>`http://`</td>
<td>자원에 접근하는 통신 규약</td>
</tr>
<tr>
<td>**호스트 / 도메인**</td>
<td>`www.codns.com`</td>
<td>서버 위치. `www`(3차/서브 도메인) · `codns`(2차/메인) · `.com`(**최상위 도메인 TLD**)</td>
</tr>
<tr>
<td>**포트 번호**</td>
<td>`:80`</td>
<td>서버 내 접속 지점 (HTTP 기본 80, 생략 가능)</td>
</tr>
<tr>
<td>**디렉터리 경로**</td>
<td>`/codns/`</td>
<td>서버 내 폴더 경로</td>
</tr>
<tr>
<td>**파일 / 형식**</td>
<td>`codns.jsp`</td>
<td>요청 파일명과 확장자(형식)</td>
</tr>
<tr>
<td>**쿼리 (Query String)**</td>
<td>`?id=1`</td>
<td>`?` 뒤에 붙는 매개변수(parameter)</td>
</tr>
</table>
---
#### HTTP (HyperText Transfer Protocol)
클라이언트와 웹 서버가 **HTTP 요청(Request)을 보내고 응답(Response)을 받는** 방식으로 통신하는 프로토콜임.
#### HTTP Request / Response 흐름
1. 클라이언트(브라우저)가 웹에 \*\*HTTP 요청(Request)\*\*을 보냄
2. 웹 서버가 요청을 **수신**
3. 서버가 애플리케이션을 실행해 요청을 **처리**
4. 서버가 처리 결과를 \*\*HTTP 응답(Response)\*\*으로 브라우저에 반환
5. 클라이언트(브라우저)가 응답을 **수신**
`클라이언트 --요청 메시지(request)--> 웹 서버` / `웹 서버 --응답 메시지(response)--> 클라이언트`
- 웹 통신은 항상 **클라이언트의 요청으로 시작**되고, 서버는 요청이 있어야 응답하는 **요청-응답(Request-Response) 구조**임.
#### HTTP - Request
클라이언트가 서버에 보내는 요청 메시지의 구조와 방식임.
#### HTTP Request 구성요소
<table header-row="true">
<tr>
<td>구성</td>
<td>내용</td>
<td>예시</td>
</tr>
<tr>
<td>**Request Line**</td>
<td>Request Method + URL + HTTP 버전</td>
<td>`POST /test/demo_form.php HTTP/1.1`</td>
</tr>
<tr>
<td>**Request Header**</td>
<td>요청 부가정보 (User-Agent, Content-Type 등)</td>
<td>`Host: w3schools.com`</td>
</tr>
<tr>
<td>**Request Body**</td>
<td>서버로 보낼 실제 Data</td>
<td>`name1=value1&name2=value2`</td>
</tr>
</table>
#### HTTP Methods
- **GET**: 지정한 자원에서 데이터를 **조회(요청)**
- **POST**: 서버로 데이터를 **보내 자원을 생성/수정**
- 그 외: PUT, HEAD, DELETE, PATCH, OPTIONS, CONNECT, TRACE
- **GET**은 조회용이라 보낼 데이터가 없어 Body가 비고, **POST**는 전송할 데이터를 **Request Body**에 담는 점이 핵심 차이임.
#### HTTP - Response
서버가 클라이언트 요청에 대해 돌려주는 응답 메시지의 구조와 상태 코드임.
#### HTTP Response 구성요소
<table header-row="true">
<tr>
<td>구성</td>
<td>내용</td>
<td>예시</td>
</tr>
<tr>
<td>**Status Line**</td>
<td>HTTP 버전 + 상태 코드 + 상태 메시지</td>
<td>`HTTP/1.1 200 OK`</td>
</tr>
<tr>
<td>**Response Header**</td>
<td>응답 부가정보 (Content-Type, Server 등)</td>
<td>`Content-Type: application/json; charset=utf-8`</td>
</tr>
<tr>
<td>**Response Body**</td>
<td>실제 응답 데이터 (HTML, JSON 등)</td>
<td>`{ "userId": 1, "id": 1, ... }`</td>
</tr>
</table>
#### HTTP Status Codes
<table header-row="true">
<tr>
<td>코드 대역</td>
<td>의미</td>
<td>대표 예시</td>
</tr>
<tr>
<td>**1xx**</td>
<td>Informational (정보)</td>
<td>—</td>
</tr>
<tr>
<td>**2xx**</td>
<td>Success (성공)</td>
<td>200 OK, 201 Created</td>
</tr>
<tr>
<td>**3xx**</td>
<td>Redirection (리다이렉션)</td>
<td>304 Not Modified</td>
</tr>
<tr>
<td>**4xx**</td>
<td>Client Error (**클라이언트** 잘못)</td>
<td>400 Bad Request, 404 Not Found</td>
</tr>
<tr>
<td>**5xx**</td>
<td>Server Error (**서버** 잘못)</td>
<td>500 Internal Server Error</td>
</tr>
</table>
- 상태 코드는 **앞자리 숫자**로 성격이 갈림. **4xx는 요청한 쪽(클라이언트) 문제**, **5xx는 처리하는 쪽(서버) 문제**라는 구분이 핵심임.
---
#### HTTP - HTTPS (HyperText Transfer Protocol Secure)

HTTP의 **보안 버전**으로, **SSL(Secure Sockets Layer) / TLS(Transport Layer Security)** 암호화를 사용해 데이터를 보호함.
#### 암호화 범위
- **암호화됨**: Request Headers, Request Body, Response Headers, Response Body (실제 주고받는 내용 전체)
- **암호화 안 됨**: 목적지 주소(**도메인과 IP**) — 목적지까지 배달하려면 이 주소만은 노출돼야 하기 때문임
<table header-row="true">
<tr>
<td>항목</td>
<td>암호화 여부</td>
</tr>
<tr>
<td>요청/응답 헤더·바디 (id/pw, Cookie, 본문 데이터 등)</td>
<td>O (암호화)</td>
</tr>
<tr>
<td>목적지 도메인 / IP</td>
<td>X (노출)</td>
</tr>
</table>
#### 실무 위치
- HTTPS는 현재 웹사이트의 **기본 표준**임.
- Google 크롬 등 브라우저는 HTTPS를 쓰지 않는 사이트에 \*\*"보안 위험 경고"\*\*를 표시함 (예: "이 사이트는 보안 연결(HTTPS)이 사용되지 않았습니다").
- 비밀번호·신용카드 번호 같은 민감 정보가 평문으로 오가면 공격자에게 도용될 수 있어, 로그인·결제가 있는 서비스는 HTTPS가 필수임.
---
#### HTML - 개요
- \*HTML(HyperText Markup Language)\*\*은 웹 페이지를 만드는 **표준 마크업 언어**임.
- **Hyper-text**: 링크를 통해 웹 페이지 간 이동이 가능
- **Markup Language**: 태그를 사용해 문서의 **구조와 스타일**을 정의
#### 핵심 특징
- 웹 브라우저가 HTML 문서를 해석해 사용자가 보는 웹 페이지로 \*\*렌더링(Rendering)\*\*함
- 텍스트·이미지·링크·폼·멀티미디어 등 다양한 콘텐츠를 포함해 **구조화**함
- 다양한 기기·브라우저에서 작동함
- **CSS**로 스타일링, **JavaScript**로 동작을 추가할 수 있음 (HTML=구조 / CSS=스타일 / JS=동작)
#### 참고 — Markup vs. Markdown
<table header-row="true">
<tr>
<td>구분</td>
<td>Markup</td>
<td>Markdown</td>
</tr>
<tr>
<td>정의</td>
<td>문서 구조·스타일을 **태그**로 지정하는 언어 (HTML, XML)</td>
<td>문서 작성용 **경량** 마크업 언어 (README, 블로그 / `.md`)</td>
</tr>
<tr>
<td>목적</td>
<td>콘텐츠 구조화 + 표현 제어 (스타일 포함)</td>
<td>텍스트 중심의 간단한 서식 표현</td>
</tr>
<tr>
<td>문법</td>
<td>복잡, **태그 기반** — 예: `<h1>제목</h1>`</td>
<td>직관적, **기호 기반** — 예: `# 제목`</td>
</tr>
</table>
- **Markup은 정밀한 구조·표현 제어**에, **Markdown은 빠르고 간단한 문서 작성**에 강점이 있음.
---
#### HTML - Page Structure
HTML 문서의 기본 뼈대 구조임. 크게 문서 선언 → `html` → `head`/`body`로 이뤄짐.
#### 기본 구조 요소
<table header-row="true">
<tr>
<td>요소</td>
<td>역할</td>
</tr>
<tr>
<td>**`<!DOCTYPE html>`**</td>
<td>**DTD(문서형 정의)**. 이 문서가 **HTML5** 문서임을 선언</td>
</tr>
<tr>
<td>**`<html>`**</td>
<td>HTML 문서의 **시작과 끝**을 감싸는 최상위 태그 (`lang` 속성으로 언어 지정)</td>
</tr>
<tr>
<td>**`<head>`**</td>
<td>문서 **정보(메타데이터)** 정의. 화면에 직접 표시되지 않음</td>
</tr>
<tr>
<td>**`<body>`**</td>
<td>웹 브라우저에 **실제 표시할 내용**</td>
</tr>
</table>
#### head 안의 주요 태그
- **`<meta charset="UTF-8">`**: 문자 인코딩 지정 (한글 깨짐 방지)
- **`<meta name="viewport" ...>`**: 반응형을 위한 화면 크기·배율 설정
- **`<title>`**: 브라우저 탭에 표시되는 문서 제목
#### 기본 골격 예시
html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>프로그래밍 기초 - HTML</title>
  </head>
  <body>
    <h1>2. HTML 개요</h1>
  </body>
</html>
```
- **`head`**** = 문서 설명서(브라우저·검색엔진용 정보)**, **`body`**** = 눈에 보이는 화면**으로 역할이 나뉘는 것이 핵심임.
#### HTML - 주요 태그 정리
카테고리별 대표 태그 모음임.
#### 문서 구조 & Metadata
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<html>`</td>
<td>문서의 **루트 요소**. 시작과 끝 표시</td>
</tr>
<tr>
<td>`<head>`</td>
<td>메타데이터(제목·스타일·스크립트) 정의</td>
</tr>
<tr>
<td>`<title>`</td>
<td>브라우저 탭에 표시되는 문서 제목</td>
</tr>
<tr>
<td>`<body>`</td>
<td>문서의 **본문 콘텐츠**</td>
</tr>
<tr>
<td>`<meta>`</td>
<td>문서 메타데이터 정의. **SEO** 및 브라우저 동작에 영향</td>
</tr>
<tr>
<td>`<link>`</td>
<td>외부 리소스(CSS 파일 등)와의 관계 정의</td>
</tr>
<tr>
<td>`<script>`</td>
<td>JavaScript 코드 삽입 또는 외부 스크립트 연결</td>
</tr>
</table>
#### Text / Contents
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<h1>~<h6>`</td>
<td>제목(Heading). `<h1>` 최대 \~ `<h6>` 최소</td>
</tr>
<tr>
<td>`<p>`</td>
<td>단락</td>
</tr>
<tr>
<td>`<br>`</td>
<td>줄바꿈 삽입</td>
</tr>
<tr>
<td>`<span>`</td>
<td>인라인 요소. 텍스트를 묶어 스타일·스크립트 적용</td>
</tr>
<tr>
<td>`<strong>`</td>
<td>중요 텍스트를 **굵게**</td>
</tr>
<tr>
<td>`<em>`</td>
<td>강조 텍스트를 *기울임꼴*로</td>
</tr>
<tr>
<td>`<a>`</td>
<td>하이퍼링크 생성 (`href` 속성으로 대상 지정)</td>
</tr>
<tr>
<td>`<hr>`</td>
<td>수평선</td>
</tr>
<tr>
<td>`<mark>`</td>
<td>형광펜 강조</td>
</tr>
<tr>
<td>`<small>`</td>
<td>작은 글씨</td>
</tr>
<tr>
<td>`<blockquote>`</td>
<td>인용 문단</td>
</tr>
<tr>
<td>\`\`</td>
<td>출처 인용</td>
</tr>
<tr>
<td>`<code>`</td>
<td>코드 조각 표현</td>
</tr>
<tr>
<td>`<pre>`</td>
<td>공백·줄바꿈 유지한 채 텍스트 표시</td>
</tr>
<tr>
<td>`<div>`</td>
<td>의미 없는 구획(block). 스타일·스크립트 용도</td>
</tr>
</table>
#### List & Table
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<ul>`</td>
<td>순서 **없는** 목록</td>
</tr>
<tr>
<td>`<ol>`</td>
<td>순서 **있는** 목록</td>
</tr>
<tr>
<td>`<li>`</td>
<td>목록 항목 (ul·ol 공통)</td>
</tr>
<tr>
<td>`<dl>` / `<dt>` / `<dd>`</td>
<td>설명 목록 / 설명 제목 / 설명 내용</td>
</tr>
<tr>
<td>`<table>`</td>
<td>표 정의</td>
</tr>
<tr>
<td>`<thead>` / `<tbody>` / `<tfoot>`</td>
<td>표의 머리글 / 본문 / 바닥글</td>
</tr>
<tr>
<td>`<tr>`</td>
<td>표의 행(Row)</td>
</tr>
<tr>
<td>`<th>`</td>
<td>헤더 셀 (굵게 + 가운데 정렬)</td>
</tr>
<tr>
<td>`<td>`</td>
<td>데이터 셀</td>
</tr>
</table>
#### Form
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<form>`</td>
<td>사용자 입력을 서버로 전송하는 폼 정의</td>
</tr>
<tr>
<td>`<input>`</td>
<td>입력 필드 (텍스트·비밀번호·체크박스 등)</td>
</tr>
<tr>
<td>`<button>`</td>
<td>버튼</td>
</tr>
<tr>
<td>`<label>`</td>
<td>입력 필드 설명 제공</td>
</tr>
<tr>
<td>`<textarea>`</td>
<td>여러 줄 텍스트 입력</td>
</tr>
<tr>
<td>`<select>` / `<option>`</td>
<td>드롭다운 선택 필드 / 선택 항목</td>
</tr>
<tr>
<td>`<fieldset>` / `<legend>`</td>
<td>입력 항목 그룹화 / 그룹 설명 제목</td>
</tr>
</table>
#### Media
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<img>`</td>
<td>이미지 삽입 (`src`=경로, `alt`=대체 텍스트)</td>
</tr>
<tr>
<td>`<audio>` / `<video>`</td>
<td>오디오 / 비디오 콘텐츠 삽입</td>
</tr>
<tr>
<td>`<source>`</td>
<td>audio·video에 미디어 소스 지정</td>
</tr>
<tr>
<td>`<track>`</td>
<td>자막 트랙</td>
</tr>
<tr>
<td>`<figure>` / `<figcaption>`</td>
<td>미디어+캡션 묶음 / 설명 캡션</td>
</tr>
</table>
#### Semantic (의미 태그)
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>`<header>` / `<footer>`</td>
<td>문서·섹션의 머리글 / 바닥글</td>
</tr>
<tr>
<td>`<main>`</td>
<td>문서의 주 콘텐츠</td>
</tr>
<tr>
<td>`<article>`</td>
<td>독립적인 콘텐츠</td>
</tr>
<tr>
<td>`<section>`</td>
<td>주제를 정의하는 섹션</td>
</tr>
<tr>
<td>`<aside>`</td>
<td>부가 콘텐츠 (예: 사이드바)</td>
</tr>
<tr>
<td>`<nav>`</td>
<td>네비게이션 링크 섹션</td>
</tr>
</table>
- **Semantic 태그**는 `<div>`처럼 단순 구획이 아니라 **의미(역할)를 가진 구획**임. 검색엔진·스크린리더가 문서 구조를 이해하기 쉬워져 SEO·접근성에 유리함.
---
#### HTML Elements (요소)
HTML 요소는 **시작 태그 + 콘텐츠 + 종료 태그**로 정의됨. 시작 태그부터 종료 태그까지 **전체**가 하나의 요소임.
```plain text
<tagname> Content goes here... </tagname>
```
#### 요소 구조 예시
<table header-row="true">
<tr>
<td>Start Tag</td>
<td>Element Content</td>
<td>End Tag</td>
<td>의미</td>
</tr>
<tr>
<td>`<h1>`</td>
<td>My First Heading</td>
<td>`</h1>`</td>
<td>제목 1</td>
</tr>
<tr>
<td>`<p>`</td>
<td>My first paragraph.</td>
<td>`</p>`</td>
<td>문단</td>
</tr>
<tr>
<td>`<br>`</td>
<td>none</td>
<td>none</td>
<td>줄바꿈</td>
</tr>
</table>
- 콘텐츠가 없는 요소를 빈 요소(empty element)라 함 (예: `<br>`, `<img>`, `<meta>`). 종료 태그가 없음.
#### 중첩 (Nesting)
HTML 요소는 **다른 요소를 포함**할 수 있음. 바깥 요소가 안쪽 요소를 감싸는 계층 구조를 이룸.
html
```html
<html>
  <body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
  </body>
</html>
```
#### 기타 특성
- HTML은 **대소문자를 구분하지 않음** (Not Case Sensitive). `<P>`와 `<p>`가 동일하게 동작하나, 관례상 **소문자 사용**이 권장됨.
#### HTML Attributes - Global Attributes
**모든 HTML Element에서 공통으로 사용 가능한 속성**임.
<table header-row="true">
<tr>
<td>Attribute</td>
<td>설명</td>
<td>예시</td>
</tr>
<tr>
<td>**id**</td>
<td>요소의 **고유 식별자**. JS·CSS에서 참조할 때 사용 - 중요</td>
<td>`<div id="title">...</div>`</td>
</tr>
<tr>
<td>**class**</td>
<td>CSS·JS에서 참조 가능한 클래스 이름 (**여러 개 가능**) - 중요</td>
<td>`<p class="red-color">...</p>`</td>
</tr>
<tr>
<td>**style**</td>
<td>인라인 스타일 지정 - 중요</td>
<td>`<h1 style="color:red;"></h1>`</td>
</tr>
<tr>
<td>title</td>
<td>요소의 추가 정보 (마우스 올리면 **툴팁** 표시)</td>
<td>`<img src="cat.jpg" title="고양이">`</td>
</tr>
<tr>
<td>lang</td>
<td>요소·콘텐츠의 언어 지정 (en, ko, fr 등)</td>
<td>`<html lang="ko">`, `<p lang="en">Hello</p>`</td>
</tr>
<tr>
<td>hidden</td>
<td>요소를 화면에 표시하지 않음 (렌더링 X)</td>
<td>`<div hidden>비밀 정보</div>`</td>
</tr>
<tr>
<td>tabindex</td>
<td>키보드 탭 순서 지정 (작은 숫자가 먼저)</td>
<td>`<button tabindex="1">확인</button>`</td>
</tr>
<tr>
<td>draggable</td>
<td>드래그 가능 여부 (true / false)</td>
<td>`<img src="logo.png" draggable="true">`</td>
</tr>
<tr>
<td>spellcheck</td>
<td>입력 텍스트 맞춤법 검사 여부 (true / false)</td>
<td>`<textarea spellcheck="true"></textarea>`</td>
</tr>
<tr>
<td>contenteditable</td>
<td>사용자가 콘텐츠를 편집 가능하게 설정 (true / false)</td>
<td>`<div contenteditable="true">편집 가능</div>`</td>
</tr>
<tr>
<td>dir</td>
<td>텍스트 방향 설정 (ltr, rtl, auto)</td>
<td>`<p dir="rtl">...</p>`</td>
</tr>
<tr>
<td>**data-\***</td>
<td>사용자가 **임의의 속성**을 생성</td>
<td>`<p data-name="spiderMan" data-hero="true">`</td>
</tr>
</table>
- **id는 문서 내 유일**, **class는 여러 요소에 중복 사용 가능**하다는 점이 핵심 차이임.
- **data-\*** 속성은 표준에 없는 커스텀 데이터를 요소에 심어 두고 JS에서 꺼내 쓸 때 사용함.
---
#### HTML Attributes - id
`id` 속성은 HTML 요소에 **고유한(unique) 식별자**를 부여함. 그 값은 **하나의 HTML 문서 안에서 중복될 수 없음**.
#### CSS에서의 사용
- CSS에서 id를 선택할 때는 **`#`**** 기호**를 붙임 → `#myHeader { ... }`
- (참고: class 선택자는 `.` 기호를 사용)
```html
<head>
  <style>
    #myHeader {
      background-color: lightblue;
      color: black;
      padding: 40px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1 id="myHeader">My Header</h1>
</body>
```
- 위 코드에서 `id="myHeader"`가 붙은 `<h1>`에만 배경색·여백·가운데 정렬 스타일이 적용됨.
- 고유값이므로 **특정 요소 하나를 정확히 지목**할 때 사용함. 여러 요소에 같은 스타일을 적용하려면 `class`를 쓰는 것이 맞음.
#### HTML Attributes - class
`class` 속성은 주로 **스타일시트의 클래스 이름을 가리킬 때** 사용함. JavaScript에서도 특정 클래스명을 가진 요소들에 접근·조작할 때 활용됨.
#### CSS에서의 사용
- CSS에서 class를 선택할 때는 **`.`**** 기호**를 붙임 → `.note { ... }`
```html
<head>
  <style>
    .note {
      font-size: 120%;
      color: red;
    }
  </style>
</head>
<body>
  <h1>My <span class="note">Important</span> Heading</h1>
  <p>This is some <span class="note">important</span> text.</p>
</body>
```
- 위 예시에서 `class="note"`가 붙은 **여러 요소에 동일한 스타일이 한꺼번에 적용**됨.
#### id와의 비교
<table header-row="true">
<tr>
<td>구분</td>
<td>id</td>
<td>class</td>
</tr>
<tr>
<td>중복</td>
<td>문서 내 **유일**</td>
<td>**여러 요소에 반복 사용 가능**</td>
</tr>
<tr>
<td>CSS 선택자</td>
<td>`#이름`</td>
<td>`.이름`</td>
</tr>
<tr>
<td>용도</td>
<td>특정 요소 하나를 지목</td>
<td>공통 스타일·그룹 처리</td>
</tr>
</table>
#### HTML Attributes - style
`style` 속성은 요소에 **인라인 스타일**(색상·글꼴·크기 등)을 직접 지정할 때 사용함.
```plain text
<tagname style="property:value;">
```
- **property**는 CSS 속성명, **value**는 CSS 값임.
#### 대표 CSS Property
<table header-row="true">
<tr>
<td>Property</td>
<td>역할</td>
<td>예시</td>
</tr>
<tr>
<td>**background-color**</td>
<td>요소의 배경색</td>
<td>`<body style="background-color:powderblue;">`</td>
</tr>
<tr>
<td>**color**</td>
<td>글자 색</td>
<td>`<h1 style="color:blue;">Heading</h1>`</td>
</tr>
<tr>
<td>**font-family**</td>
<td>글꼴</td>
<td>`<p style="font-family:courier;">Paragraph</p>`</td>
</tr>
<tr>
<td>**font-size**</td>
<td>글자 크기</td>
<td>`<h1 style="font-size:300%;">Heading</h1>`</td>
</tr>
<tr>
<td>**text-align**</td>
<td>텍스트 정렬</td>
<td>`<p style="text-align:center;">Paragraph</p>`</td>
</tr>
</table>
#### 적용 예시
```html
<body style="background-color:powderblue;">
  <h1 style="background-color:lightgray;">제목</h1>
  <p style="background-color:tomato;">문단</p>
</body>
```
- 각 요소에 개별적으로 배경색이 적용되며, `body`에 준 색은 전체 배경이 됨.
- 인라인 style은 특정 요소에만 즉시 적용되어 간편하지만, 요소마다 반복 작성해야 해 유지보수가 어려움. 여러 요소에 공통 적용할 때는 **class + 스타일시트**를 쓰는 것이 좋음.
---
#### HTML Headings - `<h1>` \~ `<h6>`
웹페이지에 표시할 **제목(title)·부제목(subtitle)**을 나타내는 태그임.
- **`<h1>`****이 가장 크고 중요**, **`<h6>`****으로 갈수록 작고 하위 수준**임.
- 검색엔진(Search engines)이 웹페이지의 **구조와 내용을 파악**하는 데도 사용됨.
```html
<body>
  <h1>Heading 1</h1>
  <h2>Heading 2</h2>
  <h3>Heading 3</h3>
  <h4>Heading 4</h4>
  <h5>Heading 5</h5>
  <h6>Heading 6</h6>
</body>
```
- Heading은 단순히 글자를 크게 만드는 태그가 아니라 **문서의 위계(계층 구조)를 표현하는 태그**임. 글자 크기만 키우려는 목적이면 CSS의 `font-size`를 쓰는 것이 맞음.
- SEO·접근성을 위해 `<h1>`은 페이지당 하나만 두고, 건너뛰지 않고 순서대로 사용하는 것이 권장됨.
#### HTML Paragraphs - `<p>`
`<p>` 요소는 단락(paragraph)을 정의함. 단락은 **항상 새 줄에서 시작**함.
```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```
#### 공백·줄바꿈 처리
브라우저는 페이지를 표시할 때 소스 코드의 **여분의 공백과 줄바꿈을 자동으로 제거**함.
- 소스에서 여러 줄로 나눠 쓰거나 스페이스를 여러 개 넣어도, 화면에는 **한 줄·공백 하나**로 합쳐져 렌더링됨.
- 즉 코드상의 들여쓰기·정렬은 가독성용일 뿐, 실제 출력에 반영되지 않음.
- 의도적으로 줄을 바꾸려면 **`<br>`**, 공백·줄바꿈을 그대로 살리려면 `<pre>`를 사용해야 함.
#### HTML Paragraphs - `<hr>` / `<br>`
<table header-row="true">
<tr>
<td>태그</td>
<td>의미</td>
<td>화면 효과</td>
</tr>
<tr>
<td>**`<hr>`**</td>
<td>주제의 전환(**thematic break**)</td>
<td>대부분 **수평선**을 그려 시각적으로 구분</td>
</tr>
<tr>
<td>**`<br>`**</td>
<td>줄바꿈(**line break**)</td>
<td>문장 중간에서 다음 줄로 내림</td>
</tr>
</table>
- 둘 다 빈 태그(empty tag)라 **종료 태그가 필요 없음**.
html
```html
<h1>This is heading 1</h1>
<p>This is some text.</p>
<hr>
<h2>This is heading 2</h2>
<p>This is some other text.</p>
<hr>
<p>This is<br>a paragraph<br>with line breaks.</p>
```
- `<hr>`은 섹션 사이를 나누는 **구분선**, `<br>`은 한 단락 안에서 줄만 바꾸는 용도임.
- `<br>`은 단락을 나누는 용도로 쓰면 안 됨. 별개 단락이면 `<p>`를 새로 여는 것이 올바른 사용임.
---
## HTML Block & Inline
모든 HTML Element는 기본 표시(**display**) 값을 가짐. 크게 **Block**과 **Inline**으로 나뉨.
<table header-row="true">
<tr>
<td>구분</td>
<td>Block Elements</td>
<td>Inline Elements</td>
</tr>
<tr>
<td>디스플레이</td>
<td>**새 줄에서 시작**, 가로 폭을 최대로 차지</td>
<td>텍스트·다른 인라인 요소와 **같은 줄에 표시**</td>
</tr>
<tr>
<td>영역 크기</td>
<td>기본적으로 **전체 폭** 차지</td>
<td>**콘텐츠 크기만큼**만 차지</td>
</tr>
<tr>
<td>배치</td>
<td>위/아래로 쌓임(수직 정렬), 겹치지 않음</td>
<td>다른 인라인 요소와 가로로 나란히 배치</td>
</tr>
<tr>
<td>주요 태그</td>
<td>`<div>`, `<p>`, `<h1>~<h6>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<form>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<nav>`</td>
<td>`<span>`, `<a>`, `<strong>`, `<em>`, `<b>`, `<i>`, `<img>`, `<input>`, `<label>`, `<button>`, `<small>`, `<code>`, `<mark>`</td>
</tr>
<tr>
<td>CSS 적용</td>
<td>width, height, margin, padding **모두 적용 가능**</td>
<td>**width·height 무시**, margin·padding은 **수평 방향만** 적용</td>
</tr>
<tr>
<td>용도</td>
<td>레이아웃 구성, 큰 영역 표현</td>
<td>텍스트·소규모 콘텐츠 강조, 링크, 부분 스타일 적용</td>
</tr>
</table>
- 핵심 차이는 줄을 차지하느냐(Block) / 줄 안에 끼어드느냐(Inline)임.
- Inline 요소에 크기를 지정해야 하면 CSS로 `display: inline-block` 또는 `block`으로 바꿔야 함.
#### HTML Inline Container - `<span>`
`<span>`은 텍스트나 문서의 일부를 감싸는 인라인 컨테이너(inline container)임.
- 필수 속성은 없으나 **style, class, id** 속성이 일반적으로 함께 사용됨.
- CSS와 결합해 **텍스트의 특정 부분에만 스타일을 지정**할 때 활용함.
```html
<p>My mother has <span style="color:blue;font-weight:bold;">blue</span> eyes
and my father has <span style="color:darkolivegreen;font-weight:bold;">dark green</span> eyes.</p>
```
- 문장 흐름을 끊지 않고 **일부 단어만** 색·굵기를 다르게 표현할 수 있음.
- `<span>` 자체에는 의미가 없음. **`<div>`****가 블록 단위 구획**이라면 **`<span>`****은 인라인 단위 구획**이라는 대응 관계로 기억하면 됨.
#### HTML Div - `<div>`
`<div>`는 **다른 HTML 요소들을 담는 컨테이너**로 사용됨.
- 기본적으로 블록 요소(block element)임 → 사용 가능한 **가로 폭을 모두 차지**하고, 앞뒤에 **줄바꿈**이 발생함.
```html
<div style="background-color:#FFF4A3;">
  <h2>London</h2>
  <p>London is the capital city of England.</p>
  <p>London has over 9 million inhabitants.</p>
</div>
<div style="background-color:#FFC0C7;">
  <h2>Oslo</h2>
  ...
</div>
```
- 여러 요소(`<h2>`, `<p>` 등)를 하나의 `<div>`로 묶으면 **그룹 단위로 배경색·여백 등 스타일을 한 번에 적용**할 수 있음.
- 위 예시처럼 도시별로 div를 나누면 각 블록이 세로로 쌓이며 시각적으로 구분됨.
- `<div>` 자체는 의미가 없는 순수 구획용 태그임. 의미가 명확한 영역이라면 `<section>`, `<article>`, `<header>` 같은 **Semantic 태그**를 쓰는 것이 더 좋음.
#### HTML Links - `<a>`
`<a>` 태그는 **하이퍼링크**를 정의함. **`href`**** 속성**으로 링크의 목적지 URL을 지정함.
html
```html
<a href="https://www.w3schools.com/">Visit W3Schools.com!</a>
```
#### target 속성 — 링크된 문서가 열리는 공간 지정
<table header-row="true">
<tr>
<td>값</td>
<td>동작</td>
</tr>
<tr>
<td>**_self**</td>
<td>**기본값**. 클릭한 것과 같은 창/탭에서 열림</td>
</tr>
<tr>
<td>**_blank**</td>
<td>**새 창 또는 새 탭**에서 열림</td>
</tr>
<tr>
<td>_parent</td>
<td>부모 프레임에서 열림</td>
</tr>
<tr>
<td>_top</td>
<td>창의 전체 영역(full body)에서 열림</td>
</tr>
</table>
```html
<a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a>
```
#### Link Bookmarks (내부 링크)
페이지가 매우 길 때 **문서 내 특정 위치로 점프**시킬 때 유용함.
```html
<a href="#C4">Jump to Chapter 4</a>
...
<h2 id="C4">Chapter 4</h2>
```
- 이동할 목적지 요소에 `id`를 부여하고, 링크의 `href`에 `#id이름`을 적는 방식임.
#### HTML Text Formatting
특별한 형태의 텍스트를 표시하기 위해 설계된 **서식(Formatting) 요소들**임.
<table header-row="true">
<tr>
<td>태그</td>
<td>역할</td>
<td>표시 결과</td>
</tr>
<tr>
<td>`<b>`</td>
<td>단순히 **굵게** (의미 없음)</td>
<td>**This text is bold**</td>
</tr>
<tr>
<td>`<strong>`</td>
<td>**중요한** 텍스트 (의미 있음)</td>
<td>**This text is important!**</td>
</tr>
<tr>
<td>`<i>`</td>
<td>단순히 *기울임* (의미 없음)</td>
<td>*This text is italic*</td>
</tr>
<tr>
<td>`<em>`</td>
<td>**강조된** 텍스트 (의미 있음)</td>
<td>*This text is emphasized*</td>
</tr>
<tr>
<td>`<small>`</td>
<td>작은 글씨</td>
<td>This is some smaller text.</td>
</tr>
<tr>
<td>`<mark>`</td>
<td>형광펜 강조</td>
<td>buy `milk` today (노란 배경)</td>
</tr>
<tr>
<td>`<del>`</td>
<td>삭제된 텍스트</td>
<td>~~blue~~</td>
</tr>
<tr>
<td>`<ins>`</td>
<td>삽입된 텍스트</td>
<td>밑줄 표시</td>
</tr>
<tr>
<td>`<sub>`</td>
<td>아래첨자(subscript)</td>
<td>H₂O 형태</td>
</tr>
<tr>
<td>`<sup>`</td>
<td>위첨자(superscript)</td>
<td>x² 형태</td>
</tr>
</table>
#### 핵심 구분
- **`<b>`**** vs ****`<strong>`**, `<i>` vs `<em>`은 겉보기는 같지만, 앞은 **시각적 표현만**이고 뒤는 **의미(중요성·강조)를 담음**.
- 검색엔진·스크린리더는 의미 태그(`<strong>`, `<em>`)를 인식하므로 SEO·접근성 측면에서 이쪽이 권장됨.
#### HTML Lists - Unordered Lists `<ul>` / `<li>`
**순서 없는 목록**은 `<ul>` 태그로 시작하고, 각 항목은 `<li>` 태그로 작성함.
```html
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
#### list-style-type — 마커(불릿) 모양 지정
CSS의 **`list-style-type`** 속성으로 항목 마커 스타일을 정의함.
<table header-row="true">
<tr>
<td>값</td>
<td>마커 모양</td>
</tr>
<tr>
<td>**disc**</td>
<td>● 검은 원 (기본값)</td>
</tr>
<tr>
<td>**circle**</td>
<td>○ 빈 원</td>
</tr>
<tr>
<td>**square**</td>
<td>■ 사각형</td>
</tr>
<tr>
<td>**none**</td>
<td>마커 없음</td>
</tr>
</table>
```html
<ul style="list-style-type:square;">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
- `none`은 마커를 없애 목록 구조는 유지하면서 디자인만 깔끔하게 만들 때 자주 쓰임(내비게이션 메뉴 등).
#### HTML Lists - Ordered Lists `<ol>` / `<li>`
**순서 있는 목록**은 `<ol>` 태그로 시작하고, 각 항목은 `<li>` 태그로 작성함.
#### type 속성 — 항목 마커 종류 지정
`<ol>`의 **`type`**** 속성**으로 번호 표기 방식을 정함.
<table header-row="true">
<tr>
<td>type</td>
<td>마커</td>
<td>표시 예</td>
</tr>
<tr>
<td>**"1"**</td>
<td>숫자 (기본값)</td>
<td>1. 2. 3.</td>
</tr>
<tr>
<td>**"A"**</td>
<td>대문자 알파벳</td>
<td>A. B. C.</td>
</tr>
<tr>
<td>**"a"**</td>
<td>소문자 알파벳</td>
<td>a. b. c.</td>
</tr>
<tr>
<td>**"I"**</td>
<td>대문자 로마 숫자</td>
<td>I. II. III.</td>
</tr>
<tr>
<td>**"i"**</td>
<td>소문자 로마 숫자</td>
<td>i. ii. iii.</td>
</tr>
</table>
```html
<ol type="A">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```
- `<ul>`은 **순서가 중요하지 않은** 항목 나열, `<ol>`은 **순서·단계가 의미를 갖는** 항목(절차, 순위 등)에 사용함.
#### HTML Lists - Nested Lists (중첩 목록)
목록은 **다른 목록 안에 중첩**될 수 있음 (list inside list).
html
```html
<ol>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea</li>
    </ul>
  </li>
  <li>Milk</li>
</ol>
```
- 중첩할 하위 목록(`<ul>`/`<ol>`)은 **부모 ****`<li>`**** 안쪽에** 넣어야 함. `<li>`의 종료 태그는 하위 목록이 끝난 뒤에 닫힘.
- `<ol>` 안에 `<ul>`을 넣는 것처럼 **서로 다른 종류의 목록도 섞어서 중첩**할 수 있음.
- 렌더링 시 하위 목록은 자동으로 **들여쓰기**되어 계층 구조가 시각적으로 드러남.
#### HTML Lists - Description Lists `<dl>` / `<dt>` / `<dd>`
**용어와 그 설명**을 짝지어 나열하는 정의 목록임.
<table header-row="true">
<tr>
<td>태그</td>
<td>역할</td>
</tr>
<tr>
<td>**`<dl>`**</td>
<td>정의 리스트 **전체를 감싸는** 태그</td>
</tr>
<tr>
<td>**`<dt>`**</td>
<td>목록 항목의 **제목** (용어·항목 이름)</td>
</tr>
<tr>
<td>**`<dd>`**</td>
<td>`<dt>`에서 정의된 항목의 **상세 설명**</td>
</tr>
</table>
```html
<dl>
  <dt>HTML</dt>
  <dd>Hypertext Markup Language, 웹 페이지를 만드는 데 사용되는 마크업 언어입니다.</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets, 웹 페이지의 스타일을 정의하는 언어입니다.</dd>
  <dt>JavaScript</dt>
  <dd>웹 페이지의 동적인 기능을 구현하는 프로그래밍 언어입니다.</dd>
</dl>
```
- 렌더링 시 `<dt>`는 왼쪽에, `<dd>`는 **들여쓰기되어** 아래에 표시됨.
- 용어사전, FAQ, 메타데이터(제목–값 쌍)처럼 **"이름 : 설명" 구조**의 콘텐츠에 적합함.
#### HTML Tables
HTML의 표는 행(row)과 열(column) 안의 셀(cell)들로 구성됨.
#### 구성 태그
<table header-row="true">
<tr>
<td>태그</td>
<td>역할</td>
</tr>
<tr>
<td>**`<table>`**</td>
<td>표 전체를 감싸는 태그</td>
</tr>
<tr>
<td>**`<thead>`**</td>
<td>표의 **머리글(제목 행)**. `<tr>`과 `<th>`로 구성</td>
</tr>
<tr>
<td>**`<tbody>`**</td>
<td>실제 **데이터 행**을 담는 부분. `<tr>`과 `<td>`로 구성</td>
</tr>
<tr>
<td>**`<tfoot>`**</td>
<td>표의 **바닥글**. 합계·요약 정보에 사용</td>
</tr>
<tr>
<td>**`<tr>`**</td>
<td>표의 한 **행(Row)**</td>
</tr>
<tr>
<td>**`<th>`**</td>
<td>**머리글 셀**(Header cell). 기본적으로 굵은 글씨 + 가운데 정렬</td>
</tr>
<tr>
<td>**`<td>`**</td>
<td>**일반 데이터 셀**(Data cell)</td>
</tr>
</table>
```html
<table style="width:100%">
  <tr>
    <td>Emil</td>
    <td>Tobias</td>
    <td>Linus</td>
  </tr>
  <tr>
    <td>16</td>
    <td>14</td>
    <td>10</td>
  </tr>
</table>
```
- 표의 구조는 **`<table>`**** → ****`<tr>`****(행) → ****`<th>`****/****`<td>`****(셀)** 순으로 중첩됨.
- 한 `<tr>` 안에 들어간 셀 개수가 그 행의 **열 수**를 결정함.
#### HTML Tables - `<thead>` / `<tbody>` / `<tfoot>`
- 단순 예제나 소규모 표에서는 `<tr>`, `<th>`, `<td>`만으로도 사용 가능함.
- 다만 **접근성, 유지보수, 스타일링, 상호작용 구현** 측면에서는 반드시 `<thead>`, `<tbody>`, `<tfoot>`을 구분해서 사용해야 함.
```html
<table>
  <thead>
    <tr>
      <th>이름</th>
      <th>나이</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>홍길동</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
```
#### 구분해서 쓰는 이유
- **접근성**: 스크린리더가 머리글 행과 데이터 행을 구분해 읽어줌
- **유지보수**: 표의 구조가 명확해져 코드 파악이 쉬움
- **스타일링**: `thead th { ... }`처럼 영역별 CSS 선택이 편함
- **상호작용**: 정렬·스크롤 고정(헤더 고정) 같은 기능 구현 시 기준이 됨
#### HTML Tables - Styling
표의 모양은 **HTML 속성이 아닌 CSS로 지정하는 것이 권장**됨.
<table header-row="true">
<tr>
<td>주요 항목</td>
<td>HTML 속성 (지양)</td>
<td>CSS (권장)</td>
</tr>
<tr>
<td>테두리</td>
<td>`border`</td>
<td>**border, border-collapse**</td>
</tr>
<tr>
<td>셀 간격</td>
<td>`cellspacing`</td>
<td>**border-spacing**</td>
</tr>
<tr>
<td>셀 안쪽 여백</td>
<td>`cellpadding`</td>
<td>**padding**</td>
</tr>
<tr>
<td>정렬</td>
<td>`align`</td>
<td>**margin, text-align**</td>
</tr>
<tr>
<td>배경색</td>
<td>`bgcolor`</td>
<td>**background-color**</td>
</tr>
</table>
#### Zebra Striped Table 예시
```html
<style>
  table { border-collapse: collapse; width: 100%; }
  th, td { text-align: left; padding: 8px; }
  tr:nth-child(even) { background-color: #D6EEEE; }
</style>
```
- **`border-collapse: collapse`**: 셀 사이의 이중 테두리를 하나로 합침
- **`tr:nth-child(even)`**: 짝수 번째 행만 선택해 배경색을 줌 → **줄무늬(zebra) 효과**로 가독성 향상
#### HTML에서 Emoji 활용
Emoji는 이미지가 아니라 \*\*UTF-8(유니코드) 문자셋의 문자(character)\*\*임.
- **이모지(Emoji)**: 감정·사물·개념 등을 나타내는 그림문자
- **유니코드**(국제 문자 인코딩 표준의 일부)로 관리됨
- 일반 텍스트처럼 전송되며 \*\*유니코드 코드포인트(`U+1F600` 형식)\*\*로 표현됨
#### Emoji 역사
<table header-row="true">
<tr>
<td>연도</td>
<td>내용</td>
</tr>
<tr>
<td>1999년</td>
<td>일본 통신사 NTT 도코모가 세계 최초로 휴대폰용 이모지 도입 (176개)</td>
</tr>
<tr>
<td>2010년</td>
<td>유니코드 6.0에 처음으로 722개 이모지가 공식 포함</td>
</tr>
<tr>
<td>2016년</td>
<td>성별(남성/여성/성중립), 직업 관련 이모지 추가</td>
</tr>
<tr>
<td>2025년</td>
<td>3,800개 이상 등록, 매년 유니코드에서 새 이모지 승인</td>
</tr>
</table>
#### HTML에서 사용하기
Emoji는 문자이므로 **그냥 복사·붙여넣기**하면 다른 문자처럼 사용 가능함.
```html
<meta charset="UTF-8">
<body>
  <h1>Sized Emojis</h1>
  <p style="font-size:48px">&#128512; &#128516; &#128525; &#128151;</p>
</body>
```
- **`<meta charset="UTF-8">`** 선언이 있어야 이모지가 깨지지 않고 표시됨.
- 문자이므로 CSS **`font-size`****로 크기 조절**이 가능하고, `color`·`font-family` 등 텍스트 속성이 그대로 적용됨.
- `&#128512;` 처럼 **10진수 유니코드 참조(numeric character reference)** 방식으로도 삽입할 수 있음.
- 같은 코드포인트라도 **플랫폼(Apple/Google/Microsoft/Samsung)마다 렌더링 모양이 다름**.
---
## HTML Forms
HTML form은 **사용자 입력을 수집**하는 데 사용되며, 수집된 입력은 대부분 **서버로 전송되어 처리**됨.
- `<form>` 요소로 사용자 입력용 폼을 생성함.
- `<form>`은 텍스트 필드, 체크박스, 라디오 버튼, 제출 버튼 등 **여러 입력 요소를 담는 컨테이너**임.
```plain text
<form>
  form elements
</form>
```
#### 기본 예시
```html
<form action="signUpResult.php" method="get">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```
#### 주요 속성
<table header-row="true">
<tr>
<td>속성</td>
<td>역할</td>
</tr>
<tr>
<td>**action**</td>
<td>입력 데이터를 보낼 **서버 측 처리 URL**</td>
</tr>
<tr>
<td>**method**</td>
<td>전송 방식 (**get** / **post**)</td>
</tr>
<tr>
<td>**name**</td>
<td>각 입력값이 서버로 전달될 때의 **키 이름**</td>
</tr>
<tr>
<td>**value**</td>
<td>입력 필드의 초기값(기본값)</td>
</tr>
</table>
- `<label>`의 **`for`**** 속성**은 `<input>`의 `id`와 짝을 이룸. 라벨 클릭 시 해당 입력 필드가 선택되어 접근성이 좋아짐.
- `<input type="submit">`을 누르면 폼 데이터가 `action`에 지정된 주소로 전송됨.
#### HTML Form 정리 (속성 · 요소 · Input)
Form 관련 태그와 속성을 하나의 표로 정리함.
<table header-row="true">
<tr>
<td>구분</td>
<td>이름</td>
<td>설명</td>
</tr>
<tr>
<td>**form 속성**</td>
<td>action</td>
<td>폼 제출 시 데이터를 **보낼 위치(URL)**</td>
</tr>
<tr>
<td></td>
<td>method</td>
<td>전송에 사용할 **HTTP 메서드** (get / post)</td>
</tr>
<tr>
<td></td>
<td>accept-charset</td>
<td>폼 제출에 사용할 문자 인코딩</td>
</tr>
<tr>
<td></td>
<td>autocomplete</td>
<td>폼의 자동완성 on/off</td>
</tr>
<tr>
<td></td>
<td>enctype</td>
<td>데이터 인코딩 방식 (`method="post"`일 때만)</td>
</tr>
<tr>
<td></td>
<td>name</td>
<td>폼의 이름</td>
</tr>
<tr>
<td></td>
<td>novalidate</td>
<td>제출 시 유효성 검사를 하지 않음</td>
</tr>
<tr>
<td></td>
<td>rel</td>
<td>연결된 리소스와 현재 문서의 관계</td>
</tr>
<tr>
<td></td>
<td>target</td>
<td>제출 후 응답을 표시할 위치</td>
</tr>
<tr>
<td>**form 요소**</td>
<td>`<input>`</td>
<td>다양한 형태의 입력을 받음 (type, name, value, placeholder, required)</td>
</tr>
<tr>
<td></td>
<td>`<label>`</td>
<td>입력 필드의 텍스트 설명 (`for`로 id와 연결)</td>
</tr>
<tr>
<td></td>
<td>`<textarea>`</td>
<td>여러 줄 텍스트 입력 (rows, cols, placeholder, name)</td>
</tr>
<tr>
<td></td>
<td>`<select>`</td>
<td>드롭다운 목록 (name, multiple, required)</td>
</tr>
<tr>
<td></td>
<td>`<option>`</td>
<td>select 안의 선택 항목 (value, selected)</td>
</tr>
<tr>
<td></td>
<td>`<button>`</td>
<td>클릭 가능한 버튼 (type: submit / reset / button)</td>
</tr>
<tr>
<td></td>
<td>`<fieldset>`</td>
<td>관련 입력 필드를 그룹화</td>
</tr>
<tr>
<td></td>
<td>`<legend>`</td>
<td>fieldset의 제목</td>
</tr>
<tr>
<td></td>
<td>`<datalist>`</td>
<td>input에 자동완성 옵션 제공 (option과 함께 사용)</td>
</tr>
<tr>
<td></td>
<td>`<output>`</td>
<td>계산 결과 등의 출력용 필드 (for, name)</td>
</tr>
<tr>
<td>**input type**</td>
<td>text</td>
<td>일반 텍스트 입력 필드</td>
</tr>
<tr>
<td></td>
<td>password</td>
<td>입력 내용을 숨기는 비밀번호 필드</td>
</tr>
<tr>
<td></td>
<td>email</td>
<td>이메일 입력 필드. **형식 검증 제공**</td>
</tr>
<tr>
<td></td>
<td>number</td>
<td>숫자 입력 필드 (min, max, step 사용 가능)</td>
</tr>
<tr>
<td></td>
<td>tel</td>
<td>전화번호 입력 필드 (형식 검증 없음)</td>
</tr>
<tr>
<td></td>
<td>url</td>
<td>URL 입력 필드. 형식 검증 제공</td>
</tr>
<tr>
<td></td>
<td>color</td>
<td>색상 선택기</td>
</tr>
<tr>
<td></td>
<td>date</td>
<td>날짜 선택 필드 (YYYY-MM-DD)</td>
</tr>
<tr>
<td></td>
<td>checkbox</td>
<td>체크박스. **여러 개 선택 가능**</td>
</tr>
<tr>
<td></td>
<td>radio</td>
<td>라디오 버튼. 같은 name 그룹에서 **하나만 선택**</td>
</tr>
<tr>
<td></td>
<td>file</td>
<td>파일 선택(업로드) 필드</td>
</tr>
<tr>
<td></td>
<td>hidden</td>
<td>숨겨진 필드. 미노출 데이터 전송용</td>
</tr>
<tr>
<td></td>
<td>range</td>
<td>슬라이더로 범위 값 선택</td>
</tr>
<tr>
<td>**input 속성**</td>
<td>value</td>
<td>입력 필드의 초기값</td>
</tr>
<tr>
<td></td>
<td>readonly</td>
<td>읽기 전용으로 지정</td>
</tr>
<tr>
<td></td>
<td>disabled</td>
<td>입력 필드 비활성화</td>
</tr>
<tr>
<td></td>
<td>size</td>
<td>입력 필드의 표시 너비(문자 수 기준)</td>
</tr>
<tr>
<td></td>
<td>maxlength</td>
<td>입력 가능한 최대 문자 수</td>
</tr>
<tr>
<td></td>
<td>min / max</td>
<td>입력 가능한 최솟값·최댓값</td>
</tr>
<tr>
<td></td>
<td>multiple</td>
<td>둘 이상의 값 입력 허용</td>
</tr>
<tr>
<td></td>
<td>pattern</td>
<td>제출 시 검사할 **정규표현식** 지정</td>
</tr>
<tr>
<td></td>
<td>placeholder</td>
<td>기대하는 입력값에 대한 짧은 힌트</td>
</tr>
<tr>
<td></td>
<td>required</td>
<td>제출 전 **반드시 입력**해야 함</td>
</tr>
<tr>
<td></td>
<td>step</td>
<td>허용되는 숫자 간격</td>
</tr>
<tr>
<td></td>
<td>autofocus</td>
<td>페이지 로드 시 자동으로 포커스</td>
</tr>
<tr>
<td></td>
<td>height / width</td>
<td>`<input type="image">`의 높이·너비</td>
</tr>
<tr>
<td></td>
<td>list</td>
<td>미리 정의된 옵션을 담은 `<datalist>` 참조</td>
</tr>
<tr>
<td></td>
<td>autocomplete</td>
<td>자동완성 on/off</td>
</tr>
</table>
- `checkbox`는 다중 선택, `radio`는 **같은 ****`name`****으로 묶인 그룹 안에서 단일 선택**이라는 점이 핵심 차이임.
- `required`, `pattern`, `min/max`는 서버로 보내기 전 **브라우저 단계에서 유효성 검사**를 수행함.
#### HTML Buttons
`<button>` 요소는 **클릭 가능한 버튼**을 정의함.
#### Button Types — `type` 속성
<table header-row="true">
<tr>
<td>type</td>
<td>동작</td>
</tr>
<tr>
<td>**button**</td>
<td>일반 클릭 버튼. 기본적으로 아무 동작도 하지 않음 (JS와 연결해 사용)</td>
</tr>
<tr>
<td>**submit**</td>
<td>폼을 **제출**함</td>
</tr>
<tr>
<td>**reset**</td>
<td>폼의 모든 필드를 **초기화**함</td>
</tr>
</table>
```html
<button type="button">클릭</button>
<button type="submit">제출</button>
<button type="reset">초기화</button>
```
#### Disabled Buttons — `disabled` 속성
**`disabled`** 속성을 사용하면 버튼을 **클릭할 수 없게** 만듦.
```html
<button type="button" disabled>클릭 불가</button>
```
- `<form>` 안에서 `<button>`의 type을 생략하면 브라우저 기본값이 **submit**이므로, 단순 클릭 버튼으로 쓸 때는 `type="button"`을 명시해야 의도치 않은 폼 제출을 막을 수 있음.
#### HTML Form 종합 예제 (회원가입 폼)
세 개의 `<fieldset>`으로 구성된 회원가입 폼 전체 코드임.
#### Example I — 계정 정보
```html
<form>
  <fieldset>
    <legend>계정 정보</legend>
    <p>
      <label for="userId">아이디: </label>
      <input type="text" id="userId" name="userId" minlength="4" maxlength="15" required placeholder="4~15자 영문/숫자">
      <small>(필수)</small>
    </p>
    <p>
      <label for="userPw">비밀번호: </label>
      <input type="password" id="userPw" name="userPw" minlength="8" required placeholder="8자 이상 입력">
      <small>(필수)</small>
    </p>
    <p>
      <label for="userEmail">이메일: </label>
      <input type="text" id="userEmail" name="userEmail" placeholder="example">
      @
      <select name="emailDomain">
        <option value="direct">직접 입력</option>
        <option value="naver.com">naver.com</option>
        <option value="gmail.com">gmail.com</option>
        <option value="daum.net">daum.net</option>
      </select>
    </p>
  </fieldset>
</form>
```
#### Example II — 개인 프로필 정보
```html
<form>
  <fieldset>
    <legend>개인 프로필 정보</legend>
    <p>
      <label for="userName">이름: </label>
      <input type="text" id="userName" name="userName" required>
    </p>
    <p>
      <label for="userBirth">생년월일: </label>
      <input type="date" id="userBirth" name="userBirth">
    </p>
    <p>
      성별:
      <label><input type="radio" name="gender" value="male" checked> 남성</label>
      <label><input type="radio" name="gender" value="female"> 여성</label>
      <label><input type="radio" name="gender" value="none"> 선택안함</label>
    </p>
    <p>
      관심 분야 (중복 선택 가능): <br>
      <label><input type="checkbox" name="interest" value="frontend"> 웹 프론트엔드 (Vue.js/HTML)</label><br>
      <label><input type="checkbox" name="interest" value="uiux"> UI/UX 디자인 표준</label><br>
      <label><input type="checkbox" name="interest" value="backend"> 백엔드 &amp; 데이터베이스</label><br>
      <label><input type="checkbox" name="interest" value="devops"> 클라우드 &amp; 인프라</label>
    </p>
  </fieldset>
</form>
```
#### Example III — 자기소개 + 제출
```html
<form>
  <fieldset>
    <legend>자기소개</legend>
    <p>
      <label for="intro">나를 표현하는 한 줄 소개 또는 가입 인사:</label><br>
      <textarea id="intro" name="intro" rows="5" cols="50" placeholder="여기에 내용을 입력하세요 (최대 200자)"></textarea>
    </p>
  </fieldset>
  <br>
  <input type="submit" value="동의하고 회원가입">
  <input type="reset" value="다시 작성">
</form>
```
---
## HTML 심화
#### Embedding Media — 이미지 · 오디오 · 비디오
웹 페이지에 미디어를 삽입하는 태그들임.
#### `<img>` — 이미지
**필수 속성 2가지**를 가짐.
<table header-row="true">
<tr>
<td>속성</td>
<td>역할</td>
</tr>
<tr>
<td>**src**</td>
<td>이미지 파일의 **경로** 지정</td>
</tr>
<tr>
<td>**alt**</td>
<td>이미지의 **대체 텍스트** (로딩 실패·스크린리더 대응)</td>
</tr>
</table>
```html
<img src="https://www.w3schools.com/images/w3schools_green.jpg"
     alt="W3Schools.com" style="width:104px;height:142px;">
```
- 크기 지정은 `width`, `height` 속성보다 **`style`**** 속성(CSS)으로 지정하는 것을 지향**함.
#### `<picture>` — 반응형 이미지
기기나 화면 크기에 따라 **다른 이미지를 표시**할 수 있게 함.
```html
<picture>
  <source media="(min-width: 650px)" srcset="img_food.jpg">
  <source media="(min-width: 465px)" srcset="img_car.jpg">
  <img src="img_girl.jpg">
</picture>
```
- 하나 이상의 `<source>` 요소를 포함하며, **`<img>`****를 항상 마지막 자식 요소로 반드시 지정**해야 함 (조건에 맞는 source가 없을 때의 기본값이자 fallback).
#### `<audio>` — 오디오
```html
<audio controls autoplay>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
```
<table header-row="true">
<tr>
<td>속성</td>
<td>역할</td>
</tr>
<tr>
<td>**controls**</td>
<td>play, pause, volume 등 기본 컨트롤 표시</td>
</tr>
<tr>
<td>**autoplay**</td>
<td>자동 재생 (브라우저에서 제한될 수 있음)</td>
</tr>
<tr>
<td>**loop**</td>
<td>반복 재생</td>
</tr>
<tr>
<td>**muted**</td>
<td>음소거</td>
</tr>
</table>
#### `<video>` — 비디오
```html
<video width="320" height="240" autoplay>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>
```
<table header-row="true">
<tr>
<td>속성</td>
<td>역할</td>
</tr>
<tr>
<td>**controls**</td>
<td>기본 컨트롤 표시</td>
</tr>
<tr>
<td>**autoplay**</td>
<td>자동 재생</td>
</tr>
<tr>
<td>**poster**</td>
<td>동영상 로딩 전 표시할 이미지</td>
</tr>
<tr>
<td>**width, height**</td>
<td>비디오 플레이어의 크기 지정</td>
</tr>
</table>
#### 공통 원리
- `<source>`는 **대체 미디어 파일 여러 개를 나열**하는 용도임. 브라우저는 **가장 먼저 인식 가능한 형식**을 사용함.
- `<audio>`·`<video>` 태그 **사이의 텍스트**는 해당 요소를 지원하지 않는 브라우저에서만 표시되는 fallback 문구임.
---
#### Semantic Layout Tags

레이아웃 영역을 **의미(역할)에 맞게 구분**하는 시맨틱 태그들임.
<table header-row="true">
<tr>
<td>태그</td>
<td>설명</td>
</tr>
<tr>
<td>**`<header>`**</td>
<td>헤더 영역을 구분</td>
</tr>
<tr>
<td>**`<nav>`**</td>
<td>내부의 다른 영역이나 외부를 연결하는 **링크 영역** 구분</td>
</tr>
<tr>
<td>**`<main>`**</td>
<td>문서의 **주요 콘텐츠**. 페이지의 핵심 내용 포함</td>
</tr>
<tr>
<td>**`<section>`**</td>
<td>**논리적으로 관련 있는** 내용 영역 구분</td>
</tr>
<tr>
<td>**`<article>`**</td>
<td>**독립적인** 영역 구분</td>
</tr>
<tr>
<td>**`<aside>`**</td>
<td>주력 내용이나 독립적 내용으로 보기 어려워 article·section으로 구분할 수 없을 때 사용 (사이드바 등)</td>
</tr>
<tr>
<td>**`<footer>`**</td>
<td>footer 영역 구분</td>
</tr>
<tr>
<td>**`<figure>`**</td>
<td>이미지·도표·코드 등 삽입된 콘텐츠를 감쌈 (`<figcaption>`과 함께 사용)</td>
</tr>
<tr>
<td>**`<figcaption>`**</td>
<td>`<figure>`에 대한 설명 제공</td>
</tr>
</table>
#### 핵심 구분
- **`<section>`**** vs ****`<article>`**: section은 **묶여 있는 관련 내용**, article은 **떼어내도 그 자체로 성립하는** 독립 콘텐츠(게시글, 뉴스 기사 등)임.
- `<div>` 대신 이들 태그를 쓰면 검색엔진·스크린리더가 문서 구조를 이해할 수 있어 **SEO와 접근성**에 유리함.
#### Web Accessibility (웹 접근성)
시각·청각·지체 장애를 가진 분들을 포함해 **어떤 사용자도 웹사이트 이용에서 소외되지 않도록** HTML 문서를 표준에 맞게 작성하는 기술임.
- 화면을 보지 못해 **스크린 리더**(소리로 읽어주는 프로그램)를 쓰는 사용자 등 모두에게 **동등한 사용자 경험**을 제공하는 것이 목적임.
#### 웹 접근성을 높이는 HTML 작성 규칙
<table header-row="true">
<tr>
<td>규칙</td>
<td>내용</td>
</tr>
<tr>
<td>**시맨틱 태그 사용**</td>
<td>`<header>`, `<nav>`, `<main>` 등을 쓰면 스크린 리더가 화면 구조를 정확히 파악할 수 있음</td>
</tr>
<tr>
<td>**Heading Elements 활용**</td>
<td>`<h1>~<h6>`으로 문서 구조와 섹션 간 관계를 명확히 표현</td>
</tr>
<tr>
<td>**`<img>`****의 alt 속성**</td>
<td>눈으로 볼 수 없는 사용자를 위해 "이 이미지가 어떤 내용인지" 말로 설명</td>
</tr>
<tr>
<td>**label과 input 연결**</td>
<td>텍스트와 입력창을 눈으로만 배치하지 말고 **코드로 연결**해야 함</td>
</tr>
</table>
```html
<label for="userId">아이디</label>
<input type="text" id="userId" name="userId">
```
- `<label>`의 `for`와 `<input>`의 `id`를 일치시켜야 스크린 리더가 입력창에 포커스됐을 때 **"어떤 내용을 적는 칸"인지 정확히 읽어줌**.
- 접근성을 위한 작업(시맨틱 태그, 명확한 제목 구조, alt)은 그대로 **SEO 향상**으로도 이어짐.
---
## CSS 개요
- CSS(Cascading Style Sheets)는 웹 페이지의 **스타일을 정의하는 스타일시트 언어**임.
- HTML 요소가 화면·인쇄물·기타 매체에서 어떻게 표시될지(how HTML elements are to be displayed)를 기술함.
#### CSS로 제어할 수 있는 것
- 색상, 글꼴, 텍스트 크기
- element 간격, element의 위치 및 레이아웃
- 배경 이미지 또는 배경색
- 다양한 장치 및 화면 크기에 따른 표시 방식(반응형)
#### 핵심 개념
- 하나의 HTML 페이지에 **서로 다른 스타일시트를 적용**하면 구조는 그대로 둔 채 완전히 다른 디자인을 만들 수 있음 (One HTML Page - Multiple Styles).
- 즉 **HTML = 구조·내용**, **CSS = 표현·디자인**으로 역할이 분리됨. 이 분리가 유지보수와 재사용성의 핵심임.
#### CSS Syntax
CSS 규칙(rule)은 선택자(selector)와 선언 블록(declaration block)으로 구성됨.
```plain text
h1 { color: blue; font-size: 12px; }
 ↑   └────── declaration ──────┘
selector      property: value
```
<table header-row="true">
<tr>
<td>구성 요소</td>
<td>역할</td>
</tr>
<tr>
<td>**selector**</td>
<td>스타일을 적용할 **HTML 요소를 지목**</td>
</tr>
<tr>
<td>**declaration block**</td>
<td>`{ }`로 감싸며, **세미콜론(;)으로 구분된** 하나 이상의 선언 포함</td>
</tr>
<tr>
<td>**declaration**</td>
<td>**property(속성명) : value(값)** 형태. 콜론(:)으로 구분</td>
</tr>
</table>
#### 작성 예시

```css
p {
  color: red;
  text-align: center;
}
```
- 위 규칙은 문서의 모든 `<p>` 요소에 **빨간 글자 + 가운데 정렬**을 적용함.
- 문법 요약: **선언은 세미콜론으로 구분**, **선언 블록은 중괄호로 감쌈**, **속성과 값은 콜론으로 연결**함.
---
### CSS How To — CSS 적용 3가지 방법
CSS를 HTML에 적용하는 방법은 **Inline / Internal / External** 세 가지임.
#### 1) Inline CSS
HTML 요소 내부의 **`style`**** 속성**에 직접 작성함.
```html
<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```
- 해당 요소 **하나에만** 적용됨. 선택자를 쓸 수 없어 재사용이 불가함.
#### 2) Internal CSS
같은 HTML 파일의 `<head>` 안에 **`<style>`**** 요소**를 넣어 작성함.
```html
<html>
<head>
  <style>
    body {background-color: linen;}
    h1 {color: maroon; margin-left: 40px;}
  </style>
</head>
<body>
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```
- 선택자를 사용할 수 있어 **그 문서 전체**에 규칙을 적용할 수 있음. 다만 다른 페이지와는 공유되지 않음.
#### 3) External CSS
별도의 `.css` 파일을 만들고 `<head>`에서 **`<link>`**** 요소**로 연결함.
```html
<html>
<head>
  <link rel="stylesheet" href="mystyle.css">
</head>
<body>
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```
```css
/* mystyle.css */
body {background-color: lightblue;}
h1 {color: navy; margin-left: 20px;}
```
- `rel="stylesheet"`로 관계를 명시하고, `href`에 CSS 파일 경로를 지정함.
#### 세 방식 비교
<table header-row="true">
<tr>
<td>방식</td>
<td>작성 위치</td>
<td>적용 범위</td>
<td>선택자 사용</td>
</tr>
<tr>
<td>**Inline**</td>
<td>태그의 `style` 속성</td>
<td>그 요소 하나</td>
<td>불가</td>
</tr>
<tr>
<td>**Internal**</td>
<td>`<head>` 안 `<style>`</td>
<td>그 HTML 문서 전체</td>
<td>가능</td>
</tr>
<tr>
<td>**External**</td>
<td>별도 `.css` 파일 + `<link>`</td>
<td>연결한 **모든 페이지**</td>
<td>가능</td>
</tr>
</table>
- 실무 기준은 **External CSS**임. 구조(HTML)와 표현(CSS)이 완전히 분리되어 유지보수·재사용에 가장 유리하고, CSS 파일이 캐싱되어 성능에도 이점이 있음.
---
#### CSS Selectors - Simple Selectors
CSS 선택자(selector)는 스타일을 적용할 **HTML 요소를 "찾는(select)"** 데 사용됨.
#### 기본 선택자 3가지
<table header-row="true">
<tr>
<td>선택자</td>
<td>표기</td>
<td>대상</td>
</tr>
<tr>
<td>**element**</td>
<td>`p { }`</td>
<td>해당 **태그명**을 가진 모든 요소</td>
</tr>
<tr>
<td>**id**</td>
<td>`#para1 { }`</td>
<td>`id="para1"`인 **요소 하나**</td>
</tr>
<tr>
<td>**class**</td>
<td>`.center { }`</td>
<td>`class="center"`인 **모든 요소**</td>
</tr>
</table>
```css
p {
  color: red;
  text-align: center;
}

#para1 {
  text-align: center;
  color: red;
}

.center {
  text-align: center;
  color: red;
}
```
- **`#`****은 id**, **`.`****은 class**, 기호 없이 이름만 쓰면 **태그(element)** 선택자임.
- id는 문서 내 유일해야 하므로 특정 요소 하나를 지목할 때, class는 여러 요소에 공통 스타일을 줄 때 사용함.
#### CSS Selectors - Universal & Grouping Selectors
#### 전체 선택자 (Universal Selector)
-  는 페이지의 **모든 HTML 요소**를 선택함.
```css
* {
  text-align: center;
  color: blue;
}
```
- 주로 초기화(reset) 용도로 사용됨 (예: `{ margin: 0; padding: 0; }`).
#### 그룹 선택자 (Grouping Selector)
**같은 스타일 정의를 공유하는** 여러 요소를 한 번에 선택함. 선택자를 **쉼표(,)로 나열**함.
```css
h1, h2, p {
  text-align: center;
  color: red;
}
```
- 위 코드는 아래 세 규칙을 따로 쓰는 것과 동일함. 중복을 줄여 코드가 간결해짐.
```css
h1 { text-align: center; color: red; }
h2 { text-align: center; color: red; }
p  { text-align: center; color: red; }
```
#### CSS Selectors - Attribute Selectors
**속성 선택자**는 특정 **속성** 또는 **속성값**(혹은 둘 다)을 가진 HTML 요소를 선택해 스타일링함.
<table header-row="true">
<tr>
<td>선택자</td>
<td>의미</td>
</tr>
<tr>
<td>`[attribute]`</td>
<td>해당 **속성을 가진** 요소</td>
</tr>
<tr>
<td>`[attribute="value"]`</td>
<td>속성값이 **정확히 일치**하는 요소</td>
</tr>
<tr>
<td>`[attribute~="value"]`</td>
<td>속성값에 해당 **단어를 포함**하는 요소 (공백 구분)</td>
</tr>
<tr>
<td>`[attribute|="value"]`</td>
<td>속성값이 해당 값과 정확히 같거나, **값 + 하이픈(-)으로 시작**하는 요소</td>
</tr>
<tr>
<td>`[attribute^="value"]`</td>
<td>속성값이 해당 값으로 **시작**하는 요소</td>
</tr>
<tr>
<td>`[attribute$="value"]`</td>
<td>속성값이 해당 값으로 **끝나는** 요소</td>
</tr>
<tr>
<td>`[attribute*="value"]`</td>
<td>속성값에 해당 값을 **포함**하는 요소</td>
</tr>
</table>
#### 사용 예시
```css
input[type="text"] {
  width: 150px;
  padding: 6px;
  margin-bottom: 10px;
  background-color: pink;
}

input[type="button"] {
  width: 100px;
  padding: 6px;
  background-color: lightgreen;
}
```
- 같은 `<input>` 태그라도 **type 값에 따라 다른 스타일**을 줄 수 있음.
- `^`(시작), `$`(끝), (포함)은 정규표현식과 같은 의미로 기억하면 됨. 예: `a[href^="https"]`는 https로 시작하는 링크만 선택함.
#### CSS Selectors - Combinator
CSS 선택자는 여러 개를 조합할 수 있으며, 선택자 사이에 결합자(combinator)를 넣어 더 구체적으로 선택함.
<table header-row="true">
<tr>
<td>결합자</td>
<td>기호</td>
<td>선택 대상</td>
</tr>
<tr>
<td>**Descendant** (후손)</td>
<td>공백</td>
<td>지정 요소의 **모든 후손** (자식, 손자 등 전부)</td>
</tr>
<tr>
<td>**Child** (자식)</td>
<td>`>`</td>
<td>지정 요소의 **직계 자식**만</td>
</tr>
<tr>
<td>**Next sibling** (인접 형제)</td>
<td>`+`</td>
<td>지정 요소 **바로 다음**에 오는 형제 하나</td>
</tr>
<tr>
<td>**Subsequent-sibling** (일반 형제)</td>
<td>`~`</td>
<td>지정 요소 **이후의 모든 형제**</td>
</tr>
</table>
#### 예시
```css
div p   { color: red; }   /* div 안의 모든 p (깊이 무관) */
div > p { color: blue; }  /* div의 직계 자식 p만 */
div + p { color: green; } /* div 바로 뒤의 p 하나(형제임. 자식 x) */
div ~ p { color: gray; }  /* div 이후의 모든 형제 p */
```
- **공백 vs ****`>`**: 후손 전체냐, 한 단계 아래 자식만이냐의 차이임.
- **`+`**** vs ****`~`**: 바로 다음 하나냐, 뒤따르는 전부냐의 차이임. 둘 다 **같은 부모를 가진 형제** 관계에서만 동작함.
---
#### CSS Selectors - Pseudo-classes
- 의사클래스(가상클래스)는 선택자에 붙여 요소의 특별한 상태(state)에 대한 스타일을 정의하는 키워드임.
#### Syntax
선택자 뒤에 콜론(:)을 붙여 사용함.
```css
selector:pseudo-class-name {
  CSS properties
}
```
#### 주요 활용 사례
- 마우스를 **올렸을 때**의 스타일 (hover)
- **방문한 링크와 방문하지 않은 링크**를 다르게 표시
- 요소가 **포커스를 받았을 때**의 스타일
- 폼 요소의 **valid / invalid / required / optional** 상태별 스타일
- 부모의 **첫 번째 자식**인 요소 스타일
#### Pseudo-class 분류
<table header-row="true">
<tr>
<td>분류</td>
<td>성격</td>
<td>예</td>
</tr>
<tr>
<td>**Interactive**</td>
<td>사용자 동작·상태에 반응</td>
<td>`:hover`, `:focus`, `:active`, `:visited`</td>
</tr>
<tr>
<td>**Structural**</td>
<td>문서 구조상의 위치로 선택</td>
<td>`:first-child`, `:last-child`, `:nth-child()`</td>
</tr>
</table>
- 의사클래스는 HTML에 별도 class를 추가하지 않고도 **상태나 위치에 따른 스타일**을 줄 수 있다는 점이 핵심임.
#### CSS Selectors - Pseudo-classes 종류
#### Interactive Pseudo-classes
**사용자와의 상호작용**에 따라 스타일을 적용함.
<table header-row="true">
<tr>
<td>의사클래스</td>
<td>상태</td>
</tr>
<tr>
<td>**`:link`**</td>
<td>방문한 적이 **없는** 링크 상태</td>
</tr>
<tr>
<td>**`:visited`**</td>
<td>사용자가 이미 **방문한(클릭한 적 있는)** 링크 상태</td>
</tr>
<tr>
<td>**`:hover`**</td>
<td>요소 위에 **마우스 커서가 올라가 있는** 상태</td>
</tr>
<tr>
<td>**`:active`**</td>
<td>요소를 마우스로 **클릭하고 있는(누르고 있는)** 상태</td>
</tr>
<tr>
<td>**`:focus`**</td>
<td>Tab 키나 클릭으로 요소(주로 input, button)가 선택되어 **초점이 맞춰진** 상태</td>
</tr>
</table>
- 링크에 적용할 때는 순서가 중요함: **`:link`**** → ****`:visited`**** → ****`:hover`**** → ****`:active`** 순으로 작성해야 의도대로 동작함.
#### Structural Pseudo-classes
**문서 트리에서의 위치**를 기준으로 요소를 선택함.
<table header-row="true">
<tr>
<td>의사클래스</td>
<td>선택 대상</td>
</tr>
<tr>
<td>**`:first-child`**</td>
<td>부모의 자식들 중 **첫 번째** 요소</td>
</tr>
<tr>
<td>**`:last-child`**</td>
<td>부모의 자식들 중 **마지막** 요소</td>
</tr>
<tr>
<td>**`:nth-child(n)`**</td>
<td>부모의 자식들 중 **n번째** 요소 (`:nth-child(2)`=2번째, `:nth-child(2n)`=짝수 번째)</td>
</tr>
<tr>
<td>**`:nth-last-child(n)`**</td>
<td>**끝에서부터** n번째 자식</td>
</tr>
<tr>
<td>**`:only-child`**</td>
<td>자식이 **하나뿐일 때** 그 요소</td>
</tr>
<tr>
<td>**`:first-of-type`**</td>
<td>같은 **타입(태그) 중 첫 번째** 요소</td>
</tr>
<tr>
<td>**`:last-of-type`**</td>
<td>같은 타입 중 **마지막** 요소</td>
</tr>
</table>
- **`child`**** vs ****`of-type`**: `child`는 **모든 형제 중 순서**를 세고, `of-type`은 **같은 태그끼리만** 순서를 셈.
- `:nth-child()`에는 숫자 외에 `2n`(짝수), `2n+1`(홀수), `even`, `odd` 같은 수식을 쓸 수 있음.
---
#### CSS Selectors - Pseudo-elements
- 의사요소(가상요소)는 선택자에 붙여 **요소의 특정 부분**에 스타일을 적용하는 키워드임.
#### Syntax
선택자 뒤에 더블콜론(::)을 붙여 사용함.
css
```css
selector::pseudo-element-name {
  CSS properties
}
```
- 의사**클래스**는 콜론 하나(`:`), 의사**요소**는 콜론 두 개(`::`)로 구분됨.
#### 주요 활용 사례
- 요소의 **첫 글자·첫 줄** 스타일링
- 요소의 **앞뒤에 콘텐츠 삽입**
- 리스트 항목의 **마커** 스타일링
- 사용자가 **선택(드래그)한 영역** 스타일링
- dialog 뒤의 viewbox 스타일링
#### Text Pseudo-elements
텍스트 콘텐츠의 **특정 부분**을 스타일링함.
<table header-row="true">
<tr>
<td>의사요소</td>
<td>대상</td>
</tr>
<tr>
<td>**`::first-line`**</td>
<td>텍스트 블록의 **첫 번째 줄**만 선택. 브라우저 창 너비에 따라 줄바꿈이 바뀌면 첫 줄 범위도 **자동 갱신**됨</td>
</tr>
<tr>
<td>**`::first-letter`**</td>
<td>텍스트 블록의 **첫 번째 글자**만 선택</td>
</tr>
<tr>
<td>**`::selection`**</td>
<td>사용자가 마우스로 **드래그해 선택한 영역**</td>
</tr>
</table>
#### Content Pseudo-elements
**생성된 콘텐츠를 삽입**하거나 스타일링함. 삽입할 내용은 **`content`**** 속성**으로 지정함.
<table header-row="true">
<tr>
<td>의사요소</td>
<td>위치</td>
</tr>
<tr>
<td>**`::before`**</td>
<td>선택한 요소의 \*\*가장 앞쪽(내부 시작점)\*\*에 가상 콘텐츠 생성</td>
</tr>
<tr>
<td>**`::after`**</td>
<td>선택한 요소의 \*\*가장 뒤쪽(내부 끝점)\*\*에 가상 콘텐츠 생성</td>
</tr>
</table>
```css
p::before { content: "▶ "; }
p::after  { content: " (끝)"; }
```
- `::before`/`::after`는 **`content`**** 속성이 없으면 렌더링되지 않음**. 내용이 없어도 `content: "";`를 반드시 써야 함.
- 실제 DOM에 요소를 추가하지 않고 시각적 장식(아이콘, 구분선 등)을 넣을 때 자주 사용됨.
#### CSS Selectors - Selector 조합 예
여러 선택자를 결합해 대상을 정밀하게 지정할 수 있음.
<table header-row="true">
<tr>
<td>조합 예시</td>
<td>의미</td>
</tr>
<tr>
<td>`p.notice`</td>
<td>class가 `notice`인 **p 요소**</td>
</tr>
<tr>
<td>`div#header`</td>
<td>id가 `header`인 **div 요소**</td>
</tr>
<tr>
<td>`button.btn.primary`</td>
<td>class가 `btn`이면서 **동시에** `primary`인 button</td>
</tr>
<tr>
<td>`input[type="text"][required]`</td>
<td>type이 `"text"`이고 `required` 속성도 가진 input</td>
</tr>
<tr>
<td>`ul li:first-child:hover`</td>
<td>ul 내 **첫 번째 li**에 마우스를 올렸을 때</td>
</tr>
<tr>
<td>`*:hover`</td>
<td>마우스를 올린 **모든** 요소</td>
</tr>
<tr>
<td>`section.news > article.featured h2.title + p.summary`</td>
<td>`.news` section의 **직계 자식** `.featured` article의 **후손** 중 `.title` h2 **바로 다음**에 오는 `.summary` p</td>
</tr>
</table>
css
```css
p.notice {font-size: 18px;}
div#header {background: gray;}
button.btn.primary {background-color: blue;}
input[type="text"][required] {border: 1px solid red;}
ul li:first-child:hover {color: red;}
*:hover {background-color: yellow;}
section.news > article.featured h2.title + p.summary {font-style: italic;}
```
#### 조합 규칙 정리
- **공백 없이 붙여 쓰면** 같은 요소에 대한 **AND 조건**임 (`button.btn.primary` = btn이면서 primary).
- **공백을 넣으면** 후손 관계로 해석됨 (`ul li` = ul 안의 li).
- 의사클래스도 **연속으로 붙여** 조건을 누적할 수 있음 (`:first-child:hover`).
- 긴 조합은 **왼쪽에서 오른쪽으로** 관계를 따라 읽으면 됨. 마지막에 오는 선택자가 **실제 스타일이 적용되는 대상**임.
#### CSS Specificity (우선순위 / 명시도)
**Specificity**는 어떤 스타일 선언이 최종적으로 요소에 적용될지 결정하는 알고리즘임. 둘 이상의 규칙이 같은 요소를 가리키면 **명시도가 가장 높은 선언이 이김(win)**.
#### Specificity Hierarchy — 선택자별 가중치(weight)
<table header-row="true">
<tr>
<td>순위</td>
<td>Selector</td>
<td>Example</td>
<td>Weight</td>
</tr>
<tr>
<td>1순위</td>
<td>**Inline styles**</td>
<td>`<h1 style="color: pink;">`</td>
<td>**1-0-0-0**</td>
</tr>
<tr>
<td>2순위</td>
<td>**Id selectors**</td>
<td>`#navbar`</td>
<td>**0-1-0-0**</td>
</tr>
<tr>
<td>3순위</td>
<td>**Classes, 속성 선택자, 의사클래스**</td>
<td>`.test`, `[type="text"]`, `:hover`</td>
<td>**0-0-1-0**</td>
</tr>
<tr>
<td>4순위</td>
<td>**Elements, 의사요소**</td>
<td>`h1`, `::before`, `::after`</td>
<td>**0-0-0-1**</td>
</tr>
<tr>
<td>—</td>
<td>**Universal selector, ****`:where()`**</td>
<td>`*`, `:where()`</td>
<td>**0-0-0-0** (우선순위 없음)</td>
</tr>
</table>
#### Specificity 작동 원칙
- **자릿수가 높으면 무조건 승리** — `[0,0,1,0]`(클래스 1개)이 `[0,0,0,15]`(태그 15개)보다 우선함. 아래 자릿수를 아무리 쌓아도 상위 자릿수를 이길 수 없음.
- **점수가 같으면 나중에 작성된 코드가 승리** — 합산 점수가 완전히 동일하면 CSS 파일에서 **가장 아래에 있는 규칙**이 이전 규칙을 덮어씀 (**Cascading 원칙**).
- **전체 선택자()는 점수가 0점** — 항상 우선순위에서 밀림.
#### 적용 예제
**① class vs element**
```html
<style>
  .test {color: green;}   /* 0-0-1-0 */
  p {color: red;}         /* 0-0-0-1 */
</style>
<p class="test">Hello World!</p>
```
→ **green** 적용
**② id 추가**
```html
<style>
  #demo {color: blue;}    /* 0-1-0-0 */
  .test {color: green;}   /* 0-0-1-0 */
  p {color: red;}         /* 0-0-0-1 */
</style>
<p id="demo" class="test">Hello World!</p>
```
→ **blue** 적용
**③ inline style 추가**
```html
<p id="demo" class="test" style="color: pink;">Hello World!</p>
```
→ **pink** 적용 (1-0-0-0으로 최상위)
- `!important`를 붙이면 이 모든 명시도를 무시하고 우선 적용되지만, 이후 수정이 어려워지므로 남용은 피해야 함.
---
### CSS Colors
CSS에서 색상은 **미리 정의된 색상 이름** 또는 **RGB, HEX, HSL, RGBA, HSLA 값**으로 지정함.
#### 지정 방식
<table header-row="true">
<tr>
<td>방식</td>
<td>표기 예</td>
<td>설명</td>
</tr>
<tr>
<td>**Color name**</td>
<td>`Tomato`, `Orange`, `DodgerBlue`, `MediumSeaGreen`, `Gray`, `SlateBlue`, `Violet`, `LightGray`</td>
<td>미리 정의된 색상 이름</td>
</tr>
<tr>
<td>**RGB**</td>
<td>`rgb(255, 99, 71)`</td>
<td>Red, Green, Blue 각 0\~255</td>
</tr>
<tr>
<td>**HEX**</td>
<td>`#ff6347`</td>
<td>16진수 색상 코드</td>
</tr>
<tr>
<td>**HSL**</td>
<td>`hsl(9, 100%, 64%)`</td>
<td>Hue(색상), Saturation(채도), Lightness(명도)</td>
</tr>
</table>
- 위 세 값 `rgb(255,99,71)`, `#ff6347`, `hsl(9,100%,64%)`은 모두 \*\*동일한 색(Tomato)\*\*임.
- **RGBA / HSLA**는 뒤에 **alpha(투명도)** 값을 추가한 형태임 (예: `rgba(255,99,71,0.5)`).
#### CSS Units
CSS 단위는 여러 속성의 **길이와 크기**를 정의하는 데 사용됨. `font-size`, `width`, `margin`, `padding`, `border` 등이 length 값을 받음.
#### Absolute Units (절대 단위)
- **px (pixels)** — 화면에서 가장 많이 쓰이는 절대 단위
#### Relative Units (상대 단위)
<table header-row="true">
<tr>
<td>단위</td>
<td>기준</td>
</tr>
<tr>
<td>**em**</td>
<td>**부모 요소의 폰트 크기** (1em = 부모의 font-size)</td>
</tr>
<tr>
<td>**rem**</td>
<td>부모와 관계없이 **최상위 Root HTML 요소**의 폰트 크기 (Root em)</td>
</tr>
<tr>
<td>**%**</td>
<td>부모 요소의 해당 속성 크기를 100%로 두고 계산한 상대 비율</td>
</tr>
<tr>
<td>**vw** (Viewport Width)</td>
<td>브라우저 화면 **전체 너비의 1%** (100vw = 화면 전체 너비)</td>
</tr>
<tr>
<td>**vh** (Viewport Height)</td>
<td>브라우저 화면 **전체 높이의 1%** (100vh = 화면 전체 높이)</td>
</tr>
</table>
css
```css
body {font-size: 16px;}      /* Base font size */
h1 {font-size: 2.5em;}       /* 2.5 * 16 = 40px */
h2 {font-size: 1.875em;}     /* 1.875 * 16 = 30px */
p {font-size: 1rem;}         /* 1 * 16 = 16px */
```
- **Viewport** = 브라우저 창 크기임. 뷰포트 너비가 500px이면 1vw = 5px임.
- **em vs rem**: em은 부모를 따라가므로 중첩되면 크기가 누적되어 계산이 꼬일 수 있음. rem은 항상 루트 기준이라 예측 가능해 실무에서 선호됨.
---
#### CSS Fonts
#### Font Family — `font-family`
```css
.p1 {font-family: "Times New Roman", Times, serif;}
```
- 브라우저가 첫 번째 폰트를 지원하지 않으면 **다음 폰트를 순서대로 시도**함. 폰트 이름은 **쉼표로 구분**함.
- 마지막에는 `serif`, `sans-serif` 같은 \*\*일반 계열(generic family)\*\*을 넣어 최후의 대체를 보장함.
#### Font Style — `font-style`, `font-weight`, `font-variant`
```css
p.italic {font-style: italic;}          /* 기울임 */
p.thick {font-weight: bold;}            /* 굵기 */
p.small {font-variant: small-caps;}     /* 작은 대문자 */
```
#### Font Size — `font-size`
```css
body {font-size: 16px;}      /* Base font size */
h1 {font-size: 2.5em;}       /* 2.5 * 16 = 40px */
h2 {font-size: 1.875rem;}    /* 1.875 * 16 = 30px */
p {font-size: 5vw;}          /* 화면 너비의 5% */
```
- `vw`를 font-size에 쓰면 화면 크기에 따라 글자가 유동적으로 커지고 작아짐(반응형 타이포그래피).
#### CSS Fonts - Google Fonts
Google Fonts는 **무료**로 사용할 수 있으며 **1000종 이상**의 폰트를 제공함.
#### 사용 방법
`<head>`에서 `<link>`로 폰트를 불러온 뒤, CSS의 `font-family`에 지정함.
```html
<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">
  <style>
    body {
      font-family: "Sofia", sans-serif;
    }
  </style>
</head>
```
#### 여러 폰트 동시 사용
URL의 `family=` 뒤에 폰트명을 **파이프(****`|`****)로 구분**해 나열함.
```html
<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide|Sofia|Trirong">
  <style>
    h1.a {font-family: "Audiowide", sans-serif;}
    h1.b {font-family: "Sofia", sans-serif;}
    h1.c {font-family: "Trirong", serif;}
  </style>
</head>
```
#### 폰트 효과 적용 — `effect=effectname`
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia&effect=fire">
```
#### 한국어 폰트 사용 절차
1. Google Fonts 공식 사이트 접속 (`https://fonts.google.com/`)
2. **Language 필터에서 Korean(한국어)** 선택 후 상세 페이지로 이동
3. 상세 페이지에서 **Get font** → 장바구니에서 **Get embed code** 확인
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dongle&display=swap" rel="stylesheet">
```
```css
.dongle-regular {
  font-family: "Dongle", sans-serif;
  font-weight: 400;
  font-style: normal;
}
```
- 웹 임베드 방식은 `<link>`와 **`@import`** 두 가지를 제공하며, 상세 페이지에서 굵기(Light 300, Regular 400, Bold 700 등)를 **필요한 것만 선택**해 불러오는 것이 로딩 성능에 유리함.
- `display=swap`은 폰트 로딩 전까지 대체 폰트로 먼저 텍스트를 보여줘 화면이 비는 현상을 막아줌.
---
#### CSS 텍스트 스타일링 (CSS Text Styling)
텍스트 자체의 **색·정렬·형태·간격·그림자**를 제어하는 속성군임. 글꼴(font-\*) 속성과는 별개로, 이미 렌더링된 텍스트의 배치와 장식을 다룸.
<table header-row="true">
<tr>
<td>분류</td>
<td>속성</td>
<td>값 예시</td>
<td>의미</td>
</tr>
<tr>
<td>색상</td>
<td>`color`</td>
<td>`blue`, `#00ff00`, `rgb(255,0,0)`</td>
<td>글자색. **키워드 / HEX / RGB 세 가지 표기 모두 가능**</td>
</tr>
<tr>
<td>정렬</td>
<td>`text-align`</td>
<td>`center`, `left`, `right`</td>
<td>블록 요소 안에서 인라인 콘텐츠의 **가로 정렬**</td>
</tr>
<tr>
<td>변형</td>
<td>`text-transform`</td>
<td>`uppercase`, `lowercase`, `capitalize`</td>
<td>원본 HTML은 그대로 두고 **표시만** 대/소문자 변환. `capitalize`는 각 단어 첫 글자만 대문자</td>
</tr>
<tr>
<td>장식</td>
<td>`text-decoration-line`</td>
<td>`underline`, `overline`, `line-through`</td>
<td>선의 **위치**</td>
</tr>
<tr>
<td></td>
<td>`text-decoration-color`</td>
<td>`red`, `green`</td>
<td>선의 **색** (글자색과 별도 지정 가능)</td>
</tr>
<tr>
<td></td>
<td>`text-decoration-style`</td>
<td>`solid`, `double`, `dotted`, `wavy`</td>
<td>선의 **모양**</td>
</tr>
<tr>
<td></td>
<td>`text-decoration-thickness`</td>
<td>`15px`, `25%`</td>
<td>선의 **두께**. px 절대값 또는 폰트 크기 대비 %</td>
</tr>
<tr>
<td>간격</td>
<td>`text-indent`</td>
<td>`50px`</td>
<td>문단 **첫 줄** 들여쓰기</td>
</tr>
<tr>
<td></td>
<td>`letter-spacing`</td>
<td>`1px`</td>
<td>글자 사이 간격</td>
</tr>
<tr>
<td></td>
<td>`word-spacing`</td>
<td>`5px`</td>
<td>단어 사이 간격</td>
</tr>
<tr>
<td></td>
<td>`line-height`</td>
<td>`1.5`</td>
<td>줄 간격. **단위 없는 배수 지정 권장**(폰트 크기에 비례)</td>
</tr>
<tr>
<td></td>
<td>`white-space`</td>
<td>`nowrap`, `pre`, `normal`</td>
<td>공백·줄바꿈 처리 방식. `nowrap`은 **자동 줄바꿈 금지**</td>
</tr>
<tr>
<td>그림자</td>
<td>`text-shadow`</td>
<td>`0 0 3px #ff0000, 0 0 5px #0000ff`</td>
<td>`x축 y축 흐림반경 색` 순서. **쉼표로 여러 겹 중첩 가능**</td>
</tr>
</table>
#### 유의점
- `text-decoration-*` 4종은 `text-decoration: underline red dotted 2px;` 형태의 **단축 속성**으로 한 줄에 쓸 수 있음.
- `text-transform`은 시각적 변환일 뿐이라 **복사하면 원본 텍스트 그대로** 나옴.
---
#### CSS 배경 (CSS Backgrounds)
요소의 **배경 영역**을 색·이미지로 채우는 속성군임. 배경은 콘텐츠 박스가 아니라 기본적으로 **패딩 영역까지 포함**해 칠해짐.
<table header-row="true">
<tr>
<td>분류</td>
<td>속성</td>
<td>값 예시</td>
<td>의미</td>
</tr>
<tr>
<td>색</td>
<td>`background-color`</td>
<td>`lightblue`</td>
<td>배경색</td>
</tr>
<tr>
<td></td>
<td>`opacity`</td>
<td>`0.3`</td>
<td>요소 **전체**의 불투명도(0\~1)</td>
</tr>
<tr>
<td>이미지</td>
<td>`background-image`</td>
<td>`url("paper.gif")`</td>
<td>배경 이미지 지정. **경로는 ****`url()`****로 감쌈**</td>
</tr>
<tr>
<td>반복</td>
<td>`background-repeat`</td>
<td>`no-repeat`, `repeat-x`, `repeat-y`</td>
<td>기본값은 **가로·세로 모두 반복(****`repeat`****)**</td>
</tr>
<tr>
<td>위치</td>
<td>`background-position`</td>
<td>`right top`, `center`, `50% 50%`</td>
<td>`가로 세로` 순서로 시작 위치 지정</td>
</tr>
<tr>
<td>고정</td>
<td>`background-attachment`</td>
<td>`scroll`, `fixed`</td>
<td>`scroll`은 콘텐츠와 **함께 스크롤**, `fixed`는 화면에 **고정**되어 패럴랙스 효과 연출</td>
</tr>
</table>
#### 유의점
- 슬라이드 표기 `background-attatchement`는 **오타**임. 실제 속성명은 `background-attachment`.
- `opacity`는 배경뿐 아니라 **자식 요소·텍스트까지 함께 투명해짐.** 배경만 반투명하게 하려면 `background-color: rgba(173,216,230,0.3);`처럼 **rgba/hsla를 쓰는 것이 정석**임.
- 여러 background 속성은 `background: url("img.png") no-repeat right top;`처럼 **단축 속성**으로 묶을 수 있음.
---
#### CSS 박스 모델 (CSS Box Model)
모든 HTML 요소는 **하나의 사각형 박스로 감싸져** 렌더링됨. 이 박스는 안쪽부터 **Content → Padding → Border → Margin** 4개 층으로 구성됨.
<table header-row="true">
<tr>
<td>영역</td>
<td>역할</td>
<td>위치</td>
</tr>
<tr>
<td>**Content**</td>
<td>요소의 실제 내용(텍스트·이미지)이 들어가는 영역</td>
<td>가장 안쪽</td>
</tr>
<tr>
<td>**Padding**</td>
<td>콘텐츠와 경계(border) 사이의 안쪽 여백</td>
<td>Content 바깥</td>
</tr>
<tr>
<td>**Border**</td>
<td>요소의 경계선</td>
<td>Padding 바깥</td>
</tr>
<tr>
<td>**Margin**</td>
<td>해당 요소와 **다른 요소** 사이의 바깥 여백</td>
<td>가장 바깥</td>
</tr>
</table>
#### 확인 방법
- 브라우저 **개발자도구 → Elements → Computed** 패널에서 각 층의 실제 픽셀값을 시각적으로 확인 가능함.
- 그림에서 안쪽부터 `61.328×19`(content) → `padding 1` → `border 2` → `margin 0` 순으로 값이 표시됨. **레이아웃이 어긋날 때 어느 층 때문인지 특정하는 데 가장 빠른 수단임.**
---
#### 박스 모델 – 너비와 높이 (Width / Height)
<table header-row="true">
<tr>
<td>속성</td>
<td>예시</td>
<td>설명</td>
</tr>
<tr>
<td>`width` / `height`</td>
<td>`div {height: 200px; width: 50%;}`</td>
<td>**Content 영역만의** 크기. padding·border·margin은 **포함하지 않음**</td>
</tr>
<tr>
<td>기본값 `auto`</td>
<td>—</td>
<td>브라우저가 콘텐츠와 부모 크기를 보고 자동 계산</td>
</tr>
<tr>
<td>`min-width` / `max-width`</td>
<td>`.div1 {max-width: 500px;}`</td>
<td>너비의 하한/상한</td>
</tr>
<tr>
<td>`min-height` / `max-height`</td>
<td>—</td>
<td>높이의 하한/상한</td>
</tr>
</table>
#### width vs max-width
<table header-row="true">
<tr>
<td>지정</td>
<td>창이 500px보다 좁아질 때</td>
<td>결과</td>
</tr>
<tr>
<td>`width: 500px`</td>
<td>500px를 그대로 유지</td>
<td>**가로 스크롤바 발생**</td>
</tr>
<tr>
<td>`max-width: 500px`</td>
<td>창 너비에 맞춰 줄어듦</td>
<td>**스크롤바 없이 자연스럽게 축소**</td>
</tr>
</table>
- 반응형 레이아웃에서는 **고정 ****`width`****보다 ****`max-width`****가 기본 선택지**임.
---
#### 박스 모델 – 마진 (Margins)
<table header-row="true">
<tr>
<td>구분</td>
<td>속성 / 예시</td>
<td>설명</td>
</tr>
<tr>
<td>개별 지정</td>
<td>`margin-top`, `margin-right`, `margin-bottom`, `margin-left`</td>
<td>방향별로 따로 지정</td>
</tr>
<tr>
<td>단축 속성</td>
<td>`p {margin: 25px 50px 75px 100px;}`</td>
<td>**시계방향으로 top → right → bottom → left** 순서</td>
</tr>
</table>
#### 마진 병합 (Margin Collapse)
- **세로 방향 마진**끼리 만나면 두 값이 더해지지 않고, **둘 중 더 큰 값 하나로 합쳐지는** 현상임.
- 예시: `h1 {margin-bottom: 50px;}` + `h2 {margin-top: 20px;}` → 실제 간격은 70px이 아니라 **50px**.
- **좌우(가로) 마진은 병합되지 않음.** 가로는 그대로 합산됨.
---
#### 박스 모델 – 패딩 (Padding)
<table header-row="true">
<tr>
<td>구분</td>
<td>속성 / 예시</td>
<td>설명</td>
</tr>
<tr>
<td>개별 지정</td>
<td>`padding-top`, `padding-right`, `padding-bottom`, `padding-left`</td>
<td>방향별로 따로 지정</td>
</tr>
<tr>
<td>단축 속성</td>
<td>`div {padding: 25px 50px 75px 100px;}`</td>
<td>**top → right → bottom → left** 순서 (margin과 동일)</td>
</tr>
</table>
#### width와 padding의 관계
- `width`는 **content 영역만의 너비**이므로, padding을 주면 요소의 실제 차지 너비는 그만큼 **더 커짐**.
- 예시: `div {width: 300px; padding: 25px;}` → 총 너비 = **300 + 25×2 = 350px**.
- 여기에 border까지 있으면 **border 두께 ×2도 추가로 더해짐.** 총 너비 = content + padding + border.
- 이 계산이 번거로우면 `box-sizing: border-box;`를 쓰면 **padding·border를 width 안에 포함**시켜 지정한 값이 곧 최종 너비가 됨.
---
#### CSS 배치 (CSS Position)
`position` 속성은 요소의 **배치 유형**을 지정함. 값에 따라 `top`/`right`/`bottom`/`left`의 **기준점**과 **문서 흐름 유지 여부**가 달라짐.
<table header-row="true">
<tr>
<td>값</td>
<td>기준점</td>
<td>문서 흐름</td>
<td>원래 공간</td>
<td>예시</td>
</tr>
<tr>
<td>`static`</td>
<td>없음 (기본값)</td>
<td>일반 흐름대로 배치</td>
<td>차지</td>
<td>`div.static {position: static;}` — **top/left 등이 적용되지 않음**</td>
</tr>
<tr>
<td>`relative`</td>
<td>**자기 자신의 원래 위치**</td>
<td>유지</td>
<td>**차지함**</td>
<td>`div.relative {position: relative; left: 30px;}`</td>
</tr>
<tr>
<td>`fixed`</td>
<td>**뷰포트(브라우저 창)**</td>
<td>제거</td>
<td>차지 안 함</td>
<td>`div.fixed {position: fixed; bottom: 0; right: 0;}` — **스크롤해도 고정**</td>
</tr>
<tr>
<td>`absolute`</td>
<td>**가장 가까운 조상 요소**</td>
<td>제거</td>
<td>차지 안 함</td>
<td>`div.absolute {position: absolute; top: 80px; right: 0;}`</td>
</tr>
<tr>
<td>`sticky`</td>
<td>스크롤 위치에 따라 전환</td>
<td>조건부</td>
<td>차지</td>
<td>`div.sticky {position: sticky; top: 0;}` — **relative ↔ fixed 자동 전환**</td>
</tr>
</table>
#### 핵심 구분
- **공간 차지 여부**가 가장 큰 갈림길임. `relative`는 원래 자리를 비워둔 채 시각적으로만 이동하지만, `absolute`·`fixed`는 **흐름에서 완전히 빠져 다른 요소가 그 자리를 채움.**
- `absolute`의 기준이 되는 "가장 가까운 조상"은 정확히는 **position이 static이 아닌 가장 가까운 조상**임. 없으면 문서 전체(초기 컨테이닝 블록)가 기준이 됨. 그래서 부모에 `position: relative;`를 걸어두고 자식을 `absolute`로 배치하는 조합이 관용적으로 쓰임.
- `sticky`는 지정한 임계선(`top: 0` 등)에 닿기 전까지는 `relative`처럼 흐르다가, 닿는 순간 `fixed`처럼 붙음. **헤더·사이드 메뉴·테이블 헤더 고정**에 주로 사용됨.
---
#### CSS 중첩 순서 (CSS Z-index)
`z-index` 속성은 동일 위치에 **겹쳐진(overlap) 요소들의 앞뒤 순서**를 지정함. 값은 **양수·음수 모두 가능**하며, 값이 클수록 앞으로 나옴.
<table header-row="true">
<tr>
<td>상황</td>
<td>결과</td>
</tr>
<tr>
<td>`z-index` 값이 큼</td>
<td>더 **앞쪽**(사용자 쪽)에 표시</td>
</tr>
<tr>
<td>`z-index: -1`</td>
<td>일반 콘텐츠보다 **뒤쪽**으로 밀려 배경처럼 깔림</td>
</tr>
<tr>
<td>`z-index` 미지정</td>
<td>HTML 문서상 **나중에 나온 요소가 위**에 표시</td>
</tr>
</table>
#### 예제 해석
```plain text
img {position: absolute; left: 0px; top: 0px; z-index: -1;}
```
- `position: absolute`로 이미지를 좌상단에 고정한 뒤, `z-index: -1`을 주어 **h1 제목과 p 문단 뒤로 보냄. → 배경 이미지로 쓴다는 뜻**
- 결과 이미지에서 나무 그림 위로 "This is a heading" 텍스트가 겹쳐 보이는 것이 그 효과임.
- **`z-index`****는 ****`position`****이 ****`static`****이 아닌 요소에만 적용됨.** 즉 `relative`/`absolute`/`fixed`/`sticky`가 함께 지정되어야 동작함. 위 예제에서 `position: absolute;`가 반드시 필요한 이유임.
---
#### CSS 상속 (CSS Inheritance)
**부모 요소에 지정된 스타일 중 일부가 자식 요소로 자동 적용되는 것**을 상속이라 함. HTML이 **계층적 트리 구조**이기 때문에 가능한 동작임.
#### 상속되는 속성
<table header-row="true">
<tr>
<td>분류</td>
<td>속성</td>
</tr>
<tr>
<td>텍스트</td>
<td>`color`, `text-align`, `text-indent`, `letter-spacing`, `word-spacing`, `line-height`, `visibility`, `white-space`</td>
</tr>
<tr>
<td>폰트</td>
<td>`font`, `font-family`, `font-size`, `font-style`, `font-variant`, `font-weight`</td>
</tr>
<tr>
<td>리스트</td>
<td>`list-style`, `list-style-type`, `list-style-position`, `list-style-image`</td>
</tr>
<tr>
<td>테이블</td>
<td>`border-collapse`, `border-spacing`, `caption-side`, `empty-cells`</td>
</tr>
</table>
#### 상속되지 않는 속성
<table header-row="true">
<tr>
<td>분류</td>
<td>속성</td>
</tr>
<tr>
<td>레이아웃</td>
<td>`margin`, `padding`, `border`, `width`, `height`, `display`, `position`</td>
</tr>
<tr>
<td>배경</td>
<td>`background-color`, `background-image`</td>
</tr>
<tr>
<td>박스 정렬</td>
<td>`flex`, `grid`, `justify-content`, `align-items`</td>
</tr>
<tr>
<td>기타</td>
<td>`box-shadow`, `z-index`, `overflow`</td>
</tr>
</table>
#### 구분 기준
- **글자의 생김새를 결정하는 속성은 상속되고, 박스의 크기·위치를 결정하는 속성은 상속되지 않음.** 만약 margin이나 border가 상속된다면 모든 자식 요소에 여백과 테두리가 중복 적용되어 레이아웃이 무너지기 때문임.
- 그래서 `body`에 `font-family`와 `color`를 한 번만 지정해 문서 전체 서체를 통일하는 방식이 관용적으로 쓰임.
---
#### 강제 상속 – inherit 키워드
`inherit` 키워드를 값으로 지정하면 **원래 상속되지 않는 속성도 부모의 값을 강제로 물려받게** 할 수 있음.
```javascript
.card {
  color: dimgray; /* 부모인 .card의 글자 색상은 dimgray */
}

.card a {
  color: inherit; /* .card 안에 있는 <a> 태그의 색상을 부모(.card)와 똑같이 맞춤 */
}
```
<table header-row="true">
<tr>
<td>요소</td>
<td>결과</td>
</tr>
<tr>
<td>`.card`</td>
<td>부모의 글자 색상은 `dimgray`</td>
</tr>
<tr>
<td>`.card`의 `<a>`</td>
<td>`inherit`으로 인해 **부모와 동일한 색상이 됨**</td>
</tr>
</table>
```plain text
p { border: 1px solid red; }
strong { border: inherit; }
```
<table header-row="true">
<tr>
<td>요소</td>
<td>결과</td>
</tr>
<tr>
<td>`<p>`</td>
<td>빨간색 1px 실선 테두리</td>
</tr>
<tr>
<td>`<strong>` (p의 자식)</td>
<td>`inherit`으로 인해 **부모와 동일한 1px solid red 테두리가 그려짐**</td>
</tr>
</table>
- `border`는 원래 비상속 속성이므로, `inherit`이 없었다면 `<strong>`에는 테두리가 생기지 않음.
- 상속 관련 키워드로는 `inherit` 외에 `initial`(속성의 CSS 기본값으로 되돌림), `unset`(상속 속성이면 상속, 비상속 속성이면 initial)도 함께 쓰임.
---
<empty-block/>
