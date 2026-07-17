---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 9. API 예외 처리"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-04
source_url: https://ch010104.tistory.com/291
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 9. API 예외 처리

## 원문

https://ch010104.tistory.com/291

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

HTML 페이지의 경우 4xx, 5xx와 같은 오류 페이지만 있으면 대부분의 문제를 해결할 수 있습니다.

반면, API는 각 오류 상황에 맞는 오류 응답 스펙을 정의하고, JSON 데이터를 내려주어야 합니다.

## 원문 기반 학습 정리

### 1. API 예외 처리 - 시작

### 목표

HTML 페이지의 경우 4xx, 5xx와 같은 오류 페이지만 있으면 대부분의 문제를 해결할 수 있습니다.

반면, API는 각 오류 상황에 맞는 오류 응답 스펙을 정의하고, JSON 데이터를 내려주어야 합니다.

서블릿 오류 페이지 방식을 시작으로 스프링이 제공하는 혁신적인 예외 처리 방식까지 알아봅니다.

### 서블릿 오류 페이지 방식의 재적용

### WebServerCustomizer 다시 동작

예외가 발생했을 때 WAS가 오류 페이지 경로를 호출하도록 이전에 작성했던 WebServerCustomizer를 다시 활성화합니다.

```java
package hello.exception;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.ErrorPage;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;

@Component
public class WebServerCustomizer implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {
    @Override
    public void customize(ConfigurableWebServerFactory factory) {
        ErrorPage errorPage404 = new ErrorPage(HttpStatus.NOT_FOUND, "/error-page/404");
        ErrorPage errorPage500 = new ErrorPage(HttpStatus.INTERNAL_SERVER_ERROR, "/error-page/500");
        ErrorPage errorPageEx = new ErrorPage(RuntimeException.class, "/error-page/500");

        factory.addErrorPages(errorPage404, errorPage500, errorPageEx);
    }
}
```

@Component 애노테이션의 주석을 해제하여 스프링 빈으로 등록합니다.

예외가 WAS까지 전달되거나 response.sendError()가 호출되면 등록된 예외 페이지 경로가 다시 호출됩니다.

### ApiExceptionController (테스트용 API 컨트롤러)

```java
package hello.exception.api;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
public class ApiExceptionController {

    @GetMapping("/api/members/{id}")
    public MemberDto getMember(@PathVariable("id") String id) {
        if (id.equals("ex")) {
            throw new RuntimeException("잘못된 사용자");
        }
        return new MemberDto(id, "hello " + id);
    }

    @Data
    @AllArgsConstructor
    static class MemberDto {
        private String memberId;
        private String name;
    }
}
```

id의 값이 "ex"로 들어오면 RuntimeException이 발생합니다.

### Postman을 이용한 API 테스트

### 1. 정상 호출

Request URL: GET <http://localhost:8080/api/members/spring>

Response Body (JSON):

```text
{
  "memberId": "spring",
  "name": "hello spring"
}
```

### 2. 예외 발생 호출 (문제 발생)

Request URL: GET <http://localhost:8080/api/members/ex>

HTTP Header Accept: application/json

Response Body (HTML):

문제점: 클라이언트는 정상 응답이든 오류 응답이든 모두 JSON 형태를 받기를 기대합니다. 하지만 기존의 오류 처리 방식은 웹 브라우저 화면용 HTML을 반환하므로 API 예외 상황에 맞지 않습니다.

```text
<!DOCTYPE HTML>
<html>
<head>...</head>
<body>...</body>
</html>
```

### 문제 해결: ErrorPageController에 API 응답 추가

클라이언트의 Accept 헤더가 application/json일 때 JSON으로 반환하도록 오류 컨트롤러를 수정합니다.

