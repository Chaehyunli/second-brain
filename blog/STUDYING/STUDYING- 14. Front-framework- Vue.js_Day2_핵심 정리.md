---
title: "[STUDYING] 14. Front-framework: Vue.js_Day2_핵심 정리"
created: 2026-08-04
updated: 2026-08-04
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-03
source_url: https://ch010104.tistory.com/330
---
# [STUDYING] 14. Front-framework: Vue.js_Day2_핵심 정리

## 원문

https://ch010104.tistory.com/330

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

Vue 3에서 도입된 현대적인 JavaScript 코딩 방식으로, 컴포넌트의 로직(데이터, 함수, 계산된 속성 등)을 하나의 세트로 조합(Composition)하여 작성하는 방법을 제공함.

데이터, Computed, methods, Lifecycle Hook 등을 각각의 옵션 속성(객체 키)으로 분리하여 구성함

## 원문 기반 개념 정리

### Composition API 개요

Vue 3에서 도입된 현대적인 JavaScript 코딩 방식으로, 컴포넌트의 로직(데이터, 함수, 계산된 속성 등)을 하나의 세트로 조합(Composition)하여 작성하는 방법을 제공함.

### Options API와의 비교

Vue 2에서는 Options API 방식을 사용함

데이터, Computed, methods, Lifecycle Hook 등을 각각의 옵션 속성(객체 키)으로 분리하여 구성함

관련 로직이 파일 안에 흩어져 있어 큰 컴포넌트에서 가독성이 떨어짐

Composition API는 연관된 로직을 한 곳에 모아 작성하므로 가독성이 높음

### 작성 방법

Vue 3.2부터 `<script setup>` 안에 작성하면 됨

```text
<script setup>
// Composition API 코드 작성 위치
</script>
```

### Vue 3 내장함수 카테고리

Vue 프레임워크에서 핵심 기능을 수행하는 함수들을 카테고리별로 제공함. 빨간색으로 표기된 함수가 특히 핵심적으로 자주 사용됨.

### 주요 포인트

반응형 상태 관리에서 핵심은 ref와 reactive — 이 둘이 Composition API의 데이터 선언 중심임

계산 및 감시 카테고리의 computed, watch, watchEffect 세 함수가 핵심 감시·파생값 처리를 담당함

라이프사이클 훅은 Options API의 created, mounted 등에 대응되는 함수형 버전임

### Reactive State - ref()

원시 타입(Primitive Datatype)과 참조 자료형(Array, Object 등) 모두를 반응형 상태로 만들 수 있는 함수임.

### 사용 규칙

`<script setup>` 상단에서 ref를 import해야 함

`<script setup>` 내부에서는 .value로 접근함

`<template>` 내부에서는 .value 없이 변수명만으로 사용 가능함 (자동 언래핑)

### ref() 예시

```typescript
<!-- Reactive State - ref() Example -->
<script setup>
import { ref } from 'vue'

const count = ref(0)
const name = ref('홍길동')
const isActive = ref(true)
const items = ref(['사과', '배'])
const user = ref({ name: '이순신', age: 30 })

const increaseRef = () => {
  count.value++         // script 내부: .value 필수
}
const changeUserName = () => {
  user.value.name = '장보고'
}
</script>

<template>
  <div class="practice-section">
    <h2>반응형 상태 ref() 기초</h2>
    <p>Ref 카운트: <strong>{{ count }}</strong></p>   <!-- template: .value 불필요 -->
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

숫자·문자열·boolean·배열·객체 등 모든 자료형에 ref() 적용 가능함

객체 내부 속성 접근 시 user.value.name처럼 .value 이후 일반 객체처럼 접근함

### Reactive State - reactive()

참조 자료형(객체, 배열, Map, Set)만 반응형 상태로 만드는 함수임.

### 사용 규칙

`<script setup>` 상단에서 reactive를 import해야 함

`<script setup>`과 `<template>` 모두에서 .value 없이 일반 객체처럼 접근함

### reactive()의 반응성 단절 문제

반응형 객체를 통째로 교체하거나 구조 분해 할당하면 반응성 연결이 끊어짐.

```text
// reactive() 반응성 단절 주의
let state = reactive({ count: 0 })

// ❌ 통째로 새 객체를 갈아끼우면 반응성 연결이 끊어진다.
state = { count: 5 }

// ✅ 내부의 알맹이 속성만 조심스럽게 변경해야 한다.
state.count = 5
```

이 약점 때문에 현업에서는 객체·배열을 다룰 때도 ref()로 통일해서 쓰는 추세가 강함

### reactive() 예시

```typescript
<!-- Reactive State - reactive() Example -->
<script setup>
import { reactive } from 'vue'

// 객체(Object) reactive
const userReactive = reactive({ name: '이순신', age: 30 })
const celebrateReactive = () => { userReactive.age++ }

// 배열(Array) reactive
const items = reactive(['사과', '바나나'])
const addItem = () => { items.push(`과일${items.length+1}`) }
const removeItem = (index) => { items.splice(index, 1) }
</script>

<template>
  <div class="practice-section">
    <h2>반응형 상태 reactive() 특징 및 주의점</h2>
    <h3>1) 객체(Object) reactive</h3>
    <p>이름: {{ userReactive.name }} / 나이: {{ userReactive.age }}세</p>
    <button @click="celebrateReactive">reactive 나이 한 살 추가</button>

    <h3>2) 배열(Array) reactive</h3>
    <ul>
      <li v-for="(item, index) in items" :key="index">
        {{ item }}
        <button @click="removeItem(index)">삭제</button>
      </li>
    </ul>
    <button @click="addItem">과일 항목 추가</button>
  </div>
</template>
```

### 배열 reactive 사용 시 참고사항

reactive로 선언된 배열은 items = ['a', 'b']처럼 전체를 새 배열로 재할당하면 반응형 연결이 끊어짐

배열 데이터 변경 시 push / splice 등 변이 메서드를 쓰거나, 재할당이 필요하면 ref()를 사용하는 것을 권장함

### Reactive State - 기타 함수들

반응형 상태 관리에 사용되는 함수들을 분류별로 정리한 요약표임. ref와 reactive 외에도 다양한 보조 함수가 존재함.

### 분류별 포인트

shallow* 계열은 성능 최적화 목적으로, 깊은 중첩 객체까지 추적하지 않고 최상위 레벨만 감시함

toRef / toRefs는 reactive 객체를 구조 분해할 때 반응성을 유지하기 위해 사용함 — 일반 구조 분해 할당만 하면 반응성이 끊어지므로 이 함수들로 감싸서 추출함

toRaw / markRaw는 Vue의 반응형 시스템 밖에서 객체를 다뤄야 할 때 활용함 (예: 서드파티 라이브러리 전달)

unref(x)는 isRef(x) ? x.value : x와 동일한 동작으로, ref 여부와 관계없이 안전하게 값을 꺼낼 때 편리함

### Computed & Watchers - computed()

의존하는 반응형 데이터(ref, reactive)가 변경될 때 자동으로 다시 계산되는 파생 값을 만드는 함수임.

### 핵심 특징

계산된 값은 메모리에 **캐싱(Caching)**되어 성능이 좋음

일반 함수는 화면이 바뀔 때마다(리렌더링) 무조건 재실행됨

computed는 의존하는 반응형 데이터가 바뀔 때만 재연산하고, 그 외에는 이전 결과를 재사용함

computed()로 생성한 Computed Property는 기본적으로 읽기 전용 — 다른 값으로 재할당 불가

### Syntax

```typescript
// Computed & Watchers - computed() 기본 문법
import { computed } from 'vue';

