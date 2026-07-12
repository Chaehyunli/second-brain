---
title: "[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/206
archive_method: Tistory sitemap + HTML content extraction
---

# [Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux

> 원문: https://ch010104.tistory.com/206

## 본문

1. 배경: 데이터의 '개수'가 아닌 '흐름' 기존의 List<User>나 User 객체는 데이터를 이미 다 가져온 '결과물'입니다. 반면 WebClient에서 사용하는 Mono와 Flux는 데이터가 도착할 것이라는 **'약속(Publisher)'**입니다. (데이터가 1개일지, 여러 개일지에 따라 적절한 그릇을 선택)  2. Mono (0 ~ 1개의 데이터)  *"단 한 번의 응답"**이 필요한 모든 곳에 사용합니다. 주로 상세 조회, 생성, 수정, 삭제 결과에 쓰입니다.  [실제 코드 예시: 단일 사용자 정보 조회] 파이썬 서버나 DB에서 특정 유저 한 명의 정보를 가져올 때의 전형적인 패턴입니다. public Mono<UserResponse> getUserDetail(Long userId) { return webClient.get() .uri("/api/users/{id}", userId) .retrieve() // 응답이 오면 딱 하나의 UserResponse 객체로 변환 .bodyToMono(UserResponse.class) // 데이터가 없을 경우 에러 처리 .switchIfEmpty(Mono.error(new RuntimeException("사용자를 찾을 수 없습니다."))); }   특징: 결과가 나오거나(onNext -> onComplete), 에러가 나거나(onError) 둘 중 하나로 깔끔하게 종료됩니다.   3. Flux (0 ~ N개의 데이터)  *"데이터의 스트림(목록)"**이 필요할 때 사용합니다. 여러 개의 데이터를 순차적으로 보낼 때 유리하며, 전체 데이터가 다 모일 때까지 기다리지 않고 도착하는 대로 처리할 수 있습니다.  [실제 코드 예시: 추천 게시글 목록 조회] 파이썬 AI 서버에서 계산된 여러 개의 추천 아이템 리스트를 받아올 때 사용합니다. public Flux<PostResponse> getRecommendedPosts(Long userId) { return webClient.get() .uri("/api/recommend/{id}", userId) .retrieve() // 여러 개의 객체가 담긴 스트림으로 변환 .bodyToFlux(PostResponse.class) // 개수 제한이나 필터링 가능 .take(10) // 최대 10개만 받기 .filter(post -> post.getScore() > 0.8); // 점수가 높은 것만 통과 }   특징: 첫 번째 데이터가 도착하는 즉시 처리를 시작할 수 있어, 사용자 체감 속도가 향상됩니다.   4. Mono와 Flux의 상호 변환 (실전 팁) 프로그래밍을 하다 보면 리스트를 Mono로 만들거나, Flux를 하나로 합쳐야 할 때가 있습니다.  Flux -> Mono (목록을 리스트 하나로 묶기):  // 여러 개의 응답을 하나의 List<PostResponse>를 가진 Mono로 변환 Mono<List<PostResponse>> listMono = getRecommendedPosts(userId).collectList();   Mono -> Flux (단일 데이터를 스트림으로 풀기):  // 하나의 유저 정보를 기반으로 여러 작업을 수행할 때 Flux<String> userRoles = getUserDetail(userId).flatMapMany(user -> Flux.fromIterable(user.getRoles()));   5. 핵심 결론: "지연 보상(Lazy Evaluation)" Mono와 Flux의 가장 중요한 점은 **.subscribe()(또는 스프링이 대신 해주는 리턴)**가 호출되기 전까지는 아무 일도 일어나지 않는다는 것입니다. // 파이썬 서버에 로그를 전송하는 비동기 작업 (결과에 상관없이 던지기만 할 때) webClient.post() .uri("/api/log") .bodyValue(logData) .retrieve() .bodyToMono(Void.class) .subscribe( result -> System.out.println("로그 전송 완료"), // 성공 시 처리 error -> System.err.println("에러 발생: " + error.getMessage()), // 에러 시 처리 () -> System.out.println("모든 프로세스 종료") // 완료 시 처리 ); // .subscribe()를 호출하는 순간, 메인 스레드는 다음 코드로 넘어가고 // 네트워크 작업은 비동기 일꾼이 별도로 처리합니다.
