---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "spring boot"]
category: "INFLEARN"
published: 2026-05-31
source_url: https://ch010104.tistory.com/280
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation

## 원문

https://ch010104.tistory.com/280

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

새로운 상품을 등록하거나 수정할 때, 올바르지 않은 값이 들어오면 검증 오류를 발생시켜야 합니다.

타입 검증: 가격(price), 수량(quantity) 필드에 문자가 입력될 경우 검증 오류 처리

## 원문 기반 학습 정리

### 1. 검증 요구사항 및 기본 개념

### 1) 상품 관리 시스템 검증 요구사항

새로운 상품을 등록하거나 수정할 때, 올바르지 않은 값이 들어오면 검증 오류를 발생시켜야 합니다.

타입 검증: 가격(price), 수량(quantity) 필드에 문자가 입력될 경우 검증 오류 처리

필드 검증:

상품명(itemName): 필수 값, 공백 금지(X)

가격(price): 1,000원 이상 1,000,000원 이하

수량(quantity): 최대 9,999개 이하

특정 필드의 범위를 넘어서는 검증 (복합 룰):

가격 * 수량의 합이 최소 10,000원 이상이어야 함

### 2) 클라이언트 검증 vs 서버 검증

웹 애플리케이션의 검증은 크게 두 가지 영역으로 나뉘며, 상호 보완적으로 사용되어야 합니다.

결론: 클라이언트 검증과 서버 검증을 적절히 섞어서 사용하되, 최종적으로 서버 검증은 필수입니다. 만약 API 방식을 사용한다면 API 스펙을 잘 정의하여 검증 오류를 API 응답 결과에 명확하게 남겨주어야 합니다.

### 2. 검증 직접 처리 (V1)

스프링이 제공하는 검증 기능을 사용하기 전에, 순수 자바 Map을 사용하여 직접 검증 로직을 구현하는 흐름을 살펴봅니다.

### 1) 아키텍처 흐름도

성공 흐름: GET /add (상품 등록 폼) → 사용자 입력 → POST /add (컨트롤러에서 검증 성공) → 상품 저장 → Redirect /items/{id} → GET /items/{id} (상품 상세 뷰)

실패 흐름: GET /add (상품 등록 폼) → 잘못된 사용자 입력 → POST /add (컨트롤러에서 검증 실패) → 오류 결과 수집 → Model에 errors 맵을 담고 addForm.html로 Forward (입력 데이터가 그대로 유지됨)

### 2) 컨트롤러 구현

검증 결과를 저장하기 위해 Map<String, String> errors를 사용하며, 필드명이나 특수 에러(globalError)를 Key로 메시지를 저장합니다.

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV1.java

```java
package hello.itemservice.web.validation;

import hello.itemservice.domain.item.Item;
import hello.itemservice.domain.item.ItemRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@Controller
@RequestMapping("/validation/v1/items")
@RequiredArgsConstructor
public class ValidationItemControllerV1 {

    private final ItemRepository itemRepository;

    @GetMapping
    public String items(Model model) {
        List<Item> items = itemRepository.findAll();
        model.addAttribute("items", items);
        return "validation/v1/items";
    }

    @GetMapping("/{itemId}")
    public String item(@PathVariable long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v1/item";
    }

    @GetMapping("/add")
    public String addForm(Model model) {
    // 검증이 실패했을 때도, 빈 Item을 넘겨서 이전의 model에 작성된 다른 속성 입력값들을 가져올 수 있음
        model.addAttribute("item", new Item());
        return "validation/v1/addForm";
    }

    @PostMapping("/add")
    public String addItem(@ModelAttribute Item item, RedirectAttributes redirectAttributes, Model model) {

        // 1. 검증 오류 결과를 보관할 Map 생성
        Map<String, String> errors = new HashMap<>();

        // 2. 개별 필드 검증 로직
        if (!StringUtils.hasText(item.getItemName())) {
            errors.put("itemName", "상품 이름은 필수입니다.");
        }

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            errors.put("price", "가격은 1,000~1,000,000 까지 허용합니다.");
        }

        if (item.getQuantity() == null || item.getQuantity() > 9999) {
            errors.put("quantity", "수량은 최대 9,999 까지 허용합니다.");
        }

        // 3. 복합 필드 검증 (특정 필드가 아닌 글로벌/복합 룰 검증)
        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                errors.put("globalError", "가격 * 수량의 합은 10,000원 이상이어야 합니다. 현재값 = " + resultPrice);
            }
        }

        // 4. 검증 실패 시 다시 입력 폼으로 이동 (Model에 errors를 담아 렌더링)
        if (!errors.isEmpty()) {
            model.addAttribute("errors", errors);
            return "validation/v1/addForm";
        }

        // 5. 성공 로직
        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v1/items/{itemId}";
    }
}
```

### 3) Thymeleaf 뷰 템플릿 구현

사용자가 무엇을 잘못 입력했는지 빨간색 글씨와 테두리로 강조하여 친절하게 안내합니다.

파일명: src/resources/templates/validation/v1/addForm.html

