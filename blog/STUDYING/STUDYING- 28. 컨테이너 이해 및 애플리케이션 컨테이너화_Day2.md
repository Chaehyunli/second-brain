---
title: "[STUDYING] 28. 컨테이너 이해 및 애플리케이션 컨테이너화_Day2"
created: 2026-08-25
updated: 2026-08-25
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-24
source_url: https://ch010104.tistory.com/346
---
# [STUDYING] 28. 컨테이너 이해 및 애플리케이션 컨테이너화_Day2

## 원문

https://ch010104.tistory.com/346

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

Bare Metal — 자원을 100% 단일 워크로드에 쏟아야 할 때 (고성능 DB, HPC). 크고 비싸서 다목적으로 쓰면 낭비

VM — 강한 격리가 필요할 때, 서로 다른 OS를 같은 서버에서 띄워야 할 때. Guest OS 오버헤드를 감수하고 보안 경계를 얻는 선택

## 원문 기반 개념 정리

### Bare Metal / VM / Container 비교

### 부동산 비유 → 기술 레이어 대응

### 스택 구조

### 핵심 특성 비교

### 언제 무엇을 쓰는가

Bare Metal — 자원을 100% 단일 워크로드에 쏟아야 할 때 (고성능 DB, HPC). 크고 비싸서 다목적으로 쓰면 낭비

VM — 강한 격리가 필요할 때, 서로 다른 OS를 같은 서버에서 띄워야 할 때. Guest OS 오버헤드를 감수하고 보안 경계를 얻는 선택

Container — 빠른 배포·스케일아웃이 중요할 때. Guest OS 없이 커널 공유로 가볍게 띄움. 커널 취약점이 전체에 파급될 수 있으므로 신뢰할 수 있는 워크로드에 적합

실무에서는 VM 안에 Container를 띄우는 혼합 구조가 흔함 → VM이 격리 경계를 담당하고, 그 안에서 Container가 경량 배포를 담당하는 역할 분담

### 컨테이너 프로세스 실행 방법과 CMD 최적화

### 문제 배경

컨테이너 운영 시 CMD 한 줄을 잘못 쓰면 다음 세 가지 문제가 연쇄적으로 발생함

컨테이너가 즉시 종료되지 않고 멈춰 있다가 강제 종료됨

트래픽 처리 중 Graceful Shutdown 없이 KILL 당함

트래픽 유실 및 배포 속도 저하

핵심 원인: PID 1 프로세스가 SIGTERM을 수신하지 못하는 구조로 CMD를 작성한 경우 발생함

### CMD 세 가지 형태 비교

### SIGTERM 핸들러 등록 — webserver.py

```python
import signal
def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    # SIGTERM 신호 처리 함수 정의 및 등록
    def handle_sigterm(signum, frame):
        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] SIGTERM 신호 수신')
        time.sleep(1)
        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] SIGTERM 처리 종료')
        httpd.server_close()
        sys.exit(0)
    signal.signal(signal.SIGTERM, handle_sigterm)
    print(f'Starting server on port{port}...')
    print(f'Access the server at <http://localhost>:{port}/login')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down server...')
        httpd.server_close()
```

앱 코드에 signal.signal(signal.SIGTERM, handle_sigterm)을 등록해야 SIGTERM 수신 시 핸들러가 호출됨. 핸들러 안에서 서버 소켓을 닫고(server_close()) 정상 종료(sys.exit(0))하는 것이 Graceful Shutdown의 핵심임

### 실습 1 — Exec Form (직접 실행)

```text
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}
...
RUN apt-get install -y python3 python3-pip
WORKDIR /app
COPY webserver.py .
CMD ["python3", "webserver.py"]
```

```bash
# docker 빌드
> docker build --tag linux-container:1.0 .

# docker image 검색
> docker images

# docker 실행
> docker run --rm -d --name linux-container linux-container:1.0
94f92313eb5698e53180083f63b06307f1b283e2e3425d8a3c43060b3e944f38.  <- Container ID (64자리)

# 실행되고 있는 컨테이너에 접속하기
> docker ps

> docker exec -it linux-container /bin/bash
# linux-container 내부에서 동작하고 있는 지 확인
# ps -ef
UID     PID  PPID C STIME TTY       TIME CMD
root      1     0 0 23:34 ?     00:00:00 python3 webserver.py
root      7     0 0 23:35 pts/0 00:00:00 /bin/bash
root     15     7 0 23:35 pts/0 00:00:00 ps -ef
# exit
```

PID 1 = python3 webserver.py → 앱이 직접 PID 1을 차지함

docker stop 시 SIGTERM이 PID 1(python3)에 바로 전달 → 핸들러 즉시 호출

```bash
terminal 1                               terminal 2
> docker logs -f linux-container         > docker stop linux-container
Starting server on port 8080...
Access the server at <http://localhost:8080/login>

# 즉시 수신
[2026-08-19 05:11:11] SIGTERM 신호 수신
[2026-08-19 05:11:12] SIGTERM 처리 종료
```

Spring Boot, FastAPI 등 프레임워크는 SIGTERM 수신 시 자체적으로 Graceful Shutdown 실행 (자원 해지, 연결 해지, 처리 중 요청 완료 등)

### 실습 2 — Shell Form (포크 실행)

```text
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}
...
RUN apt-get install -y python3 python3-pip
WORKDIR /app
COPY webserver.py .
#CMD ["python3", "webserver.py"]
CMD ["/bin/sh", "-c", "python3 -u webserver.py"]
```

```bash
# docker image 빌드
> docker build --tag linux-container:1.1 .
# docker 실행
> docker run --rm -d --name linux-container linux-container:1.1
94f92313eb5698e53180083f63b06307f1b283e2e3425d8a3c43060b3e944f38.  <- Container ID (64자리)
# 실행되고 있는 컨테이너에 접속하기
> docker ps
> docker exec -it python-container /bin/bash
# linux-container 내부에서 동작하고 있는 지 확인
# ps -ef
UID     PID  PPID C STIME TTY       TIME CMD
root      1     0 0 23:27 ?     00:00:00 /bin/sh -c python3 webserver.py  ← PID 1 = sh
root      7     1 0 23:27 ?     00:00:00 python3 webserver.py              ← 자식 프로세스
root      8     0 0 23:28 pts/0 00:00:00 /bin/bash
root     16     8 0 23:28 pts/0 00:00:00 ps -ef
# exit
```

PID 1 = /bin/sh → SIGTERM이 sh에만 전달되고, 자식인 python3에는 전달되지 않음 → 이전 Exec Form(직접 실행) 방식에서는 “python3 webserver.py”가 PID 1이어서 바로 SIGTERM을 받아서 죽었었음.(프로그램을 안전하게 정리하는 Graceful Shutdown) → Shell Form(Fork 실행)에서는 /bin/sh 가 SIGTERM을 받아 자식에게는 전달 x(자식은 10초간 기다리다가 강제 종료 명령어로 종료가 되기 때문에 데이터 유실의 문제가 발생 가능)

타임아웃(docker stop: 10초, kubectl: 30초) 이후 SIGKILL로 강제 종료됨

```bash
terminal 1                               terminal 2
> docker logs -f linux-container         > docker stop linux-container
Starting server on port 8080...
Access the server at <http://localhost:8080/login>

# 아래의 로그 미 수신. 바로 SIGKILL 실행 됨
~~[2026-08-19 05:11:11] SIGTERM 신호 수신~~
~~[2026-08-19 05:11:12] SIGTERM 처리 종료~~
```

Spring Boot, FastAPI 등 프레임워크는 SIGTERM SIGNAL 미 수신 → 비정상 종료 (Graceful Shutdown 미지원)

기존 컨테이너 중단 및 제거:

```bash
> docker stop linux-container
> docker rm linux-container
```

### 실습 3 — Shell with Exec (치환 실행)

```text
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}
...
RUN apt-get install -y python3 python3-pip
WORKDIR /app
COPY webserver.py .
#CMD ["python3", "webserver.py"]
CMD ["/bin/sh", "-c", "exec python3 -u webserver.py"]
```

```bash
# docker image 빌드
> docker build --tag linux-container:1.2 .
# docker 실행
> docker run --rm -d --name linux-container linux-container:1.2
94f92313eb5698e53180083f63b06307f1b283e2e3425d8a3c43060b3e944f38.  <- Container ID (64자리)
# 실행되고 있는 컨테이너에 접속하기
> docker ps
> docker exec -it python-container /bin/bash
# linux-container 내부에서 동작하고 있는 지 확인
# ps -ef
UID     PID  PPID C STIME TTY       TIME CMD
root      1     0 0 23:34 ?     00:00:00 python3 webserver.py  ← sh가 사라지고 앱이 PID 1
root      7     0 0 23:35 pts/0 00:00:00 /bin/bash
root     15     7 0 23:35 pts/0 00:00:00 ps -ef
# exit
```

exec 명령어로 sh 프로세스 자체를 python3으로 교체 → PID 1 = python3 → exec는 "새로운 자식 프로세스를 띄우지 말고, 현재 쉘 프로세스(PID 1)를 그 프로그램으로 완전히 덮어씌움(Replace)” → 컨테이너가 켜질 때 처음에는 /bin/sh가 PID 1로 시작 → 하지만 exec 키워드 때문에 /bin/sh가 실행되자마자 자기 자신을 python3 프로세스로 교체 → 결과적으로 /bin/sh는 사라지고, python3가 PID 1번을 물려받게 됨.

SIGTERM이 PID 1(python3)에 직접 전달 → Graceful Shutdown 정상 작동

```bash
terminal 1                               terminal 2
> docker logs -f linux-container         > docker stop linux-container
Starting server on port 8080...
Access the server at <http://localhost:8080/login>

# SIGTERM 수신 처리
[2026-08-19 05:11:11] SIGTERM 신호 수신
[2026-08-19 05:11:12] SIGTERM 처리 종료
```

쉘 환경변수($PORT 등) 처리가 필요한 경우 Exec Form 대신 이 방식을 사용함

이전의 직접 실행 방식의 경우, 쉘을 거치지 않기 때문에 환경변수를 사용할 수 없음

### [참고] Terminal을 Open 하는 의미

터미널을 연다 = Stdin/Stdout과 연결된 Shell Process를 실행하는 것임

