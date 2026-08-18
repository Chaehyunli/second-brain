---
title: "[STUDYING] 24. SpringAI_Day1_핵심 정리"
created: 2026-08-19
updated: 2026-08-19
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-18
source_url: https://ch010104.tistory.com/341
---
# [STUDYING] 24. SpringAI_Day1_핵심 정리

## 원문

https://ch010104.tistory.com/341

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

모델을 다룰 때 반드시 알아야 하는 핵심 용어들. 비용 조절, 품질 제어, 할루시네이션 대응 모두 이 개념들 위에서 작동함.

온도와 top-p는 둘 다 출력 다양성을 조절하는 파라미터이지만, 같이 건드리면 효과가 겹쳐 예측이 어려워지므로 하나만 조작하는 것이 원칙임.

## 원문 기반 개념 정리

### LLM 기본 용어

모델을 다룰 때 반드시 알아야 하는 핵심 용어들. 비용 조절, 품질 제어, 할루시네이션 대응 모두 이 개념들 위에서 작동함.

온도와 top-p는 둘 다 출력 다양성을 조절하는 파라미터이지만, 같이 건드리면 효과가 겹쳐 예측이 어려워지므로 하나만 조작하는 것이 원칙임.

### 임베딩과 벡터 검색

RAG의 동작 원리를 이해하려면 반드시 알아야 하는 아홉 개 개념. 핵심 발상은 하나 — 뜻이 가까우면 벡터도 가깝다.

차원은 임베딩 모델에 묶여 있음. 운영 중에 모델을 교체하면 기존에 저장된 벡터를 전부 다시 계산해야 하므로, 처음 선택이 중요함. 청킹 크기와 겹침 비율은 도메인·문서 성격에 따라 조정해야 하며, 800~1200자 / 10~20%가 범용 출발점임.

### RAG — 근거를 붙여 답하게 하기

RAG(Retrieval-Augmented Generation)는 검색 단계와 생성 단계로 나뉨. 답이 틀렸을 때는 항상 검색 결과부터 눈으로 확인함 — 근거에 답이 없으면 프롬프트를 아무리 고쳐도 좋아지지 않음.

RAG 파이프라인에서 권한 제어는 프롬프트에 "○○만 보여줘"라고 넣는 게 아니라, 필터로 벡터 검색 범위 자체를 제한하는 것이 올바른 방식임. 프롬프트 수준의 권한 처리는 모델이 무시할 수 있음.

### 도구와 에이전트

Tool Calling이 붙는 순간 AI는 말하는 존재가 아니라 행동하는 존재가 됨. 실행은 언제나 우리 코드 — 모델은 어떤 함수를 부를지 결정할 뿐임.

권한 검증은 도구 안에서 해야 함. 모델이 사용자 ID를 지어낼 수 있으므로, 프롬프트에 "당신은 관리자입니다"라고 넣는 방식은 신뢰할 수 없음. 실제 권한 체크는 도구 함수 내부에서 토큰·세션 기반으로 수행해야 함.

### Spring AI 구현 용어

Spring AI의 핵심 추상화 한 겹씩. 구현 교체가 쉬운 이유가 이 계층 덕분이고, 4장부터 코드로 계속 만남.

Advisor는 Spring의 인터셉터/필터 개념과 유사함. 체인 순서가 정책을 결정하므로, 가드레일·로깅 Advisor는 메모리·RAG Advisor보다 앞에 두어야 함. ToolContext는 도구 호출 시 모델이 아닌 서버 컨텍스트(인증 정보, 사용자 ID 등)를 안전하게 전달하는 전용 채널임.

### 계층 구조 — 쉽게 말하면

Spring Boot 애플리케이션의 코드를 역할별 서랍에 나눠 담는 구조임. 계층을 나누는 목적은 아름다움이 아니라 변경의 파급을 가두는 것 — 화면이 바뀌면 Controller만, 정책은 Service만, 저장소는 Repository만 고치면 되는 상태를 만드는 것임.

이렇게 생각하면 쉽다 실제로는 안 나누면

지금은 이것만 기억함 — 역할을 나누고, 위에서 아래로만 부른다. 나머지 어노테이션과 규칙은 이 두 문장을 코드로 옮긴 것임.

### 왜 계층을 나누는가LLM 기본 용어

모델을 다룰 때 반드시 알아야 하는 핵심 용어들. 비용 조절, 품질 제어, 할루시네이션 대응 모두 이 개념들 위에서 작동함.

온도와 top-p는 둘 다 출력 다양성을 조절하는 파라미터이지만, 같이 건드리면 효과가 겹쳐 예측이 어려워지므로 하나만 조작하는 것이 원칙임.

### 임베딩과 벡터 검색

RAG의 동작 원리를 이해하려면 반드시 알아야 하는 아홉 개 개념. 핵심 발상은 하나 — 뜻이 가까우면 벡터도 가깝다.

차원은 임베딩 모델에 묶여 있음. 운영 중에 모델을 교체하면 기존에 저장된 벡터를 전부 다시 계산해야 하므로, 처음 선택이 중요함. 청킹 크기와 겹침 비율은 도메인·문서 성격에 따라 조정해야 하며, 800~1200자 / 10~20%가 범용 출발점임.

### RAG — 근거를 붙여 답하게 하기

RAG(Retrieval-Augmented Generation)는 검색 단계와 생성 단계로 나뉨. 답이 틀렸을 때는 항상 검색 결과부터 눈으로 확인함 — 근거에 답이 없으면 프롬프트를 아무리 고쳐도 좋아지지 않음.

RAG 파이프라인에서 권한 제어는 프롬프트에 "○○만 보여줘"라고 넣는 게 아니라, 필터로 벡터 검색 범위 자체를 제한하는 것이 올바른 방식임. 프롬프트 수준의 권한 처리는 모델이 무시할 수 있음.

### 도구와 에이전트

Tool Calling이 붙는 순간 AI는 말하는 존재가 아니라 행동하는 존재가 됨. 실행은 언제나 우리 코드 — 모델은 어떤 함수를 부를지 결정할 뿐임.

권한 검증은 도구 안에서 해야 함. 모델이 사용자 ID를 지어낼 수 있으므로, 프롬프트에 "당신은 관리자입니다"라고 넣는 방식은 신뢰할 수 없음. 실제 권한 체크는 도구 함수 내부에서 토큰·세션 기반으로 수행해야 함.

### Spring AI 구현 용어

Spring AI의 핵심 추상화 한 겹씩. 구현 교체가 쉬운 이유가 이 계층 덕분이고, 4장부터 코드로 계속 만남.

Advisor는 Spring의 인터셉터/필터 개념과 유사함. 체인 순서가 정책을 결정하므로, 가드레일·로깅 Advisor는 메모리·RAG Advisor보다 앞에 두어야 함. ToolContext는 도구 호출 시 모델이 아닌 서버 컨텍스트(인증 정보, 사용자 ID 등)를 안전하게 전달하는 전용 채널임.

### 계층 구조 — 쉽게 말하면

Spring Boot 애플리케이션의 코드를 역할별 서랍에 나눠 담는 구조임. 계층을 나누는 목적은 아름다움이 아니라 변경의 파급을 가두는 것 — 화면이 바뀌면 Controller만, 정책은 Service만, 저장소는 Repository만 고치면 되는 상태를 만드는 것임.

지금은 이것만 기억함 — 역할을 나누고, 위에서 아래로만 부른다. 나머지 어노테이션과 규칙은 이 두 문장을 코드로 옮긴 것임.

