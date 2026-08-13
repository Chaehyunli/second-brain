---
title: "[8/13] Java, SpringBoot, Rest API 구현_Day4_핵심 정리"
notion_page_id: "3ba1d84b-f68e-804c-8c17-e7b9f02decff"
source_url: "https://app.notion.com/p/3ba1d84bf68e804c8c17e7b9f02decff"
synced_at: "2026-08-14T00:06:56+09:00"
content_sha256: "8307321542d1bf8a109b238e4681dc9daa76ecfb179e395d8887e141294e012e"
tags: [notion, skala, learning, java, spring-boot, rest-api]
---

# [8/13] Java, SpringBoot, Rest API 구현_Day4_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

[[notion/SKALA/8-12 Java, SpringBoot, Rest API 구현_Day3/[8-12] Java, SpringBoot, Rest API 구현_Day3_핵심 정리|Day3 — 객체 생성 패턴·REST API]]

> 원문: [Notion 페이지](https://app.notion.com/p/3ba1d84bf68e804c8c17e7b9f02decff) (2026-08-14 KST 확인)

### Lombok이란
Java 개발에서 반복적으로 작성해야 하는 보일러플레이트 코드(boilerplate code)를 줄이고 가독성을 높이기 위해 사용하는 라이브러리임.
보일러플레이트 코드란 본질적인 비즈니스 로직과 무관하지만 언어 구조상 반드시 작성해야 하는 반복 코드를 가리킴. Java에서는 객체 필드를 다룰 때 필요한 `getter()`, `setter()`, `equals()`, `hashCode()`, `toString()` 메서드가 대표 사례임. Lombok은 이 메서드들을 어노테이션 하나로 컴파일 시점에 자동 생성해 줌.
---
### 주요 Lombok 어노테이션
| 어노테이션 | 역할/설명 | 적용 위치 |
| --- | --- | --- |
| `@Getter` | 모든 필드에 대해 getter 메서드 자동 생성 | 클래스 |
| `@Setter` | 모든 필드에 대해 setter 메서드 자동 생성 | 클래스 |
| `@ToString` | `toString()` 메서드 자동 생성 | 클래스 |
| `@EqualsAndHashCode` | `equals()`와 `hashCode()` 메서드 자동 생성 | 클래스 |
| `@NonNull` | 해당 필드에 null을 넣으면 즉시 `NullPointerException` 발생 | 필드 |
| `@NoArgsConstructor` | 파라미터 없는 기본 생성자 자동 생성 | 클래스 |
| `@AllArgsConstructor` | 모든 필드를 파라미터로 받는 생성자 자동 생성 | 클래스 |
| `@RequiredArgsConstructor` | `final` 또는 `@NonNull` 필드만 모아서 생성자 자동 생성 | 클래스 |
| `@Data` | `@Getter` + `@Setter` + `@ToString` + `@EqualsAndHashCode` + `@RequiredArgsConstructor`를 한 번에 적용 | 클래스 |
| `@Builder` | 빌더 패턴 자동 생성 (객체 생성 유연화) | 클래스 |
| `@Slf4j` | `log` 변수(Logger 객체) 자동 생성 | 클래스 |
---
### Lombok 적용 예시
Lombok 적용 전후 코드 비교로 코드량 차이를 확인할 수 있음.
적용 전에는 기본 생성자, 전체 필드 생성자, getter/setter, `toString()`, `equals()`, `hashCode()`를 모두 직접 작성해야 함.
```java
// 적용 전
public class User {
    private Long id;
    private String name;

    public User() {}

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "'}";
    }

// equals(), hashCode() 생략
}
```
```java
// Lombok 적용 후
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private Long id;
    private String name;
}
```
`@Data` 하나가 `@Getter`, `@Setter`, `@ToString`, `@EqualsAndHashCode`, `@RequiredArgsConstructor`를 모두 포함하므로, 클래스 본문은 필드 선언만 남음.
---
### \[참고\] record를 이용한 Immutable 객체 만들기
Java 16부터 정식 지원되는 `record`는 불변(Immutable) 데이터 객체를 간결하게 정의하기 위한 문법임. constructor, getter, `toString`, `equals`, `hashCode`가 자동 생성되며, setter는 제공되지 않아 생성 후 필드 값 변경이 불가함. 주로 DTO 정의에 활용됨.
```java
import lombok.Value;

public record Stock(String symbol, String name, int price) { }

// 사용 예
Stock stock = new Stock("005930", "삼성전자", 80000);
System.out.println(stock.name()); // "삼성전자"

// stock.price(90000); // 컴파일 오류 — setter 없음, 값 변경 불가
```
record의 getter는 `getXxx()` 형식이 아니라 `필드명()`으로 호출하는 점에 유의함.
---
### Lombok — @Slf4j
클래스에 `@Slf4j`를 붙이면 `private static final org.slf4j.Logger log` 필드가 자동 생성됨. `System.out.println` 대신 로그 레벨을 구분해 출력할 수 있어 실무에서 표준적으로 사용함.
```java
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class StockService {
    public void printStock(Stock stock) {
        log.info("Stock 정보: {}", stock);
        log.debug("디버깅 로그입니다");
        log.error("에러 상황입니다");
    }
}

// 에러 발생 시 Exception을 마지막 인자로 전달하는 것이 SLF4J 권장 방식
log.error("에러 발생: {}", userId, e);
```
SLF4J 로그 메시지의 플레이스홀더는 `{}`만 지원함. `%s`, `%d` 등 printf 스타일은 지원하지 않으며, 필요하다면 `String.format()`을 사용할 수 있으나 문자열 결합 및 객체 생성 연산이 발생하므로 비권장임.
---
### \[참고\] 로그 생성 기준 — Log Level
Spring Boot에서는 `application.yaml` 또는 `application.properties`의 `logging.level` 속성으로 로그 수준을 제어함. 기본값은 `INFO`임.
```yaml
logging:
  level:
    root: INFO                       # 전체 기본 로그 수준
    com.example.demo: DEBUG          # 특정 패키지 로그 수준
    org.springframework.web: WARN    # 스프링 웹 로그만 경고 이상 출력
```
로그 레벨은 아래 순서로 상세함이 낮아짐. 설정된 레벨 이상의 로그만 출력됨.
| 레벨 | 용도 |
| --- | --- |
| `TRACE` | 가장 상세한 로그 (디버깅용 세부 정보) |
| `DEBUG` | 디버깅에 유용한 정보 |
| `INFO` | 일반적인 실행 정보 (기본값) |
| `WARN` | 경고 메시지 |
| `ERROR` | 오류 메시지 |
| `OFF` | 로그 출력 안 함 |
예를 들어 `root: INFO`로 설정하면 `TRACE`와 `DEBUG` 로그는 출력되지 않고 `INFO`, `WARN`, `ERROR`만 출력됨. 특정 패키지에만 더 상세한 레벨을 지정해 디버깅 범위를 좁히는 방식이 일반적임.
---
### 애플리케이션 설정 정보 관리 — application.properties / application.yml
Spring Boot 애플리케이션의 환경 설정은 `application.properties` 또는 `application.yml` 파일에서 관리함. 두 형식은 동일한 설정을 표현하며, yml은 계층 구조를 들여쓰기로 표현해 가독성이 더 좋음.
관리 대상 정보로는 데이터베이스 접속 정보, 서버 포트, 로깅 레벨, 외부 API 키, 커스텀 프로퍼티 등이 있으며, 개발·테스트·운영 환경별로 다른 설정값을 파일로 분리해 관리할 수 있음.
```plain text
# application.properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/stockdb
spring.datasource.username=stockuser
spring.datasource.password=stockpw
logging.level.org.springframework=INFO
stock.api.base-url=https://api.stock.com
```
```yaml
# application.yml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/stockdb
    username: stockuser
    password: stockpw
logging:
  level:
    org.springframework: INFO
stock:
  api:
    base-url: https://api.stock.com
```
---
### yml에서 List 값 작성 방법
yml에서 리스트 값을 작성하는 방식은 세 가지가 있으며, 사용하는 쪽에서 `List`로 바인딩함.
```yaml
# 방식 1 — 블록 시퀀스 (가장 명시적)
key:
  value:
    - a
    - b
    - c
    - d

# 방식 2 — 인라인 시퀀스
key:
  value: [a, b, c, d]

# 방식 3 — comma 구분 (properties 스타일과 유사)
key:
  value: a, b, c, d
```
---
### 설정 정보 관리를 위한 의존성 주입
`@ConfigurationProperties` 사용 시 IDE의 자동 완성 및 메타데이터 생성을 지원하려면 `pom.xml`에 아래 의존성을 추가해야 함. `<optional>true</optional>`로 설정하면 컴파일 시에만 사용되고 런타임 배포 산출물에는 포함되지 않음.
```xml
<!-- Configuration Properties 자동 완성 및 metadata 생성용 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```
---
### 설정 정보 사용 — @Value
`@Value("${키}")` 형식으로 설정 파일의 특정 값을 필드에 직접 주입함. 값이 한두 개일 때 간단하게 사용하기 좋으나, 값이 많아지면 관리가 어렵고 계층 구조 표현이 불편하다는 단점이 있음.
주입 시점은 componentScan 시 DI(의존성 주입) 단계임.
```java
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class StockApiClient {
    @Value("${stock.api.base-url}")
    private String baseUrl;

    public void connect() {
        System.out.println("API URL: " + baseUrl);
    }
}
```
---
### 설정 정보 사용 — @ConfigurationProperties
계층적 구조의 설정을 하나의 객체로 묶어 사용할 때 활용함. `prefix`로 yml의 특정 네임스페이스를 지정하면, 해당 하위 키들이 클래스 필드에 자동으로 바인딩됨.
```yaml
# application.yml
stock:
  api:
    base-url: https://api.stock.com
    timeout: 1000
  caching:
    enabled: true
```
prefix가 `"stock.api"`이면 그 하위 키(`base-url`, `timeout`)만 바인딩함.
```java
@Data
@Component
@ConfigurationProperties(prefix = "stock.api")
public class StockApiProperties {
    private String baseUrl;
    private int timeout;
}
```
prefix가 `"stock"`이면 중첩 구조를 내부 static 클래스로 표현해 전체를 한 번에 바인딩할 수 있음.
```java
@Data
@Component
@ConfigurationProperties(prefix = "stock")
public class StockProperties {
    private Api api;
    private Caching caching;

    @Data
    public static class Api {
        private String baseUrl;
        private int timeout;
    }

    @Data
    public static class Caching {
        private boolean enabled;
    }
}
```
사용 방법은 생성자 주입으로 Properties 클래스를 받아 필드에 접근함.
```java
@Service
public class StockApiClient {
    private final StockApiProperties stockApiProperties;

    public StockApiClient(StockApiProperties stockApiProperties) {
        this.stockApiProperties = stockApiProperties;
    }

    public void connect() {
        System.out.println("API URL: " + stockApiProperties.getBaseUrl());
    }
}
```
---
### 설정 정보 클래스 서비스 사용 예시
중첩 구조를 가진 `StockProperties`를 서비스에서 주입받아 사용하는 전체 예시임.
```java
@Service
public class StockApiClient {
    private final StockProperties stockProperties;

    public StockApiClient(StockProperties stockProperties) {
        this.stockProperties = stockProperties;
    }

    public void connect() {
        String baseUrl = stockProperties.getApi().getBaseUrl();
        int timeout = stockProperties.getApi().getTimeout();
        boolean cachingEnabled = stockProperties.getCaching().isEnabled();

        System.out.println("API URL: " + baseUrl);
        System.out.println("Timeout: " + timeout);
        System.out.println("Caching Enabled: " + cachingEnabled);
    }
}
```
`getApi().getBaseUrl()`처럼 중첩 getter 체이닝으로 각 값에 접근함.
---
### 환경별 애플리케이션 프로파일 분리
런타임 환경(개발, 테스트, 운영 등)에 따라 설정 파일명을 구분해 관리함.
| 파일명 | 적용 환경 |
| --- | --- |
| `application-dev.yml` | 개발 |
| `application-prod.yml` | 운영 |
| `application-test.yml` | 테스트 |
실행 시 활성화할 프로파일을 지정하는 방법은 두 가지임.
JVM 옵션 방식 — `-D` 플래그로 JVM 시스템 프로퍼티를 설정하며, Spring Boot가 내부적으로 `System.getProperty()`를 통해 참조함.
```bash
java -Dspring.profiles.active=dev -jar skala-stock-api.jar
```
Spring Boot 애플리케이션 아규먼트 방식 — `--` 접두사를 사용해 jar 뒤에 아규먼트로 전달함. Spring Boot가 직접 파싱함.
```bash
java -jar skala-stock-api.jar --spring.profiles.active=dev
```
---
### 의존성 (Dependency)
의존성이란 하나의 객체가 자신의 기능을 수행하기 위해 반드시 필요로 하는 다른 객체를 의미함. 하나의 객체가 다른 객체의 메서드를 호출하거나 사용하는 관계를 의존성으로 정의하며, `A → B` 방향의 점선 화살표로 표현함 (Class A는 Class B에 의존적이다).
---
### 의존관계 생성 — 직접 생성(new)의 문제
`Coffee` 객체가 `Ame` 인터페이스를 사용하는 예시에서, 의존 객체를 내부에서 직접 `new`로 생성하면 아래 문제가 발생함.
```java
public class Coffee {
    private String kind;
    private Ame ame;

    public Coffee(String kind) {
        this.kind = kind;
    }

    public void coffeeType() {
        if (kind.equals("hot")) {
            ame = new Hot();
        } else if (kind.equals("ice")) {
            ame = new Ice();
        } else if (kind.equals("thinIce")) {
            ame = new ThinIce();
        }
        ame.get();
    }
}
```
- `Coffee` 내부에서 구현체(`Ice`, `Hot`, `ThinIce`)를 직접 `new`로 생성함
- 새로운 구현체(`ThinIce` 등)를 추가하거나 교체할 때마다 `Coffee` 코드를 수정해야 함 → OCP 위반
---
### 의존성 주입 (Dependency Injection)
의존 객체의 생성을 외부로 분리하고, 생성된 객체를 주입받아 사용하는 방식임. `Coffee`는 어떤 `Ame` 구현체인지 알 필요 없이 주입받은 객체를 그대로 사용하기만 하면 됨.
![]()
```java
// 외부에서 생성 (객체 생성 책임 분리)
Coffee hot     = new Coffee(new Hot());
Coffee ice     = new Coffee(new Ice());
Coffee thinIce = new Coffee(new ThinIce());
```
```java
// Coffee 내부 — 주입받은 객체만 사용
public class Coffee {
    private Ame ame;

// 외부에서 구현체를 주입받음 (생성자 주입)
    public Coffee(Ame ame) {
        this.ame = ame;
    }

// 새로운 커피 추가 시에도 업무 로직 변경 없음
    public void coffeeType() {
        ame.get();
    }
}
```
---
### IoC (Inversion Of Control)
의존성 주입을 받는 관점에서는 외부에서 의존성이 주입(DI)되는 것이고, 의존성을 컨트롤하는 주체가 외부(Framework: Spring)라는 관점에서 IoC로 정의함.
![]()
- 개발자가 직접 `new`로 인스턴스를 만드는 것이 아니라, Spring IoC Container가 Bean을 생성하고 의존성을 주입함
- IoC Container는 `@Controller`, `@Component`, `@Service`에 포함된 Bean을 직접 주입 실행함
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService; // 생성자 의존성 주입 대상

    public UserController(UserService userService) {
        this.userService = userService;
    }
}
```
---
### IoC Container 기반 DI
객체가 의존하는 다른 객체를 직접 생성하지 않고, 외부(컨테이너)에서 주입받는 방식임. 객체 사이의 결합도를 낮추고 테스트나 변경이 용이해짐.
![]()
IoC Container(`ApplicationContext` 또는 `BeanFactory`)는 XML, Java 코드, 어노테이션 등의 Configuration Meta-Data를 읽어 Bean을 생성함. Bean B가 먼저 생성(①)된 후, Bean B를 필요로 하는 Bean A가 생성(②)되고, Bean B가 Bean A에 주입됨. Bean A는 Bean B의 구체적인 구현체를 알지 못하지만 사용할 수 있음.
| DI 주입 방식 | 장점 | 단점 |
| --- | --- | --- |
| 생성자 주입 (권장) | 불변 객체 설계, 테스트 용이, 필수 의존성 보장 | 코드 다소 길어질 수 있음 |
| 필드 주입 | 코드 간결, 간단 실습에 적합 | `final` 불가, 테스트 불편, 권장 X |
| Setter 주입 | 선택적 의존성 주입에 적합 | setter 오남용 가능, 불변성 약함 |
---
### DI — 생성자 주입 (Constructor Injection)
생성자 파라미터로 의존 객체를 받아 `final` 필드에 할당하는 방식임.
```java
@Service
public class StockService {
    private final StockRepository stockRepository;

// 생성자 주입
    public StockService(StockRepository stockRepository) {
        this.stockRepository = stockRepository;
    }