fork: 자기와 동일한 자식 프로세스를 복제해서 낳음

exec: 현재 프로세스를 다른 프로그램으로 완전히 교체함 ("에어리언" — 껍데기는 그대로, 내용물만 갈아치움)

### docker exec -it container /bin/bash 옵션

i (Keep STDIN open): 로컬 터미널의 Shell Process STDIN을 컨테이너 내부 프로세스의 STDIN으로 연결. 없으면 입력이 컨테이너 안으로 전달되지 않음

t (Allocate a pseudo-TTY): 컨테이너 내부에 가상 터미널(pty)을 생성. 없으면 프롬프트 등 터미널 UI가 정상 렌더링되지 않음

### 웹서비스 실행 컨테이너 만들기

### 실습 시나리오 개요

이 실습은 실제 웹 서비스를 컨테이너로 구성하는 전체 흐름을 다룸

Spring Boot 컨테이너 빌드 및 실행

container network skala bridge 기반 Mariadb 연동

Frontend(정적 HTML) 컨테이너 빌드 및 실행

Vue.js Frontend 컨테이너 빌드 및 실행

전체 웹 서비스 구성 완성

### 컨테이너 기반 웹 서비스 전체 구조

브라우저 → Nginx(Frontend 컨테이너) → Spring Boot(API 컨테이너) → DB 순으로 트래픽이 흐름

### Local PC 환경 (개발)

static resource: HTML, CSS, image, video 등 → Nginx가 직접 서빙

javascript: 브라우저에서 동작하며 동적으로 고정된 리소스 및 데이터 갱신

Nginx가 /api 경로를 받으면 Spring Boot로 프록시함 → 단일 포트로 Frontend + API 모두 처리 가능

### 운영 환경 (Kubernetes 내부망)

외부망(인터넷)과 내부망(Kubernetes)이 분리됨

내부 컨테이너끼리는 내부 IP(10.100.30.x)로 통신

### 실습 1 — Spring Boot 컨테이너 만들기

소스 코드 위치: 00.sample-container/01.spring-backend-v1.0

### Dockerfile

```text
FROM eclipse-temurin:21-jre
# 작업 디렉토리 설정
WORKDIR /app
# JVM 힙 메모리 고정 설정 (load-memory 64MB 할당 + JVM 오버헤드 확보)
ENV JAVA_OPTS="-Xms256m -Xmx512m"
# 애플리케이션의 jar 파일을 컨테이너에 추가
ADD ./target/*.jar  app.jar
# 애플리케이션 실행 (JAVA_OPTS 환경변수 적용)
CMD ["sh", "-c", "exec java $JAVA_OPTS -jar app.jar"]
```

eclipse-temurin:21-jre — JDK 전체가 아닌 JRE만 포함한 경량 베이스 이미지

ENV JAVA_OPTS — 힙 메모리 범위를 256m~512m으로 고정. 컨테이너 환경에서 메모리 제한이 있으므로 JVM이 무한정 메모리를 잡지 않도록 명시함

CMD에서 exec를 사용 → Shell with Exec 방식으로 java 프로세스가 PID 1을 차지 → SIGTERM 수신 가능 (앞 챕터와 연결)

### 빌드 및 실행

```bash
# 1. Maven 빌드 (jar 생성)
> mvn clean install -DskipTests
# 2. Docker 이미지 빌드
> docker buildx build --tag spring-backend:1.0 .
# 3. mariadb 실행 확인
> docker ps
865c08b411ca  mariadb:latest  "docker-entrypoint.s…"  28 minutes ago  Up 28 minutes  0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp  mariadb
> docker network ls
8c04df2f4086  skala  bridge  local
# 4. spring boot 컨테이너 실행
> docker run -d \
    --name spring-backend \
    --network skala \
    -p 8080:8080 \
    -e SPRING_PROFILES_ACTIVE=local-mariadb \
    spring-backend:1.0
# 5. 확인
> docker ps
> docker logs spring-backend
```

-network skala — mariadb와 동일한 bridge 네트워크에 연결 → 컨테이너 이름(mariadb)으로 DB 접근 가능

e SPRING_PROFILES_ACTIVE=local-mariadb — Spring 프로파일을 mariadb용으로 지정. 이 환경변수 하나로 application.yml의 DB 설정이 전환됨

### 접속 확인

http://localhost:8080/ 브라우저 접속 → SK AX 주문 관리 시스템 화면 확인

사용자 등록 후 DBeaver로 DB 확인

host: http://localhost:3306

user: user / password: password

database: skala

### [참고] Spring Multi-Stage Dockerfile

mvn build와 container build를 하나의 Dockerfile로 처리하는 방식. CI 환경에서 로컬에 Maven 없이도 빌드 가능함

참고 파일: 01.training-code/exercise-source/Dockerfile.multi-stage

```text
# ── 빌드 스테이지 ──────────────────────────────────
FROM ubuntu:24.04 AS builder
RUN apt-get update && apt-get install -y openjdk-21-jdk maven \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /build
COPY pom.xml .
RUN mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q
# ── 런타임 스테이지 ────────────────────────────────
FROM eclipse-temurin:25-jre
WORKDIR /app
ENV SPRING_PROFILES_ACTIVE=local
# builder 스테이지의 jar만 복사 (소스, JDK, Maven 캐시 제외)
COPY --from=builder /build/target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

빌드 스테이지: ubuntu에 JDK + Maven 설치 → mvn package로 jar 생성

런타임 스테이지: JRE만 있는 경량 이미지에 jar만 복사 → 소스코드, JDK, Maven 의존성 캐시가 최종 이미지에 포함되지 않음

COPY --from=builder — 이전 스테이지의 결과물만 선택적으로 가져오는 Multi-Stage의 핵심 명령어

### 실습 2 — Frontend 컨테이너 만들기 (정적 HTML)

Spring Boot의 Thymeleaf 코드를 외부 SPA 구조의 컨테이너로 전환해서 별도 배포

소스 코드: 00.sample-container/03.frontend

### default.conf — Nginx 설정

```text
server {
    listen80;
    # 정적 파일 서빙
    location / {
        root/usr/share/nginx/html;
        indexindex.html;
        try_files$uri $uri/ /index.html;
        expires-1;
        add_headerCache-Control "no-store, no-cache, must-revalidate";
        add_headerPragma "no-cache";
    }
    # Spring Boot API 프록시
    location /api {
        resolver127.0.0.11 valid=10s;
        set$backend "spring-backend:8080";
        proxy_passhttp://$backend;
        proxy_http_version1.1;
        proxy_set_headerHost $host;
    }
}
```

try_files $uri $uri/ /index.html — SPA 라우팅 지원. 존재하지 않는 경로는 모두 index.html로 떨어뜨려 클라이언트 라우터가 처리하게 함

expires -1 + Cache-Control: no-store — 정적 파일을 캐시하지 않도록 설정. 배포 시 구버전이 브라우저에 남는 문제 방지

resolver 127.0.0.11 — Docker 내부 DNS 서버. set $backend로 변수화해야 컨테이너가 뜰 때 backend가 없어도 nginx가 죽지 않음

/api 경로를 spring-backend:8080으로 프록시 → 브라우저는 같은 호스트로만 요청하면 됨 (CORS 우회 효과)

### Dockerfile

```text
FROM nginx:alpine
# 기본 nginx 설정 파일 제거
RUN rm /etc/nginx/conf.d/default.conf
# 커스텀 nginx 설정 파일 복사 (정적 서빙 + /api 프록시)
COPY default.conf /etc/nginx/conf.d/
# 정적 파일들을 nginx 기본 디렉토리로 복사
COPY src/ /usr/share/nginx/html/
# nginx 포트 노출
EXPOSE 80
# nginx 실행 (기본 CMD가 이미 설정되어 있음)
CMD ["nginx", "-g", "daemon off;"]
```

nginx:alpine — Alpine 기반 경량 Nginx 이미지

daemon off; — nginx를 포그라운드로 실행. 없으면 nginx가 백그라운드로 빠지면서 PID 1이 종료되어 컨테이너가 즉시 종료됨

### 빌드 및 실행

```bash
# 이미지 빌드
> docker buildx build --tag frontend:1.0 .
# skala bridge network 연결하여 실행
docker run -d \
  --name frontend \
  --network skala \
  -p 9090:80 \
  frontend:1.0
```

-network skala — spring-backend와 동일 네트워크 → nginx가 spring-backend:8080으로 프록시 가능

p 9090:80 — 호스트 9090 → 컨테이너 80 포트 매핑

http://localhost:9090/ 접속 → 주문 관리 시스템 확인

### 실습 3 — Vue.js Frontend 컨테이너 만들기

소스 코드: 00.sample-container/04.vue-frontend

default.conf는 앞의 정적 Frontend와 동일하게 사용함

Vue.js는 소스코드(.vue, .js)를 그대로 서빙하지 않고, npm run build로 컴파일한 static resource를 컨테이너에 담음

### Dockerfile (Multi-Stage)

```text
# ── 빌드 스테이지 ──────────────────────────────────
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build          # static resource 생성 과정
# ── 배포 스테이지 ──────────────────────────────────
FROM nginx:alpine
# 기본 nginx 설정 제거 후 커스텀 설정 복사
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
# 빌드 결과물 복사                   static resource를 포함한 nginx 컨테이너 생성 과정
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

빌드 스테이지: node:20-alpine에서 npm run build → /app/dist에 정적 파일 생성

배포 스테이지: nginx:alpine에 dist 결과물만 복사 → Node.js, node_modules가 최종 이미지에 포함되지 않음

### 빌드 및 실행

```bash
# 이미지 빌드
> docker buildx build --tag vue-frontend:1.0 .
# skala bridge network 연결하여 실행
docker run -d \
  --name vue-frontend \
  --network skala \
  -p 8090:80 \
  vue-frontend:1.0
```

http://localhost:8090/ 접속 → Vue.js SPA 기반 주문 관리 시스템 확인

브라우저의 JavaScript가 /api를 통해 01.spring-backend-v1.0을 호출함

### 컨테이너 이미지 구조

### 컨테이너 이미지란

나의 프로세스를 실행하기 위한 OS 루트 파일시스템(rootfs)과 앱 실행 환경을 tar 레이어 단위로 직렬화하여 메타데이터와 함께 묶어놓은 배포용 패키지 아카이브

