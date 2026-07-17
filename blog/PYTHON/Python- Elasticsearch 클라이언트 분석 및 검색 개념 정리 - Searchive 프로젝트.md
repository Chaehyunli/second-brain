---
title: "[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "ElasticSearch", "Python"]
category: "PYTHON"
published: 2026-03-28
source_url: https://ch010104.tistory.com/245
---

# [Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트

## 원문

https://ch010104.tistory.com/245

## 노트 유형

`project`

## 배경·목표·적용 맥락

엘라스틱서치에서 bool 쿼리는 여러 조건을 조합할 때 사용하며, 4가지 핵심 인자를 가집니다.

"삼성 노트북 중에서 100만원 이하이거나 리뷰 점수가 높은 상품을 검색 (단, 품절 상품은 제외)"

## 구현·의사결정·결과

### 1. 엘라스틱서치 핵심 쿼리 개념 (Query DSL)

엘라스틱서치에서 bool 쿼리는 여러 조건을 조합할 때 사용하며, 4가지 핵심 인자를 가집니다.

### 예시 코드 (쇼핑몰 검색 시나리오)

"삼성 노트북 중에서 100만원 이하이거나 리뷰 점수가 높은 상품을 검색 (단, 품절 상품은 제외)"

```text
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name": "삼성" } }
      ],
      "filter": [
        { "range": { "price": { "lte": 1000000 } } },
        { "term": { "status": "on_sale" } }
      ],
      "should": [
        { "match": { "category": "노트북" } },
        { "range": { "review_score": { "gte": 4.5 } } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

### 각 항목의 의미

must (반드시 포함): 조건이 반드시 참이어야 하며 점수 계산에 반영됩니다.

filter (예/아니오 거르기): 참인 문서만 포함하되 점수 계산은 하지 않아 성능이 매우 빠릅니다.

should (가점 요인): 일치하면 점수가 높아져 상단에 노출됩니다.

minimum_should_match (최소 만족 개수): should 조건 중 최소 몇 개가 일치해야 하는지 지정합니다.

### 2. 인덱스 설정 분석 (Nori 및 인프라 설정)

프로젝트의 create_index_if_not_exists 메서드에 구현된 설정입니다.

### Nori 분석기 & stoptags (한국어 처리)

한국어의 특성상 '조사'나 '어미'는 의미 추출에 방해가 됩니다. 이를 위해 Nori 분석기와 품사 필터를 사용합니다.

```text
# 프로젝트 코드 예시: Nori 및 품사 필터 설정
index_settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "korean_nori_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_tokenizer", # 형태소 분석 기계
                    "filter": ["nori_pos_filter", "lowercase"]
                }
            },
            "filter": {
                "nori_pos_filter": {
                    "type": "nori_part_of_speech",
                    "stoptags": ["J", "E", "IC", "MAG", "MM"] # 조사(J), 어미(E) 등을 제거
                }
            }
        }
    }
}
```

이유: "사과가", "사과는"에서 핵심은 '사과'입니다. stoptags로 조사를 지워야 정확한 키워드 추출이 가능해집니다.

### Shards & Replicas (인프라 최적화)

```bash
"number_of_shards": 1,   # 데이터를 1개의 조각으로 저장
"number_of_replicas": 0  # 복사본을 만들지 않음 (단일 노드 Docker 환경 최적화)
```

Shards: 데이터 분산 저장 단위입니다. 로컬/테스트 환경에서는 1개면 충분합니다.

Replicas: 데이터 유실 방지용 복사본입니다. 노드가 1개뿐인 Docker 환경에서는 0으로 설정해야 상태가 'Green'으로 유지됩니다.

### 3. 태그 추출 로직 단계별 정리 (extract_significant_terms)

문서에서 핵심 키워드를 수학적으로 뽑아내는 과정입니다.

### [Step 1] Term Vectors 데이터 획득

엘라스틱서치로부터 문서 내 단어 통계를 가져옵니다. 이때 이미 조사가 제거된 상태입니다.

### [Step 2] TF-IDF 수학적 점수 계산

프로젝트 코드에서 직접 구현된 핵심 로직입니다.

```text
# 프로젝트 코드 예시: TF-IDF 계산 부분
for term, term_info in terms.items():
    # 1. TF (Term Frequency): 이 문서 내 등장 횟수
    tf = term_info.get("term_freq", 1)

    # 2. DF (Document Frequency): 전체 시스템 내 등장 문서 수
    df = term_info.get("doc_freq", 1)

    # 3. IDF (Inverse Document Frequency): 희귀성 가중치
    total_docs = tv_response["term_vectors"]["content"]["field_statistics"]["doc_count"]
    idf = math.log((total_docs + 1) / (df + 1)) + 1

    # 4. 최종 점수 산출
    tfidf = tf * idf
```

TF (내부 인기): 한 문서에 많이 나올수록 중요합니다.

IDF (희귀성): '내용', '참고'처럼 모든 문서에 다 나오는 단어는 점수를 낮추고, '반도체'처럼 특정 문서에만 나오는 단어는 점수를 높입니다.

공식: Score = TF * IDF

### [Step 3] 필터링 및 결과 반환

```text
# 단어 길이 필터 (2자 미만은 '이', '가' 등이 남았을 경우를 대비해 제외)
if 2 <= len(term) <= 30:
    term_scores.append((term, tfidf))

# 점수 순 정렬 후 상위 N개 추출
term_scores.sort(key=lambda x: x[1], reverse=True)
keywords = [term for term, score in term_scores[:size]]
```

## 관련 글

- [[blog/PYTHON/index|PYTHON]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화|[Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert|[Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert]]
- [[blog/CODINGTEST/코딩테스트- 현대오토 2026-04-05 회고|[코딩테스트] 현대오토 2026-04-05 회고]]