    public String getStockInfo(String ticker) {
        return stockRepository.getStockInfo(ticker);
    }
}
```
`private final` 선언이 중요한 이유는 세 가지임.
- `final`로 선언하면 초기화 이후 값이 변하지 않는 불변(immutable) 객체가 됨
- 생성자를 통해 반드시 1번만 값이 할당되고 이후 변경 불가 → 안정성과 신뢰성 확보
- Spring이 주입할 때도 반드시 생성자를 통해 값을 넣기 때문에, 필수 의존성이 반드시 주입되었음을 컴파일 타임에 확인할 수 있음
---
### DI — 필드 주입 (Field Injection)
`@Autowired`를 필드에 직접 붙여 Spring이 자동으로 주입하게 하는 방식임. 코드가 간결하지만 `final` 선언이 불가하고 테스트 시 mock 주입이 어려워 실무에서는 권장하지 않음.
```java
@Service
public class StockService {
    @Autowired
    private StockRepository stockRepository;

    public String getStockInfo(String ticker) {
        return stockRepository.getStockInfo(ticker);
    }
}
```
---
### DI — Setter 주입 (Setter Injection)
`@Autowired`를 setter 메서드에 붙이는 방식임. 객체 생성 후 setter 메서드를 통해 Spring이 의존 객체를 주입함.
```java
@Service
public class StockService {
    private StockRepository stockRepository;

