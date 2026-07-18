---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-02
source_url: https://ch010104.tistory.com/287
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation

## 원문

https://ch010104.tistory.com/287

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

특정 필드에 대한 검증 로직(예: 빈 값 검증, 문자열 길이 제한, 숫자 범위 제한 등)은 거의 모든 애플리케이션에서 매우 유사하고 일반적인 형태를 가집니다. 이를 매번 수작업 코드로 작성하는 것은 대단히 번거롭습니다.

이와 같이 검증 애노테이션 하나로 검증 로직을 편리하게 적용할 수 있도록 공통화하고 표준화한 기술 표준이 바로 Bean Validation입니다.

## 원문 기반 학습 정리

### 1. Bean Validation 소개

### 1.1 검증 로직의 공통화와 표준화 필요성

특정 필드에 대한 검증 로직(예: 빈 값 검증, 문자열 길이 제한, 숫자 범위 제한 등)은 거의 모든 애플리케이션에서 매우 유사하고 일반적인 형태를 가집니다. 이를 매번 수작업 코드로 작성하는 것은 대단히 번거롭습니다.

```java
public class Item {
    private Long id;

    @NotBlank
    private String itemName;

    @NotNull
    @Range(min = 1000, max = 1000000)
    private Integer price;

    @NotNull
    @Max(9999)
    private Integer quantity;
}
```

이와 같이 검증 애노테이션 하나로 검증 로직을 편리하게 적용할 수 있도록 공통화하고 표준화한 기술 표준이 바로 Bean Validation입니다.

### 1.2 Bean Validation이란?

기술 표준: Bean Validation은 특정 구현체가 아니라 Bean Validation 2.0 (JSR-380)이라는 자바 기술 표준 규격입니다. 즉, 검증 애노테이션과 여러 인터페이스의 모음입니다.

대표 구현체: 마치 JPA 표준 사양의 대표 구현체로 하이버네이트가 있는 것처럼, Bean Validation의 가장 일반적인 구현체는 하이버네이트 Validator(Hibernate Validator)입니다. (이름에 '하이버네이트'가 붙어 있지만 ORM과는 아무런 관련이 없습니다.)

### 2. Bean Validation - 시작 (순수 자바 환경)

### 2.1 의존관계 추가

스프링 부트 환경에서 Bean Validation을 적용하기 위해 다음 라이브러리를 추가합니다.

### build.gradle

```java
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

해당 스타터를 추가하면 내부에 다음과 같은 핵심 라이브러리들이 설치됩니다.

jakarta.validation-api: Bean Validation의 표준 인터페이스

hibernate-validator: 기술 표준을 구현한 실제 구현체

### 2.2 도메인 모델에 애노테이션 적용 (Item.java)

```java
package hello.itemservice.domain.item;

import lombok.Data;
import org.hibernate.validator.constraints.Range;
import javax.validation.constraints.Max;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
public class Item {

    private Long id;

    @NotBlank
    private String itemName;

    @NotNull
    @Range(min = 1000, max = 1000000)
    private Integer price;

    @NotNull
    @Max(9999)
    private Integer quantity;

    public Item() {
    }

    public Item(String itemName, Integer price, Integer quantity) {
        this.itemName = itemName;
        this.price = price;
        this.quantity = quantity;
    }
}
```

### 검증 애노테이션 분석

@NotBlank: 빈 값(null) 및 공백("", " ")을 모두 허용하지 않습니다. (가장 강력한 문자열 제약조건)

@NotNull: null을 허용하지 않습니다. ("" 이나 " "은 허용됨)

@Range(min = 1000, max = 1000000): 지정한 범위 안의 값이어야 합니다.

@Max(9999): 최대 9999까지만 값을 허용합니다.

💡 표준 애노테이션과 구현체 애노테이션의 차이

javax.validation.constraints.NotNull과 같이 javax.validation(또는 최신 사양의 jakarta.validation)으로 시작하는 패키지는 특정 구현체에 종속되지 않는 자바 표준 인터페이스입니다.

org.hibernate.validator.constraints.Range와 같이 org.hibernate.validator로 시작하는 패키지는 하이버네이트 Validator에서만 독자적으로 제공하는 검증 기능입니다. 실무에서는 사실상 하이버네이트 Validator를 표준처럼 사용하기 때문에 둘을 자유롭게 혼용해도 무방합니다.

### 2.3 순수 자바 검증 테스트 코드

```java
package hello.itemservice.validation;

