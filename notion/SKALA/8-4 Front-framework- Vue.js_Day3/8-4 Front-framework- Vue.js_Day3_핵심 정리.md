---
title: "[8/4] Front-framework: Vue.js_Day3_핵심 정리"
notion_page_id: "3b11d84b-f68e-80bf-acb1-c41a79a054ef"
source_url: "https://app.notion.com/p/3b11d84bf68e80bfacb1c41a79a054ef"
synced_at: "2026-08-05T00:06:59+09:00"
content_sha256: "d059f4c3220dc581947a9dfefef28f1183147449b61909d23bae8822e6416a83"
tags: [notion, skala, learning, vue, frontend, vue-router, pinia]
---

# [8/4] Front-framework: Vue.js_Day3_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b11d84bf68e80bfacb1c41a79a054ef) (2026-08-05 확인)
>
> 맥락: [[notion/SKALA/8-3 Front-framework- Vue.js_Day2/8-3 Front-framework- Vue.js_Day2_핵심 정리|Vue.js Day2]]의 Composition API·상태 반응성 기초 위에서, SPA 화면 전환(Vue Router), 전역 상태(Pinia), HTTP 통신을 연결한다.

## 학습 범위

이 노트는 Vue 애플리케이션에서 다음 흐름을 다룬다.

1. URL에 맞는 화면을 교체하는 **Vue Router**
2. 컴포넌트 계층과 독립적으로 상태를 공유하는 **Pinia Store**
3. 인증 상태와 Navigation Guard의 연결
4. 브라우저와 서버가 데이터를 주고받는 HTTP·REST API
5. Axios를 이용한 비동기 요청과 CRUD 호출

이미지로 제시된 화면 예시는 임시 서명 URL이므로 보존하지 않았다. 원문의 코드와 텍스트 기반 설명을 중심으로 정리한다.

## Vue Router: 새 HTML을 받지 않는 SPA 화면 전환

Vue SPA는 최초 접속 때 HTML을 한 번 내려받고, 이후 URL이 바뀌어도 서버에 새 HTML 문서를 요청하는 대신 현재 경로에 해당하는 Vue 컴포넌트만 가상 DOM에서 교체한다. Vue Router는 이 URL 변화와 컴포넌트 교체를 담당하는 공식 라이브러리다.

`package.json`의 `dependencies`에 `vue-router`를 포함해 설치 상태를 관리한다.

```json
{
  "dependencies": {
    "pinia": "^3.0.4",
    "vue": "^3.5.32",
    "vue-router": "^5.0.4"
  }
}
```

### 1. 라우터 설정: `src/router/index.js`

`createRouter()`로 라우터 설정 객체를 만들며, `history`에는 URL 관리 방식, `routes`에는 URL과 컴포넌트의 매핑 목록을 둔다. `createWebHistory()`는 `/user/profile` 같은 일반적인 슬래시 기반 URL을 쓴다.

| routes 속성 | 자료형 | 역할 |
| --- | --- | --- |
| `path` | String | 브라우저 URL 경로(필수) |
| `component` | Component / Function | 해당 경로에 표시할 Vue 컴포넌트(필수) |
| `name` | String | 라우트를 식별하는 고유 이름 |
| `redirect` | String / Object | 강제 이동 대상 경로 |