### 왜 계층을 나누는가

각 계층의 책임은 명확히 분리됨.

Controller — 받고·검증하고·돌려준다. 업무 규칙을 넣지 않음.

Service — 업무 흐름과 트랜잭션 경계. 여러 Repository를 조합함.

Repository — 데이터에 닿는 유일한 곳. SQL·쿼리는 여기서 끝남.

Repository가 Service를 부르거나 Controller가 Repository를 직접 부르면 계층은 이미 무너진 것임.

### 요청 한 번의 여정 — 계층을 지나는 길

GET /ch02/orders/12345?userId=user1 한 번이 내부에서 어떻게 번역되는지 순서대로 따라가면 계층의 의미가 명확해짐.

```text
① web/OrderController     HTTP → 자바   @PathVariable · @RequestParam · @Valid
       넘기는 것: 값(orderId, userId)         // 요청 객체를 그대로 넘기지 않는다
② service/OrderService    업무 흐름과 트랜잭션 경계 — "무엇을 하는가"
       넘기는 것: 조건(주문번호 + 소유자)
③ repository/OrderRepository   JPA — 메서드 이름이 곧 쿼리
   mapper/OrderMapper           MyBatis — SQL 을 직접 (같은 자리, 다른 방식)
       돌아오는 것: 엔티티 또는 조회 전용 row
④ dto 변환                엔티티 → 응답 DTO   (ownerId·cost 는 여기서 버려진다)
       돌아오는 것: OrderResponse
⑤ web/OrderController    JSON 직렬화 → 200 OK

# 실패는 계층마다 다른 얼굴로 나타난다
#   400 검증(①) · 404 업무 규칙(②) · 500 SQL·연결(③) · null 변환 누락(④)
```

어디서 실패했는지 알면 어디를 고칠지도 바로 가려짐.

### 어노테이션 지도 — 무엇이 무엇을 하나

어노테이션은 표시일 뿐 — 실제 일은 스프링 부트가 스캔해서 함. 크게 여섯 갈래로 나뉨.

이름이 다른 이유는 의도를 드러내기 위해서이고, 기능은 거의 같음.

### @SpringBootApplication의 정체

@SpringBootApplication은 세 어노테이션을 합친 것임.

```java
@SpringBootApplication      // = 아래 세 개를 합친 것
// @Configuration            // 이 클래스도 설정 클래스다
// @ComponentScan            // 이 패키지 아래의 @Component 계열을 찾는다
// @EnableAutoConfiguration  // 클래스패스를 보고 필요한 빈을 자동 구성한다
public class HelpDeskApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelpDeskApplication.class, args);
    }
}
```

이 클래스가 있는 패키지 아래만 스캔함 — 위치가 곧 스캔 범위임.

```text
// com.skala.helpdesk             ← 여기에 두면
//   ├─ web/      @RestController  ✅ 스캔된다
//   ├─ service/  @Service         ✅ 스캔된다
//   └─ repository/@Repository     ✅ 스캔된다
// com.other.pkg  @Service         ❌ 스캔 안 된다
```

Spring AI의 자동 구성도 @EnableAutoConfiguration에 얹혀 동작함.

### 스테레오타입 — 이름이 다른 이유

@Service · @Repository · @Controller는 모두 @Component의 특수형임. 빈 등록 기능은 같지만 읽는 사람에게 역할을 알려 줌.

```text
@Component      // 범용 — 위 셋 어디에도 맞지 않을 때
class PasswordHasher { }

@Controller     // 화면(View) 반환 — 템플릿 렌더링
@RestController // = @Controller + @ResponseBody — JSON 반환
class OrderController { }

@Service        // 업무 흐름 — 여러 Repository·외부 호출을 조합
class OrderService { }

@Repository     // 데이터 접근 — DB 예외를 Spring Boot 표준 예외로 변환해 준다
class OrderRepository { }

// @Service 를 @Component 로 바꿔도 동작은 같다.
// 그래도 @Service 를 쓰는 이유는, 이 파일을 여는 사람이
// "여기엔 업무 로직이 있겠구나" 하고 바로 알기 때문이다.
```

@Repository만 예외 변환이라는 실제 추가 기능이 있음.

### 빈과 의존성 주입 — 쉽게 말하면

필요한 물건을 내가 만들지 않고 받아 쓰는 것. 스프링 부트가 시작할 때 한 번 만들어 두고, 이후에는 같은 객체를 여러 곳에 주입함.

받아 쓰는 것은 모두가 같이 쓰는 물건이므로, 거기에 내 데이터를 담아 두면 안 됨.

### 빈 — 언제 만들어지고 몇 개인가

빈은 기본적으로 싱글턴 — 앱 전체에 하나만 만들어짐. 생성 시점은 기동 시이므로, 설정 오류가 기동에서 바로 드러남.

```text
@Service
class BadService {
    private String currentUserId;          // ❌ 싱글턴 필드에 요청별 상태
    void handle(String userId) {
        this.currentUserId = userId;       // 동시 요청이 서로 덮어쓴다
    }
}

@Service
class GoodService {
    private final OrderRepository repository;  // ✅ 불변 협력자만 필드로
    void handle(String userId) {               // 요청별 값은 파라미터로
        repository.findByOwnerId(userId);
    }
}

// 스코프 — 특별한 이유가 없으면 기본(싱글턴)을 쓴다
// singleton   앱당 1개            (기본)
// prototype   주입할 때마다 새로
// request     HTTP 요청당 1개   (웹 전용)
```

### @RestController — 요청을 받는 곳

받고·검증하고·서비스에 넘기고·응답 형태로 바꿔 돌려주는 역할만 함. 업무 규칙을 넣지 않으며, if문이 늘어나기 시작하면 서비스로 옮길 신호임. 요청·응답은 DTO(record)로 받고, 엔티티를 그대로 노출하지 않음.

```java
@RestController
@RequestMapping("/api/orders")       // 공통 경로는 클래스에
public class OrderController {

    private final OrderService orderService;   // 서비스만 안다

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping("/{orderId}")                 // GET /api/orders/12345
    public OrderResponse find(@PathVariable String orderId,
                              Principal principal) {
        return orderService.find(orderId, principal.getName());
    }

    @PostMapping                              // POST /api/orders
    @ResponseStatus(HttpStatus.CREATED)
    public OrderResponse create(@Valid @RequestBody CreateOrderRequest request,
                                Principal principal) {
        return orderService.create(request, principal.getName());
    }
}
```

컨트롤러에 if가 쌓이기 시작하면 업무 규칙이 새어 들어온 것임. 검증은 @Valid에, 판단은 서비스에 맡김.

### @Service — 업무 흐름과 트랜잭션

여러 Repository·외부 호출을 조합해 하나의 업무를 완성함. @Transactional로 경계를 긋고, 조회 전용 메서드는 readOnly = true로 선언함.

```java
@Service
@Transactional(readOnly = true)      // 클래스 기본값: 조회
public class OrderService {
    private final OrderRepository orderRepository;
    private final MemberRepository memberRepository;

    public OrderService(OrderRepository orderRepository,  // 생성자 주입
                        MemberRepository memberRepository) {
        this.orderRepository = orderRepository;
        this.memberRepository = memberRepository;
    }

    public OrderResponse find(String orderId, String userId) {
        Order order = orderRepository.findByIdAndOwnerId(orderId, userId)
                .orElseThrow(() -> new OrderNotFoundException(orderId));
        return OrderResponse.from(order);          // 엔티티 → DTO
    }

    @Transactional                                 // 쓰기에서만 재정의
    public OrderResponse create(CreateOrderRequest req, String userId) {
        Member member = memberRepository.findById(userId)
                .orElseThrow(() -> new MemberNotFoundException(userId));
        return OrderResponse.from(orderRepository.save(Order.of(req, member)));
    }
}
```

