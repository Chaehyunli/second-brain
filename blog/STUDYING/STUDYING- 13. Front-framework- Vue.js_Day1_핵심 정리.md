---
title: "[STUDYING] 13. Front-framework: Vue.js_Day1_핵심 정리"
created: 2026-08-01
updated: 2026-08-01
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-31
source_url: https://ch010104.tistory.com/329
---
# [STUDYING] 13. Front-framework: Vue.js_Day1_핵심 정리

## 원문

https://ch010104.tistory.com/329

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

Vue.js는 사용자 인터페이스(UI) 구축을 목적으로 하는 Front-end JavaScript Framework임. JavaScript와 TypeScript를 모두 지원하며, 간결한 문법·반응형 데이터 바인딩·컴포넌트 기반 구조·가상 DOM·트랜지션 효과 지원이 주요 특징임.

유사한 프레임워크로 React·Angular가 있으나, Vue는 그 중 가장 가볍고 진입 장벽이 낮은 편임.

## 원문 기반 개념 정리

### Vue.js 개요

Vue.js는 사용자 인터페이스(UI) 구축을 목적으로 하는 Front-end JavaScript Framework임. JavaScript와 TypeScript를 모두 지원하며, 간결한 문법·반응형 데이터 바인딩·컴포넌트 기반 구조·가상 DOM·트랜지션 효과 지원이 주요 특징임.

유사한 프레임워크로 React·Angular가 있으나, Vue는 그 중 가장 가볍고 진입 장벽이 낮은 편임.

### JavaScript vs. TypeScript

Vue 버전별 언어 선택 정리:

Vue 2: 핵심 코드가 JavaScript로 작성됨

Vue 3: 코어 엔진이 100% TypeScript로 전면 재작성됨

Vue 2·3 모두 개발자가 프로젝트 단위로 JavaScript 또는 TypeScript를 선택해 사용 가능함

### Vue.js 아키텍처 — MVVM

Vue.js는 MVVM(Model-View-ViewModel) 아키텍처 패턴을 따름. MVVM은 UI를 담당하는 View와 데이터를 처리하는 Model 사이에 ViewModel을 두어, 화면 렌더링 로직과 데이터 처리 로직을 완전히 분리하는 구조임.

### 세 레이어의 역할

### 동작 흐름

View에서 사용자 이벤트 발생 → ViewModel의 DOM Listeners가 감지 → Model 업데이트

Model 데이터 변경 → ViewModel의 Data Bindings가 반영 → View(DOM) 자동 갱신

이 쌍방향 연동 덕분에 개발자는 DOM 조작 코드 없이 데이터 상태만 관리하면 됨

### Frontend Framework 3대장 비교

현재 프론트엔드 생태계의 주요 UI 프레임워크·라이브러리는 Vue.js, React, Angular 세 가지임.

### DOM이란

DOM(Document Object Model)은 브라우저가 HTML 문서를 파싱한 뒤 메모리에 만드는 트리 구조의 객체 모델임. `<html>` → `<body>` → `<div>` → `<p>` 식으로 태그가 노드(node)로 표현되며, JavaScript는 이 트리를 통해 화면 요소를 읽거나 변경할 수 있음.

문제는 DOM 조작 비용이 큰 편이라는 점임. 요소 하나를 바꿔도 브라우저는 레이아웃 계산·페인팅을 다시 수행하므로, 변경이 잦을수록 성능 부담이 커짐.

### 실제 DOM vs. Virtual DOM

Vue·React가 Virtual DOM을 쓰는 이유는 "실제 DOM 접근 횟수를 줄이기 위해서"임. 데이터가 바뀌면 먼저 Virtual DOM끼리 비교해 달라진 노드만 추려낸 뒤, 그 부분만 실제 DOM에 한 번에 적용하는 방식임.

### Vue.js Features — Virtual DOM

브라우저의 Real DOM 조작은 비용이 큰 연산임. DOM이 수정될 때마다 브라우저는 Layout 재계산(Reflow)과 화면 재색칠(Repaint)을 수행하기 때문임. 예를 들어 3,000개의 노드가 있는 상태에서 연속적인 상태 변경이 일어나면, 변경마다 Layout/Paint 연산이 반복되어 화면이 느려짐. 10번의 데이터 변화 = 10번의 브라우저 렌더링 연산이 즉시 발생하는 구조임.

Vue.js는 Virtual DOM을 도입해 이 문제를 해결함.

Virtual DOM은 실제 브라우저 DOM의 메모리상 JavaScript 복사본임. 개발자가 DOM을 직접 조작하지 않아도, 상태 변화만 선언하면 Vue가 최적의 최소 DOM 조작 지점을 자동으로 추적함.