const 식별자 = computed(() => { return 값 })
```

인자로 콜백 함수를 넘기면, Vue 내부에서 Computed Ref 객체를 반환함 (ref()의 결과물과 구조가 비슷함)

`<script setup>` 영역에서는 .value를 붙여서 값을 읽어야 함

`<template>` 내에서는 .value 없이 사용 가능함 (자동 언래핑)

### computed() 예시 — 캐싱 동작 비교

```typescript
<!-- Computed & Watchers - computed() Example -->
<script setup>
import { ref, computed } from 'vue'

const count = ref(0)
const dummy = ref(0) // computed와 무관한 변수

// 1. 일반 함수: 화면이 조금이라도 리렌더링되면 무조건 재실행
const getMethodResult = () => {
  console.log('❌ 일반 함수 실행됨!')
  return count.value * 2
}

// 2. Computed: count가 바뀔 때만 재연산 (dummy가 바뀌면 이전 값 재사용)
const doubleCount = computed(() => {
  console.log('✅ Computed 연산 실행됨!')
  return count.value * 2
})
</script>

<template>
  <div class="practice-section">
    <h2>computed() 캐싱 동작 비교</h2>
    <p>count: {{ count }} | dummy: {{ dummy }}</p>
    <button @click="count++">count 증가 (의존성 변경)</button>
    <button @click="dummy++">dummy 증가 (무관한 변경)</button>
    <!-- dummy 버튼을 누를 때 콘솔 출력 차이를 확인 -->
    <p>일반 함수 결과: {{ getMethodResult() }}</p>
    <p>Computed 결과: {{ doubleCount }}</p>
  </div>
</template>
```

### Vue Component 재렌더링 동작 원리

count가 증가하면 Vue 반응형 시스템이 DOM 재렌더링 필요성을 감지함

템플릿을 다시 그릴 때 {{ getMethodResult() }}처럼 괄호로 직접 호출한 일반 함수는 조건 불문 무조건 재실행됨

{{ doubleCount }}는 count가 바뀔 때만 재연산, dummy만 바뀌면 캐싱된 이전 결과를 그대로 씀

### Console 창으로 차이 확인

count 증가 클릭 → 일반 함수 로그 + computed 로그 모두 출력됨

dummy 증가 클릭 → 일반 함수 로그만 출력됨 (computed는 재연산 없이 캐시 재사용) → () 괄호가 있는 getMethodResult() 는 함수이기 때문에, 화면이 재렌더링될 때마다 실행함.

### (참고) `<script setup>` 내 함수 정의 방식 3종 비교

```typescript
// <script setup> 함수 정의 방식 3종 예시
import { ref } from 'vue'
const message = ref('버튼을 누르세요')

// 1) 함수 선언문 (호이스팅 가능 - 하단에 있어도 위에서 호출 가능)
function 함수명() {
  message.value = '1번 함수 선언문 방식 발동!'
}

// 2) 함수 표현식 (호이스팅 불가 - 선언 후 호출 가능)
const 변수명 = function() {
  message.value = '2번 함수 표현식 방식 발동!'
}

// 3) 화살표 함수 (실무 표준 - 호이스팅 불가, 가장 컴팩트함)
const 변수명 = () => {
  message.value = '3번 화살표 함수 방식 발동!'
}
```

### Computed & Watchers - watch()

반응형으로 선언된 데이터의 값이 변경되었을 때, 후속 로직(비동기 통신, 데이터 저장 등)을 수행하도록 콜백 함수를 지정하는 함수임.

### Syntax

```typescript
// Computed & Watchers - watch() 기본 문법
import { watch } from 'vue';

watch(반응형데이터, (newVal, oldVal) => { 실행할 후속 로직 })
```

첫 번째 인자로 감시할 데이터를 받고, 두 번째 인자로 변경 시 실행할 콜백 함수를 지정함

콜백 함수의 인자로 변경된 새 값(newVal)과 변경되기 전의 값(oldVal)이 자동으로 전달됨

### watch() 예시

```typescript
<!-- Computed & Watchers - watch() Example -->
<script setup>
import { ref, watch } from 'vue'

const currentCity = ref('서울')
const logMessage = ref('아직 감시 시스템이 작동하지 않았습니다.')

// currentCity 변수를 유심히 감시하는 watch 시스템 가동
watch(currentCity, (newValue, oldValue) => {
// 값이 바뀌는 순간, 바뀐 알맹이(값) 두 개가 자동으로 주입됨
  logMessage.value = `👀 감시자 발동! [${oldValue}]에서 [${newValue}]로 변경됨.`
// 실무 활용처 시뮬레이션
  console.log(`🌐 [서버 요청 완료] 기상청 서버에서${newValue}의 날씨 API를 다시 조회합니다...`)
})
</script>

<template>
  <div class="practice-section">
    <h2>감시자 watch()의 원리와 실무 활용</h2>
    <h3>🗺 지역 선택 제어판</h3>
    <p>현재 선택된 도시: {{ currentCity }}</p>
    <button @click="currentCity = '서울'">서울 선택</button>
    <button @click="currentCity = '수원'">수원 선택</button>
    <button @click="currentCity = '부산'">부산 선택</button>
    <div class="monitor">
      <h3>👁 파수꾼(watch) 모니터링 시스템</h3>
      <p>{{ logMessage }}</p>
      <small style="color: gray">(버튼을 누른 후 브라우저 콘솔창 F12를 확인해 보세요)</small>
    </div>
  </div>
</template>
```

### 동작 원리 정리

currentCity가 바뀌는 순간 watch 콜백이 자동 실행되며 newValue(바뀐 값)와 oldValue(이전 값)가 주입됨

실무에서는 이 콜백 안에서 API 재호출, 로컬스토리지 저장, 로그 기록 등 부수 효과(side effect) 처리에 활용함

computed가 "파생 값을 계산"하는 용도라면, watch는 "값 변화에 반응해 동작을 실행"하는 용도임

### watch() - Multi-Source Watch

반응형으로 선언된 여러 데이터를 한꺼번에 감시할 때 쓰는 기법임.

### Syntax

```typescript
// Multi-Source Watch 기본 문법
import { watch } from 'vue';

watch([변수1, 변수2], ([새값1, 새값2], [옛값1, 옛값2]) => { 실행할 후속 로직 })
```

첫 번째 인자에 감시할 대상들을 배열 [] 형태로 묶어 전달함

콜백 함수의 인자 배열 순서는 첫 번째 인자 배열의 순서와 동일함 ([변수1, 변수2] → [새값1, 새값2], [옛값1, 옛값2])

배열 내 어느 하나라도 변하면 감시자 콜백 함수가 즉시 발동함

### Multi-Source Watch 예시

```sql
<!-- watch() Multi-Source Watch Example -->
<script setup>
import { ref, watch } from 'vue'

const city = ref('서울')
const dateType = ref('오늘')
const apiStatus = ref('대기 중...')

