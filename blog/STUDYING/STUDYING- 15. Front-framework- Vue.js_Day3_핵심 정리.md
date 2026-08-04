---
title: "[STUDYING] 15. Front-framework: Vue.js_Day3_핵심 정리"
created: 2026-08-05
updated: 2026-08-05
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-04
source_url: https://ch010104.tistory.com/332
---
# [STUDYING] 15. Front-framework: Vue.js_Day3_핵심 정리

## 원문

https://ch010104.tistory.com/332

## 노트 유형

`guide`

## 적용 목적과 전제조건

Vue는 최초 접속 시 HTML을 단 한 번만 다운로드하는 SPA(Single Page Application) 구조임. 전통적인 웹사이트가 페이지 이동마다 서버에 새 HTML을 요청해 화면 전체를 새로고침하던 것과 다름.

Vue Router는 브라우저의 URL 변화를 JavaScript 엔진이 가로채, 서버에 새 페이지를 요청하지 않고 현재 경로(Path)에 매칭된 컴포넌트만 가상 DOM 상에서 실시간으로 교체해 주는 Vue 공식 라이브러리임.

## 구현 절차·검증·주의점

### Vue Router 개요

Vue는 최초 접속 시 HTML을 단 한 번만 다운로드하는 SPA(Single Page Application) 구조임. 전통적인 웹사이트가 페이지 이동마다 서버에 새 HTML을 요청해 화면 전체를 새로고침하던 것과 다름.

Vue Router는 브라우저의 URL 변화를 JavaScript 엔진이 가로채, 서버에 새 페이지를 요청하지 않고 현재 경로(Path)에 매칭된 컴포넌트만 가상 DOM 상에서 실시간으로 교체해 주는 Vue 공식 라이브러리임.

설치는 package.json의 dependencies에 "vue-router": "^5.0.4"를 추가하는 방식으로 관리함.

```text
// package.json
"dependencies": {
  "pinia": "^3.0.4",
  "vue": "^3.5.32",
  "vue-router": "^5.0.4"
}
```

### Vue Router Setup — Step 1: 라우터 설정 (src/router/index.js)

vue-router 패키지의 createRouter()를 사용해 Router configuration object를 생성함.

주요 설정 옵션:

history: URL 관리 방식을 지정함. createWebHistory()는 전통적인 슬래시(/) 방식 URL을 사용함 (예: /user/profile)

routes: 배열로 된 라우트 객체 목록을 지정함

### routes 객체 속성

### component 지정 방식

정적 import (static import): 어플리케이션 시작 시점에 컴포넌트를 메모리에 로드

동적 import (dynamic import): 해당 컴포넌트가 필요한 순간에 로드 → Lazy Loading

```typescript
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'  // ① 정적 import

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,  // ① 정적 import 방식
    },
    {
      path: '/about',
      name: 'about',
// ② 동적 import (Lazy Loading)
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
```

→ 실무에서는 위의 routes 매핑 정보를 일일이 작성하는 것은 너무 코드가 많음, 데이터베이스에서 로딩하게 하는 경우가 많음

### Vue Router Setup — Step 2: 라우터 등록 (src/main.js)

생성한 라우터 설정을 Vue 어플리케이션에 등록하는 단계임. 어플리케이션 인스턴스의 use() 메서드를 사용함.

import router from './router'에서 ./router는 router 폴더의 index.js 파일을 불러오라는 의미임

app.use(router)로 라우터 설정 객체를 등록함

```typescript
// src/main.js
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'  // ① router/index.js 불러오기

const app = createApp(App)

app.use(createPinia())
app.use(router)  // ② 라우터 등록

app.mount('#app')
```

### Vue Router Setup — Step 3: 라우터 사용 (`<RouterView>`, `<RouterLink>`)

실제 템플릿에서 라우터를 활용하는 두 가지 핵심 컴포넌트임.

