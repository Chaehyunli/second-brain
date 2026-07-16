---
title: "[Spring Boot] 11. Spring Weflux에서의 Transaction 관리"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "SPRING BOOT"
published: 2026-04-27
source_url: https://ch010104.tistory.com/267
---

# [Spring Boot] 11. Spring Weflux에서의 Transaction 관리

## 원문

https://ch010104.tistory.com/267

## 노트 유형

`guide`

## 적용 목적과 전제조건

Spring WebFlux(비동기) 환경에서 블로킹 라이브러리인 JPA를 함께 사용할 때, 가장 흔하게 겪는 문제는 트랜잭션이 적용되지 않거나 중간에 풀려버리는 현상입니다.

Spring의 전통적인 @Transactional은 ThreadLocal 방식을 사용합니다.

## 구현 절차·검증·주의점

Spring WebFlux(비동기) 환경에서 블로킹 라이브러리인 JPA를 함께 사용할 때, 가장 흔하게 겪는 문제는 트랜잭션이 적용되지 않거나 중간에 풀려버리는 현상입니다.

### 1. 왜 @Transactional이 작동하지 않는가?

### 원인 1: ThreadLocal 기반의 트랜잭션 관리

Spring의 전통적인 @Transactional은 ThreadLocal 방식을 사용합니다.

트랜잭션이 시작되면 Spring은 해당 트랜잭션 정보(Connection 등)를 현재 작업을 수행 중인 스레드 전용 저장소(ThreadLocal)에 보관합니다.

이후 호출되는 Repository의 메서드들은 같은 스레드 내의 ThreadLocal에서 이 정보를 꺼내어 같은 트랜잭션 내에서 작업을 수행합니다.

### 원인 2: WebFlux의 멀티 스레딩 및 스레드 전환

WebFlux는 비동기 이벤트 루프 기반입니다. 특히 JPA 같은 블로킹 작업을 위해 subscribeOn(dbScheduler)를 사용하여 스레드를 강제로 전환합니다.

이벤트 루프 스레드: @Transactional이 붙은 서비스 메서드 진입 (여기서 트랜잭션 정보가 ThreadLocal에 저장됨).

스레드 전환: subscribeOn(dbScheduler)에 의해 작업이 DB 전용 스레드로 이동.

DB 스레드: JPA Repository 호출. 하지만 이 스레드의 ThreadLocal에는 아까 저장한 트랜잭션 정보가 없습니다!

결과: JPA는 트랜잭션이 없다고 판단하고 각 작업을 개별적인 Auto-commit으로 처리하거나, 지연 로딩 시 LazyInitializationException을 발생시킵니다.

### 2. 해결책: TransactionTemplate (프로그래매틱 트랜잭션)

해결 방법은 트랜잭션의 시작 시점을 스레드가 전환된 이후로 늦추는 것입니다. 이를 위해 TransactionTemplate을 사용합니다.

### 특징

어노테이션 방식이 아닌 코드로 직접 트랜잭션 범위를 지정합니다.

Mono.fromCallable 내부(즉, DB 스레드로 전환된 이후)에서 트랜잭션을 시작하므로 스레드 불일치 문제가 발생하지 않습니다.

### 3. 코드 구현 상세

### Step 1. Configuration 설정

PlatformTransactionManager를 주입받아 TransactionTemplate을 빈으로 등록합니다.

```java
@Configuration
public class DatabaseConfig {
    @Bean
    public TransactionTemplate transactionTemplate(PlatformTransactionManager transactionManager) {
        // 트랜잭션 전파 속성이나 타임아웃 등을 여기서 설정할 수 있습니다.
        return new TransactionTemplate(transactionManager);
    }
}
```

### Step 2. Service 레이어 구현

@Transactional을 제거하고, transactionTemplate.execute() 블록으로 로직을 감쌉니다.

```java
@Service
@RequiredArgsConstructor
public class ItineraryServiceImpl implements ItineraryService {

    private final ItineraryRepository itineraryRepository;
    private final ItineraryLogRepository itineraryLogRepository;
    private final TransactionTemplate transactionTemplate;
    private final Scheduler dbScheduler;

    @Override
    public Mono<Void> patchItinerary(String roomId, PatchItineraryRequest req) {
        // 1. Mono.fromCallable로 래핑하여 비동기 흐름 생성
        return Mono.fromCallable(() ->
            // 2. dbScheduler로 전환된 'DB 스레드' 안에서 트랜잭션 시작
            transactionTemplate.execute(status -> {
                // [이 블록 내부가 하나의 원자적 트랜잭션 범위]

                // 데이터 조회
                Itinerary itinerary = itineraryRepository.findByRoomId(roomId)
                    .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "일정을 찾을 수 없습니다."));

                // 로그 기록 (작업 A)
                ItineraryLog log = ItineraryLog.of(itinerary);
                itineraryLogRepository.save(log);

                // 정보 수정 (작업 B)
                itinerary.update(req);
                itineraryRepository.save(itinerary);

                // 작업 B 실패 시 작업 A도 자동으로 롤백됨
                return null;
            })
        )
        .subscribeOn(dbScheduler) // 실제 실행 스레드를 DB 전용으로 지정
        .then(); // 결과가 필요 없는 경우 Mono<Void> 반환
    }
}
```

### 4. 핵심 비교: 어노테이션 vs 템플릿

### 5. 결론 및 주의사항

원자성 보장: 두 번 이상의 save()가 일어나는 비즈니스 로직(예: 수정 + 로그 기록)에는 반드시 TransactionTemplate을 사용해야 데이터 정합성이 깨지지 않습니다.

지연 로딩: JPA의 지연 로딩(FetchType.LAZY)은 트랜잭션 범위 내에서만 작동합니다. WebFlux에서 지연 로딩을 쓰려면 반드시 이 템플릿 안에서 객체에 접근해야 합니다.

성능: TransactionTemplate은 꼭 필요한 DB 스레드 타임에만 커넥션을 점유하므로, 어노테이션 방식보다 커넥션 풀 관리에 유리할 수 있습니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/NETWORK/네트워크- 네트워크 계층(Network Layer) 의 구조|[네트워크] 네트워크 계층(Network Layer) 의 구조]]
- [[blog/SPRING BOOT/Spring Boot- 4. Spring AI & Hibernate 6|[Spring Boot] 4. Spring AI & Hibernate 6]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
