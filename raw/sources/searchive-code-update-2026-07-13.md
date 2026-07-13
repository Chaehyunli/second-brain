---
source_url:
  - https://github.com/Searchive-Project/Searchive-backend/commit/4b8b63e7bf733e6a61de2e3871e604bc828f8e0c
  - https://github.com/Searchive-Project/Searchive-backend/commit/2b500fe31c9a23d009caf297125a4bc6e53d0498
  - https://github.com/Searchive-Project/Searchive-backend/commit/924cf47decdc5970645f254cb6eb02f6062dd6f2
ingested: 2026-07-13
repository: Searchive-Project/Searchive-backend
branch: main
---

# Searchive 코드 업데이트 근거 — 2026-07-13

## 확인 범위

`main`의 다음 3개 커밋과 변경된 소스 파일을 직접 검토했다.

- `4b8b63e` — 동시 요청의 임베딩 모델 초기화 보호: `EmbeddingService`의 lazy loading에 `threading.Lock`과 이중 확인을 추가했다. 다중 worker가 SentenceTransformer를 동시에 초기화할 때의 meta tensor 오류를 막는 변경이다.
- `2b500fe` — KeyBERT 키워드 추출 지연 제거: short TXT fixture에서 70초 이상 지연된 `use_maxsum=True`를 기본 ranking으로 바꿨다. 커밋 내 관찰 기준으로 동등한 후보 키워드를 1초 미만에 반환한다고 기록한다.
- `924cf47` — 문서 기반 AI 응답 컨텍스트 보강: AI 답변 온도를 0.25로 낮추고, 벡터 검색 결과가 없더라도 연결 문서의 파일명·저장 요약을 fallback context로 LLM에 전달한다. 문서 컨텍스트가 없는 경우에는 근거 부재를 명시하도록 시스템 지침을 정비했다.

## 검증 경계

이 근거는 커밋 diff와 현재 `main` 소스 검토에 기반한다. 모델 동시 초기화, KeyBERT 실제 추론 시간, RAG fallback의 end-to-end 재현 테스트는 이 아카이브 작업에서 별도로 실행하지 않았다.