```text
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}" href="../css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            max-width: 560px;
        }
        /* 오류 강조용 CSS 클래스 추가 */
        .field-error {
            border-color: #dc3545;
            color: #dc3545;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="py-5 text-center">
        <h2>상품 등록</h2>
    </div>

    <form action="item.html" th:action th:object="${item}" method="post">

        <!-- 글로벌 오류 메시지 출력 -->
        <div th:if="${errors?.containsKey('globalError')}">
            <p class="field-error" th:text="${errors['globalError']}">전체 오류 메시지</p>
        </div>

        <!-- 상품명 필드 오류 처리 -->
        <div>
            <label for="itemName">상품명</label>
            <input type="text" id="itemName" th:field="*{itemName}"
                   th:class="${errors?.containsKey('itemName')} ? 'form-control field-error' : 'form-control'"
                   placeholder="이름을 입력하세요">
            <div class="field-error" th:if="${errors?.containsKey('itemName')}"
                 th:text="${errors['itemName']}">
                상품명 오류
            </div>
        </div>

        <!-- 가격 필드 오류 처리 -->
        <div>
            <label for="price">가격</label>
            <input type="text" id="price" th:field="*{price}"
                   th:class="${errors?.containsKey('price')} ? 'form-control field-error' : 'form-control'"
                   placeholder="가격을 입력하세요">
            <div class="field-error" th:if="${errors?.containsKey('price')}"
                 th:text="${errors['price']}">
                가격 오류
            </div>
        </div>

        <!-- 수량 필드 오류 처리 -->
        <div>
            <label for="quantity">수량</label>
            <input type="text" id="quantity" th:field="*{quantity}"
                   th:class="${errors?.containsKey('quantity')} ? 'form-control field-error' : 'form-control'"
                   placeholder="수량을 입력하세요">
            <div class="field-error" th:if="${errors?.containsKey('quantity')}"
                 th:text="${errors['quantity']}">
                수량 오류
            </div>
        </div>

        <hr class="my-4">

        <div class="row">
            <div class="col">
                <button class="w-100 btn btn-primary btn-lg" type="submit">저장</button>
            </div>
            <div class="col">
                <button class="w-100 btn btn-secondary btn-lg"
                        onclick="location.href='items.html'"
                        th:onclick="|location.href='@{/validation/v1/items}'|"
                        type="button">취소</button>
            </div>
        </div>
    </form>
</div>
</body>
</html>
```

### 참고: Safe Navigation Operator (errors?.)

최초로 상품 등록 폼(GET /add)에 접속할 때는 검증 에러가 전혀 없기 때문에 Model에 errors 맵이 담기지 않아 null 상태입니다.

만약 단순 errors.containsKey('globalError')를 호출하면 NullPointerException이 발생하여 애플리케이션이 먹통이 됩니다.

errors?.containsKey(...) 문법은 errors가 null인 경우 NullPointerException을 던지는 대신 null을 반환하는 SpringEL의 유용한 기능입니다. Thymeleaf의 th:if 문에서 null은 false로 처리되므로 아무런 오류 메시지도 출력되지 않고 화면이 무사히 로드됩니다.

### 4) V1 직접 구현 방식의 남은 문제점

뷰 템플릿 내의 심한 중복: 각각의 인풋 태그와 오류 메시지 박스마다 삼항 연산자와 조건문(th:if, th:class)이 매우 유사한 패턴으로 반복해서 나타납니다.

타입 바인딩 오류 대처 불가: 가격(price)과 수량(quantity)은 자바 도메인에서 Integer 타입입니다. 사용자가 입력 창에 문자 "A"를 입력할 경우, 컨트롤러에 도달하기 전 스프링 바인딩 단계에서 오류가 터져 400 Bad Request 예외 페이지가 노출됩니다.

고객 입력 데이터의 유실: 타입 바인딩 오류가 발생하면 자바 내부 객체 변환에 실패하여 사용자가 타이핑했던 잘못된 값(예: 문자 "A")을 뷰 템플릿에 되돌려 유지할 수 없어 입력 내용이 다 사라집니다.

### 3. BindingResult 도입 (V2)

스프링 프레임워크가 제공하는 핵심 검증 조력자인 BindingResult를 적용하여 V1의 구조적인 단점을 완벽하게 보완합니다.

### 1) BindingResult의 핵심 개념과 특징

BindingResult는 검증 오류를 보관하는 스프링 제공 인터페이스로, 반드시 검증할 대상 객체(예: @ModelAttribute Item item)의 바로 다음에 위치해야 합니다.

BindingResult가 파라미터에 존재하면, @ModelAttribute 데이터 바인딩 시 오류가 발생해도 컨트롤러가 즉각 끊기지 않고 정상 호출됩니다!

BindingResult가 없을 때: 타입 mismatch 발생 $\rightarrow$ 400 Bad Request 에러 페이지 노출.

BindingResult가 있을 때: 타입 mismatch 발생 $\rightarrow$ 스프링이 오류 정보(FieldError)를 직접 생성하여 BindingResult에 고이 접어 넣은 다음 컨트롤러를 호출함.

### 2) BindingResult1 - 기본 사용 방식 (addItemV1)

