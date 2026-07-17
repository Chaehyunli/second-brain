---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-02
source_url: https://ch010104.tistory.com/288
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션

## 원문

https://ch010104.tistory.com/288

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

로그인하지 않은 사용자가 상품 관리 페이지에 접근하면 자동으로 로그인 화면으로 이동시킴.

비즈니스 룰을 담는 핵심 영역인 도메인(Domain)과 사용자 화면 및 요청 처리를 담당하는 웹(Web) 영역을 명확히 분리하여 설계해야 한다.

## 원문 기반 학습 정리

### 1. 로그인 요구사항

### 1) 화면 흐름 및 UI 요구사항

홈 화면 - 로그인 전

회원 가입 버튼

로그인 버튼

홈 화면 - 로그인 후

본인 이름 표시 ("누구님 환영합니다.")

상품 관리 버튼

로그아웃 버튼

회원 가입 및 로그인 화면

회원 가입: 로그인 ID, 비밀번호, 이름 입력

로그인: 로그인 ID, 비밀번호 입력

### 2) 보안 요구사항

로그인한 사용자만 상품에 접근하고 관리할 수 있어야 함.

로그인하지 않은 사용자가 상품 관리 페이지에 접근하면 자동으로 로그인 화면으로 이동시킴.

### 2. 패키지 구조 설계

비즈니스 룰을 담는 핵심 영역인 도메인(Domain)과 사용자 화면 및 요청 처리를 담당하는 웹(Web) 영역을 명확히 분리하여 설계해야 한다.

```text
hello.login
├── domain
│   ├── item
│   ├── member
│   └── login
└── web
    ├── item
    ├── member
    └── login
```

### 도메인과 웹의 의존관계 원칙

도메인(Domain): 화면, UI, 기술 인프라 등등의 영역을 제외한 시스템이 구현해야 하는 핵심 비즈니스 업무 영역.

의존관계 방향: web은 domain을 알고 있고 의존하지만, domain은 web을 전혀 모르게 설계해야 한다. (web -> domain 단방향 의존)

즉, web 패키지를 완전히 삭제하거나 다른 기술로 변경하더라도 domain 패키지는 아무런 영향을 받지 않고 그대로 유지될 수 있어야 한다.

### 3. 홈 화면 및 회원 가입 구현

### 1) 홈 화면 컨트롤러 (HomeController - 초기 버전)

로그인하지 않은 상태에서 처음에 마주하는 홈 화면을 반환하는 기본 컨트롤러이다.

```java
package hello.login.web;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Slf4j
@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

### 2) 홈 화면 뷰 템플릿 (templates/home.html)

```text
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}" href="css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container" style="max-width: 600px">
    <div class="py-5 text-center">
        <h2>홈 화면</h2>
    </div>
    <div class="row">
        <div class="col">
            <button class="w-100 btn btn-secondary btn-lg" type="button"
                    th:onclick="|location.href='@{/members/add}'|">
                회원 가입
            </button>
        </div>
        <div class="col">
            <button class="w-100 btn btn-dark btn-lg" type="button"
                    th:onclick="|location.href='@{/login}'|">
                로그인
            </button>
        </div>
    </div>
    <hr class="my-4">
</div> <!-- /container -->
</body>
</html>
```

### 3) 회원 도메인 객체 (Member)

```java
package hello.login.domain.member;

import lombok.Data;
import javax.validation.constraints.NotEmpty;

@Data
public class Member {

    private Long id; // 시스템 내부 관리용 키(자동 생성)

    @NotEmpty
    private String loginId; // 로그인용 ID (사용자 입력)

    @NotEmpty
    private String name; // 사용자 이름

    @NotEmpty
    private String password; // 비밀번호
}
```

### 4) 회원 리포지토리 (MemberRepository)

메모리에 회원 데이터를 저장하는 간단한 저장소이다.

참고: 동시성 문제가 고려되어 있지 않으므로 실무에서는 ConcurrentHashMap과 AtomicLong의 사용을 고려해야 한다.

```java
package hello.login.domain.member;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;
import java.util.*;

@Slf4j
@Repository
public class MemberRepository {

    private static final Map<Long, Member> store = new HashMap<>(); // static 사용
    private static long sequence = 0L; // static 사용

    public Member save(Member member) {
        member.setId(++sequence);
        log.info("save: member = {}", member);
        store.put(member.getId(), member);
        return member;
    }

    public Member findById(Long id) {
        return store.get(id);
    }

    public Optional<Member> findByLoginId(String loginId) {
        return findAll().stream()
                .filter(m -> m.getLoginId().equals(loginId))
                .findFirst();
    }

    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }
}
```

### 5) 회원 가입 컨트롤러 (MemberController)

```java
package hello.login.web.member;