Batch 처리: 한 이벤트 안에서 데이터가 여러 번 바뀌어도, 모두 끝난 시점에 단 한 번만 실제 DOM에 반영함. 10번의 변경 → 1번의 실제 DOM 업데이트로 줄어드는 것임.

### 동작 흐름 비교

Virtual DOM 방식에서는 Web page와 Virtual DOM이 먼저 동기화되고, Virtual DOM이 변경된 부분만 추려 Real DOM에 최소한으로 반영함.

### Vue.js Features — Two-Way Data Binding

양방향 데이터 바인딩(Two-Way Data Binding)은 Model(JavaScript 데이터)이 바뀌면 View(화면)가 자동으로 바뀌고, 반대로 View(화면 입력)가 바뀌면 Model도 동시에 업데이트되는 방식임. Vue에서는 v-model directive로 이를 구현함.

### 흐름 정리

Template이 컴파일되어 View(화면)를 생성함

Model은 Single Source of Truth로, 지속적으로 View와 동기화됨

View 변경 → Model 업데이트 / Model 변경 → View 업데이트, 두 방향 모두 자동으로 처리됨

React의 단방향 데이터 흐름(Model → View만)과 달리, Vue의 양방향 바인딩은 폼 입력 처리 등에서 별도의 이벤트 핸들러 없이도 Model과 View를 동기화할 수 있어 코드가 간결해짐.

### Vue.js Features — Component Based Architecture

컴포넌트 기반 개발은 웹페이지를 통째로 만들지 않고, 독립적인 UI 부품(Component)들을 각각 만든 뒤 조립하여 화면을 완성하는 방식임.

### 컴포넌트의 구조

각 컴포넌트는 하나의 .vue 파일 안에 세 가지 영역을 응집시킴(Encapsulation).

### 핵심 특성

Reusability: 잘 만든 컴포넌트는 여러 페이지에서 재사용 가능해 중복 코드가 제거됨. 예를 들어 Page A와 Page B가 동일한 Header/Footer 컴포넌트를 공유함.

Tree Structure: 컴포넌트들은 부모-자식 트리 구조로 조합됨.

부모 → 자식: Props를 내려줌(Pass Props)

자식 → 부모: 이벤트를 올려 상태 변경을 알림(Emit Events)

이 구조 덕분에 컴포넌트 간 데이터 흐름이 명확하게 분리되고, 각 컴포넌트는 독립적으로 개발·테스트·유지보수가 가능함.

### Vue.js 렌더링 — CSR vs. SSR

렌더링 방식의 핵심 질문은 "화면을 구성하는 HTML 파일을 어디서 최종적으로 완성하는가?"임.

CSR (Client-Side Rendering): 브라우저(클라이언트)가 JavaScript를 실행하여 화면을 직접 그리는 방식. Vue.js의 기본 동작 렌더링 방식임. → 사용자의 화면(index.html)에서 데이터와 화면(vue나 js)이 만나서 조립됨.

SSR (Server-Side Rendering): 서버에서 데이터까지 모두 주입하여 완성된 HTML 파일을 만들어 브라우저에 내려주는 방식. Vue 생태계에서는 주로 Nuxt.js 프레임워크로 구현함. → Spring Boot의 Thymleaf가 이에 해당함. → 백엔드 코드에서 이미 화면과 데이터를 조립해서 클라이언트에게 던짐 → 백엔드 서버에서 데이터가 포함된 html 파일 + css 파일을 따로, 브라우저로 보내서 클라이언트 브라우저에서 조립해서 렌더링함

### Vue.js 렌더링 — SPA (Single Page Application)

SPA는 브라우저가 서버로부터 오직 하나의 HTML 파일(index.html)만 받아와서 구동되는 웹 애플리케이션 구조임.

### MPA vs. SPA 동작 비교

전통적인 MPA(Multi Page Application)에서는 사용자가 메뉴를 클릭할 때마다 서버에 새 HTML 파일을 요청하고, 브라우저는 전체 페이지를 새로 렌더링함.

SPA(Vue.js)에서는 최초 진입 시 index.html + JS/CSS를 한 번만 받아오고, 이후 페이지 전환은 JavaScript가 필요한 부분만 교체하여 렌더링함. 추가 데이터가 필요하면 백엔드 API 서버에 JSON만 요청함. 브라우저는 페이지 이동 없이 화면을 갱신함.

### Vue.js 렌더링 — SPA vs. MPA 상세 비교

### Vue.js 렌더링 — SPA 추가 기술 요소 및 장단점

### Vue SPA 생태계 주요 도구

### SPA 장점

압도적인 UX: 페이지 이동이 데스크톱 소프트웨어처럼 즉각적임