필드 에러는 FieldError 객체를 생성하고, 글로벌(복합) 에러는 ObjectError 객체를 생성하여 BindingResult에 적립합니다.

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```java
package hello.itemservice.web.validation;

import hello.itemservice.domain.item.Item;
import hello.itemservice.domain.item.ItemRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Slf4j
@Controller
@RequestMapping("/validation/v2/items")
@RequiredArgsConstructor
public class ValidationItemControllerV2 {

    private final ItemRepository itemRepository;

    @GetMapping
    public String items(Model model) {
        List<Item> items = itemRepository.findAll();
        model.addAttribute("items", items);
        return "validation/v2/items";
    }

    @GetMapping("/{itemId}")
    public String item(@PathVariable long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v2/item";
    }

    @GetMapping("/add")
    public String addForm(Model model) {
        model.addAttribute("item", new Item()); // 검증이 실패했을 때도, 빈 Item을 넘겨서 이전의 model에 작성된 다른 속성 입력값들을 가져올 수 있음
        return "validation/v2/addForm";
    }

    @PostMapping("/add")
    public String addItemV1(@ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes, Model model) {
        // BindingResult는 ModelAttribute인 Item 객체의 바인딩 결과를 담고 있기 때문에, 무조건 @ModelAttribute Item item의 뒤에 와야함

        // 검증 오류 결과를 보관
        // Map<String, String> errors = new HashMap<>();
        // 이제 BlindinfResult가 기존 errors의 역할을 해줌

        // 검증 로직
        if (!StringUtils.hasText(item.getItemName())) {
            // errors.put("itemName", "상품 이름은 필수입니다.");
            bindingResult.addError(new FieldError("item", "itemName", "상품 이름은 필수입니다."));
        }

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            // errors.put("price", "가격은 1,000 ~ 1,000,000 까지 허용합니다.");
            bindingResult.addError(new FieldError("item", "price", "가격은 1,000 ~ 1,000,000 까지 허용합니다."));
        }

        if (item.getQuantity() == null || item.getQuantity() > 9999) {
            // errors.put("quantity", "수량은 최대 9,999 까지 허용합니다.");
            bindingResult.addError(new FieldError("item", "quantity", "수량은 최대 9,999 까지 허용합니다."));
        }

        // 특정 필드가 아닌 복합 룰 검증
        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                // errors.put("globalError", "가격 * 수량의 합은 10,000원 이상이어야 합니다. 현재 값 = " + resultPrice);
                // new ObjectError()로 만들면, GlobalErrors로 등록됨
                bindingResult.addError(new ObjectError("item", "가격 * 수량의 합은 10,000원 이상이어야 합니다. 현재 값 = " + resultPrice));
            }
        }

        // 검증에 실패하면 다시 입력 폼으로
//        if (!errors.isEmpty()) {
//            log.info("errors: {}", errors);
//            model.addAttribute("errors", errors);
//            return "validation/v2/addForm";
//        }
        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            // bindingResult는 자동으로 view에 같이 넘어가기 때문에, model.addAttribute에 안 담아도 됨
            return "validation/v2/addForm";
        }

        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }

    @GetMapping("/{itemId}/edit")
    public String editForm(@PathVariable Long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v2/editForm";
    }

    @PostMapping("/{itemId}/edit")
    public String edit(@PathVariable Long itemId, @ModelAttribute Item item) {
        itemRepository.update(itemId, item);
        return "redirect:/validation/v2/items/{itemId}";
    }

}
```

### 3) Thymeleaf의 BindingResult 통합 연동

Thymeleaf는 스프링의 BindingResult를 깊이 결합하여 검증 오류를 우아하게 표현하는 다양한 전용 기능들을 탑재하고 있습니다.

#fields: #fields를 사용하여 BindingResult 내부의 전체/개별 에러에 직접 접근합니다.

th:errors: 지정한 필드 경로에 오류가 담겨 있다면, 태그를 조건부로 출력해주고 내부의 가짜 텍스트를 실제 오류 메시지로 변환해 줍니다 (th:if 가 필요 없도록 단축한 것).

th:errorclass: th:field로 연계된 필드 경로에 검증 오류가 실재할 경우, 기존 클래스 옆에 특정한 CSS 클래스(예: field-error)를 알아서 붙여줍니다.

파일명: src/resources/templates/validation/v2/addForm.html

```text
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <link th:href="@{/css/bootstrap.min.css}"
          href="../css/bootstrap.min.css" rel="stylesheet">
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
        <h2 th:text="#{page.addItem}">상품 등록</h2>
    </div>

    <form action="item.html" th:action th:object="${item}" method="post">
        <!-- GlobalErrors의 경우, 오류가 여러개일 수 있기 때문에, th:errors 대신, 전체 GlobalErrors를 받아와서 th:each로 반복문으로 출력해야함-->
        <div th:if="${#fields.hasGlobalErrors()}">
            <p class="field-error" th:each="err : ${#fields.globalErrors()}" th:text="${err}">전체 오류 메시지</p>
        </div>

        <div>
            <label for="itemName" th:text="#{label.item.itemName}">상품명</label>
            <input type="text" id="itemName" th:field="*{itemName}" th:errorclass="field-error" class="form-control" placeholder="이름을 입력하세요">
            <!-- th:errors="*{itemName}" 안에 th:if="${#fields.hasErrors('itemName')}" 의 확인 로직이 포함되어 있음 -->
            <div class="field-error" th:errors="*{itemName}">
                상품명 오류
            </div>
        </div>
        <div>
            <label for="price" th:text="#{label.item.price}">가격</label>
            <input type="text" id="price" th:field="*{price}" th:errorclass="field-error" class="form-control" placeholder="가격을 입력하세요">
            <div class="field-error" th:errors="*{price}">
                가격 오류
            </div>
        </div>
        <div>
            <label for="quantity" th:text="#{label.item.quantity}">수량</label>
            <input type="text" id="quantity" th:field="*{quantity}" th:errorclass="field-error" class="form-control" placeholder="수량을 입력하세요">
            <div class="field-error" th:errors="*{quantity}">
                수량 오류
            </div>
        </div>

        <hr class="my-4">

        <div class="row">
            <div class="col">
                <button class="w-100 btn btn-primary btn-lg" type="submit" th:text="#{button.save}">저장</button>
            </div>
            <div class="col">
                <button class="w-100 btn btn-secondary btn-lg"
                        onclick="location.href='items.html'"
                        th:onclick="|location.href='@{/validation/v2/items}'|"
                        type="button" th:text="#{button.cancel}">취소</button>
            </div>
        </div>

    </form>

</div> <!-- /container -->
</body>
</html>
```

