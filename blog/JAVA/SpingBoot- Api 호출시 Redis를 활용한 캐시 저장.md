---
title: "[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cache", "java", "springboot"]
category: "JAVA"
published: 2025-04-04
source_url: https://ch010104.tistory.com/44
---

# [SpingBoot] Api 호출시 Redis를 활용한 캐시 저장

## 원문

https://ch010104.tistory.com/44

## 노트 유형

`guide`

## 적용 목적과 전제조건

백엔드에서는 controller에서 Api를 호출하면, service에서 이를 처리해서 반환함.

자주 호출하는 Api의 경우, 결과를 미리 다른 곳에 저장해 놓으면, 이 후에 같은 Api를 호출했을 때, 데이터베이스를 조회하지 않고 저장소에서 가져다 쓰면 되지 않을까??

## 구현 절차·검증·주의점

백엔드에서는 controller에서 Api를 호출하면, service에서 이를 처리해서 반환함.

자주 호출하는 Api의 경우, 결과를 미리 다른 곳에 저장해 놓으면, 이 후에 같은 Api를 호출했을 때, 데이터베이스를 조회하지 않고 저장소에서 가져다 쓰면 되지 않을까??

이는 Redis를 사용하여 key와 value의 형식으로 값을 저장해 놓음으로서 가능

만약, 동아리 목록을 호출하는 Api가 있다면 Redis를 사용하여 데이터베이스 조회 수를 줄일 수 있음.(Cacheable)

하지만, 동아리가 삭제가 되거나, 추가될 경우에 기존에 Redis에 저장된 정보가 최신의 정보를 반영하지 못하므로 삭제가 필요( CacheEvict )

### 1. Redis 캐시 설정

캐시를 설정하기 위해 CacheConfig 클래스를 생성하고, Redis 캐시 매니저를 설정

```java
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public RedisCacheConfiguration redisCacheConfiguration() {
        return RedisCacheConfiguration.defaultCacheConfig()
                .entryTtl(Duration.ofMinutes(10))  // TTL 10분 설정
                .disableCachingNullValues()
                .serializeValuesWith(
                    RedisSerializationContext.SerializationPair.fromSerializer(new GenericJackson2JsonRedisSerializer())
                );
    }
}
```

위 설정은 캐시의 TTL(Time To Live)을 10분으로 설정하고, null 값을 캐싱하지 않도록 함.

GenericJackson2JsonRedisSerializer를 사용하여 값을 직렬화

### 2. 캐시 적용 예시 – 동아리 목록

사용자 대학교 기반 동아리 리스트 캐싱

사용자의 대학교 ID를 기반으로 동아리 목록을 캐싱하는 방법(사용자 이름을 기반으로 하면, 사용자마다 캐시 생성)

```java
@Service
public class ClubServiceImpl implements ClubService {

    private final UserRepository userRepository;
    private final ClubRepository clubRepository;

    public ClubServiceImpl(UserRepository userRepository, ClubRepository clubRepository) {
        this.userRepository = userRepository;
        this.clubRepository = clubRepository;
    }

    @Cacheable(
        value = "clubListByUniversity",
        key = "T(String).valueOf(@userRepository.findByUsername(#username).orElseThrow().universityId) + ':' + #limit + ':' + #offset"
    )
    @Override
    @Transactional(readOnly = true)
    public ClubListResponseDto getClubsByUserUniversity(String username, int limit, int offset) {
        // 1. 현재 로그인한 사용자 찾기
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new IllegalArgumentException("사용자를 찾을 수 없습니다."));

        // 2. 해당 사용자의 대학교 ID로 필터링하여 동아리 조회
        List<Club> clubs = clubRepository.findByUniversity_UniversityId(user.getUniversityId());

        // 전체 동아리 개수
        int total = clubs.size();

        // 3. 페이지네이션 적용
        List<Club> paginatedClubs = clubs.stream()
                .skip(offset)
                .limit(limit)
                .collect(Collectors.toList());

        // 4. DTO 변환 후 반환
        return ClubListResponseDto.fromEntity(paginatedClubs, total, limit, offset);
    }
}
```

@Cacheable 어노테이션의 key 속성은 SpEL(Spring Expression Language)을 사용하여 캐시 키를 생성

@userRepository.findByUsername(#username).orElseThrow().universityId를 통해 사용자의 대학교 ID를 가져와서 캐시 키의 일부로 사용(UserRepository에서 이름을 userRepository로 설정 필요)

이는 동일한 대학교의 사용자들이 동일한 동아리 목록 캐시를 공유

### 3. 캐시 삭제 (Evict)

동아리 생성, 삭제, 썸네일 변경 등 동아리 목록에 변동이 생길 때 해당 캐시를 삭제하여 최신 데이터를 유지

```text
@CacheEvict(value = "clubListByUniversity", allEntries = true)
public Long createClub(ClubDto clubDto) {
    // 동아리 생성 로직
}
```

@CacheEvict 어노테이션의 allEntries = true 속성을 사용하여 clubListByUniversity 캐시의 모든 엔트리를 삭제

### 4. 캐시 만료 방식

캐시는 설정된 TTL에 따라 자동으로 만료됨

위의 CacheConfig 클래스에서 TTL을 10분으로 설정하였으므로, 캐시에 저장된 데이터는 10분 후 자동으로 삭제

```text
time-to-live: 600000  # 600,000ms = 10분
```

10분 후에는 캐시가 만료되고, 해당 메서드가 다시 실행되어 새로운 데이터로 캐시가 갱신됨.

### 5. 캐시 키 확인 및 삭제 (Redis CLI)

프로젝트 터미널에서 redis 서버 실행

```text
redis-cli
```

1) 키 전체 조회

Redis CLI를 사용하여 현재 저장된 모든 키를 조회 가능

Api 호출 후에 키 조회를 통해, 캐시가 저장되었는지 확인 가능(이후 호출에선, 로그를 통해서 redis에서 데이터를 가져오는 것을 확인 가능)

이는 bash에서 "redis-cli" 명령어를 사용하여 redis 서버 실행 후에 가능(시스템 환경 변수 설정 필요)

```text
keys '*'
```

2) 특정 키 삭제

특정 키를 삭제하여 해당 캐시를 무효화

```text
del 'clubListByUniversity::6:12:0'
```

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/Spring Boot- Websocket + STOMP를 이용한 세션 기반 채팅|[Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅]]
- [[blog/JAVA/프로그래머스- 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)|[프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
