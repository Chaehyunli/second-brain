---
title: "[8/10] Java, SpringBoot, Rest API 구현_Day1_핵심 정리"
notion_page_id: "3b71d84b-f68e-804e-8f70-ebd72787efe4"
source_url: "https://app.notion.com/p/3b71d84bf68e804e8f70ebd72787efe4"
synced_at: "2026-08-11T00:09:41+09:00"
content_sha256: "f6422d2f806b2f2a930702679162bf94b982322e90792cd463d7de66b17c7d8f"
tags: [notion, skala, learning, java, spring-boot, rest-api]
---

# [8/10] Java, SpringBoot, Rest API 구현_Day1_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b71d84bf68e804e8f70ebd72787efe4) (2026-08-11 확인)

### IP와 Port
네트워크 환경에서 프로세스 간 통신을 식별하려면 IP와 Port를 함께 사용함.
- IP 주소: 인터넷에서 특정 컴퓨터(Host)를 식별하는 논리적 주소. 유선/무선 네트워크 장비를 거쳐 각 호스트에 할당됨.
- Port: 동일한 IP를 가진 Host 안에서 실행 중인 특정 서비스/프로세스를 구분하는 번호.
둘을 합쳐 `IP:Port` 형태로 표현하며, 예를 들어 `http://168.126.63.42:8080`은 IP `168.126.63.42`의 호스트에서 포트 `8080`으로 열린 프로세스에 접근함을 의미함.
---
### Localhost vs 127.0.0.1
동일 Host 안에서 프로세스끼리 통신할 때 사용하는 특수 주소임.
- `localhost`: 로컬 호스트를 가리키는 도메인 이름
- `127.0.0.1`: 루프백(loopback) IP 주소. 두 표현은 동일한 대상을 가리킴.
예를 들어 로컬 PC(IP: 168.126.63.42)에서 포트 8080으로 실행 중인 Python 프로세스가 포트 9090의 Java 프로세스에 요청을 보낼 때, `http://localhost:9090` 또는 `http://127.0.0.1:9090`을 사용함. 외부 IP(`168.126.63.42:9090`)로 접근하지 않아도 됨.
로컬 도메인 정보는 운영체제의 hosts 파일에서 관리함.
```plain text
cat /etc/hosts
127.0.0.1    localhost
```
현재 머신의 IP 확인 명령어:
```plain text
ipconfig getifaddr en0   # 무선 (Wi-Fi)
ipconfig getifaddr en1   # 유선 (Ethernet)
```
---
### Process와 Port
프로세스는 현재 메모리에 로드되어 CPU를 할당받고 실행 중인 프로그램임. 동일 OS 위에서 여러 프로세스가 동시에 실행될 수 있으며, 각 프로세스는 고유한 포트 번호를 점유함.
실행 예시:
```plain text
python webserver.py
npm run dev
java -jar ./target/ideoperators-0.0.1-SNAPSHOT.jar
```
하나의 OS 위에서 여러 프로세스(nginx, python, java 등)가 각각 다른 포트(8888, 5555, 8080)를 점유하는 구조임.
프로세스 간 통신 방식은 위치에 따라 구분됨:
| 구분 | 방법 | 예시 |
| --- | --- | --- |
| 외부 프로세스 간 통신 | IP + Port | `172.8.32.9:8080` |
| 내부 프로세스 간 통신 | 127.0.0.1 + Port | `127.0.0.1:8080`, `localhost:8080` |
---
### Process vs Thread
프로세스와 스레드는 모두 실행의 단위이지만, 메모리 구조와 통신 방식에서 차이가 있음.

| 항목 | 프로세스 (Process) | 스레드 (Thread) |
| --- | --- | --- |
| 정의 | 실행 중인 프로그램의 인스턴스 | 프로세스 내에서 실행되는 작업 단위 |
| 메모리 공간 | 독립적인 메모리 공간 사용 | 프로세스의 메모리 공간을 공유 |
| 생성 비용 | 상대적으로 크고 무거움 | 생성 비용이 낮고 가벼움 |
| 통신 방법 | IPC(파이프, 소켓 등) 필요 | 공유 메모리를 통해 간단하게 통신 가능 |
| 충돌 영향 | 다른 프로세스에 영향 없음 | 다른 스레드에 영향을 줄 수 있음 |
| 예시 | 웹 브라우저, 게임, IDE 등 | 웹 페이지 렌더링, 백그라운드 다운로드 등 |
각 프로세스는 코드, 힙(메모리), 기타 영역을 독립적으로 보유하며, 내부에 하나 이상의 스레드를 가질 수 있음. 스레드는 프로세스의 코드·힙을 공유하되, 각자 독립된 스택을 가짐.
---
### Public IP와 Private IP

IP 주소는 사용 범위에 따라 Public IP와 Private IP로 구분됨.
- Private IP: 특정 사설 네트워크(Private Network) 안에서만 유일한 식별자. 외부 인터넷에서는 직접 접근 불가. 라우터가 내부 고유 번호 리스트를 관리함.
	- 예: `192.168.0.142`, `192.168.0.143`
- Public IP: 인터넷 전체에서 유일한 주소. 외부와의 통신 시 사용되며, 라우터가 대표 Public IP 하나로 외부와 통신함.
	- 예: `145.12.14.8`
일반 가정·사무실 환경의 기기들은 대부분 Private IP를 사용하며, 외부 인터넷과 통신할 때는 라우터의 Public IP를 통해 나가는 구조(NAT)임.
---
### Gateway, Router, Load Balancer
네트워크 구성 요소를 역할 기준으로 구분하면 다음과 같음.
Router — 연결
- 네트워크를 연결하고 확장하며, 패킷이 목적지까지 가는 경로(길)를 결정함.
- 인터넷 자체가 수많은 Router들의 집합체로 볼 수 있음.
- OSI 모델 Layer 3(네트워크 계층)에서 동작함.
Load Balancer — 분배
- 들어오는 요청 트래픽을 여러 노드(서버)에 분배/분산하는 역할.
- Layer 4(전송 계층, TCP/UDP 기반 분배)와 Layer 7(애플리케이션 계층, HTTP 기반 분배) 모두에서 동작함.
- NLB(Network Load Balancer): Layer 4 기반 / ALB(Application Load Balancer): Layer 7 기반.
Gateway — 관문
- 서비스/애플리케이션으로 진입하는 단일 진입점 역할을 함.
- 주요 기능:
	- 프로토콜 변환
	- 외부 IP를 내부 IP로 변환
	- JWT 인증, Filter, CORS, Header 변경 처리
	- Layer 7 Routing (Service Routing)
	- Service Load Balancer 기능 (선택적)
실무에서 API Gateway는 Router·Load Balancer 기능을 일부 포함하는 복합 컴포넌트로 동작하는 경우가 많음.
---
### 프론트 엔드 (Front-end)
사용자가 실제로 눈으로 보고 손으로 조작하는 웹 화면을 만드는 영역임. UI(인터페이스)와 UX(사용 경험)를 설계하고 구현하는 일을 담당함.
프론트 엔드의 역할:
| 역할 | 설명 |
| --- | --- |
| 구조 만들기 (HTML) | 웹페이지의 뼈대 — 제목, 단락, 버튼, 이미지 위치 등 |
| 꾸미기 (CSS) | 색깔, 글꼴, 여백, 애니메이션 등 디자인 요소 |
| 동작 넣기 (JavaScript) | 클릭, 입력, 드래그 등 사용자 행동에 반응하도록 기능 추가 |
| 데이터 불러오기 (API 연동) | 백엔드 서버에 데이터를 요청하고 받은 정보를 화면에 노출 |
| 사용자 경험 개선 (UX) | 더 편리하고 빠르게 사용할 수 있도록 화면 흐름과 반응을 최적화 |
자주 쓰는 기술:
| 구분 | 예시 |
| --- | --- |
| 기본 언어 | HTML, CSS, JavaScript |
| 프레임워크/라이브러리 | React, Vue.js |
| 패키지 관리자 | npm, yarn |
| 빌드 도구 | Webpack, Vite |
"End"는 종단·경계지점·맞닿는 지점(Endpoint)을 의미함. 프론트 엔드는 사용자와 맞닿는 끝단이라는 뜻임.
---
### 백 엔드 (Back-end)
웹서비스의 보이지 않는 뒷단에서 모든 기능이 제대로 작동하도록 만드는 영역임. 프론트 엔드의 요청을 받아 데이터를 처리하고 결과를 돌려주는 역할을 함.
백 엔드의 역할:
| 역할 | 설명 |
| --- | --- |
| 서버 운영 | 사용자의 요청을 받는 서버를 관리하고 실행 |
| DB 연동, 데이터 처리 | 사용자가 입력한 정보를 계산·검증·분석하고 필요한 처리를 수행 |
| API 제공 | 프론트엔드가 데이터를 주고받을 수 있도록 API를 만들어 제공 |
| 보안 및 권한 관리 | 로그인, 암호화, 접근 제한 등 사용자 정보 보호 기능을 담당 |
| 성능 관리 및 로깅 | 서버가 빠르고 안정적으로 동작하도록 최적화하고 오류를 기록 |
자주 쓰는 기술:
| 구분 | 예시 |
| --- | --- |
| 프로그래밍 언어 | Java, Python, JavaScript(Node.js), Go, Kotlin |
| 프레임워크 | Spring Boot, Django, Express, FastAPI |
| 데이터베이스 | MySQL, PostgreSQL, MongoDB, Redis |
| API 형식 | REST API, GraphQL |
| 서버/배포 환경 | AWS, Docker, Nginx, GitHub Actions |
---
### 현대적 Frontend / Backend 구조