```text
// ErrorPageController 클래스 내부에 추가할 메서드
@RequestMapping(value = "/error-page/500", produces = MediaType.APPLICATION_JSON_VALUE)
public ResponseEntity<Map<String, Object>> errorPage500Api(
        HttpServletRequest request, HttpServletResponse response) {

    log.info("API errorPage 500");

    Map<String, Object> result = new HashMap<>();
    Exception ex = (Exception) request.getAttribute(ERROR_EXCEPTION);
    result.put("status", request.getAttribute(ERROR_STATUS_CODE));
    result.put("message", ex.getMessage());

    Integer statusCode = (Integer) request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);

    return new ResponseEntity<>(result, HttpStatus.valueOf(statusCode));
}
```

produces = MediaType.APPLICATION_JSON_VALUE

클라이언트가 요청하는 HTTP Header의 Accept 값이 application/json일 때만 이 메서드가 호출됩니다.

응답용 Map을 구성한 뒤, 스프링의 ResponseEntity를 통해 반환합니다. Jackson 라이브러리가 이 Map을 JSON으로 변환하여 응답 본문에 전송합니다.

### 다시 테스트 실행 (Accept: application/json)

Response Body (JSON):

Accept 헤더가 application/json이 아니거나 text/html인 경우에는 기존의 HTML 뷰 템플릿 오류 페이지가 정상적으로 출력됩니다.

```text
{ "message": "잘못된 사용자", "status": 500 }
```

### 2. API 예외 처리 - 스프링 부트 기본 오류 처리

스프링 부트가 기본으로 제공하는 BasicErrorController를 이용해 API 예외 처리를 수행해 봅니다.

### BasicErrorController 내부 코드 (일부)

```text
@RequestMapping(produces = MediaType.TEXT_HTML_VALUE)
public ModelAndView errorHtml(HttpServletRequest request, HttpServletResponse response) {}

@RequestMapping
public ResponseEntity<Map<String, Object>> error(HttpServletRequest request) {}
```

/error와 동일한 경로를 요청받지만, 헤더 조건에 따라 분기됩니다.

errorHtml(): Accept 헤더가 text/html인 경우 HTML 뷰를 제공합니다.

error(): 그 외의 경우 ResponseEntity를 사용하여 HTTP Body에 JSON 데이터를 반환합니다.

### 스프링 부트 기본 오류 처리 테스트를 위한 준비

이전에 등록한 WebServerCustomizer의 @Component 주석을 다시 적용하여 기본 예외 처리기가 작동하게 합니다.

### Postman을 통한 예외 호출 결과 (GET <http://localhost:8080/api/members/ex>)

```text
{
  "timestamp": "2021-04-28T00:00:00.000+00:00",
  "status": 500,
  "error": "Internal Server Error",
  "exception": "java.lang.RuntimeException",
  "trace": "java.lang.RuntimeException: 잘못된 사용자\n\tat hello.exception.web.api.ApiExceptionController.getMember...",
  "message": "잘못된 사용자",
  "path": "/api/members/ex"
}
```

### 오류 정보 제어 옵션 (application.properties)

기본적으로 제공되는 오류 응답 필드는 아래 옵션들을 활성화하여 상세하게 노출할 수 있습니다.

server.error.include-binding-errors=always

server.error.include-exception=true

server.error.include-message=always

server.error.include-stacktrace=always

주의: 보안상 실제 운영 환경에서는 상세한 오류 정보를 클라이언트에 직접 제공하지 말고, 간결한 메시지만 노출하고 상세 오류 정보는 서버 측 로그로 추적해야 합니다.

### HTML 페이지 vs API 오류 처리의 차이

HTML 페이지: BasicErrorController를 사용하는 방식이 매우 단순하고 편리합니다. (4xx, 5xx 화면 분기 및 일관된 처리)

API 오류 처리: API는 시스템마다, 심지어 동일한 시스템 내의 API 컨트롤러 종류에 따라 서로 완전히 다른 구조의 JSON 형태나 상태 코드를 내려주어야 할 수도 있습니다. 결과적으로 세밀한 제어가 필요하므로 BasicErrorController보다는 뒤에서 소개할 @ExceptionHandler 방식을 사용하는 것이 실무 표준입니다.

### 3. API 예외 처리 - HandlerExceptionResolver 시작

