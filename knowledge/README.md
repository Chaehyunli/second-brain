# Knowledge

> 서로 다른 기준본에서 반복되는 개념·판단·작업 원칙을 출처와 함께 연결하는 큐레이션 레이어입니다.

## 역할

- `blog/`, `notion/`, `entities/`, `raw/`의 원본·근거 기록을 대체하지 않습니다.
- 원본에서 확인된 사실과, 그 사실을 바탕으로 한 재사용 가능한 해석을 구분합니다.
- 모든 내용은 `sources`와 본문의 `[[위키링크]]`로 역추적할 수 있어야 합니다.

## 운영

- 매일 00:15 KST: Hermes Knowledge Curator가 새 원본의 교차 출처 후보를 탐색합니다.
- 매주 일요일 00:20 KST: 읽기 중심 건강검진 후, 명백한 출처·링크 보완만 안전하게 반영합니다.
- 개인 결론, 포트폴리오 주장, Inbox 승격, 해석이 필요한 새 문서는 사용자 검토·승인을 거칩니다.

## 초기 지식 지도

- [[knowledge/INITIAL_CANDIDATE_INVENTORY|2026-08-08 초기 후보 탐색 결과]] — 358개 블로그, SKALA·Information, 프로젝트 근거를 대조한 범위·통합 기준
- [[knowledge/vue-application-composition|Vue 애플리케이션 구성]]
- [[knowledge/source-to-public-technical-writing|기준본에서 공개 기술 글로 전개하는 방법]]
- [[knowledge/evidence-grounded-portfolio-narrative|근거 기반 포트폴리오 서사]]

### 핵심 주제 묶음

- 백엔드·데이터: [[knowledge/cache-layers-and-invalidation|캐시]], [[knowledge/transaction-boundary-and-execution-context|트랜잭션]], [[knowledge/query-planning-index-and-pagination|쿼리 계획]], [[knowledge/authentication-state-and-authorization-boundaries|인증·권한]], [[knowledge/resilient-deployment-and-data-infrastructure|배포·인프라]]
- AI·에이전트: [[knowledge/rag-retrieval-and-data-boundaries|RAG]], [[knowledge/agent-harness-and-bounded-loops|Agent Harness]], [[knowledge/context-engineering-and-tool-grounding|Context Engineering]], [[knowledge/llm-reliability-and-human-oversight|LLM 신뢰성]]
- 프로젝트 판단: [[knowledge/stateful-ai-service-reliability|상태형 AI 서비스]], [[knowledge/performance-investigation-and-measurement-boundaries|성능 근거]], [[knowledge/legacy-characterization-and-team-reproducibility|특성화 테스트·재현성]]
