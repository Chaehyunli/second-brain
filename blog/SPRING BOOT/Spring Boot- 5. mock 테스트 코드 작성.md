---
title: "[Spring Boot] 5. mock 테스트 코드 작성"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/199
---

# [Spring Boot] 5. mock 테스트 코드 작성

## 원문

https://ch010104.tistory.com/199

## 노트 유형

`guide`

## 적용 목적과 전제조건

각 계층은 서로 다른 목적을 가지고 있으며, 사용하는 도구도 다릅니다.

서버 전체를 띄우지 않고 HTTP 요청과 응답만 가짜로 시뮬레이션합니다.

## 구현 절차·검증·주의점

### 1. 테스트 계층별 요약표

각 계층은 서로 다른 목적을 가지고 있으며, 사용하는 도구도 다릅니다.

계층 테스트 종류 주요 어노테이션 핵심 목적

### 2. 계층별 실제 테스트 코드 및 상세 설명

### ① Controller 테스트: "사용자를 어디로 보낼 것인가?"

서버 전체를 띄우지 않고 HTTP 요청과 응답만 가짜로 시뮬레이션합니다.

```java
@ActiveProfiles("test") // test 설정 적용
@WebMvcTest(AuthController.class) // AuthController 관련 빈만 로드
public class AccountControllerTest {

    @Autowired
    private MockMvc mockMvc; // 가짜 HTTP 요청 도구

    @MockBean // 스프링 컨텍스트에 가짜 서비스 등록
    private AccountService accountService;

    @Test
    @DisplayName("이미 존재하는 아이디로 회원가입 시도 시 리다이렉트 확인")
    void signup_fail_duplicate() throws Exception {
        // [Mocking] 서비스가 예외를 던진다고 가정 (Stubbing)
        doThrow(new AccountAlreadyExistsException("중복 ID"))
                .when(accountService).register(any());

        // [Execution & Validation]
        mockMvc.perform(post("/auth/signup")
                        .with(csrf()) // 보안 토큰 포함
                        .param("loginId", "duplicateuser"))
                .andExpect(status().is3xxRedirection()) // 302 리다이렉트 확인
                .andExpect(view().name("redirect:/")); // 홈으로 가는지 확인
    }
}
```

API 호출: mockMvc.perform(post("/auth/signup")) 명령을 내리면, 실제 프로젝트의 AuthController에 정의된 @PostMapping("/signup") 메서드가 실행됩니다.

함수 호출: AuthController 내부 코드는 평소처럼 accountService.register(dto)를 호출합니다.

가짜 객체의 응답: 이때 호출되는 accountService는 진짜 로직이 담긴 객체가 아니라 가짜(Mock)입니다. 이 가짜 객체는 앞서 doThrow(...)로 설정한 대로, **"누군가 나에게 register를 시키면 무조건 에러를 던져야지!"**라고 대기하고 있다가 즉시 예외를 뿜어냅니다.

컨트롤러의 반응: AuthController는 서비스에서 에러가 발생했으니, 이를 catch하거나 예외 처리 로직에 따라 redirect:/를 수행하게 됩니다.

### ② Service 테스트: "로직이 수학적으로 맞는가?"

DB 연결을 완전히 끊고, 순수 자바 코드의 논리(if문, exception 등)만 검증합니다.

```text
@ExtendWith(MockitoExtension.class) // 스프링 없이 Mockito만 사용 (매우 빠름)
class AccountServiceTest {

    @InjectMocks // 가짜 객체들을 주입받을 대상
    private AccountService accountService;

    @Mock // 가짜 DB 접근 객체
    private AccountMapper accountMapper;

    @Test
    @DisplayName("아이디 중복 시 예외가 발생하는지 로직 검증")
    void register_fail_duplicate() {
        // [Given] DB에 이미 해당 아이디가 있다고 가정
        given(accountMapper.existsByLoginId("testuser")).willReturn(true);

        // [When & Then] 실행 시 특정 예외가 터지는지 확인
        assertThrows(AccountAlreadyExistsException.class, () -> {
            accountService.register(new AccountDto("testuser"));
        });
    }
}
```

### ③ Repository 테스트: "DB 테이블과 쿼리가 맞는가?"

가짜(Mock)를 쓰지 않습니다. 실제 DB(H2, Docker 등)에 쿼리를 날려 봅니다.

```text
@MyBatisTest // MyBatis 설정만 로드
@AutoConfigureTestDatabase(replace = Replace.NONE) // 실제 설정된 DB 사용
@Transactional // 테스트 후 자동 롤백 (DB 오염 방지)
class AccountMapperTest {

    @Autowired
    private AccountMapper accountMapper;

    @Test
    @DisplayName("실제 DB 테이블에 INSERT가 잘 되는지 확인")
    void insert_test() {
        // [Execution] 실제 쿼리 실행
        Account account = new Account("newuser", "임채현");
        accountMapper.insertAccount(account);

        // [Validation] DB에서 다시 가져와서 확인
        Account found = accountMapper.findByLoginId("newuser");
        assertThat(found).isNotNull(); // 테이블 구조가 다르면 여기서 에러 발생
        assertThat(found.getName()).isEqualTo("임채현");
    }
}
```

### 3. 핵심 개념 및 용어 최종 정리

### 가짜 객체 다루기 (Mocking)

@Mock vs @MockBean: @Mock은 순수 자바 단위 테스트용, @MockBean은 스프링을 띄우는 컨트롤러 테스트용입니다.

Stubbing: 가짜 객체의 행동을 정의하는 것 (given(...).willReturn(...)).

### DB 환경 (Repository)

H2 Database: 메모리에만 뜨는 가짜 DB. 빠르지만 실제 DB와 문법이 다를 수 있습니다.

Testcontainers (Docker): 테스트 시 Docker로 진짜 DB를 띄우는 방식. 테이블 마이그레이션(Flyway 등)을 거쳐 실제와 똑같은 환경에서 테스트합니다.

@Transactional: 실무 필수템. 테스트가 끝나면 DB에 넣은 데이터를 자동으로 지워(Rollback) 줍니다.

### 파일 규칙

위치: src/test/java 하위의 동일 패키지 경로.

이름: 대상클래스 + Test. (예: AccountControllerTest)

이동: IntelliJ에서 Command + Shift + T로 원본과 테스트를 빠르게 전환합니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