### 참고: BindingResult와 Errors의 상속 구조

org.springframework.validation.Errors는 최상위 인터페이스이고 단순 오류 기록/조회용입니다.

org.springframework.validation.BindingResult는 Errors 인터페이스를 확장한 인터페이스로, 실제 구현 시 훨씬 더 다양한 기능과 유틸리티 메서드(addError 등)를 탑재하고 있습니다.

관례상 더 강력한 BindingResult를 실무 매개변수로 사용합니다. (구현체로는 BeanPropertyBindingResult가 투입됩니다.)

### BindingResult

스프링이 제공하는 검증 오류를 보관하는 객체이다. 검증 오류가 발생하면 여기에 보관하면 된다.

BindingResult가 있으면 @ModelAttribute에 데이터 바인딩 시 오류가 발생해도 컨트롤러가 호출된다

### 예) @ModelAttribute에 바인딩 시 타입 오류가 발생하면?

BindingResult가 없으면 400 오류가 발생하면서 컨트롤러가 호출되지 않고, 오류 페이지로 이동한다. BindingResult가 있으면 오류 정보(FieldError)를 BindingResult에 담아서 컨트롤러를 정상 호출한다.

### BindingResult에 검증 오류를 적용하는 3가지 방법

@ModelAttribute에 담아서 컨트롤러를 정상 호 의 객체에 타입 오류 등으로 바인딩이 실패하는 경우 스프링이 BindingResult에 넣어준다.

개발자가 직접 넣어준다.

Validator사용

### 4. 사용자 입력 값 유지 (FieldError, ObjectError)

BindingResult에 에러를 담더라도 addItemV1 버전은 에러가 나면 사용자의 과거 입력값이 날아가 버리는 부작용이 있습니다. 이를 해결하려면 FieldError, ObjectError가 가지고 있는 더 상세한 파라미터 생성자를 호출해야 합니다.

### 1) FieldError & ObjectError의 생성자 심층 분석

```text
// FieldError 생성자 시그니처 1
public FieldError(String objectName, String field, String defaultMessage);

// FieldError 생성자 시그니처 2 (입력 보존 및 메시지 다국화 가능)
public FieldError(String objectName, String field, @Nullable Object rejectedValue,
                  boolean bindingFailure, @Nullable String[] codes,
                  @Nullable Object[] arguments, @Nullable String defaultMessage);
```

### 파라미터별 특징

objectName: 오류가 발생한 Model 대상 객체의 이름 (예: "item")

field: 오류가 터진 구체적 필드명 (예: "price")

rejectedValue: 사용자가 입력하려다가 거부당한 원래의 입력 데이터 (보존 데이터의 핵심)

bindingFailure: 단순 검증(비즈니스 룰) 실패인지(false), 타입 변환 바인딩 단계 자체가 실패했는지(true) 구분하는 플래그

codes: 에러 메시지 번들에서 순차적으로 매칭해 찾아낼 오류 메시지 키 배열 (추후 메시지 자동화에 사용)

arguments: 에러 메시지에 인자로 주입할 외부 값 객체 배열 (예: {1000, 1000000})

defaultMessage: 혹시라도 메시지 코드 매칭에 대실패했을 때 백업으로 출력해줄 기본 고정 메시지

### 2) 입력 값 보존 구현 방식 (addItemV2)