`<RouterLink to="...">`: 링크를 생성함. HTML `<a>` 태그 대신 사용함

`<RouterView />`: 현재 경로와 일치하는 컴포넌트가 렌더링될 자리를 지정함

### HTML `<a>` 태그를 사용하면 안 되는 이유

`<a href="/about">`About`</a>` 방식은 브라우저를 강제로 새로고침시켜 메모리에 들고 있던 모든 반응형 데이터(ref, computed)를 초기화하기 때문에 SPA 구조에서는 에러를 유발함. 반드시 `<RouterLink>`를 사용해야 함.

```html
<!-- src/App.vue -->
<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo." />
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      <nav>
        <RouterLink to="/">Home</RouterLink>      <!-- ② 링크 생성 -->
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />   <!-- ① 컴포넌트 렌더링 위치 -->
</template>
```

### Vue Router 핵심 요소 요약

### views 폴더

views 폴더에 위치한 컴포넌트는 `<RouterView />` 영역에 직접 렌더링되는 **"페이지 단위의 최상위 컴포넌트"**임. routes 배열의 component 속성에 직접 매핑되어 URL Path와 1:1로 대응됨 (예: /dashboard → DashboardView.vue).

Vue.js 공식 Style Guide 및 커뮤니티 권장사항에 따르면, RouterView에 의해 직접 호출되는 최상위 페이지 컴포넌트에는 접미사로 View를 붙이는 것을 강력히 추천함.

### views vs components

### useRoute()

useRoute()는 Script Setup 환경에서 현재 활성화된 라우트(Active Route) 정보에 접근하기 위한 Composable 함수임. URL 경로, 파라미터, 쿼리 스트링, 메타 데이터 등 현재 페이지의 모든 상태 정보를 reactive 객체 형태로 제공함.

### route 객체 주요 프로퍼티

useRoute()로 추출한 route 객체는 반응성을 유지하므로 template 및 script 내부에서 즉시 활용 가능함.

```typescript
<!-- src/views/UserDetailView.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute() // Active Route Object

console.log('현재 접근한 경로:', route.path)
console.log('전달된 ID 파라미터:', route.params.id)
</script>

<template>
  <!-- template에서 route 객체 프로퍼티 직접 접근 -->
  <p>사용자 ID: {{ route.params.id }}</p>
  <p>검색 키워드: {{ route.query.q }}</p>
</template>
```

Composable: Vue의 반응형 상태(Ref, Reactive)와 로직을 묶어 재사용할 수 있도록 만든 함수

### useRoute() — Dynamic Route Matching (동적 경로 매칭)

URL의 일부분이 동적으로 변경되는 경로를 다뤄야 할 때 사용함. 예를 들어 날씨 View에서 도시별 상세 페이지(/weather/seoul, /weather/suwon)를 만들 때, 도시마다 별도 Route 객체를 선언하는 비효율을 방지할 수 있음.

주소창 뒤에 콜론(:) 식별자를 붙여 변수화(/weather/:cityId)하며, 이 부분을 **동적 세그먼트(Dynamic Segment)**라 함.

```text
// router/index.js
{
  path: '/weather/:cityId',  // [동적 세그먼트]
  name: 'WeatherDetail',
  component: WeatherDetail
}
```

컴포넌트 내부에서는 useRoute()로 route 객체를 수신하여 route.params.cityId로 값을 확인할 수 있음.

```typescript
<!-- src/views/WeatherDetail.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

console.log(route.path)           // 현재 경로: '/weather/seoul'
console.log(route.params.cityId)  // 동적 파라미터: 'seoul'
</script>
```

### useRoute() — Dynamic Route Matching (다중/중간 동적 세그먼트)

### Multiple Dynamic Segments (다중 동적 세그먼트)

URL 경로 내에 2개 이상의 동적 파라미터를 조합하여 복잡한 계층 구조를 표현할 수 있음. : 가 붙은 세그먼트만 route.params로 수신되며, 모든 동적 파라미터는 route.params 객체의 속성으로 각각 매핑됨.

