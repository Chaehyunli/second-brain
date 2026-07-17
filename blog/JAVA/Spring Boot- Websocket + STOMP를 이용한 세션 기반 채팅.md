---
title: "[Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "java", "springboot", "STOMP", "Websocket"]
category: "JAVA"
published: 2025-09-23
source_url: https://ch010104.tistory.com/140
---

# [Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅

## 원문

https://ch010104.tistory.com/140

## 노트 유형

`guide`

## 적용 목적과 전제조건

Spring Boot채팅 시스템은 RESTful API와 WebSocket API를 조합한 하이브리드 아키텍처를 채택

REST API는 채팅방 생성, 목록 조회, 이전 대화 내역 로딩과 같은 상태 관리를 담당

## 구현 절차·검증·주의점

### 1. 전체 아키텍처

Spring Boot채팅 시스템은 RESTful API와 WebSocket API를 조합한 하이브리드 아키텍처를 채택

REST API는 채팅방 생성, 목록 조회, 이전 대화 내역 로딩과 같은 상태 관리를 담당

WebSocket과 STOMP 프로토콜은 사용자들이 실시간으로 메시지를 주고받는 통신 채널의 역할을 수행

### 2. WebSocket + STOMP 설정

- 모든 실시간 통신의 기반이 되는 설정은 WebSocketConfig.java 파일에서 정의

- 이 설정은 STOMP 메시지 프로토콜을 사용하여 WebSocket 통신을 구조화

STOMP 엔드포인트: - /ws-stomp는 클라이언트가 최초로 WebSocket 연결을 맺는 진입점 - SockJS 지원을 통해 브라우저 호환성을 확보

메시지 브로커: - /topic prefix는 서버가 특정 주제(채팅방)를 구독하는 모든 클라이언트에게 메시지를 브로드캐스팅할 때 사용되는 경로

애플리케이션 Destination: - /app prefix는 클라이언트가 서버로 메시지를 보낼 때 사용되는 경로 - 서버의 @MessageMapping이 붙은 컨트롤러 메서드로 메시지를 라우팅

```java
// WebSocketConfig.java
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;

@Configuration
@EnableWebSocketMessageBroker // STOMP를 사용하는 WebSocket 메시지 브로커를 활성화합니다.
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        // 클라이언트가 WebSocket 연결을 시작할 주소(엔드포인트)를 설정합니다.
        registry.addEndpoint("/ws-stomp")
                .setAllowedOriginPatterns("*") // CORS 허용
                .withSockJS(); // WebSocket을 지원하지 않는 브라우저를 위한 SockJS 옵션
    }

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        // "/topic"으로 시작하는 destination을 구독하는 클라이언트에게 메시지를 브로드캐스팅합니다.
        registry.enableSimpleBroker("/topic");
        // "/app"으로 시작하는 destination으로 들어오는 메시지는 @MessageMapping 메서드로 라우팅됩니다.
        registry.setApplicationDestinationPrefixes("/app");
    }
}
```

### 3. 메시지 플로우

- 사용자가 보낸 메시지는 다음과 같은 명확한 흐름을 통해 처리되고 다시 모든 참여자에게 전달

발신 (Client → Server): - 클라이언트는 특정 채팅방(chatRoomId)으로 메시지를 보낼 때, /app/chat/{chatRoomId}라는 목적지로 메시지를 발행(Publish)

처리 (Server-side): - ChatMessageController가 이 메시지를 수신하여 ChatMessageService에 전 - 서비스 계층에서는 메시지를 DB에 저장(Messages 테이블)하는 등 비즈니스 로직을 수행

방송 (Server → Clients): - 처리가 완료되면, @SendTo 어노테이션에 의해 메시지는 /topic/chat/{chatRoomId}라는 토픽으로 브로드캐스팅

수신 (Clients): - 해당 토픽을 구독(Subscribe)하고 있던 모든 클라이언트(발신자 자신 포함)가 메시지를 실시간으로 수신하여 화면에 표시

### 4. 핵심 컴포넌트

ChatMessageController

실시간 메시지 처리의 진입점으로, 클라이언트로부터 메시지를 받아 서비스 계층으로 연결

처리된 결과를 다시 클라이언트들에게 브로드캐스팅하는 역할을 담당

