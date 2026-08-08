---
schema_version: 1
id: knowledge-vue-application-composition
title: Vue 애플리케이션 구성
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [frontend, vue, javascript, architecture]
sources:
  - notion/SKALA/8-3 Front-framework- Vue.js_Day2/8-3 Front-framework- Vue.js_Day2_핵심 정리.md
  - notion/SKALA/8-4 Front-framework- Vue.js_Day3/8-4 Front-framework- Vue.js_Day3_핵심 정리.md
  - notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리.md
---

# Vue 애플리케이션 구성

## 설계 질문
컴포넌트 내부 상태, 화면 전환, 전역 상태, 서버 통신, 공통 UI를 어디에서 조합하고 어디까지 분리할 것인가?

## 책임 경계
Day2는 컴포넌트·Composition API를 기능 단위의 상태와 로직으로, Day3는 Router·Pinia·Axios를 화면·공유 상태·통신으로 분리한다.

## 조합 지점: 애플리케이션 부트스트랩
Day4의 `app.use(ElementPlus)`와 CSS import는 공통 UI를 앱 진입점에서 등록하는 예다. 전역 등록은 한 번 수행하되 화면별 도메인 기능까지 전역으로 몰지 않는다.

## 경계를 넘는 규칙
route는 화면 이동, store는 공유 상태, component는 지역 UI, HTTP 계층은 서버 통신을 담당한다. 오류 정책과 도메인 상태는 UI 라이브러리가 대신 설계하지 않는다.

## 확인한 근거와 적용하지 않는 주장
[[knowledge/source-to-public-technical-writing]]은 이 기준본의 공개 글 파생 관계를 다룬다. 이 노트는 학습 자료의 구조 연결이며 특정 프로젝트가 이 조합을 채택했다거나 Element Plus가 모든 요구에 맞는다는 주장은 아니다.

## 출처
- [[notion/SKALA/8-3 Front-framework- Vue.js_Day2/8-3 Front-framework- Vue.js_Day2_핵심 정리]]
- [[notion/SKALA/8-4 Front-framework- Vue.js_Day3/8-4 Front-framework- Vue.js_Day3_핵심 정리]]
- [[notion/SKALA/8-5 Front-framework- Vue.js_Day4/8-5 Front-framework- Vue.js_Day4_핵심 정리]]