### 목표

컨트롤러 내부에서 예외가 발생하여 WAS까지 던져지면 무조건 HTTP 상태 코드 500(Internal Server Error)이 반환됩니다.

발생한 예외의 종류에 따라 상태 코드를 400, 404 등으로 유연하게 변환하고 싶습니다.

API 스펙에 맞춰 응답 포맷을 커스텀하고 싶습니다.

### 상태 코드 변환 시나리오

컨트롤러에서 IllegalArgumentException이 발생하는 경우 상태 코드를 400(Bad Request)으로 변환해 봅니다.

### ApiExceptionController 수정

```text
@GetMapping("/api/members/{id}")
public MemberDto getMember(@PathVariable("id") String id) {
    if (id.equals("ex")) {
        throw new RuntimeException("잘못된 사용자");
    }
    if (id.equals("bad")) {
        throw new IllegalArgumentException("잘못된 입력 값");
    }
    return new MemberDto(id, "hello " + id);
}
```

http://localhost:8080/api/members/bad 호출 시 IllegalArgumentException이 던져지고 기본 상태 코드는 여전히 500입니다.

### HandlerExceptionResolver (ExceptionResolver)

스프링 MVC는 컨트롤러(핸들러) 밖으로 던져진 예외를 가로채어 해결하고 동작 방식을 새롭게 정의할 수 있는 인터페이스인 HandlerExceptionResolver를 제공합니다.

### 예외 처리 동작 흐름 비교

[1] ExceptionResolver 적용 전

예외가 WAS까지 고스란히 도달하여 WAS가 다시 500 오류를 생성하거나 내부 /error 재요청을 보냅니다. (이때 인터셉터의 postHandle()은 호출되지 않습니다.)

[2] ExceptionResolver 적용 후

ExceptionResolver에서 예외를 처리하면 마치 try-catch로 감싼 것처럼 처리하여 WAS 입장에서는 정상 처리 흐름으로 인식하게 만들 수 있습니다.

### HandlerExceptionResolver 인터페이스

```text
public interface HandlerExceptionResolver {
    ModelAndView resolveException(
            HttpServletRequest request,
            HttpServletResponse response,
            Object handler,
            Exception ex);
}
```

handler: 예외가 발생한 실제 핸들러(컨트롤러)의 정보

ex: 핸들러에서 던져진 예외 객체

### 커스텀 ExceptionResolver 구현

IllegalArgumentException을 처리하여 상태 코드를 400으로 변환하는 리졸버를 구현합니다.

### MyHandlerExceptionResolver

```java
package hello.exception.resolver;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.servlet.HandlerExceptionResolver;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Slf4j
public class MyHandlerExceptionResolver implements HandlerExceptionResolver {

    @Override
    public ModelAndView resolveException(HttpServletRequest request,
                                         HttpServletResponse response,
                                         Object handler,
                                         Exception ex) {
        try {
            if (ex instanceof IllegalArgumentException) {
                log.info("IllegalArgumentException resolver to 400");
                response.sendError(HttpServletResponse.SC_BAD_REQUEST, ex.getMessage());
                return new ModelAndView(); // 빈 ModelAndView 반환
            }
        } catch (IOException e) {
            log.error("resolver ex", e);
        }
        return null; // null 반환 시 다음 ExceptionResolver 탐색
    }
}
```

### ExceptionResolver의 반환 값에 따른 DispatcherServlet 동작 방식

빈 ModelAndView (new ModelAndView()):

뷰를 렌더링하지 않고 정상 흐름으로 제어권을 리턴합니다. 서블릿 컨테이너로 그대로 정상 리턴됩니다.

지정된 ModelAndView (new ModelAndView("뷰이름")):

뷰를 지정해 렌더링을 시도합니다.

null 반환:

등록된 다음 ExceptionResolver를 순차적으로 찾아서 실행합니다. 처리할 수 있는 리졸버가 전혀 없으면 결국 기존 예외를 서블릿 밖(WAS)으로 그냥 던집니다.