```java
// ChatMessageController.java
import com.example.petner.domain.chat.dto.request.ChatMessageRequestDto;
import com.example.petner.domain.chat.dto.response.ChatMessageResponseDto;
import com.example.petner.domain.chat.service.ChatMessageService;
import lombok.RequiredArgsConstructor;
import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Controller
@RequiredArgsConstructor
public class ChatMessageController {

    private final ChatMessageService chatMessageService;

    /**
     * 클라이언트가 /app/chat/{chatRoomId}로 메시지를 보내면 이 메서드가 처리합니다.
     * @param chatRoomId 메시지를 보낼 채팅방 ID
     * @param requestDto 클라이언트가 보낸 메시지 정보 (senderId, content)
     * @return 처리된 메시지 정보. /topic/chat/{chatRoomId}를 구독하는 모든 클라이언트에게 전송됩니다.
     */
    @MessageMapping("/chat/{chatRoomId}")
    @SendTo("/topic/chat/{chatRoomId}")
    public ChatMessageResponseDto sendMessage(
            @DestinationVariable Long chatRoomId,
            ChatMessageRequestDto requestDto
    ) {
        // 서비스 레이어를 호출하여 메시지를 저장하고 필요한 비즈니스 로직을 처리합니다.
        return chatMessageService.saveAndProcessMessage(chatRoomId, requestDto);
    }
}
```

ChatMessageService

메시지 저장, 유효성 검증 등 실제 비즈니스 로직을 수행하는 컴포넌트

컨트롤러로부터 전달받은 데이터를 영속성 계층(DB)에 저장하고, 처리 결과를 컨트롤러에 반환

```java
// ChatMessageService.java
import com.example.petner.domain.chat.dto.request.ChatMessageRequestDto;
import com.example.petner.domain.chat.dto.response.ChatMessageResponseDto;
import com.example.petner.domain.chat.entity.ChatMessage;
import com.example.petner.domain.chat.repository.ChatMessageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class ChatMessageService {

    private final ChatMessageRepository chatMessageRepository;
    // 필요에 따라 ChatRoomRepository, MemberRepository 등을 주입받습니다.

    @Transactional
    public ChatMessageResponseDto saveAndProcessMessage(Long chatRoomId, ChatMessageRequestDto requestDto) {
        // 1. (필요시) 채팅방 존재 여부, 발신자의 채팅방 참여 여부 등 유효성 검증 로직 추가

        // 2. DTO를 Entity로 변환
        ChatMessage chatMessage = ChatMessage.builder()
                .chatRoomId(chatRoomId) // ERD의 Messages.chatRoomId
                .senderId(requestDto.getSenderId()) // ERD의 Messages.senderId
                .content(requestDto.getContent()) // ERD의 Messages.content
                .sendAt(LocalDateTime.now()) // ERD의 Messages.sendAt
                .build();

        // 3. 메시지를 DB에 저장 (영속화)
        ChatMessage savedMessage = chatMessageRepository.save(chatMessage);

        // 4. 저장된 Entity를 Response DTO로 변환하여 반환
        return ChatMessageResponseDto.fromEntity(savedMessage);
    }
}
```

### 5. 실시간 통신 흐름

사용자 관점에서 채팅이 이루어지는 과정은 다음과 같음

연결 수립 (Connect): - 사용자가 채팅방에 입장하면, 클라이언트는 /ws-stomp 엔드포인트로 WebSocket 연결을 요청하여 서버와 영구적인 통신 채널을 생성

구독 (Subscribe): - 연결이 성공하면, 클라이언트는 자신이 입장한 채팅방의 메시지를 받기 위해 /topic/chat/{chatRoomId} 토픽을 구독

메시지 전송 (Send): - 사용자가 메시지를 입력하고 '전송' 버튼을 누르면, 클라이언트는 /app/chat/{chatRoomId} 목적지로 메시지 데이터를 전송(발행)

처리 및 브로드캐스팅 (Process & Broadcast): - 서버는 이 메시지를 받아 DB에 저장한 후, 해당 채팅방을 구독 중인 모든 클라이언트에게 메시지를 실시간으로 전달

### 6. 주요 특징

실시간 양방향 통신: - WebSocket을 기반으로 하여 서버와 클라이언트 간의 지연 시간이 매우 짧은 메시징을 구현

토픽 기반 브로드캐스팅: - STOMP의 토픽 구독 모델을 활용하여, 각 채팅방은 독립적인 메시지 스트림을 가지며 해당 방 참여자에게만 메시지가 전달

메시지 영속화: - 모든 메시지는 Messages 테이블에 저장되어, 사용자가 나중에 채팅방에 다시 접속해도 이전 대화 기록을 확인 가능

유연한 확장성: - Spring Framework의 표준적인 패턴을 따르므로, '읽음 확인', '타이핑 중'과 같은 추가 기능을 구현하기 용이

### 7. 깃허브 링크

https://github.com/Dangdaengdan/PETNER-backend/tree/dev/src/main/java/com/example/petner/domain/chat

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장|[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장]]
- [[blog/JAVA/프로그래머스- 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)|[프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
