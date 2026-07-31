---
title: "[7/31] Front-framework: Vue.js_Day1_핵심 정리"
notion_page_id: "3ad1d84b-f68e-80ef-a38b-fb4191b0d1c1"
source_url: "https://app.notion.com/p/3ad1d84bf68e80efa38bfb4191b0d1c1"
synced_at: "2026-08-01T00:08:46+09:00"
content_sha256: "5fa8ea00b470c5e0b003c9e7deedb6e24613dc73a5bad4741336e241301a12eb"
tags: [notion, skala, learning, vue, frontend]
---

# [7/31] Front-framework: Vue.js_Day1_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3ad1d84bf68e80efa38bfb4191b0d1c1) (2026-07-31 확인)

### Vue.js 개요
Vue.js는 사용자 인터페이스(UI) 구축을 목적으로 하는 Front-end JavaScript Framework임. JavaScript와 TypeScript를 모두 지원하며, 간결한 문법·반응형 데이터 바인딩·컴포넌트 기반 구조·가상 DOM·트랜지션 효과 지원이 주요 특징임.
유사한 프레임워크로 React·Angular가 있으나, Vue는 그 중 가장 가볍고 진입 장벽이 낮은 편임.
#### JavaScript vs. TypeScript
| 구분 | JavaScript | TypeScript |
| --- | --- | --- |
| 정의 | 웹의 기본 스크립트 언어 | JavaScript에 정적 타입을 추가한 상위 집합(Superset) |
| 타입 시스템 | 동적 타이핑 — 런타임에 변수 타입 결정 | 정적 타이핑 — 컴파일 타임에 변수 타입 명시 및 검증 |
| 에러 발견 시점 | 런타임(코드 실행 도중) | 컴파일 타임(코드 작성·빌드 단계) |
| 실행 방식 | 브라우저·Node.js에서 직접 해석·실행 | 브라우저 직접 실행 불가; JS로 트랜스파일 후 실행 |
| 생산성 & DX | 소규모 프로젝트·빠른 프로토타이핑에 유리 | 대규모 프로젝트, 자동 완성·리팩토링·코드 가독성에 유리 |
Vue 버전별 언어 선택 정리:
- Vue 2: 핵심 코드가 JavaScript로 작성됨
- Vue 3: 코어 엔진이 100% TypeScript로 전면 재작성됨
- Vue 2·3 모두 개발자가 프로젝트 단위로 JavaScript 또는 TypeScript를 선택해 사용 가능함
---
### Vue.js 아키텍처 — MVVM
Vue.js는 MVVM(Model-View-ViewModel) 아키텍처 패턴을 따름. MVVM은 UI를 담당하는 View와 데이터를 처리하는 Model 사이에 ViewModel을 두어, 화면 렌더링 로직과 데이터 처리 로직을 완전히 분리하는 구조임.
![]()
#### 세 레이어의 역할
| 레이어 | 담당 영역 | Vue에서의 위치 |
| --- | --- | --- |
| Model | 순수 비즈니스 데이터 — `ref`·`reactive`의 원본 데이터 또는 Backend REST API 응답값 | `<script>` 내부의 JavaScript 객체 |
| View | 사용자에게 실제로 보여지는 화면 — DOM 구조와 시각적 스타일링 | `<template>`, `<style>` 영역 |
| ViewModel | View·Model 사이의 중재자 — DOM Listeners(이벤트 감지)와 Data Bindings로 데이터 중개 | Vue.js 엔진 + `<script>` |
#### 동작 흐름
- View에서 사용자 이벤트 발생 → ViewModel의 DOM Listeners가 감지 → Model 업데이트
- Model 데이터 변경 → ViewModel의 Data Bindings가 반영 → View(DOM) 자동 갱신
- 이 쌍방향 연동 덕분에 개발자는 DOM 조작 코드 없이 데이터 상태만 관리하면 됨
---
### Frontend Framework 3대장 비교
현재 프론트엔드 생태계의 주요 UI 프레임워크·라이브러리는 Vue.js, React, Angular 세 가지임.
| 항목 | Vue.js | React | Angular |
| --- | --- | --- | --- |
| 출시연도 | 2014년 | 2013년 | 2010년 |
| 개발 주체 | Evan You (커뮤니티 주도) | Meta (구 Facebook) | Google |
| 기술 분류 | 점진적 프레임워크 | UI 라이브러리 | 풀스택 프레임워크 |
| 개발 언어 | JavaScript, TypeScript | JavaScript, TypeScript 지원 | TypeScript 필수 |
| 학습 곡선 | 낮음 | 중간 | 높음 |
| 크기 | 약 33KB | 약 42KB | 약 500KB |
| 주요 특징 | Virtual DOM, 양방향 데이터 바인딩(v-model), 컴포넌트 기반 | Virtual DOM, 단방향 데이터 흐름, Hooks 지원 | 실제 DOM 사용, 양방향 데이터 바인딩, 종속성 주입 |
| 렌더링 방식 | CSR, SSR 지원 | CSR, SSR 지원 | CSR, SSR 지원 |
---
#### DOM이란
DOM(Document Object Model)은 브라우저가 HTML 문서를 파싱한 뒤 메모리에 만드는 트리 구조의 객체 모델임. `<html>` → `<body>` → `<div>` → `<p>` 식으로 태그가 노드(node)로 표현되며, JavaScript는 이 트리를 통해 화면 요소를 읽거나 변경할 수 있음.
문제는 DOM 조작 비용이 큰 편이라는 점임. 요소 하나를 바꿔도 브라우저는 레이아웃 계산·페인팅을 다시 수행하므로, 변경이 잦을수록 성능 부담이 커짐.
#### 실제 DOM vs. Virtual DOM
| 구분 | 실제 DOM (Real DOM) | Virtual DOM |
| --- | --- | --- |
| 실체 | 브라우저가 직접 관리하는 화면 트리 | 프레임워크가 메모리에 유지하는 DOM의 JS 복사본 |
| 업데이트 방식 | 변경 발생 시 해당 부분을 즉시 실제 화면에 반영 | 변경 전·후 Virtual DOM을 비교(diffing)해 달라진 부분만 실제 DOM에 반영 |
| 성능 특성 | 변경이 잦으면 불필요한 리렌더링이 누적됨 | 최소한의 실제 DOM 접근으로 렌더링 비용을 줄임 |
| 사용 프레임워크 | Angular | Vue.js, React |
Vue·React가 Virtual DOM을 쓰는 이유는 "실제 DOM 접근 횟수를 줄이기 위해서"임. 데이터가 바뀌면 먼저 Virtual DOM끼리 비교해 달라진 노드만 추려낸 뒤, 그 부분만 실제 DOM에 한 번에 적용하는 방식임.
---
### Vue.js Features — Virtual DOM
브라우저의 Real DOM 조작은 비용이 큰 연산임. DOM이 수정될 때마다 브라우저는 Layout 재계산(Reflow)과 화면 재색칠(Repaint)을 수행하기 때문임. 예를 들어 3,000개의 노드가 있는 상태에서 연속적인 상태 변경이 일어나면, 변경마다 Layout/Paint 연산이 반복되어 화면이 느려짐. 10번의 데이터 변화 = 10번의 브라우저 렌더링 연산이 즉시 발생하는 구조임.
![]()
Vue.js는 Virtual DOM을 도입해 이 문제를 해결함.
- Virtual DOM은 실제 브라우저 DOM의 메모리상 JavaScript 복사본임. 개발자가 DOM을 직접 조작하지 않아도, 상태 변화만 선언하면 Vue가 최적의 최소 DOM 조작 지점을 자동으로 추적함.
- Batch 처리: 한 이벤트 안에서 데이터가 여러 번 바뀌어도, 모두 끝난 시점에 단 한 번만 실제 DOM에 반영함. 10번의 변경 → 1번의 실제 DOM 업데이트로 줄어드는 것임.
#### 동작 흐름 비교
| 방식 | 흐름 |
| --- | --- |
| Real DOM 직접 조작 | Web page → (Updates) → Real DOM → (Events) → Web page |
| Virtual DOM 경유 | Web page → (Updates) → Virtual DOM → (Updates) → Real DOM |
Virtual DOM 방식에서는 Web page와 Virtual DOM이 먼저 동기화되고, Virtual DOM이 변경된 부분만 추려 Real DOM에 최소한으로 반영함.
---
### Vue.js Features — Two-Way Data Binding
양방향 데이터 바인딩(Two-Way Data Binding)은 Model(JavaScript 데이터)이 바뀌면 View(화면)가 자동으로 바뀌고, 반대로 View(화면 입력)가 바뀌면 Model도 동시에 업데이트되는 방식임. Vue에서는 `v-model` directive로 이를 구현함.
![]()
#### 흐름 정리
- Template이 컴파일되어 View(화면)를 생성함
- Model은 Single Source of Truth로, 지속적으로 View와 동기화됨
- View 변경 → Model 업데이트 / Model 변경 → View 업데이트, 두 방향 모두 자동으로 처리됨
React의 단방향 데이터 흐름(Model → View만)과 달리, Vue의 양방향 바인딩은 폼 입력 처리 등에서 별도의 이벤트 핸들러 없이도 Model과 View를 동기화할 수 있어 코드가 간결해짐.
---
### Vue.js Features — Component Based Architecture
컴포넌트 기반 개발은 웹페이지를 통째로 만들지 않고, 독립적인 UI 부품(Component)들을 각각 만든 뒤 조립하여 화면을 완성하는 방식임.
#### 컴포넌트의 구조
각 컴포넌트는 하나의 `.vue` 파일 안에 세 가지 영역을 응집시킴(Encapsulation).
| 영역 | 역할 |
| --- | --- |
| `<template>` | HTML-like 문법으로 UI 구조 정의 |
| `<script>` | JavaScript로 로직·기능 처리 |
| `<style>` | 해당 컴포넌트에만 적용되는 CSS 스타일 정의 |
![]()
#### 핵심 특성
- Reusability: 잘 만든 컴포넌트는 여러 페이지에서 재사용 가능해 중복 코드가 제거됨. 예를 들어 Page A와 Page B가 동일한 Header/Footer 컴포넌트를 공유함.
- Tree Structure: 컴포넌트들은 부모-자식 트리 구조로 조합됨.
	- 부모 → 자식: Props를 내려줌(Pass Props)
	- 자식 → 부모: 이벤트를 올려 상태 변경을 알림(Emit Events)