컨트롤러에 진입하기도 전에 문자가 숫자로 변환되지 않아 깨진 바인딩 오류 값들도, 스프링이 알아서 원래 글자 그대로 보관해 줍니다.

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```text
// addItemV1 대체 버전
    @PostMapping("/add")
    public String addItemV3(@ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes, Model model) {
        // BindingResult는 ModelAttribute인 Item 객체의 바인딩 결과를 담고 있기 때문에, 무조건 @ModelAttribute Item item의 뒤에 와야함

        // 검증 오류 결과를 보관
        // Map<String, String> errors = new HashMap<>();
        // 이제 BlindinfResult가 기존 errors의 역할을 해줌

        // 검증 로직
        if (!StringUtils.hasText(item.getItemName())) {
            // errors.put("itemName", "상품 이름은 필수입니다.");
            // bindingResult.addError(new FieldError("item", "itemName", "상품 이름은 필수입니다."));
            // 사용자가 입력한 값을 3번째 파라미터인 item.getItemName()처럼 보존해서, 잘못 입력했을 시에도 사라지지 않고 보존되게 함(필드가 맞지 않은 입력값도 보존함)
            // 5번쨰 파라미터인 code에서 error.properties 파일의 코드를 불러옴. 이게 없으면 default 사용
            // new String 배열로 사용하는 이유는, 첫번째 인덱스의 값이 없으면(선언이 안되어 있으면), 다음 인덱스의 값을 사용
            bindingResult.addError(new FieldError("item", "itemName", item.getItemName(), false, new String[]{"required.item.itemName"}, null, "default 오류 메시지"));
        }

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            // errors.put("price", "가격은 1,000 ~ 1,000,000 까지 허용합니다.");
            // bindingResult.addError(new FieldError("item", "price", "가격은 1,000 ~ 1,000,000 까지 허용합니다."));
            bindingResult.addError(new FieldError("item", "price", item.getPrice(), false, new String[]{"range.item.price"}, new Object[]{1000, 1000000}, "default 오류 메시지"));
        }

        if (item.getQuantity() == null || item.getQuantity() > 9999) {
            // errors.put("quantity", "수량은 최대 9,999 까지 허용합니다.");
            // bindingResult.addError(new FieldError("item", "quantity", "수량은 최대 9,999 까지 허용합니다."));
            bindingResult.addError(new FieldError("item", "quantity", item.getQuantity(), false, new String[]{"max.item.quantity"}, new Object[]{9999}, "default 오류 메시지"));
        }

        // 특정 필드가 아닌 복합 룰 검증
        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                // errors.put("globalError", "가격 * 수량의 합은 10,000원 이상이어야 합니다. 현재 값 = " + resultPrice);
                // new ObjectError()로 만들면, GlobalErrors로 등록됨
                bindingResult.addError(new ObjectError("item", new String[]{"totalPriceMin"}, new Object[]{10000, resultPrice}, "default 오류 메시지"));
            }
        }

        // 검증에 실패하면 다시 입력 폼으로
//        if (!errors.isEmpty()) {
//            log.info("errors: {}", errors);
//            model.addAttribute("errors", errors);
//            return "validation/v2/addForm";
//        }
        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            // bindingResult는 자동으로 view에 같이 넘어가기 때문에, model.addAttribute에 안 담아도 됨
            return "validation/v2/addForm";
        }

        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 타임리프의 보존 원리

정상 상황일 때는 th:field="*{price}"가 Model 객체 내부의 실제 price 필드 숫자 값을 출력합니다.

에러 발생 상황(오류 필드 존재)일 때는 컨트롤러에서 model에 담은 본래의 바인딩 데이터 대신, BindingResult가 고이 품고 있는 FieldError의 rejectedValue를 꺼내어 화면에 영리하게 찍어줍니다.

### 5. 오류 코드와 메시지 처리

자바 코드 안에서 하드코딩 형태로 문자열 에러 메시지("가격을 잘못 입력했습니다.")를 들고 있으면 국제화 및 문장 보수가 매우 힘들어집니다. 오류 코드를 체계적으로 외부 자원으로 격리하여 중앙 제어식으로 관리합니다.

### 1) 설정 추가 및 메시지 파일 생성

### 스프링 부트 설정 추가

스프링 부트가 우리가 새로 분리하여 작성할 에러 전용 메시지 파일(errors.properties)을 인지할 수 있게 경로를 매핑해 줍니다.

파일명: src/main/resources/application.properties

```text
spring.messages.basename=messages, errors
```

### 에러 메시지 프로퍼티 정의

파일명: src/main/resources/errors.properties

```text
required.item.itemName=상품 이름은 필수입니다.
range.item.price=가격은 {0} ~ {1} 까지 허용합니다.
max.item.quantity=수량은 최대 {0} 까지 허용합니다.
totalPriceMin=가격 * 수량의 합은 {0}원 이상이어야 합니다. 현재 값 = {1}
```

### 2) 메시지 코드를 적용한 자바 구현 (addItemV3)

FieldError의 codes 매개변수에 우리가 프로퍼티 파일에 적어둔 키 값을 배열로 던져 연동합니다.

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```text
// addItemV2 대체 버전 (메시지 연동 버전)
    @PostMapping("/add")
    public String addItemV3(@ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        if (!StringUtils.hasText(item.getItemName())) {
            bindingResult.addError(new FieldError("item", "itemName",
                    item.getItemName(), false, new String[]{"required.item.itemName"}, null, null));
        }

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            bindingResult.addError(new FieldError("item", "price",
                    item.getPrice(), false, new String[]{"range.item.price"}, new Object[]{1000, 1000000}, null));
        }

        if (item.getQuantity() == null || item.getQuantity() > 10000) {
            bindingResult.addError(new FieldError("item", "quantity",
                    item.getQuantity(), false, new String[]{"max.item.quantity"}, new Object[]{9999}, null));
        }

        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                bindingResult.addError(new ObjectError("item",
                        new String[]{"totalPriceMin"}, new Object[]{10000, resultPrice}, null));
            }
        }

        if (bindingResult.hasErrors()) {
            return "validation/v2/addForm";
        }

        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 3) 혁신: rejectValue() 및 reject()의 등장 (addItemV4)

매번 기나긴 FieldError, ObjectError 생성자를 명시하는 작업은 코드가 지저분해지고 번거롭습니다. BindingResult가 본인의 검증 타겟 객체(target인 item)를 이미 알고 있다는 특징을 백분 활용하여 비약적으로 코드를 줄여줍니다.