import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.validation.Valid;

@Controller
@RequiredArgsConstructor
@RequestMapping("/members")
public class MemberController {

    private final MemberRepository memberRepository;

    @GetMapping("/add")
    public String addForm(@ModelAttribute("member") Member member) {
        return "members/addMemberForm";
    }

    @PostMapping("/add")
    public String save(@Valid @ModelAttribute Member member, BindingResult result) {
        if (result.hasErrors()) {
            return "members/addMemberForm";
        }
        memberRepository.save(member);
        return "redirect:/";
    }
}
```

참고: @ModelAttribute("member")를 단순 @ModelAttribute로 축약해도 기능은 동일하나, 개발 도구(IDE)가 해당 명칭을 명확하게 바인딩할 수 있도록 직관적으로 명시해주었다.

### 6) 회원 가입 뷰 템플릿 (templates/members/addMemberForm.html)

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}" href="../css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            max-width: 560px;
        }
        .field-error {
            border-color: #dc3545;
            color: #dc3545;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="py-5 text-center">
        <h2>회원 가입</h2>
    </div>
    <h4 class="mb-3">회원 정보 입력</h4>
    <form action="" th:action th:object="${member}" method="post">
        <div th:if="${#fields.hasGlobalErrors()}">
            <p class="field-error" th:each="err : ${#fields.globalErrors()}" th:text="${err}">전체 오류 메시지</p>
        </div>
        <div>
            <label for="loginId">로그인 ID</label>
            <input type="text" id="loginId" th:field="*{loginId}" class="form-control" th:errorclass="field-error">
            <div class="field-error" th:errors="*{loginId}" />
        </div>
        <div>
            <label for="password">비밀번호</label>
            <input type="password" id="password" th:field="*{password}" class="form-control" th:errorclass="field-error">
            <div class="field-error" th:errors="*{password}" />
        </div>
        <div>
            <label for="name">이름</label>
            <input type="text" id="name" th:field="*{name}" class="form-control" th:errorclass="field-error">
            <div class="field-error" th:errors="*{name}" />
        </div>
        <hr class="my-4">
        <div class="row">
            <div class="col">
                <button class="w-100 btn btn-primary btn-lg" type="submit">회원 가입</button>
            </div>
            <div class="col">
                <button class="w-100 btn btn-secondary btn-lg" type="button"
                        th:onclick="|location.href='@{/}'|">취소</button>
            </div>
        </div>
    </form>
</div> <!-- /container -->
</body>
</html>
```

### 7) 테스트용 초기 데이터 추가 (TestDataInit)

매번 로그인이나 가입을 테스트하기 번거로우므로, 스프링 서버 기동 시 자동으로 더미 아이템과 테스트 계정을 추가해 주는 역할을 담당한다.

테스트 계정 정보: ID: test / Password: test! / Name: 테스터

```java
package hello.login;

import hello.login.domain.item.Item;
import hello.login.domain.item.ItemRepository;
import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import javax.annotation.PostConstruct;

@Component
@RequiredArgsConstructor
public class TestDataInit {

    private final ItemRepository itemRepository;
    private final MemberRepository memberRepository;

    /**
     * 테스트용 데이터 추가
     */
    @PostConstruct
    public void init() {
        itemRepository.save(new Item("itemA", 10000, 10));
        itemRepository.save(new Item("itemB", 20000, 20));

        Member member = new Member();
        member.setLoginId("test");
        member.setPassword("test!");
        member.setName("테스터");
        memberRepository.save(member);
    }
}
```

### 4. 로그인 기능 구현

로그인 ID와 패스워드가 저장소 정보와 일치하는지 판별하는 핵심적인 비즈니스 로직을 구현한다.

### 1) 로그인 서비스 (LoginService)

```java
package hello.login.domain.login;

import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class LoginService {

    private final MemberRepository memberRepository;

    /**
     * @return null 이면 로그인 실패
     */
    public Member login(String loginId, String password) {
        return memberRepository.findByLoginId(loginId)
                .filter(m -> m.getPassword().equals(password))
                .orElse(null);
    }
}
```

findByLoginId를 호출하여 회원을 조회한 뒤, 전달된 password와 일치하는 경우 해당 회원을 반환한다. 비밀번호가 틀리거나 회원이 존재하지 않으면 null을 최종 반환한다.

### 2) 로그인 입력 폼 객체 (LoginForm)

```java
package hello.login.web.login;

import lombok.Data;
import javax.validation.constraints.NotEmpty;

@Data
public class LoginForm {

    @NotEmpty
    private String loginId;

    @NotEmpty
    private String password;
}
```

### 3) 로그인 컨트롤러 (LoginController - 초기 버전)