이 구조 덕분에 컴포넌트 간 데이터 흐름이 명확하게 분리되고, 각 컴포넌트는 독립적으로 개발·테스트·유지보수가 가능함.
---
### Vue.js 렌더링 — CSR vs. SSR
렌더링 방식의 핵심 질문은 "화면을 구성하는 HTML 파일을 어디서 최종적으로 완성하는가?"임.
- CSR (Client-Side Rendering): <br>브라우저(클라이언트)가 JavaScript를 실행하여 화면을 직접 그리는 방식. Vue.js의 기본 동작 렌더링 방식임.<br>→ 사용자의 화면(index.html)에서 데이터와 화면(vue나 js)이 만나서 조립됨.
- SSR (Server-Side Rendering): <br>서버에서 데이터까지 모두 주입하여 완성된 HTML 파일을 만들어 브라우저에 내려주는 방식. Vue 생태계에서는 주로 Nuxt.js 프레임워크로 구현함.<br>→ Spring Boot의 Thymleaf가 이에 해당함.<br>→ 백엔드 코드에서 이미 화면과 데이터를 조립해서 클라이언트에게 던짐<br>→ 백엔드 서버에서 데이터가 포함된 html 파일 + css 파일을 따로, 브라우저로 보내서 클라이언트 브라우저에서 조립해서 렌더링함
| 비교 항목 | CSR (기본 Vue.js / SPA) | SSR (Vue + Nuxt.js) |
| --- | --- | --- |
| HTML 완성 주체 | 브라우저 (클라이언트) | 웹 서버 |
| 초기 서버 전송 데이터 | 빈 HTML + 대용량 JS 파일 | 데이터가 결합된 완성된 HTML |
| 초기 화면 표시 속도 | 느림 (JS 다운로드 및 실행 대기) | 매우 빠름 (HTML 즉시 렌더링) |
| 페이지 이동 속도 | 매우 빠름 (서버 거치지 않음) | 다소 느림 (서버가 다음 페이지를 다시 그려야 함) |
| SEO | 불리함 (봇이 빈 화면으로 인식 가능) | 강력함 (완성된 텍스트 수집 가능) |
---
#### Vue.js 렌더링 — SPA (Single Page Application)
SPA는 브라우저가 서버로부터 오직 하나의 HTML 파일(`index.html`)만 받아와서 구동되는 웹 애플리케이션 구조임.
#### MPA vs. SPA 동작 비교
전통적인 MPA(Multi Page Application)에서는 사용자가 메뉴를 클릭할 때마다 서버에 새 HTML 파일을 요청하고, 브라우저는 전체 페이지를 새로 렌더링함.
SPA(Vue.js)에서는 최초 진입 시 `index.html + JS/CSS`를 한 번만 받아오고, 이후 페이지 전환은 JavaScript가 필요한 부분만 교체하여 렌더링함. 추가 데이터가 필요하면 백엔드 API 서버에 JSON만 요청함. 브라우저는 페이지 이동 없이 화면을 갱신함.
---
#### Vue.js 렌더링 — SPA vs. MPA 상세 비교
![]()
| 구분 | MPA | SPA |
| --- | --- | --- |
| 페이지 구성 방식 | 요청할 때마다 새로운 HTML을 서버에서 전송 | 초기 로딩 시 하나의 HTML + 대용량 JS 로딩 |
| 페이지 전환 | 서버 요청 → 전체 페이지 새로 고침 | JS로 필요한 부분만 변경 (부분 렌더링) |
| 요청 처리 방식 | 요청마다 서버에서 HTML 렌더링 (SSR) | 데이터는 API로 받고 렌더링은 브라우저 수행 (CSR) |
| 속도 | 초기 로딩 빠름, 페이지 전환 다소 느림 | 초기 로딩 느림, 페이지 전환 매우 빠름 |
| 새로고침(F5) | 자연스럽게 동작 | 전체 앱이 다시 로딩되어 상태가 초기화될 수 있음 |
| SEO | HTML이 서버에서 렌더링되므로 SEO에 유리 | JS 기반 렌더링으로 SEO가 불리 (보완 가능) |
| 기술 스택 예시 | JSP, PHP, ASP.NET, Spring MVC 등 | Vue.js, React, Angular + REST API (ex: Spring Boot) |
---
#### Vue.js 렌더링 — SPA 추가 기술 요소 및 장단점
#### Vue SPA 생태계 주요 도구
| 도구 | 역할 |
| --- | --- |
| Vite | Frontend Build Tool. `.vue`, `.js`, `.css` 파일들을 브라우저가 읽을 수 있는 최적화된 정적 파일로 묶어주고 개발 서버를 띄워주는 번들러(Bundler)임 |
| Vue Router | 브라우저의 URL 주소와 Vue 컴포넌트를 연결해 주는 공식 라우팅 라이브러리 |
| Pinia | 전역 상태 관리 라이브러리. 모든 컴포넌트가 접근할 수 있는 중앙 집중식 데이터 저장소(Store)를 메모리 상에 개설함 |
| Axios | 백엔드 API 서버와 JSON 데이터만 주고받는 통신 창구 |
#### SPA 장점
- 압도적인 UX: 페이지 이동이 데스크톱 소프트웨어처럼 즉각적임
- 네트워크 효율성: 한 번 로딩된 CSS·JS 등을 재사용하고 데이터만 주고받으므로 전체 네트워크 트래픽이 크게 절감됨
- 프론트/백엔드 분리: 프론트엔드는 Vue만, 백엔드는 데이터만 담당하므로 팀 간 협업 및 서버 분산이 명확함
#### SPA 단점
- 초기 로딩 속도: 모든 JavaScript 로직이 하나의 `app.js`로 묶여 처음에 다운로드되므로, 첫 접속 시 대기 시간이 발생할 수 있음
- SEO 취약: 검색 로봇이 들어왔을 때 알맹이 없는 빈 `index.html`만 보이기 때문에 검색 노출 점수를 따기 어려움
---
#### 뷰 프로젝트 구조
VS Code에서 SKALA-VUE 프로젝트를 열면 아래와 같은 폴더/파일 구조가 나타남.
| 폴더/파일 | 역할 |
| --- | --- |
| `.vscode` | 에디터 개인 설정 폴더 |
| `node_modules` | 외부 라이브러리 물리 저장소 (`npm install` 결과물) |
| `public` | 순수 정적 자원(Static Assets) 저장소. Vite가 컴파일하지 않고 그대로 배포함 |
| `src` | 실제 소스코드 작업 공간 |
| `.gitattributes` | 서로 다른 OS를 쓰는 개발자들이 협업할 때 사용 |
| `.gitignore` | 원격 서버에 업로드되지 않는 파일 목록 명세 |
| `index.html` | 브라우저가 최초로 보여주는 단 하나의 진짜 HTML 파일 (SPA 진입점) |
| `package.json` | npm의 핵심 명세서 (의존성·스크립트 정의) |
| `README.md` | 프로젝트 가이드 문서 |
| `vite.config.js` | 빌드 도구 Vite의 전역 환경 설정 파일 |
---
#### Frontend Project Tools — 도구의 필요성
현대 웹 UI 개발은 세 가지 이유로 전용 도구가 필요함.
- 파일 분할과 모듈화: 유지보수·재사용성을 위해 JavaScript를 여러 파일로 나누어 작성하지만, 배포 시에는 하나로 묶어야 함
- 사이즈 최적화: 배포 시 전체 파일을 묶고 크기를 줄여야 함
- 브라우저 호환: 구 버전 브라우저에서 ES6 이후 문법이나 TypeScript를 사용하려면 변환 과정이 필요함
개발 편의를 위한 자동화도 도구가 담당함. 변경 시 자동 새로고침(Live Reload, HMR), 코드 압축·이미지 최적화·CSS 전처리, `.vue`·`.scss`·`.ts` 등 다양한 확장자 처리가 이에 해당함.
#### 도구 유형 정리
| 용어 | 의미/역할 | 예시 |
| --- | --- | --- |
| Packager | 패키지를 다운로드하고 설치 (종속성 관리) | npm, yarn, pnpm |
| Compiler | 코드를 다른 형식으로 변환 (ex. TypeScript → JavaScript) | Babel, TypeScript |
| Transpiler | 같은 수준의 언어에서 문법을 변환 | Babel (ES6 → ES5) |
| Task Runner | 반복 작업 자동화 (빌드, 테스트, 린트 등) | Gulp, Grunt |
| Bundler | 여러 JS/CSS 모듈을 묶어 하나의 파일 또는 청크로 만듦 | Vite, Webpack, Rollup, Parcel |
| Build Tool | 컴파일, 번들링, 최적화 등을 포함한 전체 빌드 과정 도구 | Vite, Webpack, Parcel |
---
#### Frontend Project Tools — Vite
Vite는 Vue 소스 코드를 Build하고, 로컬 개발 서버를 띄워주는 Frontend Build 도구임.
#### 주요 기능 세 가지
- Compile: `.vue`나 TypeScript를 순수한 HTML, JavaScript, CSS로 변환함
- Local 개발 서버 제공: 코드를 실시간으로 반영(HMR, Hot Module Replacement)되도록 로컬 웹 서버에 컴파일된 소스를 제공함. 파일 하나만 바꿔도 전체를 다시 빌드하지 않고 해당 모듈만 교체함
- Bundling: 수백 개의 작은 소스코드 파일들을 배포에 적합하도록 몇 개의 압축된 덩어리 파일로 묶어줌 (Staging/Production 서버용)
참고로 과거에 사용하던 Vue-CLI + Webpack 조합은 Vite 이전 기술로, 현재는 더 이상 사용하지 않음.
---
#### Frontend Project Tools — npm
NPM(Node Package Manager)은 오픈소스 라이브러리 저장소이자 Node.js 패키지 관리 도구임.
#### npm 구성 요소
- npm Registry: JavaScript 라이브러리를 업로드해 두는 공식 Cloud Server
- npm CLI: `npm install` 같은 명령어를 수행하는 커맨드라인 인터페이스
- npmjs.com: 등록된 패키지들을 웹 브라우저로 확인할 수 있는 공식 포털 사이트
#### 주요 npm 명령어
| 분류 | 명령어 | 상세 내용 |
| --- | --- | --- |
| 프로젝트 생성 | `npm create vue@latest` | `create-vue` 스캐폴딩 도구를 실행하여 Vite 기반의 최신 Vue 3 뼈대 폴더와 설정 파일을 자동 생성 |
| 의존성 설치 | `npm install` | `package.json` 명세서를 읽어, 누락된 외부 라이브러리들을 인터넷에서 다운로드하여 `node_modules` 폴더를 생성 |
| 패키지 추가 | `npm install 패키지명` | 특정 외부 라이브러리를 `node_modules`에 넣고, `package.json`의 dependencies(배포용 라이브러리 목록)에 자동 등록 |
| 패키지 제거 | `npm uninstall 패키지명` | `node_modules` 내부에서 물리 파일을 완전히 삭제하고, `package.json` 명세서에서도 이름을 삭제 |
| 로컬서버 구동 | `npm run dev` | `package.json`의 scripts에 정의된 vite 엔진을 가동하여 컴파일을 대기하고, 로컬 주소(localhost:5173)로 HTTP 개발 서버를 개설 |
| 최종 배포 | `npm run build` | 내부의 Rollup 엔진을 깨워 프로젝트의 모든 소스를 살살이 뒤진 뒤, 쓸데없는 코드를 털어내고(Tree-shaking) 압축된 정적 파일(`dist` 폴더)을 생성 |
---
### Project 구조 — 핵심 폴더와 파일
`npm create vue@latest`로 생성된 Vue 프로젝트의 디렉토리 구조는 아래와 같음.
| 디렉토리/파일 | 설명 |
| --- | --- |
| `index.html` | 어플리케이션 진입점(entry point). 브라우저가 최초로 읽는 단 하나의 진짜 HTML |
| `package.json` | 프로젝트 메타정보(이름, 버전), 실행 스크립트 명령어, 의존성 라이브러리 목록 기록 |
| `vite.config.js` | Vite 빌드 엔진 설정 파일 |
| `.gitignore` | git에서 추적하지 않을 파일 목록 |
| `public/` | 브라우저에 바로 제공되는 정적(static) 파일 폴더. 빌드 엔진이 컴파일하지 않음 |
| `src/` | 실제 소스코드 작업 공간 |
| `src/main.js` | `index.html`에서 지정하는 어플리케이션 진입점 ← `index.html`에서 호출 |
| `src/App.vue` | 어플리케이션 루트 Vue 컴포넌트 ← `main.js`에서 호출 |
| `src/style.css` | 스타일(CSS) 파일 |
| `src/assets/` | CSS, 로고 이미지, 폰트 파일 등 Vite 빌드 엔진에 의해 컴파일·최적화가 필요한 소스 자원 |
| `src/components/` | 화면의 일부분을 조각내어 만든 재사용 가능한 작은 부품(Component)들을 보관하는 곳 |
| `src/components/HelloWorld.vue` | 헬로 월드 컴포넌트 ← `App.vue`에서 호출 |
| `src/router/` | SPA의 핵심인 페이지 이동 경로를 정의 |
| `src/stores/` | 전역 상태 관리 도구인 Pinia의 데이터 저장소 |
| `src/views/` | components 조각들을 조립해서 완성한 하나의 독립된 페이지 단위 화면 |
---
### Project 구조 — 핵심 폴더와 파일
`npm create vue@latest`로 생성된 Vue 프로젝트의 디렉토리 구조는 아래와 같음.
| 디렉토리/파일 | 설명 |
| --- | --- |
| `index.html` | 어플리케이션 진입점(entry point). 브라우저가 최초로 읽는 단 하나의 진짜 HTML |
| `package.json` | 프로젝트 메타정보(이름, 버전), 실행 스크립트 명령어, 의존성 라이브러리 목록 기록 |
| `vite.config.js` | Vite 빌드 엔진 설정 파일 |
| `.gitignore` | git에서 추적하지 않을 파일 목록 |
| `public/` | 브라우저에 바로 제공되는 정적(static) 파일 폴더. 빌드 엔진이 컴파일하지 않음 |
| `src/` | 실제 소스코드 작업 공간 |
| `src/main.js` | `index.html`에서 지정하는 어플리케이션 진입점 ← `index.html`에서 호출 |
| `src/App.vue` | 어플리케이션 루트 Vue 컴포넌트 ← `main.js`에서 호출 |
| `src/style.css` | 스타일(CSS) 파일 |
| `src/assets/` | CSS, 로고 이미지, 폰트 파일 등 Vite 빌드 엔진에 의해 컴파일·최적화가 필요한 소스 자원 |
| `src/components/` | 재사용 가능한 작은 부품(Component)들을 보관하는 곳 |
| `src/components/HelloWorld.vue` | 헬로 월드 컴포넌트 ← `App.vue`에서 호출 |
| `src/router/` | SPA의 핵심인 페이지 이동 경로를 정의 |
| `src/stores/` | 전역 상태 관리 도구인 Pinia의 데이터 저장소 |
| `src/views/` | components 조각들을 조립해서 완성한 하나의 독립된 페이지 단위 화면 |
---
### Project 구조 — package.json
`package.json`은 프로젝트의 핵심 명세서로, 네 가지 영역으로 구성됨.
```json
{
  "name": "skala-vue",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "run-s lint:*",
    "lint:oxlint": "oxlint . --fix",
    "lint:eslint": "eslint . --fix --cache",
    "format": "prettier --write --experimental-cli src/"
  },
  "dependencies": {
    "pinia": "^3.0.4",
    "vue": "^3.5.32",
    "vue-router": "^5.0.4"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@vitejs/plugin-vue": "^6.0.6",
    "eslint": "^10.2.1",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-oxlint": "~1.60.0",
    "eslint-plugin-vue": "~10.8.0",
    "globals": "^17.5.0",
    "npm-run-all2": "^8.0.4",
    "oxlint": "~1.60.0",
    "prettier": "3.8.3",
    "vite": "^8.0.8",
    "vite-plugin-vue-devtools": "^8.1.1"
  },
  "engines": {
    "node": "^20.19.0 || >=22.12.0"
  }
}
```
#### Meta 정보
- `name`: 프로젝트 이름
- `version`: `0.0.0`은 `[major].[minor].[patch]` 형식
- `private: true`: 실수로 npm 레지스트리에 배포(publish)되는 것을 방지
- `type: "module"`: `.js` 파일들의 기본 모듈 시스템을 ESM(`import`/`export`)으로 지정
#### scripts
`npm run 명령어`로 실행하는 스크립트 목록.
- `dev`: 개발 서버 실행
- `build`: `dist` 폴더에 배포용 정적 자원 번들링
#### 의존성 모듈
- `dependencies`: 애플리케이션 실행에 필요한 패키지
- `devDependencies`: 개발 중에만 필요한 패키지
#### engines
- `node`: 프로젝트가 정상 동작하기 위해 요구되는 Node.js 최소 실행 버전
---
### Project 구조 — index.html
브라우저가 최초로 읽는 단 하나의 HTML 파일(Entry Point)임. 핵심 라인은 두 줄.
```html
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```
- Line 10 `<div id="app"></div>`: Vue 엔진이 Component들을 실시간으로 바꿔 끼워 화면을 그리는 마운트 대상 컨테이너
- Line 11 `<script type="module" src="/src/main.js">`: `main.js`를 모듈 형식으로 연결하여 이 시점부터 Vue 어플리케이션 코드가 실행됨
---
### Project 구조 — main.js
Vue 어플리케이션을 초기화하고 구성하는 진입 스크립트임. 코드 흐름 순서대로 정리하면 아래와 같음.
```javascript
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
```
- Line 1: `main.css`를 불러와 프로젝트 전체·모든 컴포넌트에 전역 적용
- Line 3\~4: `vue`에서 `createApp`, `pinia`에서 `createPinia` 함수를 가져옴
- Line 6\~7: `App.vue`(루트 컴포넌트)와 `router`를 가져옴
- Line 9: `createApp(App)`으로 Vue 어플리케이션 인스턴스 생성. 아직 화면에 그려지지 않은 상태
- Line 11\~12: `app.use(createPinia())`와 `app.use(router)`로 Pinia·Router 플러그인 등록
- Line 14: `app.mount('#app')`으로 `index.html`의 `<div id="app">`에 물리적으로 넣으며(mount) 화면 렌더링 시작
`createApp()`이 반환하는 `app` 객체는 `use`, `component`, `directive` 등 플러그인 설치나 전역 자원 등록에 사용하는 컨텍스트 API를 내장하고 있음. 최상위 컴포넌트(`App.vue`)를 기점으로 하위 컴포넌트들이 Component Tree를 형성하며 렌더링 파이프라인을 구축함.
---
### Project 구조 — App.vue
`App.vue`는 Vue 어플리케이션의 Root Component 역할을 함.
```plain text
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg">

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
```
- `<script setup>`: `vue-router`의 `RouterLink`·`RouterView`와 `HelloWorld.vue` 컴포넌트를 import함
- `<template>`: `<HelloWorld msg="You did it!" />`로 HelloWorld 컴포넌트를 배치하고 Props로 `msg` 값을 전달함
- `<RouterLink to="/">`: HTML `<a>` 태그로 변환되지만 브라우저 새로고침을 막고 주소창만 바꿈
- `<RouterView />` (Line 20): 주소창 변경에 따라 해당 경로의 컴포넌트가 동적으로 끼워지는 가변형 주입 구역. SPA 페이지 전환의 핵심<br>→ js에 정의된 것을 바탕으로, 이 부분이 바뀌어 끼워짐
→ 기본적으로 SFC(.vue 파일)에는 `template, script, style`로 구성됨
---
### SFC (Single File Component)
Vue 컴포넌트는 `.vue` 확장자를 가진 하나의 독립된 파일(SFC)로 구성됨. SFC는 세 영역으로 이루어짐.
| 영역 | 역할 |
| --- | --- |
| `<script setup>` | 데이터, 함수 등 기능 로직을 JavaScript로 작성하는 곳<br>  • MVVM의 M(model)에 해당 |
| `<template>` | 사용자에게 보여질 HTML 구조를 작성하는 곳<br>  • MVVM의 V(view)에 해당 |
| `<style>` | CSS 스타일을 작성하는 곳 (보통 `scoped`로 적용 범위를 제한함)MVVM의 M(model)에 해당 |
Vue3 생태계에서는 `<script setup>`을 맨 위에 먼저 쓰고, 그 아래에 `<template>`을 작성하는 방식이 트렌드가 되었음. 컴포넌트 파일명은 두 단어 이상으로 조합된 PascalCase를 권장함 (ex. `HelloWorld.vue`).
---
#### SFC 예시 — HelloWorld.vue
`App.vue`에서 Props로 받은 `msg`를 화면에 출력하는 간단한 예시 컴포넌트임.
- `defineProps()`로 부모에서 내려오는 `msg` prop을 선언하고 타입과 필수 여부를 지정함<br>→ 부모에서 자식으로 Props를 통해 데이터를 보냄
- `<template>`에서 `{{ msg }}`로 msg 값을 텍스트로 출력함 (Text Interpolation)
- `<style scoped>`로 스타일을 이 컴포넌트 안에서만 적용되도록 범위를 제한함
```javascript
<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      You've successfully created a project with
      <a href="https://vite.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
```
---
#### SFC — Options API vs. Composition API
Vue 컴포넌트의 `<script>` 영역을 작성하는 방법은 두 가지임.
| 비교 항목 | Options API (Vue 2 방식) | Composition API (Vue 3 표준) |
| --- | --- | --- |
| 코드 선언 구조 | `<script>` | `<script setup>` |
| 작성 철학 | 역할별 격리 (Options 기반). 정해진 상자(`data`, `methods`, `computed`) 안에 코드를 나누어 배치 | 논리적 기능별 그룹화 (Function 기반). 관련 있는 데이터와 함수를 한곳에 연달아 묶어 작성 |
| 코드 가독성 (규모가 커질 때) | 하나의 기능을 수정하기 위해 파일 상단 `data`와 하단 `methods`를 계속 오르내려야 함 | 하나의 기능에 필요한 데이터와 로직이 한 구역에 모여 있어 한눈에 파악 가능 |
| 반응성 변수 선언 | `data()` 함수가 반환하는 객체 내부에 선언 | `ref()` 또는 `reactive()` 내장 함수를 사용해 선언 |
| 코드 재사용성 | Mixin을 사용하나, 데이터 출처가 불분명해지고 이름 충돌 가능성이 높음 | Composable 함수를 사용해 순수 자바스크립트 함수 형태로 완벽하게 격리 및 재사용 가능 |
| TypeScript 호환 | 구조적 한계로 인해 타입 추론 및 결합이 매우 복잡하고 부자연스러움 | 순수 함수 및 변수 기반이므로 TypeScript와 완벽하게 100% 호환 및 자동 추론 가능 |
| 공식 권장 여부 | 레거시 유지보수 외에는 신규 권장 안 함 | 현재 Vue 3 공식 문서 및 생태계 기본 표준 |
Composable: Vue의 반응형 상태(Ref, Reactive)와 로직을 묶어 재사용할 수 있도록 만든 함수.
---
#### SFC — Options API vs. Composition API 코드 비교
동일한 카운터 기능을 두 방식으로 구현한 예시임.
Options API 방식 — 상태는 `data()`, 메서드는 `methods`에 각각 나뉘어 배치됨:
```javascript
// Options API 방식
<template>
  <div>
    <h1>Options API Counter</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0, // 상태 정의
    };
  },
  methods: {
    increment() {
      this.count++; // 메서드 정의
    },
  },
};
</script>

<style>
button {
  padding: 8px 16px;
  font-size: 16px;
}
</style>
```
Composition API 방식 — 상태와 메서드가 기능 단위로 함께 묶여 있음:
```javascript
// Composition API 방식
<template>
  <div>
    <h1>Composition API Counter</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const count = ref(0); // 상태 정의
const increment = () => {
  count.value++; // 메서드 정의
};
</script>

<style>
button {
  padding: 8px 16px;
  font-size: 16px;
}
</style>
```
---
### SFC — Interpolation & Directive
Vue 컴포넌트의 `<template>` 영역을 작성하는 두 가지 핵심 문법임.
#### Text Interpolation (텍스트 보간법)
- Syntax: `{{ 변수명 }}`
- 용도: JavaScript 변수 값을 그대로 문자열로 투사하고 싶을 때 사용
#### Directive
- Syntax: `v-`로 시작하는 Vue 전용 특수 속성 (`v-bind`, `v-if`, `v-for`, `v-on` 등)
- 용도: 일반 HTML 태그 안에서 태그의 속성, 스타일, 조건문, 반복문, 이벤트 리스너 등을 자바스크립트 데이터와 연결하여 제어하기 위해 사용
```javascript
<template>
  <div>
    <h1>Composition API Counter</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```