import hello.itemservice.domain.item.Item;
import org.junit.jupiter.api.Test;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import javax.validation.ValidatorFactory;
import java.util.Set;

public class BeanValidationTest {

    @Test
    void beanValidation() {
        // 검증기 팩토리 및 검증기(Validator) 생성
        ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
        Validator validator = factory.getValidator();

        // 에러를 유발하는 잘못된 데이터 세팅
        Item item = new Item();
        item.setItemName(" "); // 공백 유발
        item.setPrice(0);      // 범위 미달 (1000 미만)
        item.setQuantity(10000); // 최대값 초과 (9999 초과)

        // 검증 실행
        Set<ConstraintViolation<Item>> violations = validator.validate(item);

        // 결과 검증 및 출력
        for (ConstraintViolation<Item> violation : violations) {
            System.out.println("violation=" + violation);
            System.out.println("violation.message=" + violation.getMessage());
        }
    }
}
```

### 실행 결과 출력 로그

```text
violation={interpolatedMessage='공백일 수 없습니다', propertyPath=itemName, rootBeanClass=class hello.itemservice.domain.item.Item, messageTemplate='{javax.validation.constraints.NotBlank.message}'}
violation.message=공백일 수 없습니다

violation={interpolatedMessage='9999 이하여야 합니다', propertyPath=quantity, rootBeanClass=class hello.itemservice.domain.item.Item, messageTemplate='{javax.validation.constraints.Max.message}'}
violation.message=9999 이하여야 합니다

violation={interpolatedMessage='1000과 1000000 사이여야 합니다', propertyPath=price, rootBeanClass=class hello.itemservice.domain.item.Item, messageTemplate='{org.hibernate.validator.constraints.Range.message}'}
violation.message=1000과 1000000 사이여야 합니다
```

ConstraintViolation 객체 안에는 검증 에러가 발생한 대상(Root Bean Class), 에러 필드 경로(propertyPath), 그리고 에러 템플릿과 메시지 정보가 상세히 담겨 나옵니다.

### 3. Bean Validation - 스프링 MVC 통합 적용

### 3.1 스프링 부트의 자동 통합 메커니즘

스프링 부트가 spring-boot-starter-validation 라이브러리를 감지하면 다음과 같이 글로벌 검증 환경을 자동으로 통합합니다.

LocalValidatorFactoryBean의 글로벌 등록: 스프링 부트는 애노테이션 기반 검증을 처리하는 LocalValidatorFactoryBean을 스프링 컨테이너의 글로벌 Validator로 자동 등록합니다.

검증 실행: 컨트롤러 파라미터에 @Valid 또는 @Validated 애노테이션만 적어주면 이 글로벌 Validator가 필드들을 순차적으로 검증합니다.

BindingResult 연동: 검증 중 오류를 발견하면, 스프링은 오류 내용을 담은 FieldError 및 ObjectError를 생성하여 자동으로 BindingResult에 채워 넣습니다.

⚠️ 주의: 글로벌 Validator를 직접 수동 등록하는 경우 다음과 같이 WebMvcConfigurer를 통해 수동으로 검증기(예: ItemValidator)를 직접 등록하면, 스프링 부트는 빈 검증용 LocalValidatorFactoryBean을 글로벌 검증기로 등록하지 않습니다. 따라서 애노테이션 기반의 빈 검증기가 전혀 작동하지 않게 되므로, 수동 글로벌 Validator 등록은 지양해야 합니다.

```java
@SpringBootApplication
public class ItemServiceApplication implements WebMvcConfigurer {
    // 아래처럼 직접 등록하면 Bean Validation이 동작하지 않음!
    @Override
    public Validator getValidator() {
        return new ItemValidator();
    }
}
```

### 3.2 @Valid vs @Validated

@Valid: 자바 표준 애노테이션(javax.validation.@Valid)입니다. 사용 시 별도의 옵션 지정이 불가능합니다.

@Validated: 스프링 프레임워크 전용 애노테이션(org.springframework.validation.annotation.Validated)입니다. 순서 지정이나 그룹 지정 검증(Groups) 기능과 같이 스프링에 정교화된 추가 옵션을 탑재하고 있습니다.

### 3.3 컨트롤러 적용 코드 (ValidationItemControllerV3.java)

```java
package hello.itemservice.web.validation;