```java
package hello.login.web.login;

import hello.login.domain.login.LoginService;
import hello.login.domain.member.Member;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import javax.validation.Valid;

@Slf4j
@Controller
@RequiredArgsConstructor
public class LoginController {

    private final LoginService loginService;

    @GetMapping("/login")
    public String loginForm(@ModelAttribute("loginForm") LoginForm form) {
        return "login/loginForm";
    }

    @PostMapping("/login")
    public String login(@Valid @ModelAttribute LoginForm form, BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            return "login/loginForm";
        }

        Member loginMember = loginService.login(form.getLoginId(), form.getPassword());
        log.info("login? {}", loginMember);

        if (loginMember == null) {
            bindingResult.reject("loginFail", "아이디 또는 비밀번호가 맞지 않습니다.");
            return "login/loginForm";
        }

        // 로그인 성공 처리 TODO
        return "redirect:/";
    }
}
```

로그인 실패 시 bindingResult.reject()를 호출하여 특정 필드가 아닌 폼 전체에 해당하는 글로벌 오류(ObjectError)를 생성하고 원래의 로그인 화면으로 보낸다.

### 4) 로그인 폼 뷰 템플릿 (templates/login/loginForm.html)

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}" href="../css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            max-width: 560px;
        }
        .field-error {
            border-color: #dc3545;
            color: #dc3545;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="py-5 text-center">
        <h2>로그인</h2>
    </div>
    <form action="item.html" th:action th:object="${loginForm}" method="post">
        <div th:if="${#fields.hasGlobalErrors()}">
            <p class="field-error" th:each="err : ${#fields.globalErrors()}" th:text="${err}">전체 오류 메시지</p>
        </div>
        <div>
            <label for="loginId">로그인 ID</label>
            <input type="text" id="loginId" th:field="*{loginId}" class="form-control" th:errorclass="field-error">
            <div class="field-error" th:errors="*{loginId}" />
        </div>
        <div>
            <label for="password">비밀번호</label>
            <input type="password" id="password" th:field="*{password}" class="form-control" th:errorclass="field-error">
            <div class="field-error" th:errors="*{password}" />
        </div>
        <hr class="my-4">
        <div class="row">
            <div class="col">
                <button class="w-100 btn btn-primary btn-lg" type="submit">로그인</button>
            </div>
            <div class="col">
                <button class="w-100 btn btn-secondary btn-lg" type="button"
                        th:onclick="|location.href='@{/}'|">취소</button>
            </div>
        </div>
    </form>
</div> <!-- /container -->
</body>
</html>
```

### 5. 로그인 처리하기 - 쿠키(Cookie) 사용

HTTP 프로토콜은 상태를 유지하지 않는 무상태성(Stateless)을 띠고 있기 때문에, 로그인 상태를 유지하기 위해 서버는 클라이언트에 쿠키(Cookie)를 부여한다.

### 1) 쿠키 동작 방식

로그인 성공: 서버가 성공적으로 인증을 마친 뒤, 응답 헤더(Set-Cookie)에 식별 데이터인 memberId를 탑재하여 클라이언트에 보낸다.

쿠키 저장: 브라우저는 응답에 포함된 쿠키를 수신하여 쿠키 저장소에 보관한다.

쿠키 전송: 이후 브라우저에서 서버로 들어오는 모든 요청 헤더(Cookie)에 자동으로 해당 쿠키 정보를 첨부하여 전송한다.

```text
[클라이언트]                              [서버]
  POST /login   ----------------------->  로그인 성공 검증 완료
  (ID, PW 전송)                           쿠키 생성 (memberId=1)
                <-----------------------  HTTP 응답 헤더 (Set-Cookie: memberId=1)

  GET /welcome  ----------------------->  서버는 요청 헤더의 'Cookie'에서 memberId 확인
  (Cookie: memberId=1)                    홍길동 고객으로 식별하고 정보 응답
```

### 2) 쿠키의 종류

영속 쿠키: 만료 날짜(Expires 또는 Max-Age)를 구체적으로 기입해 두면 해당 날짜가 도래할 때까지 브라우저를 닫아도 정보가 유지된다.

세션 쿠키: 만료 날짜를 아예 기재하지 않고 생략한다. 브라우저가 종료되면 자동으로 만료되어 사라진다.

로그아웃 시점에 연결이 만료되길 희망하므로 우리에게 필요한 것은 바로 이 세션 쿠키이다.

### 3) 쿠키 발급 로그인 처리 (LoginController 수정)

```text
// 기존 login() 메서드의 PostMapping을 주석 처리하거나 변경하고 아래 코드를 작성
@PostMapping("/login")
public String login(@Valid @ModelAttribute LoginForm form, BindingResult bindingResult, HttpServletResponse response) {
    if (bindingResult.hasErrors()) {
        return "login/loginForm";
    }

    Member loginMember = loginService.login(form.getLoginId(), form.getPassword());
    log.info("login? {}", loginMember);

    if (loginMember == null) {
        bindingResult.reject("loginFail", "아이디 또는 비밀번호가 맞지 않습니다.");
        return "login/loginForm";
    }

    // 로그인 성공 처리
    // 쿠키에 별도 유효기간을 기재하지 않으면 브라우저 종료 시 증발하는 '세션 쿠키'가 생성됨
    Cookie idCookie = new Cookie("memberId", String.valueOf(loginMember.getId()));
    response.addCookie(idCookie);

    return "redirect:/";
}
```

### 4) 쿠키를 통한 홈 화면 로그인 처리 (HomeController 수정)

클라이언트가 넘겨준 쿠키 값(memberId)을 판별해 로그인 전용 홈 화면으로 보낸다.

```java
package hello.login.web;

import hello.login.domain.member.Member;
import hello.login.domain.member.MemberRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;

@Slf4j
@Controller
@RequiredArgsConstructor
public class HomeController {

    private final MemberRepository memberRepository;

    // 기존 기본 home()의 @GetMapping("/")은 중석 처리

    @GetMapping("/")
    public String homeLogin(
            @CookieValue(name = "memberId", required = false) Long memberId,
            Model model) {

        if (memberId == null) {
            return "home";
        }

        // 로그인 쿠키가 존재한다면 회원 조회
        Member loginMember = memberRepository.findById(memberId);
        if (loginMember == null) {
            return "home";
        }

        model.addAttribute("member", loginMember);
        return "loginHome";
    }
}
```

@CookieValue(name = "memberId", required = false)를 사용하여 손쉽게 특정 쿠키 값을 바인딩할 수 있다. 로그인하지 않은 사용자도 홈 화면에는 접근할 수 있어야 하므로 required = false는 필수이다.

### 5) 로그인 사용자 전용 홈 화면 (templates/loginHome.html)

```text
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}" href="../css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container" style="max-width: 600px">
    <div class="py-5 text-center">
        <h2>홈 화면</h2>
    </div>
    <h4 class="mb-3" th:text="|로그인: ${member.name}|">로그인 사용자 이름</h4>
    <hr class="my-4">
    <div class="row">
        <div class="col">
            <button class="w-100 btn btn-secondary btn-lg" type="button"
                    th:onclick="|location.href='@{/items}'|">
                상품 관리
            </button>
        </div>
        <div class="col">
            <form th:action="@{/logout}" method="post">
                <button class="w-100 btn btn-dark btn-lg" type="submit">
                    로그아웃
                </button>
            </form>
        </div>
    </div>
    <hr class="my-4">