예) 카테고리별 상품 상세 페이지: /category/electronics/product/101

```text
// router/index.js
{
  path: '/category/:categoryId/product/:productId', // :categoryId, :productId 2개 지정
  name: 'ProductDetail',
  component: ProductDetailView
}
```

```typescript
<!-- src/views/ProductDetailView.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

console.log(route.path)                // '/category/electronics/product/101'
console.log(route.params.categoryId)   // 'electronics'  ← :categoryId만 잡힘
console.log(route.params.productId)    // '101'          ← :productId만 잡힘
// 고정 경로인 'category', 'product'는 params에 없음
</script>
```

### Inline Dynamic Segment (중간 위치 동적 세그먼트)

경로의 중간에 콜론(:) 식별자를 배치하여 하위 리소스나 특정 액션을 구분함. : 가 붙은 세그먼트만 route.params로 수신되며, 고정 경로는 params에 포함되지 않음.

예) 특정 사용자의 게시글 리스트 조회: /user/42/posts

```text
// router/index.js
{
  path: '/user/:userId/posts',  // posts는 고정 경로, :userId만 동적 세그먼트
  name: 'UserPosts',
  component: UserPostsView
}
```

```typescript
<!-- src/views/UserPostsView.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

console.log(route.path)           // '/user/42/posts'
console.log(route.params.userId)  // '42'  ← :userId만 잡힘
// 고정 경로인 'posts'는 params에 없음
</script>
```

### useRoute() — Query String Routing

### Query String Routing 설정

URL 주소창 뒤에 물음표(?)에 이어 key=value 형태의 쌍으로 붙는 Query String을 Vue Router와 동기화하는 라우팅 기법임.

예) /weather?search=수원&page=2

라우터 설정 파일에는 별도의 변수 처리를 명시하지 않아도 자유롭게 확장 가능함 (Dynamic Segment처럼 :변수명 선언 불필요)

&로 연결된 여러 key=value 쌍은 Vue Router가 자동으로 파싱해 route.query 객체에 각각의 key로 담아줌. 직접 split할 필요 없음

```text
// /weather?search=수원&page=2 로 접근 시
route.query = {
  search: '수원',
  page: '2'
}
```

### Query String 수신

컴포넌트 내부에서는 useRoute()로 route 객체를 수신하여 각 key를 개별적으로 꺼내 쓸 수 있음. 컴포넌트 마운트 시점에 주소창에 query가 이미 있다면 해당 값으로 내부 상태를 복원하는 패턴으로 활용함.

```typescript
<!-- src/views/WeatherView.vue -->
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

// 컴포넌트 마운트 시점: 주소창에 query값이 이미 있다면 내부 상태 복원
onMounted(() => {
  if (route.query.search) {
    searchQuery.value = route.query.search  // '수원'
  }
  if (route.query.page) {
    currentPage.value = route.query.page    // '2'
  }
})
</script>
```

### useRouter()

useRouter()는 Script Setup 환경에서 라우터 인스턴스(Router Instance)에 접근하기 위한 Composable 함수임. `<RouterLink>`와 같은 태그 클릭 외에, 자바스크립트 코드(이벤트 핸들러, 비동기 로직 등)로 페이지를 이동할 때 활용함 → Programmatic Navigation

### router 객체의 주요 메소드

### useRouter() — Programmatic Navigation

`<RouterLink to="...">` 가 아닌 Script 내부에서 페이지를 전환하는 방법임. 로그인 성공 후 메인으로 이동, 상세 페이지에서 버튼을 눌러 스크립트 명령어로 페이지를 이동하는 상황 등에 활용함.

router.push()를 호출하면 Vue Router가 URL(경로)을 변경하고, 그 경로에 매핑된 컴포넌트를 `<RouterView/>`가 위치한 영역에 동적으로 교체(렌더링)해 줌.

