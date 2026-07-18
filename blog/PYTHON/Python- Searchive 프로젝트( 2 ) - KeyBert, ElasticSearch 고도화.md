---
title: "[Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "ElasticSearch", "fastapi", "KeyBert", "Minio", "PostgreSQL", "Python", "searchive"]
category: "PYTHON"
published: 2025-10-11
source_url: https://ch010104.tistory.com/156
---

# [Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화

## 원문

https://ch010104.tistory.com/156

## 노트 유형

`project`

## 배경·목표·적용 맥락

이 시스템은 두 가지 키워드 추출 전략을 상황에 맞게 사용하는 하이브리드(Hybrid) 방식을 채택

Cold Start (초기 단계): 시스템에 데이터가 거의 없을 때는 문맥 이해 능력이 뛰어난 KeyBERT를 사용

## 구현·의사결정·결과

이 시스템은 두 가지 키워드 추출 전략을 상황에 맞게 사용하는 하이브리드(Hybrid) 방식을 채택

Cold Start (초기 단계): 시스템에 데이터가 거의 없을 때는 문맥 이해 능력이 뛰어난 KeyBERT를 사용

Normal (안정 단계): 데이터가 충분히 쌓이면, 전체 문서와 비교하여 통계적으로 중요한 단어를 찾아내는 Elasticsearch의 TF-IDF 방식을 사용해 더 정확한 키워드를 추출

### 1. 필요 라이브러리 (Requirements)

프로젝트 실행에 필요한 핵심 라이브러리 목록

```text
# requirements.txt

# 키워드 추출
keybert
elasticsearch[async]

# 데이터베이스 연동 (재색인 스크립트용)
sqlalchemy[asyncpg] # PostgreSQL 사용 시
alembic

# 기타 (설정, 파일 처리 등)
fastapi
uvicorn
pydantic
python-dotenv
minio
python-multipart
# ... (텍스트 추출 라이브러리: python-magic, pdfplumber 등)
```

### 2. KeyBERT 사용법 (Cold Start 용)

KeyBERT는 BERT 모델을 기반으로 텍스트와 가장 유사한 키워드를 찾아주는 라이브러리

다른 문서와의 비교 없이 단일 문서만으로도 준수한 성능을 보여주므로, 데이터가 적은 초기 단계(Cold Start)에 매우 적합

주요 특징

문맥 기반: 단어의 의미와 문맥을 파악하여 키워드를 추출

독립적 수행: 다른 데이터 없이 텍스트 하나만으로 키워드 추출이 가능

간편한 사용법: 모델을 로드하고 extract_keywords 메소드만 호출

코드 예시 (KeyBERTExtractor)

```python
# keybert 라이브러리 import
from keybert import KeyBERT

class KeyBERTExtractor:
    def __init__(self):
        # 모델은 실제 사용될 때 로드 (Lazy Loading)
        self.model = None

    def _load_model(self):
        """필요할 때 한번만 모델을 로드합니다."""
        if self.model is None:
            self.model = KeyBERT()

    async def extract_keywords(self, text: str) -> List[str]:
        """KeyBERT를 사용하여 키워드를 추출합니다."""
        self._load_model()

        # 주요 파라미터 설명
        keywords_with_scores = self.model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 2),  # 1~2개 단어로 이루어진 구(phrase)까지 키워드로 인정
            stop_words='english',         # 영어 불용어 처리
            top_n=5,                      # 상위 5개 키워드 추출
            use_maxsum=True,              # 키워드 간의 유사도를 낮춰 다양한 키워드 추출
            nr_candidates=20              # 상위 20개 후보 중 가장 좋은 키워드를 선택
        )

        # (키워드, 점수) 형태에서 키워드만 리스트로 반환
        return [kw for kw, score in keywords_with_scores]
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 3. Elasticsearch 사용법 (Normal 단계용)

데이터가 일정량 이상 쌓이면, Elasticsearch의 통계 기반 기능을 활용하는 것이 더 효과적

제공된 코드에서는 TF-IDF(Term Frequency-Inverse Document Frequency) 점수를 계산하여 키워드를 추출

이는 "이 문서에서는 자주 나타나지만, 다른 모든 문서에서는 드물게 나타나는 단어"를 핵심 키워드로 간주하는 방식

3.1. 한글 처리를 위한 Nori 분석기 설정 🇰🇷

정확한 한글 키워드 추출을 위해 Nori 형태소 분석기를 사용

Nori는 문장에서 명사, 동사 등 의미 있는 형태소를 분리하고, 불필요한 조사(은/는, 을/를)나 어미(~다, ~음) 등을 제거하는 역할

Nori 플러그인 설치 (Elasticsearch 서버에서 실행)

```text
cd /usr/share/elasticsearch
bin/elasticsearch-plugin install analysis-nori
sudo systemctl restart elasticsearch
```

Nori 분석기를 적용한 인덱스 설정 코드 예시

```text
# ElasticsearchClient.create_index_if_not_exists() 메소드 내부