import hello.itemservice.domain.item.Item;
import hello.itemservice.domain.item.ItemRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import java.util.List;

@Slf4j
@Controller
@RequestMapping("/validation/v3/items")
@RequiredArgsConstructor
public class ValidationItemControllerV3 {

    private final ItemRepository itemRepository;

    @GetMapping
    public String items(Model model) {
        List<Item> items = itemRepository.findAll();
        model.addAttribute("items", items);
        return "validation/v3/items";
    }

    @GetMapping("/{itemId}")
    public String item(@PathVariable long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v3/item";
    }

    @GetMapping("/add")
    public String addForm(Model model) {
        model.addAttribute("item", new Item());
        return "validation/v3/addForm";
    }

    @PostMapping("/add")
    public String addItem(@Validated @ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        // 특정 필드가 아닌 전체 예외(글로벌 오류) 처리 - 자바 코드로 직접 구성
        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }

        // 검증 에러 발생 시 입력 폼으로 다시 이동
        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v3/addForm";
        }

        // 검증 통과 시 성공 로직 진행
        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v3/items/{itemId}";
    }

    @GetMapping("/{itemId}/edit")
    public String editForm(@PathVariable Long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v3/editForm";
    }

    @PostMapping("/{itemId}/edit")
    public String edit(@PathVariable Long itemId, @Validated @ModelAttribute Item item, BindingResult bindingResult) {

        // 글로벌 오류 검증
        if (item.getPrice() != null && item.getQuantity() != null) {
            int resultPrice = item.getPrice() * item.getQuantity();
            if (resultPrice < 10000) {
                bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }

        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v3/editForm";
        }

        itemRepository.update(itemId, item);
        return "redirect:/validation/v3/items/{itemId}";
    }
}
```

### 3.4 바인딩과 Bean Validation의 정밀한 실행 순서

검증 대상 파라미터가 유입될 때 스프링은 다음 단계를 엄격히 준수합니다.

```text
[HTTP 요청 파라미터 전송]
        ↓
1단계: @ModelAttribute 개별 필드 타입 바인딩 시도
        ├─ 바인딩 성공 ──> (2단계로 이동)
        └─ 바인딩 실패 ──> typeMismatch FieldError 추가 (2단계 검증 적용 제외)
        ↓
