---
title: "[스프링 핵심 원리 - 기본편] 12. Lombock 라이브러리"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "INFLEARN"
published: 2026-03-20
source_url: https://ch010104.tistory.com/232
archive_method: Tistory sitemap + HTML content extraction
---

# [스프링 핵심 원리 - 기본편] 12. Lombock 라이브러리

> 원문: https://ch010104.tistory.com/232

## 본문

최근 스프링 개발에서는 객체의 불변성을 유지하기 위해 필드에 final 키워드를 사용하는 것이 표준 하지만 매번 생성자를 만들고 대입하는 코드를 작성하는 것은 번거로움 이를 Lombock을 사용해서 편하게 함  1. 기본 코드 (생성자 주입) 가장 정석적인 방법으로, 생성자에 @Autowired를 붙여 의존관계를 주입 @Component public class OrderServiceImpl implements OrderService { private final MemberRepository memberRepository; private final DiscountPolicy discountPolicy; @Autowired public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) { this.memberRepository = memberRepository; this.discountPolicy = discountPolicy; } }  2. 생성자 1개 시 @Autowired 생략 스프링 프레임워크는 생성자가 딱 1개만 있으면 @Autowired를 생략해도 지동으로 주입을 수행합니다. @Component public class OrderServiceImpl implements OrderService { private final MemberRepository memberRepository; private final DiscountPolicy discountPolicy; // @Autowired 생략 가능 public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) { this.memberRepository = memberRepository; this.discountPolicy = discountPolicy; } }  3. 최종 결과 (Lombok 적용) 롬복의 @RequiredArgsConstructor를 사용하면 final이 붙은 필드를 모아 생성자를 자동으로 생성해 줍니다. 코드가 훨씬 간결해집니다. @Component @RequiredArgsConstructor // final 필드를 바탕으로 생성자를 자동 생성 public class OrderServiceImpl implements OrderService { private final MemberRepository memberRepository; private final DiscountPolicy discountPolicy; }   원리: 컴파일 시점에 자바의 '애노테이션 프로세서'가 실제 생성자 코드를 생성해 줍니다. 따라서 위 코드는 1번의 기본 코드와 완전히 동일하게 동작합니다.   롬복 라이브러리 설정 방법 1. build.gradle 설정 build.gradle 파일에 아래 설정을 추가하여 롬복을 활성화합니다. plugins { id 'org.springframework.boot' version '2.3.2.RELEASE' id 'io.spring.dependency-management' version '1.0.9.RELEASE' id 'java' } group = 'hello' version = '0.0.1-SNAPSHOT' sourceCompatibility = '11' // 1. lombok 설정 추가 시작 configurations { compileOnly { extendsFrom annotationProcessor } } repositories { mavenCentral() } dependencies { implementation 'org.springframework.boot:spring-boot-starter' // 2. lombok 라이브러리 추가 compileOnly 'org.projectlombok:lombok' annotationProcessor 'org.projectlombok:lombok' testCompileOnly 'org.projectlombok:lombok' testAnnotationProcessor 'org.projectlombok:lombok' testImplementation('org.springframework.boot:spring-boot-starter-test') { exclude group: 'org.junit.vintage', module: 'junit-vintage-engine' } } test { useJUnitPlatform() }  2. IDE(IntelliJ) 설정  Plugin 설치: Preferences (Windows: File -> Settings) -> Plugins -> Lombok 검색 후 설치 (재시작 필요). Annotation Processors 활성화: Preferences -> Build, Execution, Deployment -> Compiler -> Annotation Processors -> Enable annotation processing 체크. 확인: 임의의 클래스에 @Getter, @Setter를 작성하여 코드가 정상 작동하는지 확인   요약  최근에는 생성자 1개 유지 + @Autowired 생략 + 롬복 @RequiredArgsConstructor 조합을 가장 선호 이 방식은 불변성을 보장하면서도 상용구 코드를 최소화하여 코드 가독성을 극대화