### @Repository — 데이터에 닿는 곳

DB·외부 API 접근을 여기서 끝냄. 위 계층은 저장 방식을 모름. 인터페이스로 두면 저장소를 갈아 끼워도 서비스는 그대로임. 권한 조건은 쿼리 자체에 넣어야 함 — 조회 후 자바에서 필터링하면 새어 나감.

```java
public interface OrderRepository extends JpaRepository<Order, String> {

// 소유자 조건을 쿼리에 넣는다 — 이 한 줄이 권한 경계다
    Optional<Order> findByIdAndOwnerId(String id, String ownerId);

    List<Order> findTop5ByOwnerIdOrderByOrderedAtDesc(String ownerId);

    @Query("select o from Order o where o.ownerId = :ownerId "
         + "  and o.status in :statuses")
    List<Order> findActive(@Param("ownerId") String ownerId,
                           @Param("statuses") List<OrderStatus> statuses);
}

// 외부 API 도 같은 자리에 둔다 — 서비스는 출처를 모른다
@Repository
public class ShippingApiRepository {
    private final RestClient restClient;
    public Optional<Tracking> findTracking(String invoiceNo) { ... }
}
```

findById()로 꺼낸 뒤 자바에서 소유자를 비교하는 코드는 위험함. 조건을 쿼리에 넣어야 실수로 빠뜨릴 여지가 없음.

### Mapper — SQL을 직접 쓰는 계층

@Mapper 인터페이스에 SQL을 붙이는 방식. 구현체는 MyBatis가 만들어 빈으로 등록함. Repository와 같은 층에 서며, 서비스는 어느 쪽인지 모름. 동적 조건·집계처럼 SQL이 주인공인 자리에서 강함.

```sql
@Mapper                                    // 구현체는 MyBatis 가 만들어 빈으로 등록한다
public interface OrderMapper {
    List<OrderRow> search(OrderSearchCondition condition);  // SQL 은 XML 에

    @Select("select count(*) from orders where owner_id = #{ownerId}")
    long countByOwner(@Param("ownerId") String ownerId);    // 짧으면 애노테이션
}
```

```sql
<!-- resources/mapper/OrderMapper.xml — 조건은 있을 때만 붙는다 -->
<select id="search" resultType="...OrderRow">
  select id as orderId, item, status from orders
  <where>
    owner_id = #{ownerId}                     <!-- 권한 조건은 항상 걸리는 자리에 -->
    <if test="status != null"> and status = #{status}           </if>
    <if test="keyword != null"> and item like '%'||#{keyword}||'%' </if>
  </where>
</select>
```

#{} 는 값 바인딩(PreparedStatement ?), ${} 는 문자열 결합임. 정렬 컬럼처럼 ${} 가 필요한 자리는 허용 목록으로 값을 제한한 뒤에 써야 함 — 그렇지 않으면 SQL 인젝션임.

### JPA vs. Mapper

둘 다 데이터에 닿는 계층이고, 자리는 같고 방식만 다름. 한 프로젝트에서 같이 써도 되며, 실무에서 가장 흔한 조합임.

### DTO — 쉽게 말하면

밖으로 나갈 때 보여 줄 것만 골라 담는 상자임. DB 표를 그대로 보여 주지 않고, 귀찮아 보이지만 사고를 막는 장치임.

DB에 있는 것을 그대로 내보내지 않음. 보여 줄 것만 골라 담는 상자를 하나 만드는 것 — 그 상자가 DTO임.

### DTO와 엔티티 — 계층의 경계

엔티티를 API로 그대로 내보내면 DB 구조가 곧 API 스펙이 됨. 컬럼 하나 바꿨을 뿐인데 클라이언트가 깨짐. record로 요청·응답 DTO를 만들고 변환은 한 곳에서 함.

```text
// 요청 DTO — 검증 규칙을 여기에 붙인다
public record CreateOrderRequest(
        @NotBlank String productId,
        @Min(1) @Max(99) int quantity,
        @Size(max = 200) String memo) { }

// 응답 DTO — 내보낼 필드만 고른다
public record OrderResponse(String orderId, String item,
                             String status, LocalDate eta) {

    public static OrderResponse from(Order order) {   // 변환은 한 곳에서
        return new OrderResponse(order.getId(), order.getItem().getName(),
                order.getStatus().name(), order.getEta());
    }
}

@Entity                                   // 엔티티는 밖으로 나가지 않는다
class Order {
    @Id private String id;
    private String ownerId;               // 내부 전용 — 응답에 없다
    private BigDecimal cost;              // 원가 — 절대 노출하면 안 된다
}
```

### DTO ↔ 엔티티 — 변환은 어디서 하나

변환 코드는 한 곳에 모아야 함. 흩어지면 반드시 필드를 빠뜨림. 방식은 셋 중 하나를 고름.

```text
// ① 정적 팩토리 — 가장 가볍다. 이 프로젝트의 기본.
record OrderResponse(...) { static OrderResponse from(Order o) { ... } }

// ② 매퍼 컴포넌트 — 입구가 둘(엔티티·조회 row)이어도 출구는 하나로 모음
@Component class OrderDtoMapper { OrderResponse toResponse(Order o)    { ... }
                                  OrderResponse toResponse(OrderRow r) { ... } }

// ③ MapStruct — 구현체가 컴파일 시점에 생성된다(리플렉션 비용 없음)
```

### 의존성 주입 — 생성자 주입이 기본

필드 주입(@Autowired)은 테스트가 어렵고 순환 참조를 숨김. 생성자 주입은 final을 쓸 수 있어 불변이고, 누락 시 컴파일 오류가 발생함. 생성자가 하나면 @Autowired도 생략할 수 있음.

```text
// ❌ 필드 주입 — new 로 만들 수 없어 단위 테스트가 번거롭다
@Service
class BadOrderService {
    @Autowired private OrderRepository repository;   // final 불가
}

// ✅ 생성자 주입 — 의존성이 시그니처에 드러난다
@Service
class OrderService {
    private final OrderRepository repository;
    private final ChatClient chatClient;

    OrderService(OrderRepository repository,
                 @Qualifier("supportClient") ChatClient chatClient) {
        this.repository = repository;      // 생성자 하나면 @Autowired 생략
        this.chatClient = chatClient;      // 같은 타입이 여럿이면 @Qualifier
    }
}

// 테스트에서는 그냥 new 로 만든다 — 스프링 부트 컨텍스트가 필요 없다
var service = new OrderService(new FakeOrderRepository(), stubChatClient);
```

### @Configuration — 내가 만드는 빈

내 코드가 아닌 클래스(라이브러리)는 @Component를 붙일 수 없음. 그럴 때 @Configuration 클래스에서 @Bean으로 직접 만듦. Spring AI의 ChatClient · VectorStore도 이 방식으로 구성함.