// 두 개의 ref 변수를 배열[] 형태로 묶어 동시에 감시
watch([city, dateType], ([newCity, newDate], [oldCity, oldDate]) => {
  apiStatus.value = `[변경 감지]${oldCity}(${oldDate}) →${newCity}(${newDate})`
// 실무 활용: 두 옵션 중 하나만 바뀌어도 통합 API 요청을 보냄
  console.log(`🌐 [통합 API 호출]${newCity}의${newDate} 날씨를 불러옵니다...`)
})
</script>

<template>
  <div class="practice-section">
    <h2>여러 개의 변수 동시 감시 (watch)</h2>
    <h3>날씨 조건 설정</h3>
    <label>도시: </label>
    <select v-model="city">
      <option value="서울">서울</option>
      <option value="수원">수원</option>
      <option value="부산">부산</option>
    </select>
    <label>날짜: </label>
    <label><input type="radio" value="오늘" v-model="dateType" /> 오늘</label>
    <label><input type="radio" value="내일" v-model="dateType" /> 내일</label>
    <label><input type="radio" value="주간예보" v-model="dateType" /> 주간예보</label>
    <div class="monitor">
      <h3>통합 모니터링 로그</h3>
      <p>현재 상태: {{ apiStatus }}</p>
    </div>
  </div>
</template>
```

### watch() - Deep Watch

ref()로 선언된 객체나 배열 내부의 속성 변화를 감지할 때 쓰는 기법임.

기본 watch는 객체·배열의 주소값(참조값)만 추적하므로 내부 속성이 바뀌어도 감지하지 못함. 내부 값 변화까지 추적하려면 { deep: true } 옵션을 명시해야 함.

→ ref로 선언된 변수는 값이 변경될 때, .value의 주소값(참조값)이 바뀌는 것임

### Syntax

```typescript
// Deep Watch 기본 문법
import { watch } from 'vue';

watch(반응형데이터, (newValue) => { 실행할 후속 로직 }, { deep: true })
```

### 주의점

deep: true를 쓰면 newValue와 oldValue가 똑같이 최신 값으로 출력됨 — 주소값이 같기 때문에 이전 값 추적이 불가함

이전 값까지 추적해야 하면 아래 "특정 속성만 감시하기" 방식을 사용해야 함 → 특정 속성만 감시할 경우, 주소값이 아닌 글자(알맹이 값)만 따로 받아와서 비교하기 때문에 이전 값이 추적이 가능함

### 객체의 특정 속성만 감시하기

```typescript
// 특정 속성만 감시 - getter 함수 방식 (★ oldValue 정상 수집 가능)
watch(() => 변수.value.속성, (새값, 옛값) => { ... })
```

이 방식을 쓰면 newValue와 oldValue가 정상적으로 구분되어 수집됨.

### Deep Watch 예시

```typescript
<!-- watch() Deep Watch Example -->
<script setup>
import { ref, watch } from 'vue'

const user = ref({
  name: '홍길동',
  age: 20,
})

const logDeep = ref('아직 반응 없음')
const logTarget = ref('아직 반응 없음')

// 실패하는 예시 (가장 많이 범하는 오류)
// watch(user, () => { console.log('이 로그는 영원히 안 찍힙니다.') })

// 해결책 1: deep 옵션을 켜서 객체 하위 속성 전체 감시
// ⚠ newVal과 oldVal이 똑같이 최신 값으로 나옴 (이전 값 추적 불가)
watch(user, (newVal) => {
    logDeep.value = `[deep 감지] 누군가 변경됨! 현재 이름:${newVal.name}, 나이:${newVal.age}`
  },
  { deep: true },
)

// 해결책 2: 화살표 함수로 특정 속성(age)만 콕 집어 감시 (★ 이전 값 추적 가능!)
watch(() => user.value.age, (newAge, oldAge) => {
    logTarget.value = `[타겟 감지] 나이가${oldAge}세 →${newAge}세로 변경됨!`
  },
)
</script>

<template>
  <div class="practice-section">
    <h2>ref 객체/배열 감시</h2>
    <h3>🧑 회원 데이터 조작 panel</h3>
    <p>이름: {{ user.name }} / 나이: {{ user.age }}세</p>
    <button @click="user.name = '이순신'">이름만 변경</button>
    <button @click="user.age++">나이만 변경 (age++)</button>

    <div class="monitor">
      <p>👁 1) deep: true 모니터 (전체 감시)</p>
      <p>{{ logDeep }}</p>
    </div>
    <div class="monitor target">
      <p>🎯 2) 화살표 함수 모니터 (나이만 타겟 감시)</p>
      <p>{{ logTarget }}</p>
    </div>
  </div>
</template>
```

### 두 방식 비교 요약

### watch() - reactive 반응형 데이터 감시

reactive()로 선언된 객체나 배열은 ref()와 달리 별도의 { deep: true } 옵션 없이도 내부 속성 변화를 자동으로 감지함. 단, 이전 값 추적 불가 문제는 동일하게 발생함.

### reactive() 전체 감시 vs 특정 속성 감시

reactive 객체를 통째로 감시하면 deep이 자동 적용되어 내부 속성 변화를 감지하지만, newVal과 oldVal이 똑같이 최신값으로 출력됨

특정 속성만 감시하려면 () => state.속성 형태의 getter 함수를 넘기면 이전 값 추적이 가능함 → state.속성 은 반응형 객체가 아닌 단순 숫자 원시값이기 때문에, 첫번째 파라미터로 () => state.속성 와 같이 작성해야함.

### reactive 반응형 데이터 watch() 예시

```typescript
<!-- watch() reactive 반응형 데이터 Example -->
<script setup>
import { reactive, ref, watch } from 'vue'

// reactive로 선언한 묶음 상품 데이터
const state = reactive({
  productName: '노트북',
  price: 1000,
})

const logAutoDeep = ref('대기 중...')
const logTarget = ref('대기 중...')

// 1) 변수명 그대로 감시 (자동 deep: true 작동)
// ⚠ newVal.price와 oldVal.price가 똑같이 최신값으로 나옴
watch(state, (newVal, oldVal) => {
  logAutoDeep.value = `[자동 deep] 가격 변동! 이전가격인척하는:${oldVal.price}원 → 현재가격:${newVal.price}원`
})

// 2) 화살표 함수로 특정 속성만 감시 (이전 값 추적 가능!)
// ✅ 특정 알맹이 값만 추출했으므로 진짜 과거 가격이 정상 보존됨
watch(
  () => state.price,
  (newPrice, oldPrice) => {
    logTarget.value = `[타겟 조준] 가격이 진짜 올랐음! 옛날값:${oldPrice}원 → 바뀐값:${newPrice}원`
  },
)
</script>

<template>
  <div class="practice-section">
    <h2>reactive() 데이터 watch 감시 규칙</h2>
    <h3>🛒 상품 정보 관리 (reactive)</h3>
    <p>상품명: {{ state.productName }} / 가격: {{ state.price }}원</p>
    <button @click="state.price += 500">가격 500원 인상</button>

    <div class="monitor auto">
      <p>👁 1) state 변수 통째로 감시 (deep 자동화)</p>
      <p>{{ logAutoDeep }}</p>
      <small>※ 주의: 이전 값과 현재 값이 똑같이 찍힌다.</small>
    </div>
    <div class="monitor target">
      <p>🎯 2) () => state.price 콕 집어 감시 (과거 추적)</p>
      <p>{{ logTarget }}</p>
      <small>※ 성공: 과거의 원본 가격이 칼같이 보존된다.</small>
    </div>
  </div>