### Method Example

### useRouter() — Code Example

```typescript
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// push: 히스토리 스택에 추가 → 뒤로 가기 가능
const handleGoHome = () => {
  router.push('/')
}

// replace: 현재 히스토리 항목 대체 → 뒤로 가기 불가
const handleLoginRedirect = () => {
  router.replace('/')
}

// push with name + params + query 조합
const handleAdvancedMove = () => {
  router.push({
    name: 'WeatherDetail',        // 라우터 설정에 등록된 고유 Name 호출
    params: { cityId: 'city_02' }, // 주소창 :cityId 구역에 변수 매핑
    query: { search: '수원' }      // 주소창 뒤에 ?search=수원 쿼리 추가
  })
}

// go(-1): 1단계 이전 주소 기록으로 Back
const handleGoBack = () => {
  router.go(-1)
}
</script>

<template>
  <button @click="handleGoHome">일반 홈 이동 (push)</button>
  <button @click="handleLoginRedirect">인증 만료! 강제 리다이렉트 (replace)</button>
  <button @click="handleAdvancedMove">고급 파라미터 이동</button>
  <button @click="handleGoBack">이전 화면으로</button>
</template>
```

### Navigation Guard

특정 라우트로 진입하기 직전, 중간에 가로채서 접근 권한 검사 및 페이지 리다이렉션 같은 사용자 정의 로직을 실행할 수 있게 함.

활용 예시: 관리자 페이지나 마이페이지처럼 로그인한 회원만 들어가야 하는 주소에 비로그인 사용자가 진입하는 경우 로그인 페이지로 전환함.

Navigation Guard는 사용 방식에 따라 세 가지로 구분됨:

### Navigation Guard — Global Guard

모든 Route 전환에서 사용자 정의 로직이 실행됨. router/index.js의 라우터 인스턴스 하단에 배치함.

### Hook Method

콜백 인자:

to: 이동할 목적지 route 객체

from: 현재 출발지 route 객체

next: 이동을 허가하는 종결 함수

```typescript
// router/index.js — 라우터 인스턴스 하단에 배치
router.beforeEach((to, from, next) => {

  const isAuthenticated = false // 실제로는 쿠키나 로컬스토리지의 토큰 검사

// 권한이 필요한데 로그인이 안 된 경우
  if (to.meta.isAuth && !isAuthenticated) {
    alert('로그인이 필요한 서비스입니다.')
    next('/') // 통과를 블허하고 메인 홈 주소로 강제 이동
  } else {
    next() // 일반 통과 허가
  }
})
```

### Unmatched Route Handling

### Route 미매핑 시 발생 상황

정의되지 않은 경로(예: /unknown-page)로 접속할 경우, Vue Router는 에러를 던지는 대신 단지 매핑되는 컴포넌트를 찾지 못함. 그 결과 `<RouterView/>` 영역에 아무것도 렌더링되지 않아 화면이 하얗게 비어 보이는 현상이 발생함.

### Catch-all Route

Vue Router의 Dynamic Route Matching과 Catch-all Regex 패턴(path: '/:pathMatch(.*)*')을 활용하여 구현함. 라우트 등록 목록의 가장 마지막에 배치해야 함 — 위에 정의된 라우트와 매칭되지 않는 모든 경로를 최종적으로 잡아내는 구조이기 때문임.

```typescript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
// ... 기타 정의된 라우트들 ...

// 상단 라우트와 매칭되지 않는 모든 경로를 NotFoundView로 리다이렉트
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFoundView
  }
]
```

/:pathMatch(.*)*는 정규식 .*(모든 문자)을 동적 세그먼트로 감싼 패턴으로, 앞서 정의된 어떤 경로와도 매칭되지 않는 URL을 전부 잡아냄. 웹의 일반적인 404 페이지 처리와 동일한 개념임.

