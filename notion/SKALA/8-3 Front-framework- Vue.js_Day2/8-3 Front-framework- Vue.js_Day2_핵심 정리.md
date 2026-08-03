---
title: "[8/3] Front-framework: Vue.js_Day2_핵심 정리"
notion_page_id: "3b01d84b-f68e-80db-994a-d7cd6fd8d2ea"
source_url: "https://app.notion.com/p/3b01d84bf68e80db994ad7cd6fd8d2ea"
synced_at: "2026-08-03T00:05:00+09:00"
content_sha256: "007b59f1af9ce5488998eac3fb64cc82a422bc83760a1fe0519b69edbcdcc750"
tags: [notion, skala, learning, vue, frontend]
---

# [8/3] Front-framework: Vue.js_Day2_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b01d84bf68e80db994ad7cd6fd8d2ea) (2026-08-03 확인)
> 
> 맥락: [[notion/SKALA/7-31 Front-framework- Vue.js_Day1/7-31 Front-framework- Vue.js_Day1_핵심 정리|Vue.js Day1]]의 프레임워크·컴포넌트 기초를 이어, Vue 3 Composition API의 상태 관리·감시·컴포넌트 통신을 다룬다.

## Composition API 개요

Composition API는 Vue 3에서 도입된 작성 방식으로, 컴포넌트의 데이터·함수·계산된 값·생명주기 로직처럼 **서로 관련된 로직을 한 곳에 조합**한다. Vue 2의 Options API는 `data`, `computed`, `methods`, Lifecycle Hook을 옵션별로 나누므로 큰 컴포넌트에서는 하나의 기능에 관련된 코드가 흩어질 수 있다. Composition API는 기능 단위 응집도를 높이는 방향이다.

Vue 3.2부터는 `<script setup>` 안에 Composition API 코드를 작성할 수 있다.

```javascript
<script setup>
// Composition API 코드 작성 위치
</script>
```

### Vue 3 내장 함수의 분류

| 카테고리 | 주요 함수 |
| --- | --- |
| 애플리케이션 | `createApp`, `createSSRApp`, `app.*()`, `app.config.*` |
| 반응형 상태 관리 | `ref`, `reactive`, `readonly`, `shallowRef`, `shallowReactive`, `shallowReadonly`, `toRef`, `toRefs`, `customRef`, `unref`, `toRaw`, `markRaw`, `isRef`, `isReactive`, `isReadonly` |
| 계산 및 감시 | `computed`, `watch`, `watchEffect` |
| 라이프사이클 | `setup`, `onMounted`, `onUpdated`, `onUnmounted`, `onBeforeMount`, `onBeforeUpdate`, `onBeforeUnmount`, `onActivated`, `onDeactivated`, `onErrorCaptured` |
| 컴포넌트 구성/메타 | `defineComponent`, `defineProps`, `defineEmits`, `useAttrs`, `defineExpose`, `useSlots`, `withDefaults`, `getCurrentInstance` |
| 렌더링/DOM | `h`, `resolveComponent`, `withDirectives`, `renderList`, `renderSlot`, `mergeProps`, `nextTick`, `useCssModule`, `useCssVars` |
| 의존성 주입 | `provide`, `inject`, `hasInjectionContext` |

핵심 흐름은 `ref`·`reactive`로 상태를 만들고, `computed`로 파생값을 만들며, `watch`·`watchEffect`로 상태 변화의 부수 효과를 처리하는 것이다.

## Reactive State — `ref()`

`ref()`는 숫자·문자열·boolean 같은 원시 타입과 배열·객체 같은 참조 타입을 모두 반응형 상태로 만들 수 있다. `<script setup>`에서는 `.value`로 읽고 바꾸지만, `<template>`에서는 자동 언래핑되어 변수명만 사용한다.