</template>
```

### ref vs reactive watch 감시 비교 총정리

reactive는 .value 없이 속성에 바로 접근하므로 getter 함수에서도 state.price로 씀 (ref는 변수.value.price)

### watch() - 배열(Array) 감시 패턴

배열의 특정 인덱스 값이나 객체형 배열의 내부 속성을 감시할 때는 getter 함수 형태로 감시 대상을 지정해야 함.

### 기본형 배열의 특정 인덱스 값 감시

특정 인덱스의 값 자체(문자열, 숫자 등)를 감시할 때의 패턴임.

```typescript
// ref()로 생성된 기본형 배열 - 특정 인덱스 감시
const teamMembers = ref(['홍길동', '이순신', '강감찬'])
watch(() => teamMembers.value[0], (새값, 옛값) => { ... })

// reactive()로 생성된 기본형 배열 - 특정 인덱스 감시
const todoList = reactive(['프로젝트 기획', '퍼블리싱', 'Vue 개발'])
watch(() => todoList[0], (새값, 옛값) => { ... })
```

ref 배열은 .value[인덱스], reactive 배열은 .value 없이 배열[인덱스]로 접근함

getter 함수 방식이므로 새값과 옛값 모두 정상 수집됨

### 객체형 배열의 특정 객체 내부 속성 감시

배열의 원소가 객체일 때, 특정 객체의 내부 속성 변화까지 추적하려면 { deep: true } 옵션을 함께 사용해야 함.

```typescript
// ref()로 생성된 객체형 배열 - 특정 객체 내부 속성 감시
const cityWeather = ref([
  { name: '서울', temp: 25 },
  { name: '수원', temp: 22 }
])
watch(() => cityWeather.value[0], (새객체) => { ... }, { deep: true })

// reactive()로 생성된 객체형 배열 - 특정 객체 내부 속성 감시
const favorCities = reactive([
  { name: '수원', temp: 21 },
  { name: '부산', temp: 24 }
])
watch(() => favorCities[0], (새객체) => { ... }, { deep: true })
```

객체 내부 속성(예: temp)이 바뀌는 것까지 감지하려면 { deep: true }가 필요함

단, deep: true를 쓰면 oldValue 추적이 불가함 — 이전 속성값이 필요하면 속성까지 getter로 지정해야 함

### 배열 감시 패턴 정리

### Computed & Watchers - watchEffect()

감시 대상을 명시하지 않아도 함수 내부에서 접근한 반응형 데이터를 자동으로 추적해서 값이 바뀔 때마다 재실행되는 함수임.

### 핵심 특징

컴포넌트가 처음 태어날 때(최초 1회) 무조건 즉시 실행됨 — watch와의 가장 큰 차이점

함수 내부에서 접근한 반응형 데이터만 자동으로 감시 리스트에 등록됨

현재 시점의 값만 다루므로 이전 값(oldValue)은 제공하지 않음

### 의존성 자동 추적 원리 — Vue Proxy의 동작 방식

watchEffect가 "어떤 데이터를 감시할지 자동으로 안다"는 것은 Vue의 Proxy 기반 반응형 시스템 덕분임.

동작 순서는 다음과 같음.

watchEffect가 시작되면 Vue는 내부적으로 "의존성 수집 모드" 스위치를 켬 — 지금 실행되는 코드가 건드리는 모든 반응형 데이터를 받아 적겠다는 신호임

함수 내부가 실행되면서 user.value.name에 접근하는 순간, 해당 객체를 감싸고 있는 Proxy의 Getter가 동작함

Proxy가 Vue에게 "지금 watchEffect가 user.name을 읽어갔어!"라고 제보함

Vue는 이를 감시 목록에 등록해 두었다가, 나중에 user.value.name = '이순신'으로 바뀌면(Setter) watchEffect를 다시 실행시킴

한 줄 요약: watchEffect 함수가 실행되는 그 순간에 실제로 접근된 속성들을 Proxy가 중간에서 낚아채서 감시 목록으로 자동 등록하는 구조임.

### 속성 수준 추적 — 특정 속성에만 접근한 경우

```typescript
// watchEffect 의존성 추적 - 특정 속성만 접근
const user = ref({ name: '홍길동', age: 20 })

watchEffect(() => {
// 실행되는 순간 user.value.name 속성에 접근(Getter 실행)!
  console.log(user.value.name)
})
```

user.value.name이 바뀔 때만 watchEffect가 다시 실행됨

user.value.age = 21로 age를 바꿔도 watchEffect는 반응하지 않음 — 함수 실행 중에 age에 접근한 적이 없으므로 의존성으로 등록되지 않았기 때문임

이전 값 추적이 안됨

### Deep 추적 — 객체 전체를 다루는 경우

```typescript
// watchEffect 의존성 추적 - 객체 전체 접근
const user = ref({ name: '홍길동', age: 20 })

watchEffect(() => {
// 객체 전체를 사용하거나, JSON.stringify 등으로 내부를 순회할 때
  console.log(user.value)
})
```

콜백 함수가 실행되는 도중 접근하게 되는 모든 반응형 속성을 실시간으로 수집함

객체 내부의 모든 속성에 접근하게 되면 해당 객체의 모든 변경 사항을 자동으로 추적하게 됨

watchEffect의 경우, 개별값 추적이어도 이전값 추적이 안됨!!

### watchEffect() 예시

```typescript
<!-- Computed & Watchers - watchEffect() Example -->
<script setup>
import { ref, watchEffect } from 'vue'

const username = ref('홍길동')
const age = ref(20)
const logMessage = ref('대기 중...')

// 감시 대상을 지정하는 파라미터가 없음!
// Vue가 이 내부 코드를 읽고 'username'과 'age'를 자동으로 감시 리스트에 등록함
watchEffect(() => {
  logMessage.value = `[자동 감지] 이름:${username.value} / 나이:${age.value}세`

// 화면이 처음 켜질 때 1등으로 즉시 실행되는 증거를 콘솔에서 확인함
  console.log('🌐 watchEffect가 내부 변수 변경을 감지하여 실행되었습니다.')
})
</script>

<template>
  <div class="practice-section">
    <h2>자동 감시자 watchEffect()</h2>
    <p>이름: {{ username }} / 나이: {{ age }}세</p>
    <button @click="username = '이순신'">이름을 '이순신'으로 변경</button>
    <button @click="age++">나이 한 살 추가 (age++)</button>
    <div class="monitor">
      <h3>👁 watchEffect 자동 모니터링 시스템</h3>
      <p>{{ logMessage }}</p>
      <small style="color: gray">※ 새로고침하자마자 버튼을 안 눌러도 로그가 이미 찍혀있는 특징을 주목하세요!</small>
    </div>
  </div>