index_settings = {
    # "settings" 섹션: 인덱스의 동작 방식과 분석 방법을 정의합니다.
    "settings": {
        # "analysis": 텍스트 분석(토큰화, 필터링 등)에 대한 설정을 포함합니다.
        "analysis": {
            # "analyzer": 텍스트를 어떤 규칙으로 분석할지 정의하는 '분석기' 목록입니다.
            "analyzer": {
                # "korean_nori_analyzer": 우리가 직접 만드는 커스텀 한글 분석기입니다.
                "korean_nori_analyzer": {
                    "type": "custom",  # 기본 제공 분석기가 아닌, 사용자 정의 분석기임을 명시합니다.

                    # "tokenizer": 텍스트를 단어(토큰) 단위로 쪼개는 '토크나이저'를 지정합니다.
                    # "nori_tokenizer"는 한글 형태소 분석기 Nori를 사용하여 문장을 의미있는 최소 단위로 분리합니다.
                    # 예: "엘라스틱서치를" -> "엘라스틱서치", "를"
                    "tokenizer": "nori_tokenizer",

                    # "filter": 쪼개진 토큰들을 추가적으로 가공하는 '필터' 목록입니다. 순서대로 적용됩니다.
                    "filter": [
                        # "nori_pos_filter": 아래에서 정의한 품사(POS) 필터입니다. 불필요한 품사를 제거합니다.
                        "nori_pos_filter",
                        # "lowercase": 모든 토큰을 소문자로 변환합니다. (예: "Apple" -> "apple")
                        "lowercase"
                    ]
                }
            },
            # "filter": 위 analyzer에서 사용할 커스텀 필터를 정의합니다.
            "filter": {
                # "nori_pos_filter": 품사(Part-of-Speech)를 기준으로 토큰을 걸러내는 필터입니다.
                "nori_pos_filter": {
                    "type": "nori_part_of_speech", # Nori 플러그인에서 제공하는 품사 필터 기능을 사용합니다.

                    # "stoptags": 검색에 불필요하다고 판단되는 품사 태그 목록입니다. 여기에 해당하는 토큰은 제거됩니다.
                    # 이 목록 덕분에 검색 색인에 핵심 단어만 남길 수 있습니다.
                    "stoptags": [
                        "J",   # 조사 (은, 는, 이, 가, 을, 를 등)
                        "E",   # 어미 (다, 어, 요, 습니다 등)
                        "XPN", # 접두사
                        "XSA", # 형용사 파생 접미사
                        "XSN", # 명사 파생 접미사
                        "XSV", # 동사 파생 접미사
                        "SF",  # 마침표, 물음표, 느낌표
                        "SP",  # 쉼표, 콜론 등
                        "IC",  # 감탄사
                        "VCP", # 긍정 지정사 (이다)
                        "VCN"  # 부정 지정사 (아니다)
                    ]
                }
            }
        }
    },
    # "mappings" 섹션: 인덱스에 저장될 데이터(필드)의 타입과 속성을 정의합니다. 스키마 정의와 같습니다.
    "mappings": {
        # "properties": 각 필드의 이름과 상세 설정을 정의합니다.
        "properties": {
            # "content" 필드에 대한 설정입니다.
            "content": {
                # "type": "text" -> 전체 텍스트 검색(Full-text search)이 가능한 데이터 타입으로 지정합니다.
                # 이 타입으로 지정해야 위에서 설정한 '분석기'가 적용됩니다.
                "type": "text",

                # "analyzer": "content" 필드를 분석할 때 사용할 분석기를 지정합니다.
                # 위에서 우리가 직접 만든 "korean_nori_analyzer"를 사용하도록 연결합니다.
                "analyzer": "korean_nori_analyzer",

                # "fielddata": True -> 메모리에 필드 데이터를 로드하여 정렬이나 집계(aggregation)에 사용할 수 있도록 합니다.
                # TF-IDF 기반 키워드 추출(Term Vectors API)을 위해서는 이 옵션이 반드시 필요합니다.
                "fielddata": True
            },
            # ... other fields (다른 필드들의 정의가 여기에 들어갑니다)
            # 예: "user_id": {"type": "long"}, "filename": {"type": "keyword"}
        }
    }
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

3.2. TF-IDF 기반 키워드 추출 코드 예시

Elasticsearch의 termvectors API를 사용하여 TF(단어 빈도), DF(문서 빈도) 등의 통계 정보를 얻고, 이를 바탕으로 TF-IDF 점수를 직접 계산하여 키워드를 추출

```python
# ElasticsearchClient.extract_significant_terms() 메소드 내부
import math

async def extract_significant_terms(self, document_id: int, size: int = 5) -> List[str]:
    """TF-IDF 점수를 기반으로 문서의 핵심 키워드를 추출합니다."""

    # 1. Term Vectors API를 호출하여 단어 통계 정보 요청
    tv_response = await self.client.termvectors(
        index=self.index_name,
        id=str(document_id),
        fields=["content"],
        term_statistics=True, # TF-IDF 계산을 위한 전체 단어 통계 포함
        field_statistics=True # DF 계산을 위한 필드 통계 포함
    )

    terms = tv_response["term_vectors"]["content"]["terms"]
    total_docs = tv_response["term_vectors"]["content"]["field_statistics"]["doc_count"]

    term_scores = []
    for term, term_info in terms.items():
        # 2. TF-IDF 점수 계산
        tf = term_info.get("term_freq", 1)
        df = term_info.get("doc_freq", 1)
        idf = math.log((total_docs + 1) / (df + 1)) + 1
        tfidf = tf * idf

        # 단어 길이가 2 이상인 경우만 키워드로 간주
        if len(term) >= 2:
            term_scores.append((term, tfidf))

    # 3. 점수가 높은 순으로 정렬하여 상위 N개 키워드 반환
    term_scores.sort(key=lambda x: x[1], reverse=True)
    return [term for term, score in term_scores[:size]]
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

## 관련 글

- [[blog/PYTHON/index|PYTHON]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert|[Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert]]
- [[blog/PYTHON/Python- Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트|[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
