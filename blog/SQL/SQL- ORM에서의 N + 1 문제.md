---
title: "[SQL] ORM에서의 N + 1 문제"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Database", "SQL"]
category: "SQL"
published: 2026-06-25
source_url: https://ch010104.tistory.com/286
---

# [SQL] ORM에서의 N + 1 문제

## 원문

https://ch010104.tistory.com/286

## 노트 유형

`guide`

## 적용 목적과 전제조건

실무의 대원칙은 모든 연관 관계를 LAZY(지연 로딩)로 설정하는 것입니다. 1:N 관계인 게시글(Post)과 댓글(Comment) 엔티티를 예시로 구현합니다.

모든 연관 관계를 LAZY로 잘 막았지만, 전체 게시글을 조회한 뒤 각 게시글의 댓글을 읽어오는 로직을 실행할 때 $N+1$ 문제가 터집니다.

## 구현 절차·검증·주의점

### 📌 1. 전체 흐름 요약

```text
[EAGER (즉시 로딩)] -> 예측 불가능한 조인으로 성능 폭탄 발생 (실무 사용 금지)
       ↓
[LAZY (지연 로딩)]  -> 필요한 순간에만 조회하여 안전하지만, 루프를 돌 때 N+1 문제 발생
       ↓
[N+1 문제 해결책 선택]
  ├── 페이징 필요 X  -->  [Fetch Join] 사용 (SQL JOIN으로 한 방에 조회, 쿼리 1번)
  └── 페이징 필요 O  -->  [Batch Size (IN 절)] 사용 (SQL IN으로 묶어서 조회, 쿼리 2번)
```

### 💻 2. 실무 기본 세팅: 엔티티 설계 (LAZY)

실무의 대원칙은 모든 연관 관계를 LAZY(지연 로딩)로 설정하는 것입니다. 1:N 관계인 게시글(Post)과 댓글(Comment) 엔티티를 예시로 구현합니다.

### 게시글 엔티티 (Post.java)

```java
@Entity
@Getter @Setter
public class Post {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    // 1대N 관계는 기본값이 LAZY가 아니므로 반드시 명시해 줍니다.
    @OneToMany(mappedBy = "post", fetch = FetchType.LAZY)
    private List<Comment> comments = new ArrayList<>();
}
```

### 댓글 엔티티 (Comment.java)

```java
@Entity
@Getter @Setter
public class Comment {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String content;

    // N대1 관계는 기본값이 EAGER이므로 반드시 LAZY로 변경해야 합니다.
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id")
    private Post post;
}
```

### 🚨 3. N+1 문제의 발생 (Before)

모든 연관 관계를 LAZY로 잘 막았지만, 전체 게시글을 조회한 뒤 각 게시글의 댓글을 읽어오는 로직을 실행할 때 $N+1$ 문제가 터집니다.

### 서비스 코드 (PostService.java)

```text
@Transactional(readOnly = true)
public void printAllComments() {
    // 1. 게시글 전체 조회 (쿼리 1번 실행)
    List<Post> posts = postRepository.findAll();

    // 2. 루프를 돌며 각 게시글의 댓글에 접근 (N번 쿼리 실행)
    for (Post post : posts) {
        // 이 시점에 LAZY 로딩이 발동하여 DB에 댓글 데이터를 요청합니다.
        int commentSize = post.getComments().size();
        System.out.println("게시글 제목: " + post.getTitle() + ", 댓글 수: " + commentSize);
    }
}
```

### ❌ 실제 실행되는 SQL 로그 (N+1 발생)

게시글이 총 3개(ID: 10, 11, 12)가 있다고 가정하면, DB에 총 4번(1 + 3)의 요청이 날아갑니다.

```sql
-- 1. findAll() 메서드 호출로 게시글 조회 (1번)
SELECT * FROM post;

-- 2. 루프를 돌며 각 post의 id로 comment 테이블 개별 조회 (3번 / N번)
SELECT * FROM comment WHERE post_id = 10; -- 1번째 게시글의 댓글 조회
SELECT * FROM comment WHERE post_id = 11; -- 2번째 게시글의 댓글 조회
SELECT * FROM comment WHERE post_id = 12; -- 3번째 게시글의 댓글 조회
```

### 🛠️ 4. 해결책 1: Fetch Join (페이징이 필요 없을 때)