### ExceptionResolver의 세 가지 주요 활용법

예외 상태 코드 변환: response.sendError(statusCode)를 호출하여 상태 코드를 임의로 가로채고 바꾼 뒤 빈 ModelAndView를 반환합니다. 이후 WAS는 내부적으로 오류 페이지인 /error를 다시 호출하게 됩니다.

뷰 템플릿 처리: ModelAndView에 모델 값과 오류 뷰 정보를 설정하여 개발자가 마련한 예외 화면을 보여줍니다.

API 응답 처리: response.getWriter().println() 등을 활용해 HTTP 응답 바디에 JSON 등의 데이터를 직접 작성하여 전송할 수 있습니다.

### WebConfig에 ExceptionResolver 등록

```text
// WebMvcConfigurer 구현체 내부
@Override
public void extendHandlerExceptionResolvers(List<HandlerExceptionResolver> resolvers) {
    resolvers.add(new MyHandlerExceptionResolver());
}
```

주의: configureHandlerExceptionResolvers(..)를 사용하면 스프링이 내부적으로 등록하는 기본 ExceptionResolver들이 전부 삭제되므로, 반드시 **extendHandlerExceptionResolvers**를 사용해야 기존 설정들을 보존하면서 추가할 수 있습니다.

### 등록 후 실행 결과 비교

GET <http://localhost:8080/api/members/ex> $\rightarrow$ HTTP 상태 코드 500

GET <http://localhost:8080/api/members/bad> $\rightarrow$ HTTP 상태 코드 400 (바디는 서블릿 오류 페이지 JSON이 적용됨)

### 4. API 예외 처리 - HandlerExceptionResolver 활용

### 예외를 처리기에서 완벽하게 끝내기

앞선 예제처럼 response.sendError()를 이용하는 구조는 WAS까지 예외가 전파되었다가 다시 /error 경로를 타고 컨트롤러가 재호출되는 복잡한 경로를 거칩니다.

ExceptionResolver에서 직접 클라이언트에 JSON 응답을 내려줌으로써, 스프링 MVC 내에서 예외 처리를 깔끔하게 마무리지어 보겠습니다.

### 사용자 정의 예외 추가 (UserException)

```java
package hello.exception.exception;

public class UserException extends RuntimeException {
    public UserException() {
        super();
    }
    public UserException(String message) {
        super(message);
    }
    public UserException(String message, Throwable cause) {
        super(message, cause);
    }
    public UserException(Throwable cause) {
        super(cause);
    }
    protected UserException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
```

### ApiExceptionController에 예외 분기 추가

```text
if (id.equals("user-ex")) {
    throw new UserException("사용자 오류");
}
```

### UserHandlerExceptionResolver 구현

```java
package hello.exception.resolver;

import com.fasterxml.jackson.databind.ObjectMapper;
import hello.exception.exception.UserException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.servlet.HandlerExceptionResolver;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Slf4j
public class UserHandlerExceptionResolver implements HandlerExceptionResolver {

    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public ModelAndView resolveException(HttpServletRequest request,
                                         HttpServletResponse response,
                                         Object handler,
                                         Exception ex) {
        try {
            if (ex instanceof UserException) {
                log.info("UserException resolver to 400");
                String acceptHeader = request.getHeader("accept");
                response.setStatus(HttpServletResponse.SC_BAD_REQUEST);

                if ("application/json".equals(acceptHeader)) {
                    Map<String, Object> errorResult = new HashMap<>();
                    errorResult.put("ex", ex.getClass());
                    errorResult.put("message", ex.getMessage());

                    String result = objectMapper.writeValueAsString(errorResult);

                    response.setContentType("application/json");
                    response.setCharacterEncoding("utf-8");
                    response.getWriter().write(result);

                    return new ModelAndView(); // 예외 해결 처리 (서블릿 정상 반환)
                } else {
                    // TEXT/HTML 타입인 경우 기존의 에러 화면 뷰로 포워딩
                    return new ModelAndView("error/400");
                }
            }
        } catch (IOException e) {
            log.error("resolver ex", e);
        }
        return null;
    }
}
```