2단계: 바인딩에 성공한 필드에 한해서만 Bean Validation 적용
```

이유: 타입 변환 자체가 실패하여 객체의 해당 필드에 원하는 데이터가 들어오지도 못한 상태에서는 빈 검증(Bean Validation)을 가동하는 것이 무의미하기 때문입니다.

예시:

itemName 필드에 "A" 입력 ➡️ 타입 바인딩 성공 ➡️ @NotBlank 검증 가동 ➡️ 검증 성공

price 필드에 "A" 입력 ➡️ 문자열을 Integer로 바인딩 시도 실패 ➡️ typeMismatch 오류를 BindingResult에 즉시 추가 ➡️ price 필드는 Bean Validation을 타지 않고 검증 패스

### 4. Bean Validation - 에러 코드와 메시지 매칭 규칙

### 4.1 에러 코드의 자동 생성 원리

Bean Validation이 가동되어 검증 에러가 발생하면, 애노테이션 명칭을 기반으로 에러 코드가 자동 생성됩니다. MessageCodesResolver를 거쳐 구체적인 순서대로 메시지 코드가 할당됩니다.

### @NotBlank 에러 코드 분석 예시

NotBlank.item.itemName (애노테이션명 + 객체명 + 필드명)

NotBlank.itemName (애노테이션명 + 필드명)

NotBlank.java.lang.String (애노테이션명 + 필드타입)

NotBlank (애노테이션명)

### @Range 에러 코드 분석 예시

Range.item.price

Range.price

Range.java.lang.Integer

Range

### 4.2 오류 메시지 등록하기 (errors.properties)

이러한 규칙성에 따라 errors.properties에 원하는 메시지를 체계적으로 담아줄 수 있습니다.

```text
# Bean Validation 맞춤 메시지 정의
NotBlank={0} 공백일 수 없습니다. (필수 입력 항목)
Range={0}, {2} ~ {1} 사이의 범위여야 합니다.
Max={0}, 최대 {1} 이하여야 합니다.
```

{0}: 에러가 발생한 필드 명칭으로 자동 변환됩니다.

{1}, {2} 등: 애노테이션 내부 속성 값에 따라 달라집니다. (예: @Range(min=1000, max=1000000)인 경우 {1}은 1000000, {2}는 1000이 매칭됩니다.)

### 4.3 Bean Validation 메시지 매칭 우선순위

스프링과 빈 검증기는 에러 발생 시 다음 3단계 우선순위로 메시지를 탐색합니다.

1순위: errors.properties와 같은 메시지 소스(MessageSource)에 등록된 구체적인 키 탐색

2순위: 애노테이션의 message 속성에 직접 명시된 값 적용

예: @NotBlank(message = "공백은 입력할 수 없습니다.") private String itemName;

3순위: 하이버네이트 Validator 라이브러리가 기본으로 가지고 있는 기본 오류 메시지 출력 (예: "공백일 수 없습니다.")

### 5. 오브젝트 오류 (글로벌 오류) 처리

특정 필드가 아닌, 객체 전체의 복합 제약조건(예: 가격 * 수량의 합이 최소 10,000원 이상이어야 하는 제약)은 어떻게 해결할까요?

### 5.1 @ScriptAssert를 활용한 처리

표준 스펙상 @ScriptAssert 애노테이션을 도메인 클래스 헤더에 붙여 스크립트 기반 글로벌 검증을 처리할 수 있습니다.

```java
@Data
@ScriptAssert(lang = "javascript", script = "_this.price * _this.quantity >= 10000")
public class Item {
    // ...
}
```

### 메시지 코드 생성

ScriptAssert.item

ScriptAssert

### @ScriptAssert 사용의 한계와 실무 권장사항

실무에서 @ScriptAssert를 실제로 활용하기에는 다음과 같은 치명적 단점들이 존재합니다.

복잡성과 가독성: 자바스크립트 엔진 문법이 애노테이션 안에 뒤섞여 코드가 매우 지저분해지고 복잡해집니다.

검증 범위 제한: 실제 검증은 특정 도메인 객체의 범위만을 검증하는 것에 그치지 않고, 데이터베이스 연동 조회를 하거나 외부 API를 호출하는 등 객체 외부 데이터가 엮인 복합 검증이 잦습니다. 이 경우 애노테이션 한 장으로는 커버가 절대 불가능합니다.

권장 해결책: 따라서 오브젝트 단위 글로벌 오류는 @ScriptAssert를 억지로 사용하기보다, 컨트롤러 단에서 직접 자바 코드로 로직을 서술하고 bindingResult.reject()를 호출하여 처리하는 것이 유지보수와 안정성 측면에서 절대적으로 권장됩니다.

```text
// 권장되는 컨트롤러 내 글로벌 검증 예시
if (item.getPrice() != null && item.getQuantity() != null) {
    int resultPrice = item.getPrice() * item.getQuantity();
    if (resultPrice < 10000) {
        bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
    }
}
```

### 6. 단일 객체 기반 Bean Validation의 한계

### 6.1 등록과 수정 요구사항의 불일치

사용자가 상품을 등록할 때와 나중에 저장된 상품 정보를 수정할 때는 시스템적 비즈니스 제약조건이 충돌하는 경우가 다반사입니다.

### 6.2 하나의 도메인에 다중 조건 부여 시 발생할 수 있는 충돌

요구사항을 반영하여 Item 엔티티 한 장에 다음과 같이 일괄 애노테이션을 적용하면 큰 문제가 발생합니다.

```java
@Data
public class Item {

    @NotNull // 수정 시 필수, 등록 시에는 null이라 에러 발생!
    private Long id;

    @NotBlank
    private String itemName;

    @NotNull
    @Range(min = 1000, max = 1000000)
    private Integer price;