### Pinia 개요

Vue Application이 크고 복잡해질수록 Component간 데이터 전달은 어려워짐. Pinia는 Component 계층 구조와 상관없이 별도의 전역 데이터 저장소(Store)를 개설하여 반응형 데이터를 관리하는 Vue3의 공식 상태(state)관리 라이브러리임. Vue2에서는 Vuex라는 상태관리 라이브러리를 사용했음.

상태(State)란 웹 어플리케이션을 렌더링하는 과정에 영향을 줄 수 있는 값을 의미하며, 상태관리란 이러한 값을 관리하는 방법을 의미함.

설치는 package.json의 dependencies에 "pinia": "^3.0.4"로 관리함.

### Pinia — Store

Store는 여러 파일로 구성될 수 있으며, 일반적으로 의미가 있는 상태끼리 파일 하나로 작성함.

예) 인증스토어(authStore.js), UI스토어(uiStore.js), 알림스토어(alertStore.js), 공통코드스토어(commonStore.js) 등

### Store 핵심 개념

### Pinia 구축 3단계

### Step 1: Pinia 등록하기 (src/main.js)

createPinia() 함수를 통해 pinia 인스턴스를 생성하고, 어플리케이션 인스턴스의 use() 함수로 등록함.

```typescript
// src/main.js
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'  // ① 인스턴스 생성

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())  // ① ② 생성 + 등록
app.use(router)

app.mount('#app')
```

### Step 2: Store 생성하기 (src/stores/스토어명.js)

Pinia 패키지에서 제공하는 defineStore() 함수로 생성함. defineStore()로 생성한 Store Instance를 할당하는 변수의 식별자는 use + 파일명 + Store 규칙에 따라 작성함.

```typescript
// src/stores/counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {  // ① 스토어 ID, ② 함수
  const count = ref(0)                              // state: 전역 공유 원본 데이터
  const doubleCount = computed(() => count.value * 2) // getters: 실시간 연산 (Read-Only)
  function increment() {                            // actions: state 변경 함수
    count.value++
  }

  return { count, doubleCount, increment }          // Expose: 외부 컴포넌트에 공개
})
```

### Sample Code 설명

### Step 3: Store 사용하기

① Import Store → ② Instance 가동 → ③ state/getter/action 사용

```typescript
<script setup>
// 1. 정의한 카운터 스토어 플러그인 import
import { useCounterStore } from '@/stores/counter.js'

// 2. 인스턴스 가동 (전역 저장소 포인터 확보)
const counterStore = useCounterStore()
</script>

<template>
  <div class="practice-section">
    <h2>Counter Store 활용 실습</h2>

    <p>원본 카운트 데이터(state): <strong>{{ counterStore.count }}</strong></p>
    <p>2배 연산 데이터(getters): <span>{{ counterStore.doubleCount }}</span></p>

    <button @click="counterStore.increment">숫자 1 증가 (actions)</button>
  </div>
</template>
```

### Pinia — Frequent Mistakes

### 구조분해할당 시 반응형 유실 주의

Store의 데이터 속성(State, Getters)은 구조분해할당(Destructuring Assignment)시 반응형이 유실될 수 있음.

```typescript
// 오류 유발 코드
// 이렇게 구조 분해 할당을 하면 Vue 3 반응형 시스템(Proxy 주소)이 단절되어 화면이 갱신되지 않음
const { count, increment } = counterStore
```

데이터(State, Getters) 속성은 Pinia 내장 함수인 storeToRefs로 감싸 호출해야만 반응형 연결 고리가 보존됨. 단, 함수인 Actions는 일반 구조 분해 할당을 해도 무방함.

```typescript
import { storeToRefs } from 'pinia'

// State, Getters는 storeToRefs로 감싸야 반응형 유지
const { count, doubleCount } = storeToRefs(counterStore)
// Actions는 일반 구조분해 가능
const { increment } = counterStore
```