    @Autowired
    public void setStockRepository(StockRepository stockRepository) {
        this.stockRepository = stockRepository;
    }

    public String getStockInfo(String ticker) {
        return stockRepository.getStockInfo(ticker);
    }
}
```
`@Autowired`가 필요한 이유는 일반 자바 메서드는 Spring이 자동으로 호출해주지 않으므로, 이 메서드가 DI 용도임을 Spring에게 명확히 알려야 하기 때문임.
---
### \[참고\] 생성자 주입이 필드 주입보다 권장되는 이유
| 구분 | 생성자 주입 | Non-생성자 주입 |
| --- | --- | --- |
| 불변성(Immutable) 보장 | `final` 키워드로 객체 생성 후 의존성 변경 불가 → 안정성 증가 | `@Autowired`, setter는 `final` 선언 불가, 의존성 변경 가능성 존재 |
| 의존성 주입 시점 | Bean 생성 단계 | BeanPostProcessor 단계 |
| 필수 의존성 보장 | 생성자 파라미터로 강제하여 누락 시 컴파일/런타임 에러 → 오류 조기 발견 | 선택적 |
| 테스트 용이성 | 단위 테스트 시 생성자를 통해 mock/fake 객체 직접 주입 가능 → 테스트 코드 작성 편리 | `@Autowired`는 테스트 데이터 주입 용이하지 않음 |
| 순환 참조 조기 감지 | 순환 참조 발생 시 애플리케이션 구동 시점에 즉시 에러 발생 → 빠른 버그 확인 | `@Autowired`, Setter는 늦게 감지 |
| 의존성 명확성 및 가독성 | 생성자 시그니처만 봐도 어떤 의존성이 필요한지 한눈에 파악 → 유지보수 용이 | 가독성 낮음 |
---
### \[참고\] 순환 참조 오류
생성자 주입은 객체를 생성하면서 필수로 모든 의존성을 동시에 주입해야 하므로, A가 B를 필요로 하고 B도 A를 필요로 하면 무한루프에 빠져 객체를 만들 수 없는 상태가 됨. Spring은 이 구조를 시작 즉시 감지해 아래와 같은 에러를 발생시킴.
```plain text
APPLICATION FAILED TO START

Description:
The dependencies of some of the beans in the application context form a cycle:

    aService (field private final BService AService.bService)
        ↓
    bService (field private final AService BService.aService)
        ↓
    aService ...

Action:
There is a circular dependency between two beans.
Consider revising your code.
```
순환 참조는 비즈니스 설계 자체를 다시 점검해야 한다는 신호임. 해결 방법은 의존 구조를 리팩토링하거나, 인터페이스·이벤트 등 중간 계층으로 분리하는 것임.
---
### Spring Container
자바 객체(Bean)의 생성부터 소멸까지의 생명 주기를 관리하고, 객체 간 의존 관계를 설정하는 핵심 역할을 담당함. 내부적으로 싱글톤 객체 생성, 목록화, 의존관계 연결(생성자 함수에 넣어주기)을 수행함.
- 객체 관리: 개발자가 `new`로 객체를 직접 생성하지 않고, 컨테이너가 객체를 대신 생성/소멸
- 의존성 주입(DI): 객체 A가 객체 B를 필요로 할 때, 컨테이너가 런타임에 B를 A에게 주입하여 조립
- 싱글톤 관리: 객체를 기본적으로 단 하나만 생성(Singleton Pattern)하여 재사용
---
### IoC (Inversion Of Control) — 제어의 역전
객체의 생성, 생명주기 관리, 의존성 주입 등을 개발자가 직접 하지 않고, 컨테이너가 대신 관리해주는 원리임. 전통적 방식(개발자 직접 제어)과 반대 개념으로, 제어권이 개발자에서 프레임워크로 넘어감. 코드 결합도를 낮추고 유연한 아키텍처와 테스트가 가능한 구조를 만들 수 있음.
```java
// 전통 방식 — 개발자가 직접 생성
OrderService orderService = new OrderService(new OrderRepository());
```
```java
// IoC 적용 방식 — 컨테이너가 생성 및 주입
@Component
public class OrderService {
    private final OrderRepository orderRepository;