    @NotNull
    // @Max(9999)를 걸면 등록에는 맞지만, 수정에서 수량 제한을 풀 수 없음!
    private Integer quantity;
}
```

결과: Item 도메인 엔티티를 등록과 수정 둘 다에 일방적으로 적용하면 검증 조건들이 서로 충돌하여, 등록 프로세스 자체가 완전히 마비되거나 수정 요구사항을 충족시키지 못하는 치명적인 한계에 다다릅니다.

### 7. 한계 극복법 1 - Bean Validation groups 사용

등록용 검증 조건과 수정용 검증 조건을 그룹으로 분류하여 타겟팅 검증을 실행할 수 있습니다.

### 7.1 마커 인터페이스(Marker Interface) 생성

아무런 메소드 바디도 가지지 않는 구분용 빈 인터페이스를 각각 설계합니다.

### 저장 그룹 구분 인터페이스 (SaveCheck.java)

```text
package hello.itemservice.domain.item;
public interface SaveCheck {
}
```

### 수정 그룹 구분 인터페이스 (UpdateCheck.java)

```text
package hello.itemservice.domain.item;
public interface UpdateCheck {
}
```

### 7.2 도메인 엔티티에 groups 매핑 (Item.java)

```java
package hello.itemservice.domain.item;

import lombok.Data;
import org.hibernate.validator.constraints.Range;
import javax.validation.constraints.Max;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
public class Item {

    @NotNull(groups = UpdateCheck.class) // 수정 조건 적용
    private Long id;

    @NotBlank(groups = {SaveCheck.class, UpdateCheck.class}) // 등록, 수정 공통
    private String itemName;

    @NotNull(groups = {SaveCheck.class, UpdateCheck.class})
    @Range(min = 1000, max = 1000000, groups = {SaveCheck.class, UpdateCheck.class})
    private Integer price;

    @NotNull(groups = {SaveCheck.class, UpdateCheck.class})
    @Max(value = 9999, groups = SaveCheck.class) // 오직 등록 조건만 적용
    private Integer quantity;

    // ... 기본 생성자 생략
}
```

### 7.3 컨트롤러 적용

### 등록 메서드

```text
@PostMapping("/add")
public String addItemV2(@Validated(SaveCheck.class) @ModelAttribute Item item, BindingResult bindingResult, RedirectAttributes redirectAttributes) {
    // ...
}
```

### 수정 메서드

```text
@PostMapping("/{itemId}/edit")
public String editV2(@PathVariable Long itemId, @Validated(UpdateCheck.class) @ModelAttribute Item item, BindingResult bindingResult) {
    // ...
}
```

💡 중요: @Valid와 groups 기능 사용 불가 정보 표준 스펙인 자바의 @Valid 애노테이션은 그룹핑 기능을 직접 지정하는 옵션이 내장되어 있지 않습니다. 따라서 특정 검증 그룹을 필터링하려면 반드시 스프링 전용 검증 유틸인 @Validated(특정Check.class) 형태로 호출해야 합니다.

### 7.4 Groups의 평가와 아쉬운 점

장점: 하나의 도메인 엔티티 클래스 안에서 수동 제약 조건을 그룹별로 모듈화할 수 있습니다.

단점: 조건이 늘어날수록 엔티티 내부 코드가 groups 설정 문자열로 가득 차 매우 번잡해지며, 코드 가독성과 가독 제어율이 전체적으로 나빠집니다.

한계: 실무에서는 단순히 상품만 저장하는 것이 아니라 회원 가입 시 약관 동의 체크, 부가 정보 수취 등 도메인 범위 외의 수많은 파생 폼 데이터가 결합하여 서버로 유입됩니다. 따라서 실제 현업에서는 groups 기능을 거의 활용하지 않으며, 다음에 등장하는 "Form 전송 전용 데이터 객체 분리" 방식을 절대적 표준으로 사용합니다.

### 8. 한계 극복법 2 - Form 전송 전용 데이터 객체 분리 (실무 표준 방식)

### 8.1 폼 객체 분리 흐름 개념 분석

### 기존 방식 (한계가 존재했던 단순 흐름)

HTML Form ➡️ Item 도메인 객체 직접 수신 ➡️ Controller ➡️ Repository

장단점: 중간 변환 단계가 없어 단순하고 코드가 얇아지지만, 비즈니스 검증이 조금만 꼬여도 등록/수정 검증 조건이 충돌하고 groups를 억지로 사용해야만 합니다.

### 권장 방식 (정제된 DTO 및 전송 객체 분리 흐름)

HTML Form ➡️ 전용 Form 데이터 객체(ItemSaveForm / ItemUpdateForm) ➡️ Controller ➡️ Item 도메인 객체 새로 생성 ➡️ Repository

장단점: 중간에 Form 데이터를 도메인 객체로 이식하고 가공하는 변환용 코드가 몇 줄 추가되지만, 복잡한 폼 레이아웃 데이터에 맞춰 완벽히 명확하게 검증 조건을 다변화하여 대응할 수 있습니다. 등록과 수정이 완벽히 파일 단위로 분리되므로 groups를 고려할 필요가 전혀 없어집니다.

### 8.2 도메인 엔티티 순수화 원복 (Item.java)

폼 객체로 검증 책임을 모두 이전하므로, 도메인 핵심 객체는 검증 코드를 완전히 걷어내고 유기적인 데이터 저장 구조로 원복합니다.

```java
package hello.itemservice.domain.item;