네트워크 효율성: 한 번 로딩된 CSS·JS 등을 재사용하고 데이터만 주고받으므로 전체 네트워크 트래픽이 크게 절감됨

프론트/백엔드 분리: 프론트엔드는 Vue만, 백엔드는 데이터만 담당하므로 팀 간 협업 및 서버 분산이 명확함

### SPA 단점

초기 로딩 속도: 모든 JavaScript 로직이 하나의 app.js로 묶여 처음에 다운로드되므로, 첫 접속 시 대기 시간이 발생할 수 있음

SEO 취약: 검색 로봇이 들어왔을 때 알맹이 없는 빈 index.html만 보이기 때문에 검색 노출 점수를 따기 어려움

### 뷰 프로젝트 구조

VS Code에서 SKALA-VUE 프로젝트를 열면 아래와 같은 폴더/파일 구조가 나타남.

### Frontend Project Tools — 도구의 필요성

현대 웹 UI 개발은 세 가지 이유로 전용 도구가 필요함.

파일 분할과 모듈화: 유지보수·재사용성을 위해 JavaScript를 여러 파일로 나누어 작성하지만, 배포 시에는 하나로 묶어야 함

사이즈 최적화: 배포 시 전체 파일을 묶고 크기를 줄여야 함

브라우저 호환: 구 버전 브라우저에서 ES6 이후 문법이나 TypeScript를 사용하려면 변환 과정이 필요함

개발 편의를 위한 자동화도 도구가 담당함. 변경 시 자동 새로고침(Live Reload, HMR), 코드 압축·이미지 최적화·CSS 전처리, .vue·.scss·.ts 등 다양한 확장자 처리가 이에 해당함.

### 도구 유형 정리

### Frontend Project Tools — Vite

Vite는 Vue 소스 코드를 Build하고, 로컬 개발 서버를 띄워주는 Frontend Build 도구임.

### 주요 기능 세 가지

Compile: .vue나 TypeScript를 순수한 HTML, JavaScript, CSS로 변환함

Local 개발 서버 제공: 코드를 실시간으로 반영(HMR, Hot Module Replacement)되도록 로컬 웹 서버에 컴파일된 소스를 제공함. 파일 하나만 바꿔도 전체를 다시 빌드하지 않고 해당 모듈만 교체함

Bundling: 수백 개의 작은 소스코드 파일들을 배포에 적합하도록 몇 개의 압축된 덩어리 파일로 묶어줌 (Staging/Production 서버용)

참고로 과거에 사용하던 Vue-CLI + Webpack 조합은 Vite 이전 기술로, 현재는 더 이상 사용하지 않음.

### Frontend Project Tools — npm

NPM(Node Package Manager)은 오픈소스 라이브러리 저장소이자 Node.js 패키지 관리 도구임.

### npm 구성 요소

npm Registry: JavaScript 라이브러리를 업로드해 두는 공식 Cloud Server

npm CLI: npm install 같은 명령어를 수행하는 커맨드라인 인터페이스

npmjs.com: 등록된 패키지들을 웹 브라우저로 확인할 수 있는 공식 포털 사이트

### 주요 npm 명령어

### Project 구조 — 핵심 폴더와 파일

npm create vue@latest로 생성된 Vue 프로젝트의 디렉토리 구조는 아래와 같음.

### Project 구조 — package.json

package.json은 프로젝트의 핵심 명세서로, 네 가지 영역으로 구성됨.

```text
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

### Meta 정보

name: 프로젝트 이름

version: 0.0.0은 [major].[minor].[patch] 형식

private: true: 실수로 npm 레지스트리에 배포(publish)되는 것을 방지

type: "module": .js 파일들의 기본 모듈 시스템을 ESM(import/export)으로 지정

### scripts

npm run 명령어로 실행하는 스크립트 목록.

dev: 개발 서버 실행

build: dist 폴더에 배포용 정적 자원 번들링

### 의존성 모듈

dependencies: 애플리케이션 실행에 필요한 패키지

devDependencies: 개발 중에만 필요한 패키지

### engines

node: 프로젝트가 정상 동작하기 위해 요구되는 Node.js 최소 실행 버전

### Project 구조 — index.html

브라우저가 최초로 읽는 단 하나의 HTML 파일(Entry Point)임. 핵심 라인은 두 줄.

```text
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

Line 10 `<div id="app">``</div>`: Vue 엔진이 Component들을 실시간으로 바꿔 끼워 화면을 그리는 마운트 대상 컨테이너

Line 11 `<script type="module" src="/src/main.js">`: main.js를 모듈 형식으로 연결하여 이 시점부터 Vue 어플리케이션 코드가 실행됨

### Project 구조 — main.js

Vue 어플리케이션을 초기화하고 구성하는 진입 스크립트임. 코드 흐름 순서대로 정리하면 아래와 같음.