#### JSON Format
JSON(JavaScript Object Notation)은 데이터를 키-값 쌍 형식으로 표현하는 경량 데이터 교환 형식임. 언어에 구애받지 않아 대부분의 프로그래밍 언어에서 사용 가능하며, 사람이 읽기 쉽고 기계가 처리하기도 간단함. 주로 API 응답, 데이터 교환에 사용됨.
기본 구조:
- 객체(Object): `{}`로 묶이고 키-값 쌍으로 구성
- 배열(Array): `[]`로 묶이고 값들의 리스트를 포함
- 값(Value): 문자열, 숫자, 객체, 배열, `true`, `false`, `null` 지원
```json
{
  "name": "John Doe",
  "age": 30,
  "isMarried": false,
  "children": ["Anna", "Ben"],
  "address": {
    "city": "Seoul",
    "zipCode": "12345"
  }
}
```
---
#### YAML Format
YAML(YAML Ain't Markup Language)은 사람이 읽기 쉽도록 설계된 데이터 직렬화 형식임. JSON보다 간결하고 가독성이 높으며, 주로 구성 파일(config)에서 많이 사용됨.
기본 구조:
- 키-값 쌍: `:`으로 구분
- 리스트: 로 시작
- 계층 구조: 들여쓰기로 표현
- 주석: `#`으로 작성
```yaml
name: John Doe
age: 30
isMarried: false
children:
  - Anna
  - Ben
address:
  city: Seoul
  zipCode: "12345"
```
---
#### JSON vs YAML
| 특징 | JSON | YAML |
| --- | --- | --- |
| 형식 | `{}`와 `[]`를 사용한 구조적 표현 | 들여쓰기 기반의 구조적 표현 |
| 가독성 | 읽을 수 있으나 형식이 딱딱함 | 사람이 읽기 매우 쉬움 |
| 주석 지원 | 지원하지 않음 | `#`으로 주석 작성 가능 |
| 사용 사례 | API 응답, 데이터 교환, 브라우저 내 데이터 처리 | 구성 파일, 설정 파일 |
| 파싱 속도 | 빠름 | JSON보다 느릴 수 있음 |
| 유연성 | 고정된 형식 | 더 유연하며 덜 엄격함 |
---
#### 동기와 비동기 (Sync vs Async) — 개념
동기(Synchronous)는 요청을 보낸 뒤 응답이 올 때까지 기다리는 방식임. Request-response model로, Sender가 요청을 보내고 Receiver의 응답을 받은 뒤에야 다음 작업으로 넘어감.
비동기(Asynchronous)는 요청을 보낸 뒤 기다리지 않고 다음 작업을 이어 수행하는 방식임. Fire and forget model로, Sender가 Queue에 메시지를 넣으면 Receiver가 준비됐을 때 처리함. 두 요청을 동시에 던진 뒤 응답은 나중에 각각 받을 수 있음.
---
#### 동기와 비동기 (Sync vs Async) — 비교
| 구분 | 동기식 (Synchronous) | 비동기식 (Asynchronous) |
| --- | --- | --- |
| 처리 방식 | 요청 → 응답까지 기다림 | 요청 → 기다리지 않고 다음 작업 수행, 결과는 나중에 수신 |
| 흐름 제어 | 직렬적(Blocking) 처리 | 병렬적(Non-blocking) 처리 |
| 응답 시간 | 요청 수 많을수록 느려짐 | 병렬 처리 가능하여 시스템 응답성 향상 가능 |
| 구현 복잡도 | 단순함 (순차적 코드 흐름) | 복잡함 (콜백 지옥, 상태 관리 필요) |
| 신뢰성 | 높은 일관성 (순서대로 처리됨) | 처리 순서 불확실성 (재시도, 실패 감지 필요) |
| 리소스 사용 | 자원 점유 시간 길어짐 | 자원 효율적으로 사용 가능 |
| 사용 적합 상황 | 트랜잭션이 중요한 금융/결제 시스템 등 | 대규모 사용자 이벤트 처리, 알림, 대기열 기반 작업 등 |
| 예시 | 함수 호출 후 리턴값 기다림, HTTP 요청/응답 | 이벤트 리스너, 콜백, Promise, 메시지 큐 |
---
#### 좋은 소프트웨어란?
소프트웨어 품질을 판단하는 네 가지 관점:
| 관점 | 정의 |
| --- | --- |
| 응집도 (Cohesion) | 하나의 모듈/서비스가 하나의 역할/책임에 집중하는 정도. 높을수록 변경·이해·재사용이 쉬움. |
| 복잡도 (Complexity) | 업무 로직, 아키텍처의 복잡도. 낮을수록 유지보수와 확장이 용이함. |
| 단독 실행 (Standalone Execution) | 시스템의 일부를 독립적으로 실행하거나 테스트할 수 있는 능력. 높을수록 분산 개발/배포/장애 복구에 유리함. |
| 결합도 (Coupling) | 구성 요소 간 의존성. 낮을수록(Loosely-Coupled) 변경/확장이 쉽고, 높으면(Tightly-Coupled) 전체 시스템에 영향을 줌. |
---
#### 소프트웨어 아키텍처 비교 — Monolith vs MSA
| 기준 | Monolith | MSA (Microservice Architecture) |
| --- | --- | --- |
| 응집도 | 역할과 책임의 혼재 (응집도 낮음) | 기능별 책임 분리 (응집도 높음) |
| 복잡도 | 로직 복잡도 높음, 아키텍처 복잡도 낮음 | 로직 복잡도 낮음, 아키텍처 복잡도 높음 |
| 단독 실행 | 개별 실행이 어려움, 테스트 복잡도 증가 | 개별 실행 용이, 테스트 복잡도 낮음 |
| 결합도 | 높음(Tightly-Coupled) → 하나 변경 시 전체 영향 | 낮음(Loosely-Coupled) → 독립적 배포·확장 가능 |
Monolith가 하나의 프로그램이니 응집도가 더 높지 않냐는 의문이 생길 수 있음. 하지만 응집도는 전체 프로그램 단위가 아니라, 하나의 모듈이 얼마나 일관된 책임을 가지고 있는가의 측면에서 판단함. Monolith는 하나의 프로세스 안에 주문·결제·상품 서비스가 뒤섞이므로 모듈별 응집도가 낮아짐.
---
#### Monolith (덩어리)
Monolith에서 실행 단위(프로세스 = WAS)는 개발·배포·운영의 단위이기도 함. 주문(Order), 결제(paymt), 상품(product) 서비스가 하나의 WAS 프로세스 안에 함께 묶여 JVM 위에서 실행됨. 코드 묶음 단위는 class/bean이며, 배포 단위는 War/Jar 파일임.
나쁜 소프트웨어로 분류되는 이유:
- 내부는 낮은 응집도
- 내부는 높은 복잡도
- 개발/배포 단위가 War/Jar, 실행 단위가 WAS로 분리됨
- 서비스 간 긴밀한 결합
여기서 "나쁘다"는 잘못되었다는 의미가 아니라, 개발/운영 관점에서 관리하기 어렵다는 의미로 이해해야 함.
---
#### 마이크로 서비스 (알갱이)
마이크로 서비스(MSA)에서는 서비스마다 독립적인 프로세스(실행 단위)를 가짐. 주문(Order), 결제(paymt), 상품(product) 각각이 별도 JVM 위에서 별도 프로세스로 동작하므로, 개발·배포·실행 단위가 모두 동일함.
좋은 소프트웨어로 분류되는 이유:
- 내부는 높은 응집도
- 내부는 낮은 복잡도
- 개발/배포/실행 단위가 동일하여 독립적 관리 가능
- 서비스 간 느슨한 결합(Loosely-Coupled)
"마이크로(micro)"는 기준 단위의 10⁻⁶ — 나노도 밀리도 아닌, "적당하게 작다"는 의미로 이해하면 됨. 무조건 극단적으로 작게 쪼개는 것이 목표가 아니라, 독립적으로 관리 가능한 적절한 크기로 분리하는 것이 핵심임.
현대 웹 애플리케이션은 최초 한 번만 HTML을 로드한 뒤, 이후 화면 전환은 페이지 새로고침 없이 JavaScript로 동적으로 처리하는 방식(SPA, Single Page Application)을 따름. 화면에 필요한 변수 데이터 생성 및 처리는 클라이언트 사이드(JS)에서 담당함.
전체 흐름:
1. 최초 접속 시: 브라우저(Web Client)가 web-server(nginx 등)에 GET 요청을 보내 Vue.js/React로 빌드된 정적 리소스(JavaScript, HTML, CSS, 이미지)를 받아옴.
2. 이후 데이터 요청: 브라우저가 API Gateway에 HTTP Request를 보내면, Gateway가 REST API Server로 요청을 전달하고 JSON 형태로 응답을 받아 브라우저에 돌려줌. 데이터 형식은 `Content-Type: application/json`.
3. REST API Server는 DB/SQL과 연동해 데이터를 처리함.
구성 요소별 기술 스택:
| 구성 요소 | 예시 기술 |
| --- | --- |
| Web Client (브라우저) | HTML, CSS, JavaScript |
| Web Server (정적 리소스 제공) | nginx + Vue.js / React 빌드 결과물 |
| API Gateway | Kong, HAProxy, nginx, Spring Cloud Gateway |
| REST API Server | Spring Boot, Node.js, Python(FastAPI 등) |
| DB | MySQL, PostgreSQL 등 |
nginx가 정적 리소스(Vue.js/React 빌드 파일)를 서빙하는 역할을 맡으므로, 물리적으로는 백엔드 서버에 위치하지만 프론트엔드 코드를 전달하는 역할을 함 — 프론트엔드냐 백엔드냐 경계가 모호한 지점임.
---
### JSON Format
JSON(JavaScript Object Notation)은 데이터를 키-값 쌍 형식으로 표현하는 경량 데이터 교환 형식임. 언어에 구애받지 않아 대부분의 프로그래밍 언어에서 사용 가능하며, 사람이 읽기 쉽고 기계가 처리하기도 간단함. 주로 API 응답, 데이터 교환에 사용됨.
기본 구조:
- 객체(Object): `{}`로 묶이고 키-값 쌍으로 구성
- 배열(Array): `[]`로 묶이고 값들의 리스트를 포함
- 값(Value): 문자열, 숫자, 객체, 배열, `true`, `false`, `null` 지원
```json
{
  "name": "John Doe",
  "age": 30,
  "isMarried": false,
  "children": ["Anna", "Ben"],
  "address": {
    "city": "Seoul",
    "zipCode": "12345"
  }
}
```
---
### YAML Format
YAML(YAML Ain't Markup Language)은 사람이 읽기 쉽도록 설계된 데이터 직렬화 형식임. JSON보다 간결하고 가독성이 높으며, 주로 구성 파일(config)에서 많이 사용됨.
기본 구조:
- 키-값 쌍: `:`으로 구분
- 리스트: 로 시작
- 계층 구조: 들여쓰기로 표현
- 주석: `#`으로 작성
```yaml
name: John Doe
age: 30
isMarried: false
children:
  - Anna
  - Ben
address:
  city: Seoul
  zipCode: "12345"
```
---
### JSON vs YAML
| 특징 | JSON | YAML |
| --- | --- | --- |
| 형식 | `{}`와 `[]`를 사용한 구조적 표현 | 들여쓰기 기반의 구조적 표현 |
| 가독성 | 읽을 수 있으나 형식이 딱딱함 | 사람이 읽기 매우 쉬움 |
| 주석 지원 | 지원하지 않음 | `#`으로 주석 작성 가능 |
| 사용 사례 | API 응답, 데이터 교환, 브라우저 내 데이터 처리 | 구성 파일, 설정 파일 |
| 파싱 속도 | 빠름 | JSON보다 느릴 수 있음 |
| 유연성 | 고정된 형식 | 더 유연하며 덜 엄격함 |
---
### 동기와 비동기 (Sync vs Async) — 개념

동기(Synchronous)는 요청을 보낸 뒤 응답이 올 때까지 기다리는 방식임. Request-response model로, Sender가 요청을 보내고 Receiver의 응답을 받은 뒤에야 다음 작업으로 넘어감.
비동기(Asynchronous)는 요청을 보낸 뒤 기다리지 않고 다음 작업을 이어 수행하는 방식임. Fire and forget model로, Sender가 Queue에 메시지를 넣으면 Receiver가 준비됐을 때 처리함. 두 요청을 동시에 던진 뒤 응답은 나중에 각각 받을 수 있음.
---
### 동기와 비동기 (Sync vs Async) — 비교
| 구분 | 동기식 (Synchronous) | 비동기식 (Asynchronous) |
| --- | --- | --- |
| 처리 방식 | 요청 → 응답까지 기다림 | 요청 → 기다리지 않고 다음 작업 수행, 결과는 나중에 수신 |
| 흐름 제어 | 직렬적(Blocking) 처리 | 병렬적(Non-blocking) 처리 |
| 응답 시간 | 요청 수 많을수록 느려짐 | 병렬 처리 가능하여 시스템 응답성 향상 가능 |
| 구현 복잡도 | 단순함 (순차적 코드 흐름) | 복잡함 (콜백 지옥, 상태 관리 필요) |
| 신뢰성 | 높은 일관성 (순서대로 처리됨) | 처리 순서 불확실성 (재시도, 실패 감지 필요) |
| 리소스 사용 | 자원 점유 시간 길어짐 | 자원 효율적으로 사용 가능 |
| 사용 적합 상황 | 트랜잭션이 중요한 금융/결제 시스템 등 | 대규모 사용자 이벤트 처리, 알림, 대기열 기반 작업 등 |
| 예시 | 함수 호출 후 리턴값 기다림, HTTP 요청/응답 | 이벤트 리스너, 콜백, Promise, 메시지 큐 |
---
### 좋은 소프트웨어란?
소프트웨어 품질을 판단하는 네 가지 관점:
| 관점 | 정의 |
| --- | --- |
| 응집도 (Cohesion) | 하나의 모듈/서비스가 하나의 역할/책임에 집중하는 정도. 높을수록 변경·이해·재사용이 쉬움. |
| 복잡도 (Complexity) | 업무 로직, 아키텍처의 복잡도. 낮을수록 유지보수와 확장이 용이함. |
| 단독 실행 (Standalone Execution) | 시스템의 일부를 독립적으로 실행하거나 테스트할 수 있는 능력. 높을수록 분산 개발/배포/장애 복구에 유리함. |
| 결합도 (Coupling) | 구성 요소 간 의존성. 낮을수록(Loosely-Coupled) 변경/확장이 쉽고, 높으면(Tightly-Coupled) 전체 시스템에 영향을 줌. |
---
### 소프트웨어 아키텍처 비교 — Monolith vs MSA

| 기준 | Monolith | MSA (Microservice Architecture) |
| --- | --- | --- |
| 응집도 | 역할과 책임의 혼재 (응집도 낮음) | 기능별 책임 분리 (응집도 높음) |
| 복잡도 | 로직 복잡도 높음, 아키텍처 복잡도 낮음 | 로직 복잡도 낮음, 아키텍처 복잡도 높음 |
| 단독 실행 | 개별 실행이 어려움, 테스트 복잡도 증가 | 개별 실행 용이, 테스트 복잡도 낮음 |
| 결합도 | 높음(Tightly-Coupled) → 하나 변경 시 전체 영향 | 낮음(Loosely-Coupled) → 독립적 배포·확장 가능 |
Monolith가 하나의 프로그램이니 응집도가 더 높지 않냐는 의문이 생길 수 있음. 하지만 응집도는 전체 프로그램 단위가 아니라, 하나의 모듈이 얼마나 일관된 책임을 가지고 있는가의 측면에서 판단함. Monolith는 하나의 프로세스 안에 주문·결제·상품 서비스가 뒤섞이므로 모듈별 응집도가 낮아짐.
---
### Monolith (덩어리)
Monolith에서 실행 단위(프로세스 = WAS)는 개발·배포·운영의 단위이기도 함. 주문(Order), 결제(paymt), 상품(product) 서비스가 하나의 WAS 프로세스 안에 함께 묶여 JVM 위에서 실행됨. 코드 묶음 단위는 class/bean이며, 배포 단위는 War/Jar 파일임.

나쁜 소프트웨어로 분류되는 이유:
- 내부는 낮은 응집도
- 내부는 높은 복잡도
- 개발/배포 단위가 War/Jar, 실행 단위가 WAS로 분리됨
- 서비스 간 긴밀한 결합
여기서 "나쁘다"는 잘못되었다는 의미가 아니라, 개발/운영 관점에서 관리하기 어렵다는 의미로 이해해야 함.
---
### 마이크로 서비스 (알갱이)
마이크로 서비스(MSA)에서는 서비스마다 독립적인 프로세스(실행 단위)를 가짐. 주문(Order), 결제(paymt), 상품(product) 각각이 별도 JVM 위에서 별도 프로세스로 동작하므로, 개발·배포·실행 단위가 모두 동일함.

좋은 소프트웨어로 분류되는 이유:
- 내부는 높은 응집도
- 내부는 낮은 복잡도
- 개발/배포/실행 단위가 동일하여 독립적 관리 가능
- 서비스 간 느슨한 결합(Loosely-Coupled)
"마이크로(micro)"는 기준 단위의 10⁻⁶ — 나노도 밀리도 아닌, "적당하게 작다"는 의미로 이해하면 됨. 무조건 극단적으로 작게 쪼개는 것이 목표가 아니라, 독립적으로 관리 가능한 적절한 크기로 분리하는 것이 핵심임.
---
### Java의 역사 — 등장 배경
1990년대 초반 주요 개발 환경의 문제점:
- 플랫폼 종속성 문제 (OS·하드웨어 의존)
- 메모리 관리의 어려움
- 메모리 직접 접근 및 OS 권한을 가지는 프로그램으로 인한 보안 취약
- 네트워크/분산 프로그램 개발의 어려움
Java는 하드웨어·OS 중심 개발에서 "플랫폼 독립적, 네트워크 중심, 엔터프라이즈 중심 개발"로 패러다임 전환을 위해 등장함.
Java가 해결한 다섯 가지 핵심 문제:
1. 플랫폼 독립성 해결
	- write once, run anywhere — 소스코드를 바이트 코드로 컴파일한 뒤 JVM 위에서 실행
	- Windows, Linux, Unix 등 OS에 관계없이 동일하게 동작함
2. 메모리 관리 자동화
	- Garbage Collection(GC) 도입 — 개발자가 메모리 해제를 직접 신경 쓸 필요 없음
	- 메모리 누수 감소, 서버 장기 실행에 안정적
3. 강력한 보안 모델
	- 포인터 없음 (메모리 직접 접근 차단)
	- 샌드박스 실행 모델
	- 클래스 로딩 시 검증
4. 네트워크를 기본 전제로 설계
	- `java.net` 패키지 기본 제공
	- socket, http, URL 추상화
	- 예외 기반 오류 처리
	- 웹서버, WAS, 분산 시스템으로 확장 가능
5. 대규모 엔터프라이즈 개발에 적합
	- 강제적 OOP(객체지향 프로그래밍)
	- 명확한 타입 시스템
	- 패키지 구조
	- 멀티스레딩 표준화
	- 비동기 처리 기반의 대용량 처리 지원
---
### Java의 역사 — 버전 연표
Sun Microsystems의 제임스 고슬링(James Gosling)과 팀이 가전 제품용 언어 개발에서 출발하여 범용 언어로 발전시킴. 2010년 Oracle이 Sun을 인수하면서 Java의 상품권, 저작권, 브랜드가 Oracle로 이전됨.
주요 버전 흐름:
- 1995년: Java 1.0 공개 — Write Once, Run Anywhere 선언
- 1998년: Java 2 (J2SE 1.2) — Swing UI 도입, JVM 안정성 강화
- 2018년: Java 11 — Oracle이 LTS 정책 발표. 6개월마다 새 버전, 3년마다 LTS 버전 출시 체계로 전환
- 2025년 기준: GA 최신 버전 Java SE 25 / LTS 버전 Java SE 21
에디션 구분:
- SE(Standard Edition): Java 언어의 기준이 되는 표준 플랫폼
- EE(Enterprise Edition): WAS 같은 기업용 서버의 표준 사양. 현재는 Jakarta EE로 이전됨.
버전 지원 정책:
- GA(General Availability): 정식 릴리즈. 검증된 안정 버전으로 새로운 기능이나 변경 사항을 포함함. 최신 기술을 빠르게 경험하고 싶은 개발자용이며, 일반적으로 다음 버전까지 6개월 단기 지원 (신규 기능이라도 deprecated 될 수 있음)
- LTS(Long Term Support): 장기지원 버전. 몇 년간 안정적이고 지속적인 보안/버그 패치, 호환성 검증이 이루어지는 버전으로, 기업·프로덕션 환경용으로 사용됨.
---
### Interpreter와 Compiler
소스 코드를 기계가 이해할 수 있는 기계어로 변환하는 방식에는 두 가지가 있음.
| 구분 | Compiler | Interpreter |
| --- | --- | --- |
| 변환 시점 | 프로그램 전체를 먼저 변환 (실행 전 완료) | 실행하면서 조금씩 변환 (실행 중 계속 수행) |
| 변환 횟수 | 한 번만 컴파일 | 실행할 때마다 해석 및 변환 |
- ByteCode: 컴파일러가 생성하는 중간 언어. Java의 `.class`, Python의 `.pyc`가 해당됨.
- JIT(Just In Time): 실행 시점에 바이트코드를 네이티브 기계어로 변환하는 방식. 컴파일과 인터프리터의 혼합 접근으로 성능을 높임.
- Compiler의 기기 의존 문제(OS·아키텍처마다 다른 바이너리 필요)는 컨테이너로 해결 가능함.
---
### \[참고\] 다양한 언어의 실행 방식
| 언어 | 방식 | Bytecode | JIT | 실행 방식 |
| --- | --- | --- | --- | --- |
| C | 컴파일 | X | X | Native 실행 |
| C++ | 컴파일 | X | X | Native 실행 |
| Rust | 컴파일 | X | X | Native 실행 |
| Go | 컴파일 | X | X | Native 실행 |
| Java | 혼합 (.class) | O | O | Bytecode → JIT → Native |
| Python | 혼합 (.pyc) | O | X (외부 C/C++ Lib 호출) | Bytecode → Python VM |
| JavaScript | 혼합 (실행시 Bytecode) | O | O | Bytecode → JIT → Native |
언어별 주요 포지션:
| 역할 | 언어 |
| --- | --- |
| 엔터프라이즈 비즈니스 로직 | Java, Kotlin |
| 클라우드 인프라 / 플랫폼 | Go |
| 시스템 핵심 / 고성능 | Rust |
| AI / 데이터 | Python |
---
### Java의 특징
- 객체 지향적인 언어: 모든 것을 객체로 표현하고, Object 클래스에서 모든 클래스가 파생됨.
- 플랫폼 독립적: 자바 가상 머신(JVM) 위에서 동작하기 때문에 OS에 종속적이지 않음.
- 메모리 관리: Garbage Collector가 존재하기 때문에 개발자가 직접 메모리 할당/해제를 하지 않아도 됨.
- 풍부한 라이브러리: 방대한 표준 라이브러리(Java API)를 제공 — 네트워크, 데이터베이스 연결, GUI 개발 등.
---
### Java 프로그램의 구조
Java 프로그램은 클래스(Class)를 기본 단위로 구성하며, 가장 간단한 프로그램도 최소 하나 이상의 클래스를 포함함.
```java
// 패키지 선언 (선택 사항)
package edu.skala;

// 클래스 선언
public class HelloSkala {

// main 메서드 (프로그램의 시작점)
    public static void main(String[] args) {
// 실행할 코드 작성
        System.out.println("Hello, Skala!");
    }

// 다른 메서드들 (선택 사항)
    public void anotherMethod() {
// ...
    }
}
```
---
### Java 메모리 구조
Java 프로그램 실행 시 메모리는 크게 Stack 영역과 Heap 영역으로 나뉨.
Stack 영역:
- 메서드 호출 정보와 지역 변수(Local Variables), 기본형(Primitive type) 변수가 저장됨.
- 메서드가 호출될 때마다 하나의 프레임(Frame)이 스택에 쌓이고, 메서드 실행이 끝나면 해당 프레임이 제거됨.
- 스레드마다 별도의 스택 영역을 가짐.
Heap 영역:
- 객체(Object)와 배열(Array)이 저장되는 공간.
- 프로그램 실행 중 생성되는 거의 모든 데이터가 이곳에 저장됨.
- 여러 스레드가 공유하는 영역.
- Garbage Collector(GC)가 주로 활동하는 영역으로, 더 이상 사용되지 않는 객체를 찾아내 메모리에서 제거함.
```java
void method() {
    int a = 10;              // Stack (지역 변수)
    String s = "Hello";     // Stack (참조), 문자열은 Heap의 상수 풀
    Person p = new Person(); // p는 Stack, 객체는 Heap
}
```
---
### \[참고\] 메모리 Stack vs Heap

`Method1()`이 실행되면:
- `int a = 10`, `int b = 20`은 기본형이므로 Stack에 값 자체가 저장됨.
- `class1 obj = new class1()`은 참조 변수 `obj`가 Stack에 생성되고, 실제 객체(Object)는 Heap에 생성됨. Stack의 `obj`는 Heap의 객체를 가리키는 참조(ref)를 저장함.
메서드가 종료되면 Stack 프레임 전체가 사라지며, Heap에 남은 객체는 GC가 수거함.
---
### 자바와 JVM
JVM(Java Virtual Machine)은 자바를 실행하기 위한 가상 머신임. Java 어플리케이션은 JVM 위에서 동작하기 때문에 OS에 종속적이지 않음.
계층 구조:

JVM이 OS와 Java 애플리케이션 사이의 추상화 계층 역할을 하기 때문에, 동일한 `.class` 파일을 Windows에서도 Linux에서도 실행할 수 있음.
---
### Java 파일과 컴파일
Java 소스코드가 실행 프로그램이 되기까지의 흐름:
`.java 파일` → Compiler → `.class 파일` → JVM → `Program`
- `.java` 파일: 개발자가 작성하는 텍스트 기반의 소스 코드. 사람 친화적.
- `.class` 파일: 컴파일러가 `.java`를 변환한 바이트코드 파일. JVM이 읽고 실행할 수 있는 중간 언어. 플랫폼 독립적. JVM 친화적.
- JVM: 바이트코드(`class` 파일)를 읽어 실제 CPU가 실행할 수 있는 기계어로 변환하는 실행 엔진. CPU 친화적.
---
### \[참고\] IP vs Port의 실제 의미 — 계층 구조
네트워크 통신은 여러 계층에 걸쳐 동작함.
- User 영역: 프로세스(크롬, 파이어폭스 등)가 Socket을 통해 네트워크 I/O를 수행함. Socket은 파일 I/O처럼 추상화된 인터페이스임.
- Kernel 영역: TCP(전송 계층)와 IP(네트워크 계층)가 실제 패킷 전송을 담당함. TCP가 Port를, IP가 호스트 주소를 처리함.
- H/W 영역: NIC(Network Interface Card)가 물리적 신호를 송수신하며, Driver가 H/W와 Kernel 사이를 연결함.
즉, Port는 TCP 계층에서 관리되고 IP는 그 아래 계층에서 관리됨. 애플리케이션(프로세스)은 Socket이라는 추상화된 인터페이스를 통해 이 모든 계층을 투명하게 사용함.
---
### Java 프로그램의 구조 — 개발환경 구성
Java 프로그램은 클래스(Class)를 기본 단위로 구성하며, 가장 간단한 프로그램도 최소 하나 이상의 클래스를 포함함.
```java
// 클래스 선언
public class HelloSkala {

// main 메서드 (프로그램의 시작점)
    public static void main(String[] args) {
// 실행할 코드 작성
        System.out.println("Hello, Skala!");
    }
}
```
구성 요소별 역할:
| 구성 요소 | 역할 |
| --- | --- |
| 클래스 (class) | 프로그램 단위 구성 블록 |
| main() 메서드 | 자바 프로그램 실행의 시작점 |
| 출력문 (System.out.println) | 텍스트를 콘솔에 출력 |
---
### 자바 변수와 자료형
Java의 자료형은 기본형(Primitive)과 참조형(Reference)으로 구분됨.
| 분류 | 자료형 | 크기 (byte) | 기본값 | 설명 | 예시 코드 |
| --- | --- | --- | --- | --- | --- |
| 기본형 | byte | 1 | 0 | 정수형, -128 \~ 127 | `byte b = 100;` |
|  | short | 2 | 0 | 정수형, -32,768 \~ 32,767 | `short s = 30000;` |
|  | int | 4 | 0 | 기본 정수형 | `int i = 100000;` |
|  | long | 8 | 0L | 큰 범위의 정수형, 접미사 L 필요 | `long l = 10000000000L;` |
|  | float | 4 | 0.0f | 실수형, 접미사 f 필요 | `float f = 3.14f;` |
|  | double | 8 | 0.0 | 기본 실수형 | `double d = 3.141592;` |
|  | char | 2 | '\\u0000' | 문자형, 유니코드 사용 | `char c = 'A';` |
|  | boolean | 1 (논리적) | false | true 또는 false | `boolean flag = true;` |
| 참조형 | String | - | null | 문자열 객체 (클래스) | `String msg = "Hello";` |
|  | 배열 (\[\]) | - | null | 같은 타입의 집합 | `int[] arr = {1, 2, 3};` |
|  | 사용자 정의 클래스 | - | null | 객체 생성 필요 | `Student s = new Student();` |
---
### 기본형과 참조형 래퍼(Wrapper) 클래스
기본 타입을 래퍼 클래스로 변환하는 과정을 boxing, 반대를 unboxing이라고 함. Java에서는 기본형과 래퍼 클래스 간의 boxing/unboxing이 자동으로 처리됨(오토박싱).
기본형 → 래퍼 클래스 대응:

| 기본형 | 래퍼 클래스 |
| --- | --- |
| byte | Byte |
| short | Short |
| long | Long |
| int | Integer |
| float | Float |
| char | Character |
| boolean | Boolean |
| void | Void |
```java
// Boxing (기본형 → 래퍼)
int primitive = 10;
Integer wrapper = primitive;  // 자동 boxing

// Unboxing (래퍼 → 기본형)
Integer wrapper = 100;
int primitive = wrapper;      // 자동 unboxing
```
---
### \[참고\] 기본형 저장 위치
기본형은 객체가 아니기 때문에 실행 컨텍스트에 따라 저장 위치가 달라짐.
```java
// 케이스 1: 메서드 지역 변수
void foo() {
    int a = 10;
    long b = 20L;
}
// → Stack Frame의 Local Variables 영역에 저장

// 케이스 2: 연산
int c = a + b;
// → a, b는 Operand Stack으로 복사되어 계산
// → c는 Local Variables에 저장

// 케이스 3: 객체의 필드
class A { int x; }
A a = new A();
// → new A() 객체는 Heap
// → x attribute는 Heap (객체 내부에 포함)
// → 참조 변수 a는 Stack

// 케이스 4: static 필드
class A { static int count; }
// → 클래스 메타 데이터는 Metaspace
// → java.lang.Class 객체는 Heap
// → static int count는 Class 객체 내 Heap에 저장
```
---
### \[참고\] 기본형과 참조형의 저장 방식
| 데이터 타입 | 저장 위치 | 메모리 구조 설명 |
| --- | --- | --- |
| Primitive 타입 | 스택(Stack) | 고정된 크기의 값이므로 스택에 저장 가능 |
| Reference 타입 | 힙(Heap) | 동적 크기를 가지므로 힙에 객체가 저장됨 |
| Reference 변수 자체 | 스택(Stack) | 참조값(주소)이 저장됨 |
핵심 차이:
- `int b = a`처럼 기본형을 복사하면 JVM이 값을 그대로 복사함 (독립적인 두 변수)
- `int[] d = c`처럼 참조형을 복사하면 Stack의 참조값(주소)이 복사됨 — d와 c는 같은 Heap 객체를 가리킴
- `int[] e = {5, 6, 7}`과 `int[] f = {5, 6, 7}`은 값은 같지만 서로 다른 Heap 객체를 가리킴
- `String g = "hello"`의 참조 변수 g는 Stack, 실제 문자열 객체는 Heap(상수 풀)에 위치함
---
### \[참고\] 참조형 변수의 불변 객체 (Immutable Object)
불변 객체(Immutable Object)란 한 번 생성된 후 내부 상태(필드 값)가 절대 변경되지 않는 객체임. 값을 변경하는 것처럼 보이는 연산은 실제로는 새로운 객체를 생성해서 반환함.
Java의 Wrapper Class인 Integer, Float, Double, Long, Character, Boolean과 String이 모두 불변 객체에 해당함.
Call by Value (기본형 `int`):
```java
int a = 10;
int b = a;
a = 20;
// 결과: a=20, b=10
// b는 a의 값을 복사했으므로 a 변경에 영향받지 않음
```
Call by Reference이지만 불변 객체 (래퍼 `Integer`):
```java
Integer a = 10;
Integer b = a;   // b도 같은 Integer(10) 객체를 가리킴
a = 20;          // 새로운 Integer(20) 객체 생성 후 a가 가리킴
// 결과: a=20, b=10
// b는 여전히 Integer(10)을 가리키므로 영향받지 않음
```
Integer는 참조형이지만 불변이기 때문에 `a = 20` 시 기존 객체를 수정하지 않고 새 Integer(20) 객체를 생성함. 따라서 b는 여전히 Integer(10)을 가리켜 결과는 `a=20 b=10`이 됨.
---
### 자바의 키워드
언어의 문법을 구성하는 예약어(reserved words)로, 변수명이나 메서드 이름 등으로 사용 불가함.
| 제어문/흐름 | 클래스/객체 관련 | 자료형/리터럴 | 접근/제어 | 기타 키워드 |
| --- | --- | --- | --- | --- |
| if, else | class | int | public | package |
| switch, case, default | interface | double | private | import |
| while, do, for | enum | boolean | protected | return |
| break, continue, return | extends | char | static | new |
| yield (Java 14+) | implements | byte, short, long | final | this, super |
| record (Java 16+) | instanceof | float, void | abstract | throws, throw |
|  | new, super, this |  | synchronized | try, catch, finally |
|  | null (리터럴) |  | transient, volatile | assert |
|  |  |  |  | goto\*, const\* |
추가 설명:
- `yield`: switch expression에서 여러 줄 return 시 `return` 대신 사용 (Java 14+)
- `record`: 불변 데이터 전용 클래스. DTO 작성 시 반복 코드를 제거해줌 (Java 16+)
- `goto`와 `const`: Java에서 실제로 사용되지 않지만, 예약어로 지정되어 있어 변수명으로 사용 불가
---
### 자바 연산자
| 분류 | 연산자 예시 | 설명 |
| --- | --- | --- |
| 산술 | `+`, `-`, `*`, `/`, `%` | 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지 연산 |
| 비교 | `==`, `!=`, `<`, `>`, `<=`, `>=` | 두 값의 크기나 동등성 비교 |
| 논리 | `&&`, `\|\|`, `!` | AND, OR, NOT 논리 연산 |
| 대입 | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | 값을 변수에 저장하거나 연산 후 대입 |
| 증감 | `++`, `--` | 값 1 증가 또는 감소 (전위, 후위 모두 가능) |
| 삼항 | `조건 ? 참값 : 거짓값` | 조건에 따라 값을 선택하는 연산 |
| 비트 | `&`, `\|`, `^`, `~`, `<<`, `>>`, `>>>` | 비트 단위 연산 |
| 문자열 연결 | `+` | 문자열을 이어 붙일 때 사용 |
---
### 산술 연산
```java
int a = 10;
int b = 3;

System.out.println(a + b); // 13
System.out.println(a % b); // 1  (10을 3으로 나눈 나머지)
```
---
### 비교 연산
결과는 항상 `boolean`(true/false)으로 반환됨.
```java
int a = 10;
int b = 3;

System.out.println(a > b);   // true
System.out.println(a == 10); // true
```
---
### 논리 연산
```java
boolean x = true;
boolean y = false;

System.out.println(x && y); // false  (AND: 둘 다 true여야 true)
System.out.println(x || y); // true   (OR: 하나라도 true면 true)
System.out.println(!x);     // false  (NOT: 반전)
```
단축 평가(Short-circuit evaluation):
- `&&`: 앞의 조건이 `false`면 뒤 조건을 평가하지 않음
- `||`: 앞의 조건이 `true`면 뒤 조건을 평가하지 않음
---
### 대입 및 복합 대입 연산
복합 대입 연산자는 연산과 대입을 한 번에 처리함.
```java
int num = 5;
num += 2; // num = num + 2 와 동일

System.out.println(num); // 7
```
---
### 증감 연산 — 전위/후위 차이
```java
int i = 5;

System.out.println(++i); // 6  (전위: 먼저 1 증가 후 출력)
System.out.println(i++); // 6  (후위: 현재 값 출력 후 1 증가)
System.out.println(i);   // 7  (이전 후위 증가 결과 반영)
```
전위(`++i`)는 증가 후 표현식에서 사용하고, 후위(`i++`)는 표현식에서 먼저 사용한 뒤 증가함.
---
### 삼항 연산
조건식 `?` 참일 때 값 `:` 거짓일 때 값 형태로 사용함. if-else를 한 줄로 표현할 수 있어 간단한 조건 분기에 유용함.
```java
int score = 85;

String result = (score >= 80) ? "합격" : "불합격";
System.out.println(result); // 합격  (85 >= 80이므로 참)
```
---
### 문자열 연결
`+` 연산자를 사용해 문자열과 다른 타입의 값을 이어 붙일 수 있음. 숫자나 변수도 자동으로 문자열로 변환됨.
```java
String name = "스칼라";

System.out.println("안녕하세요, " + name + "님!"); // 안녕하세요, 스칼라님!
```
---
### 문자열 포맷터 — String.format(), printf()
형식 지정자(서식):
| 서식 | 설명 |
| --- | --- |
| `%s` | 문자열 |
| `%d` | 10진수 정수 |
| `%f` | 실수 (소수점 기본 6자리) |
| `%c` | 문자 |
| `%b` | boolean 값 |
| `%%` | % 자체 |
```java
String name = "스칼라";
int age = 30;
String formatted = String.format("이름: %s, 나이: %d", name, age);
System.out.println(formatted); // 이름: 스칼라, 나이: 30

double pi = 3.141592;
System.out.println(String.format("원주율: %.2f", pi)); // 원주율: 3.14

// 정렬
System.out.printf("|%10s|\n", "Java");  // |      Java|  오른쪽 정렬 (총 10자리)
System.out.printf("|%-10s|\n", "Java"); // |Java      |  왼쪽 정렬

// 숫자 앞 0 채우기
System.out.printf("%05d\n", 42); // 00042
```
---
### 문자열 포맷터 — StringBuilder
StringBuilder는 문자열을 빠르고 효율적으로 조립(append)할 수 있는 클래스임. 반복적이거나 동적으로 문자열을 생성할 때 매우 유용하며, 포맷 효과를 수동으로 구성할 수 있음.
```java
String name = "스칼라";
int age = 25;

StringBuilder sb = new StringBuilder();
sb.append("이름: ").append(name)
  .append(", 나이: ").append(age);

System.out.println(sb.toString()); // 출력: 이름: 스칼라, 나이: 25
```
`String.format()`과 조합해 정렬 효과도 낼 수 있음:
```java
StringBuilder sb = new StringBuilder();
sb.append(String.format("%-10s", "스칼라")) // 왼쪽 정렬
  .append(String.format("%5d", 25));        // 오른쪽 정렬

System.out.println(sb.toString()); // 출력: 스칼라          25
```
`append()`를 연속으로 체이닝해서 쓰는 방식을 Method Chaining / Fluent API 방식이라고 함. 각 `append()`가 StringBuilder 자신을 반환하기 때문에 가능한 패턴임.
---
### Mutex (상호 배제, Mutual Exclusion)
Multi-Thread 환경에서 "공유 자원에는 한 번에 하나의 Thread만 접근해야 한다"는 개념을 구현한 동기화 메커니즘임.
Thread 1이 공유 자원에 접근해 Mutex를 잠그면(LOCKED), Thread 2는 접근이 차단(Blocked)되어 대기함. Thread 1이 작업을 마치고 잠금을 해제해야 Thread 2가 접근할 수 있음.
---
### Mutex Lock 구현체 — synchronized
Java에서 Mutex Lock을 구현하는 키워드는 `synchronized`임. 멀티 스레드 환경에서 동기화를 보장하며, 공유 자원에 여러 스레드가 동시에 접근할 때 데이터 불일치를 차단함.

```java
public synchronized void withdraw(int amount) {
    ...
}
```
thread1이 `withdraw()`를 호출해 synchronized 메서드를 잠그면, thread2\~thread5는 모두 잠금이 해제될 때까지 대기(waiting for lock)함. thread1 실행이 끝나야 다음 스레드가 진입 가능함.
---
### StringBuilder vs StringBuffer
두 클래스는 사용법이 완전히 동일하지만, 스레드 안전성과 성능에서 차이가 있음.
| 항목 | StringBuilder | StringBuffer |
| --- | --- | --- |
| 스레드 안전성 | 스레드 안전하지 않음 | 스레드 안전함 (synchronized) |
| 성능 | 빠름 (단일 스레드 환경에서 권장) | 느림 (동기화 오버헤드 있음) |
| 사용 시점 | 단일 스레드 또는 동기화 불필요한 경우 | 멀티 스레드 환경에서 동시 접근이 필요한 경우 |
| 도입 시기 | Java 5 이후 | Java 초창기부터 |
| 대체 관계 | StringBuffer의 비동기화 버전 | StringBuilder보다 안정적이나 느림 |
| 기본 메서드 | `append()`, `insert()`, `delete()`, `toString()` 등 | 동일 |
StringBuilder는 StringBuffer보다 최대 2\~3배 빠름 (동기화 오버헤드 없음). 단, 멀티스레드 환경에서 동기화 없이 StringBuilder를 공유하면 데이터 손상 위험이 있으므로 그 경우에는 StringBuffer를 사용해야 함.
---
### 네이밍 컨벤션
코드의 품질은 작명에서 시작함. 짧고 명확하며 일관성 있는 네이밍이 중요하며, 좋은 이름은 개발자의 사고를 명확히 하고 코드의 의미를 드러내는 가장 강력한 도구임.
| 관점 | 설명 |
| --- | --- |
| 의사 전달 | 잘 지은 이름은 주석 없이도 코드의 역할을 자연스럽게 설명함 |
| 유지보수 | 시간이 지나도 이름만 보고 코드의 의도를 쉽게 이해할 수 있음 |
| 협업 | 팀원들이 코드를 읽고 빠르게 파악할 수 있어 협업 효율이 올라감 |
| 디버깅/확장 | 적절한 네이밍은 추적, 검색, 재사용 시 핵심 단서 역할을 함 |
나쁜 예 vs 좋은 예:
| 나쁜 예 | 좋은 예 | 설명 |
| --- | --- | --- |
| `int d;` | `int daysUntilDeadline;` | 의미 없는 이름 대신 명확한 의미 |
| `getData()` | `getCustomerList()` | 반환 값의 성격을 명확히 표현 |
| `doStuff()` | `calculateTotalPrice()` | 기능을 명확하게 표현 |
---
### 네이밍 컨벤션 종류
| 명칭 | 표기 방식 | 예시 | 설명 |
| --- | --- | --- | --- |
| Camel Case (카멜 표기법) | 첫 단어 소문자, 이후 단어는 대문자 | `myVariableName` | Java 변수, 메서드명에 사용 |
| Pascal Case (파스칼 표기법) | 모든 단어의 첫 글자를 대문자 | `MyClassName` | Java 클래스, 인터페이스명에 사용 |
| Snake Case (스네이크 표기법) | 소문자 단어를 `_`로 구분 | `my_variable_name` | Python 변수, 데이터베이스 필드명 등 |
| Kebab Case (케밥 표기법) | 소문자 단어를 `-`로 구분 | `my-variable-name` | URL, 파일명 등에서 사용 |
| Upper Snake Case (Screaming Snake Case) | 대문자 단어를 `_`로 구분 | `MAX_VALUE` | Java 상수(final static)에 사용 |
- 는 대부분의 프로그래밍 언어에서 빼기 연산자로 해석되므로 식별자에 사용 불가함. 그래서 단어 구분에는 underbar(`_`)를 사용함.
---
### Java에서 사용하는 네이밍 규칙
| 항목 | 네이밍 방식 | 예시 |
| --- | --- | --- |
| 클래스 이름 | PascalCase | `HelloWorld`, `StockManager` |
| 인터페이스 이름 | PascalCase | `Runnable`, `Comparable` |
| 메서드 이름 | camelCase | `calculateBMI()`, `getName()` |
| 변수 이름 | camelCase | `studentName`, `stockCount` |
| 상수 이름 | Upper Snake Case | `MAX_SIZE`, `DEFAULT_PORT` |
- 상수(constant)는 항상 대문자 + 언더스코어(`SCREAMING_SNAKE_CASE`)로 작성
- 패키지 이름은 모두 소문자로 작성하며, 보통 도메인 역순으로 표기 (예: `com.example.service`)
---
### Java에서 사용되는 CRUD 메서드 명 (동사 + 명사)
메서드 이름은 동사 + 명사로 구성하는 것이 일반적임. 예: `getUser()` = 사용자를 get한다.
| 동작 구분 | 대표 메서드 접두어 | 의미 / 설명 | 예시 메서드 이름 |
| --- | --- | --- | --- |
| 조회 (Read) | `get` | 단일 항목 조회 (by ID 등) | `getUserById()` |
|  | `find` | 조건 검색, 존재 여부 포함 | `findUserByEmail()` |
|  | `search` | 다중 조건 검색 (보통 리스트) | `searchUsersByKeyword()` |
|  | `load` | 지연 로딩 시 사용 (JPA 등) | `loadProfile()` |
| 추가 (Create) | `add` | 목록에 항목 추가 | `addItemToCart()` |
|  | `create` | 새 객체 생성 및 저장 | `createUser()` |
|  | `save` | DB에 저장 (create 또는 update 포함) | `saveProduct()` |
| 수정 (Update) | `update` | 기존 데이터 수정 | `updatePassword()` |
|  | `modify` | 특정 필드 일부 수정 | `modifyUserRole()` |
| 삭제 (Delete) | `delete` | 객체 또는 항목 삭제 | `deleteUserById()` |
|  | `remove` | 컬렉션/리스트 등에서 제거 | `removeItemFromList()` |
---
### 클래스 명
클래스 명은 명사로 짓는 것을 원칙으로 하며, UpperCamelCase(PascalCase)로 작성함. 두 개 이상의 단어가 조합될 때는 각 단어의 첫 번째 글자를 대문자로 씀.
예시:
- `OrderHistory.java`
- `UserJoinService.java`
---
### 메서드 명
동사 + 명사를 조합해 메서드 명을 구성하는 것이 일반적임. 동사로 시작하고, lowerCamelCase로 작성함. 두 개 이상의 단어가 조합될 때는 첫 글자만 소문자로 씀.
예시:
- `validateAndRun()`
- `findOrderHistories()`
- `execute()` — 동사만 있는 경우는 클래스명 또는 인터페이스명 자체로 명사 역할이 명확한 경우에 동사만으로 구성 가능
---
### 변수 명
변수명은 일반적으로 명사로 짓는 것을 권고함. 변수명을 읽었을 때 어떤 의미인지 파악이 가능해야 하며, AI Tool 등 도구 활용 시에도 변수명만으로 의미를 파악할 수 있어야 함.
예시:
- `username` (사용자 이름)
- `totalPrice` (총 금액)
- `createdAt` (생성일시)
- `maxRetryCount` (최대 재시도 횟수)
고려 사항:
- for 반복문에서 순서를 나타내기 위한 정수 변수명은 `i`, `j`, `k` 등을 관례적으로 활용함
- 변수명에 특수문자는 사용할 수 있지만 지양함
- `a`, `b2` 등 의미를 알기 힘든 단어는 지양함
---
### Java에서 객체를 만드는 방법
객체는 클래스의 인스턴스이며, 모든 객체는 `java.lang.Object`를 상속함.
클래스(Class)는 객체를 만들기 위한 설계도로 속성(Properties)과 동작(Methods)을 정의함. 객체(Object)는 클래스를 기반으로 실제 메모리 공간이 할당된 실체이며, 각 속성에 구체적인 값이 채워진 상태임. 객체의 위치는 주소(참조값)로 식별됨.
예를 들어 `Car` 클래스는 `color`, `price`, `km`, `model` 속성과 `start()`, `backward()`, `forward()`, `stop()` 메서드를 정의하고, `new Car()`로 생성된 객체는 `color: red`, `price: 23,000`, `km: 1,200`, `model: Audi` 같은 실제 값을 가짐.
---
### Java 핵심 용어
| 개념 | 설명 | Java 예제 코드 |
| --- | --- | --- |
| 클래스 (Class) | 객체를 만들기 위한 설계도. 속성과 동작을 정의. | `class Student` |
| 객체 (Object) | 클래스를 기반으로 생성된 실체(인스턴스). | `Student s1 = new Student();` |
| 속성 (Field) | 객체가 가지는 상태/정보 (변수). | `String name; double grade;` |
| 메서드 (Method) | 객체가 수행하는 동작 (함수). | `void study();` |
| 생성자 (Constructor) | 객체 생성 시 초기화 메서드. 클래스 이름과 동일. | `Student(String name, int id)` |
---
### Java — 클래스 (Class)
클래스는 객체를 생성하기 위한 설계도로 속성과 동작을 포함하며 생성자를 가짐.
| 구성 요소 | 설명 | 예시 |
| --- | --- | --- |
| 필드(Field) | 객체의 상태를 저장하는 변수 | `String name; double price;` |
| 메서드(Method) | 객체의 동작을 정의하는 함수 | `void updatePrice(double price) {...}` |
| 생성자(Constructor) | 객체 생성 시 초기화 (클래스 이름과 동일) | `public Stock(String name, double price) {...}` |
| this | 클래스 기반 생성된 객체 참조 | `this.name = name;` |
| super | 부모 클래스의 멤버에 접근 | `super(name, price);` |
```java
public class Stock {
    String name;
    double price;

    public Stock(String name, double price) {
        this.name = name;   // this: 현재 객체
        this.price = price;
    }

    public void updatePrice(double newPrice) {
        this.price = newPrice;
    }

    public void printInfo() {..}
}
```
---
### Java — 객체 (Object)
Class로부터 생성된 실체(Instance)로, 속성(필드)과 동작(메서드)을 갖는 메모리 상의 실제 존재임.
| 구성 요소 | 설명 | 예시 |
| --- | --- | --- |
| 인스턴스 생성 | 객체를 메모리에 생성 | `Stock s = new Stock("스칼라 AI", 17000);` |
| 필드 | 객체가 가지고 있는 상태/정보 | `s.name = "스칼라 AI";` |
| 메서드 | 객체가 수행할 수 있는 기능/행동 | `s.updatePrice(17000);` |
| 생성자 | 객체가 생성될 때 초기값 설정 | `new Stock("스칼라 AI", 17000);` |
```java
public class Main {
    public static void main(String[] args) {
// 객체 생성 (인스턴스화)
        Stock scalaEdu = new Stock("스칼라 에듀", 15000);
        Stock scalaAI  = new Stock("스칼라 AI", 17500);

// 객체 상태 변경
        scalaEdu.updatePrice(15800);
        scalaEdu.printInfo();
    }
}
```
---
### Java — 필드 (Field)
클래스 내부에 선언된 변수로, 객체의 고유한 "속성" 또는 "상태"를 저장함. 필드는 객체가 생성될 때 메모리에 할당되며, 각 객체는 독립적인 자신의 필드 값을 가짐.
| 종류 | 설명 | 예시 |
| --- | --- | --- |
| 인스턴스 필드 | 객체마다 독립적인 값을 가짐 | `String name;` |
| 정적 필드 (static) | 클래스 전체에서 공유되는 값 | `static int count;` |
| 상수 필드 (final) | 한 번 값이 정해지면 변경 불가 | `final String STOCK_TYPE = "우선주";` |
---
### this 이해하기
`this`는 클래스를 객체로 Heap에 생성될 때 그 객체를 가리키는 주소임. 클래스 자기 자신을 의미함.
생성자나 메서드에서 매개변수명과 필드명이 같을 때, `this.필드명`으로 명확히 구분함.
```java
class User {
    private String name;

    User(String name) {
        this.name = name; // this.name: 필드, name: 매개변수
    }
}
```
---
### Java — 메서드 (Method)
메서드는 객체의 동작(기능)을 정의하는 코드 블록임.
```plain text
[접근제어자] [반환형] [메서드이름](매개변수 목록) {
    // 메서드 본문
    return 값; // 반환형이 void가 아닌 경우
}
```
| 구성 요소 | 설명 | 예시 |
| --- | --- | --- |
| 접근제어자 | 외부에서 메서드 접근 가능 여부 | `public`, `private`, `protected`, (default) |
| 반환형 | 메서드 실행 후 반환하는 값의 타입 | `int`, `String`, `void` 등 |
| 메서드명 | 동작을 나타내는 이름 (소문자로 시작) | `getPrice`, `calculateTax` |
| 매개변수(Parameter) | 메서드에 전달되는 입력 값들 | `(int a, int b)` |
| return문 | 결과를 반환하고 메서드 종료 | `return a + b;` |
4가지 메서드 유형 예시 및 오버로딩:
```java
public class StockUtils {
// 1. 반환값도 없고, 매개변수도 없음
    public void printWelcomeMessage() { ... }

// 2. 매개변수만 있고, 반환값 없음
    public void printStockPrice(String stockName, double price) { ... }

// 3. 반환값만 있고, 매개변수 없음
    public String getMarketStatus() {
        return "장 마감";
    }

// 4. 매개변수도 있고, 반환값도 있음
    public double calculatePriceChange(double yesterday, double today) {
        return today - yesterday;
    }

// 5. 오버로딩(Overloading): 이름은 같지만 매개변수가 다름
    public void printStockPrice(String stockName, double price) {
        System.out.println("종목명: [" + stockName + "]");
        System.out.println("가격:   [" + price + "]");
    }
}
```
---
### Java — 메서드: 매개 변수와 인자
혼용되는 경우가 많지만 엄밀히 다른 개념임.
- 매개 변수(Parameters): 메서드에 전달된 입력값을 저장하는 변수. 메서드 선언부에 위치함.
- 인자, 전달 인자(Arguments): 메서드를 호출할 때 실제로 전달하는 입력값.
```java
int sum(int a, int b) { // a와 b는 매개 변수 (parameters)
    return a + b;
}

sum(1, 2); // 1과 2는 인자, 전달인자 (arguments)
```
---
### static 클래스, 변수, 메서드
`static` 키워드는 객체가 아니라 클래스 자체에 속하는 변수나 메서드를 정의할 때 사용함.
```java
static class Example {
    public static final int INITIAL_COUNT = 10; // Metaspace의 상수 풀에 존재
    private static int count = 0;               // Heap 내 java.lang.Class의 Index 정보
    private int instanceId;

    Example() {
        count++;
        instanceId = count + INITIAL_COUNT;
    }

    public static int getLastInstanceId() { return count + INITIAL_COUNT; }
    public static int getCount()          { return count; }
    public int getInstanceId()            { return instanceId; }
}
```
static 메서드는 객체 없이 클래스명으로 직접 호출하고, 인스턴스 메서드는 객체를 통해 호출함.
```java
// static 메서드: 클래스명으로 호출
System.out.println(Example.getCount());
System.out.println(Example.getLastInstanceId());

// 인스턴스 메서드: 객체를 통해 호출
Example e1 = new Example();
System.out.println(e1.getInstanceId());
```
e1, e2, e3를 순서대로 생성하면 각각의 `instanceId`는 `INITIAL_COUNT(10)` + 생성 순서로 결정됨. `count`는 static이므로 모든 인스턴스가 공유하며, `instanceId`는 인스턴스마다 독립적임.
---
### Java의 주석(comment) 방식
| 구분 | 사용 문법 | 용도 | 예시 |
| --- | --- | --- | --- |
| 한 줄 주석 | `//`로 시작 | 간단한 설명, TODO, 디버깅 등 | `// 변수 초기화` |
| 여러 줄 주석 | `/* ... */`로 감싸기 | 여러 줄 설명, 블록 주석 등 | `/* 여러 줄 주석입니다 */` |
| 문서 주석 | `/** ... */`로 시작 (Javadoc) | 메서드, 클래스 문서 자동화 | `/** 이름을 반환합니다 **/` |
```java
public class Example {

// 한 줄 주석: 사용자 이름 출력
    public static void main(String[] args) {
        /* 여러 줄 주석:
           변수 선언과 초기화 */
        String name = "Skala";

        /**
         * 사용자 이름을 출력합니다.
         * @param name 사용자 이름
         */
        System.out.println("Hello, " + name);
    }
}
```
---
#### Javadoc 주요 태그
| 태그 | 설명 |
| --- | --- |
| `@param` | 메서드 매개변수 설명 |
| `@return` | 반환값 설명 |
| `@throws` | 예외 설명 |
| `@author` | 작성자 |
| `@since` | 버전 표시 |
```java
/**
 * 주어진 두 수의 합을 반환합니다.
 *@parama 첫 번째 정수
 *@paramb 두 번째 정수
 *@return 두 정수의 합
 */
public int add(int a, int b) {
    return a + b;
}
```
---
### \[실습\] Javadoc 만들어보기
터미널 명령어로 HTML 문서를 생성할 수 있음:
```bash
javadoc -d doc JavaDocsExample.java
```
실제 적용 예시:
```java
/**
 * 간단한 계산기 클래스.
 * <p>
 * 두 개의 정수에 대해 덧셈과 뺄셈 기능을 제공합니다.
 * </p>
 *
 *@author 홍길동
 *@version 1.0
 *@since 2025-08-13
 */
public class Calculator {

    /** 마지막 계산 결과를 저장합니다. */
    private int lastResult;

    /**
     * 기본 생성자.
     * 초기 lastResult 값은 0입니다.
     */
    public Calculator() {
        this.lastResult = 0;
    }

    /**
     * 두 정수를 더합니다.
     *@parama 첫 번째 정수
     *@paramb 두 번째 정수
     *@return 덧셈 결과
     */
    public int add(int a, int b) {
        lastResult = a + b;
        return lastResult;
    }

    /**
     * 두 정수를 뺍니다.
     *@parama 첫 번째 정수
     *@paramb 두 번째 정수
     *@return 뺄셈 결과 (a - b)
     */
    public int subtract(int a, int b) {
        lastResult = a - b;
        return lastResult;
    }
}
```
생성된 HTML 문서는 VSCode의 Live Server로 `index.html`을 열어 확인할 수 있음.
---
### Java 주석 작성 가이드
| 가이드 항목 | 설명 |
| --- | --- |
| 필요한 경우만 작성 | 코드 자체로 의미가 명확할 경우 불필요한 주석은 피함 |
| 주석 내용은 왜(Why)와 무엇(What)을 설명 | 선택한 이유, 의도, 대안 비교 / 코드의 기능이나 동작 설명 |
| 오래된 주석 제거 | 코드가 변경되면 주석도 함께 업데이트 |
| Javadoc 사용 권장 | public 클래스/메서드는 `/** ... */` 문서 주석 사용 |
| TODO / FIXME 주석 | 작업 항목 추적 시 명확히 구분: `// TODO: 로그인 로직 추가` |
| API 문서 자동 생성 시 문서 주석 활용 | javadoc 도구로 HTML 문서 생성 가능 |
`// TODO`와 `// FIXME`는 개발자가 작업 중인 코드에 메모를 남길 때 사용하는 특별한 주석 패턴임. IntelliJ, Eclipse 같은 IDE에서도 자동으로 인식해 작업 추적(TODO 리스트) 용도로 널리 사용됨.
- `// TODO`: 해야 할 작업(To-Do)을 기록해두는 주석
- `// FIXME`: 현재 코드에 문제가 있음을 나타내고 수정이 필요함을 알리는 주석
---
### Java의 제어문 (Control Statements)
| 분류 | 제어문 종류 | 설명 | 사용 예시 또는 키워드 |
| --- | --- | --- | --- |
| 조건문 | if, else if, else | 조건에 따라 다른 블록을 실행 | `if (a > b) { ... }` |
|  | switch | 여러 값 중 하나와 일치하는 분기 실행 | `switch (value) { case 1: ... }` |
| 반복문 | for | 조건에 따라 정해진 횟수만큼 반복 | `for (int i = 0; i < 10; i++)` |
|  | while | 조건이 참인 동안 계속 반복 | `while (i < 10)` |
|  | do-while | 최소 1회는 실행되고 조건이 참인 동안 반복 | `do { ... } while (i < 10)` |
| 분기문 | break | 반복문 또는 switch문을 즉시 종료 | `if (...) break;` |
|  | continue | 현재 반복을 건너뛰고 다음 반복으로 진행 | `if (...) continue;` |
|  | return | 현재 메서드의 실행을 종료 또는 값을 반환 | `return value;` 또는 `return;` |
| 예외 처리 | try-catch-finally | 예외 상황을 처리하기 위한 제어 흐름 구조 | `try { ... } catch (Exception e) { ... } finally { ... }` |
|  | throw, throws | 예외를 발생시키거나 메서드에서 예외를 위임 | `throw new IOException();` |
---
### if, else if, else
조건식의 결과에 따라 코드 블록을 선택적으로 실행함.
```java
int score = 85;

if (score >= 90) {
    System.out.println("A 학점");
} else if (score >= 80) {
    System.out.println("B 학점");
} else {
    System.out.println("C 학점 이하");
}
// 출력: B 학점
```
---
### Java의 논리 연산자
| 연산자 | 의미 | 설명 | 예제 조건 |
| --- | --- | --- | --- |
| `&&` | and | 양쪽 조건이 모두 참이어야 전체 조건이 참 | `a > 0 && b > 0` |
| `\|\|` | or | 한쪽 조건이 참이면 전체 조건이 참 |  |
| `!` | not | 조건을 반대로 뒤집음 (참→거짓, 거짓→참) | `!(a > 0)` |
`&&`와 `||`는 단락 평가(short-circuit evaluation)로 처리됨:
- `a && b`: a가 false이면 b는 평가하지 않음
- `a || b`: a가 true이면 b는 평가하지 않음
```java
if (arriveAt <= "0900" && !leaderAtWork) {
// 출근한 동료들과 커피를 마시러 간다
}
```
---
### switch/case
여러 값 중 하나와 일치하는 분기를 선택하여 실행함. 각 case 끝에 `break`가 없으면 다음 case로 fall-through가 발생하므로 주의해야 함.
```java
int menu = 2;
switch (menu) {
    case 1:
        System.out.println("주식 조회");
        break;
    case 2:
        System.out.println("주식 매수");
        break;
    case 3:
        System.out.println("주식 매도");
        break;
    default:
        System.out.println("잘못된 선택");
}
```
입력값이 정형화되어 있는 경우(예: ENUM 활용)에는 if문보다 switch/case문이 가독성이 좋음.
```java
public enum LoginChannel {
    FACEBOOK, KAKAO, APPLE, NAVER, DEFAULT;
}

public static void executeLogin(LoginChannel channel) {
    switch (channel) {
        case FACEBOOK: facebookLogin(); break;
        case KAKAO:    kakaoLogin();    break;
        case APPLE:    appleLogin();    break;
        case NAVER:    naverLogin();    break;
        case DEFAULT:  defaultLogin();  break;
    }
}
```
---
### \[참고\] enum 내부 method 사용 방법
enum은 특수한 형태의 클래스임. 각 상수는 `public static final` 싱글턴 인스턴스이며, `name()`, `ordinal()`, `toString()` 등의 메서드를 기본으로 가짐. enum 내부에 일반 메서드를 추가할 수도 있음.
```java
public enum LoginChannel {
    FACEBOOK, KAKAO, APPLE, NAVER, DEFAULT;

    public boolean isSocial() {
        return this == FACEBOOK || this == KAKAO || this == NAVER;
    }
}

// 직접 enum 상수에서 호출
boolean result1 = LoginChannel.FACEBOOK.isSocial(); // true

// 변수를 통해 호출
LoginChannel channel = LoginChannel.FACEBOOK;
boolean result2 = channel.isSocial(); // true

// 조건문에서 활용
if (channel.isSocial()) {
    System.out.println(channel + "은 소셜 로그인입니다.");
}
```
---
### switch 표현식 (Java 14+)
기존 switch문에 함수형 스타일로 값을 반환할 수 있게 확장된 문법 체계임.
특징:
- 결과를 변수에 할당 가능 (Expression)
- `break` 불필요 — `>` 사용 시 자동 종료
- 다중 문장 사용 시 `{}` 블록 + `yield` 필수
- N개 case에 같은 동작 가능: `case 1, 2 -> "Value"`
장점: 코드 간결화, break 누락으로 인한 버그 방지, 가독성 향상.
```java
int menu = 2;

String message = switch (menu) {
    case 1 -> "주식 조회";
    case 2 -> {
        System.out.println("거래 로그 기록");
        System.out.println("DB 저장");
        yield "주식 매수"; // 다중 문장일 때 yield로 값 반환
    }
    case 3 -> "주식 매도";
    default -> "잘못된 선택";
};

System.out.println(message);
```
기존 방식 vs switch expression 비교:
```java
// 기존 방식
switch (channel) {
    case FACEBOOK: facebookLogin(); break;
    case KAKAO:    kakaoLogin();    break;
    ...
}

// switch expression
switch (channel) {
    case FACEBOOK -> facebookLogin();
    case KAKAO    -> kakaoLogin();
    case APPLE    -> appleLogin();
    case NAVER    -> naverLogin();
    case DEFAULT  -> defaultLogin();
}
```
---
### while
조건이 참인 동안 반복 실행함. 조건을 먼저 검사하므로 처음부터 조건이 거짓이면 한 번도 실행되지 않을 수 있음.
```java
int i = 1;
while (i <= 3) {
    System.out.println("잔고 확인: " + i + "번째");
    i++;
}
```
무한 루프 패턴: `while(true)`로 무한 반복하다가 특정 조건 충족 시 `break`로 탈출하는 구조로 자주 사용됨.
```java
while (true) {
    if (number <= 5) {
        System.out.println("무한루프탈출 " + number);
        break;
    }
    number = random.nextInt(100) + 1;
    System.out.println("현재 숫자 = " + number);
}
```
---
### do while
무조건 한 번은 실행되고, 이후 조건이 참이면 반복함. while과 달리 본문을 먼저 실행한 뒤 조건을 검사함.
```java
int count = 0;
do {
    System.out.println("거래 내역 조회 시도: " + count);
    count++;
} while (count < 2);
// 출력:
// 거래 내역 조회 시도: 0
// 거래 내역 조회 시도: 1
```
---
### for 반복문
반복 횟수가 정해진 상황에서 주로 사용하는 반복문임. 구조는 `for (초기식; 조건식; 증감식)` 형태임.
```java
for (int i = 1; i <= 5; i++) {
    System.out.println("주식 가격 확인: " + i + "일차");
}
```
- i가 1부터 시작해 5 이하일 동안 반복하며, 매 회 i를 1씩 증가시킴
- 반복 횟수가 명확할 때 가장 적합한 형태임
배열 전체를 순회할 때는 `students.length`를 조건식에 활용함. 배열 인덱스는 0부터 시작하므로 `i < length`가 맞는 조건임.
```java
for (int i = 0; i < students.length; i++) {
    System.out.println(students[i]);
}
```
---
### 중첩 for 반복문
for 반복문 안에 또 다른 for 반복문을 넣는 구조임. 이중 배열이나 행렬 형태의 출력에 유용함.
```java
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        System.out.print(i * j + " ");
    }
    System.out.println();  // 행 바꿈
}
```
- 바깥 루프(i)가 한 번 돌 때 안쪽 루프(j)가 9번 모두 수행됨
- `System.out.print`는 줄바꿈 없이 출력하고, 안쪽 루프 종료 후 `println()`으로 줄을 바꿔 구구단 형태로 출력됨
- 총 수행 횟수는 9 × 9 = 81회임
---
### for-each 문
배열이나 컬렉션의 모든 요소를 순서대로 꺼낼 때 쓰는 반복문임. 인덱스 변수를 직접 관리하지 않아도 돼 코드가 간결해짐.
전통적인 for 문과 비교하면 다음과 같음.
```java
// 전통적 for 문
for (int i = 0; i < students.length; i++) {
    System.out.println(students[i]);
}

// for-each 문
for (String student : students) {
    System.out.println(student);
}
```
- `for (타입 변수명 : 배열/컬렉션)` 형태로 선언함
- 매 반복마다 요소가 변수에 자동으로 담겨 나옴
for-each가 갖는 장점은 아래와 같음.
| 항목 | 특징 |
| --- | --- |
| 가독성 | 코드가 간결해짐 |
| 안정성 | 인덱스 범위를 벗어나는 실수(Index Out Of Bounds)를 문법적으로 차단 |
| 일관성 | 일반 배열(`String[]`)과 컬렉션(`ArrayList`, `HashSet`, `LinkedList` 등) 구분 없이 동일 문법 적용 가능 |
단, 인덱스 값이 직접 필요하거나 역방향 순회가 필요한 경우에는 전통적인 for 문을 사용해야 함.
---
### break
자신을 감싸고 있는 가장 가까운 반복문 또는 switch를 즉시 탈출하는 제어문임.
```java
for (int i = 1; i <= 10; i++) {
    if (i == 4) {
        break;
    }
    System.out.println("거래 횟수: " + i);
}
// 출력: 1, 2, 3 (i가 4가 되는 순간 루프 탈출)
```
중첩 반복문에서 일반 break는 가장 안쪽 루프만 탈출함. 바깥 루프까지 한 번에 탈출하려면 **Labeled Break**를 사용함.
```java
OUTER_LOOP:  // 바깥쪽 루프에 라벨을 붙임
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        if (i == 5 && j == 5) {
            break OUTER_LOOP;  // 바깥쪽 루프까지 바로 탈출
        }
    }
}
```
- 라벨은 탈출하고 싶은 루프 바로 위에 `이름:` 형태로 붙임
- `break 라벨명;` 실행 시 해당 라벨이 붙은 루프 전체를 탈출함
---
### continue
현재 회차의 루프 본문 나머지를 건너뛰고 다음 반복으로 바로 점프하는 제어문임. 루프 자체를 탈출하지는 않음.
```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    System.out.println("처리 중인 거래 번호: " + i);
}
// 출력: 1, 2, 4, 5 (i == 3인 회차만 println을 건너뜀)
```
- break와 달리 루프를 끝내지 않고, 해당 회차만 스킵함
- 특정 조건의 항목을 필터링할 때 유용함
---
### return
루프뿐만 아니라 해당 루프를 포함하는 **메서드 자체**를 즉시 종료함. break/continue와 달리 메서드 스코프 전체에서 빠져나옴.
```java
public static void checkNumber(int number) {
    for (int i = 1; i <= 10; i++) {
        if (i == number && i > 5) {
            return;  // 메서드 전체 종료
        }
        System.out.println("반복문 진행 중... 현재 값: " + i);
    }
    System.out.println("함수 끝자리에 있는 남은 로직 (정상 종료 시에만 출력됨)");
}
```
- `return` 실행 시 루프와 메서드 모두 종료되므로, 루프 이후의 코드도 실행되지 않음
- 반환값이 없는 `void` 메서드에서도 조기 종료 목적으로 `return;` 단독 사용 가능함
| 제어문 | 탈출 범위 |
| --- | --- |
| break | 가장 가까운 반복문 / switch |
| continue | 현재 회차만 스킵 (루프 유지) |
| return | 메서드 전체 종료 |
---
### 예외 처리 — throw / throws
예외(Exception)를 직접 발생시키거나, 메서드가 예외를 발생시킬 수 있음을 선언할 때 사용함.
```java
public static void buyStock(int amount) throws Exception {
    if (amount <= 0) {
        throw new Exception("매수 금액은 0보다 커야 합니다.");
    }
}
```
두 키워드의 역할이 다름.
- **throws** : 메서드 시그니처에 붙이며, 이 메서드가 해당 예외를 발생시킬 수 있음을 선언함. 호출하는 쪽에서 try-catch로 받아야 함
- **throw** : 메서드 본문 안에서 예외 객체를 실제로 던지고 즉시 탈출함
---
### 예외 처리 — try-catch
예외 발생 시 프로그램이 비정상 종료되지 않도록 예외를 잡아 처리하는 구문임.
```java
try {
    buyStock(-500);  // 예외 발생 → catch 블록으로 점프
    System.out.println("주식 매수가 성공적으로 완료되었습니다.");  // 실행 안 됨

} catch (Exception e) {
    System.out.println("매수 실패 오류: " + e.getMessage());  // throw 시 담긴 메시지 출력

} finally {
    System.out.println("주식 거래 프로세스 종료");  // 예외 여부 무관하게 항상 실행
}
```
- try 블록에서 예외가 발생하면 이후 코드는 건너뛰고 즉시 catch로 이동함
- `e.getMessage()`는 `throw new Exception("...")`에 담은 메시지를 꺼내는 메서드임
- **finally** 블록은 예외 발생 여부와 무관하게 무조건 실행됨. 자원 해제·로깅 등 마무리 처리에 활용함
---
### 예외 처리 — try-with-resources
**외부 자원(External Resource)** 을 사용할 때 반드시 `close()`를 호출해 자원을 반납해야 함. Socket, File, DB Connection 등은 JVM이 아닌 OS가 FD(File Descriptor)를 발급하는 자원이기 때문임.
`close()`를 finally에서 수동으로 처리하면 각 자원마다 별도 try-catch가 필요해 코드가 매우 복잡해짐. 미 해지 시 아래 문제가 발생함.
- Socket port 고갈
- Too Many Open File
- Memory Leak
**try-with-resources** 는 자원을 try 괄호 안에 선언하면 블록 종료 시 자동으로 `close()`를 호출해 주는 문법임.
```java
// 기본 구조
try (자원 선언1; 자원 선언2; ...) {
// 자원을 사용하는 코드
} catch (예외타입 e) {
// 예외 처리
}
```
```java
// 실제 사용 예시
try (
    Socket client = serverSocket.accept();
    InputStream in = client.getInputStream();
    OutputStream out = client.getOutputStream()
) {
// ...
} catch (IOException e) {
    e.printStackTrace();
}
// try 블록 종료 시 out → in → client 역순으로 자동 close()
```
- finally에서 수동으로 null 체크 후 close하던 번거로운 코드가 사라짐
- 선언 순서의 역순으로 close()가 호출됨
Stream 관련 보충 개념: **Stream**은 바이트(byte) 단위 입출력을 의미하며, `InputStream`은 바이트를 읽어 문자/스트링으로 변환하고, `OutputStream`은 문자/스트링을 바이트로 변환해 출력함.
---
### \[참고\] Custom Exception
기본 제공 예외 타입만으로는 도메인별 예외 상황을 명확히 구분하기 어려울 때, `Exception`을 상속해 직접 예외 클래스를 만들 수 있음.
```java
public class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
    public CustomException(String message, Throwable cause) {
        super(message, cause);
    }
}
```
- 생성자에서 `super(message)`를 호출해 부모 클래스인 `Exception`에 메시지를 전달함
- `Throwable cause`를 받는 생성자는 다른 예외가 원인이 된 경우 원인 예외를 함께 연결(chaining)할 때 사용함
```java
public static void buyStock(int amount) throws CustomException {
    if (amount <= 0) {
        throw new CustomException("매수 금액은 0보다 커야 합니다.");
    }
}
```
- `throws Exception` 대신 `throws CustomException`으로 선언하면, 호출하는 쪽에서 어떤 종류의 예외인지 시그니처만 보고도 파악 가능함
- 예외 타입별로 catch 블록을 분리할 수 있어 처리 로직을 세밀하게 구분할 수 있음
---
### Java의 패키지 (Package)
관련 있는 클래스들을 논리적으로 묶는 단위임. 실제 파일 시스템의 폴더 구조와 1:1로 대응하며, 클래스 이름 충돌 방지, 접근 범위 관리, 재사용성 향상의 역할을 함.
```java
package com.skala.stock;  // 소스 코드 상단에 패키지 선언
```
위 선언은 해당 클래스 파일이 `com/skala/stock/` 폴더 안에 위치함을 의미함. 같은 이름의 클래스라도 패키지가 다르면 충돌하지 않음.
```plain text
com/
└── skala/
    ├── stock/
    │   └── Stock.java
    └── player/
        └── Player.java
```
- Maven/Gradle 프로젝트에서는 패키지 루트가 `/src/main/java`부터 시작함
---
### 접근 제어자
클래스, 메서드, 필드, 생성자 등에 외부에서 접근할 수 있는 범위(가시성)를 제어하는 키워드임. OOP의 정보 은닉(encapsulation)을 구현하는 핵심 수단임.
| 접근 제어자 | 같은 클래스 | 같은 패키지 | 자식 클래스 | 외부 클래스 |
| --- | --- | --- | --- | --- |
| public | ✅ | ✅ | ✅ | ✅ |
| protected | ✅ | ✅ | ✅ | ❌ |
| (default) | ✅ | ✅ | ❌ | ❌ |
| private | ✅ | ❌ | ❌ | ❌ |
- **default** : 접근 제어자를 아무것도 명시하지 않은 상태. package-private이라고도 부르며, 같은 패키지 안에서만 접근 가능함
- **protected** : 같은 패키지 또는 상속받은(자식) 클래스에서 접근 가능함. 다른 패키지의 비상속 클래스는 접근 불가
---
### 패키지와 접근 제어자의 연결
접근 제어자가 패키지 경계를 기준으로 어떻게 작동하는지를 정리하면 아래와 같음.
| 접근 제어자 | 설명 | 패키지 간 접근 |
| --- | --- | --- |
| public | 모든 패키지에서 접근 가능 | ✅ |
| protected | 같은 패키지 + 다른 패키지의 하위 클래스에서 접근 가능 | ⭕ (상속관계만) |
| (default) | 같은 패키지에서만 접근 가능 (접근 제어자 생략) | ❌ |
| private | 같은 클래스 내부에서만 접근 가능 | ❌ |
아래는 default 접근 제어자가 패키지 경계에서 어떻게 막히는지 보여주는 예시임.
```java
// skala.domain 패키지
package skala.domain;

class Stock {
    String name = "스칼라 AI";  // default 접근 제어자
}
```
```java
// skala 패키지 (다른 패키지)
package skala;

import skala.domain.Stock;

public class Player {
    public static void main(String[] args) {
        Stock s = new Stock();
        System.out.println(s.name);  // 컴파일 오류 — default 필드는 다른 패키지에서 접근 불가
    }
}
```
- `Stock` 클래스 자체도 `class Stock`으로 선언돼 default이므로, `import`는 됐더라도 `s.name` 접근 시 컴파일 오류가 발생함
- 다른 패키지에서 자유롭게 사용하려면 클래스와 필드 모두 `public`으로 선언해야 함
---
### Java 필수 클래스 개요
주로 `java.lang` 패키지에 포함되어 있으며, 별도 import 없이 사용할 수 있는 핵심 클래스들임.
| 클래스 | 역할 |
| --- | --- |
| Object | 모든 클래스의 부모. `toString()`, `equals()` 등 객체 기본 기능 이해 필수 |
| System | 콘솔 입출력, 시간 측정, 시스템 종료 등 시스템 관련 기능 제공 |
| Thread | 동시성 처리. `start()`, `sleep()`, `join()` 등 멀티스레드 기초 |
| Exception | 예외 처리의 최상위 클래스. try-catch와 함께 사용 |
| Runtime | JVM 자체를 다루는 클래스. 메모리 정보, GC, 외부 프로세스 실행 |
| Class | 클래스 자체를 다루는 메타 클래스. 리플렉션의 핵심 |
---
### Object 클래스
Java의 모든 클래스는 명시적으로 상속을 선언하지 않아도 **Object를 암묵적으로 상속**함. 객체의 가장 기본적인 동작을 정의하는 뿌리 클래스임.
자주 재정의(Override)하는 메서드는 다음 세 가지임.
- `toString()` : 객체를 문자열로 표현. `System.out.println(객체)` 호출 시 자동으로 사용됨
- `equals()` : 객체의 동등성 비교. 재정의하지 않으면 참조값(주소)을 비교함
- `hashCode()` : 해시값 반환. HashMap, HashSet 등 컬렉션에서 키 비교 시 사용됨
```java
public class Stock {
    String name;

    public Stock(String name) { this.name = name; }

    @Override
    public String toString() {
        return "Stock[name=" + name + "]";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Stock) {
            Stock other = (Stock) obj;
            return this.name.equals(other.name);
        }
        return false;
    }
}
```
```java
Stock s1 = new Stock("SKALA");
Stock s2 = new Stock("SKALA");

System.out.println(s1);            // toString() 호출 → Stock[name=SKALA]
System.out.println(s1.equals(s2)); // equals() 재정의 → true
```
- `equals()`를 재정의하지 않으면 s1과 s2는 서로 다른 객체 주소를 가지므로 `false`가 반환됨
- `equals()`를 재정의할 때는 `hashCode()`도 함께 재정의하는 것이 원칙임 (컬렉션 오작동 방지)
---
### System 클래스
표준 입출력, 환경정보 접근, 시간 측정, 프로그램 종료 등 시스템 관련 기능을 정적(static) 메서드로 제공함. 인스턴스를 생성하지 않고 바로 사용함.
```java
System.out.println("스칼라에 오신 것을 환영합니다.");

long start = System.currentTimeMillis();       // 현재 시간(ms) 조회
for (int i = 0; i < 1000000; i++) {}           // 더미 연산
long end = System.currentTimeMillis();

System.out.println("걸린 시간: " + (end - start) + "ms");

// System.exit(0);  // 프로그램 강제 종료 (0 = 정상 종료)
```
- `System.currentTimeMillis()` : 유닉스 에포크(1970-01-01)로부터 현재까지의 밀리초 반환. 구간 성능 측정에 자주 씀
- `System.exit(0)` : JVM 전체를 종료함. 0은 정상 종료, 그 외 값은 비정상 종료를 의미함
---
### Thread 클래스
동시성 처리를 위한 클래스임. 별도의 실행 흐름(스레드)을 만들어 메인 스레드와 병렬로 작업을 수행할 수 있음.
```java
Thread t = new Thread(() -> {  // 람다로 실행할 작업 정의
    try {
        Thread.sleep(1000);    // 1초 일시정지 (ms 단위)
        System.out.println("1초 후에 실행되는 작업");
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
});

t.start();                          // 새 스레드 시작
System.out.println("메인 스레드 종료");  // 새 스레드와 무관하게 즉시 출력됨
```
주요 메서드 정리.
- `start()` : 새 스레드를 실행함. `run()`을 직접 호출하면 새 스레드가 아닌 현재 스레드에서 실행됨
- `sleep(ms)` : 현재 스레드를 지정한 시간(ms)만큼 일시정지. `InterruptedException` 처리 필요
- `join()` : 해당 스레드가 종료될 때까지 호출한 스레드가 대기함
`join()`을 호출하지 않으면 main이 먼저 종료돼도 JVM은 살아있는 스레드가 끝날 때까지 대기함.
---
### Exception 클래스
예외 처리 계층의 최상위 클래스임. 예외를 처리하지 않으면 프로그램은 강제 종료됨.
```java
try {
    int result = 10 / 0;  // ArithmeticException 발생
} catch (Exception e) {
    System.out.println("예외 발생: " + e.getMessage());  // 메시지 출력
    e.printStackTrace();  // 스택 트레이스 출력 (디버깅용)
}
```
예외 클래스의 계층 구조는 다음과 같음.
```plain text
Throwable
├── Error                          (JVM 수준 오류, 복구 불가)
└── Exception
    ├── RuntimeException           (Unchecked — 컴파일러가 강제하지 않음)
    └── Non-RuntimeException       (Checked — 반드시 처리 필요)
```
---
### \[참고\] Checked vs Unchecked Exception
| 구분 | Non-RuntimeException (Checked) | RuntimeException (Unchecked) |
| --- | --- | --- |
| 발생 원인 | 외부 환경 문제 (파일, 네트워크, DB 등) | 개발자 실수, 잘못된 로직/데이터 |
| 복구 가능성 | 높음 (recoverable) | 낮음 |
| 컴파일러 강제 | 반드시 try-catch 또는 throws 선언 필요 | 강제하지 않음 |
| 대표 예시 | `IOException`, `SQLException`, `ClassNotFoundException`, `FileNotFoundException`, `InterruptedException` | `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`, `IllegalArgumentException`, `ClassCastException` |
Checked Exception을 강제하는 이유는 세 가지임.
- 파일, 네트워크, DB 같은 외부 리소스 문제는 언제든 발생할 수 있어 **복구 가능성이 높음**
- 처리하지 않으면 앱이 중단될 수 있으므로 **미처리 시 비정상 종료**가 발생함
- Java는 안정성을 중요시하며, 외부 자원 접근을 안전하게 처리하도록 강제하는 **언어 설계 철학**을 따름
---
### Runtime 클래스
JVM 자체와 상호작용하는 클래스임. `new`로 생성하지 않고 `Runtime.getRuntime()`으로 싱글톤 인스턴스를 얻어 사용함.
```java
Runtime rt = Runtime.getRuntime();

System.out.println("메모리 사용 전: " + rt.freeMemory());

int[] bigArray = new int[1000000];
System.out.println("메모리 사용 후: " + rt.freeMemory());

bigArray = null;
System.gc();  // 가비지 컬렉션 요청 (즉시 실행 보장은 아님)

System.out.println("GC 후: " + rt.freeMemory());
```
- `freeMemory()` : JVM 힙에서 현재 사용 가능한 여유 메모리(byte) 반환
- `System.gc()` : GC 실행을 JVM에 요청함. 실제 실행 시점은 JVM이 결정함
---
### Class 클래스
자바 클래스 자체를 객체로 다루는 메타 클래스임. **리플렉션(reflection)** 의 핵심으로, 런타임에 클래스 정보(이름, 부모 클래스, 메서드, 필드 등)를 동적으로 조회할 수 있음.
```java
String skala = "스칼라";
Class<?> clazz = skala.getClass();  // String 객체로부터 Class 정보 획득

System.out.println("클래스 이름: " + clazz.getName());         // java.lang.String
System.out.println("슈퍼 클래스: " + clazz.getSuperclass());   // java.lang.Object
```
- `getClass()` : 인스턴스에서 Class 객체를 얻는 방법
- `Class.forName("패키지.클래스명")` : 클래스 이름 문자열로 Class 객체를 얻는 방법. 동적 로딩에 사용됨
- `Class<?>` 의 `?`는 와일드카드 제네릭으로, 어떤 타입의 클래스든 담을 수 있음을 의미함
---
### 객체 (Object) 란?
어떤 행동을 하는 쪽이 **주체**라면, 그 행동의 영향을 받거나 향하는 대상이 **객체**임. 예를 들어 "사람이 상품을 주문한다"에서 사람은 주체, 상품은 객체임.
객체는 메시지를 받고, 역할(책임)을 수행하며, 그 결과로 상태를 변경하거나 응답을 반환함. 은행직원 예시로 풀면 다음과 같음.
- 고객 → 주체, 은행직원 → 객체, 계좌 개설 → 행동(Behavior)
- 은행직원의 상태(속성): 직원 번호, 이름, 소속지점, 계좌 개설 권한 여부 등
| 객체 | 요청/자극 | Behavior | 속성 |
| --- | --- | --- | --- |
| 문 | 손잡이를 돌리고 민다 | 열린다 | 색상, 재질, 잠금 상태 |
| 자동차 | 가속 페달을 밟는다 | 속도를 낸다 | 색상, 속도, 연료량 |
| 사람 | 이름을 부른다 | 대답한다 | 이름, 나이, 성별, 직업 |
| 엘리베이터 | 버튼을 누른다 | 해당 층으로 이동한다 | 현재층, 운행상태, 수용인원 |
객체는 행동/책임(Methods)과 속성(Data)을 하나로 묶는 **캡슐화(Encapsulation)** 의 단위임. 즉, 객체 = 행위(method) + 상태(attribute).
역할(Role) = 책임(Responsibility) + 내부 정보(Info)로 분해되며, 이것이 코드에서 객체 = 행위 + 상태로 구체화됨.
---
### 좋은 설계란? — Cohesion & Coupling
좋은 설계의 목표는 **높은 응집도(cohesion) + 낮은 결합도(coupling)** 임.
- **응집도(Cohesion)** : 하나의 객체가 하나의 역할/책임에 집중하는 정도. 응집도가 낮으면 너무 많은 기능이 뒤섞여 수정 시 예상치 못한 부분까지 영향을 받음
- **결합도(Coupling)** : 객체 간 의존 정도. 결합도가 높으면 한 객체를 수정할 때 연관된 다른 객체들도 줄줄이 수정해야 함
나쁜 설계는 기능/역할이 섞이고 강하게 결합된 형태(낮은 응집도 + 높은 결합도)이고, 좋은 설계는 역할과 책임을 분리하고 명확한 인터페이스로 연결한 형태(높은 응집도 + 낮은 결합도)임.
---
### 객체지향 프로그래밍 (OOP)
시스템을 역할(Role)과 책임(Responsibility) 중심으로 객체(Object)로 모델링하여, 높은 응집도와 낮은 결합도를 통해 유지보수성과 확장성을 향상시키는 프로그래밍 패러다임임.
응집도를 높이는 원칙: **Single-Responsibility Principle** (단일 책임 원칙)
결합도를 낮추는 원칙: **Dependency-Inversion Principle** (제어 역전 원칙)
---
### OOP의 핵심 특징 4가지
- **캡슐화 (Encapsulation)** — 높은 응집도: What을 설명하는 Behavior(Method)만 외부에 노출하고, 상세 구현과 속성은 숨김. 내부 구현을 변경해도 외부에 영향을 주지 않아 유지보수가 용이하고, 외부에서 내부 데이터를 직접 조작하는 것을 방지함
- **추상화 (Abstraction)** — 낮은 결합도: 인터페이스와 구현을 분리하여 향후 부품을 쉽게 교체 가능하게 함. 시스템 복잡도를 낮추고 상호 운영성을 높임
- **상속 (Inheritance)** — 중복 제거: 부모 클래스의 특성을 자식 클래스가 물려받아 재사용성을 높임. 공통 기능을 부모 클래스 한 곳에서만 수정하면 모든 자식 클래스에 자동 반영됨
- **다형성 (Polymorphism)** — 낮은 결합도: 동일 인터페이스 호출 시 상속 관계의 다른 객체들이 각자의 방식으로 동작함. 기존 클라이언트 코드를 전혀 수정하지 않고 새로운 클래스를 쉽게 추가 가능함
---
### Java 기반 OOP — 캡슐화 (Encapsulation)
객체의 속성(필드)을 외부에서 직접 접근하지 못하도록 숨기고, 공개된 getter/setter 메서드를 통해서만 간접적으로 접근하게 하는 것임. 실무에서는 대부분 **Lombok**을 사용해 getter/setter를 자동 생성함.
```java
public class Stock {
    private double price;  // 필드는 private으로 숨김

    public int getPrice() {           // getter로 읽기 제공
        return this.price;
    }

    public void setPrice(double price) {  // setter에 유효성 검사 추가
        if (price > 0) {
            this.price += price;
        } else {
            System.out.println("에러: 0원 이하 가격은 설정 불가");
        }
    }
}
```
필드 공개 방식 vs 캡슐화 방식 비교.
| 항목 | public 필드 직접 접근 | private + getter/setter |
| --- | --- | --- |
| 유효성 검사 | 불가 | setter에 검사 로직 가능 |
| 데이터 보호 | 불안전 | 안전 (변경 제어 가능) |
| 유지보수 | 변경 시 외부 코드 모두 영향 | 내부 변경 시 외부 영향 최소화 |
| OOP 원칙 | 객체지향 위반 | 정보 은닉 원칙 충실 |
---
### Java 기반 OOP — 상속 (Inheritance)
기존(부모) 클래스의 속성과 메서드를 새로운(자식) 클래스가 물려받아 사용하는 개념임. `extends` 키워드로 구현하며, 자식 생성자에서 `super()`로 부모 생성자를 호출해야 함. 상속 시 부모 필드는 `protected`로 선언해 자식 클래스에서 접근 가능하게 함.
```java
// 부모 클래스
public class Stock {
    protected String name;
    protected double price;

    public Stock(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public void printInfo() {
        System.out.println("[일반주] 종목: " + name + ", 가격: " + price + "원");
    }
}

// 자식 클래스
public class PreferredStock extends Stock {
    private double dividendRate;

    public PreferredStock(String name, double price, double dividendRate) {
        super(name, price);  // 부모 생성자 호출
        this.dividendRate = dividendRate;
    }
}
```
---
### Java 기반 OOP — 추상화 (Abstraction)
복잡한 시스템에서 핵심 개념만 추출하고, 불필요한 세부사항은 숨기는 것임. Java에서는 `abstract class` 또는 `interface`로 구현함.
| 항목 | abstract class | interface |
| --- | --- | --- |
| 용도 | 상태와 일부 공통 구현을 자식과 공유 | 동작 규약만 선언 (구현 없음) |
| 다중 상속 | 불가 | 가능 |
| 필드 | 인스턴스 변수, 생성자 포함 가능 | 상수만 가능 (`public static final`) |
| 메서드 | 일부 구현 가능 | `default`, `static` 메서드 구현 가능 |
```java
// abstract class
abstract class Asset {
    protected String name;
    protected double price;

    public Asset(String name, double price) { ... }

    public abstract void printInfo();  // 자식이 반드시 구현해야 함
}

// interface
public interface Valuable {
    void printInfo();  // 구현 없이 시그니처만 선언
}
```
---
### Java 기반 OOP — 다형성 (Polymorphism)
하나의 타입으로 여러 형태의 동작을 표현할 수 있는 능력임. 같은 메서드 호출이라도 객체의 실제 타입에 따라 다르게 동작함.
| 구분 | 설명 |
| --- | --- |
| 오버라이딩 (Overriding) | 자식 클래스가 부모의 메서드를 재정의. 런타임에 실제 타입으로 결정됨 |
| 오버로딩 (Overloading) | 동일 클래스에서 같은 이름, 다른 매개변수의 메서드를 여러 개 정의 |
```java
class Human {
    void introduce() { System.out.println("저의 이름은 " + name + "입니다"); }
}

class Student extends Human {
    @Override
    void introduce() {                      // 오버라이딩
        System.out.println("저의 이름은 " + name + "이고, 학생 Id는 " + studentId + "입니다");
    }

    void introduce(Integer myId) {          // 오버로딩 (매개변수 타입이 다름)
        System.out.println("저의 이름은 " + name + "이고, 나의 Id는 " + myId + "입니다");
    }
}
```
---
### Java 기반 OOP — 업캐스팅 (Upcasting)
자식 객체를 부모 타입 변수에 담는 것임. 자동으로 처리되며 별도 캐스팅 문법이 필요 없음.
```java
Stock s = new PreferredStock();   // 업캐스팅 — 자동

s.printInfo();        // 자식의 오버라이딩된 메서드가 실행됨 (런타임 다형성)
s.showDividend();     // 컴파일 오류 — 부모 타입에 존재하지 않는 메서드는 보이지 않음

// 다운캐스팅 (다시 자식 타입으로 되돌리기)
if (s instanceof PreferredStock) {
    PreferredStock ps = (PreferredStock) s;
    ps.dividendRate = 5.0;
    ps.showDividend();  // 가능
}
```
업캐스팅을 쓰는 이유는 **사용(Client)과 구현(Implementation)을 분리**하기 위함임. 아래 예시처럼 `pressPowerButton`은 부모 타입(`ElectronicProduct`)만 받으므로, TV든 오디오든 새 제품이 추가되어도 이 메서드를 수정할 필요가 없음.
```java
static void pressPowerButton(ElectronicProduct product) {
    product.turnOn();  // 실제 타입에 따라 TV 또는 오디오의 turnOn()이 실행됨
}

pressPowerButton(new Television());  // TV 화면이 켜짐
pressPowerButton(new Audio());       // 오디오에서 음악 출력
```
---
### \[참고\] 절차적 vs 객체지향 프로그래밍
| 구분 | 절차적 프로그래밍 | 객체지향 프로그래밍 |
| --- | --- | --- |
| 구조 | 함수 중심 | 클래스/객체 중심 |
| 데이터 처리 | 데이터와 함수를 분리 | 데이터를 객체 내부에서 캡슐화 |
| 재사용성 | 함수 재사용 | 클래스/객체 단위 재사용 및 상속 |
| 유지보수성 | 복잡한 프로그램에서 어려움 | 캡슐화, 상속, 다형성으로 용이 |
| 실행 흐름 | 위에서 아래로 순차적 | 객체 간 메시지 전달로 흐름 제어 |
| 성능 | 상대적으로 단순하고 빠름 | 객체 생성 및 메서드 호출 오버헤드 존재 |
| 대표 언어 | C, Pascal, Fortran | Java, C++, Python, C# |
---
### \[참고\] static 클래스, 변수, 메서드
`static` 키워드는 객체(인스턴스)가 아닌 **클래스 자체에 속하는** 변수나 메서드를 정의할 때 사용함. 인스턴스를 생성하지 않아도 클래스 이름으로 바로 접근할 수 있음.
```java
static class Example {
    public static final int INITIAL_COUNT = 10;  // 상수 — Metaspace 상수 풀에 존재
    private static int count = 0;                // 클래스 변수 — 모든 인스턴스가 공유
    private int instanceId;                      // 인스턴스 변수 — 객체마다 독립

    Example() {
        count++;
        instanceId = count + INITIAL_COUNT;      // 생성될 때마다 고유 ID 부여
    }

    public static int getCount() { return count; }
    public static int getLastInstanceId() { return count + INITIAL_COUNT; }
    public int getInstanceId() { return instanceId; }
}
```
```java
Example e1 = new Example();  // count = 1, instanceId = 11
Example e2 = new Example();  // count = 2, instanceId = 12
Example e3 = new Example();  // count = 3, instanceId = 13

System.out.println(Example.getCount());           // 3 — 클래스 변수이므로 클래스 이름으로 접근
System.out.println(Example.getLastInstanceId());  // 13
System.out.println(e1.getInstanceId());           // 11 — 인스턴스 변수이므로 객체로 접근
```
- `static` 변수는 Metaspace(클래스 메타데이터 영역)에 저장되어 모든 인스턴스가 공유함
- `static` 메서드 안에서는 `this`나 인스턴스 변수에 접근할 수 없음 (인스턴스에 속하지 않으므로)
---
### \[참고\] 설계 추상화 단위의 확장
소프트웨어 설계의 추상화 단위는 시대와 요구사항에 따라 점진적으로 확장되어 왔음. 각 단계는 이전 단계의 한계를 보완하는 방향으로 발전함.
- 절차적 (함수): 함수 단위로 로직을 분리하지만, 코드 중복과 날코딩(ad-hoc 구현)이 발생하기 쉬움
- 객체지향 (OOP): 클래스/객체 단위로 코드를 재사용하고, 패턴을 통해 변경 영향을 최소화함
- 컴포넌트 기반 (CBD): OOP보다 큰 단위인 컴포넌트 단위로 재사용하고, 변경 영향을 격리함
- 서비스 지향 아키텍처 (SOA): 컴포넌트를 독립 실행 단위인 서비스로 확장하고, 서비스 통합에 초점을 맞춤
- 마이크로서비스 아키텍처 (MSA): 서비스를 더욱 작게 쪼개 빠른 개발과 빠른 변화 대응을 가능하게 함
MSA에서는 도메인별로 패키지 구조를 분리하는 것이 일반적임. 아래는 그 예시임.
```plain text
com.example
├── order
│   ├── api          (OrderController, DTO)
│   ├── application  (OrderService/UseCase)
│   ├── domain       (Order, OrderItem, Policy, Event)
│   └── infra        (JpaOrderRepository, FeignClient, Outbox 등)
├── payment
│   ├── api
│   ├── application
│   ├── domain
│   └── infra
└── shipping
    ├── api
    ├── application
    ├── domain
    └── infra
```
- 도메인(order, payment, shipping)별로 완전히 수직 분리된 구조임
- 각 도메인 내에서 api → application → domain → infra의 계층을 따로 가짐
- 이 구조는 한 도메인의 변경이 다른 도메인에 영향을 주지 않도록 경계를 명확히 하는 것이 목적임
---
<empty-block/>