    public OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }
}
```
IoC Container는 `@Component`로 표시된 객체 생성 단계(Bean)에서 `OrderRepository` 객체를 주입하여 의존성 주입을 IoC Container가 실행함.
---
### IoC Container
![]()
Spring Container는 IoC 컨테이너 패턴을 적용한 컨테이너임. 애플리케이션에서 사용할 객체(Bean)를 생성하고, 필요한 의존성을 주입하며, 객체의 생명주기를 관리함. IoC는 프로그램의 흐름 제어 권한을 개발자가 아닌 프레임워크에게 넘긴다는 의미임.
역할은 세 가지로 요약됨.
- 애플리케이션 컴포넌트(Bean)의 중앙 저장소
- Bean 소스부터 Bean을 생성 및 관리
- 의존성 주입을 통한 객체 주입 실행
IoC Container는 XML, Java 어노테이션, Configurations 등의 메타데이터를 읽어 Bean 1과 Bean 2를 각각 생성(Creation)하고, Bean 1에게 Bean 2를 Dependency Injection하는 흐름으로 동작함.
---
### IoC 컨테이너 구현체 — BeanFactory vs ApplicationContext
스프링 빈의 생성, 설정, 관리, 소멸 등 생명주기(Lifecycle) 전반을 담당하는 핵심 엔진임. IoC Container의 구현체가 `ApplicationContext`이며, 이것은 `BeanFactory`를 상속함.
| 구분 | BeanFactory | ApplicationContext |
| --- | --- | --- |
| 설명 | 가장 기본적인 컨테이너 | BeanFactory 확장판 |
| 주요 기능 | Bean의 생성/조회/관리 | BeanFactory의 모든 기능 + 부가기능 지원 |
| Bean 로딩 방식 | 지연 로딩 (Lazy Loading) | 즉시 로딩 (Eager Loading) |
| Bean 저장 | `ConcurrentHashMap<String, BeanDefinition>`, ComponentScan 대상을 생성/등록 | BeanFactory 상속 |
| 부가 기능 | 미 지원 | 국제화, 이벤트 발행, AOP, Proxy Pattern, 메시지 자원, 환경설정 등 |
| 사용 예 | Spring 2.x 이전 사용 | Spring 2.x 이후부터 사용 |
---
### 빈 (Bean)
![]()
스프링이 관리하는 객체(인스턴스)를 의미함. IoC Container가 Bean을 생성하고 생명주기를 관리하며, `@Component`, `@Controller`, `@Service` 등의 어노테이션을 통해 실행 시점에 Bean이 자동 생성됨.
Bean의 특징은 두 가지임.
- 싱글톤(Singleton) 방식으로 관리 (기본)
- 객체 생성, 의존성 주입, 소멸 등 생명주기를 컨테이너가 책임짐
IoC Container는 내부적으로 Map과 유사한 Collection을 가지고 있으며, 여기에 Bean을 등록하고 Bean 호출 시 생성이 아닌 기존 Bean을 Input Argument로 전달함. 컨테이너 내부에는 일반 Bean과 Proxy Bean이 함께 관리됨 (빈 인스턴스 생성 → 의존 관계 설정 → 빈 제공).
---
### 싱글톤 (Singleton) 방식
싱글톤 패턴이란 프로그램 실행 내내 단 하나의 객체만 생성해서 공유하는 디자인 패턴임. Spring 컨테이너는 기본적으로 모든 Bean을 싱글톤으로 관리함.
싱글톤 특징은 세 가지임.
- 메모리 절약: 객체를 한 번만 생성해서 여러 곳에서 같이 쓰면 메모리를 아낄 수 있음
- 일관된 데이터 관리: 모든 사용자가 같은 객체(=동일 인스턴스)를 사용하므로 데이터 일관성이 높아짐
- 객체 생성 비용 감소: 반복적인 객체 생성 작업을 줄일 수 있음
스프링에서의 싱글톤 Bean은 `@Component`, `@Service`, `@Repository`, `@Controller` 형태로 어노테이션으로 등록된 Bean을 컨테이너당 한 개만 생성 관리함.
---
### \[참고\] POJO 클래스
Spring Bean은 기본적으로 POJO(Plain Old Java Object) 기반으로 구성되어, 특정 프레임워크에 종속되지 않도록 POJO 기반 구성을 지향함.
Spring이 POJO를 관리하는 방식은 단순한 POJO 클래스와 약간의 차이가 있음. Spring은 POJO 객체를 IoC 컨테이너(`WebApplicationContext`)에 등록하여 관리하고, 이를 통해 의존성 주입(DI) 및 AOP 기능을 추가함.
```java
// 일반적인 POJO 클래스
public class UserService {
    public void getUserInfo() {
        System.out.println("Fetching user information...");
    }
}
```
```java
// @Component를 이용한 자동 Bean 등록
import org.springframework.stereotype.Component;

@Component
public class UserService {
    public void getUserInfo() {
        System.out.println("Fetching user information...");
    }
}
```
클래스 코드 자체는 동일하지만, `@Component`가 붙으면 Spring IoC Container가 이 클래스를 Bean으로 등록하고 DI·AOP 기능을 적용함.
---
### 어노테이션(Annotation)을 이용한 DI 대상 식별
`@Component`, `@Controller`, `@Service` 등을 적용하여 복잡한 설정 없이 객체(Bean)를 자동으로 등록하거나 관리하고, 의존성 주입을 간편하게 처리함.
개발자 코드에 어노테이션(`@Component`, `@Autowired`, `@Transactional` 등)을 붙이면, Spring IoC Container(`BeanFactory` / `ApplicationContext`)가 두 가지 처리를 수행함.
- `ClassPathScanner`: 패키지 내부를 탐색하여 어떤 클래스가 Bean인지 검색
- `BeanPostProcessor`: 스캔된 Bean들이 실제 객체로 생성되는 과정에서 생성 전/후 특별한 로직을 실행 (의존성 주입, Proxy 객체 바꿔치기)
---
### \[참고\] Bean 생성 클래스 정의 Annotation
| 어노테이션 | 용도/설명 |
| --- | --- |
| `@Component` | 스프링이 자동으로 Bean으로 등록해줌 |
| `@Service` | 비즈니스 로직을 담은 Service 클래스에 사용 |
| `@Repository` | 데이터 접근 계층(DAO)에 사용, 데이터 예외 변환 처리 |
| `@Controller` | MVC 패턴에서 Controller 역할, 웹 요청 처리 |
| `@RestController` | RESTful API Controller (JSON 반환) |
| `@Autowired` | 필요한 의존성을 자동 주입 (DI) |
| `@Bean` | 메서드의 반환 객체를 직접 Bean으로 등록 |
---
### Proxy 패턴 정의
Proxy라는 용어는 원래 법률 및 정치 분야에서 대리인이라는 개념에서 유래함. Proxy Vote(대리 투표)나 Proxy Server(프록시 서버)처럼, 어떤 주체가 직접 처리하지 않고 다른 주체가 대신 처리하는 구조를 의미함.
![]()
소프트웨어에서의 Proxy는 원래 객체를 감싸는 래퍼 역할을 함. 원본 객체(회색 사각형)를 Proxy(빨간 테두리)가 둘러싸고, Client는 Proxy를 통해서만 원본 객체에 접근하게 됨.
---
### Proxy 패턴 구조
Proxy Pattern은 동일한 인터페이스를 가진 구현 클래스를 Client에서 사용할 때 Overriding으로 동일한 인터페이스에 다른 기능을 정의하여 사용하는 패턴임.
![]()
- `Subject` 인터페이스를 `Proxy`와 `RealSubject`가 모두 구현함
- Client는 `Subject` 인터페이스에 의존하므로 `Proxy`인지 `RealSubject`인지 알 수 없음
- `Proxy`는 내부적으로 `RealSubject`를 delegate(위임) 방식으로 호출함
- 시퀀스 흐름: Client → `doAction()` → Proxy → `doAction()` → RealSubject
---
#### Proxy 패턴 예시코드
Proxy Class는 RealSubject를 Wrapping해서 내부에 감싸는 방식으로 지정하고, Proxy Class의 `operation()`은 `realSubject.operation()` 호출 전/후에 추가적인 작업을 수행할 수 있도록 지원하는 구조임.
```java
// Subject 인터페이스
interface Subject {
    String operation(String name);
}
```
```java
// RealSubject: 실제 기능을 수행하는 클래스
class RealSubject implements Subject {
    @Override
    public String operation() {
        System.out.println("RealSubject: 작업 수행");
    }
}
```
```java
// Proxy: RealSubject에 대한 접근을 제어하는 클래스
class Proxy implements Subject {
    private RealSubject realSubject;