컨테이너를 실행할 때 필요한 파일시스템

이미지 레이어의 집합체 (파일 내용과 메타 정보를 포함)

레이어는 부모·자식 관계로 쌓임

변경분만 기록 (전체를 복사하지 않음)

Read Only — 실행 중에는 쓸 수 없음

공통 레이어를 이미지 간에 공유 → 디스크 용량을 줄이고 높은 이동성 실현

### tar (Tape ARchiver) 명령어

여러 개의 파일과 디렉토리를 하나의 파일로 묶거나 풀 때 사용하는 명령어

docker image는 실행을 위한 파일들을 계층적으로 묶어서 제공하는 방식으로 tar 묶음과 유사함

```text
# tar로 파일을 패키징 해보자
> cd 00.sample-container
> tar cvf sample-container.tar *
# 묶여진 파일 목록을 확인해보자
> tar tvf sample-container.tar
```

### 컨테이너의 이미지 내부 구조 확인하기

소스 코드 위치: 01.answer-code/07.in-images

### 실습용 Dockerfile

#← = 이미지 레이어로 만들어지는 대상

```text
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}            # ← 레이어 생성
RUN apt-get update && apt-get install -y curl lsb-release nginx  # ← 레이어 생성
ARG UBUNTU_VERSION
RUN echo "현재 빌드에 사용된 ubuntu version: ${UBUNTU_VERSION}"  # ← 레이어 생성
LABEL maintainer="himang10@gmail.com"
LABEL description="SKALA Linux Version"
EXPOSE 8080/tcp
EXPOSE 80/tcp
WORKDIR /var/www/html                    # ← 레이어 생성
COPY index.html .                        # ← 레이어 생성
CMD ["nginx", "-g", "daemon off;"]
```

### 이미지 빌드 및 tar로 추출

```bash
# 이미지 빌드
> docker build --tag indepth-container:1.0 .
# 컨테이너 이미지를 로컬에 저장하기
> mkdir indepth-container
# Docker Image를 저장하기
> cd indepth-container
> docker save indepth-container:1.0 -o indepth-container.tar
# 이미지 내용 확인하기
> tar  tvf indepth-container.tar   # 목록 확인
> tar  xvf indepth-container.tar   # 압축 해제
> ls
# 타일 유형 확인
> file *
```

### 이미지 내부 구조 — manifest.json

압축 해제 후 manifest.json을 보면 이미지의 전체 구성이 보임

```text
> cat manifest.json | jq
[
  {
    "Config": "blobs/sha256/19e1da3667ffa7305b54fb0ec640b156d87e4b948e1614f2e6a5eee8b89fe3ed",
    "RepoTags": [
      "container-linux:1.0"
    ],
    "Layers": [
      "blobs/sha256/119d19e001bafa21919289095e1dbfac64f1e16d2469dd14c2d2a520039d26d9",
      "blobs/sha256/0655737b94e69d8feaadb404d3c32bf6054788b8a7bd799836335a13252e7c1f",
      "blobs/sha256/4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1",
      "blobs/sha256/4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1",
      "blobs/sha256/a1b97ad067fc4da50b167f14c5b3f46da3db6906061e5c187fd30ea57bfb9a40"
    ]
  }
]
```

Config — 이미지 메타데이터(환경변수, CMD, LABEL 등)가 담긴 JSON 파일 경로

Layers — Dockerfile의 각 명령어가 만든 레이어 목록. 순서대로 쌓임

같은 해시(4f4fb700...)가 두 번 등장 → 동일 레이어를 재사용하고 있음 (빈 레이어인 경우 발생)

### Config 메타데이터 확인

```text
> cat blobs/sha256/5b666a89cbc7dd0abf11902346cc178118d055d8b8000fb29ecaaea6592d0491 | jq
```

manifest.json의 Config 경로를 따라가면 Dockerfile에 명시한 ENV, LABEL, EXPOSE, CMD 등이 JSON으로 저장되어 있음

### 각 Layer와 Dockerfile 명령어 대응

각 blobs/sha256 레이어를 tar tvf로 열면 어떤 Dockerfile 명령어가 만든 레이어인지 확인 가능함

```text
# blobs/sha256 디렉토리 내부 파일 유형 확인
> cd indepth-container/blobs/sha256
> file *
# JSON data  → 메타데이터 파일
# gzip compressed data  → 실제 파일시스템 레이어 (tar.gz)
# 특정 레이어 열기 (COPY index.html에 해당하는 레이어)
> tar tvf blobs/sha256/a1b97ad067fc4da50...
# → var/www/html/index.html 파일이 들어 있음을 확인
# JSON 파일 하나 읽어보기
> cat c56b5750cb2b38d26fa199072dece168efb35faac501544bb4e1beab67177b64
```

### [실습] mariadb image layer 확인해보기

공식 Mariadb 이미지 Dockerfile 참고:

Docker Hub: https://hub.docker.com/_/mariadb

GitHub: https://github.com/MariaDB/mariadb-docker/blob/master/10.11/Dockerfile

공식 Dockerfile 구조 (일부):

```bash
# vim:set ft=dockerfile:
FROM ubuntu:jammy
# add our user and group first to make sure their IDs get assigned consistently
RUN groupadd -r mysql && useradd -r -g mysql mysql --home-dir /var/lib/mysql
# add gosu for easy step-down from root
# <https://github.com/tianon/gosu/releases>
# gosu key is B42F6819007F00F88E364FD4036A9C25BF357DD4
ENV GOSU_VERSION 1.17
ARG GPG_KEYS=177F4010FE56CA3336300305F1656F24C74CD1D8
```

### mariadb 이미지 추출 및 분석

```bash
# 이미지 pull
> docker pull mariadb:10.11
# 컨테이너 이미지를 로컬에 저장하기
> mkdir indepth-mariadb
# Docker Image를 저장하기
> cd indepth-container
> docker save mariadb:10.11 -o mariadb.tar
# 이미지 내용 확인하기
> tar  xvf mariadb.tar
> ls
# 타일 유형 확인
> file *
```

### mariadb manifest.json 분석

```text
> cat manifest.json | jq
[
  {
    "Config": "blobs/sha256/b5898e2f865470ead4d653b985c74c640ea00be8e384d7c84d5eade2c58ff705",
    "RepoTags": [ "mariadb:latest" ],
    "Layers": [
      "blobs/sha256/69c262fc30fc134b6d373dee8db695319c41d8b9489deb0f682565473bf29748",
      "blobs/sha256/4a585ea2a801a7e852a88607392a2682abe6163f7c62138bc8d2d7387ea51501",
      "blobs/sha256/986b7028e52e39fadc4122e969e818c2b9a57ad0d041026ea995dd6310da15be",
      "blobs/sha256/9bf0665a0c3d191cb19d9f0027302e47db304a8c37fc255b0e842ff49df3fb83",
      "blobs/sha256/94b6ebcad19f3488fa4c4b89d30aa75faa444d86a85f1821f148fe75c8ea949e",
      "blobs/sha256/570cbed76d34d44a0a098a84f2505d1fc8b985225a71dc15599eb394c6d1b859",
      "blobs/sha256/de133d0ba73769c923f524a0d704fff2f8a88b3cd32981200611eefc83b078a7",
      "blobs/sha256/6eb5750376860940038ecdc9dc28a18962385a25331e2986326f0d2462a0a50c"
    ]
  }
]
...
```

각 레이어가 Dockerfile의 어떤 명령어에 대응하는지 화살표로 연결됨:

### 마지막 레이어 내용 확인

```bash
> cd ./blobs/sha256
> tar tvf 6eb5750376860940038ecdc9dc28a18962385a25331e2986326f0d2462a0a50c
drwxr-xr-x  0 0    0    0  5 29 11:22 usr/
drwxr-xr-x  0 0    0    0  5 29 11:22 usr/local/
drwxr-xr-x  0 0    0    0  6 11 07:36 usr/local/bin/
-rwxr-xr-x  0 0    0 26472  6 11 07:35 usr/local/bin/docker-entrypoint.sh
```

마지막 레이어에 docker-entrypoint.sh가 들어 있음 → 컨테이너 시작 시 초기화 스크립트를 담당하는 파일임을 레이어 단위로 직접 확인할 수 있음

### Docker Architecture — 컨테이너 생성 흐름

Client가 명령을 내리면 Docker daemon이 Registry에서 이미지를 pull해 로컬 Images에 저장하고, 그 이미지로 Container를 생성함

Registry는 Docker Hub처럼 이미지를 저장·배포하는 저장소

### Docker에서 사용되는 기술 스택

전체 호출 체인:

```bash
Docker 데몬 → containerd → containerd-shim → runc (바이너리) ──내장──→ libcontainer (라이브러리) → Linux Kernel
```

Docker 데몬 (dockerd): 고수준 명령(이미지 관리, 네트워크/볼륨 설정 등)을 받아 처리하는 관리자입니다.

containerd: 컨테이너의 생명주기(생성, 실행, 정지, 삭제)를 관리하는 핵심 엔진입니다.

containerd-shim: Docker 데몬이 재시작되거나 죽더라도 실행 중인 컨테이너가 따라 죽지 않도록 독립적으로 지켜주는 중간 관리자 역할을 합니다.

runc (실행 바이너리): OCI 표준 규격에 맞추어 실제로 컨테이너를 실행하는 커맨드라인 도구입니다.

libcontainer (내장 라이브러리): runc 내부에 내장된 핵심 패키지로, 리눅스 커널에 직접 명령을 내려 격리 공간을 생성합니다.

### libcontainer

리눅스 커널의 네임스페이스 생성, Cgroups 자원 할당, pivot_root, Capabilities 드롭 등 커널 시스템 콜을 직접 호출하는 순수 Go 언어 패키지(내부 엔진). Apache License 2.0 하에 공개, 리눅스 재단 산하 OCI 프로젝트

### runc

OCI(Open Container Initiative) 런타임 규격에 맞게 만들어진 CLI 커맨드라인 도구

OCI 스펙의 config.json을 읽어 컨테이너 생명주기 관리

Docker 아래에 libvirt, LXC(Linux Containers), systemd-nspawn 등도 동일하게 Linux Kernel 위에서 동작함

### Container Feature — Linux Kernel 기능의 조합

컨테이너는 가상 머신이 아니라 Linux Kernel 기능들의 조합으로 만들어진 격리 실행 환경