구조분해할당(Destructuring Assignment): Array나 Object의 구조를 분해하여, 내부의 값들을 별도의 독립된 개별 변수에 각각 직접 할당하는 모던 JavaScript 표현식

### (사례연구) authStore — Login Flow

### Login 전체 Sequence Flow

### Backend login() vs Pinia authStore.login()

### (사례연구) authStore — JWT

JWT(JSON Web Token) 은 정보를 안전하게 JSON 객체 형태로 주고받기 위해 정의된 표준 규격으로 Backend가 발급함.

### JWT 구조

```text
eyJhbGci... . eyJzdWIi... . d3g4eT...
  [Header]      [Payload]   [Signature]
```

점(.) 2개로 구분된 3개의 긴 암호문(Base64) 문장으로 이루어져 있음. Base64로 누구나 쉽게 복호화할 수 있으므로 Payload에 민감정보를 넣으면 안됨.

### JWT vs Session

Pinia에 저장된 JWT Token은 HTTP 요청 헤더(Authorization)에 포함하여 Backend로 전달해야 함. 웹 브라우저가 백엔드 서버로 API를 요청할 때, 토큰은 주로 Authorization 헤더에 Bearer 타입으로 실어 보냄.

```text
GET /api/user/profile HTTP/1.1
Host: api.skala.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
```

실무에서는 Axios Request Interceptor를 사용해 자동으로 토큰을 주입함.

### (사례연구) authStore — Source Code

사용자의 토큰(JWT), 사용자 정보, 로그인 상태 등을 앱 전체에서 공유하기 위한 전역 인증 스토어 파일임. 파일명은 authStore.js로 지정하고, 외부에서 불러올 함수명은 Vue Composable 관례에 따라 useAuthStore로 내보냄(export).

```typescript
// src/stores/authStore.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
// 1. State: 로그인 토큰 및 사용자 정보 (새로고침 대비 localStorage에서 초기값 복원)
  const token = ref(localStorage.getItem('accessToken') || null)
  const user = ref(JSON.parse(localStorage.getItem('userInfo') || 'null'))

// 2. Getters: 로그인 여부 확인 및 사용자이름
  const isLoggedIn = computed(() => !!token.value)
  const username = computed(() => user.value?.name || '게스트')

// 3. Actions: 로그인 / 로그아웃 로직
  function login(userData, authToken) {
    user.value = userData
    token.value = authToken
// 브라우저 재접속 시 유지용
    localStorage.setItem('accessToken', authToken)
    localStorage.setItem('userInfo', JSON.stringify(userData))
  }

  function logout() {
    user.value = null
    token.value = null
    localStorage.removeItem('accessToken')
    localStorage.removeItem('userInfo')
  }

  return { token, user, isLoggedIn, userName, login, logout }
})
```

### (사례연구) authStore — Navigation Guard와 연동

router/index.js에서 store/authStore.js를 import하여 이동 직전 접근 권한을 검사함.

```typescript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const routes = [
  … 생략 …
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation Guard 연동
router.beforeEach((to, from) => {
// Guard 내부에서 authStore 호출
  const authStore = useAuthStore()

// 1. 인증이 필요한 페이지 접근 시 로그인 여부 체크
  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    alert('로그인이 필요한 서비스입니다.')
    return { name: 'Login', query: { redirect: to.fullPath } } // 로그인 후 돌아올 위치 전달
  }

// 2. 이미 로그인한 사용자가 로그인 페이지 접근 시 메인으로 이동
  if (to.name === 'Login' && authStore.isLoggedIn) {
    return { name: 'Dashboard' }
  }
})

export default router
```

### Data Communication — HTTP

HTTP(HyperText Transfer Protocol) 는 웹 브라우저와 웹 서버가 인터넷상에서 데이터를 주고받기 위해 세계적으로 약속한 표준 통신 규약(Protocol)임. 일반적으로 Client에서 Server로 HTTP Request를 보내고 서버는 요청에 대해 HTTP Response를 보냄.