```java
@Configuration
public class AiConfig {

// 라이브러리 타입이라 @Component 를 붙일 수 없다 → @Bean 으로 만든다
    @Bean
    public ChatClient supportClient(ChatClient.Builder builder) {
        return builder.defaultSystem("너는 친절한 고객 상담원이다.")
                .defaultAdvisors(new SimpleLoggerAdvisor())
                .build();
    }

    @Bean                                           // 조건부 등록 —
    @ConditionalOnMissingBean(VectorStore.class)    // 같은 타입이 있으면 물러난다
    public VectorStore vectorStore(EmbeddingModel embeddingModel) {
        return SimpleVectorStore.builder(embeddingModel).build();
    }
}

// 외부 설정 바인딩 — 코드에 상수를 남기지 않는다
@ConfigurationProperties(prefix = "helpdesk")
public record HelpDeskProperties(int topK, double threshold) { }
```

@ConfigurationProperties를 쓰면 application.yml의 값이 타입 안전하게 바인딩되어 코드에 하드코딩된 상수를 남기지 않아도 됨.

### AOP — 본래 코드를 건드리지 않고

로깅·감사·측정처럼 여기저기 흩어지는 코드를 한곳에 모으는 방법임. @Transactional도 사실 AOP고, Spring AI의 Advisor(12장)도 발상이 같음.

```java
@Aspect
@Component
public class ExecutionTimeAspect {

// "service 패키지의 모든 public 메서드" 를 가로챈다
    @Around("execution(public * com.skala..service..*(..))")
    public Object measure(ProceedingJoinPoint joinPoint) throws Throwable {
        long started = System.nanoTime();
        try {
            return joinPoint.proceed();              // 본래 메서드 실행
        } finally {
            log.info("{} {}ms", joinPoint.getSignature().toShortString(),
                    (System.nanoTime() - started) / 1_000_000);
        }
    }
}

// ⚠ 프록시 기반이라 같은 클래스 안에서 부르면 안 걸린다
//     this.otherMethod();  → AOP 통과 안 함 (자기 호출)
```

AOP는 프록시 기반이므로 같은 클래스 내부에서 this.xxx()로 호출하면 Aspect가 적용되지 않음. 이 제약은 @Transactional에도 동일하게 적용됨.

### 입력 검증과 예외 처리

검증은 DTO에 선언하고 @Valid로 켬 — 컨트롤러에 if를 쌓지 않음. 예외는 던지고, 응답으로 바꾸는 일은 @RestControllerAdvice 한 곳에서 함.

```java
@RestControllerAdvice                         // 모든 컨트롤러의 예외를 여기서 받는다
public class ApiExceptionHandler {

    @ExceptionHandler(OrderNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(OrderNotFoundException e) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body(new ErrorResponse("주문을 찾을 수 없습니다.", null));
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)   // @Valid 실패
    public ResponseEntity<ErrorResponse> handleInvalid(MethodArgumentNotValidException e) {
        String message = e.getBindingResult().getFieldErrors().stream()
                .map(f -> f.getField() + ": " + f.getDefaultMessage()).collect(joining(", "));
        return ResponseEntity.badRequest().body(new ErrorResponse(message, null));
    }

    @ExceptionHandler(Exception.class)                         // 예상 못 한 오류
    public ResponseEntity<ErrorResponse> handleUnexpected(Exception e) {
        String traceId = UUID.randomUUID().toString().substring(0, 8);
        log.error("[{}] 처리 중 오류", traceId, e);              // 상세는 로그에만
        return ResponseEntity.internalServerError()
                .body(new ErrorResponse("처리 중 문제가 발생했습니다.", traceId));
    }
}
```

스택트레이스를 응답에 담으면 내부 구조가 그대로 노출됨. 사용자에겐 안전한 문구와 추적 ID만, 상세는 로그에만 남김.

### API 문서 — 코드에서 나오게 한다

따로 쓴 문서는 반드시 코드와 어긋남 — 시간 문제일 뿐임. 의존성 한 줄이면 컨트롤러가 곧 문서가 되고, @NotBlank 같은 검증 규칙도 문서에 자동 반영됨.

```text
// build.gradle — 이 한 줄이면 /swagger-ui.html 이 생긴다
implementation 'org.springdoc:springdoc-openapi-starter-webmvc-ui:2.8.6'

@Tag(name = "주문", description = "주문 조회·생성")           // 컨트롤러 묶음 이름
@RestController @RequestMapping("/ch02/orders")
class OrderController {

    @Operation(summary = "주문 단건 조회",                    // 목록에 보이는 한 줄
               description = "소유자 조건을 쿼리 안에서 함께 건다")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "조회 성공"),
        @ApiResponse(responseCode = "404", description = "없거나 남의 주문")})
    OrderResponse find(@Parameter(description = "주문번호", example = "12345")
                       @PathVariable String orderId, ...) { ... }
}

// 확인: <http://localhost:8080/swagger-ui.html>  ·  문서(JSON) /v3/api-docs
```

### Swagger UI로 계층을 검증한다

Swagger UI는 '실행되는 문서'임. 프런트·QA·기획이 같은 화면을 보고 이야기하게 되는 것이 가장 큰 이득 — 스펙을 두고 다투는 회의가 사라짐.

### 프로파일 — 환경별로 다르게

개발·운영의 차이는 코드가 아니라 설정으로 표현함. application-{profile}.yml이 공통 설정을 덮어씀. @Profile로 빈 자체를 갈아 끼울 수도 있음.

```text
# application.yml — 공통
helpdesk:
  rag: { top-k: 5, threshold: 0.62 }
---
spring.config.activate.on-profile: local
helpdesk:
  rag: { top-k: 3 }          # 로컬은 빠르게
logging.level.com.skala: DEBUG
---
spring.config.activate.on-profile: prod
logging.level.com.skala: INFO
spring.ai.chat.observations.log-prompt: false
```

```text
@Bean
@Profile("!prod")                              // 운영이 아닐 때만
VectorStore devVectorStore(EmbeddingModel m) {
    return SimpleVectorStore.builder(m).build();  // 인메모리
}
```

운영 프로파일에서는 Swagger UI도 비활성화하는 것이 일반적임 (springdoc.swagger-ui.enabled: false).

### 테스트 — 어디까지 띄울까

전체 컨텍스트를 띄우는 테스트는 느리고 잘 깨짐. 슬라이스 테스트로 필요한 계층만 띄우는 것이 훨씬 빠르며, 계층을 나눠 뒀기 때문에 이런 선택이 가능함.

```text
@DataJpaTest                                // JPA 관련 빈만 — AI 자동구성은 안 뜬다
@Import(OrderService.class)                 // 검증할 서비스만 얹는다
class OrderServiceTest {
    @Autowired OrderService service;
    @Autowired OrderRepository repository;
}
```

### 로깅 — 무엇을 어떻게 남기나

로그는 나중의 나를 위한 것 — 문제가 났을 때만 읽힘. 추적 ID가 없으면 흩어진 로그를 이을 수 없음. 개인정보를 남기지 않는 것이 AI 서비스에서 특히 중요함.

```text
// ❌ 무엇이 실패했는지 알 수 없다
log.error("실패");

// ✅ 추적 ID · 식별자 · 원인을 함께 (개인정보는 제외)
log.error("traceId={} user={} orderId={} 주문 조회 실패",
        traceId, userId, orderId, e);
```

프롬프트 원문을 INFO로 남기지 말아야 함. 고객이 말한 주문번호·전화번호가 그대로 로그에 쌓이고, 로그는 대개 보존 기간이 길고 접근 범위가 넓음.

### AI는 어느 계층에 두나