    @Override
    public void operation(String name) {
        if (realSubject == null) {
            realSubject = new RealSubject();
        }
// pre-processing 처리
        String fullName = "pre:" + name;
        fullName = realSubject.operation(fullName); // delegate
// post-processing 처리
        fullName = fullName + ":post";
    }
}
```
```java
// 클라이언트 코드
public class ProxyPatternExample {
    public static void main(String[] args) {
        Subject proxy = new Proxy();  // Proxy가 RealSubject를 호출
        String name = "honggildong";
        proxy.operation(name);
    }
}
```
---
### Spring Proxy 구현 방식
동적 프록시(Dynamic Proxy)를 통해 개발자가 작성한 코드를 직접 수정하지 않고 기능 확장이 가능함. Spring은 두 가지 방식으로 Proxy를 생성함.
JDK Proxy (Interface based)
![]()
CGLIB Proxy (Class based)
![]()
| 구분 | JDK Proxy (Interface based) | CGLIB Proxy (Class based) |
| --- | --- | --- |
| 동작 방식 | 인터페이스 기반 | 바이트코드 조작으로 프록시 생성 |
| 사용 클래스 | `java.lang.reflect.Proxy` | Code Gen Lib |
| 인터페이스 필요 여부 | 반드시 필요 | 없어도 사용 가능 |
| 프록시 생성 방식 | Reflection 활용 | 서브클래스(Proxy Class)를 생성하여 원래 클래스의 메서드를 오버라이드 |
| 성능 | 상대적으로 느림 | JDK Proxy 대비 뛰어남 (Non-Reflection) |
JDK Proxy는 `TargetObject` 인터페이스를 `Spring Proxy`(`Aspect` + `TargetObjectImpl`)가 implements 방식으로 구현하고, CGLIB Proxy는 `TargetObject`를 `Spring Proxy`가 extends 방식으로 상속해 서브클래스를 만듦.
---
### CGLIB Proxy 메커니즘을 사용하여 동작하는 기술들
CGLIB Proxy를 기반으로 Spring의 다양한 선언적 기능이 동작함.
- Custom AOP (`@Aspect`): 횡단 관심사(Aspect Oriented Programming)를 직접 정의
- `@Transactional`: 스프링 트랜잭션 관리 (내장 선언적 기능)
- `@Cacheable` / `@CacheEvict`: 스프링 캐시 추상화
```java
@Cacheable(value = "products", key = "#productId")
public ProductDto getProductById(Long productId) {
    return productRepository.findById(productId).orElseThrow();
}
```
- `@Async`: 비동기 메서드 실행
- `@Validated`: 메서드 레벨 검증
---
### 수동으로 Proxy Bean 생성 방법 — @Configuration과 @Bean
`@Configuration`으로 정의된 클래스 내에서 `@Bean`을 사용해 Bean을 수동으로 생성할 수 있음. 내부적으로 IoC Container에 Bean 등록을 요청(위임)하는 방식임. `@Service` 등 스테레오타입 어노테이션이 없는 클래스도 이 방법으로 Bean으로 등록할 수 있음.
```java
// @Service 없이 자동 Bean 생성하지 않음
public class UserService {
    private final UserRepository userRepository;

    public MyService UserService(UserRepository userRepository) {
        return new UserService(userRepository);
    }
}
```
```java
// @Configuration + @Bean으로 수동 등록
@Configuration
public class AppConfig {

    @Bean
    public MyService UserService(UserRepository userRepository) {  // 의존성 주입
        return new UserService(userRepository);
    }
}
```
---
### Proxy with Bean 만들기
`@Configuration`을 이용해 실제 대상 객체를 생성한 뒤 Proxy로 감싸서 Bean으로 등록하면, IoC Container에는 Proxy Bean이 등록됨. 이후 다른 곳에서 해당 타입을 주입받을 때 Proxy 객체가 주입됨.
```java
@Configuration
public class AppConfig {

    @Bean
    public UserService userService(UserRepository userRepository) {
// 실제 대상 생성
        UserService target = new UserServiceImpl(userRepository);
// 프록시로 감싸서 반환
        return new UserServiceProxy(target);
    }
}
```
IoC Container 내부에는 일반 Bean과 함께 Proxy with Bean이 함께 등록되어 관리됨. Client는 `UserService` 타입을 주입받지만 실제로는 `UserServiceProxy` 인스턴스를 사용하게 됨.
---
### AOP (Aspect-Oriented Programming)
AOP(관점 지향 프로그래밍)는 OOP(객체지향 프로그래밍)의 한계를 보완하는 프로그래밍 패러다임임. OOP는 주로 '기능' 단위로 클래스를 구현하는 반면, AOP는 '공통 관심사(Aspect)'를 모듈화하여 코드 중복을 줄이고 유지보수가 쉽도록 구현함.
![]()
핵심 관심(비즈니스 로직)과 횡단 관심(AOP)의 관계를 도식으로 보면, 사용자 정보 관리·주문 정보 관리·배송 정보 관리라는 각각의 핵심 관심 위에 로깅·보안·트랜잭션이 수평으로 공통 적용됨. 이처럼 여러 모듈을 횡단하여 공통적으로 적용되는 기능을 AOP로 분리해 관리함.
대표적인 공통 관심사(Aspect) 예시: 로깅(Logging), 트랜잭션 처리(Transaction), 보안(Security), 성능 측정(Profiling)
---
### Spring Boot의 AOP
별도 설정 없이 `spring-boot-starter-aop` 의존성만 추가하면 바로 사용 가능함. `@Aspect` 어노테이션 기반으로 Aspect 클래스를 작성하는 선언적 AOP 방식을 지원함.
```xml
<!-- Spring Boot Starter AOP -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aspectj</artifactId>
</dependency>
```
---
### AOP 핵심 구성요소
AOP 적용을 위한 AOP 클래스는 아래와 같이 구성됨.
```java
@Aspect          // AOP 적용 클래스라고 명시; Bean 객체 생성 시 AOP Proxy 생성 및 wrapping
@Component       // AOP 설정 클래스는 반드시 Bean 객체로 정의되어야 함
public class LoggingAspect {

// 포인트컷 정의: com.example.service 패키지 내 모든 서비스(*), 모든 method(*) 에 적용
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

// Before 어드바이스 — 메서드(serviceMethods()) 호출 전 먼저 실행
    @Before("serviceMethods()")
    public void beforeAdvice(JoinPoint joinPoint) {
        System.out.println("[Before] " + joinPoint.getSignature());
    }

// After 어드바이스 — 메서드(serviceMethods()) 호출 후 동일한 포인트컷 재사용
    @After("serviceMethods()")
    public void afterAdvice(JoinPoint joinPoint) {
        System.out.println("[After] " + joinPoint.getSignature());
    }

// Around 어드바이스 — 메서드 실행 전/후 모두 제어
    @Around("serviceMethods()")
    public Object aroundAdvice(ProceedingJoinPoint joinPoint) {
        System.out.println("[Around] 메서드 실행 전");
        Object result = joinPoint.proceed();
        System.out.println("[Around] 메서드 실행 후");
        return result;
    }
}
```
핵심 구성요소 정리:
| 구성요소 | 설명 |
| --- | --- |
| Aspect | AOP 적용 클래스라고 명시. Bean 객체 생성 시 AOP Proxy 생성 및 wrapping |
| Bean Component | AOP 설정 클래스는 반드시 Bean 객체로 정의되어야 함 |
| Pointcut | 어떤 메서드를 대상으로 하는지 정의. `execution` 표현식으로 패키지·클래스·메서드를 패턴 매칭 |
| Advice | 메서드 호출 시 횡단 관심 기능을 어느 지점에서 실행할지 결정. `@Before`는 메서드 호출 전 먼저 실행 |
| JoinPoint | 메서드 정보를 담고 있는 객체들의 역할 |
| Target | Advice가 적용되는 실제 비즈니스 객체 (원본 Bean). Proxy가 감싸고 있는 원본 인스턴스를 의미 |
---
### \[참고\] JoinPoint Method
- `joinPoint.getSignature()`: 현재 어드바이스가 걸린 메서드의 서명 정보(이름, 반환타입, 파라미터 타입 등)를 반환
- `joinPoint.getArgs()`: 호출 시 전달된 인자 값 배열. 실제 호출 시 넘어온 런타임 값. 예: `updateMember(7, "bob")` 호출 시 → `[7, "bob"]`
- `joinPoint.getTarget()`: 프록시가 감싸고 있는 원본 Bean Instance. 예: `joinPoint.getTarget().getClass().getName()` → `com.example.service.MemberService`
- `joinPoint.getThis()`: 현재 호출을 처리 중인 프록시 인스턴스(가장 바깥쪽 프록시). CGLIB 프록시의 경우 `com.example.service.MemberService$$SpringCGLIB$$a1b2c3`, JDK 동적 프록시의 경우 `jdk.proxy2.$Proxy38` 형태로 표시됨
---
### Pointcut 표현식: execution
메서드 실행(join point)을 메서드 시그니처 패턴으로 매칭하는 포인트컷임.
```plain text
execution(* com.example.domain.*Service.find*(..))
         ↑         ↑               ↑        ↑   ↑
       반환값     패키지          클래스(타입)  메서드  파라미터