### HTTP Methods

Client가 Server에 요청하는 작업이 무엇인지를 나타내며, 데이터베이스 CRUD 연산과 매핑됨. 각 Method의 역할은 강제 규칙은 아님 (POST로 데이터를 삭제하거나 변경해도 문제 없음).

### Data Communication — API

API(Application Programming Interface) 는 서로 다른 소프트웨어 애플리케이션이 자신들의 기능이나 데이터를 상대방이 안전하고 쉽게 가져다 쓸 수 있도록 열어놓은 규칙임. Web에서의 API는 Browser와 Server간에 HTTP를 사용해 데이터를 주고 받는 약속을 의미함.

### REST(REpresentational State Transfer) API

웹의 HTTP를 활용하면서, 자원을 이름으로 구분하여 해당 자원의 데이터를 주고 받는 방식의 웹 인터페이스 스타일임. HTTP Method(GET, POST, DELETE, PUT)를 활용하여 자원에 대한 CRUD 작업을 적용하는 것을 의미하며, 오늘날 대부분의 인터페이스에 활용됨.

### REST API 설계 원칙

주소(URI)는 오직 명사(자원)로만 구성함

나쁜 예: /getWeather, /deleteUser, /update_city (주소에 동사 포함)

바른 예: /weather, /users, /cities (오직 깔끔한 명사만 남김)

행위(동사)는 HTTP Method로 대체함

### Data Communication — Frontend vs. Backend

### API — JSON Placeholder