ChatClient를 컨트롤러에서 직접 부르는 것이 가장 흔한 실수임. AI는 새로운 계층이 아니라 기존 계층에 얹히는 하나의 관심사 — 그래서 자리를 정해 줘야 함.

Controller — AI를 모름. 서비스 인터페이스만 봄.

Service — 어떤 도구를 붙일지, 어떤 프롬프트를 쓸지 결정함.

Config + Advisor — 모델·옵션·공통 관심사(RAG · 메모리 · 안전 · 감사)를 담음.

이 경계를 지키면 프롬프트를 고쳐도 업무 코드는 그대로임.

ChatClient의 정의: Spring AI에서 제공하는 LLM 호출 전용 인터페이스(Fluent API)입니다. Spring의 RestClient나 WebClient처럼 chatClient.prompt().user(...).call().content() 형태로 프롬프트 작성과 모델 호출을 담당

Advisor(어드바이저)란?

개념: 스프링의 인터셉터(Interceptor)나 AOP와 같은 개념. LLM에 요청을 보내기 전과 응답을 받은 후를 낚아채서 공통 관심사를 처리해 주는 모듈

주요 역할:

Chat Memory (대화 메모리): 서비스 로직에서 일일이 대화 이력을 끌어오지 않아도, Advisor가 알아서 이전 대화 목록을 프롬프트 앞단에 붙여주고 응답을 저장.

RAG (검색 증강 생성): 질문이 들어오면 Advisor가 백그라운드에서 VectorStore를 조회해 연관 문맥을 프롬프트에 자동으로 합성.

안전 및 감사: 개인정보 마스킹, 비속어 필터링, 토큰 사용량 로깅 등을 일관되게 처리.

### AI 계층 — 네 축의 책임

AI는 하나의 계층이지 하나의 클래스가 아님. 바뀌는 이유가 다른 것끼리 따로 두어야 따로 고칠 수 있음.

### AI 요청의 여정 — /api/chat 한 번

앞서 본 계층 왕복 위에 AI 축이 얹힌 모습임. Advisor 순서가 곧 정책 — 차단은 저장보다 앞에 있어야 함.

```text
POST /api/chat  {"question":"주문 12345 반품 되나요?"}

① web/ChatController      인증 확인 → 질문·세션 ID 만 서비스로 넘긴다
② advisor/AuditAdvisor    감사 기록 시작           (order 0 — 가장 바깥)
③ advisor/SafetyAdvisor   입력 차단 — 민감어·인젝션 (저장보다 반드시 먼저)
④ advisor/MemoryAdvisor   같은 세션의 앞 대화를 붙인다
⑤ rag/RetrievalService    질문으로 문서 검색 → 근거를 프롬프트에
⑥ chat/HelpDeskService    프롬프트 조립 → 모델 호출
⑦ tools/OrderTools        모델이 필요하다고 판단하면 호출
   repository/OrderRepo     └ 권한 검증과 실제 데이터는 결국 아래 계층에서
⑧ advisor/TokenMeter      토큰·지연 기록 → 지표
⑨ chat/AnswerDto          답변 + 출처 + 도구 사용 여부를 조립해 반환

# 실패도 계층마다 얼굴이 다르다
#   401 인증(①) · 차단(③) · 근거 없음(⑤) · 도구 권한(⑦) · 타임아웃(⑥)
```

### 실습 코드 — 3계층 완성본 (간식 추천)

세 파일이면 계층이 완성됨. GET /lab0/snack?mood=피곤 → 초코바·당 충전.

```text
// ① Controller — 요청을 받아 서비스에 넘기기만 한다
@RestController @RequestMapping("/lab0/snack")
class SnackController {
    private final SnackService service;                  // 저장소는 모른다
    SnackController(SnackService service) { this.service = service; }

    @GetMapping                                          // GET /lab0/snack?mood=피곤
    SnackResponse pick(@RequestParam String mood) { return service.recommend(mood); }
}

// ② Service — '무엇을 하는가' 는 여기에만 적는다
@Service
class SnackService {
    private final SnackRepository repo;
    SnackService(SnackRepository repo) { this.repo = repo; }

    SnackResponse recommend(String mood) {
        Snack s = repo.findByMood(mood)                  // ③ 데이터는 저장소에서만
                      .orElse(new Snack("아메리카노", "무난하게"));
        return new SnackResponse(s.name(), s.reason());  // ④ 나갈 때는 DTO 로
    }
}

record SnackResponse(String name, String reason) {}      // 밖으로 나가는 모양
// 실행 → {"name":"초코바","reason":"당 충전"}
```

### 실행·테스트 — 간식 추천 3계층

```text
# 1) 파일 위치 — 이 폴더에 이미 들어 있다
src/main/java/com/skala/lab0/
    web/SnackController.java    service/SnackService.java    SnackResponse.java
# → 실행: SpringAI_실습/01_간식추천_3계층 폴더를 VS Code 로 열고 F5 (또는 ./gradlew bootRun)

# 2) 호출 (셋 중 편한 것)
curl 'localhost:8080/lab0/snack?mood=피곤'
http/samples.http 에 한 줄 추가해 [Send Request]
<http://localhost:8080/swagger-ui.html>  →  Day1 실습 태그

# 3) 기대 결과
{"name":"초코바","reason":"당 충전"}          # mood 를 바꾸면 답도 바뀐다

# 4) 테스트로 굳히기 — AI 를 안 쓰므로 키 없이 돈다
@WebMvcTest(SnackController.class)
class SnackControllerTest {
    @Autowired MockMvc mvc;  @MockitoBean SnackService service;
    @Test void 추천이_내려온다() throws Exception {
        given(service.recommend("피곤")).willReturn(new SnackResponse("초코바","당 충전"));
        mvc.perform(get("/lab0/snack").param("mood","피곤"))
           .andExpect(status().isOk()).andExpect(jsonPath("$.name").value("초코바"));
    }
}
# 안 되면 —  404: 경로 오타 · 500: 저장소 빈 미등록 · 한글 깨짐: files.encoding utf8
```

### 핵심 요약 — Spring Boot 계층 구조

이 장의 결론은 하나 — 역할을 먼저 정하고 어노테이션은 따라옴. AI 코드도 같은 규칙을 따름.

### LLM과 토큰 — 쉽게 말하면

LLM은 다음에 올 말을 확률로 고르는 프로그램임. 글자가 아니라 토큰 단위로 읽고 쓰며, 토큰이 곧 돈과 길이 제한임.

모델은 기억하지 않음 — 매번 다시 읽음. 대화가 길어지면 느려지고 비싸지는 이유가 여기에 있으며, 이 사실이 뒤에 나오는 메모리·비용 설계의 전부임.

### Spring AI란 무엇인가

AI 모델을 Spring Boot답게 다루게 해 주는 공식 프레임워크임.

HTTP 호출·JSON 파싱·인증을 직접 다루지 않음.

익숙한 의존성 주입·AutoConfiguration·빈 위에서 AI를 씀 — ChatClient 같은 빈을 주입받아 메서드 호출로 끝냄.

Portable API — 공급자가 달라도 코드는 같음.

### LLM 기본 — 토큰·컨텍스트·확률

모델이 다음 토큰을 확률로 고른다는 한 문장이 모든 특성의 원인임.

### 전체 아키텍처 한눈에

내 코드는 추상화(ChatClient · ChatModel)에만 의존함. 공급자 선택은 의존성 + application.yml — Spring Boot가 자동 구성함.

공급자 교체 = 의존성 한 줄 + application.yml — 코드는 그대로임.

### 핵심 설계 원칙