```
| 표현식 | 대상 |
| --- | --- |
| `execution(* com.example.user.*.*(..))` | user 패키지 아래의 모든 클래스의 전체 메서드, 모든 반환값 유형 |
| `execution(* com.example.user.UserService.*(..))` | UserService 클래스의 전체 메서드 |
| `execution(* com.example.user.UserService.find*(..))` | UserService 클래스에서 find로 시작하는 메서드 |
| `execution(String com.example.user.UserService.*(..))` | UserService 클래스에서 반환값이 String인 메서드 |
와일드카드: `*`는 하나의 패키지 또는 클래스 이름 매칭, `..`는 하위 패키지 포함
---
### Pointcut 표현식: within
특정 타입(클래스 또는 패키지) 내부의 모든 메서드를 포인트컷으로 지정할 때 사용함. `execution`과 달리 메서드 시그니처가 아닌 타입(클래스/패키지) 기준으로 매칭함.
```plain text
within(com.example.domain..*)
       ↑                ↑  ↑
    기준 패키지        하위  모든 클래스
```
와일드카드: `*`는 하나의 패키지 또는 클래스 이름 매칭, `..`는 하위 패키지 포함
---
### Pointcut 표현식: annotation
특정 어노테이션이 붙어 있는 메서드를 포인트컷으로 지정할 때 사용함.
```java
@Pointcut("@annotation(com.sk.skala.myapp.aop.Metrics)")
public void metricsAnnotation() {}
```
`com.sk.skala.myapp.aop.Metrics`는 어노테이션 타입이며, 해당 어노테이션이 붙은 메서드에만 Aspect가 적용됨.
```java
// @Aspect 적용 방식
@Around("metricsAnnotation()")
public Object measureExecutionTime(ProceedingJoinPoint joinPoint) {...}
```
---
### Pointcut 표현식: bean
스프링 IoC 컨테이너에 등록된 Bean의 이름(ID)을 직접 지정하여 포인트컷을 정의하는 지시자임.
```java
// 특정 Bean 이름 지정
@Pointcut("bean(orderService)")
public void targetOrderService() {}

// Bean 이름 패턴 (접미사 Service)
@Pointcut("bean(*Service)")
public void targetAllService() {}
```
```java
// @Aspect 적용 방식
@Around("targetAllServices()")
public Object logExecution(ProceedingJoinPoint joinPoint) {...}
```
---
### Spring Boot의 Advice Type
| 어노테이션 | 역할 |
| --- | --- |
| `@Before` | 메서드 실행 전에 Advice 실행 |
| `@After` | 메서드 실행 후에 Advice 실행 (정상/예외 상관없이 항상 실행) |
| `@AfterReturning` | 메서드 정상 실행 후 Advice 실행 |
| `@AfterThrowing` | 예외 발생 후 Advice 실행 |
| `@Around` | 메서드를 감싸서 실행 전후 모두 Advice 실행되도록 설정 |
Advice 유형별 동작 방식을 다이어그램으로 보면:
![]()
- Before Advice: AOP Proxy → Before Advice 실행 → Target 메서드 호출 → Return/Exception
- After Advice: AOP Proxy → Target 메서드 호출 → Return 또는 Exception 어느 쪽이든 → After Advice 실행
![]()
- After Returning Advice: Return 경로에서만 After Returning Advice 실행 (Exception 경로에서는 미실행)
- After Throwing Advice: Exception 경로에서만 After Throwing Advice 실행 (Return 경로에서는 미실행)
![]()
- Around Advice: AOP Proxy와 Target 사이에 Around Advice가 위치하여 호출 전/후, Return/Exception 모두를 하나의 메서드에서 제어함
---
### \[참고\] @Around 구현 예시
메서드 실행 전/후, 예외 발생 여부 등 "전체 실행 흐름"을 모두 제어하는 가장 강력한 Advice 타입임.
```java
@Aspect
@Component
public class LoggingAspect {
    @Around("execution(* com.example.service.*.*(..))")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("메서드 실행 전");
        Object result = joinPoint.proceed(); // 실제 메서드 실행
        System.out.println("메서드 실행 후");
        return result;
    }
}
```
Target Method의 Input parameter를 변경하고 싶은 경우:
```java
Object[] args = joinPoint.getArgs();

Long userId   = (Long) args[0];
String item   = (String) args[1];
Integer qty   = (Integer) args[2]; // int는 오토박싱되어 들어옴

// 인자 수정: 공백 제거 + 수량 상한
args[1] = item.trim();
args[2] = Math.min(qty, 99);

