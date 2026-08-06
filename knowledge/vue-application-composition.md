---
schema_version: 1
id: knowledge-vue-application-composition
title: Vue 애플리케이션 구성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [frontend, vue, javascript, architecture]
sources:
  - notion/SKALA/8-3 Front-framework- Vue.js_Day2/8-3 Front-framework- Vue.js_Day2_핵심 정리.md
  - notion/SKALA/8-4 Front-framework- Vue.js_Day3/8-4 Front-framework- Vue.js_Day3_핵심 정리.md
  - notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리.md
---

# Vue 애플리케이션 구성

## 핵심
Vue 애플리케이션은 컴포넌트 내부 상태와 화면 전환, 서버 통신, 공통 UI를 한 기능으로 섞기보다 역할별 경계를 둔다. Day2의 컴포넌트·Composition API 기반, Day3의 Router·Pinia·HTTP 통신, Day4의 Element Plus 등록은 하나의 앱 진입점에서 조합되지만 각각의 책임은 분리된다.

## 연결된 근거
- [[notion/SKALA/8-3 Front-framework- Vue.js_Day2/8-3 Front-framework- Vue.js_Day2_핵심 정리|Vue Day2]] — 컴포넌트와 Composition API의 기본 단위.
- [[notion/SKALA/8-4 Front-framework- Vue.js_Day3/8-4 Front-framework- Vue.js_Day3_핵심 정리|Vue Day3]] — Router·Pinia·Axios를 통한 화면·상태·통신 분리.
- [[notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리|Vue Day4]] — `app.use(ElementPlus)` 및 CSS import를 통한 공통 UI 등록.

## 적용 기준
- 전역 등록은 애플리케이션 부트스트랩에서 한 번 수행하고, 화면별 기능은 route·store·컴포넌트로 분리한다.
- UI 라이브러리는 공통 컴포넌트와 접근성·반응형 구현을 돕지만, 도메인 상태와 API 오류 정책을 대신 설계하지는 않는다.

## 주의점 또는 한계
이 노트는 SKALA 학습 기준본에서 확인한 구조적 연결이다. 특정 프로젝트가 위 조합을 실제로 채택했다거나, Element Plus가 모든 UI 요구에 적합하다는 결론은 포함하지 않는다.