### 권한 체계

전통적 리눅스 모델: UID 0 (root) 와 일반 사용자 (UID > 0) 로 구분

문제점:

웹 서버가 80번 포트에 바인딩(Privileged Port)하려면 root 권한으로 실행 필요

root 권한만 있으면 시스템 전체 실행 가능

파일 소유자나 root는 파일 권한을 임의로 변경 가능 → 악성 코드 침투 시 시스템 보호 불가 (DAC 무력화)

솔루션 — Linux Capabilities: 주체 행위 특권의 세분화

root 특권을 약 40개로 나눔 (최소 권한 원칙 적용)

특정 프로세스가 탈취되더라도 root 전체 권한으로 승격되는 것을 방지

CAP_NET_BIND_SERVICE: 1024 미만 포트 바인딩만 허용

CAP_SYS_ADMIN: 시스템 관리성 작업 허용 (컨테이너 등에서 격리용으로 사용)

CAP_NET_ADMIN: 네트워크 인터페이스 설정 및 라우팅 제어 허용

SELinux: 객체 접근 및 행위에 대해 주체에게 강제 통제

프로세스가 파일, 디렉토리, 포트 등에 대해 수행할 수 있는 작업을 강제로 정의. 프로세스가 root(UID 0)이고 모든 Capability를 가지고 있더라도, SELinux 정책에 명시적으로 allow가 정의되어 있지 않으면 커널 단에서 접근을 차단함

### [예시] Kubernetes에서의 Capability & SELinux 적용

```text
# 쿠버네티스 Capability 예시
apiVersion: v1
kind: Pod
metadata:
  name: capability-demo
spec:
  containers:
    - name: nginx
      image: nginx:latest
      securityContext:
        runAsUser: 1000
        runAsNonRoot: true
        capabilities:
          drop:
            - ALL
          add:
            - NET_BIND_SERVICE
# → 1024 이하 포트 사용 권한 할당 (예: nginx 80 포트 할당 가능)
```

```text
# 쿠버네티스 SELinux 예시
apiVersion: v1
kind: Pod
metadata:
  name: selinux-demo
spec:
  securityContext:
    seLinuxOptions:
      user: system_u
      role: system_r
      type: container_t
      level: "s0:c123,c456"
  containers:
    - name: nginx
      image: nginx:latest
```

### 컨테이너 내 프로세스 격리 — namespace

PID, Network, Mount 등의 커널 데이터 구조를 네임스페이스로 분리해서 컨테이너 내 실행되는 프로세스가 지정된 네임스페이스의 커널 데이터를 참조하도록 구성하는 방식

핵심: 커널 레벨에서 보이는 세상(view)을 분리 → 실행되는 프로세스 입장에서는 논리적 OS만 볼 수 있음

### 프로세스에 할당된 리소스 — Control Group: cgroup

동일 namespace에 할당된 프로세스 집합에 대해 CPU, Memory, I/O 등의 사용량을 제한, 격리, 모니터링하는 기능

컨테이너에 할당하는 자원을 조정하는데 사용

프로세스 및 Thread를 그룹화하여 관리

Host OS의 CPU, 메모리와 같은 리소스를 그룹별로 제한 가능

계층구조로 프로세스를 그룹화하여 관리 가능

하위 cgroup은 상위 cgroup의 제한 설정이 그대로 적용

```bash
docker run -d \
  --name my-resource-container \
  --cpus="2.0" \
  --memory="512m" \
  nginx
```

### [참고] 자원 초과 시 처리 과정

메모리 limit 512M 설정 컨테이너에서 init process가 700MiB 사용 → limit 초과 시:

Linux 커널의 OOM Killer가 동작 → 프로세스 강제 종료

shim이 PID 1 종료 감지 → container 종료 상태를 containerd에 알림

containerd가 container 상태 갱신 (Docker는 Exited/137, k8s는 OOMKilled)

→ 나에게 할당되어 있는 자원 이외의 것을 사용하게 되면, 반대로 다른 프로세스의 메모리를 사용하지 못하기 되기 때문에 의도되지 않은 동작이 일어날 확률이 늘어나기 때문에, 할당되어 있는 자원을 넘어서 사용하는 프로세스를 죽임

자원 종류 컨트롤러 제어 방식 예시

### 이미지 관리 기술 — OverlayFS 기반 계층 파일 시스템

컨테이너 이미지를 가볍게 유지하고 빠른 속도로 컨테이너를 생성할 수 있는 핵심 기술. 여러 개의 폴더를 하나의 디렉토리로 합쳐서(Overlay) 보여주는 기술 (리눅스 커널 3.18 이후 정식 추가)

### 구성 요소

예시: python 3.10 (LowerDir) → python 3.11 (UpperDir) / /usr/bin/python (3.10) → /usr/bin/python (3.11)

### 주요 특성

레이어링(Layering): 읽기 전용(lowerdir)과 읽기-쓰기 가능(upperdir) 디렉토리를 하나의 통합된 파일 시스템처럼 사용. 사용자가 파일을 수정하면 변경 사항은 upperdir에 기록되며 lowerdir의 원본은 변경되지 않음

Copy-on-Write (CoW) 전략: 파일 수정 시 원본(lowerDir)을 그대로 두고 upperdir에 수정 파일을 복사하여 변경 관리 → 원본 불변성(Immutable) 보장

디렉토리 병합 및 우선순위: 동일한 파일이 존재할 경우, upperdir 파일이 우선

파일 시스템 투명성: 사용자에게는 하나의 디렉토리처럼 보임. 실제로는 여러 레이어를 OverlayFS가 조합하여 동작

```text
mount -t overlay overlay \
  -o lowerdir=/image/layers,\
     upperdir=/container/writable,\
     workdir=/container/work \
  /container/rootfs
```

### [참고] 디렉토리 구성 흐름

runC는 pivot_root()를 이용해서 이 병합된 디렉토리를 컨테이너의 루트 파일 시스템(/)으로 전환

```text
/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/<id>/fs/
├── lowerdir/    ← 읽기 전용 레이어들 (이미지)
├── upperdir/    ← 컨테이너 실행 중 변경사항 저장
├── workdir/     ← OverlayFS 내부 작업 디렉토리
└── merged/      ← OverlayFS 병합 mount 결과 → 이것이 /run/containerd/.../rootfs
```

merged = lowerdir + upperdir + workdir

runC는 이 merged 디렉토리를 /로 설정

### [실습] OverlayFS 기반 rootfs 만들어보기

ubuntu 컨테이너 내부에서 overlayfs 동작 원리를 이해해보자

```bash
# 1. ubuntu container 실행하기
> docker run --rm -it \
    --privileged \
    ubuntu:24.04 \
    /bin/bash
# 2. 컨테이너 내부에서 tmpfs를 마운트하기
> mkdir -p /mnt/ovtest
> mount -t tmpfs tmpfs /mnt/ovtest    # p1: 파일시스템 종류, p2: 장치식별자
> df -T /mnt/ovtest
Filesystem  Type  1K-blocks  Used  Available  Use%  Mounted on
tmpfs       tmpfs  4012648    12   4012636    1%   /mnt/ovtest
# 3. OverlayFS 디렉토리 만들기
mkdir -p /mnt/ovtest/{lower,upper,work,merged}
# 4. 파일 생성하기
echo "AAA from lower" > /mnt/ovtest/lower/a.txt
echo "BBB from lower" > /mnt/ovtest/lower/b.txt
# 5. 여러 파일을 중첩해서 마운트하기
mount -t overlay overlay \
  -o lowerdir=/mnt/ovtest/lower,upperdir=/mnt/ovtest/upper,workdir=/mnt/ovtest/work \
  /mnt/ovtest/merged
# 6. /mnt/ovtest/merged mount 확인하기
> mountpoint /mnt/ovtest/merged
/mnt/ovtest/merged is a mountpoint
> ls /mnt/ovtest/lower
a.txt  b.txt
> ls /mnt/ovtest/merged    # lower, upper merged 된 상태
a.txt  b.txt
# 7. /mnt/ovtest/merged 의 a.txt에 값을 변경해보자
> echo "add line test" >> /mnt/ovtest/merged/a.txt
# 8. /mnt/ovtest/merged/a.txt를 수정 후 확인
# - /mnt/ovtest/upper/a.txt가 생성되었는지 확인하기
# - /mnt/ovtest/lower/a.txt의 내용 확인하기 (cat /mnt/ovtest/lower/a.txt)
# - /mnt/ovtest/upper/a.txt 의 내용을 /lower와 비교해보자 (cat /mnt/ovtest/upper/a.txt)
```

CoW 동작 확인: merged에서 a.txt를 수정하면 lower의 원본은 그대로 유지되고, upper에 수정본이 새로 생성됨

### 컨테이너 실행 구조 — Docker Engine, containerd, runc

모든 통신 방식은 UDS(Unix Domain Socket) 기반으로 통신

(docker v1.11 이후부터 적용된 docker architecture)

### dockerd (docker engine)

Docker의 진입점이면 Docker 전체 운영을 관리

Docker 엔진에 이미지 실행을 요청하면 containerd 데몬에 책임을 위임

### containerd (=cri-o) — kubernetes kubelet과 연동

OCI 표준 번들 (config.json + rootfs) 직접 생성

OverlayFS 기반으로 rootfs (MergedDir) 준비

dockerd로부터 받은 컨테이너 실행 설정을 config.json으로 구성

containerd-shim fork 및 exec 후 OCI 번들 전달

### containerd-shim (=podman/crio는 conmon 경량 프로세스)

runC 프로그램 실행 (Args: config.json, rootfs 경로)

namespace 생성, cgroups 설정

pivot_root 로 / 교체

execve() init process 실행 및 init process PID shim에 전달

해당 PID를 감시 및 I/O 파이프라인 연결/대기 (docker exec | logs)

### [참고] 컨테이너 프로세스 (CMD init Process) 실행 구조

```text
[ containerd ]
      ↓
[ containerd-shim ]
      ↓ fork + exec ( cmd := exec.Command("runc", "create", …)  cmd.Start() )
[ runc ] ──→ [ namespace 생성 ]
      |       [ cgroup 설정 ]
      |       [ rootfs pivot ]
      ↓ fork+exec
[ init process (PID 1) ] ← container 내부 최상위 프로세스
      ├── [ user process 1 ]
      ├── [ user process 2 ]
      └── ...
```