</template>
```

### watch vs watchEffect 비교

### Computed & Watchers - 기타 함수들

Computed & Watchers 카테고리의 함수 전체 요약표임.

### 타이밍 제어 함수 보충

watchPostEffect는 DOM이 완전히 업데이트된 이후에 실행되어야 하는 로직(예: DOM 요소의 크기·위치 측정)에 적합함

watchSyncEffect는 Vue의 비동기 큐를 거치지 않고 즉시 실행되므로 성능에 영향을 줄 수 있어 특수한 경우에만 사용함

일반적인 상황에서는 watchEffect로 충분하며, watchPostEffect / watchSyncEffect는 실행 타이밍을 세밀하게 제어해야 할 때 선택적으로 활용함

### Component Overview

### Component란?

Software공학에서 Component는 **독립적인 기능을 수행하며, 언제든지 다른 부품으로 교체할 수 있고, 다른 프로그램과 연결할 수 있는 '표준화된 소프트웨어 모듈(부품)'**을 뜻함. 가장 중요한 핵심은 독립성(Independency)과 교체 가능성(Replaceability)임.

### Vue Component란?

웹페이지를 구성하는 독립적이고 재사용 가능한 '블록(부품)'을 말함.

HTML, CSS, JavaScript를 하나의 .vue 파일 안에 뭉쳐 놓은 하나의 화면 단위를 뜻함 (SFC)

어플리케이션 하나를 완성하기 위해 여러 개의 컴포넌트를 사용함

컴포넌트는 일정한 형식을 가지고 내부적으로 Tree 구조로 연결됨

```text
<Root>
├── <Header>
├── <Main>
│   └── <Article> x2
└── <Aside>
    └── <Item> x3
```

### Component Overview - Hierarchy

### Parent-Child (부모-자식 관계)

다른 컴포넌트를 품고 있는 상위 블록이 부모, 그 안에 박혀서 작동하는 하위 블록이 자식이 됨

부모와 자식은 철저하게 독립되어 있어 자식은 부모의 변수를 가져다 쓸 수 없고, 부모 역시 자식의 내부를 들여다볼 수 없음

### Sibling (형제 관계)

동일한 부모 컴포넌트 아래에 나란히 조립된 자식 컴포넌트들끼리의 관계임

형제끼리는 다이렉트로 대화하는 선이 없음 — 형제에게 말을 걸고 싶다면 반드시 부모를 거쳐서 올라갔다가 내려와야 함

### Ancestors-Descendants (조상-후손 관계)

컴포넌트가 거대해져서 자식의 자식, 그 자식의 자식까지 내려가는 다중 계층 구조를 말함

### Component Overview - Component Local Registration

부모 컴포넌트가 자식 컴포넌트를 import하여 사용하는 방식임. 등록된 자식 컴포넌트는 `<template>` 영역에서 내장 태그처럼 쓸 수 있으며, PascalCase와 kebab-case 두 스타일 모두 사용 가능함.

```html
<!-- Component Local Registration -->
<script setup>
import BaseButton from './components/BaseButton.vue'
</script>

<template>
  <div class="box">
    <h3>컴포넌트 조립 테스트</h3>
    <hr />
    <BaseButton />           <!-- PascalCase -->
    <base-button></base-button>  <!-- kebab-case -->
  </div>
</template>
```

### Component Overview - Component Global Registration

전역 등록된 컴포넌트는 Vue 어플리케이션 모든 곳에서 별도 import 없이 사용할 수 있음. 전역 등록은 main.js 파일에서 진행함.

```typescript
// main.js - Component Global Registration
import { createApp } from 'vue'
import App from './App.vue'

import BaseButton from './components/BaseButton.vue'
import BaseInput from './components/BaseInput.vue'

const app = createApp(App)

// app.component()를 사용해 등록: 인자 (<template>에서 호출할 태그 이름, import한 컴포넌트 변수명)
app.component('BaseButton', BaseButton)
app.component('BaseInput', BaseInput)

// 팁: 체이닝(Chaining) 형태로 줄여 쓸 수도 있다
// app.component('BaseButton', BaseButton).component('BaseInput', BaseInput)

app.mount('#app')
```

### Component Overview - Vue 3 내장함수 (4. Vue Component 기준)

이전 챕터와 동일한 내장함수 표이나, 4. Vue Component 단원에서 새로 강조되는 함수들이 추가됨.

이번 단원에서 새로 강조되는 함수: 라이프사이클 훅의 setup, onMounted, onUpdated, onUnmounted, 컴포넌트 구성의 defineProps, defineEmits, 의존성 주입의 provide, inject임.

### Component Lifecycle

컴포넌트가 생성되고 파괴되기까지의 여러 단계를 의미함.

### Component Lifecycle - Lifecycle Hooks

컴포넌트의 생명주기 각 단계에 맞춰 Vue 엔진이 자동으로 실행해 주는 콜백 함수임.

실무에서 핵심적으로 자주 쓰이는 훅은 setup, onMounted, onUpdated, onUnmounted 네 가지임.

→ 제일 많이 쓰는 것이 onMounted, onUnmounted 임

→ 화면에 Component 가 onMounted, onUnmounted 될 때, 데이터를 가져옴

### Lifecycle Hook 예시

```typescript
<!-- Component Lifecycle - Lifecycle Hook Example -->
<script setup>
import { ref, onMounted, onUpdated, onUnmounted } from 'vue'

const count = ref(0)
let timerId = null // 실시간 타이머 메모리 주소를 담을 변수

// 생성 (Creation) 단계 = <script setup> 본문 그 자체
console.log('1. [setup] 컴포넌트가 메모리에 생성되었습니다. (DOM 접근 불가능)')

// 부착 (Mounting) 단계
onMounted(() => {
  console.log('2. [onMounted] 화면에 완벽히 부착되었습니다! (API 호출/DOM 조작 적기)')
// 실무 활용 시뮬레이션: 3초마다 숫자가 자동으로 올라가는 타이머 가동
  timerId = setInterval(() => {
    count.value++
  }, 3000)
})

// 갱신 (Updating) 단계 - count 변수가 바뀌어서 화면이 리렌더링(새로고침)될 때마다 매번 실행됨
onUpdated(() => {
  console.log(`3. [onUpdated] 데이터가 변경되어 화면을 새로 그렸습니다. (현재 count:${count.value})`)
})

// 소멸 (Unmounting) 단계 - v-if="false" 등으로 이 컴포넌트가 화면에서 완전히 파괴되어 사라질 때 실행됨
onUnmounted(() => {
// ❌ 주의: 여기서 타이머를 안 꺼주면 컴포넌트가 사라져도 백그라운드에서 영원히 타이머가 돔 (메모리 누수)
  clearInterval(timerId)
  console.log('4. [onUnmounted] 컴포넌트가 소멸했습니다. 타이머 청소 완료!')
})
</script>
```

### 단계별 실행 순서 요약

setup 본문 → onBeforeMount → onMounted → (데이터 변경 시) onBeforeUpdate → onUpdated → (컴포넌트 제거 시) onBeforeUnmount → onUnmounted

onMounted는 DOM 접근과 API 호출이 가능한 첫 시점이므로 초기 데이터 패칭의 표준 위치로 사용함

onUnmounted에서 clearInterval, 이벤트 리스너 제거 등 정리 작업을 반드시 수행해야 메모리 누수를 막을 수 있음

### Props & Emits

### Component 연동 구조

Vue 3의 모든 컴포넌트 연동은 "데이터는 위에서 아래로 물려주고, 이벤트는 아래에서 위로 쏘아 올린다"는 단방향 흐름 구조를 따름.

Compiler Macro란 Runtime 시점이 아닌 Build 시점에 Vue Compiler가 코드를 변환하는 특수 예약어임. defineProps(), defineEmits(), defineExpose() 같은 함수들은 `<script setup>`에서만 사용 가능함.

### Props & Emits - defineProps()

자식 컴포넌트 내부에서 "부모가 넘겨줄 데이터(속성)의 이름과 규격"을 선언하는 Vue 3 내장 컴파일러 매크로 함수임. `<script setup>` 안에서 import 없이 즉시 호출할 수 있음.

### 정의 형식 비교

```typescript
// defineProps() - 배열 형식 (간단)
const props = defineProps(['title', 'count'])

