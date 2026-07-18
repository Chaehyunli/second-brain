---
title: "[Spring Boot] 2. Flyway 마이그래이션 규칙"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/196
---

# [Spring Boot] 2. Flyway 마이그래이션 규칙

## 원문

https://ch010104.tistory.com/196

## 노트 유형

`guide`

## 적용 목적과 전제조건

문제: 공용 DB(public)의 장부에는 20260210102236 기록이 있는데, 내 로컬 폴더(가방)에는 해당 파일이 없음.

결과: Flyway가 "파일 유실"로 판단하여 서버 구동을 차단(500 에러).

## 구현 절차·검증·주의점

### 1. Flyway 장애 원인 요약 (Post-Mortem)

문제: 공용 DB(public)의 장부에는 20260210102236 기록이 있는데, 내 로컬 폴더(가방)에는 해당 파일이 없음.

결과: Flyway가 "파일 유실"로 판단하여 서버 구동을 차단(500 에러).

교훈: 여러 서버가 하나의 DB를 쓸 때는 방어적 쿼리가 필수이며, 서버별로 이력 테이블을 분리하는 것이 안전함.

### 2. 유형별 방어적 마이그레이션 쿼리 (Best Practices)

### ① 테이블 생성 (Create Table)

테이블이 이미 존재할 경우 에러가 나는 것을 방지합니다.

```sql
-- IF NOT EXISTS 하나로 해결됩니다.
CREATE TABLE IF NOT EXISTS public.tb_por_board_custom_fields ( field_id serial PRIMARY KEY, field_name varchar(100) NOT NULL, required_yn char(1) DEFAULT 'N'
);
```

### ② 컬럼 이름 변경 (Rename Column) - 질문하신 핵심 쿼리

이미 이름이 바뀌어 있거나, 컬럼이 없는 경우에도 에러 없이 실행됩니다.

```sql
DO $$
BEGIN
    -- 1. 변경 전 컬럼(add_col_yn)이 존재하는지 확인
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'tb_por_board_custom_fields'
          AND column_name = 'add_col_yn'
    ) THEN
        -- 2. 조건 만족 시 실제 명령어 실행
        EXECUTE 'ALTER TABLE public.tb_por_board_custom_fields RENAME COLUMN add_col_yn TO required_yn';
    END IF;
END
$$;
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### ③ 컬럼 추가 및 코멘트 (Add Column & Comment)

컬럼이 이미 추가되어 있을 때 중복 추가 에러를 방지합니다.

```sql
DO $$
BEGIN
    -- 1. 추가하려는 컬럼(required_yn)이 없을 때만 실행
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'tb_por_board_custom_fields'
          AND column_name = 'required_yn'
    ) THEN
        ALTER TABLE public.tb_por_board_custom_fields ADD COLUMN required_yn char(1) DEFAULT 'N';
    END IF;

    -- 2. 코멘트 설정 (설명 등록)
    EXECUTE 'COMMENT ON COLUMN public.tb_por_board_custom_fields.required_yn IS ''필수입력여부''';
END
$$;
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 3. 재발 방지를 위한 설정 (application.yml)

4개의 서버가 서로 간섭하지 않게 하려면 서버마다 이력 테이블 이름을 다르게 가져가야 합니다.

```text
spring:
  flyway:
    enabled: true
    # 각 서버별 프로젝트명에 맞춰 테이블 이름을 지정하세요.
    table: flyway_schema_history_judgement
    # 내 가방에 없는 파일이 장부에 있어도 일단 무시하고 실행하는 옵션 (임시방편)
    ignore-missing-migrations: true
    locations: classpath:db/migration
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 4. 용어 최종 정리

DO $$BEGIN...END$$;: "지금부터 복잡한 로직(조건문 등)을 시작할게"라는 신호.

SELECT 1: "내용은 안 궁금하고, 조건에 맞는 데이터가 한 줄이라도 있는지만 알려줘."

EXECUTE: "따옴표 안의 문장을 진짜 SQL 명령어로 바꿔서 실행해."

table_schema: "기본 폴더인 public 구역에서 찾아."

information_schema.columns: "DB 안에 어떤 테이블과 컬럼이 있는지 적혀 있는 시스템 대백과사전."

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