```typescript
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

Line 1: main.css를 불러와 프로젝트 전체·모든 컴포넌트에 전역 적용

Line 3~4: vue에서 createApp, pinia에서 createPinia 함수를 가져옴

Line 6~7: App.vue(루트 컴포넌트)와 router를 가져옴

Line 9: createApp(App)으로 Vue 어플리케이션 인스턴스 생성. 아직 화면에 그려지지 않은 상태

Line 11~12: app.use(createPinia())와 app.use(router)로 Pinia·Router 플러그인 등록

Line 14: app.mount('#app')으로 index.html의 `<div id="app">`에 물리적으로 넣으며(mount) 화면 렌더링 시작

createApp()이 반환하는 app 객체는 use, component, directive 등 플러그인 설치나 전역 자원 등록에 사용하는 컨텍스트 API를 내장하고 있음. 최상위 컴포넌트(App.vue)를 기점으로 하위 컴포넌트들이 Component Tree를 형성하며 렌더링 파이프라인을 구축함.

### Project 구조 — App.vue

App.vue는 Vue 어플리케이션의 Root Component 역할을 함.

```html
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

`<script setup>`: vue-router의 RouterLink·RouterView와 HelloWorld.vue 컴포넌트를 import함

`<template>`: `<HelloWorld msg="You did it!" />`로 HelloWorld 컴포넌트를 배치하고 Props로 msg 값을 전달함

`<RouterLink to="/">`: HTML `<a>` 태그로 변환되지만 브라우저 새로고침을 막고 주소창만 바꿈

`<RouterView />` (Line 20): 주소창 변경에 따라 해당 경로의 컴포넌트가 동적으로 끼워지는 가변형 주입 구역. SPA 페이지 전환의 핵심 → js에 정의된 것을 바탕으로, 이 부분이 바뀌어 끼워짐

→ 기본적으로 SFC(.vue 파일)에는 template, script, style로 구성됨

### SFC (Single File Component)

Vue 컴포넌트는 .vue 확장자를 가진 하나의 독립된 파일(SFC)로 구성됨. SFC는 세 영역으로 이루어짐.

Vue3 생태계에서는 `<script setup>`을 맨 위에 먼저 쓰고, 그 아래에 `<template>`을 작성하는 방식이 트렌드가 되었음. 컴포넌트 파일명은 두 단어 이상으로 조합된 PascalCase를 권장함 (ex. HelloWorld.vue).

### SFC 예시 — HelloWorld.vue

App.vue에서 Props로 받은 msg를 화면에 출력하는 간단한 예시 컴포넌트임.

defineProps()로 부모에서 내려오는 msg prop을 선언하고 타입과 필수 여부를 지정함 → 부모에서 자식으로 Props를 통해 데이터를 보냄

`<template>`에서 {{ msg }}로 msg 값을 텍스트로 출력함 (Text Interpolation)

`<style scoped>`로 스타일을 이 컴포넌트 안에서만 적용되도록 범위를 제한함

```text
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
```

### {{ msg }}

### You've successfully created a project with Vite + Vue 3.

### SFC — Options API vs. Composition API

Vue 컴포넌트의 `<script>` 영역을 작성하는 방법은 두 가지임.

Composable: Vue의 반응형 상태(Ref, Reactive)와 로직을 묶어 재사용할 수 있도록 만든 함수.

### SFC — Options API vs. Composition API 코드 비교

동일한 카운터 기능을 두 방식으로 구현한 예시임.

Options API 방식 — 상태는 data(), 메서드는 methods에 각각 나뉘어 배치됨:

```text
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

```typescript
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

### SFC — Interpolation & Directive

Vue 컴포넌트의 `<template>` 영역을 작성하는 두 가지 핵심 문법임.

### Text Interpolation (텍스트 보간법)

Syntax: {{ 변수명 }}

용도: JavaScript 변수 값을 그대로 문자열로 투사하고 싶을 때 사용

### Directive

Syntax: v-로 시작하는 Vue 전용 특수 속성 (v-bind, v-if, v-for, v-on 등)

용도: 일반 HTML 태그 안에서 태그의 속성, 스타일, 조건문, 반복문, 이벤트 리스너 등을 자바스크립트 데이터와 연결하여 제어하기 위해 사용

```text
<template>
  <div>
    <h1>Composition API Counter</h1>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

위 예시에서 {{ count }}는 Text Interpolation으로 count 변수 값을 화면에 출력하고, @click="increment"는 v-on:click의 축약형 Directive로 버튼 클릭 이벤트를 increment 함수에 연결하는 것임.

### 학습환경 구성 — App.vue 비우기

실습 시작 전 App.vue를 아래와 같이 최소 구조로 비워서 시작함. `<script setup>`은 빈 상태로 두고, `<template>`에는 확인용 제목만 남긴 형태임.

App.vue

```text
<script setup>
// 자바스크립트 영역 (우선 비워둡니다)
</script>

