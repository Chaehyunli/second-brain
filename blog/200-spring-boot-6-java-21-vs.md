---
title: "[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/200
archive_method: Tistory sitemap + HTML content extraction
---

# [Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드

> 원문: https://ch010104.tistory.com/200

## 본문

1. 가상 스레드 개념 정리 등장 배경: 기존 스레드의 한계 기존의 Java 스레드(Platform Thread)는 OS 스레드와 1:1로 매핑됩니다.  리소스 소모: 스레드 하나 생성 시 약 1MB~2MB의 메모리가 필요합니다. 컨텍스트 스위칭 비용: 스레드 전환 시 OS 커널이 개입하므로 CPU 비용이 큽니다. 확장성 문제: 수천 명의 동시 접속자를 처리하려면 수천 개의 스레드가 필요한데, 메모리 한계로 인해 서버가 버티지 못하는 '스레드 고갈' 현상이 발생합니다.  가상 스레드(Virtual Thread)란? JVM이 관리하는 경량 논리 단위로, OS 스레드와 직접 연결되지 않습니다.  수백만 개 생성 가능: 메모리를 KB 단위로 아주 적게 사용하여 일반 노트북에서도 수십만 개 이상을 동시에 띄울 수 있습니다. M:N 매핑: 수많은 가상 스레드가 소수의 실제 OS 스레드(Carrier Thread) 위에서 번갈아 가며 실행됩니다. Non-blocking처럼 동작: I/O 작업(DB 조회 등)으로 대기 상태가 되면, JVM이 해당 가상 스레드를 OS 스레드에서 내려놓고(Unmount) 다른 가상 스레드를 실행합니다.  주요 특징 요약 특징 기존 스레드 (Platform) 가상 스레드 (Virtual)    생성 비용 매우 높음 (스레드 풀 필수) 매우 낮음 (필요할 때마다 생성)   메모리 점유 MB 단위 (무거움) KB 단위 (매우 가벼움)   개수 제한 수백 ~ 수천 개 수십만 ~ 수백만 개   주요 용도 CPU 집약적 작업 I/O 집약적 작업 (웹 서버 등)     2. Java 코드 비교 (직접 사용할 때) 기존에는 스레드를 아껴 쓰기 위해 **풀링(Pooling)**을 했지만, 가상 스레드는 작업당 하나씩(Per-task) 던지는 것이 핵심입니다. [기존 방식: Fixed Thread Pool] // 스레드를 10개로 제한하고 돌려막기 try (var executor = Executors.newFixedThreadPool(10)) { for (int i = 0; i < 100; i++) { executor.submit(() -> { Thread.sleep(1000); // 여기서 스레드가 1초간 점유됨 return null; }); } }  [가상 스레드 방식: Virtual Thread Per Task] // 작업이 올 때마다 새로운 가상 스레드 생성 (제한 없음) try (var executor = Executors.newVirtualThreadPerTaskExecutor()) { for (int i = 0; i < 10000; i++) { // 1만 개를 동시에 띄워도 멀쩡함 executor.submit(() -> { Thread.sleep(1000); // JVM이 알아서 스레드를 효율적으로 관리 return null; }); } }   3. k6를 통한 성능 비교 [테스트용 k6 스크립트] import http from 'k6/http'; import { sleep } from 'k6'; export const options = { vus: 500, // 동시 접속자 500명 duration: '30s', // 30초 동안 테스트 }; export default function () { http.get('<http://localhost:8080/api/slow-job>'); // 1초 대기가 있는 API sleep(0.1); }  [예상 결과 리포트] 지표 기존 스레드 (Pool 200개) 가상 스레드 (Virtual)    처리량 (TPS) 약 180 ~ 200 req/s 약 450 ~ 500 req/s   평균 응답 시간 약 2.5초 (대기 발생) 약 1.0초 ~ 1.1초 (대기 없음)     4. Spring Boot에서의 활용 Spring Boot 환경에서는 개발자가 직접 위와 같은 스레드 관리 코드를 짤 필요가 거의 없습니다. 내장 톰캣(Tomcat)이 일꾼(스레드)을 배분하는 역할을 자동으로 수행하기 때문입니다. 우리는 단순히 **설정 파일(yml)**을 통해 톰캣이 "무거운 정직원 스레드" 대신 "가벼운 가상 스레드"를 사용하도록 엔진만 갈아끼워 주면 됩니다. application.yml 설정 (Spring Boot 3.2+ / Java 21+) spring: threads: virtual: enabled: true   효과: 위 설정을 켜는 순간, 톰캣은 요청 하나당 가상 스레드 하나를 할당합니다. 결과: 기존처럼 스레드 풀 크기(max-threads)를 고민하며 튜닝할 필요가 없어지며, I/O 작업이 많은 서비스에서 비약적인 성능 향상을 얻을 수 있습니다.  결론적으로, 가상 스레드는 "코드는 동기식으로 편하게 짜되, 성능은 비동기식의 효율을 내는" 기술!!