### 3대 핵심 추상화

Spring AI의 뼈대는 세 인터페이스임 — ChatModel · EmbeddingModel · VectorStore. 이 셋의 조합이 챗봇·검색·RAG·에이전트로 확장됨.

ChatModel (대화 및 생성 모델)

역할: 사람이 입력한 프롬프트(질문·지시)를 받아 자연어로 텍스트 응답을 생성하는 LLM 추상화 인터페이스입니다.

주요 기능: 대화(Chat), 문서 요약, 번역, 코드 작성, 도구 호출(Tool Calling) 판단 등 실제 AI의 '추론 및 답변 생성'을 담당합니다.

연동 예시: OpenAI(GPT-4o), Anthropic(Claude), Google Gemini, Ollama 등

EmbeddingModel (의미 벡터 변환 모델)

역할: 사람이 읽는 텍스트(문장·문서)를 컴퓨터가 수학적으로 비교할 수 있는 숫자 배열(Vector)로 변환하는 인터페이스입니다.

주요 기능: 단어의 문자열 자체를 비교하는 것이 아니라 '문장의 의미'를 수치화합니다. 서로 다른 단어를 써도 의미가 비슷하면 벡터 공간상에서 가까운 거리에 위치하게 만들어 RAG(검색 증강 생성)의 기반을 다집니다.

연동 예시: OpenAI text-embedding-3, Ollama Embedding 모델 등

VectorStore (벡터 저장 및 유사도 검색 DB)

역할: EmbeddingModel이 변환한 벡터 데이터를 저장하고, 사용자의 질문과 가장 유사한 의미를 가진 근거 문서를 찾아내는 DB 추상화 인터페이스입니다.

주요 기능: 단순 키워드 matching이 아닌 의미 기반 유사도 검색(Cosine Similarity 등)을 수행하여 질문에 필요한 관련 문맥(Context)을 끌어옵니다.

연동 예시: PGVector, Redis, Pinecone, Qdrant, Chroma 등

셋을 조합하면 — RAG · 챗봇 · 문서 검색 · 에이전트.

### ① ChatModel — 대화의 기본

가장 기본이 되는 추상화 — 프롬프트 → 텍스트 응답. 공급자별 구현(OpenAI·Anthropic·Azure OpenAI 등)을 같은 인터페이스로 씀. 저수준 API이므로 실무에선 대개 ChatClient로 감싸서 씀.

```java
@Service
public class SummaryService {

    private final ChatModel chatModel;   // 생성자 주입

    public String summarize(String text) {
        Prompt prompt = new Prompt("요약해줘:\n" + text);
        return chatModel.call(prompt)
                        .getResult().getOutput().getText();
    }
}
```

### ② EmbeddingModel — 의미를 벡터로

텍스트를 의미를 담은 숫자 목록(벡터)으로 바꿈. 뜻이 비슷하면 벡터도 가깝다는 성질이 의미 기반 검색의 토대임. 검색·RAG·분류·군집의 준비물이 됨.

```java
@Service
public class EmbedService {
    private final EmbeddingModel embeddingModel;

    public float[] embed(String text) {
        return embeddingModel.embed(text);   // 의미 벡터
    }
}
```

### 임베딩과 벡터 — 쉽게 말하면

문장을 숫자 배열로 바꾸는 것이 임베딩임. 뜻이 가까우면 숫자도 가깝고, 그래서 단어가 달라도 찾을 수 있음.

뜻이 가까우면 숫자도 가깝다 — 이 한 문장이 검색(RAG)의 전부임. 키워드가 하나도 안 겹쳐도 찾아 주는 이유가 여기에 있음.

### ③ VectorStore — 유사도 검색

벡터를 저장하고, 질문 벡터와 가까운 조각을 검색함. pgvector·Redis·Chroma 등 여러 저장소를 같은 인터페이스로 씀.

'휴가 내는 법'으로 물어도 '연차 신청' 규정을 찾아냄 — 의미 검색이 가능한 이유임.

### 공급자 독립성 — 코드는 그대로

같은 ChatClient·추상화 코드로 여러 공급자를 교체할 수 있음. 개발은 소형 모델, 운영은 고성능 모델 — 설정만 바꿈.

내 코드 ChatClient·추상화에만 의존 — 한 줄도 바뀌지 않음.

바뀌는 것은 스타터 의존성과 application.yml 뿐.

그래서 개발은 소형 모델 · 운영은 고성능 모델로 분리 가능함.

### 공급자별 옵션 — 공통과 고유

공통 옵션(model · temperature · maxTokens)은 ChatOptions로 동일하게 씀. 공급자 고유 옵션은 각자의 XxxChatOptions로만 지정함. 고유 옵션을 쓰는 순간 그 코드는 그 공급자에 묶임 — 경계를 알고 써야 함.

### 미니 실습 — 3대 추상화 확인

키가 없으면 ①④만 해도 됨.

### 실습 코드 — 내 말과 닮은 속담 찾기

임베딩이 숫자로 보이는 순간임. ?q=조심해서 나쁠 건 없지 → "돌다리도 두들겨..." 가 1등으로 나옴.

```text
@RestController
class ProverbLab {
    private final EmbeddingModel embedding;              // ① 뜻을 숫자로 바꾸는 도구
    ProverbLab(EmbeddingModel embedding) { this.embedding = embedding; }

    static final List<String> 속담 = List.of(
            "티끌 모아 태산", "돌다리도 두들겨 보고 건너라",
            "원숭이도 나무에서 떨어진다", "가는 말이 고와야 오는 말이 곱다");

    @GetMapping("/lab1/proverb")                         // GET ?q=조심해서 나쁠 건 없지
    Map<String, Double> match(@RequestParam String q) {
        float[] 내문장 = embedding.embed(q);             // ② 내 문장 → 숫자 배열
        Map<String, Double> 점수 = new LinkedHashMap<>();
        for (String p : 속담)
            점수.put(p, cosine(내문장, embedding.embed(p)));  // ③ 속담과 거리 재기
        return 점수;
    }

    static double cosine(float[] a, float[] b) {         // 두 화살표가 이루는 각도
        double dot=0, na=0, nb=0;
        for (int i=0;i<a.length;i++){ dot+=a[i]*b[i]; na+=a[i]*a[i]; nb+=b[i]*b[i]; }
        return dot / (Math.sqrt(na)*Math.sqrt(nb));       // 1에 가까울수록 비슷
    }
}
// 결과 예: 돌다리도...(0.62) · 원숭이도...(0.21) · 티끌 모아...(0.18)
```

결과 숫자를 적어 두면 8장에서 다시 씀.

### 실행·테스트 — 속담 유사도

```text
# 1) 파일 위치
src/main/java/com/skala/lab1/ProverbLab.java
# → 실행: SpringAI_실습/02_속담유사도 폴더를 VS Code 로 열고 F5 (또는 ./gradlew bootRun)

# 2) 호출 — 세 문장을 차례로 넣어 본다
curl 'localhost:8080/lab1/proverb?q=조심해서 나쁠 건 없지'
curl 'localhost:8080/lab1/proverb?q=작은 돈도 모으면 커진다'
curl 'localhost:8080/lab1/proverb?q=오늘 점심 뭐 먹지'    # 전부 낮게 나와야 정상

# 3) 기대 결과
{"돌다리도 두들겨 보고 건너라":0.62, "원숭이도...":0.21, "티끌 모아 태산":0.18}

# 4) 테스트로 굳히기 — 값이 아니라 '순서'를 검증한다
@Test void 뜻이_가까운_속담이_1등이다() {
    var r = lab.match("조심해서 나쁠 건 없지");
    String top = r.entrySet().stream().max(Map.Entry.comparingByValue()).get().getKey();
    assertThat(top).contains("돌다리");   // 점수는 모델 버전마다 조금씩 달라진다
}
# 안 되면 —  401: 키 오류 · 빈 결과: 임베딩 모델 설정 · 429: 잠시 후 재시도
```

