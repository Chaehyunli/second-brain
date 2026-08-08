# Knowledge

> 서로 다른 기준본에서 반복되는 개념·판단·작업 원칙을 출처와 함께 연결하는 큐레이션 레이어입니다.

## 역할과 안전선

- `blog/`, `notion/`, `entities/`, `raw/`의 원본·근거 기록을 대체하지 않습니다.
- 원본에서 확인된 사실과, 그 사실을 바탕으로 한 해석을 구분합니다.
- 모든 내용은 `sources`와 본문의 `[[위키링크]]`로 역추적할 수 있어야 합니다.
- 제목 유사도만으로 링크를 만들지 않으며, 사례의 수치·역할·범위를 다른 노트의 일반 사실로 바꾸지 않습니다.

## 적응형 읽기 지도

Knowledge note는 고정 본문 템플릿이 아니라 질문에 맞는 아키타입을 사용합니다. 아래 묶음은 탐색을 위한 지도이며, 각 노트의 제목 순서는 서로 다를 수 있습니다.

### 개념·아키텍처 지도

- [[knowledge/vue-application-composition|Vue 애플리케이션 구성]] — 컴포넌트·Router·Pinia·HTTP·공통 UI의 책임 경계.
- [[knowledge/rag-retrieval-and-data-boundaries|RAG 검색 품질과 데이터 경계]] — 원본, 인덱스, 권한, context의 흐름.
- [[knowledge/agent-harness-and-bounded-loops|Agent Harness와 제한된 자율 루프]] — tool·state·검증·복구의 제어 루프.
- [[knowledge/python-analysis-and-service-boundaries|Python의 분석 실험과 서비스 통합 경계]] — 분석 실험·재현성과 FastAPI 서비스 통합의 경계.

### 선택·비교 가이드

- [[knowledge/data-store-selection-by-consistency|데이터 저장소 선택]] — 일관성·작업 부하·운영 요구의 역할 분리.
- [[knowledge/query-planning-index-and-pagination|쿼리 계획·인덱스·페이지네이션]] — query shape와 접근 경로 선택.
- [[knowledge/request-response-and-server-events|요청·응답과 서버 주도 이벤트]] — 통신 방향·연결 수명·전달 요구의 선택.
- [[knowledge/typescript-contract-preserving-types|TypeScript 계약 보존형 타입 설계]] — 정보 보존과 타입 복잡도의 trade-off.

### 절차·문제 해결 패턴

- [[knowledge/performance-investigation-and-measurement-boundaries|성능 조사와 측정 근거 경계]]
- [[knowledge/legacy-characterization-and-team-reproducibility|레거시 특성화 테스트와 팀 재현성]]
- [[knowledge/blocking-work-in-async-systems|비동기 시스템의 블로킹 작업 격리]]
- [[knowledge/cache-layers-and-invalidation|캐시 계층·범위·무효화 전략]]
- [[knowledge/transaction-boundary-and-execution-context|트랜잭션 경계와 실행 컨텍스트]]

### 근거 프레임워크·사례 종합

- [[knowledge/evidence-grounded-portfolio-narrative|근거 기반 포트폴리오 서사]]
- [[knowledge/source-to-public-technical-writing|기준본에서 공개 기술 글로 전개하는 방법]]
- [[knowledge/cold-start-ml-product-boundaries|콜드스타트 ML의 제품 통합 경계]]
- [[knowledge/stateful-ai-service-reliability|상태를 가진 AI 서비스의 신뢰성]]
- [[knowledge/llm-reliability-and-human-oversight|LLM 신뢰성 경계와 사람 검토]]
- [[knowledge/machine-learning-lifecycle-and-validation|ML 수명주기와 검증 경계]]

### 운영·인프라와 모델 비교

- [[knowledge/authentication-state-and-authorization-boundaries|인증 상태와 권한 경계]]
- [[knowledge/git-flow-ci-cd-and-secret-boundaries|Git 흐름·CI/CD·비밀 경계]]
- [[knowledge/resilient-deployment-and-data-infrastructure|복원력 있는 배포·데이터 인프라]]
- [[knowledge/graph-models-and-dependency-propagation|그래프와 의존성 전파 모델]]

## 운영

- 매일 00:15 KST: Hermes Knowledge Curator가 새 원본의 교차 출처 후보를 탐색합니다.
- 매주 일요일 00:20 KST: 읽기 중심 건강검진 후, 명백한 출처·링크 보완만 안전하게 반영합니다.
- 개인 결론, 포트폴리오 주장, Inbox 승격, 해석이 필요한 새 문서는 사용자 검토·승인을 거칩니다.
- [[knowledge/INITIAL_CANDIDATE_INVENTORY|2026-08-08 초기 후보 탐색 결과]]는 후보 탐색의 범위·통합 기준을 보존합니다.