<template>
  <h1>Hello Skala-Vue</h1>
</template>
```

브라우저에서 확인하면 "Hello Skala-Vue" 텍스트만 렌더링되고, Vue DevTools의 컴포넌트 탭에서 `<App>` 하나만 존재하는 깨끗한 상태를 확인할 수 있음.

### 학습환경 구성 — App.vue 샘플 컴포넌트 채우기

실습 컴포넌트를 만든 뒤, App.vue에서 import하여 자식 컴포넌트로 끼워 넣는 방식으로 테스트함. 교육과정에서 작성되는 컴포넌트들은 특정 폴더에 분류하여 넣음 (ex. src/components/practices/basic/).

App.vue

```html
<script setup>
import SampleOne from './components/practices/basic/SampleOne.vue'
</script>

<template>
  <div style="padding: 20px">
    <SampleOne />
  </div>
</template>
```

### 학습환경 구성 — 반응성 데이터 (Reactivity) Example

일반 변수와 ref()로 감싼 반응형 변수의 차이를 직접 비교한 예시임.

일반 변수(let normalCount)는 버튼을 눌러도 화면의 숫자가 변경되지 않음. 내부 값은 바뀌지만 Vue가 변화를 감지하지 못하기 때문임.

ref()로 감싼 반응형 변수(const vueCount)는 버튼을 누르는 순간 숫자가 즉시 화면에 반영됨.

반응형 변수를 누르는 순간 화면을 새로 고침으로 일반 변수의 변경된 값도 같이 반영됨.

참고: JavaScript 소스 끝 부분의 ;를 빼먹어도 ASI(Automatic Semicolon Insertion) 기능으로 자동 삽입되어 잘 동작함.

src/components/practices/basic/SampleOne.vue

```typescript
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

### 학습환경 구성 — JavaScript in Text Interpolation Example

{{ }} 안에는 변수명뿐 아니라 JavaScript 표현식(Expression)도 직접 사용할 수 있음.

src/components/practices/basic/SampleTwo.vue

```typescript
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

{{ welcomeMessage }} → 변수 값 그대로 출력

{{ welcomeMessage.toUpperCase() }} → 문자열 메서드 호출 결과 출력

{{ 'Random number: ' + Math.ceil(Math.random() * 100) }} → 연산식 결과 출력

{{ }} 안에서는 단일 JavaScript 표현식이라면 무엇이든 사용 가능하지만, if문 같은 구문(statement)은 사용할 수 없고 삼항 연산자로 대체해야 함.

### Vue Directive

Vue Directive는 v- 접두사가 붙은 특수한 HTML 속성으로 Vue 인스턴스와 연동됨. Directive 뒤에 오는 값인 v-명령어="값" 구역의 따옴표 내부(" ")는 단순 문자열이 아니라 자바스크립트 변수나 연산식이 작동하는 공간임.

자주 쓰는 핵심 Directive는 v-bind(:)와 v-on(@)이며, 이 둘의 축약형을 실무에서 거의 항상 사용함. v-if와 v-show는 둘 다 조건부 표시이지만 동작 방식이 다름

### Vue Directive — v-html

v-html은 자바스크립트 변수에 담긴 문자열을 단순 텍스트가 아니라 실제 HTML Element로 해석하여 화면에 주입하는 Directive임. 내부적으로는 자바스크립트의 element.innerHTML 속성과 동일하게 동작함.

{{ }} 보간법과의 차이:

{{ rawHtmlData }} → HTML 태그를 문자열 그대로 출력 (태그가 텍스트로 보임)

v-html="rawHtmlData" → HTML 태그를 실제로 파싱하여 렌더링 (스타일 적용됨)

src/components/practices/basic/SampleVHtml.vue

```typescript
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

### Vue Directive — v-html XSS 위협

v-html은 XSS(Cross-Site Scripting) 공격에 노출되므로 사용 시 각별히 주의해야 함.

XSS란 해커가 게시판 댓글이나 입력창에 악성 자바스크립트 코드를 심어두고, 다른 사용자가 그 글을 읽을 때 그 사용자의 브라우저에서 해커의 코드가 강제로 실행되게 만들어 쿠키·세션 토큰·로그인 정보를 탈취하는 해킹 기법임.

v-html은 입력값을 HTML로 그대로 파싱하기 때문에, 사용자가 입력한 악성 HTML이 그대로 실행될 수 있음. 아래 예시에서

를 입력 후 확인 버튼을 클릭하면 다른 사이트로 강제 이동됨.