// defineProps() - 객체 형식 (기본값 지정)
defineProps({
// 1. 타입만 간단히 지정하는 경우
  title: String,

// 2. 필수 값과 기본값까지 꼼꼼하게 지정하는 경우
  likes: {
    type: Number,
    required: true // 부모가 이 값을 안 넘기면 에러발생
  },
  status: {
    type: String,
    default: '대기 중' // 부모가 값을 안 주면 이 값이 기본으로 세팅
  }
})
```

→ 부모로부터 title, count 혹은 title, likes, status 를 받겠다라고 선언하는 것

### template / script 에서 사용하기

```text
<!-- defineProps() - template에서 사용 -->
<template>
  <h1>{{ title }}</h1>      <!-- props 변수명 그대로 사용 -->
  <p>좋아요: {{ likes }}</p>
</template>
```

```typescript
<!-- defineProps() - script setup에서 사용 -->
<script setup>
// 반환값을 변수에 받아서 .점 문법으로 접근해야 함
const props = defineProps({
  title: String,
  likes: Number
})

// 내부 함수에서 쓸 때는 props.을 앞에 꼭 붙여야 함
const checkPopularity = () => {
  if (props.likes > 100) {
    console.log(`${props.title}은 인기 게시글입니다.`)
  }
}
</script>
```

### Readonly 규칙

defineProps로 전달된 값은 읽기 전용임. Child Component에서 직접 수정하려 하면 에러가 발생함.

```typescript
// defineProps() - ReadOnly 주의
const props = defineProps(['likes'])

const brokenFunction = () => {
// ❌ 절대 금지! 콘솔에 ReadOnly 에러 발생
  props.likes = 999
}
```

### 부모 → 자식 데이터 전달 예시

```typescript
<!-- ChildComponent.vue -->
<script setup>
const props = defineProps({
  message: String
})
</script>

<template>
  <div>{{ message }}</div>
</template>
```

```typescript
<!-- ParentComponent.vue -->
<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

const parentMessage = ref('안녕하세요, 자식 컴포넌트!')
</script>

<template>
  <!-- 콜론(:)으로 반응형 데이터를 props로 주입 -->
  <ChildComponent :message="parentMessage" />
</template>
```

### camelCase / kebab-case 네이밍 컨벤션

Component 내부 데이터는 camelCase, 컴포넌트 속성(HTML 태그)은 kebab-case로 작성함. HTML 표준 마크업 언어는 대소문자를 구분하지 못하고 전부 소문자로 인식하기 때문이며, Vue 엔진이 JavaScript의 camelCase를 HTML의 kebab-case로 자동 매핑해 줌.

```typescript
<!-- ParentComponent.vue - camelCase → kebab-case 자동 매핑 -->
<script setup>
import { ref } from 'vue'
import WeatherCard from './components/WeatherCard.vue'

const selectCityName = ref('수원시 영통구')  // 내부 데이터: camelCase
const areaCode = ref(103)
</script>

<template>
  <div>
    <WeatherCard
      :city-name="selectCityName"   <!-- 속성: kebab-case -->
      :area-code="areaCode"
    />
  </div>
</template>
```

```text
<!-- ChildComponent(WeatherCard.vue) - 수신 측: camelCase -->
<script setup>
defineProps({
  cityName: String,   // camelCase로 선언
  areaCode: Number
})
</script>

<template>
  <div class="card">
    <p>지역명: {{ cityName }}</p>
    <p>지역 코드: {{ areaCode }}</p>
  </div>
</template>
```

### Prop Validation (유효성 검사)

부모가 넘긴 데이터에 대한 유효성 검사를 통해 에러 추적의 용이성을 높이고 견고한 컴포넌트를 만들 수 있음.

```text
// defineProps() - Prop Validation 전체 예시
defineProps({
// 1. 가장 기본: 타입(Type)만 단독 검사
  cityName: String,

// 2. 다중 타입 허용: 문자열 혹은 숫자 둘 다 괜찮을 때
  areaId: [String, Number],

// 3. 필수 여부(Required): 부모가 무조건 넘겨야 하는 필수 데이터일 때
  temperature: {
    type: Number,
    required: true  // 안 넘기면 콘솔에 [Vue warn]: Missing required prop 경고가 뜸
  },

// 4. 기본값(Default): 부모가 깜빡하고 안 넘겼을 때 채워줄 디폴트 값
  status: {
    type: String,
    default: '맑음'  // 부모가 값을 생략하면 '맑음'으로 자동 세팅
  },

// 5. 커스텀 유효성 검사기(Validator): 내 입맛대로 세부 조건 필터링
  score: {
    type: Number,
    validator(value) {
      return value >= 0 && value <= 100  // 값이 0부터 100 사이일 때만 합격(true)
    }
  }
})
```

### Vue Props 지원 자료형(Type) 종류

```typescript
// Vue Props 지원 자료형 - 전체 예시
defineProps({
  cityName: String,        // 1. 문자열
  temperature: Number,     // 2. 숫자

  isActive: {              // 3. 논리형
    type: Boolean,
    default: false
  },

  weeklyForecast: {        // 4. 배열
    type: Array,
// 중요: 배열의 기본값은 무조건 '새 바구니를 구워내는 화살표 함수' 형태로!
    default: () => []
  },

  coordinates: {           // 5. 객체
    type: Object,
// 중요: 객체의 기본값도 무조건 화살표 함수 형태로 반환!
    default: () => ({ lat: 37.5, lng: 126.9 })
  }
})
```

### Props & Emits - defineEmits()

자식 컴포넌트에서 부모에게 사용자 정의 이벤트를 전달하기 위해 사용하는 Vue 3 내장 컴파일러 매크로 함수임. `<script setup>` 안에서 import 없이 즉시 호출할 수 있음.

### 핵심 동작 방식

자식 컴포넌트 내부의 브라우저 표준 이벤트(클릭, 키보드 입력 등) 또는 내부 로직 변화를 트리거로 삼아, 부모 컴포넌트가 등록한 Custom Event Listener를 호출하여 콜백 함수를 가동함

데이터 전달(Payload): emit() 함수의 첫 번째 인자로 이벤트 식별 문자열을, 두 번째 인자부터는 부모 컴포넌트의 콜백 함수로 인계할 Payload(데이터)를 Argument로 바인딩하여 전달함

이벤트 타입명은 kebab-case로 작성함

### defineEmits() Example 1 — 기본 사용

```typescript
<!-- ChildComponent.vue - defineEmits 기본 -->
<script setup>
// 발생시킬 이벤트 타입을 배열로 등록
const emit = defineEmits(['childEvent'])

const sendToParent = () => {
// emit('이벤트타입', 보낼데이터)으로 이벤트 발생
  emit('childEvent', '안녕하세요, 부모 컴포넌트!')
}
</script>