</div> <!-- /container -->
</body>
</html>
```

### 6) 로그아웃 구현 (LoginController 추가)

쿠키의 생존 만료 시간을 0으로 세팅해서 내보내면 클라이언트는 즉시 해당 쿠키를 파기하게 된다.

```text
@PostMapping("/logout")
public String logout(HttpServletResponse response) {
    expireCookie(response, "memberId");
    return "redirect:/";
}

private void expireCookie(HttpServletResponse response, String cookieName) {
    Cookie cookie = new Cookie(cookieName, null);
    cookie.setMaxAge(0); // 만료 시간을 0으로 기재하여 쿠키 삭제 유도
    response.addCookie(cookie);
}
```

### 6. 쿠키와 보안 문제

단순 쿠키 방식(memberId 노출)은 구현은 편리하지만 매우 심각한 치안적 취약점을 안고 있다.

### 1) 보안적 취약성 및 이슈

쿠키 값 위변조 가능: 브라우저 개발자 도구의 Application 탭을 활용하여 사용자가 로컬에서 수동으로 memberId=1을 memberId=2로 손쉽게 바꿀 수 있다. 변경하는 순간 다른 유저의 신원으로 위조되어 로그인 처리된다.

쿠키 내 정보 탈취: 쿠키 내부에 비밀번호나 개인 신상 정보, 신용카드 번호 등이 담겨 있다면, 네트워크 패킷 탈취(스니핑) 혹은 로컬 PC에 존재하는 악성코드에 의해 고스란히 유출될 수 있다.

해커의 쿠키 탈취 후 재사용: 한번 유출된 쿠키 값은 해커가 무제한으로 사용하며 비정상적인 요청을 계속해서 수행할 수 있다.

### 2) 보완책 (대안)

중요한 데이터는 클라이언트 PC가 아닌 서버 메모리(세션 저장소) 내부에 직접 저장하고 관리해야 한다.

클라이언트에게는 정보가 유추 불가능한 랜덤 키 문자열인 토큰(Token)만 전달해야 한다.

이 토큰은 해커가 추론해 낼 수 없도록 완전 무작위 형태(예: UUID)여야 한다.

토큰 탈취 범죄를 예방하기 위해 만료 시간(예: 30분)을 매우 짧게 두고, 의심 정황 발견 시 원격으로 무력화할 수 있어야 한다.

### 7. 로그인 처리하기 - 세션(Session) 동작 방식

쿠키의 보안 위협을 해결하기 위해 개발된 개념이 바로 세션(Session)이다.

```text
[웹브라우저]                               [서버 (세션 관리자)]
  POST /login   ----------------------->  1. 계정 정보 일치 확인
                                          2. 추정 불가능한 세션 ID(UUID) 생성
                                             - sessionId = "zz0101xx..."
                                          3. 세션 저장소에 매핑 값 저장
                                             - ["zz0101xx..."] : [memberA]
                                          4. sessionId를 쿠키로 반환
                <-----------------------  HTTP 응답 헤더 (Set-Cookie: mySessionId="zz0101xx...")