src/components/practices/basic/SampleVHtmlXSS.vue

```typescript
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

따라서 v-html은 신뢰할 수 있는 내부 데이터에만 사용해야 하며, 사용자 입력값을 그대로 v-html에 바인딩하는 것은 금지해야 함.

### Vue Directive — v-text

v-text는 지정한 변수의 값을 태그의 텍스트 내용으로 채워 넣는 Directive임. 내부적으로는 자바스크립트의 element.innerText 속성과 똑같이 동작함. Text Interpolation {{ }}과 동일하므로 실무에서는 v-text 대신 {{ }}을 사용함.

세 가지 방식의 출력 결과 비교:

src/components/practices/basic/SampleVText.vue

```typescript
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

### Vue Directive — v-bind (기본)

v-bind는 HTML 태그 내부의 Attribute에 자바스크립트 값을 동적으로 연결(Binding)하는 Directive임. 문법은 v-bind:[attribute]="[Vue data]"이며, 실무에서는 v-bind를 생략하고 콜론(:) 축약형을 100% 사용함.

세 가지 활용 예시:

:href — URL 변수를 `<a>` 태그의 링크에 동적으로 연결

:src — 이미지 경로 변수를 `<img>` 태그의 src에 동적으로 연결

:disabled — 반응형 변수로 버튼의 활성화/비활성화 상태를 동적으로 제어

src/components/practices/basic/SampleVBind.vue

```typescript
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

### Vue Directive — v-bind (Class Binding)

:class는 스타일시트 클래스를 동적으로 붙였다 뗐다 하는 클래스 바인딩임. 단순 문자열 주입이 아니라 객체(Object)와 배열(Array) 형식을 지원하여 강력한 조건부 디자인을 가능하게 함.

→ 위의 예시에서 isActive, isPrimary 는 boolean 타입 변수임

src/components/practices/basic/SampleVBindClass.vue

```typescript
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

### Vue Directive — v-bind (Style Binding)

:style은 인라인 스타일을 동적으로 제어하는 바인딩임. 클래스 바인딩처럼 객체(Object)와 배열(Array)을 지원함.

객체 구문: CSS 속성명을 camelCase로 작성. kebab-case 문자열도 사용 가능

기본 구조: :style="{ color: 변수명, fontSize: 변수명 + 'px' }"

배열 구문: 여러 개의 스타일 객체 변수들을 하나로 합쳐서 태그에 주입

src/components/practices/basic/SampleVBindStyle.vue

```typescript
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

→ `<input>` 의 step은 얼마만큼의 간격씩 늘지

### Vue Directive — v-bind (Class vs. Style Binding 비교)

### Vue Directive — v-bind (Same-name Shorthand)

Vue 3.4 버전부터 공식 도입된 문법으로, 연결할 자바스크립트 변수명과 HTML 속성명이 완전히 일치할 때 코드를 극단적으로 줄여주는 방법임.

```html
<img v-bind:src="src" />  <!-- 전체 문법 -->
<img :src="src" />        <!-- 콜론 축약형 -->
<img :src />              <!-- same-name shorthand (Vue 3.4+) -->
```

동작 원리: 속성 앞에 콜론(:)만 붙이고 뒤의 ="src"를 생략하면, Vue 엔진이 "이 태그의 src 속성에 이름이 똑같은 src라는 자바스크립트 변수를 자동으로 매핑하라는 뜻이구나!" 하고 알아서 해석함. 실무 활용 팁으로, 변수명을 id, src, href, disabled 등 HTML 표준 속성명과 똑같이 맞춰 선언해 두면 코딩 속도가 빨라짐.

src/components/practices/basic/SampleVBindShorthand.vue

```html
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

### Vue Directive — v-if / v-else-if / v-else

JavaScript 조건식의 결과(true/false)에 따라 HTML 태그를 화면에 그릴지, 아니면 지울지 결정하는 제어문 역할의 Directive임.

src/components/practices/basic/SampleVIf.vue

```typescript
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

### Vue Directive — v-show

조건식의 결과(true/false)에 따라 태그를 화면에 '보여줄지(Show)' 아니면 '숨길지(Hide)' 결정하는 Directive임. 조건이 false가 되더라도 HTML DOM에서 태그를 삭제하지 않고, CSS 속성인 display: none을 실시간으로 붙여서 숨기는 방식임.

src/components/practices/basic/SampleVShow.vue

```typescript
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

### Vue Directive — v-if vs. v-show 비교

### Vue Directive — v-for

배열이나 객체를 사용해서 뷰에서 반복적으로 렌더링하는 HTML Element를 생성하는 데 사용하는 Directive임. v-for를 쓸 때는 Vue 엔진이 각 태그를 고유하게 식별할 수 있도록 반드시 고유한 값을 :key 속성에 바인딩해야 함. 그렇지 않으면 에러 또는 성능 저하가 발생함.