Object result = joinPoint.proceed(args); // 수정된 인자 전달
return result;
```
→ Controller가 아닌, Service 로직에서 validation을 사용할 경우에 위의 방식을 사용함
---
### Bean과 AOP
Aspect Class 기반으로 Target이 된 `@Component`, `@Service` 등의 클래스는 Bean으로 IoC Container를 통해 생성 후 BeanFactory에 등록될 때 두 단계로 처리됨.
![]()
- Bean 등록 시: Bean 객체 생성 후 AOP Proxy 객체로 Wrapping하여 Proxy 기반 Bean으로 등록
- Bean 호출 시: `@Controller` 등의 Bean 호출 시 Proxy Object를 호출하며, Advice 실행 전/후로 Bean Method를 호출
IoC Container 내부에는 일반 Bean과 함께 Proxy with Bean이 등록되며, Proxy Object는 내부적으로 Advice(before, after...)와 실제 Bean Object를 포함하는 구조임.
---
### 입력값 검증이란?
클라이언트(사용자)로부터 받은 데이터가 사전에 정의된 규칙에 맞는지 확인하는 과정임. 검증 과정 없이 잘못된 데이터가 시스템으로 들어오면 예상치 못한 오류 또는 데이터베이스에 원치 않는 값이 저장될 수 있음. 입력값 검증 과정을 통해 애플리케이션의 안정성과 데이터의 신뢰성을 확보함.
검증 위치는 클라이언트 → Controller → Service → Repository → DB 흐름에서, 각 레이어가 사용하는 도메인 모델/DTO에 유효성 검사를 붙여 여러 지점에서 검증을 수행함.
---
### 의존성 추가
입력값 검증 기능을 사용하려면 `pom.xml`에 아래 의존성을 추가해야 함.
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```
---
### DTO (Data Transfer Object)
소프트웨어 아키텍처에서 계층 간 데이터 전달만을 담당하는 순수한 자료 구조임. 비즈니스 로직은 포함하지 않고 데이터 속성(Field)과 제어 메서드(Getter 생성자)만 존재함. 서비스 ↔ 컨트롤러 ↔ 외부 API/클라이언트 사이에서 전달 형식을 안정적으로 유지함.
DTO를 쓰는 이유:
- 엔티티(Entity) 보호 및 보안: 전달해야 하는 데이터만 선별해서 전달 가능
- 클라이언트 요구 사항과 도메인 로직과 격리
- 데이터 전송 도중 변하지 않는 불변성 권장 (Java 14부터 record 지원)
- 네트워크 오버헤드 감소 (원격 호출 시)
```java
@Data
@AllArgsConstructor
@NoArgsConstructor
public class UserResponse {
    private Long id;
    private String name;
    private String email;

// 정적 팩토리 메서드로 Entity → DTO 변환
    public static UserResponse from(User user) {
        return new UserResponse(
            user.getId(),
            user.getName(),
            user.getEmail()
        );
    }
}
```
---
### \[참고\] DTO 작성 시 주의점
- Don't Include Business Logic: DTO는 순수하게 데이터를 전달하는 "데이터 상자" 역할만 해야 함. 계산, 로직 처리, 데이터베이스 접근 등의 코드는 Service나 Domain 계층에 위치시킴.
- Don't Use Entities as DTOs: 엔티티는 데이터베이스 테이블과 직접 매핑되는 핵심 도메인 객체임. 엔티티를 클라이언트에 직접 노출하면 원치 않는 필드(비밀번호 등)가 외부에 노출될 수 있고, 양방향 연관관계 직렬화 시 StackOverflowError가 발생할 수 있음.
- Name and Separate Appropriately: DTO의 역할을 이름에 명시하면 가독성이 높아짐. 요청(Request)용 DTO: `UserCreateRequest`, `ProductUpdateRequest`. 응답(Response)용 DTO: `UserResponse`, `OrderDetailResponse`. 하나의 DTO를 요청과 응답에 모두 사용하면 용도가 다른 필드가 섞여 혼란을 줄 수 있음.
- Consider Serialization: DTO는 네트워크를 통해 JSON 등의 형태로 변환되어 전송되는 경우가 많음. Jackson 같은 라이브러리가 객체를 JSON으로 변환할 때 기본 생성자나 Getter가 없으면 오류 발생 가능 → Lombok으로 해결.
- Validation annotation belongs in the DTO: 클라이언트로부터 들어오는 데이터에 대한 검증은 DTO의 필드에 `@NotNull`, `@Size`, `@Email` 등의 어노테이션을 붙여 처리함.
---
### @Valid 검증 적용
DTO + `@Valid` 조합으로 IoC 컨테이너가 아니라 Spring MVC의 바인딩 과정에서 검증이 이루어짐.
```java
// DTO
public class UserRequest {
    @NotBlank
    private String name;

    @Email
    private String email;

    @Min(18)
    private int age;
}
```
```java
// 컨트롤러에서 @Valid 사용 검증
@PostMapping("/users")
public ResponseEntity<?> createUser(@Valid @RequestBody UserRequest request) {
// 유효성 검증 통과 시 로직 진행
    return ResponseEntity.ok("가입 완료");
}
```
검증 실패 시 400 Bad Request로 예외가 발생함. 내부적으로 `RequestMappingHandlerAdapter` 내 `HandlerMethodArgumentResolver`가 Body/Parameter를 DTO로 바인딩하는 과정에서 검증을 수행함.
---
### 입력값 검증 어노테이션
개별 데이터에 설정하고 `@Valid` 또는 `@Validated`를 통해 검증함.
| 어노테이션 | 설명 | 예시 |
| --- | --- | --- |
| `@NotNull` | Null이면 안됨 | 필수 입력값 |
| `@NotEmpty` | 개수가 0이면 안됨 | String, Array, Collection 대상 |
| `@NotBlank` | Null, 빈 문자, 스페이스 모두 안됨 | String 전용 |
| `@Size` | 문자열, 컬렉션, 배열의 길이/크기 제한 | `@Size(min=2, max=20)` |
| `@Min` | 최솟값(숫자) | `@Min(18)` |
| `@Max` | 최댓값(숫자) | `@Max(100)` |
| `@Positive` | 양수여야 함 | 1, 2, ... |
| `@PositiveOrZero` | 0 또는 양수여야 함 | 0, 1, 2, ... |
| `@Negative` | 음수여야 함 | -1, -2, ... |
| `@NegativeOrZero` | 0 또는 음수여야 함 | 0, -1, -2, ... |
| `@Email` | 이메일 형식 |  |
| `@Pattern` | 정규표현식 패턴 일치 | `@Pattern(regexp="^[0-9]+$")` |
| `@Past` | 과거 날짜여야 함 | 생년월일 등 |
| `@PastOrPresent` | 과거나 오늘 날짜 |  |
| `@Future` | 미래 날짜여야 함 | 예약일 등 |
| `@FutureOrPresent` | 오늘 또는 미래 날짜여야 함 |  |
| `@Digits` | 자릿수 및 소수점 자리 제한 | `@Digits(integer=5, fraction=2)` |
| `@AssertTrue` | 반드시 true | 체크박스 등 |
| `@AssertFalse` | 반드시 false |  |
| `@Null` | null이어야 함 |  |
---
### \[참고\] Spring MVC와 @Valid 적용 흐름
![]()
Spring MVC 구조에서 `@Valid` 처리는 `RequestMappingHandlerAdapter`에서 수행됨. HTTP 요청이 들어오면 `DispatcherServlet` → 핸들러 매핑 → 핸들러 어댑터 목록 조회 → `핸들러 어댑터`(컨트롤러 호출 전 `Argument Resolver`가 바인딩 + `@Valid` 검증 수행) → 컨트롤러 메서드 실행 순서로 처리됨.
`@Valid`는 Argument Resolver 과정에서 DTO request의 Validation 처리를 수행하며, 검증 실패 시 `MethodArgumentNotValidException`이 발생함. `ReturnValue Handler`는 컨트롤러의 반환값을 `ModelAndView`, `@ResponseBody`, `HttpEntity` 등으로 변환함.
---
### Controller와 Bean에서 Valid 적용 방법
`@Valid`는 Spring MVC의 메서드 파라미터 바인딩 과정에서 동작함.
Controller에서 `@Valid` 동작 흐름:
```plain text
HTTP 요청 → DispatcherServlet → HandlerMapping → HandlerAdapter
→ Argument Resolver (데이터 바인딩 + @Valid 검증) → Controller 메서드 실행
```
Service에서 `@Valid`가 불가능한 이유: `@Service`의 메서드 파라미터는 IoC 컨테이너가 생성자나 메서드 호출로 직접 주입하는 객체이기 때문에, Spring MVC의 요청 바인딩 + 검증 흐름이 아예 적용되지 않음. Service에서의 해결책은 클래스에 `@Validated`를 붙여 AOP Proxy 기반으로 동작하게 구성하는 것임.
---
### 입력값 검증 — @Valid vs @Validated
| 구분 | @Valid | @Validated |
| --- | --- | --- |
| 종류 | Java 표준 어노테이션 | Spring 제공 확장 검증 어노테이션 |
| 주요 사용처 | Controller DTO 검증 | Controller 단일 파라미터에 `@NotEmpty`, `@Min` 같은 제약 검증 / Spring AOP를 통한 Service·Component 메서드 호출 시 검증 |
검증 실패 시 발생하는 예외:
| 어노테이션 적용 위치 | 발생 예외 |
| --- | --- |
| `@RequestBody` | `MethodArgumentNotValidException` |
| `@ModelAttribute` | `BindException` |
| `@RequestParam` | `ConstraintViolationException` |
---
### 서비스에 @Validated 검증 적용
Service에 `@Validated`를 붙이면 AOP Proxy 기반으로 동작함.
```java
@Service
@Validated // Method Validation AOP Proxy 활성화
public class UserService {

// DTO 검증
    public void createUser(@Valid UserDto user) {
        System.out.println("유저 생성: " + user.getName());
    }

// 단일 파라미터 검증
    public void deleteUser(@Min(value = 1, message = "ID는 1 이상이어야 합니다.") Long id) {
        System.out.println("유저 삭제: " + id);
    }
}
```
동작 방식:
- Spring IoC Container가 UserService 빈 생성 시 `@Validated` 감지
- `MethodValidationPostProcessor`가 해당 빈을 AOP 프록시로 감싼 후 Bean으로 등록
- Controller가 AOP Proxy로 감싸진 Service 메서드를 호출하면: AOP 프록시가 메서드 호출을 가로채고 → Hibernate Validator로 파라미터 제약 검사 → 검증 실패 시 `ConstraintViolationException` 발생 → 검증 성공 시 원래 메서드 실행
---
### Controller에 @Validated 검증 적용
단일 파라미터 + `@Validated` 조합으로 Spring AOP(Method Validation)로 검증함.
```java
@RestController
@RequestMapping("/users")
@Validated // Method Validation AOP 활성화
public class UserController {

    @GetMapping("/search")
    public String search(@NotEmpty String name) {
        return "검색: " + name;
    }
}
```
동작 방식은 Service의 `@Validated`와 동일하게, IoC Container가 `@Validated` 감지 → `MethodValidationPostProcessor`가 AOP 프록시로 감싸 Bean 등록 → 메서드 호출 시 AOP 프록시가 가로채고 → Hibernate Validator로 파라미터 검사 → 실패 시 `ConstraintViolationException` 발생 → 성공 시 원래 메서드 실행 순서로 처리됨.
---
### @Async란?
메서드를 호출한 스레드와 분리하여 비동기(Async)로 실행하도록 지시하는 Spring 기능 어노테이션임. 호출자는 즉시 반환하고, 실제 실행은 별도 스레드 풀에서 처리되도록 구성함.
특징은 세 가지임.
- 긴 작업(메일 전송, 파일 처리, 외부 API 호출 등)을 메인 흐름에서 분리하여 성능 향상
- 웹 요청 처리 시간을 단축하고, 시스템의 병렬 처리 능력 향상
- 비동기 로직을 직접 스레드 생성 없이 어노테이션만으로 쉽게 구현
| 구분 | 동기 방식 | 비동기 방식 |
| --- | --- | --- |
| 실행 방식 | 한 작업 끝나야 다음 작업 수행 | 여러 작업 병렬 수행 |
| 응답 | 처리 끝까지 대기 | 즉시 응답 |
| 스레드 | 동일 스레드 | 별도 스레드 풀 |
| 사용 예 | 단순 로직 | I/O, 외부 연동, 시간이 긴 작업 |
---
### @Async 동작 원리
Spring은 Bean을 Proxy로 감싸 비동기 실행을 구현함.
동작 순서:
1. ComponentScan → Bean 등록
2. `@EnableAsync` Bean → `AsyncAnnotationBeanPostProcessor` 등록
3. `AsyncAnnotationBeanPostProcessor`가 모든 Bean을 확인
4. `@Async` 메서드가 존재하는 Bean 발견
5. 해당 Bean을 AOP Proxy Bean으로 교체
6. 메서드 호출 시 프록시가 가로채서 `ThreadPoolExecutor`에 위임
7. 호출자는 즉시 응답
흐름: Client → 호출 → Proxy Bean (`@Async`) → intercept → `ThreadPoolExecutor` → Real Service Instance
---
### @Async 활성화 방법 — 디폴트 TaskExecutor
`@Async`는 기본적으로 동작하지 않으며, Spring에서 비동기 기능을 활성화하기 위해 아래 설정이 반드시 필요함.
```java
@Configuration
@EnableAsync
public class AsyncConfig {
}
```
`@EnableAsync` → Spring이 `AsyncAnnotationBeanPostProcessor`를 등록하여 `@Bean` 중 `@Async` 메서드를 자동 감지하고 프록시 생성함.
디폴트로 사용되는 `SimpleAsyncTaskExecutor`의 특징은 세 가지임.
- 스레드 풀 없음: 매번 새로운 스레드 생성 (성능 저하 가능)
- 설정 불가: 스레드 풀 크기, 큐 등을 제어할 수 없음
java
```java
@Async
public void asyncMethodWithoutReturn(String message) { ... }
```
---
### @Async 활성화 방법 — TaskExecutor 지정
프로덕션 환경, 많은 비동기 작업이 필요한 경우 `ThreadPoolTaskExecutor`를 명시적으로 지정함.
```java
@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean(name = "taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);      // 기본 스레드 수
        executor.setMaxPoolSize(5);       // 최대 스레드 수
        executor.setQueueCapacity(100);   // 대기 큐
        executor.setThreadNamePrefix("async-");  // 스레드 이름 Prefix
        executor.initialize();
        return executor;
    }
}
```
```java
@Async("taskExecutor")
public CompletableFuture<String> asyncMethodWithReturn(String message) { ... }
```
`ThreadPoolTaskExecutor` 사용 시 스레드 풀에서 재사용하고, 설정한 풀 크기(2\~5)에서 효율적인 스레드 관리 및 큐 처리가 가능함.
---
### @Async vs @Async("taskExecutor") 비교
| 항목 | `@Async` | `@Async("taskExecutor")` |
| --- | --- | --- |
| Executor | SimpleAsyncTaskExecutor | ThreadPoolTaskExecutor |
| 스레드 생성 | 매번 새로 생성 | 풀에서 재사용 |
| 코어 스레드 | 없음 | 2개 (설정값) |
| 최대 스레드 | 무제한 | 5개 (설정값) |
| 큐 용량 | 없음 | 100 (설정값) |
| 스레드 명 | SimpleAsyncTaskExecutor-N | async-1, async-2 |
---
### @Async 사용 방식 — 기본 (반환값 없음)
```java
@Service
public class MailService {

    @Async
    public void sendMail(String email) {
        System.out.println("Send mail to " + email);
        System.out.println("Thread: " + Thread.currentThread().getName());
    }
}
```
```java
@RestController
public class MailController {
    private final MailService mailService;

    public MailController(MailService mailService) {
        this.mailService = mailService;
    }

    @GetMapping("/mail")
    public String send() {
        mailService.sendMail("user@test.com");
        return "Request Accepted!";
    }
}
```
Main Thread는 바로 응답을 발송하고, `sendMail` 메서드는 별도의 Thread에서 실행됨.
---
### @Async 사용 방식 — Blocking 방식 (CompletableFuture + .get())
`@Async` 메서드가 `CompletableFuture`를 반환하도록 하고, 호출 측에서 `.get()`으로 결과를 기다리는 방식임.
```java
@Service
public class ReportService {

    @Async
    public CompletableFuture<String> generateReport() {
        Thread.sleep(2000); // 무거운 작업
        return CompletableFuture.completedFuture("Report Complete!");
    }
}
```
```java
// Blocking 대기
String status = reportService.generateReport().get(); // "Report Complete"
```
실행 흐름:
1. `@Async` → `generateReport()`는 별도 스레드에서 실행
2. 하지만 `.get()`을 호출하면
3. 현재 스레드(예: 톰캣 요청 처리 스레드)가 작업 완료까지 대기
4. `generateReport()`가 끝나야 `get()`이 반환됨
즉, 비동기 실행이지만 `.get()`을 호출하는 순간 다시 동기 방식이 됨.
---
### @Async 사용 방식 — Non-Blocking 방식
`.get()`을 호출하지 않고 `CompletableFuture` 자체를 반환하여 완전한 비동기 흐름을 유지하는 방식임.
```java
// Service 파일
@Async("taskExecutor")
public CompletableFuture<String> asyncMethodWithReturn(String message) {
    try {
        Thread.sleep(3000); // 3초 대기
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    String result = "처리 완료: " + message;
    return CompletableFuture.completedFuture(result);
}
```
```java
// Controller 파일
@GetMapping("/future")
public CompletableFuture<String> callAsyncFuture(@RequestParam String message) {
// 즉시 리턴
    CompletableFuture<String> future = asyncService.asyncMethodWithReturn(message);
    return future;
}
```
호출 흐름: `asyncService`는 순수한 원본 객체가 아니라 스프링이 만든 프록시 객체이며, 컨트롤러는 원본 메서드를 직접 실행하는 게 아니라 프록시의 메서드를 호출하게 됨.
---
### \[참고\] CompletableFuture 주요 메서드
| 메서드 | 설명 | 사용 예시 코드 |
| --- | --- | --- |
| `thenApply` | Stream의 map과 유사 | `.thenApply(s -> s + " world")` |
| `thenAccept` | 결과를 수신해서 처리하며 리턴 없음 | `.thenAccept(d -> System.out.println(d))` |
| `whenComplete` | 결과값을 관찰하고 PASS | `future.whenComplete((res, ex) -> { if (ex != null) log.error(...); })` |
| `thenCompose` | FlatMap과 유사 | `.thenCompose(id -> getUserOrderAsync(id))` |
| `thenCombine` | 서로 독립적인 두 비동기 작업을 병합 | `futureA.thenCombine(futureB, (resA, resB) -> resA + resB)` |
| `complete` | 대기 중인 CompletableFuture를 외부에서 수동으로 완료 처리하고 결과 값을 강제로 채움 | `future.complete("Manual Result")` |
---
<empty-block/>