```

세션 저장소 조회: 이후 사용자가 GET / 같은 요청 시 mySessionId 쿠키를 동봉하면, 서버는 세션 저장소 안에서 "zz0101xx..." 키를 바탕으로 내부에 연동해 둔 memberA 객체를 꺼내어 식별한다.

보안적 강점:

정보 위변조 차단: 랜덤 문자열 세션 ID는 위변조해봤자 서버 측 저장소에 해당 키가 매핑되어 있지 않으면 무효 처리된다.

탈취 한계: 쿠키 속에는 의미 없는 문자열인 세션 ID만 존재하므로 개인 정보가 유출되지 않는다.

타임아웃 만료: 탈취되더라도 서버 측에서 임의로 세션을 강제 종료하거나 유효 시간을 단축할 수 있다.

### 8. 로그인 처리하기 - 세션 직접 만들기

세션 메커니즘을 보다 명확히 이해하기 위해 세션 저장 기능(생성, 조회, 만료)을 수동으로 직접 작성해 본다.

### 1) 세션 관리자 (SessionManager)

다중 스레드 환경에서 안전하게 사용하기 위해 HashMap 대신 ConcurrentHashMap을 사용했다.

```java
package hello.login.web.session;

import org.springframework.stereotype.Component;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Arrays;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 세션 관리
 */
@Component
public class SessionManager {

    public static final String SESSION_COOKIE_NAME = "mySessionId";

    // 동시성 해결을 위해 ConcurrentHashMap 사용
    private Map<String, Object> sessionStore = new ConcurrentHashMap<>();

    /**
     * 세션 생성
     */
    public void createSession(Object value, HttpServletResponse response) {
        // 세션 id 생성 (임의의 추정 불가능한 값 생성)
        String sessionId = UUID.randomUUID().toString();
        sessionStore.put(sessionId, value);

        // 쿠키 생성 후 응답에 탑재
        Cookie mySessionCookie = new Cookie(SESSION_COOKIE_NAME, sessionId);
        response.addCookie(mySessionCookie);
    }

    /**
     * 세션 조회
     */
    public Object getSession(HttpServletRequest request) {
        Cookie sessionCookie = findCookie(request, SESSION_COOKIE_NAME);
        if (sessionCookie == null) {
            return null;
        }
        return sessionStore.get(sessionCookie.getValue());
    }

    /**
     * 세션 만료
     */
    public void expire(HttpServletRequest request) {
        Cookie sessionCookie = findCookie(request, SESSION_COOKIE_NAME);
        if (sessionCookie != null) {
            sessionStore.remove(sessionCookie.getValue());
        }
    }

    private Cookie findCookie(HttpServletRequest request, String cookieName) {
        if (request.getCookies() == null) {
            return null;
        }
        return Arrays.stream(request.getCookies())
                .filter(cookie -> cookie.getName().equals(cookieName))
                .findAny()
                .orElse(null);
    }
}
```

### 2) 세션 관리자 테스트 (SessionManagerTest)

실제 톰캣 등 서블릿 컨테이너 환경 없이 단위 테스트 코드를 구동해 보기 위해 스프링이 지원하는 가짜 객체(MockHttpServletRequest, MockHttpServletResponse)를 활용하여 테스트를 검증한다.

```java
package hello.login.web.session;

import hello.login.domain.member.Member;
import org.junit.jupiter.api.Test;
import org.springframework.mock.web.MockHttpServletRequest;
import org.springframework.mock.web.MockHttpServletResponse;
import static org.assertj.core.api.Assertions.assertThat;

class SessionManagerTest {