클라이언트의 Accept 유형에 따라 동작이 달라집니다.

application/json: JSON 포맷 데이터를 직접 response.getWriter()로 출력하고 빈 ModelAndView를 반환해 흐름을 마칩니다.

text/html 등: error/400에 해당하는 뷰 템플릿 경로를 담아 정상 응답으로 리턴합니다.

### WebConfig에 등록 순서 추가

```text
@Override
public void extendHandlerExceptionResolvers(List<HandlerExceptionResolver> resolvers) {
    resolvers.add(new MyHandlerExceptionResolver());
    resolvers.add(new UserHandlerExceptionResolver());
}
```

### 결과 확인

Request URL: GET <http://localhost:8080/api/members/user-ex>

ACCEPT Header: application/json

Response Body (JSON):(HTTP 상태 코드는 400으로 반환되며, WAS가 오류 컨트롤러를 다시 부르는 복잡한 내부 호출을 막았습니다.)

{ "ex": "hello.exception.exception.UserException", "message": "사용자 오류" }

### 5. API 예외 처리 - 스프링이 제공하는 ExceptionResolver 1 & 2

직접 구현한 커스텀 ExceptionResolver 방식은 수동으로 응답 객체를 조작하고 직접 JSON 문자열을 써야 하므로 매우 복잡합니다. 스프링 부트는 기본적으로 아래 세 개의 ExceptionResolver를 우선순위 순으로 자동 등록해 둡니다.

HandlerExceptionResolverComposite 등록 순서

ExceptionHandlerExceptionResolver (우선순위 최고, @ExceptionHandler 전담)

ResponseStatusExceptionResolver (예외의 @ResponseStatus 애노테이션 전담)

DefaultHandlerExceptionResolver (스프링 내부 기본 예외 전담, 가장 최하위)

### [1] ResponseStatusExceptionResolver

두 가지 예외 상황을 감지하여 알맞은 HTTP 상태 코드를 지정합니다.

예외 클래스에 @ResponseStatus 애노테이션이 설정되어 있는 경우

컨트롤러 내부에서 ResponseStatusException 예외가 명시적으로 발생한 경우

### 1. @ResponseStatus가 붙은 사용자 정의 예외

```java
package hello.exception.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.BAD_REQUEST, reason = "잘못된 요청 오류")
public class BadRequestException extends RuntimeException {
}
```

이 예외가 컨트롤러 밖으로 던져지면 ResponseStatusExceptionResolver가 이 애노테이션을 파싱하고 response.sendError(400, "잘못된 요청 오류")를 내부적으로 대리 호출해 줍니다. 결국 WAS가 /error 재호출 흐름을 유발하게 됩니다.

### 메시지 기능 적용 (reason에 다국어/메시지 리소스 지정)

애노테이션의 reason에 메시지 소스 키값을 설정할 수 있습니다.

```java
@ResponseStatus(code = HttpStatus.BAD_REQUEST, reason = "error.bad")
public class BadRequestException extends RuntimeException {
}
```

messages.properties에 정의된 값을 사용하여 메시지를 출력합니다.

```text
error.bad=잘못된 요청 오류입니다. 메시지 사용
```

### 2. ResponseStatusException 명시적 사용

직접 만든 소스 코드가 아니어서 @ResponseStatus 애노테이션을 동적으로 삽입하기 어려운 외부 라이브러리 예외의 경우나 동적인 예외 조건 변경이 필요할 때는 ResponseStatusException 예외를 생성해 직접 던질 수 있습니다.

```text
// ApiExceptionController 내부에 추가
@GetMapping("/api/response-status-ex2")
public String responseStatusEx2() {
    throw new ResponseStatusException(HttpStatus.NOT_FOUND, "error.bad", new IllegalArgumentException());
}
```

### [2] DefaultHandlerExceptionResolver