```javascript
<script setup>
import { ref } from 'vue'

const count = ref(0)
const name = ref('홍길동')
const isActive = ref(true)
const items = ref(['사과', '배'])
const user = ref({ name: '이순신', age: 30 })

const increaseRef = () => {
  count.value++
}
const changeUserName = () => {
  user.value.name = '장보고'
}
</script>
```

```html
<template>
  <div class="practice-section">
    <h2>반응형 상태 ref() 기초</h2>
    <p>Ref 카운트: <strong>{{ count }}</strong></p>
    <p>이름: <input v-model="name" />{{ name }}</p>
    <p>활성 상태: {{ isActive ? '활성' : '비활성' }}</p>
    <p>과일 목록: {{ items.join(', ') }}</p>
    <p>사용자 정보: 이름 - {{ user.name }}, 나이 - {{ user.age }}</p>
    <button @click="increaseRef">Ref 변수 증가</button>
    <button @click="isActive = !isActive">토글</button>
    <button @click="items.push('귤')">과일 추가</button>
    <button @click="changeUserName">사용자 이름 변경</button>
  </div>
</template>
```

객체 속성에는 `user.value.name`처럼 `.value` 뒤에 일반 객체 접근을 사용한다. 단, 템플릿에서는 `user.name`으로 충분하다.

## Reactive State — `reactive()`

`reactive()`는 객체·배열·`Map`·`Set` 등 **참조 자료형만** 반응형으로 만든다. `ref`와 달리 스크립트와 템플릿 모두에서 `.value` 없이 속성에 접근한다.

```javascript
import { reactive } from 'vue'

let state = reactive({ count: 0 })

// ❌ 새 객체로 통째로 교체하면 기존 반응성 연결이 끊어진다.
state = { count: 5 }

// ✅ 기존 반응형 객체의 속성을 바꾼다.
state.count = 5
```

반응형 객체를 구조 분해 할당하거나 통째로 재할당하면 연결이 끊길 수 있다. `reactive` 객체의 속성을 구조 분해해 써야 한다면 `toRef`·`toRefs`를 사용해 반응형 참조를 유지한다. 원문은 이 약점 때문에 객체·배열도 `ref()`로 통일하는 현업 경향을 언급한다.

| 함수 | 의미 |
| --- | --- |
| `readonly` | 반응형 객체를 읽기 전용으로 만든다. |
| `shallowRef` | 객체 내부가 아니라 참조 자체의 교체를 중심으로 감지한다. |
| `shallowReactive` / `shallowReadonly` | 최상위 레벨만 반응형/읽기 전용으로 처리한다. |
| `toRef` / `toRefs` | `reactive`의 속성을 반응형 `ref`로 꺼낸다. |
| `unref` | ref면 `.value`, 아니면 원값을 반환한다. |
| `toRaw` / `markRaw` | Vue 반응형 프록시 밖의 원본을 다뤄야 할 때 사용한다. |

## `computed()` — 캐시되는 파생 값

`computed()`는 `ref`·`reactive`에 의존하는 파생 값을 만든다. 의존성이 바뀔 때만 다시 계산하고, 바뀌지 않으면 이전 값을 재사용(캐싱)한다. 기본적으로 읽기 전용이며, 스크립트에서는 `.value`, 템플릿에서는 자동 언래핑으로 사용한다.

```javascript
import { ref, computed } from 'vue'

const count = ref(0)
const dummy = ref(0)

const getMethodResult = () => {
  console.log('일반 함수 실행됨')
  return count.value * 2
}

const doubleCount = computed(() => {
  console.log('Computed 연산 실행됨')
  return count.value * 2
})
```

일반 함수를 템플릿에서 호출하면 리렌더링마다 실행된다. 반면 `doubleCount`는 `count`가 바뀔 때만 재계산한다. 따라서 `dummy`만 바꾸면 일반 함수는 실행될 수 있지만 `computed`는 캐시를 재사용한다.

## `watch()`와 `watchEffect()`