컴포넌트는 시작 때 불러오는 정적 import 또는 실제 진입 시 불러오는 동적 import로 지정할 수 있다. 동적 import는 필요한 화면만 내려받는 Lazy Loading에 해당한다.

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
```

원문은 규모가 커질수록 모든 매핑을 코드에 직접 나열하기보다 데이터베이스 등에서 읽어오는 설계도 사용한다고 설명한다.

### 2. 라우터 등록: `src/main.js`

만든 라우터는 애플리케이션 인스턴스에 `app.use(router)`로 등록해야 한다. `import router from './router'`는 통상 `router` 폴더의 `index.js`를 가리킨다.

```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
```

### 3. 템플릿에서 사용: `RouterLink`, `RouterView`

- `<RouterLink to="...">`: SPA 내부 링크를 만든다.
- `<RouterView />`: 현재 URL과 일치한 화면 컴포넌트가 렌더링될 자리다.

일반 `<a href="/about">`는 브라우저 전체 새로고침을 일으켜 메모리의 `ref`, `computed` 같은 반응형 상태를 초기화할 수 있다. SPA 내부 이동에는 `RouterLink`를 쓴다.

```html
<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  <RouterView />
</template>
```

## `route`와 `router`, views와 components

| 요소 | 성격 | 위치 | 역할 |
| --- | --- | --- | --- |
| `route` | JavaScript 객체 | 각 컴포넌트의 `<script setup>` | 현재 주소·파라미터·쿼리 등 활성 경로 정보 |
| `router` | JavaScript 객체 | `src/router/index.js`, `src/main.js` | 앱 전체 라우팅 시스템 제어 |
| `RouterView` | Vue 내장 컴포넌트 | 레이아웃 | 현재 URL에 매칭된 컴포넌트의 출력 위치 |
| `RouterLink` | Vue 내장 컴포넌트 | 메뉴·내비게이션 | 페이지 새로고침 없이 URL 변경 |

`views` 폴더의 컴포넌트는 `RouterView`에 직접 렌더링되는 페이지 단위 최상위 컴포넌트다. 보통 `DashboardView.vue`처럼 `View` 접미사를 붙이며, `routes`의 `component`에 직접 연결된다. 반면 `components`는 여러 화면에서 재사용하는 UI·기능 조각으로, 보통 RouterView에 직접 매핑하지 않는다.

## 현재 경로 읽기: `useRoute()`

`useRoute()`는 활성 경로의 반응형 정보를 제공하는 Composable이다. URL의 경로·동적 파라미터·쿼리 문자열·메타데이터를 템플릿과 스크립트에서 활용할 수 있다.

| 프로퍼티 | 설명 | 예 |
| --- | --- | --- |
| `route.params` | `:`가 붙은 동적 세그먼트 | `/user/:id` → `{ id: '42' }` |
| `route.query` | `?` 뒤 쿼리 문자열 | `/search?q=vue` → `{ q: 'vue' }` |
| `route.path` | 현재 요청 URL의 순수 경로 | `/user/42` |
| `route.name` | 라우터 설정의 고유 이름 | `UserDetail` |

```html
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.path)
console.log(route.params.id)
</script>

<template>
  <p>사용자 ID: {{ route.params.id }}</p>
  <p>검색 키워드: {{ route.query.q }}</p>
</template>
```

### 동적 세그먼트와 쿼리 문자열

`/weather/:cityId`처럼 콜론 뒤에 둔 부분은 동적 세그먼트이며 `route.params.cityId`로 받는다. `/category/:categoryId/product/:productId`처럼 여러 동적 세그먼트도 각각 `params` 속성으로 들어간다. `/user/:userId/posts`에서 `posts`처럼 고정된 부분은 `params`에 포함되지 않는다.

반면 `/weather?search=수원&page=2`의 `search`, `page`는 `route.query`에 자동 파싱된다. 쿼리는 라우터 설정에 동적 세그먼트 선언을 추가하지 않아도 확장할 수 있으며, 마운트 시 기존 URL 값으로 화면 상태를 복원하는 데 활용할 수 있다.

## 코드로 이동하기: `useRouter()`

`useRouter()`는 Router 인스턴스를 가져와 클릭 링크 밖의 이벤트·비동기 작업에서 이동시키는 Composable이다.

| 메서드 | 동작 |
| --- | --- |
| `router.push()` | 새 히스토리 항목을 추가해 이동(뒤로 가기 가능) |
| `router.replace()` | 현재 히스토리를 교체해 이동(뒤로 가기 불가) |
| `router.go(n)` | 히스토리에서 앞·뒤로 n단계 이동 |
| `router.back()` / `router.forward()` | 이전 / 다음 기록으로 이동 |

```javascript
import { useRouter } from 'vue-router'