스프링 MVC 프레임워크 내부에서 자체적으로 발생하는 예외를 상황에 어울리는 적절한 HTTP 상태 코드로 자동 변환하는 역할을 수행합니다.

예시: 파라미터 바인딩 시 데이터 타입이 맞지 않을 때 발생하는 TypeMismatchException.

원래는 단순 서버 런타임 예외이므로 500 에러를 유발하지만, 실제로는 클라이언트의 요청 파라미터가 잘못된 형식이므로 HTTP 규약상 400 Bad Request가 정당합니다.

DefaultHandlerExceptionResolver는 이 상황을 감지해 response.sendError(400)를 직접 대리 호출해 줍니다.

```text
// ApiExceptionController 내부에 추가
@GetMapping("/api/default-handler-ex")
public String defaultException(@RequestParam Integer data) {
    return "ok";
}
```

결과: data 파라미터에 숫자가 아닌 문자를 전달하면(GET /api/default-handler-ex?data=hello), 상태 코드 400으로 정상 변환되는 것을 확인할 수 있습니다.

### 6. API 예외 처리 - @ExceptionHandler

### 기존 방식의 한계점

ExceptionResolver들을 직접 설정하고 코딩하기에는 비즈니스 에러 모델(ErrorResult)을 생성하고 일일이 JSON 문자열로 변환하는 과정이 무척 장황합니다.

특정 컨트롤러마다 혹은 예외마다 서로 유연하게 스펙을 독립시키는 세밀한 처리가 매우 힘듭니다.

### @ExceptionHandler 등장

스프링은 이 모든 장벽을 제거하고 가장 간편하고 혁신적인 예외 처리 방식인 @ExceptionHandler 기능을 제공합니다. 이를 지원하는 핵심 처리기가 바로 최고의 우선순위를 자랑하는 ExceptionHandlerExceptionResolver입니다.

### @ExceptionHandler 기본 사용 형태

### 에러 공통 응답 전송용 DTO

```java
package hello.exception.exhandler;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class ErrorResult {
    private String code;
    private String message;
}
```

### ApiExceptionV2Controller (V2 버전 테스트 컨트롤러)

```java
package hello.exception.exhandler;

import hello.exception.exception.UserException;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
public class ApiExceptionV2Controller {

    // [1] IllegalArgumentException 발생 시 해당 에러 객체를 400 상태 코드로 응답
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ExceptionHandler(IllegalArgumentException.class)
    public ErrorResult illegalExHandle(IllegalArgumentException e) {
        log.error("[exceptionHandle] ex", e);
        return new ErrorResult("BAD", e.getMessage());
    }

    // [2] UserException 발생 시 ResponseEntity를 동적으로 빌드하여 400 상태 코드로 응답
    @ExceptionHandler
    public ResponseEntity<ErrorResult> userExHandle(UserException e) {
        log.error("[exceptionHandle] ex", e);
        ErrorResult errorResult = new ErrorResult("USER-EX", e.getMessage());
        return new ResponseEntity<>(errorResult, HttpStatus.BAD_REQUEST);
    }

    // [3] 상위 예외인 Exception.class를 설정해 타 리졸버에서 거르지 못한 서버 예외를 500 상태 코드로 일괄 캐치
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    @ExceptionHandler
    public ErrorResult exHandle(Exception e) {
        log.error("[exceptionHandle] ex", e);
        return new ErrorResult("EX", "내부 오류");
    }

    @GetMapping("/api2/members/{id}")
    public MemberDto getMember(@PathVariable("id") String id) {
        if (id.equals("ex")) {
            throw new RuntimeException("잘못된 사용자");
        }
        if (id.equals("bad")) {
            throw new IllegalArgumentException("잘못된 입력 값");
        }
        if (id.equals("user-ex")) {
            throw new UserException("사용자 오류");
        }
        return new MemberDto(id, "hello " + id);
    }

    @Data
    @AllArgsConstructor
    static class MemberDto {
        private String memberId;
        private String name;
    }
}
```

### @ExceptionHandler 상세 규칙 및 동작 순서

