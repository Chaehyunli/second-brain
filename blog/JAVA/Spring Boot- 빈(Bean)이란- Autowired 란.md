---
title: "[Spring Boot] 빈(Bean)이란? Autowired 란?"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "backend", "java", "spring boot"]
category: "JAVA"
published: 2025-03-07
source_url: https://ch010104.tistory.com/6
---

# [Spring Boot] 빈(Bean)이란? Autowired 란?

## 원문

https://ch010104.tistory.com/6

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

빈(Bean)은 스프링 프레임워크에서 관리하는 객체(인스턴스)!! 스프링 컨테이너(Spring Container)가 생성하고, 필요한 곳에서 사용할 수 있도록 관리함.

빈을 사용하지 않으면 객체를 new를 사용해서 위와 같이 직접 생성해야함.

## 원문 기반 개념 정리

1. 빈(Bean)이란?

빈(Bean)은 스프링 프레임워크에서 관리하는 객체(인스턴스)!! 스프링 컨테이너(Spring Container)가 생성하고, 필요한 곳에서 사용할 수 있도록 관리함.

💡 즉, "스프링이 직접 관리하는 객체이다.

빈 없이 객체를 생성하는 경우

```java
public class UserService {
    private UserRepository userRepository = new UserRepository(); // 직접 생성

    public void processUser() {
        userRepository.save(new User("홍길동"));
    }
}
```

단점

빈을 사용하지 않으면 객체를 new를 사용해서 위와 같이 직접 생성해야함.

UserRepository의 구현이 바뀌면, UserService도 수정해야 함 → 유지보수 어려움

객체 생성을 직접 해야 하므로, 재사용이 어려움

의존성이 강하게 결합됨 (강한 결합 → 변경이 어려움)

빈을 사용하여 객체를 관리하는 경우

```java
import org.springframework.stereotype.Service;

@Service // UserService를 스프링 빈으로 등록
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) { // 스프링이 자동으로 주입
        this.userRepository = userRepository;
    }

    public void processUser() {
        userRepository.save(new User("홍길동"));
    }
}
```

-> 따라서, 스프링 컨테이너가 직접 객체를 생성해서, 관리하는 부담을 줄이고, 의존성을 주입함. 이처럼 스프링 컨테이너가 객체를 직접 관리하게 하기 위해선 빈으로 클래스를 등록해야함.

일반적으로 서비스 클래스, DAO 클래스, 컨트롤러 클래스 같은 것들이 빈으로 등록.

2. 빈을 등록하는 방법

1) 어노테이션(@Component, @Service, @Repository, @Controller) 사용 (권장)

```java
import org.springframework.stereotype.Service;

@Service // 자동으로 빈으로 등록됨
public class UserService {
    public void hello() {
        System.out.println("Hello, Spring Bean!");
    }
}
```

@Component 는 @Service, @Repository, @Controller 가 모두 포함하고 있는 공통적인 어노테이션!!

하지만, 범용적인 범용적인 어노테이션이라서 역할이 명확하지 않음.

즉, @Component에 역할을 정확하게 명시한 것이 @Service, @Repository, @Controller

2) @Bean을 사용하여 직접 등록

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration // 설정 클래스
public class AppConfig {
    @Bean // UserService를 빈으로 등록
    public UserService userService() {
        return new UserService();
    }
}
```

@Bean을 사용하면 특정 객체를 직접 등록할 수도 있음.

보통 외부 라이브러리나 직접 만든 클래스를 빈으로 등록할 때 사용.

3. 빈 사용하기(@Autowired 란?)

빈을 사용하려면 의존성 주입(DI, Dependency Injection)을 이용함.

1) @Autowired 사용 (권장)

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepository;

    @Autowired // 자동으로 주입
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

@Autowired 없이 Lombok 라이브러리의 @RequiredArgsConstructor를 사용해서도 생성자 주입이 가능!!

```java
@Service
@RequiredArgsConstructor // Lombok이 자동으로 생성자 만들어 줌
public class UserService {
    private final UserRepository userRepository;
}
```

2) ApplicationContext로 직접 가져오기 (비추천)

```java
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        UserService userService = context.getBean(UserService.class);
        userService.hello();
    }
}
```

이 방법은 보통 테스트에서 많이 사용함. 직접 빈을 가져오는 방식은 피하는 것이 좋음.

4. @Autowired 란? (더 자세히)

@Autowired는 크게 3가지 방식으로 의존성을 주입하여 사용할 수 있음.

1) 생성자 주입 (추천)

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) { // 생성자에서 주입
        this.userRepository = userRepository;
    }
}
```

장점

불변성 보장 (final 사용 가능)

테스트가 쉬움 (Mock 객체를 생성자에서 주입 가능)

순환 참조(Circular Dependency) 방지 (잘못된 DI 구조를 피할 수 있음) 💡 스프링 4.3 이상에서는 @Autowired를 생략해도 자동으로 주입됨!

2) 필드 주입(비추천)

```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository; // 필드에 직접 주입

    public void processUser() {
        userRepository.save(new User("홍길동"));
    }
}
```

단점

필드에 직접 주입하면 테스트하기 어려움 (Mock 객체를 넣을 수 없음)

의존성이 명확하지 않음 (어떤 객체가 들어오는지 생성자에서 확인 불가능)

권장되지 않는 방식이므로 지양하는 게 좋음!

3) 세터 주입(특정 경우 사용)

```java
@Service
public class UserService {
    private UserRepository userRepository;

    @Autowired
    public void setUserRepository(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

장점

필요할 때만 주입 가능

선택적 의존성을 가질 때 유용함

단점

불변성 보장 불가 (final 사용 불가능)

세터 메서드가 있어야 함

일반적으로 생성자 주입을 더 권장함.

5. 주의할 점

1) final과 함께 사용하기

final을 사용하면 필수적으로 값이 할당되도록 강제할 수 있음.

스프링이 객체를 주입하지 못하면 컴파일 오류 발생 → 안정성 증가.

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) { // 생성자 주입
        this.userRepository = userRepository;
    }
}
```

2) 순환 참조(Circular Dependency) 피하기

두 개의 빈이 서로를 참조하면 순환 참조 오류가 발생할 수 있음.

```java
@Service
public class AService {
    private final BService bService;

    public AService(BService bService) {
        this.bService = bService;
    }
}

@Service
public class BService {
    private final AService aService;

    public BService(AService aService) {
        this.aService = aService;
    }
}
```

AService에서는 BService를 사용하고, BService에서는 AService를 사용함. 이는 순환 참조 오류가 발생!!

해결 방법:

한쪽의 의존성을 제거하거나

@Lazy 사용하여 순환 참조 해결

```java
@Service
public class AService {
    private final BService bService;

    public AService(@Lazy BService bService) { // @Lazy 추가
        this.bService = bService;
    }
}
```

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/카테고리 없음/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
