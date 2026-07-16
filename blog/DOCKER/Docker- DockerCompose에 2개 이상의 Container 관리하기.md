---
title: "[Docker] DockerCompose에 2개 이상의 Container 관리하기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-20
source_url: https://ch010104.tistory.com/100
---

# [Docker] DockerCompose에 2개 이상의 Container 관리하기

## 원문

https://ch010104.tistory.com/100

## 노트 유형

`guide`

## 적용 목적과 전제조건

📌 주의: YAML 문법에서는 들여쓰기가 매우 중요. 공백 실수는 에러의 주원인!!!

https://start.spring.io 에서 아래와 같이 설정 후 프로젝트를 생성

## 구현 절차·검증·주의점

### 1. 기본 구성: Docker Compose로 MySQL, Redis 실행하기

```text
# compose.yml
services:
  my-server: # springboot 서버
    build: .
    ports:
      - 8080:8080

  my-db: # mysql 서버
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: pwd1234
    volumes:
      - ./mysql_data:/var/lib/mysql
    ports:
      - 3306:3306

  my-cache-server: # redis 서버
    image: redis
    ports:
      - 6379:6379
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

📌 주의: YAML 문법에서는 들여쓰기가 매우 중요. 공백 실수는 에러의 주원인!!!

실행하기

```bash
$ docker compose up -d
```

실행 상태 확인

```bash
$ docker compose ps
$ docker ps
```

컨테이너 종료 및 삭제

```bash
$ docker compose down
```

### 2. Spring Boot + MySQL 연동 컨테이너 구성

1) Spring Boot 프로젝트 생성

https://start.spring.io 에서 아래와 같이 설정 후 프로젝트를 생성

Java 17

Dependencies:

Spring Web

Spring Boot DevTools

Spring Data JPA

MySQL Driver

기본적으로 생성 후에 test 코스가 있는데, 빌드할 때 에러를 발생시키므로 삭제!(테스트 코드 작성 설정을 하면 무관)

🧾 2) 간단한 컨트롤러 코드 작성

```java
# AppController.java
@RestController
public class AppController {
    @GetMapping("/")
    public String home() {
        return "Hello, World!";
    }
}
```

```text
# application.yml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb # localhost는 자기 자신의 컴퓨터를 가리킴. springboot container안에서 3306 port를 봐도 mysql container는 없음!!
    username: root
    password: pwd1234
    driver-class-name: com.mysql.cj.jdbc.Driver
```

❌ 왜 연결이 안 될까?(그림에서 보면, mysql DB는 잘 생성되었는데, springboot container에서 찾지 못하는 것!)

Docker 컨테이너는 서로 고립된 네트워크를 사용

Spring Boot 컨테이너 입장에서 localhost는 자신의 컨테이너를 의미

즉, localhost:3306은 MySQL이 아닌 자기 자신을 가리키는 주소!!

📌 해결 방법: 같은 Compose 네트워크 내에서 서비스 이름을 호스트 주소로 사용

3) 수정된 application.yml

```text
# application.yml
spring:
  datasource:
    url: jdbc:mysql://my-db:3306/mydb #
    username: root
    password: pwd1234
    driver-class-name: com.mysql.cj.jdbc.Driver
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

여기서 my-db는 compose.yml의 서비스 이름입니다. 내부 DNS처럼 작동

🧱 4) Dockerfile 작성

```text
# Dockefile
FROM openjdk:17-jdk
COPY build/libs/*SNAPSHOT.jar /app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

🧾 5) 전체 compose.yml 구성 (MySQL 포함)

```text
services:
  my-server:
    build: .
    ports:
      - 8080:8080
    depends_on:
      my-db:
        condition: service_healthy # springboot 서버는 mysql과 redis가 완료된 뒤에 실행 가능

  my-db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: pwd1234
      MYSQL_DATABASE: mydb
    volumes:
      - ./mysql_data:/var/lib/mysql
    ports:
      - 3306:3306
    healthcheck: # my-db 서버를 먼저 실행하고 테스트해서 성공 나오면 my-server를 실행
      test: ["CMD", "mysqladmin", "ping"] # 테스트 명령어
      interval: 5s # 5초 주기로 테스트
      retries: 10 # 최대 10번까지 테스트
```

### 3. Redis 연동까지 추가하기

1) 의존성 추가 (build.gradle)

```java
# build.gradle
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-data-redis'
}
```

🧾 2) application.yml에 Redis 설정 추가

```text
# application.yml
spring:
  datasource:
    url: jdbc:mysql://my-db:3306/mydb
    username: root
    password: pwd1234
    driver-class-name: com.mysql.cj.jdbc.Driver

  data:
    redis:
      host: my-cache-server # 이 부분!! localhost말고 redis container의 이름으로 적어야함.
      port: 6379
```

처음에 localhost로 작성하면 에러 발생 → Redis도 컨테이너이므로 my-cache-server로 접근해야 함

⚙️ 3) Redis 설정 클래스 작성

```java
# RedisConfig.java
@Configuration
public class RedisConfig {
    @Bean
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<String, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);
        template.setKeySerializer(new StringRedisSerializer());
        template.setValueSerializer(new GenericJackson2JsonRedisSerializer());
        return template;
    }
}
```

🎮 4) Redis 테스트용 API

```java
# AppController
@RestController
public class AppController {
    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    @GetMapping("/")
    public String home() {
        redisTemplate.opsForValue().set("abc", "def");
        return "Hello, World!";
    }
}
```

🧾 5) 최종 compose.yml 구성 (MySQL + Redis)

```text
# compose.yml
services:
  my-server:
    build: .
    ports:
      - 8080:8080
    depends_on:
      my-db:
        condition: service_healthy
      my-cache-server:
        condition: service_healthy

  my-db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: pwd1234
      MYSQL_DATABASE: mydb
    volumes:
      - ./mysql_data:/var/lib/mysql
    ports:
      - 3306:3306
    healthcheck:
      test: [ "CMD", "mysqladmin", "ping" ]
      interval: 5s
      retries: 10

  my-cache-server:
    image: redis
    ports:
      - 6379:6379
    healthcheck:
      test: [ "CMD", "redis-cli", "ping" ]
      interval: 5s
      retries: 10
```

🚀 6) 실행 순서

```bash
# 1. 빌드
$ ./gradlew clean build

# 2. 이전 컨테이너 종료
$ docker compose down

# 3. 새로 실행
$ docker compose up --build -d

# 4. 실행 상태 확인
$ docker compose ps
$ docker ps
```

브라우저에서 http://localhost:8080 접속하면 Redis에 abc=def 값이 저장되고 "Hello, World!" 응답이 반환!!

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker Compose 란|[Docker] Docker Compose 란??]]
- [[blog/DOCKER/Docker- AWS EC2에 서버 배포하기(Express 서버 배포하기)|[Docker] AWS EC2에 서버 배포하기(Express 서버 배포하기)]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