    SessionManager sessionManager = new SessionManager();

    @Test
    void sessionTest() {
        // [1] 세션 생성 (서버 -> 응답에 담기)
        MockHttpServletResponse response = new MockHttpServletResponse();
        Member member = new Member();
        sessionManager.createSession(member, response);

        // [2] 요청에 응답 쿠키 저장 (클라이언트 -> 요청 헤더로 쿠키 전송 모사)
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.setCookies(response.getCookies());

        // [3] 세션 조회 검증
        Object result = sessionManager.getSession(request);
        assertThat(result).isEqualTo(member);

        // [4] 세션 만료 검증
        sessionManager.expire(request);
        Object expired = sessionManager.getSession(request);
        assertThat(expired).isNull();
    }
}
```

### 3) 직접 만든 세션 적용 (LoginController - V2)

직접 설계한 SessionManager 컴포넌트를 비즈니스 컨트롤러 단에 반영한다.

```text
// LoginController 필드에 SessionManager 추가 의존성 주입 필수
private final SessionManager sessionManager;

// 기존 login() PostMapping은 주석 처리
@PostMapping("/login")
public String loginV2(@Valid @ModelAttribute LoginForm form, BindingResult bindingResult, HttpServletResponse response) {
    if (bindingResult.hasErrors()) {
        return "login/loginForm";
    }

    Member loginMember = loginService.login(form.getLoginId(), form.getPassword());
    log.info("login? {}", loginMember);

    if (loginMember == null) {
        bindingResult.reject("loginFail", "아이디 또는 비밀번호가 맞지 않습니다.");
        return "login/loginForm";
    }

    // 로그인 성공 시 세션 관리자를 통해 무작위 ID 세션 저장소 생성 및 쿠키 발급
    sessionManager.createSession(loginMember, response);
    return "redirect:/";
}

// 기존 logout() PostMapping은 주석 처리
@PostMapping("/logout")
public String logoutV2(HttpServletRequest request) {
    sessionManager.expire(request);
    return "redirect:/";
}
```

### 4) 직접 만든 세션 적용 (HomeController - V2)

```text
// HomeController 내 sessionManager 필드 의존 관계 주입 필요

// 기존 homeLogin() @GetMapping("/") 주석 처리
@GetMapping("/")
public String homeLoginV2(HttpServletRequest request, Model model) {
    // 세션 저장소에 보관된 회원 정보 조회
    Member member = (Member) sessionManager.getSession(request);
    if (member == null) {
        return "home";
    }

    // 로그인 된 사용자
    model.addAttribute("member", member);
    return "loginHome";
}
```

### 9. 로그인 처리하기 - 서블릿 HTTP 세션1

웹 프레임워크 수준에서 범용적으로 세션을 손쉽게 쓸 수 있도록 서블릿 사양은 HttpSession이라는 기술 표준을 이미 내재화해 두었다.

### 1) HttpSession 핵심 구조

동작 방식이 앞서 수동 제작한 SessionManager와 대동소이하다.

클라이언트에 부여하는 쿠키 명칭은 JSESSIONID 이며 그 값은 유추할 수 없는 난수 문자열 형태를 가진다.

예: Cookie: JSESSIONID=5B78E23B513F50164D6FDD8C97B0AD05

### 2) 세션 상수 정의 (SessionConst)

스프링 데이터 연동 시 일관성 있는 세션의 Key 이름을 위해 문자열 상수를 선언한다.

```java
package hello.login.web;

public class SessionConst {
    public static final String LOGIN_MEMBER = "loginMember";
}
```

### 3) 서블릿 공식 세션 로그인 처리 (LoginController - V3)

```text
// 기존 loginV2()의 PostMapping 주석 처리

@PostMapping("/login")
public String loginV3(@Valid @ModelAttribute LoginForm form, BindingResult bindingResult, HttpServletRequest request) {
    if (bindingResult.hasErrors()) {
        return "login/loginForm";
    }

    Member loginMember = loginService.login(form.getLoginId(), form.getPassword());
    log.info("login? {}", loginMember);

    if (loginMember == null) {
        bindingResult.reject("loginFail", "아이디 또는 비밀번호가 맞지 않습니다.");
        return "login/loginForm";
    }

    // 로그인 성공 처리
    // 세션이 존재하면 기존 세션을 조회하고, 없으면 새로 만들어 반환한다. (디폴트: create = true)
    HttpSession session = request.getSession();

    // 세션에 로그인 회원 정보 및 인스턴스 보관
    session.setAttribute(SessionConst.LOGIN_MEMBER, loginMember);

    return "redirect:/";
}
```

### request.getSession(boolean create) 옵션 분석

request.getSession(true) 또는 request.getSession():

세션이 있으면 기존 세션을 반환한다.

세션이 없으면 새로운 신규 세션을 생성하여 반환한다.

request.getSession(false):

세션이 있으면 기존 세션을 반환한다.

세션이 없으면 새로운 세션을 생성하지 않고 null을 최종 리턴한다.

### 4) 서블릿 세션 로그아웃 구현 (LoginController - V3)

```text
// 기존 logoutV2()의 PostMapping 주석 처리