import lombok.Data;

@Data
public class Item {
    private Long id;
    private String itemName;
    private Integer price;
    private Integer quantity;
}
```

### 8.3 등록 전용 폼 데이터 수신 객체 (ItemSaveForm.java)

```java
package hello.itemservice.web.validation.form;

import lombok.Data;
import org.hibernate.validator.constraints.Range;
import javax.validation.constraints.Max;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
public class ItemSaveForm {

    @NotBlank
    private String itemName;

    @NotNull
    @Range(min = 1000, max = 1000000)
    private Integer price;

    @NotNull
    @Max(value = 9999) // 등록 상황에 알맞은 검증 조건 적용
    private Integer quantity;
}
```

### 8.4 수정 전용 폼 데이터 수신 객체 (ItemUpdateForm.java)

```java
package hello.itemservice.web.validation.form;

import lombok.Data;
import org.hibernate.validator.constraints.Range;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
public class ItemUpdateForm {

    @NotNull // 수정 시 필수 조건
    private Long id;

    @NotBlank
    private String itemName;

    @NotNull
    @Range(min = 1000, max = 1000000)
    private Integer price;

    // 수정 상황에 맞춤: 수량 제한 제거 (@Max 제한 없음)
    private Integer quantity;
}
```

### 8.5 폼 분리 적용 컨트롤러 구현 (ValidationItemControllerV4.java)

```java
package hello.itemservice.web.validation;

import hello.itemservice.domain.item.Item;
import hello.itemservice.domain.item.ItemRepository;
import hello.itemservice.web.validation.form.ItemSaveForm;
import hello.itemservice.web.validation.form.ItemUpdateForm;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import java.util.List;

@Slf4j
@Controller
@RequestMapping("/validation/v4/items")
@RequiredArgsConstructor
public class ValidationItemControllerV4 {

    private final ItemRepository itemRepository;

    @GetMapping
    public String items(Model model) {
        List<Item> items = itemRepository.findAll();
        model.addAttribute("items", items);
        return "validation/v4/items";
    }

    @GetMapping("/{itemId}")
    public String item(@PathVariable long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v4/item";
    }

    @GetMapping("/add")
    public String addForm(Model model) {
        model.addAttribute("item", new Item());
        return "validation/v4/addForm";
    }

    @PostMapping("/add")
    public String addItem(@Validated @ModelAttribute("item") ItemSaveForm form, BindingResult bindingResult, RedirectAttributes redirectAttributes) {

        // 글로벌 오브젝트 오류 수동 검증
        if (form.getPrice() != null && form.getQuantity() != null) {
            int resultPrice = form.getPrice() * form.getQuantity();
            if (resultPrice < 10000) {
                bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }

        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v4/addForm";
        }

        // 성공 시 폼 전송 데이터 기반 도메인 엔티티(Item) 객체 생성 및 이식
        Item item = new Item();
        item.setItemName(form.getItemName());
        item.setPrice(form.getPrice());
        item.setQuantity(form.getQuantity());

        Item savedItem = itemRepository.save(item);
        redirectAttributes.addAttribute("itemId", savedItem.getId());
        redirectAttributes.addAttribute("status", true);
        return "redirect:/validation/v4/items/{itemId}";
    }

