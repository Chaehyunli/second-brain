---
title: "[Dokcer] Docker란 무엇일까?? (Container 란??, Image 란??)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-17
source_url: https://ch010104.tistory.com/95
---

# [Dokcer] Docker란 무엇일까?? (Container 란??, Image 란??)

## 원문

https://ch010104.tistory.com/95

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

서로 다른 환경에서도 똑같은 결과를 보장한다는 것이 Docker의 가장 큰 장점!!

친구는 MySQL을 잘 설치했는데, 나는 같은 방식으로 설치했는데도 오류가 뜬다?

## 원문 기반 개념 정리

### 🐳 1. 왜 Docker를 배워야 할까?

핵심 이유: 이식성 (Portability)

서로 다른 환경에서도 똑같은 결과를 보장한다는 것이 Docker의 가장 큰 장점!!

❓ 예를 들어서

친구는 MySQL을 잘 설치했는데, 나는 같은 방식으로 설치했는데도 오류가 뜬다?

이유는 다양:

OS 차이 (Windows vs Mac)

버전 충돌

보안 프로그램 간 충돌

이런 복잡한 상황을 Docker는 한 줄 명령어로 해결

```bash
docker run mysql
```

💡 설치 과정 X, 환경 설정 X → 바로 실행!

### 🧩 2. Docker의 핵심 개념 세 가지

1) Docker란?

하나의 컴퓨터 안에 여러 개의 독립된 미니 컴퓨터 환경(컨테이너)을 만들 수 있는 툴

2) 컨테이너(Container)란?

독립적인 실행 환경

각 컨테이너는 자기만의 저장공간, IP 주소, 포트 등을 가짐

다른 컨테이너와는 충돌하지 않음

🧠 비유:

윈도우의 사용자 계정처럼 각각 독립된 공간

= 미니 컴퓨터라고 생각

3. 이미지(Image)란?

실행 가능한 프로그램을 미리 저장해놓은 ‘템플릿’

설치 과정, 환경 설정, 버전 정보가 모두 포함된 스냅샷

예: nginx, mysql, node 서버를 이미지로 실행 가능

컨테이너와 컨테이너를 포함하고 있는 컴퓨터를 구분하기 위해 컨테이너를 포함하고 있는 컴퓨터를 ‘ 호스트 (host) 컴퓨터 ʼ라고 부름

```bash
docker pull mysql            # 이미지 다운로드
docker run -d --name my-db mysql  # 이미지 → 컨테이너 생성 및 실행
```

즉, docker Image를 통해 나의 호스트 컴퓨터에 docker Container를 만드는 것!!

docker Image가 음식을 만들기 위한 레시피라면, docker Container는 진짜 음식!!

4. Dokcer 설치

윈도우에 도커 데스크탑 설치

### 🌐 3. 보충: IP와 포트 개념

1) IP란?

네트워크 상에서 특정 컴퓨터의 주소

예: 13.250.15.132

2) Port란?

한 컴퓨터 내에서 특정 프로그램을 구분하는 주소

예: 13.250.15.132:3000 → 해당 컴퓨터의 3000번 포트에서 실행 중인 프로그램과 통신

🔍 왜 포트를 지정해야 할까?

하나의 컴퓨터에서 여러 프로그램 실행 중

외부에서는 IP만으로는 어떤 프로그램에 연결해야 할지 알 수 없음

그래서 포트 번호까지 알아야 통신 가능

🌐 웹 브라우저는 왜 포트를 안 써도 될까?

기본 포트가 자동 설정됨:

http: 80번

https: 443번

그래서 naver.com이라고만 입력해도 자동으로 80 포트로 연결

### 🔧4. 실습 예제: Nginx 컨테이너 실행

```bash
# 1. 이미지 다운로드
docker pull nginx

# 2. 다운로드된 이미지 확인
docker image ls

# 3. 컨테이너 실행 (80포트 매핑)
# 이미지를 컨테이너에 올려 Nginx 서버 실행시키기
# nginx 라는 이미지를 사용해서 detach 모드(백그라운드 실행)으로 80 포트에서 webserver 라는 이름의 컨테이너를 생성 후 실행
docker run --name webserver -d -p 80:80 nginx

# 4. 실행 중 컨테이너 확인
# localhost:80 에 접속하면 Ngnix 컨테이너의 webserver 화면이 보임
docker ps

# 5. 컨테이너 종료
docker stop webserver
# localhost:80 에 접속하면 아무것도 나오지 않음
```

### 💡5. 정리

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker CLI 익히기|[Docker] Docker CLI 익히기]]
- [[blog/DOCKER/Docker- Docker Container 데이터 유실 방지하기 - Volume 사용하기|[Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
