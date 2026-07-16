---
title: "[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/205
---

# [Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)

## 원문

https://ch010104.tistory.com/205

## 노트 유형

`troubleshooting`

## 문제·재현 맥락

프로젝트 구조: React Native(Web/App) → Spring Boot(Java) → FastAPI(Python) 문제 현상: 웹 브라우저에서 Java 서버로 API 호출 시, 아래와 같은 CORS 에러 발생하며 통신 차단.

CORS policy: The 'Access-Control-Allow-Origin' header contains multiple values 'http://localhost:8081, http://localhost:8081', but only one is allowed.

## 원인·해결 근거

### 1. 배경 및 문제 식별

프로젝트 구조: React Native(Web/App) → Spring Boot(Java) → FastAPI(Python) 문제 현상: 웹 브라우저에서 Java 서버로 API 호출 시, 아래와 같은 CORS 에러 발생하며 통신 차단.

CORS policy: The 'Access-Control-Allow-Origin' header contains multiple values 'http://localhost:8081, http://localhost:8081', but only one is allowed.

핵심 원인: 서버 응답 헤더에 Access-Control-Allow-Origin 값이 하나가 아니라 두 번 중복되어 포함됨.

### 2. 초기 분석 및 환경 확인

### 의존성 (build.gradle)

전통적인 REST API를 위한 spring-boot-starter-web과 FastAPI와의 비동기 통신을 위한 spring-boot-starter-webflux를 동시에 사용.

```java
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation ('org.springframework.boot:spring-boot-starter-webflux') {
       exclude group: 'org.springframework.boot', module: 'spring-boot-starter-netty'
    }
}
```

시도: 서버 엔진 충돌을 막기 위해 WebFlux에서 Netty를 제외하고 Tomcat으로 단일화함.

### CORS 설정 (WebConfig.java)

처음에는 WebMvcConfigurer를 사용했으나, 우선순위 문제 해결을 위해 CorsFilter를 Bean으로 직접 등록하는 정석적인 방식을 채택함.

```text
@Bean
public CorsFilter corsFilter() {
    UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
    CorsConfiguration config = new CorsConfiguration();
    config.setAllowCredentials(true);
    config.addAllowedOriginPattern("*");
    config.addAllowedHeader("*");
    config.addAllowedMethod("*");
    source.registerCorsConfiguration("/**", config);
    return new CorsFilter(source);
}
```

### 3. 해결 시도 과정 및 시행착오

좀비 프로세스 확인: netstat과 taskkill을 통해 이전 설정이 남은 서버가 중복 실행 중인지 확인 (확인 결과 단일 실행 중).

브라우저 캐시 및 확장 프로그램: 시크릿 모드 테스트를 통해 브라우저 자체의 헤더 추가 가능성 배제.

필터 우선순위 조정: FilterRegistrationBean을 사용하여 Ordered.HIGHEST_PRECEDENCE로 설정했으나 여전히 중복 발생.

Postman 검증: Postman 결과에서 Vary 헤더와 CORS 관련 값이 중복되는 것을 확인하여 **"서버 내부 로직의 중복"**임을 확정함.

### 4. 최종 해결: 리턴 타입의 변경

### 기존 코드 (문제 발생)

```text
@GetMapping("/connect")
public Mono<String> connectToPython() {
    return webClient.get()...bodyToMono(String.class);
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

원인: 컨트롤러가 Mono(WebFlux 타입)를 반환하면, Spring은 MVC 필터 외에 WebFlux 전용 응답 핸들러를 추가로 가동함. 이 과정에서 CORS 헤더가 한 번 더 붙게 됨.

### 수정 코드

```text
@GetMapping("/connect")
public String connectToPython() { // 리턴 타입을 일반 String으로 변경
    return webClient.get()
            .uri("/api/test/python-test")
            .retrieve()
            .bodyToMono(String.class)
            .block(); // 비동기 결과를 동기적으로 변환
}
```

결과: 리턴 타입을 String으로 바꾸어 Spring MVC(Tomcat) 엔진이 응답을 전담하게 함. WebFlux 핸들러의 개입이 차단되면서 헤더 중복 문제가 해결됨.

의문점: 이 방식을 사용하면 weflux를 사용하는 비동기의 이점이 없어짐. → 동기 방식인 web 라이브러리를 사용하지 않고, 비동기의 weflux로 리펙토링

### 최종 수정 코드(해결)

```java
package com.mju.capstone_backend.domain.test.controller; // 수정한 패키지 경로

import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Tag(name = "Test API", description = "프론트-자바-파이썬 통신 확인을 위한 테스트용 API")
@RestController
@RequestMapping("/api/test")
@RequiredArgsConstructor
public class TestController {

    @Value("${ai.agent.url}")
    private String aiAgentUrl; // 로그 찍기용 url 변수
    private final WebClient webClient;

    @GetMapping("/connect")
    public Mono<String> connectToPython() {
        String javaMessage = "✅ [Spring Boot 응답]: " + aiAgentUrl + " 로 토스합니다.\\n";

        return webClient.get()
                .uri("/api/test/python-test")
                .retrieve()
                .bodyToMono(String.class)
                .map(pythonResponse -> javaMessage + "✅ [FastAPI 응답]: " + pythonResponse)
                .onErrorResume(e -> Mono.just(javaMessage + "⚠️ [Error]: 파이썬 서버 연결 실패!"));
    }
}
```

### 5. 교훈 및 결론

라이브러리 혼용 주의: 한 프로젝트에 MVC와 WebFlux 라이브러리가 공존할 경우, 의도치 않게 두 엔진의 자동 설정이 모두 작동할 수 있다.

정확한 도구 활용: netstat을 통한 프로세스 확인과 Postman을 이용한 원본 헤더 분석이 문제의 범위를 좁히는 데 결정적인 역할을 했다.

동기 vs 비동기: 비동기 처리가 필수적인 프로젝트의 성격에 맞게 라이브러리를 선택하여 조치했다.(기존에 동기 방식으로 설정되어 있던 redis와 postgres도 비동기 방식으로 수정 고려)

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리|[Spring Boot] 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