### 핵심 요약 — 개요와 3대 추상화

2장의 결론 — 내 코드는 추상화에만 의존하고, 공급자는 설정으로 바꿈. 뒤에 나오는 모든 기능이 이 세 인터페이스의 조합임.

### 의존성 설정 (build.gradle)

```java
plugins {
    id 'java'
    id 'org.springframework.boot' version '4.1.0'
    id 'io.spring.dependency-management' version '1.1.7'
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springdoc:springdoc-openapi-starter-webmvc-ui:2.8.6'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'

    // Spring AI BOM — 버전을 한 줄로 맞춤
    implementation platform("org.springframework.ai:spring-ai-bom:2.0.0")

    // 공급자 스타터 — OpenAI 예시, 교체 시 이 줄만 바꿈
    implementation 'org.springframework.ai:spring-ai-starter-model-openai'
}
```

### API 키 보관 원칙

소스와 로그에는 절대 남기지 않음.

```text
# ❌ 절대 하지 않는다
spring.ai.openai.api-key=sk-proj-abc123...   # 소스에 직접

# ✅ yml에는 자리표시만, 실제 값은 환경변수로
# application.yml: api-key: ${OPENAI_API_KEY}
export OPENAI_API_KEY="sk-..."
```

이미 커밋했다면 히스토리에서 지워도 키는 이미 유출된 것으로 봄 — 즉시 폐기·재발급이 우선임.

### 벡터 DB — 언제 무엇을 띄우나

RAG 전까지는 인메모리로 충분함. 운영에 가깝게 해 보려면 Docker로 pgvector 한 줄이면 뜸. 인메모리는 재시작하면 사라짐 — 그것이 교체 시점의 신호임.

```bash
# docker-compose.yml
services:
  pgvector:
    image: pgvector/pgvector:pg17
    environment:
      POSTGRES_DB: springai
      POSTGRES_USER: springai
      POSTGRES_PASSWORD: springai
    ports: ["5432:5432"]
    volumes: ["pgdata:/var/lib/postgresql/data"]
volumes:
  pgdata:
```

```bash
docker compose up -d      # 띄우기
docker compose ps         # 상태 확인
docker compose down       # 내리기 (-v 를 붙이면 데이터도 삭제)
```

### 첫 실행 확인

환경 구성이 끝났는지는 한 번 돌려 봐야 앎. 응답이 한 줄 나오면 이후 장에서 생기는 문제를 코드 문제로 좁힐 수 있음.

```text
@RestController
class HelloAiController {
    private final ChatClient chat;

    HelloAiController(ChatClient.Builder builder) {
        this.chat = builder.build();    // 자동 구성된 빌더를 주입받는다
    }

    @GetMapping("/hello")
    String hello(@RequestParam(defaultValue = "안녕하세요") String q) {
        return chat.prompt().user(q).call().content();
    }
}
```

```text
export OPENAI_API_KEY="sk-..."
./gradlew bootRun       # VS Code 에서는 F5

curl '<http://localhost:8080/hello?q=Spring+Boot+AI를+한+문장으로>'
# → 모델 응답이 그대로 출력되면 환경 구성 완료
```

### 환경 트러블슈팅

이 표에서 안 잡히면 대개 네트워크(사내 프록시)임. 회사 망에서 외부 API가 막혀 있는지부터 확인함.

### 실행·테스트 — 작명 봇

```text
# 1) 실행
# SpringAI_실습/03_작명봇 폴더를 VS Code 로 열고 F5

# 2) 호출
curl 'localhost:8080/lab2/name?keyword=AI,커피,야근'

# 3) 고장 재현 → 복구 순서
unset OPENAI_API_KEY && ./gradlew bootRun    # 기동은 정상
curl 'localhost:8080/lab2/name?keyword=AI'  # 502 + traceId 확인
export OPENAI_API_KEY="sk-..." && ./gradlew bootRun  # 되돌리면 정상
```

### 핵심 요약 — 개발환경 구성

### BOM과 스타터

BOM으로 Spring AI 모듈들의 버전을 한 번에 맞추고, 스타터를 넣으면 해당 공급자 연동이 자동 구성됨. 공급자를 바꾸려면 스타터만 교체 — 코드는 그대로임.

```java
dependencies {
    implementation platform("org.springframework.ai:spring-ai-bom:2.0.0")  // 버전 일괄 관리
    implementation "org.springframework.ai:spring-ai-starter-model-openai"
}
```

### Spring AI 모듈 지도

아티팩트 이름에 규칙이 있음. spring-ai-starter-*는 자동 구성 포함, 나머지는 라이브러리만임.

### application.yml — 기본 설정

공급자 설정은 application.yml에 선언 — 코드가 아님. API 키는 환경변수로 주입 — 소스에 넣지 않음.

```text
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}    # 환경변수에서 주입
      chat:
        options:
          temperature: 0.7          # 응답 다양성(예시값)
```

API 키를 소스·깃에 커밋하지 말 것. 환경변수·시크릿 매니저로 주입함. 유출된 키는 곧 비용·보안 사고로 이어짐.

### 프로파일 전환 — 개발과 운영을 나눈다

```text
# application.yml — 공통(키는 환경변수로만)
spring.ai.openai.api-key: ${OPENAI_API_KEY}

# application-dev.yml — 싸고 빠르게
spring.ai.openai.chat.options:
  model: gpt-4o-mini
  temperature: 0.0
  max-tokens: 300

# application-prod.yml — 품질과 안정성
spring.ai.openai.chat.options:
  model: gpt-4o
  temperature: 0.2
```

```text
SPRING_PROFILES_ACTIVE=dev ./gradlew bootRun    # 코드는 그대로, 설정만 바뀐다
```

### 설정 우선순위

같은 설정이 여러 곳에 있으면 정해진 순서로 덮어씀. "분명히 바꿨는데 안 먹는다"는 대부분 이 순서를 몰라서 생김.

환경변수 이름 규칙 — 점·하이픈을 밑줄로, 대문자로 변환함. spring.ai.openai.api-key → SPRING_AI_OPENAI_API_KEY.

### AutoConfiguration — 무엇이 자동인가

스타터 + 설정만 있으면 Spring Boot가 필요한 빈(ChatModel · ChatClient.Builder · EmbeddingModel 등)을 자동 등록함. 그 빈을 주입받아 쓰기만 하면 됨 — 배선 코드가 없음.

### 프로젝트 구조 — 패키지 나누기

AI 관련 코드를 한 덩어리로 몰아 두지 않음 — 역할별로 나눔. 컨트롤러는 AI를 모름 — 서비스 인터페이스만 봄.

```text
com.skala.ai
├─ config/    AiConfig.java          // ChatClient·Advisor·VectorStore 빈
├─ web/       ChatController.java    // REST·SSE 엔드포인트
├─ service/   AssistantService.java  // 업무 흐름(프롬프트 조립·호출)
├─ rag/       IngestService.java     // 문서 인제스트
│             RetrievalService.java  // 검색·근거 구성
├─ tools/     OrderTools.java        // @Tool 정의(행동)
├─ advisor/   AuditAdvisor.java      // 공통 관심사(로깅·안전)
└─ dto/       AnswerDto.java         // 구조화 출력용 record
```