전 세계 프론트엔드 개발자들이 통신 및 CRUD 코드를 테스트할 때 사용하는 무료 가상 REST API 서비스임. (https://jsonplaceholder.typicode.com/)

### API — Open Weather

전 세계 20만 개 이상의 도시 데이터를 일관된 규격으로 제공하는 가장 대중적인 REST API 서비스임. 월 1,000,000건, 분당 60건의 호출을 무료로 제공하며, 데이터 응답 결과가 완벽한 JSON 형식으로 전달됨.

회원가입(Sign Up) 후 My API Keys에서 API 키를 확인하여 사용함.

Free Tier 기준으로 Current Weather API, 3-hour Forecast (5 days), Air Pollution API, Weather Maps (15 layers), Geocoding API를 무료로 제공함.

### Current Weather API 호출 URL

좌표 기반 호출:

```text
<https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr>
```

도시명 기반 호출 (Geocoding API):

```text
<https://api.openweathermap.org/data/2.5/weather?q=${targetCity.english}&appid=${API_KEY}&units=metric&lang=kr>
```

### API — API Test (Postman)

서버에서 제공하는 API를 테스트하는 도구임. 실제 코드 작성 전에 API 엔드포인트, 파라미터, 응답 구조를 확인하는 용도로 활용함.

### API — Fetch API vs. Axios

### Axios — Installation

```text
npm install axios
```

설치 확인 (package.json):

```text
"dependencies": {
  "axios": "^1.18.1",
  "pinia": "^3.0.4",
  "vue": "^3.5.32",
  "vue-router": "^5.0.4"
}
```

### Axios — API Example (Open Weather Map)

```typescript
<script setup>
import { ref } from 'vue'
import axios from 'axios'

const weatherData = ref(null)
const isLoading = ref(false)

const handleFetchWeather = async () => {
  isLoading.value = true

  const API_KEY = '8964edc63b366d27b5b728b7976570b7'
  const URL = `https://api.openweathermap.org/data/2.5/weather?lat=35.158582&lon=126.804975&appid=${API_KEY}&units=metric&lang=kr`

  try {
// 비동기 통신: 서버에서 데이터를 다 가져올 때까지 await로 기다린다
    const response = await axios.get(URL)
// fetch()는 응답 String을 Json으로 변환해야 하지만
// Axios에서는 응답 String(response.data)가 자동으로 JSON 파싱됨
    console.log('Axios 통신 응답 전체 객체:', response)
    console.log('백엔드가 준 핵심 날씨 데이터(JSON):', response.data)
    weatherData.value = response.data
  } catch (error) {
// 4xx, 5xx 에러나 네트워크 오프라인 시 자동으로 reject되어 catch 영역에서 처리함
    console.error('통신 중 에러가 발생했습니다:', error)
    alert('데이터를 가져오지 못했습니다. API 키 활성화 여부나 주소를 확인하세요.')
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="practice-section">
    <h2>⚡ Axios 통신 검증</h2>
    <button @click="handleFetchWeather" :disabled="isLoading">
      {{ isLoading ? '데이터 로딩 중...' : '실시간 날씨 데이터 당겨오기' }}
    </button>
    <div v-if="weatherData" class="result-card">
      <p>📍 위치: <strong>{{ weatherData.name }}</strong></p>
      <p>🌡 현재 기온: <strong>{{ weatherData.main.temp }}°C</strong> (정상 섭씨 변환 완료)</p>
      <p>☁ 날씨 상태: <strong>{{ weatherData.weather[0].description }}</strong></p>
      <p>💧 습도: <strong>{{ weatherData.main.humidity }}%</strong></p>
    </div>
    <div v-else>
      <p>아직 가져온 데이터가 없습니다. 버튼을 눌러 통신을 가동하세요.</p>
    </div>
  </div>
</template>
```

### Axios — Method List

배경색이 들어간 axios 통신 메서드들은 호출 후 자바스크립트의 Standard Promise 객체를 반환함.

### Axios — 비동기 호출 방식

Axios가 Promise를 리턴하기 때문에 두 가지 비동기 처리 방식을 사용할 수 있음.

```typescript
// Promise (.then()) 방식
const fetchWeatherPromise = () => {
  console.log('1. 통신 시작 구역')

  axios.get(URL)
    .then((response) => {  // 통신이 성공했을 때
      console.log('3. 데이터 도착:', response.data)
    })
    .catch((error) => {    // 에러가 났을 때
      console.error('에러 발생:', error)
    })

  console.log('2. 통신 요청 직후 라인')
// 백엔드 데이터가 오기 전에 '2번 로그'가 콘솔창에 먼저 기록됨
}
```

```typescript
// async / await 방식
const fetchWeatherAsync = async () => {
  console.log('1. 통신 시작 구역')

  try {
// 서버 데이터가 도착할 때까지 대기하고 함수를 호출한 바깥 부분 먼저 실행
    const response = await axios.get(URL)
// 데이터가 도착하면 실행
    console.log('2. 데이터 도착:', response.data)
  } catch (error) {
    console.error('에러 발생:', error)
  }

  console.log('3. 모든 통신 프로세스 완전히 끝난 후 라인')
// '1번 -> 2번 -> 3번' 순서대로 기록됨
}
```

### Axios — API Example (JSONPlaceholder CRUD)

```typescript
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 1. 백엔드 공용 주소
const BASE_URL = '<<a href=https://jsonplaceholder.typicode.com/posts>https://jsonplaceholder.typicode.com/posts</a>>'

// 2. 반응형 상태 데이터
const items = ref([])   // 서버에서 받아온 데이터 배열 박스
const textInput = ref('') // 입력창과 연결된 글자 데이터 박스

// [READ] GET: 데이터 가져오기
const handleRead = async () => {
  try {
// 공부용으로 딱 3개만 들고 옴
    const response = await axios.get(BASE_URL, { params: { _limit: 3 } })
    items.value = response.data
    console.log('GET 성공:', response.data)
  } catch (error) {
    console.error('GET 실패:', error)
  }
}

// … (POST, PUT, DELETE 동일 패턴으로 이어짐)
```

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