`watch()`는 지정한 반응형 데이터가 바뀔 때 API 재호출·저장·로그처럼 **부수 효과(side effect)** 를 실행한다. 콜백은 새 값과 이전 값을 받는다.

```javascript
import { ref, watch } from 'vue'

const currentCity = ref('서울')
watch(currentCity, (newValue, oldValue) => {
  console.log(`[서버 요청] ${oldValue} → ${newValue}`)
})
```

여러 데이터를 동시에 감시할 때는 배열을 첫 번째 인자로 넘긴다.

```javascript
watch([city, dateType], ([newCity, newDate], [oldCity, oldDate]) => {
  // 어느 하나라도 바뀌면 실행
})
```

### 객체·배열 감시의 주의점

`ref`로 만든 객체·배열의 내부 속성 변화까지 감지하려면 `{ deep: true }`가 필요하다. 다만 deep watch에서는 같은 객체 참조를 보므로 `newValue`와 `oldValue`가 모두 최신 값처럼 보일 수 있다. 이전 값을 확실히 비교해야 하면 특정 속성만 getter로 감시한다.

```javascript
const user = ref({ name: '홍길동', age: 20 })

watch(user, (newValue) => {
  // 객체 내부 전체 감시
}, { deep: true })

watch(() => user.value.age, (newAge, oldAge) => {
  // 특정 원시값을 감시하므로 이전 값 비교 가능
})
```

`reactive` 객체를 직접 `watch(state, callback)`으로 넘기면 내부 속성을 자동으로 깊게 감시한다. 그러나 이전 값 참조 문제는 같으므로, `watch(() => state.price, callback)`처럼 특정 속성을 감시하는 방식이 비교에 적합하다.

`watchEffect()`는 별도로 감시 대상을 선언하지 않는다. 실행 중 실제로 접근한 반응형 데이터가 자동으로 의존성으로 등록되고, 처음 한 번 즉시 실행된다. 과거 값이 아니라 현재 상태를 기반으로 여러 의존성을 함께 추적할 때 적합하다.

```javascript
import { ref, watchEffect } from 'vue'

const username = ref('홍길동')
const age = ref(20)

watchEffect(() => {
  console.log(`이름:${username.value} / 나이:${age.value}`)
})
```

| 항목 | `watch` | `watchEffect` |
| --- | --- | --- |
| 감시 대상 | 명시적으로 지정 | 실행 중 접근한 값 자동 추적 |
| 최초 실행 | 기본적으로 변경 시 | 즉시 1회 실행 |
| 이전 값 | 제공 | 제공하지 않음 |
| 적합한 경우 | 변화 전후 비교·정확한 트리거 | 여러 의존성·초기 실행이 필요한 동기화 |

## 컴포넌트와 라이프사이클

Vue 컴포넌트는 독립적이고 교체 가능한 UI 단위이며, 컴포넌트 트리에서 부모·자식·형제 관계를 이룬다. 자식은 부모의 내부 변수에 직접 접근하지 않고 Props로 데이터를 받고, 부모는 자식의 이벤트를 Emits로 받는다. 형제끼리 직접 통신하지 않으며 부모를 경유한다.

라이프사이클은 생성 → 마운트 → 업데이트 → 언마운트의 순서로 진행한다.

| 단계 | 대표 훅 | 주된 용도 |
| --- | --- | --- |
| 생성 | `<script setup>` 본문, `setup()` | 상태·함수 초기화 |
| 마운트 전/후 | `onBeforeMount`, `onMounted` | DOM 접근, 초기 API 요청 |
| 업데이트 전/후 | `onBeforeUpdate`, `onUpdated` | 화면 재렌더링 전후 처리 |
| 언마운트 전/후 | `onBeforeUnmount`, `onUnmounted` | 타이머·이벤트 리스너 정리 |

```javascript
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const count = ref(0)
let timerId = null

onMounted(() => {
  timerId = setInterval(() => { count.value++ }, 3000)
})

onUnmounted(() => {
  clearInterval(timerId)
})
</script>
```