### 빌더와 점(.) 이어 쓰기 — Fluent API

앞으로 나올 코드는 점(.)을 계속 찍는 모양임. 마지막 한 번에서야 실제 일이 벌어짐.

```text
// ① 생성자로만 만들면 — 인자가 늘수록 못 읽는다
var chat = new Chat("gpt-4o-mini", 0.0, 300, "너는 상담원이다", true, null);

// ② 빌더 — 이름을 붙여, 필요한 것만 담는다
ChatOptions o = ChatOptions.builder()
        .model("gpt-4o-mini")
        .temperature(0.0)
        .maxTokens(300)
        .build();               // ③ 종료 메서드 — 여기서 객체가 실제로 만들어짐

// ④ Fluent API — 체이닝으로 '문장처럼' 읽힘
String answer = chat.prompt()
        .system("너는 상담원이다")
        .user("반품 규정 알려줘")
        .call()                 // 종료 — 여기서 비로소 모델을 부름
        .content();
```

### ChatClient — 쉽게 말하면

모델을 부르는 표준 창구임. 미리 말투와 옵션을 정해 둔 창구를 만들어 두면, 부르는 쪽 코드는 훨씬 단순해짐.

### ChatClient 빈 — 용도별로 나눈다

하나의 ChatClient로 모든 일을 시키면 기본값이 서로 충돌함. 요약용·분류용·상담용처럼 용도별 빈을 만들어 이름으로 주입함.

```text
@Configuration
class AiConfig {

    @Bean                                           // 분류·추출 — 흔들리면 안 되는 일
    ChatClient extractClient(ChatClient.Builder b) {
        return b.defaultSystem("너는 정확한 추출기다. 추측하지 말고 없으면 null.")
                .defaultOptions(ChatOptions.builder().temperature(0.0).build())
                .build();
    }

    @Bean                                           // 상담 — 자연스러움이 중요한 일
    ChatClient supportClient(ChatClient.Builder b) {
        return b.defaultSystem("너는 친절한 고객 상담원이다.")
                .defaultOptions(ChatOptions.builder().temperature(0.7).build())
                .defaultAdvisors(new SimpleLoggerAdvisor())
                .build();
    }
}
```

### HelloAI — 첫 번째 앱

```text
@RestController
class HelloAiController {
    private final ChatClient chat;

    HelloAiController(ChatClient.Builder builder) {
        this.chat = builder.build();
    }

    @GetMapping("/ai")
    String ask(@RequestParam String q) {
        return chat.prompt().user(q).call().content();
    }
}
```

### ChatClient vs ChatModel

### ChatClient 기본 사용법

체인 한 줄에 프롬프트 구성부터 객체 변환까지 담김. .call()은 동기 응답, 결과는 .content() / .entity()로 꺼냄.

### 세 가지 호출 방식

```text
String text    = chat.prompt().user(q).call().content();
Ticket ticket  = chat.prompt().user(q).call().entity(Ticket.class);
var full       = chat.prompt().user(q).call().chatClientResponse();
Flux<String> s = chat.prompt().user(q).stream().content();
```

### 빌더 패턴 — 공통 기본값

```text
@Configuration
class AiConfig {
    @Bean
    ChatClient chatClient(ChatClient.Builder builder) {
        return builder
                .defaultSystem("너는 친절한 고객 상담원이다.")
                .build();
    }
}
```

기본 시스템 메시지·기본 옵션·기본 Advisor를 미리 심어 빈으로 등록함. 이후 호출은 필요한 것만 얹으면 됨 — 중복 제거.

### 메시지 역할 — System과 User

프롬프트는 역할이 다른 메시지의 묶음임.

System — 역할·규칙·말투·페르소나. 매번 같음.

User — 이번 질문. 매번 다름.

대화 이력 — Advisor가 자동으로 주입함.

역할을 나누면 프롬프트가 재사용·관리하기 쉬워짐.

### 결과 받기 — content · entity

응답을 꺼내는 방법은 세 가지임. 무엇이 필요한지에 따라 골라 씀.

.content() — 그냥 문자열 응답. 짧은 답·분류·추출처럼 텍스트만 필요할 때 씀.

.entity(Xxx.class) — 타입 안전한 객체로 변환. 구조화 출력이 필요한 API에서 씀. 문자열 파싱 없이 바로 객체로 받음. → dto와 유사한 기능임(spring ai계의 dto)

.chatClientResponse() — 메타데이터까지 포함한 전체 응답. 토큰 사용량·finishReason·모델명 등 운영 정보가 필요할 때 씀.

```text
// 1) 문자열
String text = chat.prompt().user(q).call().content();

// 2) 객체 (구조화 출력)
record Answer(String summary, List<String> keywords) {}
Answer a = chat.prompt().user(q).call().entity(Answer.class);
```

### 응답 메타데이터 — 무엇이 함께 오나

응답에는 텍스트 말고도 운영에 필요한 정보가 함께 옴. finishReason이 length면 답이 잘린 것임 — 그냥 넘기면 잘린 JSON 파싱이 실패하거나 문장이 끊긴 답이 사용자에게 나감.

```text
ChatResponse response = chat.prompt().user(q).call().chatClientResponse();

// ① 본문
String text = response.getResult().getOutput().getText();

// ② 왜 끝났나 — stop(정상) · length(잘림) · tool_calls(도구 호출)
String finishReason = response.getResult().getMetadata().getFinishReason();
if ("length".equalsIgnoreCase(finishReason)) {
    log.warn("응답이 maxTokens 에서 잘렸다 — 상한을 올리거나 요약을 시키자");
}

// ③ 얼마나 썼나 — 비용 계산의 근거
Usage usage = response.getMetadata().getUsage();
log.info("prompt={} completion={} total={}",
        usage.getPromptTokens(), usage.getCompletionTokens(), usage.getTotalTokens());

// ④ 어떤 모델이 답했나
String model = response.getMetadata().getModel();
```

### 프롬프트 — 쉽게 말하면

프롬프트는 모델에게 주는 업무 지시서임. 잘 쓴 지시서 = 역할·지시·맥락·예시·형식 다섯 가지. 애매하게 시키면 애매하게 돌아옴.

사람에게 일을 시킬 때와 똑같이 쓰면 됨. 역할·할 일·참고 자료·견본·제출 형식 — 이 다섯이면 프롬프트는 충분함.

### 동적 프롬프트 — 파라미터 바인딩

문자열을 이어 붙이지 말고 자리표시자 + 파라미터로 조립함. 주입 위험을 줄이고, 프롬프트를 템플릿으로 재사용할 수 있음.

```text
String reply = chat.prompt()
        .user(u -> u.text("{topic}를 초보자에게 3문장으로 설명해줘")
                    .param("topic", topic))
        .call()
        .content();
```

사용자 입력을 프롬프트 문자열에 직접 이어 붙이지 말 것. 파라미터로 바인딩하면 관리가 쉽고, 뒤에서 배울 주입 공격 방어에도 유리함.

### 핵심 요약 — 설정과 ChatClient

설정은 yml로, 호출은 ChatClient로. 여기까지가 Spring AI의 기본기임.

체크 — 추출용과 상담용 ChatClient의 temperature가 같다면 빈을 나눌 때가 된 것임.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