위 예시에서 `{{ count }}`는 Text Interpolation으로 `count` 변수 값을 화면에 출력하고, `@click="increment"`는 `v-on:click`의 축약형 Directive로 버튼 클릭 이벤트를 `increment` 함수에 연결하는 것임.
---
### 학습환경 구성 — App.vue 비우기
실습 시작 전 `App.vue`를 아래와 같이 최소 구조로 비워서 시작함. `<script setup>`은 빈 상태로 두고, `<template>`에는 확인용 제목만 남긴 형태임.
![]()
`App.vue`
```javascript
<script setup>
// 자바스크립트 영역 (우선 비워둡니다)
</script>

<template>
  <h1>Hello Skala-Vue</h1>
</template>
```
브라우저에서 확인하면 "Hello Skala-Vue" 텍스트만 렌더링되고, Vue DevTools의 컴포넌트 탭에서 `<App>` 하나만 존재하는 깨끗한 상태를 확인할 수 있음.
---
#### 학습환경 구성 — App.vue 샘플 컴포넌트 채우기
실습 컴포넌트를 만든 뒤, `App.vue`에서 import하여 자식 컴포넌트로 끼워 넣는 방식으로 테스트함. 교육과정에서 작성되는 컴포넌트들은 특정 폴더에 분류하여 넣음 (ex. `src/components/practices/basic/`).
`App.vue`
```javascript
<script setup>
import SampleOne from './components/practices/basic/SampleOne.vue'
</script>

<template>
  <div style="padding: 20px">
    <SampleOne />
  </div>
</template>
```
---
#### 학습환경 구성 — 반응성 데이터 (Reactivity) Example
일반 변수와 `ref()`로 감싼 반응형 변수의 차이를 직접 비교한 예시임.
- 일반 변수(`let normalCount`)는 버튼을 눌러도 화면의 숫자가 변경되지 않음. 내부 값은 바뀌지만 Vue가 변화를 감지하지 못하기 때문임.
- `ref()`로 감싼 반응형 변수(`const vueCount`)는 버튼을 누르는 순간 숫자가 즉시 화면에 반영됨.
- 반응형 변수를 누르는 순간 화면을 새로 고침으로 일반 변수의 변경된 값도 같이 반영됨.
- 참고: JavaScript 소스 끝 부분의 `;`를 빼먹어도 ASI(Automatic Semicolon Insertion) 기능으로 자동 삽입되어 잘 동작함.
![]()
`src/components/practices/basic/SampleOne.vue`
```javascript
<script setup>
import { ref } from 'vue'

// 1. 일반 변수 (화면이 실시간으로 바뀌지 않음)
let normalCount = 0
// 2. 반응성 변수 (화면이 실시간으로 바뀜)
const vueCount = ref(0)
</script>

<template>
  <div class="practice-section">
    <h2>Hello Skala-Vue</h2>
    <h3>일반 변수 클릭: {{ normalCount }}</h3>
    <button @click="normalCount++">일반 변수 증가</button>
    <br />
    <h3>Vue 반응성 변수 클릭: {{ vueCount }}</h3>
    <button @click="vueCount++">Vue 변수 증가</button>
  </div>
</template>
```
---
#### 학습환경 구성 — JavaScript in Text Interpolation Example
`{{ }}` 안에는 변수명뿐 아니라 JavaScript 표현식(Expression)도 직접 사용할 수 있음.
![]()
`src/components/practices/basic/SampleTwo.vue`
```javascript
<script setup>
import { ref } from 'vue'

const welcomeMessage = 'Welcome to Skala-Vue'
</script>

<template>
  <div class="practice-section">
    <h2>{{ welcomeMessage }}</h2>
    <p>{{ welcomeMessage.toUpperCase() }}</p>
    <p>{{ 'Random number: ' + Math.ceil(Math.random() * 100) }}</p>
  </div>
</template>
```
- `{{ welcomeMessage }}` → 변수 값 그대로 출력
- `{{ welcomeMessage.toUpperCase() }}` → 문자열 메서드 호출 결과 출력
- `{{ 'Random number: ' + Math.ceil(Math.random() * 100) }}` → 연산식 결과 출력
`{{ }}` 안에서는 단일 JavaScript 표현식이라면 무엇이든 사용 가능하지만, `if`문 같은 구문(statement)은 사용할 수 없고 삼항 연산자로 대체해야 함.
---
### Vue Directive
Vue Directive는 `v-` 접두사가 붙은 특수한 HTML 속성으로 Vue 인스턴스와 연동됨. Directive 뒤에 오는 값인 `v-명령어="값"` 구역의 따옴표 내부(`" "`)는 단순 문자열이 아니라 자바스크립트 변수나 연산식이 작동하는 공간임.
| Directive | 설명 | 비고 |
| --- | --- | --- |
| `v-html` | 요소의 HTML 콘텐츠를 표현식의 값으로 업데이트 | 보안사고(XSS) 유의 |
| `v-text` | 텍스트 콘텐츠를 표현식의 값으로 업데이트 | Text Interpolation과 유사 |
| `v-bind` | Elements의 Attributes에 표현식(변수, 함수, 객체 등)을 동적으로 바인딩 | 축약형 → `:` |
| `v-model` | 폼 입력 `<input>`과 Vue 인스턴스 데이터 간에 양방향 데이터 바인딩 |  |
| `v-if` | 표현식의 참/거짓에 따라 요소 또는 템플릿 `<template>` 블록을 조건부로 렌더링 | `v-else-if`, `v-else` |
| `v-show` | 표현식의 참/거짓에 따라 HTML element를 보이거나 숨김 | `v-if`와 구분 |
| `v-for` | 반복적으로 렌더링하는 HTML 요소를 생성 |  |
| `v-on` | 클릭 또는 키 입력과 같은 사용자 이벤트에 응답하고자 지정 메서드를 실행 | 축약형 → `@` |
| `v-cloak` | 템플릿이 렌더링 되기 전까지 요소를 숨김 | 자주 사용되지 않음 |
| `v-once` | 요소와 하위 콘텐츠를 한 번만 렌더링하고, 이후 변경하지 않음 | 자주 사용되지 않음 |
| `v-pre` | 템플릿 구문을 무시하고 원본 HTML을 그대로 렌더링 | 자주 사용되지 않음 |
자주 쓰는 핵심 Directive는 `v-bind`(`:`)와 `v-on`(`@`)이며, 이 둘의 축약형을 실무에서 거의 항상 사용함. `v-if`와 `v-show`는 둘 다 조건부 표시이지만 동작 방식이 다름
---
### Vue Directive — v-html
`v-html`은 자바스크립트 변수에 담긴 문자열을 단순 텍스트가 아니라 실제 HTML Element로 해석하여 화면에 주입하는 Directive임. 내부적으로는 자바스크립트의 `element.innerHTML` 속성과 동일하게 동작함.
`{{ }}` 보간법과의 차이:
- `{{ rawHtmlData }}` → HTML 태그를 문자열 그대로 출력 (태그가 텍스트로 보임)
- `v-html="rawHtmlData"` → HTML 태그를 실제로 파싱하여 렌더링 (스타일 적용됨)
![]()
`src/components/practices/basic/SampleVHtml.vue`
```javascript
<script setup>
const rawHtmlData = '이 글자는 <span style="color: red; font-weight: bold;">빨간색 굵은 글자</span>이다.'
</script>

<template>
  <div class="practice-section">
    <h2>v-html 디렉티브 학습</h2>
    <h3>일반 보간법 {{}} 사용 결과:</h3>
    <p>{{ rawHtmlData }}</p>
    <br />
    <h3>v-html 디렉티브 사용 결과:</h3>
    <p v-html="rawHtmlData"></p>
  </div>
</template>
```
---
### Vue Directive — v-html XSS 위협
`v-html`은 XSS(Cross-Site Scripting) 공격에 노출되므로 사용 시 각별히 주의해야 함.
XSS란 해커가 게시판 댓글이나 입력창에 악성 자바스크립트 코드를 심어두고, 다른 사용자가 그 글을 읽을 때 그 사용자의 브라우저에서 해커의 코드가 강제로 실행되게 만들어 쿠키·세션 토큰·로그인 정보를 탈취하는 해킹 기법임.
`v-html`은 입력값을 HTML로 그대로 파싱하기 때문에, 사용자가 입력한 악성 HTML이 그대로 실행될 수 있음. 아래 예시에서 `<img src="x" onerror="window.location.href='https://google.com'" />`를 입력 후 확인 버튼을 클릭하면 다른 사이트로 강제 이동됨.
![]()
`src/components/practices/basic/SampleVHtmlXSS.vue`
```javascript
<script setup>
import { ref } from 'vue'

const inputValue = ref('')
const message = ref('')

function showMessage() {
  message.value = inputValue.value
}
</script>

<template>
  <div class="practice-section">
    <h2>v-html XSS 학습</h2>
    <input v-model="inputValue" placeholder="내용을 입력하세요" />
    <button @click="showMessage">확인</button>
    <div v-html="message"></div>
  </div>
</template>
```
따라서 `v-html`은 신뢰할 수 있는 내부 데이터에만 사용해야 하며, 사용자 입력값을 그대로 `v-html`에 바인딩하는 것은 금지해야 함.
---
### Vue Directive — v-text
`v-text`는 지정한 변수의 값을 태그의 텍스트 내용으로 채워 넣는 Directive임. 내부적으로는 자바스크립트의 `element.innerText` 속성과 똑같이 동작함. Text Interpolation `{{ }}`과 동일하므로 실무에서는 `v-text` 대신 `{{ }}`을 사용함.
세 가지 방식의 출력 결과 비교:
| 방식 | 코드 | 출력 결과 |
| --- | --- | --- |
| `{{ }}` 보간법 | `{{ content }}` | HTML 태그를 문자열 그대로 출력 |
| `v-text` | `v-text="'출력: ' + content"` | HTML 태그를 문자열 그대로 출력 (동일) |
| `v-html` | `v-html="content"` | HTML 태그를 실제로 파싱하여 렌더링 |
![]()
`src/components/practices/basic/SampleVText.vue`
```javascript
<script setup>
const content = '안녕하세요! <strong>Skala-Vue</strong> 강의입니다.'
</script>

<template>
  <div class="practice-section">
    <h2>v-text 디렉티브 학습</h2>
    <h3>1) 일반 보간법 {{}} 결과:</h3>
    <p>출력: {{ content }}</p>
    <br />

    <h3>2) v-text 디렉티브 결과:</h3>
    <p v-text="'출력: ' + content"></p>
    <br />

    <h3>3) v-html 결과 비교:</h3>
    <p v-html="content"></p>
  </div>
</template>
```
---
### Vue Directive — v-bind (기본)
`v-bind`는 HTML 태그 내부의 Attribute에 자바스크립트 값을 동적으로 연결(Binding)하는 Directive임. 문법은 `v-bind:[attribute]="[Vue data]"`이며, 실무에서는 `v-bind`를 생략하고 콜론(`:`) 축약형을 100% 사용함.
세 가지 활용 예시:
- `:href` — URL 변수를 `<a>` 태그의 링크에 동적으로 연결
- `:src` — 이미지 경로 변수를 `<img>` 태그의 src에 동적으로 연결
- `:disabled` — 반응형 변수로 버튼의 활성화/비활성화 상태를 동적으로 제어
![]()
`src/components/practices/basic/SampleVBind.vue`
```javascript
<script setup>
import { ref } from 'vue'

const dynamicUrl = 'https://www.naver.com'
const logoImgSrc = 'https://vuejs.org/images/logo.png'
const isButtonDisabled = ref(true)
</script>

<template>
  <div class="practice-section">
    <h2>v-bind 디렉티브 기본 (축약형: 콜론)</h2>
    <h3>1) 동적 링크 연결</h3>
    <a :href="dynamicUrl">여기를 클릭하면 네이버로 이동합니다</a>
    <br />

    <h3>2) 동적 이미지 연결</h3>
    <img :src="logoImgSrc" alt="Vue 로고" style="width: 100px" />
    <br />

    <h3>3) 버튼 비활성화 제어</h3>
    <p>현재 버튼 사용 불가능 상태: {{ isButtonDisabled }}</p>
    <button :disabled="isButtonDisabled">동의해야 클릭할 수 있는 버튼</button>&nbsp;
    <button @click="isButtonDisabled = !isButtonDisabled">위 버튼 잠금 해제/토글하기</button>
  </div>
</template>
```
---
#### Vue Directive — v-bind (Class Binding)
`:class`는 스타일시트 클래스를 동적으로 붙였다 뗐다 하는 클래스 바인딩임. 단순 문자열 주입이 아니라 객체(Object)와 배열(Array) 형식을 지원하여 강력한 조건부 디자인을 가능하게 함.
| 형식 | 예시 | 설명 |
| --- | --- | --- |
| 문자열 | `:class="'active'"` | 클래스 이름 문자열 하나 |
| 객체 | `:class="{ 'active-style': isActive, primary: isPrimary }"` | 조건에 따라 클래스 포함 여부 지정. 조건 불리언이 `true`일 때만 해당 클래스 활성화 |
| 배열 | `:class="[active, primary]"`, `:class="[baseClass, isError ? 'text-red' : 'text-blue']"` | 여러 클래스를 조건에 따라 조합. 삼항 연산자로 상황별 클래스 주입 가능 |
| 조합 | `class="기본스타일" :class="'추가스타일'"` | 정적 클래스와 동적 클래스 동시 적용 |
→ 위의 예시에서 `isActive`, `isPrimary` 는 boolean 타입 변수임
![]()
`src/components/practices/basic/SampleVBindClass.vue`
```javascript
<script setup>
import { ref } from 'vue'

const isWarning = ref(false) // 객체 바인딩용 스위치
const themeClass = ref('bg-dark') // 배열 바인딩용 고정 클래스
</script>

<template>
  <div class="practice-section">
    <h2>v-bind 디렉티브 고급 (클래스 바인딩)</h2>
    <h3>클래스 바인딩 (객체 형식)</h3>
    <p :class="{ 'text-danger': isWarning }">현재 경고 상태: {{ isWarning }}</p>
    <button @click="isWarning = !isWarning">경고 상태 토글</button>
    <br />
    <h3>클래스 바인딩 (배열 형식)</h3>
    <div :class="[themeClass, isWarning ? 'border-red' : 'border-gray']">다중 클래스가 조립된 박스 구역입니다.</div>
  </div>
</template>

<style scoped>
.text-danger { color: red; font-weight: bold; }
.bg-dark { background-color: #333; color: white; padding: 15px; }
.border-red { border: 3px solid red; }
.border-gray { border: 3px solid #ccc; }
</style>
```
---
### Vue Directive — v-bind (Style Binding)
`:style`은 인라인 스타일을 동적으로 제어하는 바인딩임. 클래스 바인딩처럼 객체(Object)와 배열(Array)을 지원함.
- 객체 구문: CSS 속성명을 camelCase로 작성. `kebab-case` 문자열도 사용 가능
	- 기본 구조: `:style="{ color: 변수명, fontSize: 변수명 + 'px' }"`