### RunC

LXC (LinuX Container) → libcontainer → OCI 표준의 Reference 구현체 RunC (libcontainer wrapping)

namespace 생성 & cgroup 설정

rootfs 마운트 및 교체

UID/GID 매핑

Capability, seccomp, AppArmor 적용

init 프로세스 (PID 1) 실행 (CMD, ENTRYPOINT) 기준

### OCI (Open Container Initiative)

컨테이너 이미지와 컨테이너 실행 방법을 표준화한 오픈 표준 프로젝트

### 1. OCI Image Spec

어떤 도구든 이미지를 다운받아 해석할 수 있는 패키지 표준 규격

컨테이너 이미지 구조, 압축 파일(tar) 레이어

manifest.json 표준

### 2. OCI Runtime Spec

컨테이너 실행을 위한 OCI Bundle을 정의하는 표준 규격

```text
OCI Bundle
├── config.json    ← 어떻게 실행할 것인가
└── rootfs/        ← 무엇을 실행할 것인가
    ├── bin/
    ├── usr/
    ├── lib/
    └── ...
```

### 3. OCI Distribution Spec

컨테이너 이미지를 Registry에 Push/Pull 하기 위한 API 규격

```text
Registry 관리
/v2/library/nginx/
  ├── manifests/latest
  │     ├── config → sha256:AAA
  │     ├── layer  → sha256:BBB
  │     └── layer  → sha256:CCC
  └── blobs/
        ├── sha256:AAA ← Image Config
        ├── sha256:BBB ← Layer
        └── sha256:CCC ← Layer

manifest GET   GET /v2/library/nginx/manifests/latest
layer GET      GET /v2/library/nginx/blobs/sha256:AAA...
```

### [참고] OCI를 통해 이종(Heterogeneous) 도구간 호환성 보장

OCI 호환 이미지를 생성한다는 의미 = Docker가 만든 이미지가 OCI에서 정한 표준 형식에 맞는 컨테이너 이미지라는 의미 (이미지 메타데이터 구조, 레이어 구조, Image Spec manifest.json, Runtime Spec config.json)

공통 형식(OCI 표준)을 사용하기 때문에 특정 벤더에 종속되지 않는 에코시스템 빌드가 가능함

로컬 검증 (CLI): 개발자 로컬 PC에서 Docker나 Podman으로 즉시 실행 및 테스트 가능

빌드 (Build): buildkit, Buildah, Kaniko로 이미지를 빌드하고

저장 (Registry): Harbor나 Docker Hub 같은 OCI 레지스트리에 저장(Push/Pull)하며

배포 및 실행 (Runtime): docker, 쿠버네티스의 containerd나 CRI-O에서 이 이미지 pull/run

### Docker Network 유형

### 네트워크 구조 다이어그램

Container (172.17.0.2) 패킷 흐름:

eth0 (L2 이더넷) → veth (L2 가상 이더넷) → docker0 (bridge) → Host IP stack (NAPT 처리) → enp0s3 (L2 NIC) → Router → Internet

### Docker Networking — bridge 및 가상 NIC

Docker 컨테이너는 서버의 물리 NIC와 별도로 각 컨테이너마다 가상 NIC 할당

Default gateway로 Linux bridge인 docker0를 만듦

외부 네트워크와 교환하는 패킷에 NAT 작업 수행

컨테이너 간 네트워크 연결

각 컨테이너에 격리된 네트워크 공간을 만들고 컨테이너의 eth0에 static IP 할당

### -network bridge

HOST의 netfilter + ipTable을 통해 DNAT에서 container IP:port를 매핑

예) 192.168.1.22:8888 → 172.17.0.3:8080

### -network host

컨테이너가 호스트 네트워크를 직접 공유. Bridge 없음, veth 없음. 호스트의 eth0(192.168.0.11)를 컨테이너가 그대로 사용 → NAT 오버헤드 없어 성능 최고

AWS는 VPC Network 이용하고, calico도 적용할 수 있음

### [참고] 패킷 변환 및 전달 흐름

HostIP: 192.168.1.22:888 → 컨테이너 IP: 172.17.0.3:8080으로 전달되는 흐름

Host 물리 NIC 진입 → Netfilter 최초 낚아채기 (PREROUTING)

외부 Client → eth0 → Netfilter PREROUTING → ipTable NAT 규칙 (8888 → 172.17.0.3:8080)

Kernel Routing Table 검색 → docker0 결정

DST IP: 172.17.0.3 → kernel Routing Table → 172.17.0.0/16 dev docker0 → docker0 결정

커널 라우팅 테이블(Routing Table)의 172.17.0.0/16 대역은 docker0로 결정

docker0 브리지 연결된 가상 NIC (Veth)로 중계

Host Kernel은 Host Network Interface(eth0) Neighbor(or ARP) 테이블을 통해 172.17.0.3의 MAC 주소(02:42:ac:11:00:03)를 확인

Kernel은 해당 MAC 주소를 destination MAC으로 Ethernet Frame을 구성하여 docker0로 전달

docker0는 FDB에서 Destination MAC에 해당하는 Bridge Port(vethxxx)를 검색

docker0 → veth220960a → Container eth0로 Frame 전달

용어 정리:

Bridge Port: Bridge에 연결되어 있는 Network Interface를 의미

ARP (Address Resolution Protocol) Table = Neighbor Table: IP와 MAC Address 매핑 테이블

FDB (Forwarding Database): MAC Address → Bridge Port (veth) 매핑 테이블

### Network 유형 별 특성

docker0를 포함한 bridge는 L2 Switch 역할 수행 (MAC 기반 vethXX → eth0 연결)

유형 격리 DNS 성능 사용 목적

Custom Bridge는 DNS를 지원하는데, 이것은 Docker Network 내부에 DNS 서버가 자동으로 동작하기 때문임. 컨테이너 이름(myservice)으로 다른 컨테이너에 접근 가능 → curl myservice 형태로 서비스 디스커버리 가능

### [참고] 무선공유기 DHCP / NAPT

DHCP(Dynamic Host Configuration Protocol): 무선 공유기(또는 DHCP 서버)가 각 기기에게 자동으로 IP 주소, 서브넷 마스크, 게이트웨이, DNS 서버 등을 할당해 주는 프로토콜

NAPT(Network Address and Port Translation): 사설 IP(192.168.1.42, 192.168.1.23)를 공인 IP(203.0.113.57)의 서로 다른 포트(2001, 2002)로 변환하여 인터넷 통신 → docker0도 동일 원리로 동작

ipconfig / ifconfig로 나의 IP를 확인하고 다른 사람 네트워크로 접속해보기

### Docker 컨테이너간 통신

Docker Network는 단일 노드에서의 통신만을 정의하고 있음

### Docker 컨테이너간 통신 (링크 기능)

동일 호스트 내 bridge docker0에 접속한 컨테이너간 통신. /etc/hosts에 db 항목을 추가해 이름으로 접근하는 Link 방식 사용

### Docker 컨테이너와 외부 네트워크 통신

가상 bridge docker0와 Host OS의 물리 NIC에서 패킷 전송 — DNAT: Destination NAT, IP + PORT 변환

```bash
docker run -d -p 8080:80 nginx
# 호스트 port 8080 ⟹ 컨테이너A port 80
# 호스트 port 8080 ⟹ 컨테이너B port 3306
```

### [참고] Kubernetes Calico Network

Calico는 Kubernetes에서 사용하는 CNI(Container Network Interface) 구현체로, 멀티 노드 환경에서 Pod 간 네트워크 통신을 가능하게 하는 네트워크 플러그인

Kubernetes는 calico, EKS VPC CNI 등의 CNI 기반 네트워크 플러그인을 제공하고 있음

### 단일 노드 내 컨테이너 간 통신

etho:veth → caliXXX:VR (Virtual Router 경유)

### 외부 노드의 컨테이너와 통신

eth0:veth → caliXXX:VR → tunl0 → eth0

tunnel (tunl0): 리눅스 커널이 제공하는 IP-in-IP(IPIP) 터널 인터페이스. 다른 노드에 패킷 전송 시 Container IP를 Encapsulation하고 Node IP를 기반 통신

Virtual Router (flex + BGP daemon): "Pod IP(CIDR 대역)가 어느 노드에 있는지를 알려주는 역할". 예시: 10.1.2.0/24 → 192.168.100.20 eth0

참고: BGP(Border Gateway Protocol): 라우팅 프로토콜(Routing Protocol)로, L3(IP 기반)의 경로 정보를 교환

### [참고] CIDR (Classless Inter-Domain Routing)

IP 주소 범위를 표현하는 방식. 예전에는 클래스로 A, B, C를 나눴는데 너무 비효율적이어서, CIDR은 필요한 크기만큼 유연하게 IP 대역을 나누기 위해 사용

예시 — 192.168.0.0/24:

192.168.0.0: 네트워크 시작 주소

/24: 앞의 24비트가 네트워크 부분이라는 뜻

앞 24비트가 네트워크, 뒤 8비트가 호스트 → 총 256개 주소 범위 (Broadcast, NA 제외 총 254개)

보통 192.168.0.0 ~ 192.168.0.255

```text
192.168.0.0/24 이진수:
11000000.10101000.00000000.xxxxxxxx
|<---------- /24 ---------->|
                    00000000 ~ 11111111
                         0  ~     255

network address : 11000000.10101000.00000000.00000000
broadcast       : 11000000.10101000.00000000.11111111
```

### [참고] Unix Domain Socket (UDS) 프로그램

네트워크 대신 파일 경로(Socket file)를 주소로 사용하는 로컬 IPC Socket

dockerd ↔ containerd ↔ containerd-shim ↔ init process 간 통신은 일반적으로 Unix Domain Socket을 이용해서 통신 실행

TCP Socket: 127.0.0.1:8080

Unix Domain Socket: /tmp/my.sock

특징:

IP 스택/라우팅/포트 등 네트워크 계층을 거치지 않음

같은 서버 내부 통신에는 TCP보다 더 빠르고 오버헤드가 적음

소켓이 파일이라서 권한 제어 가능

외부 네트워크 접근 자체 불가능

사용처:

Docker: /var/run/docker.sock

