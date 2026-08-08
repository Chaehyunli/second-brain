---
type: knowledge-inventory
status: verified
created: 2026-08-08
checked_at: 2026-08-08
sources:
  - knowledge/cache-layers-and-invalidation.md
  - knowledge/agent-harness-and-bounded-loops.md
  - knowledge/stateful-ai-service-reliability.md
---

# 초기 Knowledge 후보 탐색 결과

> 2026-08-08 수동 초기화에서 Vault 전체의 재사용 가능한 개념 후보를 상세 대조한 결과다. 원본을 대체하지 않으며, 각 항목은 실제 근거 경로를 가진 Knowledge 노트로 승격했다.

## 탐색 범위

| 기준본 | 점검한 Markdown 수 | 반영 방식 |
| --- | ---: | --- |
| `blog/` | 358 | 카테고리·본문의 반복 개념을 교차 대조 |
| `notion/SKALA/` | 37 | 학습 개념·구조·한계를 대조 |
| `notion/Information/` | 15 | 조사·아키텍처·운영 판단을 대조 |
| `entities/`, `raw/` | 23 | 프로젝트·경력 근거와 측정 한계를 대조 |

## 후보군과 초기 반영

### 웹·백엔드·데이터

- [[knowledge/cache-layers-and-invalidation|캐시 계층·범위·무효화]]
- [[knowledge/transaction-boundary-and-execution-context|트랜잭션 경계와 실행 컨텍스트]]
- [[knowledge/query-planning-index-and-pagination|쿼리 계획·인덱스·페이지네이션]]
- [[knowledge/authentication-state-and-authorization-boundaries|인증 상태와 권한 경계]]
- [[knowledge/blocking-work-in-async-systems|비동기 시스템의 블로킹 작업 격리]]
- [[knowledge/request-response-and-server-events|요청·응답과 서버 주도 이벤트]]
- [[knowledge/resilient-deployment-and-data-infrastructure|복원력 있는 배포·데이터 인프라]]
- [[knowledge/git-flow-ci-cd-and-secret-boundaries|Git 흐름·CI/CD·비밀 경계]]
- [[knowledge/data-store-selection-by-consistency|일관성과 작업 부하에 따른 저장소 선택]]

### AI·데이터·에이전트

- [[knowledge/rag-retrieval-and-data-boundaries|RAG 검색 품질과 데이터 경계]]
- [[knowledge/machine-learning-lifecycle-and-validation|ML 수명주기와 검증 경계]]
- [[knowledge/cold-start-ml-product-boundaries|콜드스타트 ML의 제품 통합 경계]]
- [[knowledge/graph-models-and-dependency-propagation|그래프와 의존성 전파 모델]]
- [[knowledge/agent-harness-and-bounded-loops|Agent Harness와 제한된 자율 루프]]
- [[knowledge/context-engineering-and-tool-grounding|Context Engineering과 도구 근거화]]
- [[knowledge/llm-reliability-and-human-oversight|LLM 신뢰성 경계와 사람 검토]]
- [[knowledge/stateful-ai-service-reliability|상태를 가진 AI 서비스의 신뢰성]]

### 구현 판단·품질

- [[knowledge/typescript-contract-preserving-types|TypeScript 계약 보존형 타입 설계]]
- [[knowledge/performance-investigation-and-measurement-boundaries|성능 조사와 측정 근거 경계]]
- [[knowledge/legacy-characterization-and-team-reproducibility|레거시 특성화 테스트와 팀 재현성]]

## 제외·통합 원칙

- 기존 [[knowledge/vue-application-composition|Vue 애플리케이션 구성]]은 SKALA·Information 후보의 Vue 구조 항목과 중복돼 새로 만들지 않고 유지했다.
- blog·SKALA·Information에서 겹친 인증, RAG, 배포, DB 페이지네이션 후보는 출처를 결합한 하나의 노트로 통합했다.
- 제품별 가격·런타임 제한, 특정 서비스 내부 구현, 합성 데이터 성능, 제한된 조건의 성능 수치는 각 노트의 한계로 남겼다.