```text
// rejectValue() 메서드 원형
void rejectValue(@Nullable String field, String errorCode,
                 @Nullable Object[] errorArgs, @Nullable String defaultMessage);
```

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```text
// addItemV3 대체 버전 (rejectValue 단축형 버전)
    @PostMapping("/add")
    public String addItemV4(@ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        // 로그를 찍어보면 타겟 객체의 정보를 BindingResult가 이미 꽉 쥐고 있음을 확인 가능
        log.info("objectName={}", bindingResult.getObjectName()); // 결과: item
        log.info("target={}", bindingResult.getTarget()); // 결과: Item(...)

        if (!StringUtils.hasText(item.getItemName())) {
            bindingResult.rejectValue("itemName", "required");
        }

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            bindingResult.rejectValue("price", "range", new Object[]{1000, 1000000}, null);
        }

        if (item.getQuantity() == null || item.getQuantity() > 10000) {
            bindingResult.rejectValue("quantity", "max", new Object[]{9999}, null);
        }

        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                // 특정 필드가 없는 글로벌 에러는 reject() 사용
                bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }

        if (bindingResult.hasErrors()) {
            return "validation/v2/addForm";
        }

        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

의문점: 분명 errors.properties에는 range.item.price 또는 required.item.itemName 등의 풀-네임 메시지 키를 정의했습니다. 하지만 컨트롤러 내에서 축약형인 "required", "range"만 적었을 뿐인데도 스프링은 어떻게 풀-네임 메시지를 정확하게 찾아서 화면에 보여주는 걸까요? 그 핵심 비밀은 **MessageCodesResolver**에 있습니다.

### 4) 핵심 원리: MessageCodesResolver

MessageCodesResolver는 우리가 전달한 단순 축약 에러 코드(예: "required")와 에러가 발생한 구체적인 도메인 객체명, 필드명, 그리고 필드 데이터의 타입을 유기적으로 결합하여 순서가 명확하게 정렬된 다수의 상세 메시지 후보군 코드를 즉각 자동 매칭해 주는 비밀 해결사 인터페이스입니다.

### 테스트 코드를 통한 검증 코드 분석

파일명: src/test/java/hello/itemservice/validation/MessageCodesResolverTest.java

```java
package hello.itemservice.validation;

import org.junit.jupiter.api.Test;
import org.springframework.validation.DefaultMessageCodesResolver;
import org.springframework.validation.MessageCodesResolver;

import static org.assertj.core.api.Assertions.assertThat;

public class MessageCodesResolverTest {

    MessageCodesResolver codesResolver = new DefaultMessageCodesResolver();

    @Test
    void messageCodesResolverObject() {
        // 객체 전체 에러일 때 메시지 후보코드 생성
        String[] messageCodes = codesResolver.resolveMessageCodes("required", "item");
        assertThat(messageCodes).containsExactly("required.item", "required");
    }

    @Test
    void messageCodesResolverField() {
        // 특정 필드 에러일 때 세밀한 후보코드들 순차 자동 생성
        String[] messageCodes = codesResolver.resolveMessageCodes("required", "item", "itemName", String.class);

        assertThat(messageCodes).containsExactly(
                "required.item.itemName",  // 1순위: 가장 구체적
                "required.itemName",       // 2순위: 덜 구체적
                "required.java.lang.String",// 3순위: 타입 매칭
                "required"                 // 4순위: 범용적인 최상위 코드
        );
    }
}
```

### DefaultMessageCodesResolver의 생성 규칙 상세

객체 에러 (ObjectError)

1순위: 에러코드 + "." + 객체명

2순위: 에러코드

예시: resolveMessageCodes("required", "item") → ["required.item", "required"]

필드 에러 (FieldError)

1순위: 에러코드 + "." + 객체명 + "." + 필드명

2순위: 에러코드 + "." + 필드명

3순위: 에러코드 + "." + 필드 타입

4순위: 에러코드

예시: resolveMessageCodes("typeMismatch", "user", "age", int.class) → ["typeMismatch.user.age", "typeMismatch.age", "typeMismatch.int", "typeMismatch"]

### 실제 컨트롤러 호출 후 로그 분석

bindingResult.rejectValue("itemName", "required") 호출 시, BindingResult가 가지고 있는 FieldError 내부의 codes 배열 필드에는 다음과 같은 4가지 상세 키가 차곡차곡 적립됩니다.

codes [required.item.itemName, required.itemName, required.java.lang.String, required]

Thymeleaf 뷰 단에서 th:errors가 실행되면, 이 codes 배열의 1순위 원소부터 4순위 원소까지 순차적으로 errors.properties에서 에치해 보다가 가장 먼저 발견되는 메시지를 골라서 출력합니다.

### 5) 효과적인 오류 코드 계층 관리 전략

모든 자잘한 검증 에러 코드마다 개별 메시지를 일일이 기입하는 행위는 재앙에 가깝습니다. 평범하고 덜 중요한 메시지는 Level4처럼 아주 넓은 범용의 디폴트 성격 메시지로 커버하고, 정말 정교함이 요구되는 핵심 필드는 Level1 수준의 세부적인 개별 매핑 코드를 투입하는 계층형 수립 전략을 취합니다.

파일명: src/resources/errors.properties

```text
# ==========================================================
# ObjectError (복합/글로벌 룰 에러)
# ==========================================================
# Level 1 (구체적)
totalPriceMin.item=상품의 가격 * 수량의 합은 {0}원 이상이어야 합니다. 현재 값 = {1}

# Level 2 (범용)
totalPriceMin=전체 가격은 {0}원 이상이어야 합니다. 현재 값 = {1}