const router = useRouter()

const handleGoHome = () => router.push('/')
const handleLoginRedirect = () => router.replace('/')
const handleAdvancedMove = () => {
  router.push({
    name: 'WeatherDetail',
    params: { cityId: 'city_02' },
    query: { search: '수원' },
  })
}
```

정의하지 않은 URL은 기본적으로 매칭 컴포넌트가 없어 `RouterView`가 빈 화면처럼 보일 수 있다. 마지막 route에 `/:pathMatch(.*)*` catch-all 패턴을 두고 `NotFoundView`를 매핑하면 일반적인 404 화면을 구현할 수 있다.

## Navigation Guard: 진입 전의 접근 제어

Navigation Guard는 경로 전환 직전에 실행되는 로직이다. 로그인 필요 페이지 차단·관리자 권한 확인·최종 데이터 검사·분석 로그 기록 등에 사용한다.

| 종류 | 실행 범위 |
| --- | --- |
| Global Guard | 모든 라우트 전환 |
| Per-route Guard | 지정한 라우트 |
| In-component Guard | 컴포넌트 내부 |

| Hook | 시점 | 대표 용도 |
| --- | --- | --- |
| `router.beforeEach` | 이동 시작 직전 | 인증·권한 확인 |
| `router.beforeResolve` | 컴포넌트/비동기 라우트 분석 후, 진입 직전 | 최종 데이터·토큰 확인 |
| `router.afterEach` | 화면 전환 완료 후 | 로그·분석 전송 |

```javascript
router.beforeEach((to, from, next) => {
  const isAuthenticated = false
  if (to.meta.isAuth && !isAuthenticated) {
    next('/')
  } else {
    next()
  }
})
```

## Pinia: 전역 반응형 상태 저장소

Pinia는 컴포넌트 계층과 무관하게 반응형 데이터를 공유하는 Vue 3의 공식 상태 관리 라이브러리다. 화면이 커질수록 props와 emits만으로 먼 컴포넌트까지 상태를 전달하기 어려워질 때 Store를 별도로 둔다. Vue 2에서는 Vuex가 주로 사용됐다.

Store는 인증·UI·알림·공통 코드처럼 의미 있는 상태 묶음별 파일로 나눌 수 있다. 핵심은 다음 세 종류다.

| Pinia 개념 | Vue 3 대응 | 역할 |
| --- | --- | --- |
| `state` | `ref()` / `reactive()` | 전역 공유 원본 데이터 |
| `getters` | `computed()` | state를 기반으로 하는 읽기 전용 파생 값 |
| `actions` | 일반 함수 | 상태 변경·비동기 API 통신 |

```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  return { count, doubleCount, increment }
})
```

Store의 state/getter를 일반 구조 분해 할당하면 반응형 연결이 끊길 수 있다. 데이터 속성은 `storeToRefs(counterStore)`로 꺼내고, action은 일반 구조 분해 할당을 해도 된다.

```javascript
import { storeToRefs } from 'pinia'

