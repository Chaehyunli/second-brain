---
title: "대규모 백엔드 인프라 아키텍처 및 배포 전략 - Ngnix, Load Balancer, 웹/앱"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "load balancer", "ngnix", "배포"]
category: "기타"
published: 2026-06-12
source_url: https://ch010104.tistory.com/284
---

# 대규모 백엔드 인프라 아키텍처 및 배포 전략 - Ngnix, Load Balancer, 웹/앱

## 원문

https://ch010104.tistory.com/284

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

초기 서비스는 단일 서버(Single Server)로 시작하지만, 트래픽 폭주 시 서버의 사양을 높이는 스케일 업(Scale-Up)에는 물리적/비용적 한계가 존재합니다. 이를 해결하기 위해 똑같은 애플리케이션 서버를 여러 대 복제하여 트래픽을 나누어 처리하는 수평 확장(Scale-Out) 아키텍처를 도입하며, 인프라는 거대한 분산 시스템으로 진화합니다.

로드 밸런서는 하나의 공인 주소(Domain/IP)로 들어오는 수많은 사용자의 요청을 뒤에 대기 중인 여러 대의 백엔드 서버(K대)로 균등하게 분배해 주는 최전선 문지기이자 트래픽 지휘관입니다.

## 원문 기반 개념 정리

### 1. 대규모 백엔드 인프라 아키텍처: 트래픽 분산과 동기화

초기 서비스는 단일 서버(Single Server)로 시작하지만, 트래픽 폭주 시 서버의 사양을 높이는 스케일 업(Scale-Up)에는 물리적/비용적 한계가 존재합니다. 이를 해결하기 위해 똑같은 애플리케이션 서버를 여러 대 복제하여 트래픽을 나누어 처리하는 수평 확장(Scale-Out) 아키텍처를 도입하며, 인프라는 거대한 분산 시스템으로 진화합니다.

### 1.1. 로드 밸런서 (Load Balancer)와 Nginx 심화

로드 밸런서는 하나의 공인 주소(Domain/IP)로 들어오는 수많은 사용자의 요청을 뒤에 대기 중인 여러 대의 백엔드 서버(K대)로 균등하게 분배해 주는 최전선 문지기이자 트래픽 지휘관입니다.

### L4 vs L7 로드 밸런서

L4 로드 밸런서 (네트워크/전송 계층): IP 주소와 포트(Port) 번호만 보고 트래픽을 분산합니다. 패킷의 내용물을 열어보지 않으므로 연산 속도가 매우 빠르고 효율적입니다.

L7 로드 밸런서 (애플리케이션 계층): HTTP 헤더, 쿠키, URL 경로(Path), 페이로드 등을 분석하여 지능적으로 라우팅합니다. (예: /api/users는 유저 서버로, /api/payments는 결제 서버로 분산). Nginx, AWS ALB(Application Load Balancer)가 대표적입니다.

### 💡 Nginx 로드 밸런싱 및 헬스 체크 설정 (nginx.conf)

Nginx를 리버스 프록시(Reverse Proxy) 및 로드 밸런서로 사용할 때, 단순히 트래픽만 나누는 것이 아니라 장애가 발생한 서버를 격리(Health Check)하고 가중치(Weight)를 부여할 수 있습니다.

```text
http {
    # 백엔드 서버 그룹 (Upstream) 정의
    upstream my_backend_servers {
        # 1. 라운드 로빈 (기본값): 순서대로 분배
        # 2. least_conn: 현재 연결 수가 가장 적은 한가한 서버로 분배
        # 3. ip_hash: 클라이언트 IP를 해싱하여 항상 동일한 서버로 접속 보장 (세션 유지에 유리)
        least_conn;

        # weight: 서버 사양에 따라 가중치 부여 (8081 서버에 3배 더 많은 트래픽 할당)
        # max_fails / fail_timeout: 10초 동안 3번 응답이 없으면 해당 서버를 죽은 것으로 간주하고 트래픽 차단
        server 127.0.0.1:8081 weight=3 max_fails=3 fail_timeout=10s;
        server 127.0.0.1:8082 weight=1 max_fails=3 fail_timeout=10s;
        server 127.0.0.1:8083 backup; # 다른 서버가 모두 죽었을 때만 작동하는 예비 서버
    }

    server {
        listen 80;
        server_name api.myservice.com;

        location / {
            proxy_pass http://my_backend_servers;

            # 클라이언트의 진짜 IP와 프로토콜 정보를 백엔드 서버에 전달 (X-Forwarded 헤더)
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

[무중단 배포 메커니즘] 8081 서버의 코드를 교체하기 위해 프로세스를 종료하면, Nginx의 max_fails 설정이 이를 즉각 감지하여 8082 서버로만 트래픽을 우회시킵니다. 업데이트가 완료되어 8081 서버가 다시 켜지면 트래픽 분산이 자동으로 재개되어 사용자 입장에서는 서비스가 단 1초도 끊기지 않습니다.

### 1.2. Docker 기반 다중 컨테이너 배포 (Docker Compose)

분산 환경을 물리적 서버에 일일이 세팅하는 것은 비효율적입니다. Docker를 활용하면 Nginx와 수많은 백엔드 서버를 도커 브릿지 네트워크(Bridge Network)라는 격리된 가상 망으로 묶어, IP 대신 컨테이너 이름으로 통신하는 깔끔한 아키텍처를 구축할 수 있습니다.

### 💡 실무형 docker-compose.yml 상세 예시

```text
version: '3.8'