Kubernetes (kubelet과 통신 시): containerd /run/containerd/containerd.sock, CRI /run/crio/crio.sock

Nginx ↔ upstream 앱 통신(예: PHP-FPM)

DB 로컬 연결: MySQL /var/run/mysqld/mysqld.sock, PostgreSQL도 로컬 소켓 사용 가능

### runc 들여다 보기

nerdctl, docker, ctr은 containerd를 거쳐 runc로 컨테이너 실행

podman은 데몬 없이 직접 crun(C언어 구현 OCI 런타임)으로 실행

### runc 기반 container 라이프사이클 관리

### [실습] runc 직접 동작시켜보기

dockerd-shim이 직접 호출해서 컨테이너를 생성하는 과정을 직접 수동으로 동작시키면서 OCI 런타임 표준과 컨테이너 동작 방식을 이해해보자

목표: containerd-shim 대신 본인이 runc를 직접 호출해서 다음 동작을 확인

namespace와 cgroup을 설정하고

pivot_root를 통해 컨테이너의 root filesystem을 변경한 뒤

해당 namespace 환경에서 프로세스를 실행한다

실습 코드 위치: 01.answer-code/runc/ (Dockerfile, build.sh, run.sh)

### Dockerfile

```bash
FROM ubuntu:24.04
RUN apt-get update && apt-get install -y curl lsb-release nginx
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y jq vim net-tools lsof tar gzip runc
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY webserver.py .
# Docker CLI 설치
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL <https://download.docker.com/linux/ubuntu/gpg> | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    bash -lc 'ARCH=$(dpkg --print-architecture); \
    echo "deb [arch=${ARCH} signed-by=/etc/apt/keyrings/docker.gpg] <https://download.docker.com/linux/ubuntu> \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list' && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*
CMD ["python3", "webserver.py"]
```

### build.sh

```bash
#!/bin/bash
IMAGE_NAME="runc-test"
VERSION="1.0"
#IS_CACHE="--no-cache"
# Docker 이미지 빌드
docker buildx build \
  --tag ${IMAGE_NAME}:${VERSION} \
  --platform linux/arm64,linux/amd64 \
  --file Dockerfile \
  ${IS_CACHE} .
```

### run.sh

```bash
#!/bin/bash
set -eux
IMAGE_NAME="skala-registry.skala-ai.com/library/runc-test"
VERSION="1.0"
if docker ps -a --format '{{.Names}}' | grep -q '^runc-test$'; then
  docker stop runc-test
  docker rm runc-test
fi
docker run -d \
  --name runc-test \
  -p 8888:8080 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --group-add 0 \
  --privileged \
  ${IMAGE_NAME}:${VERSION} \
  sleep infinity
```

v /var/run/docker.sock:/var/run/docker.sock — 호스트 Docker 소켓을 컨테이너 내부로 마운트 → 컨테이너 내부에서 docker 명령 사용 가능

-privileged — 컨테이너 내부에서 namespace/cgroup 조작 등 커널 수준 작업을 허용

### 실습 1 — ubuntu 컨테이너 실행

bash

```bash
# runc-test 빌드하기
./build.sh
# 레포지토리 루트에서
./run.sh
# 컨테이너가 정상적으로 올라왔는지 확인
docker ps --filter name=runc-test
# 2. ubuntu 컨테이너에 진입
# 호스트에서 컨테이너로 진입
docker exec -it runc-test /bin/bash
# 3. runc-test container 내부
# 설치 확인
> runc --version
```

### 4. OCI bundle(rootfs + config.json) 준비

OCI bundle은 container image를 풀어놓은 rootfs와 컨테이너 실행을 위한 설정 환경 정보 (Containerd의 역할)

```bash
# 작업 디렉토리 생성 및 이동
> cd
> mkdir -p ./mybundle/rootfs    # alpine:latest image를 풀어헤치기 위한 rootfs
> cd ./mybundle
# Docker 소켓을 공유했으므로 컨테이너 내부에서도 Docker 명령 사용 가능
# Alpine 이미지의 rootfs 추출
> docker export $(docker create alpine:latest) | tar -C rootfs -xf -
# 풀어진 이미지 내용 확인하기
> ls -al rootfs
# 기본 OCI spec 생성 (config.json)
> runc spec
> ls
config.json  rootfs
```

### 5. OCI Bundle 기반 container 생성 및 실행

```bash
# container 생성/실행
> runc run mycontainer
/# ps -ef
PID  USER   TIME  COMMAND
  1  root   0:00  sh
  7  root   0:00  ps -ef
/# ifconfig
/# exit
# 별도의 터미널을 열고 생성된 컨테이너를 확인해보자
> docker exec -it runc-test /bin/bash
> runc list
ID           PID    STATUS   BUNDLE          CREATED
mycontainer  230    running  /app/mybundle   Z  root
```

runc run mycontainer 실행 시 config.json의 namespace 설정에 따라 격리된 환경에서 sh(PID 1)가 실행됨

runc list로 호스트(runc-test 컨테이너) 입장에서 runc가 관리하는 컨테이너 목록 확인 가능

이것이 containerd-shim이 매번 수행하는 동작의 수동 재현임

### [실습 2] 볼륨 마운트하기

config.json에 볼륨을 마운트해보자

```text
# Ubuntu 컨테이너 내부에서 공유할 디렉토리 생성
> mkdir -p /mydata
> echo "Hello from host" > /mydata/test.txt
# config.json에 마운트 추가
> cd /app/mybundle
> cat config.json | jq '.mounts += [{
  "destination": "/data",
  "type": "bind",
  "source": "/mydata",
  "options": ["rbind", "rw"]
}]' > config_volume.json
# 추가된 마운트 확인
> cat config_volume.json | jq '.mounts[] | select(.destination == "/data")'
> cp config_volume.json config.json
```

### 마운트 대상 디렉토리와 파일 추가하기

```text
> runc run mycontainer
/# cd /data
/data # ls
/data # cat test.txt
/data # exit
```

핵심 원리: config.json의 mounts 배열에 bind mount 항목을 추가하면, runC가 컨테이너 시작 시 호스트 디렉토리를 컨테이너 내부에 마운트함. docker의 -v /mydata:/data 옵션과 동일한 동작임

### [실습 3] Local Host와 컨테이너 간 PID 공유하기

config.json의 namespaces에서 PID type을 제거 후 Host와 PID 공유를 확인해보자

```text
# config.json의 namespace의 pid와 network를 각각 제거해보기
> vi config.json
    "namespaces": [
                {
                    "type": " pid"    ← 이 블록 제거하기
                },
                {
                    "type": "uts"
                },
                {
                    "type": "network"
                },
    ],
<ESC>
:wq!
```

### 컨테이너 내에서 PID 검색 시 Host PID 목록이 보임

```text
> runc run mycontainer
# ps -ef
PID  USER   TIME  COMMAND
  1  root   0:00  sleep infinity      ← runc-test 컨테이너의 PID 1 (호스트 관점 PID)
240  root   0:00  /bin/bash
300  root   0:00  runc run mycontainer   ← 빨간색: 현재 runc 프로세스가 보임
314  root   0:00  sh
```

namespace에서 "type": "pid" 항목을 제거하면 → PID namespace가 격리되지 않음 → 컨테이너 내부에서 ps -ef를 실행하면 호스트의 모든 프로세스가 보임 → docker의 --pid=host 옵션과 동일한 효과

### [실습 4] Local Host와 컨테이너 간 Network 공유하기

config.json의 namespaces에서 network type을 제거 후 Host와 네트워크 공유를 확인해보자

```text
> vi config.json
    "namespaces": [
                {
                    "type": "uts"
                },
                {
                    "type": "network"    ← 이 블록 제거하기
                },
    ],
<ESC>
:wq!
```

### 컨테이너 내에서 Network 검색 시 Host Network 목록이 보임

```text
> runc run mycontainer
/ # ifconfig
eth0    Link encap:Ethernet  HWaddr 8A:63:9C:1E:23:23
        inet addr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0
        UP BROADCAST RUNNING MULTICAST  MTU:65535  Metric:1
        RX packets:12 errors:0 dropped:0 overruns:0 frame:0
        TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
        collisions:0 txqueuelen:0
        RX bytes:1172 (1.1 KiB)  TX bytes:126 (126.0 B)
```

다른 터미널에서:

```bash
> docker exec -it runc-test /bin/bash
> ifconfig    # runc-test 컨테이너와 동일한 네트워크 인터페이스가 보임을 확인
```

network namespace 항목을 제거하면 → 컨테이너가 호스트의 network namespace를 공유 → docker의 --network host 옵션과 동일한 효과 → 컨테이너 내부에서 보이는 eth0가 호스트(runc-test 컨테이너)의 eth0와 동일함

### [실습 5] runc를 통해 직접 init process 실행하기

runc를 통해 init(PID 1)을 직접 실행하는 스크립트를 만들어보자 — Dockerfile의 CMD ["/bin/sh", "/init.sh"]과 동일하게 동작

### 1. init.sh PID 1 프로세스 만들기

```text
cd /app/mybundle
cat > rootfs/init.sh <<'EOF'
#!/bin/sh
echo
echo [init] hello from runc
date
sleep 1
echo [init] done
sleep 3600
EOF
chmod +x rootfs/init.sh
```

### 2. config.json에서 init 프로세스 등록하기

```text
"process": {
    "terminal": false,    ← true에서 false로 변경
    "user": {
        "uid": 0,
        "gid": 0
    },
    "args": [
        "sh", "/init.sh"    ← "/init.sh" 추가
    ]
```

### 3. runc를 통해 container 실행하기

```text
# runc를 동작시킬때 config.json이 있는 위치여야 함
> ls
config.json  rootfs
> runc run -d mycontainer
> runc list
ID           PID    STATUS   BUNDLE      CREATED                        OWNER
mycontainer  1112   running  /mybundle   2026-02-25T22:37:27.852760555Z  root
> runc state mycontainer
ID           PID  STATUS   BUNDLE          CREATED                          OWNER
mycontainer  231  running  /app/mybundle   2026-08-20T11:41:42.783856045Z   root
```

### 4. mycontainer 내부 init.sh 실행 확인하기

