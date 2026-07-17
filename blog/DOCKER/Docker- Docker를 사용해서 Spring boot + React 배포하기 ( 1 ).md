---
title: "[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "backend", "docker", "frontend", "GCP", "react", "springboot", "배포"]
category: "DOCKER"
published: 2025-04-07
source_url: https://ch010104.tistory.com/45
---

# [Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )

## 원문

https://ch010104.tistory.com/45

## 노트 유형

`guide`

## 적용 목적과 전제조건

현재 진행 중인 동아리 게시물 웹 프로젝트가 어느덧 배포 단계까지 오게되었다.

구글에서 지원하는 GCP와 Docker를 사용해서 배포할 예정이다.

## 구현 절차·검증·주의점

현재 진행 중인 동아리 게시물 웹 프로젝트가 어느덧 배포 단계까지 오게되었다.

구글에서 지원하는 GCP와 Docker를 사용해서 배포할 예정이다.

배포 흐름

1. 내 인텔리제이 프로젝트에서 프론트엔드와 백엔드 프로젝트에 각각 DockerFile 및 .dockerignore 작성

2. 백엔드(./gradlew build -x test), 프론트엔드(npm run build) 로 앱 빌드

3. docker build -t 로 docker 이미지 파일로 빌드(Docker 설치 필요)

4. 프론트엔드 백엔드 docker 이미지에 각각 GCP 주요용 이름(tag) 붙이기

5. docker 이미지를 Artifact Registry로 푸쉬

6. 이후에는 VM을 사용해서 배포할지, Cloud Run을 이용해서 할건지 선택

7. 배포 후에, 도메인까지 연결하기!

우선은 5번까지의 이번 글에서 해보겠음.

### 📁 프로젝트 구조 (예시: 동아리 게시물 프로젝트)

```bash
/TeamProject2025
├── Dockerfile                  ← 백엔드용 Dockerfile
├── .dockerignore               ← 백엔드에서 제외할 파일들
├── build/libs/*.jar            ← Spring Boot 빌드 결과물 (JAR)
├── frontend/
│   ├── Dockerfile              ← 프론트엔드용 Dockerfile
│   ├── .dockerignore           ← 프론트에서 제외할 파일들
│   └── build/                  ← React 빌드 결과물
```

나의 동아리 게시물 프로젝트에서는 따로 backend 폴더가 존재하지 않고, TeamProject2025 프로젝트 파일 아래에 둠

### 1. 백엔드(Spring Boot)

1) 📄 Dockerfile (/TeamProject2025/Dockerfile)

```text
FROM openjdk:17-jdk-slim           # OpenJDK 17 기반의 슬림 이미지 사용
COPY build/libs/*.jar app.jar      # 빌드된 JAR 파일을 복사
ENTRYPOINT ["java", "-jar", "/app.jar"]  # 컨테이너 실행 시 JAR 실행
```

2) 📄 .dockerignore (/TeamProject2025/.dockerignore)

```text
.gradle
.git
.gitignore
.idea
*.iml
*.log
node_modules
```

이 파일은 Docker 이미지 빌드 시 불필요한 파일이나 폴더를 제외하기 위한 설정.

빌드 속도 개선과 보안에 도움이 됨.

3) 🛠️ 명령어 단계별

docker Desktop이 실행되어 있어야 가능

```text
# 1. Spring Boot 프로젝트 빌드
./gradlew build -x test
```

-x test는 테스트 코드를 생략하고 빌드할 때 사용

실패한 테스트 때문에 빌드가 막히는 걸 방지

```bash
# 2. Docker 이미지 빌드
docker build -t backend-image .
```

현재 디렉토리 기준으로 Dockerfile을 읽어 backend-image라는 이름의 이미지를 생성

```bash
# 3. GCP Registry에 올릴 수 있도록 태그 지정
docker tag backend-image asia-northeast3-docker.pkg.dev/{Project ID}/{artifact registry name}/backend:latest
```

docker tag는 이미지를 GCP Artifact Registry 형식으로 바꿔주는 작업

GCP 내에 docker 이미지를 업로드할 프로젝트를 생성하여, Project ID를 입력

GCP 내 프로젝트의 저장소를 생성(콘솔에 artifact registry를 입력) 하여 artifact registry 이름을 정한 후 입력

```bash
# 4. Docker 이미지 Artifact Registry에 업로드
docker push asia-northeast3-docker.pkg.dev/{Project ID}/{artifact registry name}/backend:latest
```

이 명령어로 백엔드 이미지를 GCP로 실제로 업로드

### ✅ 2. 프론트엔드(React)

1) 📄 Dockerfile (/TeamProject2025/frontend/Dockerfile)

```text
FROM node:18-alpine as build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

위 Dockerfile은 2단계 방식

1단계에서 React 앱을 빌드

2단계에서 Nginx를 통해 정적 파일을 서빙

2) 📄 .dockerignore (/TeamProject2025/frontend/.dockerignore)

```text
node_modules
build
.git
.idea
*.log
*.iml
```

3) 🛠️ 명령어 단계별

```text
cd frontend

# 1. React 앱 빌드
npm install
npm run build
```

React 프로젝트에서 정적 HTML, JS 파일을 생성하는 단계

```bash
# 2. Docker 이미지 빌드
docker build -t frontend-image .
```

```bash
# 3. 태그 지정
docker tag frontend-image asia-northeast3-docker.pkg.dev/{Project ID}/{artifact registry name}/frontend:latest
```

```bash
# 4. 이미지 GCP에 업로드
docker push asia-northeast3-docker.pkg.dev/{Project ID}/{artifact registry name}/frontend:latest
```

### ☁️ 3. 공통 준비: GCP 인증 설정 (최초 1회만)

```bash
# 1. Google 계정 인증
gcloud auth login

# 2. 프로젝트 설정
gcloud config set project {Project ID}

# 3. Docker 권한 인증 (Artifact Registry용)
gcloud auth configure-docker asia-northeast3-docker.pkg.dev
# artifact registry를 생성할 때, 지역을 asia_northeast3(서울), 타입을 docker로 설정함.
```

위 과정은 3단계 이전에 최초 1회만 해주면 되고, 이후에는 생략

GCP에서 artifact registry에 docker 이미지를 업로드 하기 위해서는 "소유자", "artifact registry 작성자" 권한이 필요함. -> GCP 콘솔 - IAM - 역할 추가

GCP에서 artifact registry를 사용하기 위해서는 결제 수단 등록이 필수적(무료버전만 사용하더라도 등록은 필수)

### 4. 확인

1) docker 이미지 파일 빌드 확인(2단계)

- docker Desktop을 켜서 docker 이미지가 추가되어있는지 확인

2) GCP artifact registry에 docker 이미지 파일 업로드 확인(4단계)

- GCP artifact registry내에 docker 이미지 파일이 추가되었는지 확인

### 5. 태그와 푸시 순서 요약표

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/SpringBoot- application.properties 환경 분리하기|[SpringBoot] application.properties 환경 분리하기]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