### 문법 패턴

배열 렌더링:

```text
<div v-for="(item, index) in items" :key="고유값"></div>
<div v-for="item in items" :key="고유값"></div>
```

객체 렌더링:

```text
<div v-for="(value, key, index) in object" :key="고유값"></div>
<div v-for="(value, key) in object" :key="고유값"></div>
<div v-for="value in object" :key="고유값"></div>
```

src/components/practices/basic/SampleVFor.vue

```typescript
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

배열 렌더링: (fruit, index) in fruits — 값과 인덱스를 동시에 받음. :key에는 index 또는 고유 식별자를 씀

객체 렌더링: (value, key, index) in user — 값, 키 이름, 인덱스 순서로 받음. :key에는 key(속성명)를 씀 → 무조건 (value, key, index) 의 순서로 받아야함

배열 내 객체 렌더링: (item, index) in items — 객체 배열을 순회. :key에는 객체의 고유 id(item.id)를 쓰는 것이 가장 안전함

### Vue Directive — v-pre

Vue의 템플릿 컴파일러가 Vue 문법으로 해석(Compile)하지 말고, 써진 그대로 HTML 텍스트로 화면에 표시하라고 지시하는 Directive임. Vue 엔진은 원래 HTML을 읽다가 {{ }}나 v-디렉티브를 만나면 자바스크립트 데이터로 갈아 끼우는 연산을 하지만, v-pre가 붙은 태그와 그 자식 태그들은 아무런 연산 없이 그대로 출력함

src/components/practices/basic/SampleVPre.vue

```typescript
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

일반 출력 결과: 안녕하세요! (변수값으로 치환됨)

v-pre 출력 결과: {{ message }} (문자열 그대로 출력됨)

### Vue Directive — v-cloak

Vue 어플리케이션의 렌더링 과정에서 데이터 바인딩이 완료되기 전에 Template을 노출하면 {{ message }}같은 해석 안 된 뼈대 문자열이 그대로 노출되는 현상이 발생함. 네트워크가 아주 느린 환경에서 발생하는 현상으로, v-cloak은 이런 현상을 예방함. 이 Directive는 혼자서는 작동하지 않고, CSS의 속성 선택자 [v-cloak]이 반드시 필요함.

src/components/practices/basic/SampleVCloak.vue

```typescript
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

### Vue Directive — v-once

해당 요소와 그 하위 요소는 최초에 한 번만 반응형으로 렌더링하고, 그 이후부터는 데이터가 변경되어도 DOM은 갱신되지 않음. Vue 엔진이 데이터를 실시간으로 감시하려면 메모리를 계속 소모해야 하는데, 소개글·약관 내용처럼 처음 백엔드에서 한 번 받아온 이후로는 절대 바뀔 일이 없는 데이터에 v-once를 붙여 두면 Vue가 더 이상 감시하지 않아 메모리 부담이 줄어듦.

src/components/practices/basic/SampleVOnce.vue

```typescript
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

### Vue Directive — v-memo

지정한 조건(변수)이 바뀔 때만 태그 내부를 업데이트하고, 그렇지 않으면 이전에 그려둔 화면(캐시)을 그대로 재사용하는 Directive임. 문법: v-memo="[감시할변수1, 감시할변수2]".

아래 예시에서 v-memo="[name]"을 설정하면 name이 바뀔 때만 해당 블록이 리렌더링됨. age만 증가시켜도 name이 바뀌지 않는 한 블록 내부는 갱신되지 않음.

src/components/practices/basic/SampleVMemo.vue

```typescript
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

### Vue Event Handling — v-on (@)

v-on은 DOM 요소에 이벤트 리스너를 연결하여 이벤트를 감지하고 처리할 때 사용하는 Directive임. 주로 사용자 입력(클릭, 키보드 입력 등)에 반응하여 원하는 동작을 실행하는 데 사용함. 실무에서는 @ 축약형을 사용함.

→ JS에서의 eventhandler와 유사함.

```text
<!-- 축약형 없이 사용 -->
<button v-on:click="doSomething">클릭</button>