```text
> runc exec -t mycontainer /bin/sh
/ # ps -ef
PID  USER   TIME  COMMAND
  1  root   0:00  sh /init.sh       ← PID 1 = init.sh
  9  root   0:00  sleep 3600
 23  root   0:00  /bin/sh
 29  root   0:00  ps -ef
/ # exit
> ps -ef
```

### container 종료시키기

```text
> runc list
ID           PID  STATUS   BUNDLE          CREATED                          OWNER
mycontainer  231  running  /app/mybundle   2026-08-20T11:41:42.783856045Z   root
> runc kill mycontainer KILL
ID           PID  STATUS   BUNDLE          CREATED                          OWNER
mycontainer  0    stopped  /app/mybundle   2026-08-20T11:41:42.783856045Z   root
> runc delete mycontainer
> runc list
```

실습 의미: config.json의 args에 /init.sh를 넣으면 그것이 PID 1이 됨. 이것이 Dockerfile의 CMD가 결국 하는 일 — containerd가 config.json을 작성하고 runC가 이 파일을 읽어 init process를 실행하는 것임

### 컨테이너가 실행 단위인가?

컨테이너란?

containerd나 dockerd 등의 컨테이너 런타임이 정의한 논리적 그룹이며, Linux 커널의 namespace와 cgroup 기능으로 프로세스 그룹을 격리·제한하여 구현된 것

그리고, dockerd, containerd 등이 컨테이너라는 단위로 논리적으로 추상화하여 관리

컨테이너는 결국 **"프로세스의 모음"**이며, 그 실행은 일반 리눅스 프로세스와 같지만, 단지 런타임에 의해 격리(namespace) 및 자원 제한(cgroup) 된 상태로 운영되는 것

### 컨테이너의 실행 주체는 프로세스

컨테이너는 Host 환경의 파일 디렉토리와 프로세스로 동작한다

컨테이너는 별도의 OS가 아님. Host의 Linux Kernel 위에서 프로세스로 동작함

컨테이너가 보는 루트 파일시스템(/)은 OverlayFS + pivot_root로 교체된 것뿐

HOST 프로세스와 Container 내 프로세스는 동일한 커널을 공유함

실습 3(PID namespace 제거)에서 확인했듯, namespace만 제거하면 컨테이너 경계가 사라지고 호스트 프로세스가 그대로 보임 → 컨테이너의 격리는 커널 기능으로 만든 논리적 경계임

### Docker-Compose란?

단일 노드 내에서 여러 개의 컨테이너를 조율하는 컨테이너 오케스트레이션 플랫폼임. 정확히는 여러 컨테이너로 구성된 애플리케이션을 하나의 docker-compose.yaml 파일로 정의하고, 한 번의 명령으로 실행/중지/관리할 수 있게 해주는 도구임.

### 주요 활용 상황

여러 컨테이너가 함께 동작하는 애플리케이션 실행

로컬 개발 환경 구성

교육·실습 환경 구성

통합 테스트 환경 구성

### Compose가 해결하는 문제

컨테이너 수가 늘어날수록 아래 문제가 심해짐:

명령어가 길고 복잡해짐

네트워크/볼륨/환경변수 설정을 서비스마다 반복해야 함

실행 순서를 사람이 직접 관리해야 함

### docker-compose.yaml이 담당하는 역할

동작 흐름: docker-compose.yaml → Docker Compose 엔진 → 각 서비스별 이미지 빌드(혹은 pull) → 컨테이너 실행

### docker-compose 기본 구조

### yaml 기본 구성 예시

```text
services:
  db:
    image: postgres:15
    volumes:
      - ./data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: postgres
  backend:
    image: my-backend
    depends_on:
      - db
  frontend:
    image: my-frontend
    ports:
      - "8080:80"
```

### 주요 필드 의미

db — 서비스 이름 (컨테이너를 지칭하는 논리적 단위)

image — 사용할 컨테이너 이미지

volumes — 호스트 경로와 컨테이너 경로를 마운트, ./data:/var/... 형식

environment — 컨테이너 내부 환경변수 설정

ports — 호스트:컨테이너 포트 매핑

depends_on — 해당 서비스가 먼저 기동되어야 함을 선언

참고: docker run -v는 절대 경로 또는 볼륨명을 사용하는 반면, docker-compose의 volumes는 상대 경로(./...) 사용 가능함. 기준은 docker-compose.yaml이 위치한 디렉토리임.

### [실습] docker-compose 시작하기

### 1. docker-compose.yaml 작성

```bash
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: postgres
    ports:
      - 5432:5432
    restart: always
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.backend
    ports:
      - 9090:8080
```

build.context — Dockerfile이 있는 디렉토리

build.dockerfile — 사용할 Dockerfile 파일명 지정 (기본값 Dockerfile과 다를 때 명시)

restart: always — 컨테이너 비정상 종료 시 자동 재시작

### 2. 실행

```bash
cd 10.docker-compose/01.start
docker compose up --build -d
```

### 3. 접속 확인

http://localhost:9090 → { "message": "Hello from FastAPI backend" } 응답 확인

### 4. 종료 및 네트워크 삭제

```bash
docker compose down
```

### 명령어: 컨테이너 빌드/실행/중지

### 이미지 빌드

```bash
docker compose build               # 전체 빌드
docker compose build --no-cache    # 캐시 없이 완전 재빌드
docker compose build backend       # 특정 서비스만 빌드
```

### 빌드 + 실행

```bash
docker compose up                       # foreground 실행
docker compose up -d                    # background 실행
docker compose up -d db backend         # 특정 서비스만 실행
docker compose up -d --build            # 빌드 후 바로 실행 (가장 자주 씀)
```

### 중지 및 재시작

```bash
docker compose stop                     # 중지 (컨테이너 삭제 안 함)
docker compose start                    # 중단된 서비스 재시작
docker compose restart                  # stop + start
docker compose restart backend          # 특정 서비스만 stop & start
```

### 명령어: 상태 확인

### 로그 추적

```bash
docker compose logs -f                  # 모든 서비스 로그 실시간 추적
docker compose logs -f backend          # 특정 서비스만 지정
```

### 컨테이너 상태 확인

```bash
docker compose ps                       # 실행 중인 컨테이너 목록
docker compose ps -a                    # 실행 중 + stop 상태 포함
```

### 컨테이너 메타데이터 상세 조회

```bash
docker inspect {container-name} | less
```

less는 결과를 페이지 단위로 보기 좋게 출력하는 유틸리티임. inspect로 확인 가능한 정보:

컨테이너 상태, 실행 여부, 종료 코드, OOM 여부

네트워크 정보 (IP 주소, 연결된 네트워크)

마운트 경로, 볼륨/바인드 마운트

환경 변수

실행 명령 (CMD, ENTRYPOINT)

restart 정책, healthcheck 결과

### 명령어: 리소스 제거

볼륨에 DB 데이터가 있을 경우, -v 옵션은 데이터도 함께 삭제되므로 주의 필요함.

### 명령어: 장애 복구

### 설정/환경 변경을 반영해 컨테이너 재생성

```bash
docker compose up -d --force-recreate backend
```

기존 컨테이너를 중지하고 새로 생성함. 이미지 변경 없이 yaml 설정만 바뀌었을 때 사용함.

### 네트워크까지 포함한 완전 초기화 후 재기동

```bash
docker compose down
docker compose up -d --build
```

### 명령어: 디버깅

### 컨테이너 내부 셸 접속

```bash
docker compose exec backend sh      # alpine 등 경량 이미지
docker compose exec backend bash    # ubuntu/debian 계열
```

### 컨테이너에서 네트워크 확인

```bash
docker compose exec backend cat /etc/resolv.conf   # DNS 설정 확인
docker compose exec backend ping db                # 서비스명으로 통신 확인
```

ping db가 성공하면 Compose 내부 DNS가 정상 동작 중임을 의미함. 서비스 이름이 호스트네임으로 자동 등록되기 때문임.

### 명령어: 네트워크 점검

### 네트워크 목록/상세

```bash
docker network ls                          # 생성된 네트워크 목록
docker network inspect <network_name>      # 어떤 컨테이너가 연결되어 있는지 확인
```

### 특정 컨테이너의 네트워크 연결 확인

```bash
docker inspect docker-compose-backend-1 | grep -i network -n
```

i: 대소문자 무시

n: 결과에 줄 번호 표시

### 네트워크 삭제

```bash
docker network rm <network_name>    # 특정 네트워크 삭제
docker network prune                # 어떤 컨테이너에도 연결되지 않은 네트워크 삭제
docker network prune -f             # 확인 없이 강제 삭제
```

### 명령어: 특정 compose 파일 지정

기본적으로 docker compose up은 현재 디렉토리 이름을 compose project name으로 사용함. 파일이나 프로젝트 이름을 명시적으로 지정하고 싶을 때 아래 옵션을 씀.

### f 옵션: 특정 yaml 파일 지정

```bash
docker compose -f docker-compose-app1.yaml ps
docker compose -f docker-compose-app2.yaml logs -f
```

### p 옵션: 프로젝트 이름 지정

```bash
docker compose -p app1 ps
docker compose -p app2 logs -f
```

같은 이름의 docker-compose.yaml이 app1/, app2/ 폴더에 각각 있을 때, p로 구분해 다른 프로젝트로 관리할 수 있음

docker compose -p myapp up -d → myapp을 project name으로 사용

### [실습] docker-compose 확장 — nginx 프록시 연동

### 구성 목표

frontend nginx가 정적 파일을 직접 서빙하고, /api/ 경로 요청은 backend 컨테이너로 **역방향 프록시(reverse proxy)**함.

### 1. docker-compose.yaml — frontend 서비스

```bash
frontend:
  build:
    context: ./frontend
    dockerfile: Dockerfile.frontend
  ports:
    - 8080:80
  volumes:
    - ./nginx.conf:/etc/nginx/conf.d/default.conf
```

nginx 설정 파일을 볼륨 마운트로 주입함. 컨테이너 내부의 default.conf를 호스트 nginx.conf로 덮어씀.

### 2. nginx.conf

