---
title: "[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/195
---

# [Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)

## 원문

https://ch010104.tistory.com/195

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

원래 Java에서 외부 서버에 데이터를 요청하려면 RestTemplate이나 WebClient를 써서 복잡한 코드를 짜야 했습니다.

주소 조립하고, 헤더 넣고, 예외 처리하고... 코드가 너무 길어집니다.

## 원문 기반 개념 정리

### 1. FeignClient란 무엇인가?

### 왜 사용하는가? (The Why)

원래 Java에서 외부 서버에 데이터를 요청하려면 RestTemplate이나 WebClient를 써서 복잡한 코드를 짜야 했습니다.

주소 조립하고, 헤더 넣고, 예외 처리하고... 코드가 너무 길어집니다.

FeignClient는 이 모든 과정을 생략하고 "인터페이스만 선언하면 알아서 구현체를 만들어주는" 도구입니다. 마치 Mybatis나 JPA 쓰듯이 메서드 호출만으로 외부 API를 쓸 수 있게 해줍니다.

### 언제 사용하는가? (The When)

MSA(마이크로서비스) 구조에서 서버 A가 서버 B의 데이터가 필요할 때.

AI 에이전트처럼 Spring이 메인 로직을 담당하고, 실제 계산이나 AI 추론은 Python 서버가 담당할 때.

외부 공공 API(날씨, 지도 등)를 가져와야 할 때.

### 2. Spring ↔ Spring 통신 (내부망 통신)

같은 Java 환경끼리의 통신이므로 객체 구조가 복잡해도 공유하기 쉽습니다.

### [Java] 1. 의존성 및 설정

파일명: build.gradle

```java
dependencies {
    implementation 'org.springframework.cloud:spring-cloud-starter-openfeign'
}
```

파일명: CommonConfig.java (또는 Application 클래스)

```java
@Configuration
@EnableFeignClients(basePackages = "kr.or.kosti.yestrade") // Feign 활성화
public class FeignConfig { }
```

### [Java] 2. API 클라이언트 인터페이스

파일명: OrderApiClient.java

```text
@FeignClient(name = "order-service", url = "<http://localhost:8081>")
public interface OrderApiClient {

    // @SpringQueryMap: 중요! GET 요청 시 객체를 ?page=1&size=10 형태의 쿼리 스트링으로 변환함
    @GetMapping("/api/orders")
    PageResponse<OrderDto> getOrders(@SpringQueryMap OrderSearchRequest request);
}
```

### [Java] 3. 실제 서비스 로직

파일명: OrderService.java

```java
@Service
@RequiredArgsConstructor
public class OrderService {
    private final OrderApiClient orderApiClient; // 주입받아서

    public void process() {
        // 마치 내 로직인 것처럼 메서드 호출만 하면 8081 서버로 요청이 날아감
        var response = orderApiClient.getOrders(new OrderSearchRequest(1, 10));
    }
}
```

### 3. Spring ↔ Python 통신 (AI 에이전트 구조)

Spring(클라이언트)이 요청을 보내고 Python(서버)이 응답하는 구조입니다. AI 에이전트 구축 시 가장 많이 쓰이는 형태입니다.

### [Java] 1. API 클라이언트 (Spring 측)

파일명: AiAgentClient.java

```text
@FeignClient(name = "ai-agent", url = "<http://localhost:8000>")
public interface AiAgentClient {

    @PostMapping("/agent/analyze") // AI는 보통 데이터가 커서 POST를 선호함
    AiResponse analyzeData(@RequestBody AiRequest request);
}
```

### [Python] 2. FastAPI 서버 (Python 측)

파일명: main.py

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AiRequest(BaseModel):
    task: str
    data_list: list

@app.post("/agent/analyze")
async def process_ai(request: AiRequest):
    # Spring이 보낸 JSON이 request 객체로 자동 변환됨
    result = {"answer": f"{request.task} 완료", "score": 0.98}
    return result # Python dict를 리턴하면 자동으로 JSON으로 변환되어 Spring에 전달됨
```

### 4. 상세 동작 원리 (보낼 때 vs 받을 때)

많은 분이 헷갈려 하는 부분입니다.

### ① 보낼 때 (객체 → HTTP 요청)

Spring 역할: 내가 넘긴 자바 객체를 텍스트(JSON 또는 Query String)로 바꿉니다.

핵심 어노테이션:

@SpringQueryMap: 객체를 ?key=value 형태의 주소로 바꿀 때 (GET)

@RequestBody: 객체를 JSON 덩어리로 바꿀 때 (POST)

주의: 아까 404 에러가 난 이유는 @SpringQueryMap이 없어서 Spring이 주소를 조립하지 못하고 objectMapper 같은 내부 시스템 변수까지 주소에 다 집어넣었기 때문입니다.

### ② 받을 때 (HTTP 응답 → 객체)

상대 서버(Python/Spring) 역할: 결과를 JSON 텍스트로 보냅니다.

Spring 역할: 받은 JSON 텍스트를 내 DTO 클래스 필드명에 맞춰서 값을 하나하나 채워줍니다.

핵심 라이브러리: Jackson (자동으로 작동함)

### 5. 요약: 이것만 기억하세요!

항목 Spring끼리 통신할 때 Python(AI)과 통신할 때

### 6.주요 API 서비스별 발급처서비스발급처

기상청/공공데이터: 공공데이터포털(날씨, 미세먼지, 버스 정보 등 국가 데이터)

카카오 지도/로그인: Kakao Developers (지도, 카카오톡 공유, 소셜 로그인)

네이버 지도/검색: NAVER Cloud Platform(지도, 검색, 클로바(AI))

토스 페이먼츠: 토스페이먼츠 개발자센터(결제창 연동, 정기 결제, 계좌 조회)

구글/유튜브: Google Cloud Console(구글 지도, 유튜브 데이터, 번역)

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