<template>
  <button @click="sendToParent">부모에게 메시지 보내기</button>
</template>
```

```typescript
<!-- ParentComponent.vue - 자식 이벤트 수신 -->
<script setup>
import { ref } from 'vue'
import ChildComponent from './ChildComponent.vue'

// @이벤트타입="이벤트핸들러"로 수신
const handleChildEvent = (message) => {
  console.log('자식으로부터 받은 메시지:', message)
}
</script>

<template>
  <ChildComponent @childEvent="handleChildEvent" />
</template>
```

### defineEmits() Example 2 — Props + Emits 통합

```typescript
<!-- WeatherCard.vue (ChildComponent) -->
<script setup>
// 부모에게 물려받을 Props
defineProps({
  cityName: String,
  status: String
})

// 부모에게 전달할 커스텀 이벤트 타입을 배열로 등록
// (관례상 변수명은 'emit'이라고 똑같이 지어줌)
const emit = defineEmits(['select-city'])

// 카드가 클릭되었을 때 실행될 함수
const handleCardClick = (name) => {
// 부모에게 'select-city' 이벤트 발생하면서, 선택된 도시 이름 전달
  emit('select-city', name)
}
</script>

<template>
  <div class="weather-card" @click="handleCardClick(cityName)">
    <h4>{{ cityName }} ({{ status }})</h4>
    <p>클릭하면 부모에게 신호를 보냅니다.</p>
  </div>
</template>
```

```typescript
<!-- ParentComponent.vue -->
<script setup>
import { ref } from 'vue'
import WeatherCard from './components/WeatherCard.vue'

const selectedCityInfo = ref('카드를 클릭해 보세요.')

// 자식이벤트 발생 시 이벤트 핸들러
const receiveCitySignal = (cityName) => {
  selectedCityInfo.value = `${cityName}이(가) 성공적으로 선택되었습니다.`
}
</script>

<template>
  <div class="parent-box">
    <h2>부모 관제탑 (Emits 수신 패널)</h2>
    <!-- @이벤트타입(kebab-case)="핸들러"로 청취 -->
    <WeatherCard cityName="서울" status="맑음" @select-city="receiveCitySignal" />
    <WeatherCard cityName="수원" status="비" @select-city="receiveCitySignal" />
    <div class="status-bar">{{ selectedCityInfo }}</div>
  </div>
</template>
```

### Props & Emits - 통합 예시

Props(하행)와 Emits(상행)이 함께 동작하는 완전한 부모-자식 연동 패턴임.

```typescript
<!-- PropsEmitsParent.vue -->
<script setup>
import { ref } from 'vue'
import PropsEmitsChild from './PropsEmitsChild.vue'

// 1. 상위 컴포넌트의 로컬 반응형 상태 정의
const message = ref('Parent 초기 메시지')

// 2. 하위 컴포넌트의 커스텀 이벤트를 수신했을 때 실행될 핸들러 함수
// 인자(newValue)로 하위 컴포넌트가 보낸 페이로드가 자동 주입됨
const handleUpdateRequest = (newValue) => {
  message.value = newValue
}
</script>

<template>
  <div class="practice-section">
    <h2>Props & Emits</h2>
    <div class="parent-container">
      <h2>상위 컴포넌트 (Parent)</h2>
      <p>현재 로컬 데이터(State): <strong>{{ message }}</strong></p>
      <br />
      <!-- Props: :parent-data로 내려줌 / Emits: @update-request로 청취 -->
      <PropsEmitsChild
        :parent-data="message"
        @update-request="handleUpdateRequest"
      />
    </div>
  </div>
</template>
```

```typescript
<!-- PropsEmitsChild.vue -->
<script setup>
// 1. 상위 컴포넌트로부터 주입받을 데이터의 자료형 및 필수 여부 정의
defineProps({
  parentData: {
    type: String,
    required: true,
  },
})

// 2. 상위 컴포넌트로 송신할 커스텀 이벤트 식별자 등록
const emit = defineEmits(['update-request'])

// 3. 내부 이벤트 발생 시 페이로드를 실어 상위로 이벤트를 디스패치하는 함수
const sendNotification = () => {
  const payload = 'Child에서 가공한 새로운 데이터'
  emit('update-request', payload)
}
</script>

<template>
  <div class="child-container">
    <h2>하위 컴포넌트 (Child)</h2>
    <p>수신된 Props 데이터: <strong>{{ parentData }}</strong></p>
    <br />
    <button @click="sendNotification">상위 컴포넌트로 갱신 요청 (Emit)</button>
  </div>
</template>
```

### Props & Emits 흐름 요약

```text
ParentComponent
  ↓  :parent-data="message"       (Props 하행: 데이터 주입)
ChildComponent
  ↑  emit('update-request', data) (Emits 상행: 이벤트 발사)
ParentComponent
  → handleUpdateRequest(newValue) 실행 → message.value 갱신
```

### Provide & Inject

### 등장 배경 — Props Drilling 문제

컴포넌트 아키텍처의 계층이 깊어질 때(예: 상위 → 하위 → 최하위), 중간에 위치한 컴포넌트들은 해당 데이터가 필요 없음에도 오직 최하위 컴포넌트로 전달하기 위해 Props를 받아 아래로 토스하는 과정을 반복해야 하는 현상을 Props Drilling이라 함.

```text
[Props Drilling 문제]          [Provide & Inject 해결]

<Root>                         <Root> ──── provide('globalTheme')
  └── <Footer>                   └── <Footer>
        └── <DeepChild>                └── <DeepChild> ← inject('globalTheme')
             ↑ Props로 계속 토스           ↑ 중간 계층 건너뛰고 직접 수신
```

중간 계층의 컴포넌트들을 완전히 건너뛰고, 조상 컴포넌트가 선언한 반응형 상태를 하위 컴포넌트에서 inject 함수를 통해 다이렉트로 결합하여 사용하는 방식임

중첩된 컴포넌트 계층에서도 중간 컴포넌트가 해당 값을 몰라도 전달 가능함

[참고] 전역 상태 관리 라이브러리(Pinia)로 인해 Provide & Inject 사용빈도는 높지 않음

### 핵심 코드

```typescript
// GrandParent.vue - provide 측
import { ref, provide } from 'vue'

const themeColor = ref('dark-mode')

// 주입할 키(Key) 이름과 실제 데이터(Value)를 등록
provide('globalTheme', themeColor)
```

```typescript
// GrandChild.vue - inject 측
import { inject } from 'vue'