```html
server {
    listen80;
    # 정적 파일 제공
    location / {
        root /usr/share/nginx/html;
        indexindex.html;
    }
    # 백엔드 API 프록시: /api/* → backend:8080/*
    location /api/ {
        proxy_pass       <http://backend:8080/>;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### nginx.conf 주요 변수

backend는 Compose 서비스 이름 → Compose 내부 DNS가 자동으로 IP로 해석함

proxy_set_header Host $host — 원래 Host 헤더를 유지해 backend가 도메인 정보를 알 수 있게 함

proxy_set_header X-Real-IP $remote_addr — 클라이언트 실제 IP를 backend에 전달 (nginx 뒤에서도 클라이언트 추적 가능)

### 3. 실행 및 접속

```bash
docker compose up --build -d
```

http://localhost:8080 접속 → nginx가 정적 파일 서빙

http://localhost:8080/api/... → nginx가 backend:8080으로 프록시

### command 필드

컨테이너 시작 시 실행할 기본 명령을 yaml에서 재정의하는 필드임. Dockerfile의 CMD를 덮어쓰되, ENTRYPOINT는 그대로 유지됨.

### Dockerfile vs docker-compose.yaml 비교

entrypoint를 compose에서 재정의하면 Dockerfile의 CMD가 무시되므로, command도 함께 재선언해야 함

ENTRYPOINT는 "실행 파일" 역할, CMD는 "기본 인자" 역할로 분리하는 것이 일반적임

### 이미지 빌드 및 실행 — build 블록 상세

### build 블록 구성 예시

```bash
services:
  app:
    build:
      context: ./app          # Dockerfile이 있는 디렉토리
      dockerfile: Dockerfile.prod   # 사용할 Dockerfile 파일명
      args:
        APP_ENV: prod         # 빌드 시 ARG로 전달되는 값
    ports:
      - "8080:8080"
```

### Dockerfile.prod 구조

```text
FROM eclipse-temurin:17-jre
ARG APP_ENV
ENV APP_ENV=${APP_ENV}
```

ARG는 빌드 시에만 존재하는 변수 → docker build --build-arg APP_ENV=prod 와 동일한 효과

ENV로 변환하면 런타임에도 환경변수로 유지됨

### up --build 와 build + up의 관계

```bash
docker compose up --build   # = docker compose build + docker compose up
```

두 명령을 순서대로 실행한 것과 동일하므로, 코드 변경 후 재빌드가 필요할 때 가장 자주 씀.

### 장애 발생 시 재시작 모드 설정 (restart)

컨테이너 비정상 종료 시 자동으로 재시작할 기준을 설정하는 필드임.

```text
services:
  db:
    image: postgres:9.6.1
    restart: always
```

### restart 정책 비교

always와 unless-stopped의 차이: 서버 재부팅 후 always는 무조건 재시작, unless-stopped는 docker stop으로 멈춘 상태였으면 재시작하지 않음

실운영 DB나 API 서버는 unless-stopped를 선호하는 경우가 많음

### Health Check

컨테이너 기동 중 주기적으로 상태를 확인해 healthy / unhealthy로 표시하는 기능임. 상태에 따른 자동 종료·복구는 지원하지 않으며(Kubernetes의 probe가 그 역할), 주로 depends_on의 condition: service_healthy와 함께 씀.

```text
services:
  db:
    image: postgres:9.6.1
    healthcheck:
      test: "curl -f <http://localhost:8080/health>"
      interval: 10s
      retries: 5
      start_period: 10s
```

### 각 필드 의미

### 환경변수 주입 방법

### 1. environment 옵션 — yaml 내 직접 선언

```text
# 방법 A: Key-Value 딕셔너리 형태 (추천 — 가독성 좋음)
environment:
  APP_ENV: production
  PORT: 8080
# 방법 B: List 형태 ("=" 기호 사용)
environment:
  - APP_ENV=production
  - PORT=8080
```

### 2. env_file 옵션 — 외부 파일 로딩

```text
# env.dev 파일:
# DB_HOST=localhost
# DB_USER=admin
# DB_PASS=secret123
services:
  backend:
    image: node:18
    env_file:
      - env.dev
```

파일 한 줄에 변수 하나씩, 여러 개를 한 번에 로딩 가능함. 민감한 값을 yaml에 노출하지 않아도 됨.

### 3. 기본 .env 파일 — compose가 자동으로 읽음

docker-compose.yaml과 같은 디렉토리의 .env 파일은 별도 지정 없이 자동으로 로딩됨. yaml 내에서 ${변수명} 형태로 참조 가능함.

```text
# .env 파일:
# PORT=3000
# DB_PASSWORD=my_secure_password
services:
  web:
    image: nginx
    ports:
      - "${PORT}:80"
    environment:
      DATABASE_PASS: ${DB_PASSWORD}
```

### 4. -e 옵션 — 명령어로 직접 주입

```bash
docker compose -e APP_ENV=prod up -d
```

${APP_ENV} 변수를 참조하는 서비스에만 적용됨.

### 5. --env-file 옵션 — 실행 시 파일 지정

```bash
docker compose --env-file .env.production up -d
docker compose --env-file config/my.env up -d
```

기본 .env 대신 다른 파일을 명시적으로 지정할 때 사용함. 환경별(dev/staging/prod) 설정 분리에 유용함.

### 네트워크 호출 — 서비스명으로 통신

같은 Compose 네트워크 내 컨테이너 간에는 서비스 이름이 곧 호스트네임으로 동작함. IP나 localhost로는 접근 불가함.

컨테이너 IP로도 통신은 가능하나, 컨테이너 재생성 시 IP가 바뀔 수 있으므로 서비스명 사용을 권장함

Compose가 자동으로 생성하는 bridge network 안에서 DNS 해석이 서비스명 → IP로 이루어짐

### 서비스 외부 노출 방법

### (1) ports — 호스트 포트에 공개 (가장 일반적)

```text
ports:
  - "8080:80"    # 호스트:8080 → 컨테이너:80
```

8080:80은 0.0.0.0:8080 → container:80과 동일

0.0.0.0 바인딩이므로 외부 모든 IP에서 접근 가능함

### (2) 특정 IP에만 바인딩 — 로컬 전용 노출

```text
ports:
  - "127.0.0.1:8080:80"    # 로컬(호스트)에서만 접근 가능
```

외부 PC에서 들어오는 호출은 차단되며, "외부 노출 차단(로컬 전용)"으로 많이 사용됨.

### 서비스 외부 차단 방법

### (1) ports 미지정 — 외부 노출 없음

```text
services:
  db:
    image: postgres
# ports: 없음
```

외부에서 직접 접근 불가

같은 Compose 네트워크 내 다른 서비스는 db:5432로 내부 접근 가능

### (2) expose — 내부 서비스에만 포트 명시

```text
services:
  backend:
    image: my-backend
    expose:
      - "8080"
```

외부 노출 없음, 호스트와 바인딩하지 않음

같은 네트워크의 다른 컨테이너가 접근할 수 있는 포트를 문서화 목적으로 명시하는 것에 가까움

### (3) networks 분리를 통한 접근 통제

```text
services:
  frontend:
    networks: [public]
  backend:
    networks: [public, private]
  db:
    networks: [private]
networks:
  public:
  private:
    internal: true    # 컨테이너 내부 → 외부 인터넷 차단
```

frontend ↔ backend: 통신 가능 (같은 public 네트워크)

frontend ↔ db: 통신 불가 (다른 네트워크)

backend ↔ db: 통신 가능 (같은 private 네트워크)

internal: true: 해당 네트워크의 컨테이너가 외부 인터넷으로 나가는 것도 차단함

external: true: 이미 존재하는 외부 bridge 네트워크를 compose에서 재사용할 때 사용

### 네트워크 분리 구조 (참고)

각 컨테이너는 소속 네트워크에 해당하는 가상 이더넷(veth)을 통해 bridge에 연결됨. backend만 두 네트워크(public + private)에 동시 연결되어 있으므로 eth0, eth1 두 인터페이스를 가짐.

### 서비스간 의존 관계 설정 — depends_on + healthcheck 연동

단순 depends_on은 컨테이너 시작 순서만 보장하며, 실제 서비스가 준비됐는지는 보장하지 않음. condition: service_healthy를 사용하면 healthcheck가 통과된 후에야 다음 서비스를 기동함.

```text
services:
  db:
    image: postgres:9.6.1
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 10s
  backend:
    image: my-backend
    depends_on:
      db:
        condition: service_healthy    # db가 healthy 상태가 될 때까지 대기
```

pg_isready -U postgres: postgres가 실제 쿼리를 받을 준비가 됐는지 확인하는 명령

start_period 동안의 실패는 retries에 포함되지 않으므로, 초기 기동 느린 서비스에 여유를 줄 수 있음

### [실습] docker-compose 확장하기 — 완성 구조 가이드

### 목표 구성

기존 base(db + backend)에 frontend를 추가하고, 네트워크 분리 + healthcheck + 의존 관계를 모두 적용하는 완성형 구조임.

### 최종 시작 순서 및 네트워크

```text
시작 순서: db (healthy) → backend (healthy) → frontend

네트워크:
  db       ↔ private
  backend  ↔ private + public
  frontend ↔ public
```

### db 서비스 구성 포인트

volumes: ./db_data:/var/lib/postgresql/data → 컨테이너 재생성 후에도 데이터 유지

network: private 전용 (외부 격리)

healthcheck: pg_isready -U postgres, 10초 주기, 대기 5초, 5회 반복, 시작 10초 유예

### backend 서비스 구성 포인트

build: ./backend/Dockerfile.backend

ports: 외부 9090 → 컨테이너 8080

networks: public + private

restart: unless-stopped

healthcheck: wget -qO- `<http://localhost:8080/health>`, 10초 주기, 대기 5초, 5회 반복, 시작 10초 유예

depends_on: db / condition: service_healthy

### frontend 서비스 구성 포인트

build: ./frontend/Dockerfile.frontend

ports: 외부 8080 → 컨테이너 80

networks: public

volumes: ./nginx.conf:/etc/nginx/conf.d/default.conf:ro

depends_on: backend / condition: service_healthy

restart: unless-stopped

### 검증 명령어

```bash
# 전체 빌드 및 실행
docker compose up --build -d
# 서비스 상태 확인
docker compose ps
# 로그 확인
docker compose logs -f backend
# 헬스체크 상태 상세 확인
docker inspect <container_name> --format '{{json .State.Health}}'
# 네트워크 확인
docker network ls
docker network inspect 03anwsers_public
docker network inspect 03anwsers_private
```

브라우저 접속 확인: localhost:8080 / localhost:8080/health / localhost:8080/users

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