@PostMapping("/logout")
public String logoutV3(HttpServletRequest request) {
    // 세션을 소멸시켜야 하므로 생성하지 않고 조회만 하도록 false 옵션 사용
    HttpSession session = request.getSession(false);
    if (session != null) {
        session.invalidate(); // 해당 세션을 즉시 폭파 제거시킴
    }
    return "redirect:/";
}
```

### 5) 서블릿 세션 홈 화면 로그인 조회 (HomeController - V3)

```text
// 기존 homeLoginV2()의 GetMapping("/") 주석 처리

@GetMapping("/")
public String homeLoginV3(HttpServletRequest request, Model model) {
    // 세션을 찾을 때는 신규 가입을 억제하기 위해 false 설정 사용
    HttpSession session = request.getSession(false);
    if (session == null) {
        return "home";
    }

    Member loginMember = (Member) session.getAttribute(SessionConst.LOGIN_MEMBER);

    // 만약 세션 속성에 적재된 회원 데이터가 아예 없다면 비로그인 홈으로 회송
    if (loginMember == null) {
        return "home";
    }

    // 세션이 안전하게 유지되고 있는 회원이므로 로그인 완료 전용 화면 전환
    model.addAttribute("member", loginMember);
    return "loginHome";
}
```

### 10. 로그인 처리하기 - 서블릿 HTTP 세션2

스프링 프레임워크는 컨트롤러 핸들러 단에서 훨씬 효율적으로 연동 세션에 다가갈 수 있도록 어노테이션 기반 기능들을 다채롭게 수혈해 준다.

### 1) @SessionAttribute 어노테이션의 활용

이미 로그인되어 안정적으로 맺어진 기존 사용자의 특정 세션 값만을 안전하게 뽑아낼 때 유용하다. 이 방식은 세션을 새로 유도/생성하지 않는 특징을 내포한다.

required = false 옵션을 주어 로그인 유무와 무관하게 타깃 메서드 진입을 가능케 처리한다.

```text
// HomeController 내 homeLoginV3() @GetMapping("/")을 주석 처리

@GetMapping("/")
public String homeLoginV3Spring(
        @SessionAttribute(name = SessionConst.LOGIN_MEMBER, required = false) Member loginMember,
        Model model) {

    // 세션 바인딩 데이터가 부재하면 로그인 전 화면으로 환원
    if (loginMember == null) {
        return "home";
    }

    // 세션이 성공적으로 유지 확인되면 회원 데이터를 모델에 할당
    model.addAttribute("member", loginMember);
    return "loginHome";
}
```

스프링의 내부 동작에 힘입어 세션을 직접 구하고 뜯어 수동 다운캐스팅하는 절차를 생략하고 한 번에 원하는 어트리뷰트를 꺼낼 수 있게 고도화되었다.

### 2) Tracking Modes (URL 전송 방식과 jsessionid 비활성화)

사용자 브라우저가 최초 로그인 시도 시 쿠키 지원 상태가 비확정 상태일 때, WAS(서블릿 컨테이너)는 URL의 맨 끝자락에 ;jsessionid=...와 같은 세션 파라미터를 강제로 부착하여 리다이렉트 처리한다.

타임리프 등의 가변 동적 템플릿 엔진이 이 주소를 자동으로 렌더링에 반영하는 원리이다.

하지만 실제 대부분의 프로덕션은 쿠키만 써서 세션 관계를 굳히는 방식을 정론으로 삼는다. URL에 지속해서 중요 키 세션정보가 노출되면 유출 및 404 오류 유발 등의 문제가 있다.

이를 제어하기 위해 항상 쿠키를 주축으로만 강제 추적하도록 설정해야 한다.

### application.properties 설정 추가

```text
server.servlet.session.tracking-modes=cookie
```

위 문구를 삽입해주면 주소창 끝에 원치 않게 붙던 거슬리는 ;jsessionid=... 문자열 정보가 강제 소멸하고 오로지 순수 쿠키만으로 연동하게 제한된다.

### 11. 세션 정보와 타임아웃 설정

WAS 내부 세션 영역이 점유하고 있는 기술 데이터 및 만료시간 보존 전략이다.

### 1) 세션 상태값 데이터 상세 검토 (SessionInfoController)

실제 생성된 세션 안에 어떤 보조 메타데이터 값들이 채워지는지 직접 로깅하여 알아볼 수 있다.

```java
package hello.login.web.session;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.Date;