services:
  # 1. 백엔드 서버 1번 (App Container)
  backend-app-1:
    image: my-spring-boot-app:latest
    container_name: web-app-1
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - DB_HOST=master-db # 내부 DNS를 통해 DB 컨테이너 이름으로 맵핑
      - REDIS_HOST=redis-cluster
    networks:
      - my-network

  # 2. 백엔드 서버 2번 (App Container)
  backend-app-2:
    image: my-spring-boot-app:latest
    container_name: web-app-2
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - DB_HOST=master-db
      - REDIS_HOST=redis-cluster
    networks:
      - my-network

  # 3. 최전선 Nginx 로드 밸런서
  nginx-loader:
    image: nginx:1.21-alpine
    container_name: nginx-gateway
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro # 호스트의 설정 파일을 읽기 전용으로 마운트
      - ./certs:/etc/nginx/certs # HTTPS 인증서 마운트
    depends_on:
      - backend-app-1
      - backend-app-2
    networks:
      - my-network

networks:
  # 컨테이너들끼리 통신할 가상 네트워크 정의
  my-network:
    driver: bridge
```

이 환경에서는 nginx.conf 내부의 upstream 블록을 server web-app-1:8080; 처럼 작성할 수 있습니다. 도커 내장 DNS가 컨테이너 이름을 해당 컨테이너의 내부 IP로 자동 변환해주기 때문입니다.

### 1.3. 대용량 트래픽 처리의 정석: K : N : M 분산 아키텍처

트래픽을 견디기 위해 백엔드 서버 1개를 복사할 때, 묶여있는 DB와 Redis까지 통째로 세트로 늘리는 것은 데이터 동기화의 재앙을 초래합니다. 현업에서는 각 컴포넌트의 역할과 특징에 맞게 독립적인 클러스터 그룹을 형성하여 수평 확장합니다.

### 1) 백엔드 서버 그룹 (K대) : 무상태성(Stateless) 일꾼

Stateless 구조: 서버 내부에 사용자 세션(로그인 상태)이나 중요 데이터를 저장하지 않습니다. 서버가 $K$대로 분산되어 있기 때문에, 1번 서버에 로그인한 유저가 다음 요청 시 2번 서버로 배정되면 로그아웃 처리되는 '세션 불일치' 문제가 발생하기 때문입니다.

해결책: 세션 정보는 JWT(JSON Web Token)로 클라이언트에 맡기거나, 모든 서버가 공유하는 Redis 세션 스토어에 저장하여 서버 자신은 언제든 죽고 새로 태어나도 문제없는 순수한 연산 장치로 만듭니다.

### 2) Redis 클러스터 그룹 (N대) : 동시성 제어 및 초고속 캐시

동시성 제어 (Distributed Lock): K대의 서버가 동시에 DB의 재고를 차감하려고 할 때 발생하는 경합(Race Condition)을 방지합니다.

자바의 synchronized는 단일 서버 메모리에서만 동작하므로, 분산 환경에서는 모든 서버가 공통으로 바라보는 Redis를 이용해 분산 락을 구현합니다.

구현 원리: Redis의 원자적 연산인 SETNX (Set if Not Exists)를 활용하거나, Redisson 라이브러리의 Pub/Sub 기능을 활용해 스레드 대기 부하 없이 락을 획득/반환합니다.

캐싱 (Caching): DB 디스크 I/O를 줄이기 위해 자주 조회되는 데이터(이벤트 배너, 상품 목록)를 메모리 단에 저장합니다. (Look-aside, Write-through 전략 등 활용)

Redis 고가용성 구성: 레디스 자체의 장애를 막기 위해 데이터가 동기화되는 Master-Slave 구조를 띄우고, Sentinel(감시자) 컨테이너를 배치하여 Master가 죽으면 즉각 Slave를 Master로 승격(Failover)시킵니다. 극단적인 대용량 데이터는 Redis Cluster(샤딩) 구조로 쪼개어 저장합니다.

### 3) Database 레플리카 그룹 (M대) : 최종 데이터의 보루

Master-Slave 복제 (Replication): 데이터베이스를 여러 대 띄우고 역할을 철저히 분리합니다.

Master DB (1대): 데이터의 삽입/수정/삭제(INSERT, UPDATE, DELETE) 등 '쓰기' 요청만을 전담합니다.

Slave DB (여러 대): 전체 트래픽의 80~90%를 차지하는 '조회(SELECT)' 요청을 여러 대가 분산 처리합니다.

엔진 단위의 동기화: 쓰기 작업이 Master DB에서 발생하면, DB 엔진은 이를 바이너리 로그(Binary Log)에 기록합니다. Slave DB들은 백그라운드 스레드를 통해 이 로그를 실시간으로 가져와(Relay Log) 자신의 디스크에 반영하여 데이터를 동일하게 맞춥니다.

코드 단의 라우팅: Spring Boot 등의 백엔드 프레임워크에서는 @Transactional(readOnly = true) 어노테이션이 붙은 메서드는 DB 커넥션 풀에서 Slave DB 주소를, 그렇지 않은 트랜잭션은 Master DB 주소를 선택하도록 AbstractRoutingDataSource 등을 통해 지능적으로 라우팅합니다.

### 2. 프론트엔드와 모바일 앱의 배포 전략 (AWS 기반)

거대한 K:N:M 백엔드 API 클러스터가 구축된 위에서, 최종 사용자에게 UI/UX를 제공하는 '클라이언트'를 어떻게 배포하느냐에 따라 웹과 앱의 아키텍처가 확연히 달라집니다.

### 2.1. 웹 환경의 배포 (SPA vs SSR)

웹 브라우저는 빈 껍데기로 시작하여 접속할 때마다 화면을 그릴 리소스(HTML/CSS/JS)를 서버로부터 다운로드해야 합니다.

SPA (정적 파일 기반 - React, Vue):

프론트엔드 연산 서버를 따로 띄우지 않는 Serverless에 가까운 구조입니다.

빌드된 정적 리소스를 AWS S3에 업로드하고, 전 세계 수백 곳의 엣지 로케이션에 캐싱해 주는 AWS CloudFront(CDN)를 덮어씌웁니다. 전 세계 어디서 접속하든 물리적으로 가장 가까운 엣지 서버에서 즉각적으로 파일을 응답하므로, 서버 관리 포인트 없이 대규모 트래픽을 완벽하게 소화합니다.

SSR (서버 연산 기반 - Next.js 등):

SEO 최적화와 초기 로딩 속도를 위해 서버에서 먼저 HTML을 동적으로 그려서(렌더링) 내려주는 방식입니다.

정적 파일이 아니기 때문에, 백엔드 서버처럼 Docker 컨테이너 이미지로 빌드한 후 AWS ALB(로드밸런서) 뒤에 K대의 프론트엔드 Node.js 서버를 수평 확장하여 배포해야 합니다.

### 2.2. 모바일 앱 환경의 배포 특이성과 아키텍처

앱 배포의 가장 큰 특징은 수천만 명의 사용자 스마트폰(단말기) 하나하나가 화면을 그리는 개별 프론트엔드 서버 역할을 한다는 점입니다.

클라이언트의 분산 (Zero-Frontend Server in AWS):

화면을 구성하는 UI 코드(컴포넌트)는 구글 플레이스토어나 애플 앱스토어를 통해 스마트폰의 디스크에 100% 영구 설치됩니다.

따라서 AWS 인프라에는 프론트엔드 화면을 주기 위한 서버(S3, CDN 등)가 일절 필요 없으며, 스마트폰이 화면을 그리기 위해 요청하는 JSON 데이터만 내려주는 순수 API 서버 클러스터만 존재하면 됩니다.

장점: 화면 에셋 전송이 사라지므로 네트워크 아웃바운드(Egress) 트래픽 비용이 극단적으로 절감되며, 렌더링을 폰의 CPU가 담당하므로 체감 성능이 매우 뛰어납니다.

앱 환경의 SSR 대체 기술 (실시간 업데이트 딜레마 극복): 정석적인 SSR은 불가능하지만, "스토어 심사(수일 소요)를 거치지 않고 실시간으로 화면을 변경하고 싶다"는 니즈를 해결하기 위해 다음과 같은 아키텍처를 도입합니다.

코드푸시 (CodePush / OTA 업데이트): React Native, Flutter 환경에서 사용되며, 앱 구동 시 클라우드(S3 등)를 찔러 최신 JS 번들 코드를 백그라운드에서 다운로드하여 화면 로직을 즉각 덮어씌웁니다.

서버 주도 UI (SDUI - Server Driven UI): 백엔드가 단순 텍스트 데이터를 넘어 "어떤 컴포넌트를 어디에 무슨 색상으로 배치하라"는 화면 설계도(Schema)를 JSON으로 내려줍니다. 단말기는 이를 파싱하여 레고 블록 조립하듯 즉석에서 네이티브 화면을 그려냅니다. (토스, 배달의민족 등에서 적극 활용)

웹뷰 (WebView) 하이브리드: 앱 내의 특정 이벤트 탭 등에 보이지 않는 브라우저(WebView)를 띄워, 기존 웹 SSR 환경(AWS 배포 Next.js 등)의 URL을 호출해 렌더링된 화면을 그대로 투영합니다.

## 관련 글

- [[blog/기타/index|기타]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCS 란- GCS 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCS 란?  GCS 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기 (89)|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