    @GetMapping("/{itemId}/edit")
    public String editForm(@PathVariable Long itemId, Model model) {
        Item item = itemRepository.findById(itemId);
        model.addAttribute("item", item);
        return "validation/v4/editForm";
    }

    @PostMapping("/{itemId}/edit")
    public String edit(@PathVariable Long itemId, @Validated @ModelAttribute("item") ItemUpdateForm form, BindingResult bindingResult) {

        // 글로벌 오브젝트 오류 수동 검증
        if (form.getPrice() != null && form.getQuantity() != null) {
            int resultPrice = form.getPrice() * form.getQuantity();
            if (resultPrice < 10000) {
                bindingResult.reject("totalPriceMin", new Object[]{10000, resultPrice}, null);
            }
        }

        if (bindingResult.hasErrors()) {
            log.info("errors={}", bindingResult);
            return "validation/v4/editForm";
        }

        // 폼 전송 데이터 기반 업데이트 객체 매핑
        Item itemParam = new Item();
        itemParam.setItemName(form.getItemName());
        itemParam.setPrice(form.getPrice());
        itemParam.setQuantity(form.getQuantity());

        itemRepository.update(itemId, itemParam);
        return "redirect:/validation/v4/items/{itemId}";
    }
}
```

### ⚠️ @ModelAttribute("item") 이름 명시 시 주의점

@ModelAttribute("item") ItemSaveForm form에서 명시적으로 "item" 문자열을 지정해 주는 부분이 대단히 핵심적입니다.

만약 이를 지정해 주지 않으면, 스프링의 규칙에 의해서 파라미터 클래스명인 ItemSaveForm을 소문자로 시작하도록 변경한 itemSaveForm이라는 명칭으로 MVC Model 영역에 등록이 되게 됩니다.

그렇게 되면 타임리프 뷰 템플릿 영역에서 데이터에 정기 바인딩하는 th:object="${item}"의 이름을 전부 다 수정해야 하므로, 기존 템플릿과의 부드러운 호환성을 위해 이름을 꼭 명시해 주어야 합니다.

### 9. Bean Validation - HTTP 메시지 컨버터 (API 검증 환경)

@Valid 및 @Validated는 HTML 폼 파라미터 파싱뿐만 아니라, HttpMessageConverter (@RequestBody 기반 JSON 요청 등) 환경에서도 동일하게 가동할 수 있습니다.

### 9.1 API 컨트롤러 구현 (ValidationItemApiController.java)

```java
package hello.itemservice.web.validation;

import hello.itemservice.web.validation.form.ItemSaveForm;
import lombok.extern.slf4j.Slf4j;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("/validation/api/items")
public class ValidationItemApiController {