@Slf4j
@RestController
public class SessionInfoController {

    @GetMapping("/session-info")
    public String sessionInfo(HttpServletRequest request) {
        HttpSession session = request.getSession(false);
        if (session == null) {
            return "세션이 없습니다.";
        }

        // 세션 데이터 출력
        session.getAttributeNames().asIterator()
                .forEachRemaining(name -> log.info("session name = {}, value = {}", name, session.getAttribute(name)));

        log.info("sessionId = {}", session.getId());
        log.info("maxInactiveInterval = {}", session.getMaxInactiveInterval());
        log.info("creationTime = {}", new Date(session.getCreationTime()));
        log.info("lastAccessedTime = {}", new Date(session.getLastAccessedTime()));
        log.info("isNew = {}", session.isNew());

        return "세션 출력";
    }
}
```

### 세션 반환 메타데이터 목록 정보

sessionId: 세션 ID (JSESSIONID 값)

maxInactiveInterval: 세션의 최대 유효 지정 허용 기간(초 단위). 디폴트는 1800초 (30분).

creationTime: 실제 해당 세션이 신규로 잉태되어 발생한 시간 기록.

lastAccessedTime: 연동 사용자가 가장 마지막으로 WAS를 터치 및 유입하여 접근했던 최종 최신 시각 기록.

isNew: 이 세션이 해당 요청을 타고 방금 막 조립된 따끈따끈한 세션인지, 아니면 전부터 쓰이던 세션의 조회인지 여부 판별.

### 2) 세션 무한정 누적 시 발생하는 자원 메모리 문제

대다수 이용자는 수동 로그아웃 처리를 하기보다 단순히 크롬 브라우저를 X 눌러 즉시 이탈하곤 한다.

비연결성(Connectionless)을 고수하는 HTTP 환경 하에서는 WAS 입장에서 사용자가 아예 떠난 것인지 식별할 재간이 마땅치 않다.

세션을 영원히 메모리에 남겨둔다면:

해커가 JSESSIONID 쿠키 하나만 갈취해서 들어와도 무한정 타인의 세션 권한을 빌릴 수 있는 악의적 위협이 잔존한다.

물리 RAM 서버 자원은 한정되어 있는데, 동시 사용자 수만큼 세션 객체가 적체되어 서버 메모리 부족(OOM) 및 장애로 뻗을 수 있다.

### 3) 해결 방안: 세션 타임아웃 설정 (최근 요청 시각 기준 30분 연장)

사용자가 직접 서비스를 구동해 마우스를 누르고 주소를 호출할 때마다 lastAccessedTime이 계속 초기화되는 원리를 이용한다.

WAS는 세션의 lastAccessedTime 시각으로부터 타임아웃 만료 지정 시간이 경과할 때 비로소 그 죽은 세션을 제거(수거)한다.

즉, 사용자가 30분 동안 아무런 움직임 없이 자리를 비웠을 때에만 로그아웃 처리된다.

### 스프링 부트 글로벌 설정 (application.properties)

```text
# 유효 시간 설정은 반드시 분(Minute) 단위로 적어주어야 한다. (디폴트: 1800 -> 30분)
server.servlet.session.timeout=1800
```

만약 최소 60초(1분) 등으로 가혹하게 테스트해 보려면 server.servlet.session.timeout=60 혹은 120 형태로 적는다.

### 소스코드 레벨 개별 지정 (특정 세션 인스턴스에만 시간 설정 적용)

```text
session.setMaxInactiveInterval(1800); // 초 단위 설정으로 특정 세션만 정교 제어 가능
```

### 12. 최종 요약 정리 및 주의점

도메인 분리: 웹 계층(web)의 결합과 오염으로부터 비즈니스 중심(domain)을 격리하는 철저한 단방향 의존성 아키텍처는 향후 유지보수 확장 시 필수이다.

세션 메커니즘: 쿠키에 중요한 고유값(memberId)을 유출하면 위변조 및 해킹에 무방비가 된다. 중요 상태는 오로지 서버 상의 안전한 세션에 탑재하고, 유추 불가능한 랜덤 키 문자열 토큰으로 사용자들을 구분 연동해야 한다.

리소스 최소화: 세션 저장소 공간은 서버 물리 메모리(JVM Heap)를 곧바로 점유한다. 여기에 지나치게 크고 뚱뚱한 컬렉션이나 다량의 객체를 무분별하게 실어 나르면 안 된다. 필요한 최소한의 고유 식별 Key(memberId 등) 정보만 담는 것을 정론으로 삼아야 한다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