# ==========================================================
# FieldError (필드 에러)
# ==========================================================
# Level 1 (가장 구체적)
required.item.itemName=상품 이름은 필수입니다.
range.item.price=가격은 {0} ~ {1} 까지 허용합니다.
max.item.quantity=수량은 최대 {0} 까지 허용합니다.

# Level 2 (생략 가능)

# Level 3 (데이터 바인딩 오류 대비용 타입 매칭)
required.java.lang.String=필수 문자입니다.
required.java.lang.Integer=필수 숫자입니다.
min.java.lang.String={0} 이상의 문자를 입력해주세요.
min.java.lang.Integer={0} 이상의 숫자를 입력해주세요.
range.java.lang.String={0} ~ {1} 까지의 문자를 입력해주세요.
range.java.lang.Integer={0} ~ {1} 까지의 숫자를 입력해주세요.
max.java.lang.String={0} 까지의 문자를 허용합니다.
max.java.lang.Integer={0} 까지의 숫자를 허용합니다.

# Level 4 (최하단 범용 - 최종 백업 디폴트 메시지)
required=필수 값 입니다.
min={0} 이상이어야 합니다.
range={0} ~ {1} 범위를 허용합니다.
max={0} 까지 허용합니다.
```

이렇게 구성해두면, Level 1을 모두 주석처리해도 Level 4에서 정의된 "필수 값 입니다." 등의 범용 메시지가 최후의 보루로서 알아서 매칭되어 나갑니다.

### 6) ValidationUtils 편의 제공 클래스

자주 사용되는 null 체크 및 공백("" 혹은 " ") 여부 체크 단계를 간결하게 한 줄로 줄여줍니다.

```text
// ValidationUtils 적용 전
if (!StringUtils.hasText(item.getItemName())) {
    bindingResult.rejectValue("itemName", "required", "기본: 상품 이름은 필수입니다.");
}

// ValidationUtils 적용 후 (위 세 줄의 문장과 완벽히 동치)
ValidationUtils.rejectIfEmptyOrWhitespace(bindingResult, "itemName", "required");
```

### 7) 스프링이 내부적으로 자동 발생시키는 타입 에러 대응

우리가 직접 비즈니스 로직에서 검증해 낸 에러가 아닌, 스프링 프레임워크가 바인딩 단계에서 숫자가 필요한 Integer 타입 필드에 사용자가 문자 "A"를 집어넣는 등의 비정상 입력을 받았을 경우를 상상해 봅시다.

이때 스프링은 개발자의 손을 타기 전에 내부적으로 typeMismatch라는 에러 코드를 가지고 스스로 BindingResult에 FieldError를 적재시킵니다.

MessageCodesResolver를 거쳐 codes 배열 필드에 적재되는 키는 다음과 같이 4가지입니다:

typeMismatch.item.price

typeMismatch.price

typeMismatch.java.lang.Integer

typeMismatch

우리는 자바 소스코드를 한 줄도 만지지 않고, 오직 프로퍼티 파일 수정만을 통하여 지저분하게 표출되던 스프링 디폴트 영문 에러 메시지(Failed to convert property value...)를 한국어 전용의 예쁜 에러 문구로 완벽하게 덮어쓸 수 있습니다.

파일명: src/resources/errors.properties에 아래 구문을 한 줄 추가합니다.

```text
# 스프링 자체 타입 오류 커스텀 매핑 추가
typeMismatch.java.lang.Integer=숫자를 입력해주세요.
typeMismatch=타입 오류입니다.
```

### 6. Validator의 분리 및 검증의 자동화

컨트롤러에서 검증 로직이 차지하는 부피는 매우 막대하므로, 별도의 전담 검증 클래스(Validator)로 책임을 깔끔하게 떼어내야 유지보수가 수월하고 차후 동일한 규칙을 재활용할 수도 있습니다.

### 1) 스프링 제공 Validator 인터페이스 구조

```java
package org.springframework.validation;

public interface Validator {
    // 1. 해당 검증기 클래스가 인자로 넘어온 클래스 타입을 검증할 능력이 있는지 판단
    boolean supports(Class<?> clazz);

    // 2. 본격적인 검증 수행 및 오류 결과를 Errors(BindingResult의 상위 클래스)에 적립
    void validate(Object target, Errors errors);
}
```

### 2) ItemValidator 구현

Validator 인터페이스를 구현하고 비즈니스 검증 로직을 전부 통으로 옮겨옵니다.

파일명: src/main/java/hello/itemservice/web/validation/ItemValidator.java

```java
package hello.itemservice.web.validation;

import hello.itemservice.domain.item.Item;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

@Component // 스프링 빈 등록 필수
public class ItemValidator implements Validator {

    @Override
    public boolean supports(Class<?> clazz) {
        // Item 클래스가 지원 대상인지, 하위 자식 타입까지 안전하게 검사하는 assignable 사용 권장
        return Item.class.isAssignableFrom(clazz);
    }