가장 직관적이고 빠른 해결책입니다. SQL의 JOIN을 사용하여 처음부터 게시글과 댓글을 한 방에 긁어옵니다.

### 리포지토리 코드 (PostRepository.java)

```sql
public interface PostRepository extends JpaRepository<Post, Long> {

    // fetch 키워드를 사용하여 연관된 자식 엔티티까지 한 번에 조인 조회합니다.
    @Query("select p from Post p join fetch p.comments")
    List<Post> findAllWithComments();
}
```

### ⭕ 실제 실행되는 SQL 로그 (쿼리 딱 1번)

```sql
SELECT p.*, c.*
FROM post p
INNER JOIN comment c
ON p.id = c.post_id;

또는

SELECT p.*, c.*
FROM comment c            -- 1. 중심 테이블을 comment로 잡고
INNER JOIN post p         -- 2. 거기에 post를 내부 조인으로 붙인다!
ON c.post_id = p.id       -- 3. 조건은 동일
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

장점: 단 1번의 쿼리로 모든 데이터를 가져오므로 성능상 가장 빠릅니다.

단점(한계): 1:N 관계에서 사용할 경우, 데이터가 댓글 수만큼 뻥튀기(중복 생성)되어 데이터베이스 레벨의 페이징(LIMIT, OFFSET)이 불가능해집니다. (JPA가 페이징을 시도하면 데이터를 메모리에 전부 올린 뒤 처리하므로 서버가 폭발할 수 있습니다.)

### 🛠️ 5. 해결책 2: Batch Size / SQL IN 절 (페이징이 필요할 때)

1:N 관계에서 페이징을 안전하게 처리하면서 N+1 문제를 방어하고 싶을 때 사용하는 실무 최적화의 정석입니다. SQL의 IN 연산자를 활용합니다.

### 방법 A. 글로벌 설정 (가장 권장)

application.yml 파일에 설정해 두면 전체 프로젝트에 자동 적용됩니다.

```text
spring:
  jpa:
    properties:
      hibernate:
        default_batch_fetch_size: 100 # IN 절에 한 번에 넣을 ID 최대 개수
```

### 방법 B. 특정 연관관계에만 설정

```text
@OneToMany(mappedBy = "post", fetch = FetchType.LAZY)
@BatchSize(size = 100) // 100개씩 묶어서 IN 쿼리 실행
private List<Comment> comments = new ArrayList<>();
```

### ⭕ 실제 실행되는 SQL 로그 (쿼리 딱 2번)

페이징을 적용해 게시글 3개(ID: 10, 11, 12)만 먼저 정상적으로 가져온 뒤, 설정한 Batch Size만큼 IN 절로 댓글을 모아서 가져옵니다.

```sql
-- 1단계: 게시글을 먼저 페이징 처리하여 정상 조회 (1번)
SELECT * FROM post LIMIT 3;

-- 2단계: 가져온 게시글의 ID들을 모아 IN 절로 댓글 한 번에 조회 (1번)
SELECT * FROM comment
WHERE post_id IN (10, 11, 12);
```

장점: 1:N 관계에서도 데이터 뻥튀기가 없으므로 안전하게 페이징을 처리할 수 있습니다. 쿼리도 전체 데이터 개수와 상관없이 딱 2번(1 + 1)만 수행됩니다.

단점: Fetch Join처럼 쿼리 1번으로 끝내는 것보다는 물리적인 쿼리 횟수가 1번 더 많습니다. (하지만 실무 성능상 거의 미미한 차이입니다.)

### 💡 최종 실무 선택 가이드

N:1 이나 1:1 관계 (예: 댓글 -> 게시글, 게시글 -> 작성자)

데이터가 뻥튀기되지 않으므로, 페이징 여부와 상관없이 Fetch Join을 적극적으로 사용합니다.

1:N 관계 (예: 게시글 -> 댓글, 카테고리 -> 상품 목록)

페이징이 필요 없다면 ➡️ Fetch Join

페이징이 필요하다면 ➡️ 기본적으로 LAZY 로딩을 유지한 상태에서 default_batch_fetch_size (IN 절) 옵션으로 방어

## 관련 글

- [[blog/SQL/index|SQL]]
- [[blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX|[SQL] MySql의 인덱스 설정 - BTREE INDEX]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜젝션과 Serializability|[데이터베이스 설계] 트랜젝션과 Serializability]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