### 1. 대상 지정 및 우선순위 법칙

@ExceptionHandler(특정예외.class) 처럼 잡고 싶은 타겟 예외를 특정할 수 있습니다. 지정된 클래스 뿐만 아니라 그 자식 클래스들까지 같이 타겟팅됩니다.

만약 부모 예외 처리기와 자식 예외 처리기가 모두 존재하고 해당 자식 예외가 발생한다면, 스프링의 대원칙에 의해 더 자세히 세분화되어 작성된 자식 예외 처리기가 우선 호출됩니다.

@ExceptionHandler(부모예외.class) public String 부모예외처리(부모예외 e) {} @ExceptionHandler(자식예외.class) public String 자식예외처리(자식예외 e) {}

### 2. 다양한 다중 예외 처리

여러 예외를 묶어서 하나의 리졸버 메서드에서 처리하게 만들 수도 있습니다.

```text
@ExceptionHandler({AException.class, BException.class})
public String ex(Exception e) {
    log.info("exception e", e);
}
```

### 3. 예외명 생략 가능 규칙

@ExceptionHandler 애노테이션 괄호 안의 대상 예외 파라미터를 생략하면, 컨트롤러 메서드 매개변수에 선언되어 있는 파라미터 타입의 예외가 자동으로 지정됩니다.

```text
@ExceptionHandler // (UserException.class) 생략 가능
public ResponseEntity<ErrorResult> userExHandle(UserException e) {}
```

### @ExceptionHandler 예외 처리 실행 과정 상세

예시로 bad라는 파라미터 요청이 들어와 IllegalArgumentException이 던져진 경우의 실제 스프링 동작 흐름은 다음과 같습니다.

컨트롤러 메서드를 타며 던져진 IllegalArgumentException이 스프링 영역인 컨트롤러 밖으로 유출됩니다.

예외가 유출되었으므로 우선순위가 가장 높은 ExceptionHandlerExceptionResolver가 가로챕니다.

해당 컨트롤러 클래스 안에 IllegalArgumentException 또는 상위 부모 타입을 핸들링할 수 있는 @ExceptionHandler가 붙은 타겟 메서드가 정의되어 있는지 샅샅이 검색합니다.

검색 결과 illegalExHandle() 메서드를 탐색하여 실행시킵니다.

@RestController 내의 메서드이므로 반환 시 @ResponseBody가 자동으로 선언된 효과를 냅니다. 따라서 내부의 HTTP 메시지 컨버터가 이를 동작시켜 JSON 문자열 응답으로 완성해 냅니다.

타겟 메서드 위에 선언해 둔 @ResponseStatus(HttpStatus.BAD_REQUEST) 가 동작해 HTTP 응답 상태 코드가 400으로 클라이언트에 전달됩니다.

### 7. API 예외 처리 - @ControllerAdvice

### 도입 배경

정상적으로 요청을 받아 처리하는 비즈니스 비전 서비스 소스 코드와 예외 상황을 격리 수용하여 복구하는 로직이 하나의 컨트롤러 클래스에 한데 엉켜 섞여 유지 보수성을 악화시키는 단점을 개선하기 위해, 스프링은 예외 처리용 소스를 아예 외주 분리할 수 있는 도구를 제공합니다.

### ExControllerAdvice (글로벌 예외 처리 클래스 정의)

```java
package hello.exception.exhandler.advice;

import hello.exception.exception.UserException;
import hello.exception.exhandler.ErrorResult;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
public class ExControllerAdvice {

    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ExceptionHandler(IllegalArgumentException.class)
    public ErrorResult illegalExHandle(IllegalArgumentException e) {
        log.error("[exceptionHandle] ex", e);
        return new ErrorResult("BAD", e.getMessage());
    }

    @ExceptionHandler
    public ResponseEntity<ErrorResult> userExHandle(UserException e) {
        log.error("[exceptionHandle] ex", e);
        ErrorResult errorResult = new ErrorResult("USER-EX", e.getMessage());
        return new ResponseEntity<>(errorResult, HttpStatus.BAD_REQUEST);
    }

    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    @ExceptionHandler
    public ErrorResult exHandle(Exception e) {
        log.error("[exceptionHandle] ex", e);
        return new ErrorResult("EX", "내부 오류");
    }
}
```