    @Override
    public void validate(Object target, Errors errors) {
        Item item = (Item) target; // 대상을 구체 캐스트하여 작업 시작

        ValidationUtils.rejectIfEmptyOrWhitespace(errors, "itemName", "required");

        if (item.getPrice() == null || item.getPrice() < 1000 || item.getPrice() > 1000000) {
            errors.rejectValue("price", "range", new Object[]{1000, 1000000}, null);
        }

        if (item.getQuantity() == null || item.getQuantity() > 10000) {
            errors.rejectValue("quantity", "max", new Object[]{9999}, null);
        }

        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                errors.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }
    }
}
```

### 3) ItemValidator의 수동 직접 호출 처리 (addItemV5)

스프링 빈으로 직접 주입받은 검증기 객체의 validate()를 파라미터로 명시 호출합니다.

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```text
private final ItemValidator itemValidator; // 생성자 빈 자동 주입

    // addItemV4 대체 버전 (Validator 수동 호출 버전)
    @PostMapping("/add")
    public String addItemV5(@ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        // 직접 검증 로직을 타겟(item)과 바인딩결과(bindingResult)를 넘겨 처리
        itemValidator.validate(item, bindingResult);

        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v2/addForm";
        }

        // 성공 로직
        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 4) WebDataBinder 및 @Validated 애노테이션을 활용한 자동화 (addItemV6)

더욱 진보한 기술을 통해 자바 단에서 우리가 직접 검증기 클래스 인스턴스를 불러와 validate를 쳐대던 한 줄 마저 지워버릴 수 있습니다. 검증 대상을 가리켜 @Validated를 명시하기만 하면 됩니다.

### @InitBinder 적용

컨트롤러 내부의 WebDataBinder에 해당 전담 검증기(itemValidator)를 추가해 줍니다. @InitBinder는 선언된 해당 컨트롤러 클래스 인스턴스 전용 바인더로 한정해서만 발동하여 스코프를 제한합니다.

```text
@InitBinder
    public void init(WebDataBinder dataBinder) {
        log.info("init binder {}", dataBinder);
        dataBinder.addValidators(itemValidator);
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### @Validated 적용한 최종 자동화 메서드

파일명: src/main/java/hello/itemservice/web/validation/ValidationItemControllerV2.java

```text
// addItemV5 대체 최종 버전 (@Validated 적용 검증 무인화 자동 처리)
    @PostMapping("/add")
    public String addItemV6(@Validated @ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        // [특징]: 자바 개발자가 직접 호출하던 검증기 실행 코드가 한 줄도 없습니다!
        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v2/addForm";
        }

        // 성공 로직
        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v2/items/{itemId}";
    }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 무인 작동 원리 및 흐름

매개변수 선두에 달린 @Validated 애노테이션을 감지한 스프링 프레임워크가 해당 메서드 호출 직전, 우리가 등록한 WebDataBinder 내부를 뒤져서 사용 가능한 모든 Validator 목록을 스캔합니다.

각각의 Validator들이 구현해 둔 supports(Item.class)를 번갈아 돌려보며, 어떤 검증기가 타겟 클래스를 담당할 수 있는지 체크합니다.

여기서는 우리가 등록해 둔 ItemValidator 클래스의 supports()가 true를 뱉으므로, 최종 매칭되어 내부의 validate(item, bindingResult)가 우리 몰래 자동으로 기폭되어 모든 에러들을 BindingResult에 파종합니다.

### 5) 글로벌 설정법 (모든 컨트롤러 적용)

특정 컨트롤러에서 매번 바인더 설정을 선언하는 과정조차 생략하고, 스프링부트 메인 클래스 등에 연계 설정하여 전체 영역에 글로벌 검증 시스템을 전격 적용할 수도 있습니다.

파일명: src/main/java/hello/itemservice/ItemServiceApplication.java (메인 애플리케이션 파일 예시)

```java
package hello.itemservice;

import hello.itemservice.web.validation.ItemValidator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.validation.Validator;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class ItemServiceApplication implements WebMvcConfigurer {

    public static void main(String[] args) {
        SpringApplication.run(ItemServiceApplication.class, args);
    }

    // 글로벌 검증기를 반환하도록 WebMvcConfigurer 인터페이스 메서드 오버라이드 구현
    @Override
    public Validator getValidator() {
        return new ItemValidator();
    }
}
```

매우 중요한 경고: 이렇게 글로벌 설정을 수동으로 등록해두면, 차후 스프링 부트에서 절대적으로 사용하는 어마어마한 전용 검증 어노테이션 기반 기능인 BeanValidator (Hibernate Validator)가 수동 오버라이드에 덮어씌워져 자동 등록되지 않는 심각한 부작용을 야기합니다. 실무에서 글로벌 검증 설정을 직접 설계하여 사용하는 사례는 매우 희귀합니다. 반드시 테스트 목적이 종료되면 글로벌 설정은 다시 주석화하거나 조심스럽게 사용해야 합니다.

### 참고: @Valid vs @Validated

javax.validation.@Valid: 자바 표준 스펙(JSR-303 / Jakarta)에 정의된 표준 검증 애노테이션입니다. 이를 활성화해 사용하려면 build.gradle에 implementation 'org.springframework.boot:spring-boot-starter-validation' 의존성 라이브러리를 직접 장착해야 정상 동작합니다.

org.springframework.validation.annotation.@Validated: 스프링 프레임워크 전용 검증 유틸 애노테이션으로, 자바 표준 검증 기능에 스프링 특화 편리성(그룹 검증 기능 등)을 한층 업그레이드하여 기본 탑재한 버전입니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 3. 메시지와 국제화|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 3. 메시지와 국제화]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 2. 타임리프 - 스프링 통합과 폼|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 2. 타임리프 - 스프링 통합과 폼]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