const { count, doubleCount } = storeToRefs(counterStore)
const { increment } = counterStore
```

## 인증 Store와 Guard의 결합

인증 Store는 토큰·사용자·로그인 여부를 전역에 보관하고, 로그인 성공 시 저장하며 로그아웃 시 제거한다. 원문 사례에서는 새로고침 뒤에도 상태를 복원하려고 `localStorage`를 이용한다.

```javascript
export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('accessToken') || null)
  const user = ref(JSON.parse(localStorage.getItem('userInfo') || 'null'))
  const isLoggedIn = computed(() => !!token.value)

  function login(userData, authToken) {
    user.value = userData
    token.value = authToken
    localStorage.setItem('accessToken', authToken)
    localStorage.setItem('userInfo', JSON.stringify(userData))
  }

  function logout() {
    user.value = null
    token.value = null
    localStorage.removeItem('accessToken')
    localStorage.removeItem('userInfo')
  }

  return { token, user, isLoggedIn, login, logout }
})
```

Guard 안에서 Store를 읽어 `to.meta.requiresAuth`와 로그인 상태를 비교하면, 비로그인 사용자를 로그인 화면으로 보내고 원래 목적 경로를 query로 전달하는 흐름을 만들 수 있다.

## HTTP·REST API와 프런트엔드/백엔드 역할

HTTP는 브라우저(Client)와 웹 서버(Server)가 데이터를 주고받는 표준 통신 규약이다. Client가 Request를 보내면 Server가 Response를 돌려준다.

| HTTP 메서드 | CRUD | 의미 |
| --- | --- | --- |
| GET | Read | 서버 데이터를 변경하지 않고 조회 |
| POST | Create | 새 데이터 생성 요청 |
| PUT / PATCH | Update | 기존 데이터 전체 / 일부 변경 |
| DELETE | Delete | 특정 데이터 삭제 |

REST API는 자원을 이름으로 구분하고 HTTP 메서드로 CRUD 행위를 표현하는 웹 인터페이스 스타일이다. URI는 `/weather`, `/users`, `/cities`처럼 명사 중심으로 두고, `getWeather`처럼 동사를 URL에 넣지 않는 원칙을 제시한다.

프런트엔드는 UI/UX, 이벤트 감지, 받은 데이터의 화면 렌더링을 맡고, 백엔드는 비즈니스 로직·보안·데이터베이스 제어와 API 응답을 맡는다.

## Axios: 비동기 API 호출

Axios는 HTTP 요청 라이브러리다. 브라우저 내장 Fetch와 달리 응답 JSON 변환, 오류 처리 편의 기능, `axios.create()` 기반 Base URL, 요청·응답 인터셉터를 제공한다. 인증 토큰은 보통 요청 인터셉터에서 `Authorization: Bearer …` 헤더에 넣는다. 실제 비밀 키나 토큰은 코드와 이 노트에 기록하지 않는다.

```javascript
import { ref } from 'vue'
import axios from 'axios'

const weatherData = ref(null)
const isLoading = ref(false)

const handleFetchWeather = async () => {
  isLoading.value = true
  try {
    const response = await axios.get('/api/weather', {
      params: { lat: 35.158582, lon: 126.804975 },
    })
    weatherData.value = response.data
  } catch (error) {
    console.error('통신 중 오류:', error)
  } finally {
    isLoading.value = false
  }
}
```

`axios.get`, `post`, `put`, `patch`, `delete`는 Promise를 반환한다. Promise 체이닝은 `.then().catch()`로, 현대적인 비동기 흐름은 대체로 `async / await`와 `try/catch/finally`로 작성한다. `await`는 응답을 기다리는 동안 함수 바깥의 다른 작업을 막지 않으며, 응답 이후의 처리 순서를 읽기 쉽게 만든다.

## 주의점

- SPA 내부 이동에는 `<a>`보다 `RouterLink`를 사용해 전체 새로고침과 상태 초기화를 피한다.
- catch-all route는 일반 route 뒤, 즉 `routes` 배열의 마지막에 둔다.
- `route`는 현재 위치 정보, `router`는 이동을 실행하는 인스턴스라는 역할 차이를 구분한다.
- Pinia state/getter의 구조 분해에는 `storeToRefs`를 사용해 반응성을 보존한다.
- JWT Payload는 Base64로 쉽게 읽을 수 있으므로 민감정보를 담지 않는다. 토큰·API 키 같은 비밀값은 저장소와 학습 노트에 남기지 않는다.
- `localStorage` 기반 토큰 보관에는 XSS 위험 등 별도 보안 검토가 필요하다. 원문은 상태 유지 흐름을 설명한 것이며, 보안 정책을 대체하지 않는다.
- HTTP Method와 CRUD의 관례는 API 설계의 일관성을 위한 것이며, 서버의 인증·인가·입력 검증을 대체하지 않는다.