    @PostMapping("/add")
    public Object addItem(@RequestBody @Validated ItemSaveForm form, BindingResult bindingResult) {
        log.info("API 컨트롤러 호출");

        if (bindingResult.hasErrors()) {
            log.info("검증 오류 발생 errors={}", bindingResult);
            // 에러 객체 통째 반환 (테스트 용도)
            return bindingResult.getAllErrors();
        }

        log.info("성공 로직 실행");
        return form;
    }
}
```

### 9.2 API 환경에서의 3가지 결과 시나리오 및 분석

API 요청을 통해 들어오는 상황은 크게 다음과 같은 세 갈래의 시나리오로 제어됩니다.

### 시나리오 ①: 성공 케이스 (바인딩 성공 + 검증 통과)

요청 정보: POST <http://localhost:8080/validation/api/items/add>

JSON 바디: {"itemName":"hello", "price": 1000, "quantity":10}

서버 동작 로그:

API 컨트롤러 호출 성공 로직 실행

### 시나리오 ②: 실패 케이스 (JSON 객체 생성 자체 실패)

클라이언트가 타입 규격에 전혀 맞지 않는 원시 데이터를 제공한 경우입니다.

요청 정보: 동일 경로

JSON 바디: {"itemName":"hello", "price": "A", "quantity": 10} (숫자 필드인 price에 문자 "A" 기입)

서버 에러 응답: Bad Request (400) 반환

{ "timestamp": "2026-07-01T19:43:00.000+00:00", "status": 400, "error": "Bad Request", "message": "", "path": "/validation/api/items/add" }

서버 동작 로그:

org.springframework.http.converter.HttpMessageNotReadableException: JSON parse error: Cannot deserialize value of type `java.lang.Integer` from String "A"...

중요 메커니즘 분석:

HttpMessageConverter 단계에서 JSON에서 자바 DTO인 ItemSaveForm 객체로 역직렬화하는 자체가 실패합니다.

객체 생성 자체가 불발되었기 때문에 컨트롤러 호출 자체가 원천적으로 취소되며 예외를 바로 터트립니다.

당연히 Validator에 도달하지도 못합니다.

### 시나리오 ③: 검증 실패 케이스 (객체 생성은 성공했으나, 비즈니스 검증 실패)

요청 정보: 동일 경로

JSON 바디: {"itemName":"hello", "price": 1000, "quantity": 10000} (수량 최대 제약조건인 @Max(9999) 초과)

서버 에러 응답: bindingResult.getAllErrors()가 JSON 배열 형식으로 포매팅되어 응답됩니다.

```text
[
    {
        "codes": [
            "Max.itemSaveForm.quantity",
            "Max.quantity",
            "Max.java.lang.Integer",
            "Max"
        ],
        "arguments": [
            {
                "codes": [
                    "itemSaveForm.quantity",
                    "quantity"
                ],
                "arguments": null,
                "defaultMessage": "quantity",
                "code": "quantity"
            },
            9999
        ],
        "defaultMessage": "9999 이하여야 합니다",
        "objectName": "itemSaveForm",
        "field": "quantity",
        "rejectedValue": 10000,
        "bindingFailure": false,
        "code": "Max"
    }
]
```

서버 동작 로그:

```java
API 컨트롤러 호출
검증 오류 발생, errors=org.springframework.validation.BeanPropertyBindingResult: 1 errors
Field error in object 'itemSaveForm' on field 'quantity': rejected value [10000]; ... default message [9999 이하여야 합니다]
```

실무 설계 조언: 여기서 bindingResult.getAllErrors()를 직접 리턴하면 위 에러 JSON 구조가 그대로 노출됩니다. 실제 개발 진행 시에는 API 연동 규격을 간결하게 유지하기 위해 필요한 메시지 항목만 정교하게 커스텀 클래스로 다시 생성하여 가공한 뒤 반환하는 방식을 취해야 합니다.

### 10. @ModelAttribute vs @RequestBody

HTTP 요청을 정밀 검증할 때 두 처리 스펙은 데이터를 가공하는 근본적인 단위에서 격차가 납니다.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                              작동 차이 비교                              │
├───────────────────┬────────────────────────────────────────────────────┤
│   @ModelAttribute │ 개별 필드 단위로 바인딩이 각각 개별 가동됨                  │
│                   │ ➡️ 특정 필드가 실패해도 나머지 필드는 정상 가동 및 검증 가능 │
├───────────────────┼────────────────────────────────────────────────────┤
│      @RequestBody │ 객체 전체 단위로 바인딩이 일괄 가동됨                      │
│                   │ ➡️ JSON 역직렬화 실패 시 즉각 작동 차단, 컨트롤러 가동 안 됨 │
└───────────────────┴────────────────────────────────────────────────────┘
```

@ModelAttribute (세밀하고 개별적인 필드 접근):

쿼리 스트링이나 Form 기반 파라미터는 개별 필드가 독자적으로 쪼개져 컨트롤러 객체 안으로 밀려 들어옵니다.

설령 특정 필드 하나가 타입 바인딩 오류로 좌초하더라도, 나머지 정상적으로 들어온 필드들은 무사히 바인딩에 골인하며, 빈 검증(Bean Validation) 단계까지 진입해서 필드 검증을 이어갈 수 있습니다.

@RequestBody (한배를 탄 거대한 일괄 체계):

JSON 형식 데이터는 하나의 단일한 거대 데이터 군집을 이룹니다.

JSON 파서와 HttpMessageConverter가 JSON을 정해진 자바 모델 객체로 완벽히 가공 및 완성시키지 못하는 한, 예외를 일으키며 모든 비즈니스 흐름을 정지시킵니다.

따라서 컨트롤러 내부 진입은 물론이고, 데이터 검증용 Validator 작동 구역조차 구경하지 못하고 중도 이탈하게 됩니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 6. 로그인처리1 - 쿠키, 세션|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