<!-- 축약형 (@) 사용 -->
<button @click="doSomething">클릭</button>
```

### 주요 이벤트 목록

### Vue Event Handling — Event Handler 종류

이벤트 핸들러는 두 가지 방식으로 작성함.

Inline Handler — 태그 안에서 즉시 간단한 자바스크립트 연산을 처리할 때 사용 (숫자 증감, 스위치 토글 등):

```text
<button @click="count++">클릭 수: {{ count }}</button>
```

Method Handler — 복잡한 로직은 `<script setup>` 구역에 함수를 만들어서 연결. @click="handleClick"처럼 괄호 없이 함수 이름만 넘기면, Vue는 이 함수를 호출하는 것이 아니라 함수의 참조(주소) 자체를 이벤트 리스너로 등록함. button.addEventListener('click', handleClick)과 동일한 동작임:

→ 즉, “괄호 없이” 함수의 참조 주소 자체를 이벤트 리스너로 등록해서 동작하는 것임

```text
<button @click="handleClick">클릭하세요</button>
```

### Vue Event Handling — Event Handler Example

src/components/practices/basic/SampleVOn.vue

```typescript
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

### Vue Event Handling — JavaScript Event Object

Event Object란 사용자가 웹페이지에서 버튼을 클릭하거나, 키보드를 누르거나, 마우스를 움직이는 등의 이벤트를 발생시켰을 때 브라우저가 자동으로 생성하는 객체임.

### Event Object 주요 Properties

### Event Object 주요 Methods

### Vue Event Handling — Event Object 사용 패턴

Vue에서 Event 객체($event)를 받는 Pattern 2가지:

Method Handler에 함수 이름만 적어서 호출하면, JavaScript Engine이 첫 번째 인자로 이벤트 객체를 묵시적으로 전달함. Syntax: @click="handleEvent" → 스크립트: const handleEvent = (e) => { ... } → $event 을 안 적음

함수에 특정 데이터를 던지면서 이벤트 객체도 동시에 넘기고 싶을 때는, Vue가 제공하는 특별한 기호인 $event를 명시적으로 적어주어야 함. Syntax: @click="handleEvent('홍길동', $event)"

src/components/practices/basic/SampleVOnEvent.vue

```typescript
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

### Vue Event Handling — Event Modifier (이벤트 수식어)

Event Modifier는 이벤트 리스너의 기본 동작을 보완하거나 제어하는 데 사용되는 특수 접미어임. v-on:submit.prevent="onSubmit"처럼 이벤트명 뒤에 .수식어를 붙여 사용함.

### 주요 Event Modifier

src/components/practices/basic/SampleVOnModifier.vue

```typescript
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

### Form Data Binding — Two-way Data Binding with v-model

v-model은 HTML의 입력 요소의 값과 JavaScript 데이터(Ref)를 묶어, 한쪽이 바뀌면 다른 한쪽도 실시간으로 똑같이 바뀌게 만드는 양방향(Two-way) 바인딩 장치임.

내부 작동 원리: v-model은 :value(단방향 바인딩)와 @input(이벤트 감지)를 결합한 축약 문법임. v-model="text2"는 아래와 동일하게 작동함:

```html
<input type="text" :value="text2" @input="(e) => (text2 = e.target.value)" />
```

src/components/practices/basic/SampleVModel.vue

```typescript
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

### Form Data Binding — v-model 변수 선언 규칙

HTML Form 요소별로 v-model에 연결할 ref 초기값 타입이 다름. HTML 요소의 특성에 맞게 초기값을 선언해야 예외나 의도치 않은 버그를 막을 수 있음.

내부 이벤트 차이:

일반 텍스트 입력(input, textarea)은 타이핑할 때마다 반응하는 @input 이벤트를 기반으로 작동함

선택형 요소(checkbox, radio, select)는 값이 확정되는 시점에 반응하는 @change 이벤트를 기반으로 작동함

### Form Data Binding — Form Elements Code Example

src/components/practices/basic/SampleVModelForm.vue

```sql
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

### Form Data Binding — v-model Modifiers

v-model 수식어는 입력 요소의 동작 방식이나 수집되는 데이터 형태를 손쉽게 제어할 수 있도록 Vue가 제공하는 편의 기능(Syntactic Sugar)임. 수식어는 필요한 만큼 이어 붙여서 사용 가능함 (Modifier Chaining).

src/components/practices/basic/SampleVModelModifiers.vue

```typescript
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

### Vue Style — Scoped Style & External Style

### Scoped Style

SFC 파일의 `<style>` 영역에 작성된 스타일은 기본적으로 모든 컴포넌트에 전역 적용됨. `<style scoped>`를 사용하면 현재 컴포넌트 내부에 선언된 HTML 태그에만 적용되고, 다른 컴포넌트에는 영향을 주지 않음.

### External Style

공통 CSS나 외부 라이브러리 CSS를 사용하는 방법

프로젝트 전체에 적용할 공통 스타일은 src/main.js에 등록함

특정 컴포넌트에 외부 CSS 파일을 적용할 때는 `<style>` 방 내부에서 자바스크립트의 @import 문법을 사용함

src/components/practices/basic/SampleStyle.vue

```text
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

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