// 상위 조상이 provide한 키 이름을 지정하여 직접 인젝션 유도
const theme = inject('globalTheme')
```

→ 기본적으로 단방향 — 조상이 provide, 후손이 inject하는 방향만 지원함.

→ 반대 방향(자식 → 부모)은 provide/inject로는 안 되고, 그건 Emits가 담당하는 영역임.

### provide / inject 사용 규칙 요약

### Component Slot

자식 컴포넌트의 특정 구역을 비워두고, 부모 컴포넌트가 자식 컴포넌트를 호출할 때 내장할 HTML 마크업 및 템플릿 콘텐츠를 동적으로 주입받아 렌더링할 수 있도록 해주는 기능임.

Props가 부모가 자식에게 데이터를 주입한다면, Slot은 HTML 마크업 태그나 디자인 레이아웃 자체를 주입함.

### Slot 유형 3가지

Default Slot: 자식 컴포넌트에서 `<slot>` 태그만 사용하여 부모로부터 전달받은 콘텐츠를 표시

Named Slot: 여러 슬롯이 필요한 경우 v-slot:name 또는 #name을 사용해 위치에 지정

Scoped Slot: 자식 컴포넌트에서 부모 컴포넌트로 데이터를 전달할 때 사용 (v-slot 바인딩)

### Component Slot - Default Slot

별다른 속성 없이 단순하게 `<slot>` 태그만 사용하는 슬롯임. 부모로부터 교체할 템플릿 조각이 넘어오지 않으면 `<slot>``</slot>` 내 기본 콘텐츠가 렌더링됨.

```text
<!-- SlotDefaultChild.vue - slot outlet 정의 -->
<template>
  <div class="base-card">
    <slot>
      <p>기본 콘텐츠 영역입니다.</p>  <!-- 부모가 아무것도 안 넣으면 이게 보임 -->
    </slot>
  </div>
</template>
```

```text
<!-- SlotDefaultParent.vue - slot content 주입 -->
<script setup>
import SlotDefaultChild from '@/components/practices/component/SlotDefaultChild.vue'
</script>

<template>
  <div class="practice-section">
    <h2>Default Slot 레이아웃 주입 실습</h2>

    <!-- 1) 텍스트 주입 -->
    <SlotDefaultChild>
      <p>단순한 텍스트 문장을 주입합니다.</p>
    </SlotDefaultChild>

    <!-- 2) 복잡한 마크업 주입 -->
    <SlotDefaultChild>
      <h2 style="color: #e74c3c">🔥 경고 상태</h2>
      <button>확인</button>
    </SlotDefaultChild>

    <!-- 3) 아무것도 안 넣으면 자식의 기본값 렌더링 -->
    <SlotDefaultChild></SlotDefaultChild>
  </div>
</template>
```

최종 렌더링 결과 — 부모가 넣어준 콘텐츠가 `<slot>` 자리를 그대로 대체함.

```text
<!-- 최종 렌더링 결과 -->
<div class="base-card">
  <p>단순한 텍스트 문장을 주입합니다.</p>   <!-- 1번: 부모 콘텐츠 -->
</div>

<div class="base-card">
  <h2 style="color: #e74c3c">🔥 경고 상태</h2>   <!-- 2번: 부모 콘텐츠 -->
  <button>확인</button>
</div>

<div class="base-card">
  <p>기본 콘텐츠 영역입니다.</p>   <!-- 3번: 부모가 아무것도 안 넣어서 자식 기본값 -->
</div>
```

### Component Slot - Named Slot

자식 컴포넌트 내에서 여러 개의 슬롯을 사용할 때 `<slot name="값">` 으로 이름을 지정함. 부모 컴포넌트에서는 `<template v-slot:값>` 또는 축약형 `<template #값>`으로 해당 슬롯에 콘텐츠를 주입함.

```text
<!-- SlotNamedChild.vue - named slot outlet 정의 -->
<template>
  <div class="base-card">
    <header>
      <slot name="header"></slot>   <!-- 이름있는 슬롯 -->
    </header>
    <main>
      <slot></slot>                 <!-- 이름없는 default 슬롯 -->
    </main>
  </div>
</template>
```

```text
<!-- SlotNamedParent.vue - named slot content 주입 -->
<script setup>
import SlotNamedChild from './SlotNamedChild.vue'
</script>

<template>
  <div class="practice-section">
    <h2>Named Slot 주입 실습</h2>
    <SlotNamedChild>
      <!-- v-slot:슬롯이름으로 해당 위치에 주입 -->
      <template v-slot:header>
        <h3>Child 주입 제목</h3>
      </template>

      <!-- template 없이 작성하면 default slot으로 들어감 -->
      <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."</p>
    </SlotNamedChild>
  </div>
</template>
```

최종 렌더링 결과 — 각 v-slot:이름이 대응하는 `<slot name="이름">` 자리를 채움.

```text
<!-- 최종 렌더링 결과 -->
<div class="base-card">
  <header>
    <h3>Child 주입 제목</h3>           <!-- name="header" 슬롯 자리 -->
  </header>
  <main>
    <p>"Lorem ipsum dolor sit amet..."</p>  <!-- default 슬롯 자리 -->
  </main>
</div>
```

### Component Slot - Scoped Slot

자식 컴포넌트에서 부모 컴포넌트로 데이터를 전달할 때 사용함. 일반 Slot과 흐름이 반대로, 자식이 `<slot>` 태그의 속성 바인딩(:이름="변수명")을 통해 데이터를 위로 올려 보내고, 부모는 v-slot="변수주머니이름"으로 수신하여 HTML 코드 안에 배치함.

```typescript
<!-- SlotScopedChild.vue - 자식: 데이터를 slot 속성으로 올려 보냄 -->
<script setup>
import { ref } from 'vue'

// 하위 컴포넌트 내부에서 관리하는 2개의 서버 상태 데이터
const message = ref('현재 서버 상태 정상')
const userCount = ref(150)
</script>

<template>
  <div class="base-card">
    <h3>하위 컴포넌트 (Child)</h3>
    <!-- :text, :count 속성으로 부모에게 데이터를 올려 보냄 -->
    <slot :text="message" :count="userCount">
      <p>부모가 마크업을 주입하지 않았을 때의 디폴트 화면</p>
    </slot>
  </div>
</template>
```

```text
<!-- SlotScopedParent.vue - 부모: v-slot="변수주머니"로 수신 -->
<script setup>
import SlotScopedChild from './SlotScopedChild.vue'
</script>

<template>
  <div class="practice-section">
    <h2>Scoped Slot 주입 실습</h2>
    <h3>상위 컴포넌트 (Parent)</h3>

    <!-- v-slot="slotBag"으로 자식이 올린 데이터를 통째로 수신 -->
    <SlotScopedChild v-slot="slotBag">
      <div class="display-panel">
        <p>알림 메시지: {{ slotBag.text }}</p>
        <p>접속자 수: {{ slotBag.count }}명</p>
      </div>
    </SlotScopedChild>

    <!-- 아무것도 안 넣으면 자식의 기본값 화면 렌더링 -->
    <SlotScopedChild></SlotScopedChild>
  </div>
</template>
```

최종 렌더링 결과 — 자식이 올려 보낸 message, userCount를 부모가 받아서 마크업 안에 배치함.

```text
<!-- 최종 렌더링 결과 -->

<!-- 1번: 부모가 slotBag으로 수신한 데이터를 배치한 경우 -->
<div class="base-card">
  <h3>하위 컴포넌트 (Child)</h3>
  <div class="display-panel">
    <p>알림 메시지: 현재 서버 상태 정상</p>   <!-- slotBag.text -->
    <p>접속자 수: 150명</p>                   <!-- slotBag.count -->
  </div>
</div>

<!-- 2번: 부모가 아무것도 안 넣은 경우 → 자식 기본값 렌더링 -->
<div class="base-card">
  <h3>하위 컴포넌트 (Child)</h3>
  <p>부모가 마크업을 주입하지 않았을 때의 디폴트 화면</p>
</div>
```

### 3가지 Slot 비교 요약

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
