---
title: "[React] state 문법이란?, useEffect 문법이란?"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "JavaScript", "react"]
category: "REACT"
published: 2025-02-19
source_url: https://ch010104.tistory.com/2
---

# [React] state 문법이란?, useEffect 문법이란?

## 원문

https://ch010104.tistory.com/2

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

state는 React에서 컴포넌트의 상태를 관리하는 데 사용되는 개념으로, 특정 값이 변경될 때 자동으로 UI가 다시 렌더링되도록 하는 역할을 한다. 일반 변수를 사용할 경우에는 UI가 state 값이 바뀔 때마다 렌더링하지 않아, 최신 상태를 UI에 반영할 수 없다.

const [count, setCount] = useState(0); 에서 변수 count를 선언하고, 이 변수의 제어를 위해 setCount를 선언함.

## 원문 기반 개념 정리

State 문법

state는 React에서 컴포넌트의 상태를 관리하는 데 사용되는 개념으로, 특정 값이 변경될 때 자동으로 UI가 다시 렌더링되도록 하는 역할을 한다. 일반 변수를 사용할 경우에는 UI가 state 값이 바뀔 때마다 렌더링하지 않아, 최신 상태를 UI에 반영할 수 없다.

state를 사용하지 않은 경우 (비효율적인 방법)

```typescript
let count = 0;

function App() {
  function increase() {
    count += 1;
    console.log(count); // 값은 증가하지만 UI는 업데이트되지 않음
  }

  return (
    <div>
      <h1>현재 카운트: {count}</h1>
      <button onClick={increase}>+1 증가</button>
    </div>
  );
}
```

위 코드에서는 count 값이 증가해도 UI가 변경되지 않음

React에서는 state를 변경해야 UI가 다시 렌더링됨.

state 사용 예제 (useState 훅 사용)

```typescript
import React, { useState } from "react";

function App() {
  // count라는 상태(state)를 선언하고 초기값을 0으로 설정
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>현재 카운트: {count}</h1>
      {/* setCount를 사용해 state 값을 변경하면 자동으로 UI가 업데이트됨 */}
      <button onClick={() => setCount(count + 1)}>+1 증가</button>
      <button onClick={() => setCount(count - 1)}>-1 감소</button>
    </div>
  );
}

export default App;
```

import 문에서 useState 사용을 선언

const [count, setCount] = useState(0); 에서 변수 count를 선언하고, 이 변수의 제어를 위해 setCount를 선언함.

useState(0)은 count 변수의 초기값을 0으로 설정.

<button onClick={() => setCount(count + 1)}>+1 증가</button> setCount(count + 1) 을 사용하여 count 변수에 1을 더함. 이후에 count 변수의 변경을 감지하고, UI를 다시 렌더링

하지만, 이 경우 count의 현재 값을 기준으로 동작하기 때문에, 최신 상태를 기준으로 업데이트 못할 가능이 있다 -> 콜백 함수를 사용하여 처리 가능

setCount에 함수 전달하기(콜백 함수 사용)

```typescript
<button onClick={() => setCount(prev => prev + 1)}>+1 증가</button>
```

React에서는 상태 변경이 비동기적으로 처리되기 때문에, 이전 상태를 기반으로 새로운 상태를 설정하려면 콜백 함수를 사용하는 것이 좋음.

UseEffect 문법

useEffect는 React 컴포넌트가 렌더링될 때 실행되는 함수를 정의하는 훅(Hook) 으로, 컴포넌트가 처음 나타날 때, 사라질 때, 값이 변경될 때 실행되는 코드를 넣을 수 있다.

useEffect(콜백 함수, [의존성 배열])

```typescript
useEffect(() => {

    }, []);
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

콜백 함수: 실행할 코드

의존성 배열: 언제 실행할지 결정하는 값들

```typescript
import React, { useState, useEffect } from "react";

function Example() {
  const [count, setCount] = useState(0);

  // count 값이 변경될 때마다 실행됨
  useEffect(() => {
    console.log(`count가 변경됨: ${count}`);
  }, [count]);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>+1 증가</button>
    </div>
  );
}

export default Example;
```

useEffect(() => { console.log("count 변경됨"); }, [count]);

count 값이 변경될 때마다 실행됨.

버튼 클릭 시 setCount(count + 1)로 상태가 바뀌면, useEffect가 실행됨

[] 위치에 의존성 배열이 없을 경우([count] 가 없으면) 모든 렌더링 마다 실행됨

빈 배열 [] : 최초 1회에 실행됨. (보통 초기 데이터 로딩, API 호출, 이벤트 리스너 등록 등에 사용)

```typescript
useEffect(() => {
  console.log("컴포넌트가 나타남!");

  return () => {
    console.log("컴포넌트가 사라짐!");
  };
}, []);
```

return () => {...} 부분은 컴포넌트가 사라질 때 실행됨

이벤트 리스너 해제, 타이머 제거, 구독 취소 같은 작업에 사용됨

예시

```typescript
useEffect(() => {
    const fetchUserInfo = async () => {
        try {
            const userData = await getUserProfile();
            setUser(userData.data || userData);
        } catch (error) {
            console.error("프로필 정보를 불러오는 데 실패했습니다.", error);
        }
    };

    fetchUserInfo(); // 위에서 선언한 fetchUserInfo 함수를 실행하여 작동
}, []);
```

useEffect(() => {...}, []);

의존성 배열이 [] → 즉, 컴포넌트가 처음 마운트될 때 한 번만 실행됨.

이후 useEffect는 다시 실행되지 않음.

fetchUserInfo 함수

비동기 함수(async)로 선언됨 → 서버에서 데이터를 가져오는 역할

await getUserProfile(); → 비동기 함수 getUserProfile()을 호출하여 사용자 정보를 가져옴.

setUser(userData.data || userData);

가져온 데이터에서 data 속성이 있으면 userData.data를, 없으면 userData 자체를 setUser()로 상태 업데이트.

만약 API 요청이 실패하면 catch 블록에서 오류를 출력함.

fetchUserInfo() 실행

useEffect 내부에서 fetchUserInfo();를 호출하여 비동기적으로 데이터 요청을 실행함.

```typescript
useEffect(async () => { // ❌ 오류 발생
    const userData = await getUserProfile();
    setUser(userData);
}, []);
```

useEffect 내부에서는 직접 async를 사용할 수 없기 때문에, useEffect 안에서 비동기 함수를 따로 선언하고 호출해서 사용.

## 관련 글

- [[blog/REACT/index|REACT]]
- [[blog/REACT/React- param, outlet 문법|[React] param, outlet 문법]]
- [[blog/REACT/React- CLERK을 이용한 토큰 로그인|[React] CLERK을 이용한 토큰 로그인]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
