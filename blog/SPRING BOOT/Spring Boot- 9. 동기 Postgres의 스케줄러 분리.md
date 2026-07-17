---
title: "[Spring Boot] 9. 동기 Postgres의 스케줄러 분리"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/207
---

# [Spring Boot] 9. 동기 Postgres의 스케줄러 분리

## 원문

https://ch010104.tistory.com/207

## 노트 유형

`guide`

## 적용 목적과 전제조건

현재 프로젝트의 성능을 극대화하기 위해 Full-Async 지향 구조를 설계했습니다.

Reactive Redis: Upstash 캐시 접근 비동기화.

## 구현 절차·검증·주의점

### 1. 서두: 성능 최적화를 위한 아키텍처 설계 상황

현재 프로젝트의 성능을 극대화하기 위해 Full-Async 지향 구조를 설계했습니다.

WebClient: FastAPI와의 외부 통신 비동기화.

Reactive Redis: Upstash 캐시 접근 비동기화.

Postgres (JPA): 유일한 동기(Blocking) 구간인 DB 접근을 스케줄러 분리를 통해 해결.

### 2. 전략: 스케줄러 분리와 자원 동기화

Postgres는 현재 JPA(동기) 방식을 사용하므로, 메인 비동기 일꾼(Event Loop)이 DB 작업 때문에 멈추는 것을 방지하기 위해 **boundedElastic**이라는 별도의 주차장(스레드 풀)을 할당했습니다.

### 🔧 설정 1: 환경 변수 (.env 또는 application.properties)

DB 커넥션(열쇠)의 개수를 명확히 정의합니다.

```text
# application.properties
spring.datasource.hikari.maximum-pool-size=20
```

### 🔧 설정 2: 스케줄러 설정 (DatabaseConfig.java)

비동기 일꾼의 수를 열쇠 수와 일치시킵니다.

```java
@Configuration
public class DatabaseConfig {
    @PostConstruct
    public void init() {
        // 일꾼(Thread)의 수를 열쇠(Connection) 수와 동일하게 20개로 제한
        System.setProperty("reactor.schedulers.defaultBoundedElasticSize", "20");
    }
}
```

### 3. 왜 '열쇠'와 '일꾼'의 수가 동일해야 하는가?

이것이 이번 최적화의 핵심입니다.

일꾼(Thread) > 열쇠(Connection): 일꾼은 많은데 열쇠가 부족하면, 남은 일꾼들은 열쇠가 날 때까지 주차장에서 대기하며 메모리만 낭비하고 컨텍스트 스위칭 비용만 발생시킵니다.

일꾼(Thread) < 열쇠(Connection): 열쇠는 남는데 일꾼이 없으면 DB의 처리 능력을 100% 활용하지 못합니다.

결론: **1:1 매칭(20개:20개)**을 통해 일꾼이 일을 시작하자마자 열쇠를 쥐고 DB에 접근할 수 있는 최적의 병목 제거 상태를 구현했습니다.

### 4. 실제 사용 코드

동기 DB 작업을 Mono.fromCallable로 감싸고 전용 일꾼에게 맡기는 방식입니다.

```text
public Mono<AnalysisResult> saveToDb(AnalysisResult data) {
    return Mono.fromCallable(() -> repository.save(data))
               .subscribeOn(Schedulers.boundedElastic()); // 20명의 전용 일꾼 중 하나 사용
}
```

### 5. 회고 요약

완벽한 비동기 DB(R2DBC)로 가기 전, 기존 JPA의 안정성을 유지하면서도 서버 전체의 응답성을 확보할 수 있는 최선의 하이브리드 전략을 성공적으로 구축했습니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 7. Spring Boot CORS 중복 응답(web & webflux 충돌)|[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
