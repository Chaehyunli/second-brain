---
title: "[Docker] Docker Compose 란??"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-20
source_url: https://ch010104.tistory.com/99
---

# [Docker] Docker Compose 란??

## 원문

https://ch010104.tistory.com/99

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

여러 개의 Docker 컨테이너를 하나의 서비스 단위로 정의하고, 일괄적으로 실행/관리할 수 있게 도와주는 도구

즉, 여러 개의 Container를 한 번에 묶어서 관리 가능!!

## 원문 기반 개념 정리

### 1. Docker Compose란?

여러 개의 Docker 컨테이너를 하나의 서비스 단위로 정의하고, 일괄적으로 실행/관리할 수 있게 도와주는 도구

즉, 여러 개의 Container를 한 번에 묶어서 관리 가능!!

1) 사용하는 이유

복잡한 애플리케이션 구성 간소화 - 여러 컨테이너(MySQL, Redis, Spring Boot, Frontend 등)를 하나의 compose.yml 파일에 정의해 일괄 실행 가능.

명령어 단순화 - 복잡한 Docker CLI 명령어 없이 docker compose up 한 줄이면 실행 가능. - 아래의 명령어를 compose.yml 파일 작성과 docker compose up 명령어를 이용하여 실행 가능

$ docker run -e MYSQL_ROOT_PASSWORD=pwd1234 -p 3306:3306 -v /Users/jaeseong/Documents/Develop/docker-mydb/sql_data:/var/lib/mysql -d mysql

환경별 구성 관리 - 개발/운영 환경을 나누거나 특정 서비스만 수정하는 작업이 수월해짐.

버전 관리에 용이 - 모든 설정이 .yml 파일에 있기 때문에 Git 등으로 이력을 관리하기 쉬움.

### 🛠️ 2. 기본 명령어 정리

⚠️ docker-compose (v1)는 더 이상 사용되지 않으며, docker compose (v2)를 사용할 것을 권장

### 📂 3. compose.yml 기본 구조

```text
services:
  서비스명:
    container_name: 컨테이너_이름
    image: 사용할_이미지
    build: .
    ports:
      - "호스트포트:컨테이너포트"
    volumes:
      - ./로컬경로:/컨테이너경로
    environment:
      - 환경변수=값
```

### 4. 실습 예제 모음

1) Nginx 웹서버 실행

```bash
#compose.yml
# docker run --name webserver -p 80:80 nginx 와 같은 기능
services:
  my-web-server:
    container_name: webserver
    image: nginx
    ports:
      - 80:80
```

🧪 실행 명령

```bash
docker compose up -d
```

2) Redis 캐시 서버 실행

```bash
# compose.yml
# docker run -p 6379:6379 redis 와 같은 기능
services:
  my-cache-server:
    image: redis
    ports:
      - 6379:6379
```

🧪 테스트 명령

```bash
docker exec -it [컨테이너명] bash
redis-cli
127.0.0.1:6379> set key value
127.0.0.1:6379> get key
```

3) MySQL 데이터베이스 실행

```bash
# compose.yml
# docker run -e MYSQL_ROOT_PASSWORD=pwd1234 -v C:\Users\chaeh\Documents\Develop\compose-practice/mysql_data:/var/lib/mysql -p 3306:3306 mysql 와 같은 기능
services:
  my-db:
    image: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=pwd1234
    volumes:
      - ./mysql_data:/var/lib/mysql # compose.yml 파일이 있는 경로에서 상대 경로로 볼륨을 지정 가능
    ports:
      - 3306:3306
```

```bash
docker compose up -d
```

볼륨 확인

MySQL 데이터는 ./mysql_data 폴더에 지속적으로 저장

4) 백엔드: Spring Boot 실행

```bash
# Dockerfile
FROM openjdk:17-jdk
COPY build/libs/*SNAPSHOT.jar /app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

```bash
# compose.yml
# ./gradlew clean build
# docker build -t my-app .
# docker run -p 8080:8080 my-app 와 같은 기능
services:
  my-server:
    build: .
    ports:
      - 8080:8080
```

🧪 빌드 및 실행

```bash
./gradlew clean build
docker compose up -d --build
```

5) 백엔드: Nest.js 실행

```bash
# Dockerfile
FROM node
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000
ENTRYPOINT ["node", "dist/main.js"]
```

```bash
# compose.yml
# docker build -t my-server .
# docker run -p 3000:3000 my-server 와 같은 기능
services:
  my-server:
    build: .
    ports:
      - 3000:3000
```

```bash
docker compose up -d --build
```

6) 프론트엔드: Next.js 실행

```bash
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000
ENTRYPOINT ["npm", "run", "start"]
```

```bash
# compose.yml
# docker build -t web-server .
# docker run -p 80:3000 web-server 와 같은 기능
services:
  my-web-server:
    build: .
    ports:
      - 80:3000
```

```bash
docker compose up -d --build
```

7) 정적 HTML/CSS + Nginx 실행

```text
# index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>My Web Page</h1>
</body>
</html>
```

```bash
# Dockerfile
FROM nginx
COPY ./ /usr/share/nginx/html
```

```bash
# compose.yml
# docker build -t web-server .
# docker run -p 80:80 web-server 와 같은 기능
services:
  my-web-server:
    build: .
    ports:
      - 80:80
```

### 5. Docker CLI ↔ Compose 변환 사이트

### 6. 컨테이너 정리

```bash
docker compose down
```

모든 컨테이너, 네트워크를 정리합니다.(생성된 컨테이너를 삭제함. 연결된 볼륨은 삭제 x) 데이터가 삭제되지 않도록 주의!!

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
- [[blog/DOCKER/Docker- DockerCompose에 2개 이상의 Container 관리하기|[Docker] DockerCompose에 2개 이상의 Container 관리하기]]
- [[blog/DOCKER/Docker- Docker Container 데이터 유실 방지하기 - Volume 사용하기|[Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기]]
