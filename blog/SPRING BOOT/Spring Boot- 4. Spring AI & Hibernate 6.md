---
title: "[Spring Boot] 4. Spring AI & Hibernate 6"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/198
---

# [Spring Boot] 4. Spring AI & Hibernate 6

## 원문

https://ch010104.tistory.com/198

## 노트 유형

`guide`

## 적용 목적과 전제조건

Spring AI는 파이썬 에이전트가 보내주는 복잡한 JSON 데이터를 자바의 **Type-safe한 객체(Record)**로 자동 변환하는 역할을 합니다.

Hibernate 6는 위에서 Spring AI가 만들어준 자바 객체를 별도의 변환 과정 없이 PostgreSQL의 JSONB 컬럼에 그대로 저장합니다.

## 구현 절차·검증·주의점

### 1. Spring AI: AI 서버(Python)와의 통격 및 객체 변환

Spring AI는 파이썬 에이전트가 보내주는 복잡한 JSON 데이터를 자바의 **Type-safe한 객체(Record)**로 자동 변환하는 역할을 합니다.

### 💡 예시 코드: AI 응답 수신 및 변환

```java
// 1. 파이썬 서버가 보내줄 JSON 구조와 동일하게 Record 정의
public record PlanDetail(
    String time,
    String activity,
    String description,
    Map<String, Object> extraInfo // AI가 자유롭게 추가한 데이터들
) {}

public record AiItineraryResponse(
    String chatResponse,
    int targetDay,
    List<PlanDetail> dayPlans
) {}

// 2. Spring AI 기능을 활용한 서비스 로직
@Service
public class AiAgentService {
    private final RestClient restClient; // Spring AI에서 권장하는 통신 클라이언트

    public AiItineraryResponse getItineraryFromPython(String userMessage) {
        return restClient.post()
            .uri("<http://python-agent-server/ask>")
            .body(Map.of("prompt", userMessage))
            .retrieve()
            .onStatus(HttpStatusCode::isError, (req, res) -> { /* 예외 처리 */ })
            // 핵심: JSON 응답을 AiItineraryResponse 객체로 자동 매핑
            .body(AiItineraryResponse.class);
    }
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 2. Hibernate 6: 자바 객체를 PostgreSQL JSONB에 저장

Hibernate 6는 위에서 Spring AI가 만들어준 자바 객체를 별도의 변환 과정 없이 PostgreSQL의 JSONB 컬럼에 그대로 저장합니다.

### 💡 예시 코드: JSONB 엔티티 및 저장

```java
import jakarta.persistence.*;
import org.hibernate.annotations.JdbcTypeCode;
import org.hibernate.type.SqlTypes;

@Entity
@Table(name = "travel_plans")
public class TravelPlanEntity {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long chatroomId;

    // 핵심: Hibernate 6가 List<PlanDetail>을 JSONB로 자동 직렬화
    @JdbcTypeCode(SqlTypes.JSON)
    @Column(columnDefinition = "jsonb")
    private List<PlanDetail> dayPlans;

    // 비즈니스 로직: 특정 일차의 일정만 교체 (채현님이 구상한 방식)
    public void updateDayItinerary(List<PlanDetail> newPlans) {
        this.dayPlans = newPlans;
    }
}

// 3. Repository를 통한 저장
@Repository
public interface TravelPlanRepository extends JpaRepository<TravelPlanEntity, Long> {
}
```

### 3. 전체 흐름 요약 (The Synergy)

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/NETWORK/네트워크- 네트워크 계층(Network Layer) 의 구조|[네트워크] 네트워크 계층(Network Layer) 의 구조]]
- [[blog/SPRING BOOT/Spring Boot- 11. Spring Weflux에서의 Transaction 관리|[Spring Boot] 11. Spring Weflux에서의 Transaction 관리]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
