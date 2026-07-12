---
title: "[스프링 입문] 1. Spring Boot에서 정적 페이지 로드 순서"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "INFLEARN"
published: 2026-03-03
source_url: https://ch010104.tistory.com/201
archive_method: Tistory sitemap + HTML content extraction
---

# [스프링 입문] 1. Spring Boot에서 정적 페이지 로드 순서

> 원문: https://ch010104.tistory.com/201

## 본문

1. 정적 페이지 조회 흐름 (그림 설명)  웹 브라우저 요청: 사용자가 주소창에 localhost:8080/hello-static.html을 입력합니다. 내장 톰캣 서버: 요청을 받아 스프링 컨테이너로 넘깁니다. 1순위 - 컨트롤러 확인: 스프링 컨테이너는 먼저 @GetMapping("/hello-static.html")이 설정된 컨트롤러가 있는지 찾습니다. (그림 상에서는 컨트롤러X) 2순위 - 정적 리소스 확인: 매핑된 컨트롤러가 없으므로, 내부 resources: static/hello-static.html 파일을 찾습니다. 반환: 해당 파일이 있으면 브라우저로 그대로 던져줍니다.   2. 전체 폴더 구조 및 예시 코드 프로젝트의 구조와 각 위치에 들어갈 코드는 다음과 같습니다. [전체 폴더 구조] spring-study ├── src │ └── main │ ├── java │ │ └── com.example.study │ │ └── HelloController.java (컨트롤러 위치) │ └── resources │ ├── static │ │ └── hello-static.html (정적 파일 위치) │ └── templates │ └── hello.html (타임리프 템플릿 위치) └── build.gradle   [각 폴더별 예시 코드] ① 컨트롤러 (src/main/java/...) 그림처럼 정적 파일이 실행되려면, 이 주소를 가로채는 컨트롤러가 없어야 합니다. @Controller public class HelloController { // 만약 여기에 @GetMapping("hello-static.html") 이 있다면 // static 폴더의 파일은 무시되고 이 메서드가 실행됩니다. }  ② 정적 HTML (src/main/resources/static/hello-static.html) 이곳에 파일을 두면 서버 사이드 렌더링(타임리프 등) 없이 파일 내용 그대로 전달됩니다. <!DOCTYPE html> <html> <head> <title>static content</title> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> </head> <body> 이것은 정적 컨텐츠입니다. 컨트롤러를 거치지 않고 바로 출력됩니다. </body> </html>   3. 핵심 요약  우선순위: 컨트롤러(@Controller) > 정적 리소스(static/) 차이점:  정적 페이지: 서버가 가공하지 않고 파일 그대로 브라우저에 보냄. (사용자마다 화면이 같음) 템플릿 엔진(타임리프): 서버(자바)에서 데이터를 넣어서 HTML을 동적으로 만들어 보냄. (사용자마다 화면이 다를 수 있음)
