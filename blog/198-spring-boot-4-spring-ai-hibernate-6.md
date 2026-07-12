---
title: "[Spring Boot] 4. Spring AI & Hibernate 6"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "카테고리 없음"
published: 2026-03-03
source_url: https://ch010104.tistory.com/198
archive_method: Tistory sitemap + HTML content extraction
---

# [Spring Boot] 4. Spring AI & Hibernate 6

> 원문: https://ch010104.tistory.com/198

## 본문

1. Spring AI: AI 서버(Python)와의 통격 및 객체 변환 Spring AI는 파이썬 에이전트가 보내주는 복잡한 JSON 데이터를 자바의 **Type-safe한 객체(Record)**로 자동 변환하는 역할을 합니다. 💡 예시 코드: AI 응답 수신 및 변환 // 1. 파이썬 서버가 보내줄 JSON 구조와 동일하게 Record 정의 public record PlanDetail( String time, String activity, String description, Map<String, Object> extraInfo // AI가 자유롭게 추가한 데이터들 ) {} public record AiItineraryResponse( String chatResponse, int targetDay, List<PlanDetail> dayPlans ) {} // 2. Spring AI 기능을 활용한 서비스 로직 @Service public class AiAgentService { private final RestClient restClient; // Spring AI에서 권장하는 통신 클라이언트 public AiItineraryResponse getItineraryFromPython(String userMessage) { return restClient.post() .uri("<http://python-agent-server/ask>") .body(Map.of("prompt", userMessage)) .retrieve() .onStatus(HttpStatusCode::isError, (req, res) -> { /* 예외 처리 */ }) // 핵심: JSON 응답을 AiItineraryResponse 객체로 자동 매핑 .body(AiItineraryResponse.class); } }   2. Hibernate 6: 자바 객체를 PostgreSQL JSONB에 저장 Hibernate 6는 위에서 Spring AI가 만들어준 자바 객체를 별도의 변환 과정 없이 PostgreSQL의 JSONB 컬럼에 그대로 저장합니다. 💡 예시 코드: JSONB 엔티티 및 저장 import jakarta.persistence.*; import org.hibernate.annotations.JdbcTypeCode; import org.hibernate.type.SqlTypes; @Entity @Table(name = "travel_plans") public class TravelPlanEntity { @Id @GeneratedValue(strategy = GenerationType.IDENTITY) private Long id; private Long chatroomId; // 핵심: Hibernate 6가 List<PlanDetail>을 JSONB로 자동 직렬화 @JdbcTypeCode(SqlTypes.JSON) @Column(columnDefinition = "jsonb") private List<PlanDetail> dayPlans; // 비즈니스 로직: 특정 일차의 일정만 교체 (채현님이 구상한 방식) public void updateDayItinerary(List<PlanDetail> newPlans) { this.dayPlans = newPlans; } } // 3. Repository를 통한 저장 @Repository public interface TravelPlanRepository extends JpaRepository<TravelPlanEntity, Long> { }   3. 전체 흐름 요약 (The Synergy)    단계 수행 주체 작업 내용   1. 요청 Spring AI 사용자의 메시지를 Python 에이전트 서버로 전달합니다.   2. 변환 Spring AI Python이 준 JSON 텍스트를 자바의 AiItineraryResponse 객체로 바꿉니다.   3. 처리 Java Logic 받은 데이터가 유효한지 검증하고, 기존 엔티티의 데이터를 갈아 끼웁니다.   4. 저장 Hibernate 6 dayPlans 객체 리스트를 PostgreSQL JSONB 텍스트로 자동 변환하여 저장합니다.   5. 조회 Hibernate 6 나중에 데이터를 읽을 때, JSONB 텍스트를 다시 List<PlanDetail> 객체로 복원합니다.