### ApiExceptionV2Controller 최종 모습 (핵심 로직만 보존)

```java
package hello.exception.exhandler;

import hello.exception.exception.UserException;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
public class ApiExceptionV2Controller {

    @GetMapping("/api2/members/{id}")
    public MemberDto getMember(@PathVariable("id") String id) {
        if (id.equals("ex")) {
            throw new RuntimeException("잘못된 사용자");
        }
        if (id.equals("bad")) {
            throw new IllegalArgumentException("잘못된 입력 값");
        }
        if (id.equals("user-ex")) {
            throw new UserException("사용자 오류");
        }
        return new MemberDto(id, "hello " + id);
    }

    @Data
    @AllArgsConstructor
    static class MemberDto {
        private String memberId;
        private String name;
    }
}
```

비즈니스 로직과 복잡한 예외 대처 로직이 깔끔하게 물리적으로 100% 분리되었습니다.

### @ControllerAdvice / @RestControllerAdvice 속성 및 특징

@ControllerAdvice는 여러 대상 컨트롤러에 공통적으로 @ExceptionHandler 및 @InitBinder 기능을 위임하여 일괄 적용해 주는 편리한 서포팅 수단입니다.

@RestControllerAdvice는 @ControllerAdvice에 @ResponseBody 기능이 결합되어 추가된 형태입니다. (이는 @Controller와 @RestController와의 관계와 맥을 같이 합니다.)

어드바이스 클래스에 별도의 구체적인 대상을 명시하지 않으면, 프로젝트 내부 전체에 글로벌 영역으로 모든 컨트롤러에 예외 해결이 적용됩니다.

### 대표적인 대상 컨트롤러 지정 메커니즘 3가지 (공식 문서 패턴)

```java
// 1. 특정 애노테이션 타입 지정 (예: @RestController 마킹 클래스 대상)
@ControllerAdvice(annotations = RestController.class)
public class ExampleAdvice1 {}

// 2. 특정 패키지 포함 지정 (하위 모든 서브 패키지 컨트롤러 대상)
@ControllerAdvice("org.example.controllers")
public class ExampleAdvice2 {}

// 3. 인터페이스 상속 클래스 또는 특정 자바 타입 지정
@ControllerAdvice(assignableTypes = {ControllerInterface.class, AbstractController.class})
public class ExampleAdvice3 {}
```

### 8. 전체 요약 및 핵심정리

API 예외처리의 특성: HTML 화면 예외 처리는 일반 BasicErrorController에서 4xx/5xx 오류 템플릿을 통해 쉽게 처리되지만, API는 다양한 예외 상황에 부합하는 정교한 JSON 응답을 필요로 합니다.

ExceptionResolver의 가치: 컨트롤러 밖으로 유출된 예외를 WAS에 바로 보내지 않고, 가로채어 상태 코드를 변경하거나 정상적인 ModelAndView 객체 또는 JSON 데이터 응답 처리로 깔끔하게 마무리 해결하는 핵심 중개역입니다.

기본 리졸버 3종: 스프링은 상황별 에러 매핑을 위해 기본적으로 @ExceptionHandler용, @ResponseStatus용, 내부 프레임워크 예외(DefaultHandlerExceptionResolver)용 리졸버 체인을 제공합니다.

혁신적인 해결책: @ExceptionHandler 방식을 사용하여 컨트롤러 내에서 처리하고 싶은 예외를 자유롭게 지정해 우아하게 응답할 수 있으며, 더 나아가 @ControllerAdvice를 활용하면 예외 로직을 글로벌 공통 클래스로 완전히 독립시켜 코드 응집도와 설계 품질을 극대화할 수 있습니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 10. 스프링 타입 컨버터|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 10. 스프링 타입 컨버터]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