`onUnmounted`에서 타이머나 전역 이벤트 리스너를 정리하지 않으면 컴포넌트가 사라진 뒤에도 작업이 남아 메모리 누수로 이어질 수 있다.

## Props와 Emits — 단방향 통신

Vue의 기본 데이터 흐름은 **Props는 부모 → 자식**, **Emits는 자식 → 부모**다. `defineProps`와 `defineEmits`는 `<script setup>`에서 import 없이 쓰는 컴파일러 매크로다.

```javascript
// ChildComponent.vue
<script setup>
defineProps({
  message: String,
  likes: { type: Number, required: true },
  status: { type: String, default: '대기 중' }
})

const emit = defineEmits(['update-request'])
const requestUpdate = () => emit('update-request', 'Child에서 가공한 값')
</script>
```

```html
<!-- ParentComponent.vue -->
<template>
  <ChildComponent
    :message="parentMessage"
    :likes="likes"
    @update-request="handleUpdateRequest"
  />
</template>
```

Props는 자식에서 읽기 전용이다. 자식이 `props.likes = 999`처럼 직접 바꾸면 안 되며, 변경 요청은 이벤트로 부모에 전달해야 한다. JavaScript 변수명은 `camelCase`, 템플릿 속성은 `kebab-case`로 쓰는 관례도 중요하다. 예를 들어 자식의 `cityName` prop은 부모 템플릿에서 `:city-name="selectCityName"`으로 전달한다.

## `provide` / `inject`와 Props Drilling

깊은 컴포넌트 트리에서 중간 컴포넌트가 필요하지 않은 값을 전달만 하는 현상을 Props Drilling이라고 한다. 조상은 `provide('키', 값)`, 후손은 `inject('키')`로 중간 계층을 건너뛸 수 있다.

```javascript
// GrandParent.vue
import { ref, provide } from 'vue'
const themeColor = ref('dark-mode')
provide('globalTheme', themeColor)

// GrandChild.vue
import { inject } from 'vue'
const theme = inject('globalTheme')
```

이는 조상 → 후손의 주입 방식이며, 자식 → 부모 통신을 대신하지 않는다. 반대 방향 요청은 Emits를 사용한다.

## Slot

Slot은 부모가 자식 컴포넌트의 지정 영역에 마크업을 주입하는 기능이다.

- **Default Slot**: 자식의 `<slot>` 자리에 부모 콘텐츠를 넣는다.
- **Named Slot**: 자식의 `<slot name="header">`에 부모가 `<template #header>`를 제공한다.
- **Scoped Slot**: 자식이 slot 속성으로 데이터를 제공하고, 부모가 `v-slot`으로 받아 렌더링한다.

```html
<!-- SlotNamedChild.vue -->
<template>
  <div class="base-card">
    <header><slot name="header"></slot></header>
    <main><slot></slot></main>
  </div>
</template>
```

```html
<!-- SlotNamedParent.vue -->
<template>
  <SlotNamedChild>
    <template #header><h3>주입 제목</h3></template>
    <p>default slot 콘텐츠</p>
  </SlotNamedChild>
</template>
```

## 학습 체크포인트

1. 상태가 단순 값이든 객체든 `ref`로 만들고, 스크립트에서만 `.value`가 필요함을 구분한다.
2. `reactive` 객체는 통째로 재할당하거나 무심코 구조 분해하지 않는다.
3. 화면에 보여 줄 계산 결과는 `computed`, 외부 요청·저장 같은 반응 작업은 `watch`로 분리한다.
4. 객체의 특정 이전 값을 비교해야 하면 deep watch보다 getter 기반 감시를 우선 검토한다.
5. 컴포넌트 경계를 넘는 데이터는 Props로 내려 보내고, 변경 요청은 Emits로 올린다.
6. HTML 예제는 실행 가능한 본문이 아니라 항상 `html` 코드 펜스 안에서 보존한다.