- 배열 구문: 여러 개의 스타일 객체 변수들을 하나로 합쳐서 태그에 주입
![]()
`src/components/practices/basic/SampleVBindStyle.vue`
```javascript
<script setup>
import { ref } from 'vue'

// 1. 객체 바인딩용 변수
const textColor = ref('purple')
const boxWidth = ref(150) // 숫자만 제어
// 2. 배열 바인딩용 스타일 객체 무더기
const baseBoxStyle = ref({
  backgroundColor: '#42b883',
  height: '100px',
  transition: 'all 0.3s ease', // 부드러운 애니메이션 효과
})
</script>

<template>
  <div class="practice-section">
    <h2>v-bind 디렉티브 고급 (스타일 바인딩)</h2>
    <h3>1) 인라인 스타일 변수 조작 (객체 형식)</h3>
    <p :style="{ color: textColor, fontWeight: 'bold' }">이 글자의 색상은 실시간으로 바뀝니다.</p>
    <button @click="textColor = textColor === 'purple' ? 'blue' : 'purple'">글자 색상 토글</button>
    <br />

    <h3>2) 다중 스타일 객체 조립 (배열 형식)</h3>
    <label>박스 가로 크기(px): </label>
    <input type="number" v-model="boxWidth" step="50" />
    <br />
    <div :style="[baseBoxStyle, { width: boxWidth + 'px' }]">
      <p style="color: white; padding: 10px; text-align: center">가로 크기: {{ boxWidth }}px 박스</p>
    </div>
  </div>
</template>
```
→ `<input>` 의 `step`은 얼마만큼의 간격씩 늘지
![]()
---
### Vue Directive — v-bind (Class vs. Style Binding 비교)
| 비교 항목 | 클래스 바인딩 (`:class`) | 스타일 바인딩 (`:style`) |
| --- | --- | --- |
| 기술적 실체 | HTML의 `class` 속성에 동적으로 문자열 주입 | HTML의 인라인 `style` 속성에 동적으로 스타일 주입 |
| 주요 활용 목적 | 이미 정의된 디자인 옷을 갈아 입힐 때 (활성화/비활성화, 다크모드 켜기, 경고 상태 등) | 수치나 색상을 실시간으로 미세 가공할 때 (슬라이더 수치 반영, 프로그레스바 게이지 등) |
| 속성명 작성 규칙 | CSS 클래스명을 문자열 그대로 작성. `{ 'text-danger': isWarning }` | camelCase 표기법 권장. `{ backgroundColor: '#fff', fontSize: '14px' }` |
| 객체 구문 해석 | `{ '클래스명': 조건불리언 }` → 조건이 `true`일 때만 해당 클래스 추가 | `{ CSS속성명: 자바스크립트변수 }` → 속성값에 변수의 데이터가 실시간 매핑 |
| 배열 구문 해석 | `[고정클래스, 조건부삼항연산클래스]` → 여러 클래스 이름을 나열하여 동시 적용 | `[스타일객체A, 스타일객체B]` → 분리되어 있던 여러 스타일 변수를 하나로 병합 |
| 실무 권장도 | 압도적 적극 권장 (90%). 구조와 스타일을 완벽히 분리하여 유지보수에 유리 | 특수 상황에서만 제한적 사용 (10%). 인라인 스타일 남용은 코드 복잡도를 높임 |
---
### Vue Directive — v-bind (Same-name Shorthand)
Vue 3.4 버전부터 공식 도입된 문법으로, 연결할 자바스크립트 변수명과 HTML 속성명이 완전히 일치할 때 코드를 극단적으로 줄여주는 방법임.
```html
<img v-bind:src="src" />  <!-- 전체 문법 -->
<img :src="src" />        <!-- 콜론 축약형 -->
<img :src />              <!-- same-name shorthand (Vue 3.4+) -->
```
동작 원리: 속성 앞에 콜론(`:`)만 붙이고 뒤의 `="src"`를 생략하면, Vue 엔진이 "이 태그의 `src` 속성에 이름이 똑같은 `src`라는 자바스크립트 변수를 자동으로 매핑하라는 뜻이구나!" 하고 알아서 해석함. 실무 활용 팁으로, 변수명을 `id`, `src`, `href`, `disabled` 등 HTML 표준 속성명과 똑같이 맞춰 선언해 두면 코딩 속도가 빨라짐.
![]()
`src/components/practices/basic/SampleVBindShorthand.vue`
```javascript
<script setup>
const id = 'user-profile-card'
const src = 'https://vuejs.org/images/logo.png'
</script>

<template>
  <div class="practice-section">
    <h2>v-bind 디렉티브 고급 (단축 문법)</h2>
    <div :id>
      <img :src alt="Vue 로고" style="width: 50px" />
    </div>
  </div>
</template>
```
---
### Vue Directive — v-if / v-else-if / v-else
JavaScript 조건식의 결과(true/false)에 따라 HTML 태그를 화면에 그릴지, 아니면 지울지 결정하는 제어문 역할의 Directive임.
![]()
`src/components/practices/basic/SampleVIf.vue`
```javascript
<script setup>
import { ref } from 'vue'

// 1. 조건부 온/오프 스위치 변수
const isLogged = ref(false)
// 2. 다중 조건 분기용 숫자 변수
const score = ref(85)
</script>

<template>
  <div class="practice-section">
    <h2>v-if, v-else-if, v-else 디렉티브 학습</h2>
    <h3>1) 기본 로그인 상태 스위치</h3>
    <p v-if="isLogged">환영합니다! 회원 전용 화면입니다.</p>
    <p v-else>로그인이 필요합니다. 먼저 로그인해 주세요.</p>
    <button @click="isLogged = !isLogged">
      {{ isLogged ? '로그아웃 하기' : '로그인 하기' }}
    </button>
    <br />
    <h3>2) 성적별 학점 등급 측정 (다중 조건문)</h3>
    <label>현재 점수 입력: </label>
    <input type="number" v-model="score" min="0" max="100" step="5" />
    <br />
    <div v-if="score >= 90" style="color: green; font-weight: bold">합격 등급: A 학점 (훌륭합니다!)</div>
    <div v-else-if="score >= 80" style="color: blue">합격 등급: B 학점 (양호합니다.)</div>
    <div v-else-if="score >= 70" style="color: orange">합격 등급: C 학점 (조금 더 분발하세요.)</div>
    <div v-else style="color: red; font-weight: bold">합격 등급: F 학점 (재시험 대상입니다.)</div>
  </div>
</template>
```
---
### Vue Directive — v-show
조건식의 결과(true/false)에 따라 태그를 화면에 '보여줄지(Show)' 아니면 '숨길지(Hide)' 결정하는 Directive임. 조건이 false가 되더라도 HTML DOM에서 태그를 삭제하지 않고, CSS 속성인 `display: none`을 실시간으로 붙여서 숨기는 방식임.
![]()
`src/components/practices/basic/SampleVShow.vue`
```javascript
<script setup>
import { ref } from 'vue'
const isVisible = ref(true)
</script>

<template>
  <div class="practice-section">
    <h2>v-show 디렉티브 학습</h2>
    <button @click="isVisible = !isVisible">화면 토글하기</button>
    <br />
    <div v-show="isVisible" class="box">
      <p>v-show 상자</p>
      <p>조건이 false가 되면 CSS display: none이 붙습니다.</p>
    </div>
  </div>
</template>

<style scoped>
.box {
  padding: 10px;
  margin-top: 5px;
  color: white;
  border-radius: 5px;
  background-color: #3498db; /* 파란색 */
}
</style>
```
---
### Vue Directive — v-if vs. v-show 비교
| 비교 항목 | v-if (조건부 렌더링) | v-show (조건부 가시성) |
| --- | --- | --- |
| 렌더링 방식 | 실제 DOM 파괴 및 생성. 조건이 맞지 않으면 태그 자체가 존재하지 않음 | CSS `display` 속성 조작. 태그는 항상 존재하며 눈에만 숨김 |
| 초기 렌더링 비용 | 낮음. 처음에 false이면 아예 그리지 않으므로 빠름 | 높음. true/false 상관없이 일단 다 그려 놓으므로 느림 |
| 화면 전환(Toggle) 비용 | 높음. 바뀔 때마다 태그를 새로 부수고 지어야 해서 부담 | 낮음. 단순 CSS 속성 한 줄만 끄고 켜는 것이라 매우 가볍고 빠름 |
| v-else 조합 가능 여부 | 가능 (`v-else-if`, `v-else` 연동 가능) | 불가능 (오직 단독 조건으로만 사용) |
| `<template>` 태그 사용 | 가능 (여러 태그를 한 번에 묶어서 제어 가능) | 불가능 (실제 눈에 보이는 HTML 태그에만 작동) |
| 실무 권장 선택 기준 | 화면 전환이 드물게 일어나는 경우 (로그인 후 회원 화면, 권한별 메뉴 전환 등) | 화면 전환이 매우 빈번하게 일어나는 경우 (모달 팝업, 탭 메뉴, 아코디언 접고 펴기 등) |
---
### Vue Directive — v-for
배열이나 객체를 사용해서 뷰에서 반복적으로 렌더링하는 HTML Element를 생성하는 데 사용하는 Directive임. `v-for`를 쓸 때는 Vue 엔진이 각 태그를 고유하게 식별할 수 있도록 반드시 고유한 값을 `:key` 속성에 바인딩해야 함. 그렇지 않으면 에러 또는 성능 저하가 발생함.
#### 문법 패턴
배열 렌더링:
```html
<div v-for="(item, index) in items" :key="고유값"></div>
<div v-for="item in items" :key="고유값"></div>
```
객체 렌더링:
```html
<div v-for="(value, key, index) in object" :key="고유값"></div>
<div v-for="(value, key) in object" :key="고유값"></div>
<div v-for="value in object" :key="고유값"></div>
```
![]()
`src/components/practices/basic/SampleVFor.vue`
```javascript
<script setup>
import { ref } from 'vue'

const fruits = ref(['사과', '바나나', '딸기'])
const user = ref({
  name: '홍길동',
  age: 25,
  role: '개발자',
})
const items = ref([
  { id: 'prod_101', name: '아이폰' },
  { id: 'prod_102', name: '갤럭시' },
])
</script>

<template>
  <div class="practice-section">
    <h2>v-for 디렉티브 학습</h2>
    <h3>1) 배열 렌더링</h3>
    <ul>
      <li v-for="(fruit, index) in fruits" :key="index">{{ index + 1 }}번 과일: {{ fruit }}</li>
    </ul>
    <h3>2) 객체 렌더링</h3>
    <ul>
      <li v-for="(value, key, index) in user" :key="key">[{{ index }}] {{ key }} : {{ value }}</li>
    </ul>
    <h3>3) 배열 내 객체 렌더링</h3>
    <ul>
      <li v-for="(item, index) in items" :key="item.id">[{{ index }}] {{ item.name }}</li>
    </ul>
  </div>
</template>
```
세 가지 렌더링 패턴 정리:
- 배열 렌더링: `(fruit, index) in fruits` — 값과 인덱스를 동시에 받음. `:key`에는 index 또는 고유 식별자를 씀
- 객체 렌더링: `(value, key, index) in user` — 값, 키 이름, 인덱스 순서로 받음. `:key`에는 key(속성명)를 씀<br>→ 무조건 `(value, key, index)` 의 순서로 받아야함
- 배열 내 객체 렌더링: `(item, index) in items` — 객체 배열을 순회. `:key`에는 객체의 고유 id(`item.id`)를 쓰는 것이 가장 안전함
---
### Vue Directive — v-pre
Vue의 템플릿 컴파일러가 Vue 문법으로 해석(Compile)하지 말고, 써진 그대로 HTML 텍스트로 화면에 표시하라고 지시하는 Directive임. Vue 엔진은 원래 HTML을 읽다가 `{{ }}`나 v-디렉티브를 만나면 자바스크립트 데이터로 갈아 끼우는 연산을 하지만, `v-pre`가 붙은 태그와 그 자식 태그들은 아무런 연산 없이 그대로 출력함.
![]()
`src/components/practices/basic/SampleVPre.vue`
```javascript
<script setup>
import { ref } from 'vue'

const message = ref('안녕하세요!')
</script>

<template>
  <div class="practice-section">
    <h2>v-pre 디렉티브 학습</h2>
    <p>일반 출력: {{ message }}</p>
    <p v-pre>v-pre 출력: {{ message }}</p>
  </div>
</template>
```
- 일반 출력 결과: `안녕하세요!` (변수값으로 치환됨)
- v-pre 출력 결과: `{{ message }}` (문자열 그대로 출력됨)
---
### Vue Directive — v-cloak
Vue 어플리케이션의 렌더링 과정에서 데이터 바인딩이 완료되기 전에 Template을 노출하면 `{{ message }}`같은 해석 안 된 뼈대 문자열이 그대로 노출되는 현상이 발생함. 네트워크가 아주 느린 환경에서 발생하는 현상으로, `v-cloak`은 이런 현상을 예방함. 이 Directive는 혼자서는 작동하지 않고, CSS의 속성 선택자 `[v-cloak]`이 반드시 필요함.
![]()
`src/components/practices/basic/SampleVCloak.vue`
```javascript
<script setup>
import { ref } from 'vue'

const message = ref('느린 네트워크에서도 안전하게 출력되는 메시지!')
</script>

<template>
  <div v-cloak class="practice-section">
    <h2>v-cloak 디렉티브 학습</h2>
    <p>{{ message }}</p>
  </div>
</template>

<style scoped>
/* ⚠ 필수: Vue가 로딩되기 전까지 해당 구역을 물리적으로 숨기는 CSS 규칙 */
[v-cloak] {
  display: none !important;
}
</style>
```
---
### Vue Directive — v-once
해당 요소와 그 하위 요소는 최초에 한 번만 반응형으로 렌더링하고, 그 이후부터는 데이터가 변경되어도 DOM은 갱신되지 않음. Vue 엔진이 데이터를 실시간으로 감시하려면 메모리를 계속 소모해야 하는데, 소개글·약관 내용처럼 처음 백엔드에서 한 번 받아온 이후로는 절대 바뀔 일이 없는 데이터에 `v-once`를 붙여 두면 Vue가 더 이상 감시하지 않아 메모리 부담이 줄어듦.
![]()
`src/components/practices/basic/SampleVOnce.vue`
```javascript
<script setup>
import { ref } from 'vue'

const count = ref(1)
</script>

<template>
  <div class="practice-section">
    <h2>v-once 디렉티브 학습</h2>
    <p>일반 변수 (실시간): {{ count }}</p>
    <p v-once>v-once 변수 (최초 고정): {{ count }}</p>
    <button @click="count++">숫자 증가 버튼</button>
  </div>
</template>
```
---
### Vue Directive — v-memo
지정한 조건(변수)이 바뀔 때만 태그 내부를 업데이트하고, 그렇지 않으면 이전에 그려둔 화면(캐시)을 그대로 재사용하는 Directive임. 문법: `v-memo="[감시할변수1, 감시할변수2]"`.
아래 예시에서 `v-memo="[name]"`을 설정하면 `name`이 바뀔 때만 해당 블록이 리렌더링됨. `age`만 증가시켜도 `name`이 바뀌지 않는 한 블록 내부는 갱신되지 않음.
![]()
`src/components/practices/basic/SampleVMemo.vue`
```javascript
<script setup>
import { ref } from 'vue'

const name = ref('홍길동')
const age = ref(20)
</script>

<template>
  <div class="practice-section">
    <h2>v-memo 디렉티브 학습</h2>
    <div v-memo="[name]" style="padding: 20px; border: 1px solid #42b883; margin-bottom: 10px">
      <p>🪙 v-memo 적용 영역 (기준: name)</p>
      <p>이름: {{ name }}</p>
      <p>나이: {{ age }} (name이 바뀌어야 애도 갱신됨)</p>
    </div>
    <button @click="name = '이순신'">1. 이름 변경 (이순신)</button> &nbsp;
    <button @click="age++">2. 나이 한 살 추가 (age++)</button>
  </div>
</template>
```
---
### Vue Event Handling — v-on (@)
`v-on`은 DOM 요소에 이벤트 리스너를 연결하여 이벤트를 감지하고 처리할 때 사용하는 Directive임. 주로 사용자 입력(클릭, 키보드 입력 등)에 반응하여 원하는 동작을 실행하는 데 사용함. 실무에서는 `@` 축약형을 사용함.
→ JS에서의 eventhandler와 유사함.
```html
<!-- 축약형 없이 사용 -->
<button v-on:click="doSomething">클릭</button>

<!-- 축약형 (@) 사용 -->
<button @click="doSomething">클릭</button>
```
#### 주요 이벤트 목록
| 이벤트 이름 | 설명 |
| --- | --- |
| `click` | 클릭 이벤트 |
| `submit` | 폼 제출 이벤트 |
| `keyup` | 키보드 키를 뗐을 때 |
| `keydown` | 키보드를 눌렀을 때 |
| `input` | 입력 필드 변경 시 |
| `change` | 입력 값 변경 후 포커스 아웃 시 |
| `mouseenter` | 마우스가 요소 위로 올라올 때 |
| `mouseleave` | 마우스가 요소에서 벗어날 때 |
---
### Vue Event Handling — Event Handler 종류
이벤트 핸들러는 두 가지 방식으로 작성함.
Inline Handler — 태그 안에서 즉시 간단한 자바스크립트 연산을 처리할 때 사용 (숫자 증감, 스위치 토글 등):
```html
<button @click="count++">클릭 수: {{ count }}</button>
```
Method Handler — 복잡한 로직은 `<script setup>` 구역에 함수를 만들어서 연결. `@click="handleClick"`처럼 괄호 없이 함수 이름만 넘기면, Vue는 이 함수를 호출하는 것이 아니라 함수의 참조(주소) 자체를 이벤트 리스너로 등록함. `button.addEventListener('click', handleClick)`과 동일한 동작임:
→ 즉, “괄호 없이” 함수의 참조 주소 자체를 이벤트 리스너로 등록해서 동작하는 것임
```html
<button @click="handleClick">클릭하세요</button>
```
---
### Vue Event Handling — Event Handler Example
![]()
`src/components/practices/basic/SampleVOn.vue`
```javascript
<script setup>
import { ref } from 'vue'
const count = ref(0)

// 메서드 핸들러 함수 정의
const showAlert = () => {
  alert('함수가 성공적으로 호출되었습니다!')
}
</script>

<template>
  <div class="practice-section">
    <h2>v-on 이벤트 핸들링 기초</h2>
    <h3>1) 인라인 연산 처리</h3>
    <p>현재 카운트: {{ count }}</p>
    <button @click="count++">1씩 증가</button>
    <br />
    <h3>2) 스크립트 함수 호출</h3>
    <button @click="showAlert">알림창 띄우기</button>
  </div>
</template>
```
---
### Vue Event Handling — JavaScript Event Object
Event Object란 사용자가 웹페이지에서 버튼을 클릭하거나, 키보드를 누르거나, 마우스를 움직이는 등의 이벤트를 발생시켰을 때 브라우저가 자동으로 생성하는 객체임.
#### Event Object 주요 Properties
| 분류 | 속성명 | 데이터 타입 | 설명 |
| --- | --- | --- | --- |
| 공통 | `e.target` | HTMLElement | 이벤트를 발생시킨 HTML 태그. `e.target.value`(입력값), `e.target.tagName`(BUTTON, INPUT..) |
|  | `e.currentTarget` | HTMLElement | 이벤트 리스너가 걸려있는 HTML 태그 (부모 태그에 이벤트를 걸었을 때 `e.target`과 달라짐) |
|  | `e.type` | String | 발생한 이벤트의 종류 (예: click, keyup, submit 등) |
|  | `e.timeStamp` | Number | 웹페이지가 로드된 후 이벤트를 실행하기까지 걸린 시간(ms) |
| 마우스 | `e.clientX / e.clientY` | Number | 브라우저 화면(Viewport) 기준 마우스 커서의 X, Y 좌표 |
|  | `e.pageX / e.pageY` | Number | 전체 HTML 문서(Document) 기준 마우스 커서의 X, Y 좌표 |
|  | `e.screenX / e.screenY` | Number | 사용자의 모니터 화면 기준 마우스 커서의 X, Y 좌표 |
|  | `e.button` | Number | 클릭한 마우스 버튼 번호 (0: 왼쪽, 1: 휠/가운데, 2: 오른쪽) |
| 키보드 | `e.key` | String | 사용자가 누른 키의 실제 문자 값 (예: Enter, ArrowUp, a, A, Escape) |
|  | `e.code` | String | 사용자가 누른 물리적인 키보드 자판의 위치 값 (예: Enter, KeyA, Digit1, Escape) |
|  | `e.shiftKey` | Boolean | 이벤트를 유발할 때 Shift 키를 같이 누르고 있었는지 여부 |
|  | `e.ctrlKey / e.altKey` | Boolean | 이벤트를 유발할 때 Ctrl 또는 Alt 키를 같이 누르고 있었는지 여부 |
#### Event Object 주요 Methods
| Method | 주요 역할 | 실무 핵심 활용처 |
| --- | --- | --- |
| `e.preventDefault()` | 브라우저가 특정 태그에 대해 가지는 기본 고유 동작을 강제로 중단 | `<a>` 태그 클릭 시 링크 이동 방지, `<form>` submit 시 페이지 새로고침 방지 |
| `e.stopPropagation()` | 이벤트가 부모 태그로 타고 올라가는 이벤트 버블링(Bubbling)을 완전히 차단 | 팝업창(자식) 내부 클릭 시 팝업창 뒤편의 배경(부모) 닫기 이벤트까지 동시에 실행되는 버블 버그 방지 |
| `e.stopImmediatePropagation()` | 현재 태그에 걸려있는 다른 이벤트 리스너들의 실행까지 전부 중단시키고 버블링도 막음 | 하나의 버튼에 여러 개의 클릭 함수가 중복으로 얽혀 있을 때, 첫 번째 함수만 실행하고 뒤는 싹 다 마비시키고 싶을 때 |
---
### Vue Event Handling — Event Object 사용 패턴
Vue에서 Event 객체(`$event`)를 받는 Pattern 2가지:
- Method Handler에 함수 이름만 적어서 호출하면, JavaScript Engine이 첫 번째 인자로 이벤트 객체를 묵시적으로 전달함. Syntax: `@click="handleEvent"` → 스크립트: `const handleEvent = (e) => { ... }` <br>→ `$event` 을 안 적음
- 함수에 특정 데이터를 던지면서 이벤트 객체도 동시에 넘기고 싶을 때는, Vue가 제공하는 특별한 기호인 `$event`를 명시적으로 적어주어야 함. Syntax: `@click="handleEvent('홍길동', $event)"`
![]()
`src/components/practices/basic/SampleVOnEvent.vue`
```javascript
<script setup>
import { ref } from 'vue'

const position = ref('')
const tagName = ref('')
const getOnlyEvent = (e) => {
  position.value = `좌표: X=${e.clientX}, Y=${e.clientY}`
}
const getWithParam = (name, e) => {
  tagName.value = `대상:${name} / 클릭된 태그:${e.target.tagName}`
}
</script>

<template>
  <div class="practice-section">
    <h2>v-on 이벤트 객체($event) 활용</h2>
    <p>좌표: {{ position }}</p>
    <p>태그: {{ tagName }}</p>
    <button @click="getOnlyEvent">클릭 좌표 알아내기</button>
    <button @click="getWithParam('회원A', $event)">회원 정보와 태그 확인</button>
  </div>
</template>
```
---
### Vue Event Handling — Event Modifier (이벤트 수식어)
![]()
Event Modifier는 이벤트 리스너의 기본 동작을 보완하거나 제어하는 데 사용되는 특수 접미어임. `v-on:submit.prevent="onSubmit"`처럼 이벤트명 뒤에 `.수식어`를 붙여 사용함.
#### 주요 Event Modifier
| 분류 | 수식어 | 실제 자바스크립트 동작 | 주요 기능 및 활용처 |
| --- | --- | --- | --- |
| 공통 | `.prevent` | `e.preventDefault()` | 태그의 기본 동작 방지 (폼 제출 시 새로고침 방지, 링크 이동 방지) |
|  | `.stop` | `e.stopPropagation()` | 이벤트 버블링 차단 (자식 버튼 클릭 시 부모 박스 이벤트로 전염되는 것 방지) |
|  | `.once` | 최초 1회 트리거 후 리스너 제거 | 이벤트를 딱 한 번만 실행 (설문조사 제출 버튼 중복 클릭 방지) |
|  | `.self` | `e.target === e.currentTarget` | 오직 자기 자신을 직접 클릭했을 때만 이벤트 실행 (자식 태그 클릭 시 패스) |
|  | `.capture` | 캡처링 단계에서 이벤트 감지 | 버블링과 반대로 부모 이벤트가 자식보다 먼저 터지게 설정 |
|  | `.passive` | scroll 성능 최적화 | 모바일 화면에서 무거운 스크롤/터치 이벤트 부드럽게 처리 |
| 키보드 | `.enter` | Enter 키 | 로그인, 댓글 입력 후 엔터 쳤을 때 즉시 전송 |
|  | `.tab` | Tab 키 | 다음 입력 칸으로 포커스가 넘어갈 때 사전 유효성 검사 |
|  | `.delete` | Delete 또는 Backspace 키 | 텍스트 칩(Tag)을 선택하고 지우기 키를 눌러 삭제할 때 |
|  | `.esc` | Escape 키 | 팝업창이나 모달 열린 상태에서 Esc 누르면 창 닫기 |
|  | `.space` | Space 키 | 체크박스 형태의 UI에서 스페이스바 누르면 토글 처리 |
|  | `.up / .down` | 방향키 위/아래 | 자동완성 검색어 목록에서 화살표로 리스트 이동할 때 |
|  | `.left / .right` | 방향키 왼쪽/오른쪽 | 이미지 슬라이더(캐러셀)에서 화살표 키로 사진 넘기기 |
| 시스템 | `.ctrl` | Ctrl 키 | Ctrl + 클릭으로 링크를 새 탭에서 열 때 전용 로직 처리 |
|  | `.alt` | Alt 키 | 일반 클릭과 Alt + 클릭의 동작을 다르게 분기할 때 |
|  | `.shift` | Shift 키 | Shift + Enter를 누르면 전송되지 않고 인풋창 줄바꿈 처리 |
|  | `.meta` | 윈도우 키 / 커맨드 키 (Mac) | OS 전용 시스템 단축키 조합을 웹앱에 이식할 때 |
|  | `.exact` | 오직 지정한 키만 눌렸을 때 지정 | `@click.ctrl.exact`: 다른 키 안 섞이고 쌩 Ctrl만 누르고 클릭해야 함 |
| 마우스 | `.left` | 마우스 왼쪽 버튼 (기본값) | 일반적인 버튼 클릭 처리 |
|  | `.right` | 마우스 오른쪽 버튼 | 웹페이지 순정 메뉴 대신 개발자가 만든 커스텀 우클릭 컨텍스트 메뉴를 띄울 때 |
|  | `.middle` | 마우스 휠 (가운데 버튼) | 마우스 휠 클릭으로 빠른 탭 닫기나 특수 스크롤 기능을 넣을 때 |
![]()
`src/components/practices/basic/SampleVOnModifier.vue`
```javascript
<script setup>
const handleLink = () => {
  alert('수식어 덕분에 네이버로 이동하지 않고 함수만 실행됩니다!')
}

const handleBox = () => {
  alert('부모 박스가 클릭되었습니다!')
}

const handleChild1 = () => {
  alert('1번 자식 클릭!')
}
const handleChild2 = () => {
  alert('2번 자식(나만 켜짐) 클릭!')
}

// 추가 실습: .once 수식어 (한 번만 실행되는 이벤트) 확인용
let clickCount = 0
const handleOnce = () => {
  clickCount++
  alert(`이 알림은 최초 1회만 뜹니다. (호출 횟수: ${clickCount})`)
}
</script>

<template>
  <div class="practice-section">
    <h2>이벤트 수식어(Modifiers) 학습</h2>
    <h3>1) .prevent (기본 동작 막기)</h3>
    <a href="https://www.naver.com" @click.prevent="handleLink">네이버 링크</a>
    <br />

    <h3>2) .stop (이벤트 버블링 막기)</h3>
    <div @click="handleBox" style="padding: 20px; background-color: #eee">
      <p>부모 영역 (클릭 시 alert 발동)</p>
      <button @click="handleChild1">버블링 발생 버튼</button>
      <button @click.stop="handleChild2">버블링 차단 버튼</button>
    </div>

    <!-- 추가 실습: .once 수식어로 이벤트가 딱 한 번만 실행되는지 확인 -->
    <br />
    <h3>추가 실습 - .once (한 번만 실행)</h3>
    <button @click.once="handleOnce">한 번만 반응하는 버튼</button>
  </div>
</template>
```
---
### Form Data Binding — Two-way Data Binding with v-model
`v-model`은 HTML의 입력 요소의 값과 JavaScript 데이터(Ref)를 묶어, 한쪽이 바뀌면 다른 한쪽도 실시간으로 똑같이 바뀌게 만드는 양방향(Two-way) 바인딩 장치임.
내부 작동 원리: `v-model`은 `:value`(단방향 바인딩)와 `@input`(이벤트 감지)를 결합한 축약 문법임. `v-model="text2"`는 아래와 동일하게 작동함:
```html
<input type="text" :value="text2" @input="(e) => (text2 = e.target.value)" />
```
![]()
`src/components/practices/basic/SampleVModel.vue`
```javascript
<script setup>
import { ref } from 'vue'
const text1 = ref('') // v-model용 변수
const text2 = ref('') // 원리 이해용 변수
</script>

<template>
  <div class="practice-section">
    <h2>v-model 양방향 데이터 바인딩</h2>
    <h3>1) v-model 축약 문법 (양방향)</h3>
    <input type="text" v-model="text1" placeholder="여기에 입력하세요" />
    <p>입력된 값: <strong>{{ text1 }}</strong></p>
    <h3>2) v-model의 내부 작동 원리 (단방향 + 이벤트)</h3>
    <input type="text" :value="text2" @input="(e) => (text2 = e.target.value)" placeholder="원리 파악용 입력창" />
    <p>입력된 값: <strong>{{ text2 }}</strong></p>
  </div>
</template>
```
---
### Form Data Binding — v-model 변수 선언 규칙
HTML Form 요소별로 `v-model`에 연결할 `ref` 초기값 타입이 다름. HTML 요소의 특성에 맞게 초기값을 선언해야 예외나 의도치 않은 버그를 막을 수 있음.
| Form 태그 종류 | 연결된 ref 초기값 타입 | v-model이 변수에 담아주는 실제 값 |
| --- | --- | --- |
| `textarea` (장문 입력) | `ref('')` (문자열) | 사용자가 입력한 장문의 줄바꿈 포함 텍스트 |
| `input[type="checkbox"]` (단일) | `ref(false)` (불리언) | 체크하면 true, 해제하면 false |
| `input[type="checkbox"]` (다중) | `ref([])` (배열) | 체크된 항목들의 value 속성 값이 배열에 차곡차곡 쌓임 |
| `input[type="radio"]` (단일선택) | `ref('')` (문자열) | 여러 라디오 중 사용자가 최종 선택한 하나의 value 값 |
| `select` (드롭다운) | `ref('')` (문자열) | 사용자가 선택한 `<option>`의 value 값 |
내부 이벤트 차이:
- 일반 텍스트 입력(`input`, `textarea`)은 타이핑할 때마다 반응하는 `@input` 이벤트를 기반으로 작동함
- 선택형 요소(`checkbox`, `radio`, `select`)는 값이 확정되는 시점에 반응하는 `@change` 이벤트를 기반으로 작동함
---
### Form Data Binding — Form Elements Code Example
![]()
`src/components/practices/basic/SampleVModelForm.vue`
```javascript
<script setup>
import { ref } from 'vue'
const comment = ref('')
const isAgreed = ref(false)        // 단일 체크박스는 Boolean
const favoriteFruits = ref([])     // 다중 체크박스는 반드시 배열([])로 시작!
const gender = ref('')
const selectedCar = ref('')
</script>

<template>
  <div class="practice-section">
    <h2>모든 HTML Form 요소와 v-model 매핑</h2>

    <div>
      <h3>1) Textarea (장문 텍스트)</h3>
      <textarea v-model="comment" placeholder="의견을 남겨주세요"></textarea>
      <p>데이터 상태: <span>{{ comment }}</span></p>
    </div>

    <div>
      <h3>2) 단일 Checkbox (동의 여부)</h3>
      <label><input type="checkbox" v-model="isAgreed" /> 약관에 동의합니다.</label>
      <p>데이터 상태: <span>{{ isAgreed }}</span></p>
    </div>

    <div>
      <h3>3) 다중 Checkbox (복수 선택 -> 배열에 저장)</h3>
      <label><input type="checkbox" value="사과" v-model="favoriteFruits" /> 사과</label> &nbsp;
      <label><input type="checkbox" value="바나나" v-model="favoriteFruits" /> 바나나</label> &nbsp;
      <label><input type="checkbox" value="딸기" v-model="favoriteFruits" /> 딸기</label>
      <p>데이터 상태 (배열): <span>{{ favoriteFruits }}</span></p>
    </div>

    <div>
      <h3>4) Radio (단일 선택)</h3>
      <label><input type="radio" value="남성" v-model="gender" /> 남성</label> &nbsp;
      <label><input type="radio" value="여성" v-model="gender" /> 여성</label>
      <p>데이터 상태: <span>{{ gender }}</span></p>
    </div>

    <div>
      <h3>5) Select (드롭다운 선택)</h3>
      <select v-model="selectedCar">
        <option value="">-- 선택하세요 --</option>
        <option value="tesla">테슬라</option>
        <option value="hyundai">현대자동차</option>
        <option value="bmw">BMW</option>
      </select>
      <p>데이터 상태: <span>{{ selectedCar }}</span></p>
    </div>
  </div>
</template>
```
---
### Form Data Binding — v-model Modifiers
v-model 수식어는 입력 요소의 동작 방식이나 수집되는 데이터 형태를 손쉽게 제어할 수 있도록 Vue가 제공하는 편의 기능(Syntactic Sugar)임. 수식어는 필요한 만큼 이어 붙여서 사용 가능함 (Modifier Chaining).
| 수식어 | 기본 동작 이벤트 | 수식어 적용 후 동작 | 주요 사용 목적 |
| --- | --- | --- | --- |
| `.lazy` | `@input` (타이핑할 때마다 반영) | `@change` (포커스를 잃거나 Enter 시 반영) | 불필요한 실시간 상태 업데이트 및 API 요청 방지 |
| `.number` | String 타입 수집 | Number 타입으로 자동 형변환 | 숫자 데이터 입력 시 자동 타입 변환 처리 |
| `.trim` | 입력값 그대로 수집 | 양끝 공백(Whitespace) 제거 후 수집 | 공백 입력으로 인한 Validation 오류 예방 |
![]()
![]()
`src/components/practices/basic/SampleVModelModifiers.vue`
```javascript
<script setup>
import { ref } from 'vue'

// v-model Modifiers 실습용 reactive 변수 선언
const lazyText = ref('')
const age = ref('')
const userEmail = ref('')
const price = ref('')
</script>

<template>
  <div class="practice-section">
    <h2>v-model 수식어 (Modifiers) 활용</h2>

    <!-- 1) .lazy 수식어 실습 -->
    <section style="margin-bottom: 20px">
      <h3>1) .lazy 수식어 (change 이벤트 시점 반영)</h3>
      <input type="text" v-model.lazy="lazyText" placeholder="입력 후 Enter 또는 외부 클릭" />
      <p>실시간이 아닌 확정된 값: <strong>{{ lazyText }}</strong></p>
    </section>

    <!-- 2) .number 수식어 실습 -->
    <section style="margin-bottom: 20px">
      <h3>2) .number 수식어 (Number 타입 자동 형변환)</h3>
      <input type="text" v-model.number="age" placeholder="나이를 입력하세요" />
      <p>입력된 값: <strong>{{ age }}</strong></p>
      <p>데이터 타입: <strong>{{ typeof age }}</strong></p>
    </section>

    <!-- 3) .trim 수식어 실습 -->
    <section>
      <h3>3) .trim 수식어 (양끝 공백 자동 제거)</h3>
      <input type="text" v-model.trim="userEmail" placeholder="앞뒤 공백을 포함해 입력해 보세요" />
      <p>공백 제거된 값: <strong>"{{ userEmail }}"</strong></p>
      <p>문자열 길이: <strong>{{ userEmail.length }}</strong></p>
    </section>

    <!-- 4) 수식어 체이닝 (Chaining) 실습 -->
    <section>
      <h3>4) Chaining (수식어 체이닝: .trim.number)</h3>
      <input type="text" v-model.trim.number="price" placeholder="공백과 숫자를 섞어 입력해 보세요" />
      <p>처리된 값: <strong>"{{ price }}"</strong></p>
      <p>데이터 타입: <strong>{{ typeof price }}</strong></p>
    </section>
  </div>
</template>
```
---
### Vue Style — Scoped Style & External Style
#### Scoped Style
SFC 파일의 `<style>` 영역에 작성된 스타일은 기본적으로 모든 컴포넌트에 전역 적용됨. `<style scoped>`를 사용하면 현재 컴포넌트 내부에 선언된 HTML 태그에만 적용되고, 다른 컴포넌트에는 영향을 주지 않음.
| 방식 | 적용 범위 |
| --- | --- |
| `<style>` | 프로젝트 전체 컴포넌트에 전역 적용 |
| `<style scoped>` | 현재 컴포넌트 내부 태그에만 적용 |
#### External Style
- 공통 CSS나 외부 라이브러리 CSS를 사용하는 방법
- 프로젝트 전체에 적용할 공통 스타일은 `src/main.js`에 등록함
- 특정 컴포넌트에 외부 CSS 파일을 적용할 때는 `<style>` 방 내부에서 자바스크립트의 `@import` 문법을 사용함
![]()
`src/components/practices/basic/SampleStyle.vue`
```javascript
<script setup>
// 자바스크립트 방은 깨끗하게 비워둡니다.
</script>

<template>
  <div class="practice-section">
    <h2>Scoped 스타일 및 외부 CSS 활용</h2>
    <p class="title">이 글자는 이 컴포넌트 내부에서만 빨간색이 됩니다.</p>
    <button class="btn-external">외부 CSS에서 불러온 버튼 스타일</button>
  </div>
</template>

<style scoped>
/* 내 방 전용 타이틀 디자인 */
.title {
  color: #ff7675;
  font-weight: bold;
  font-size: 18px;
}
</style>

<style>
/* ⚠ 외부 스타일 파일(예: 버튼 디자인 뭉치)을 이 방 안으로 쏙 가리켜 가져옵니다 */
@import '@/assets/challenge.css';
</style>
```
---
<empty-block/>
