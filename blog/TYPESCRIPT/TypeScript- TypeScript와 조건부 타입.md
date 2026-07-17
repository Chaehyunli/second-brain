---
title: "[TypeScript] TypeScript와 조건부 타입"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-30
source_url: https://ch010104.tistory.com/111
---

# [TypeScript] TypeScript와 조건부 타입

## 원문

https://ch010104.tistory.com/111

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

제네릭을 사용하면 입력 타입에 따라 결과 타입이 동적으로 바뀌어 재사용성과 안전성이 높아짐

as any를 사용하면 오류는 사라지지만, 타입 안전성이 사라짐

## 원문 기반 개념 정리

### 1. 기본 문법

```text
// 조건부 타입 -> 3항 연산자를 이용하여 조건에 따라 타입을 변경
type A = number extends string ? string : number; // number가 string을 확장하는 타입이냐?? 참이면 A는 string 타입, 거짓이면 number 타입
// -> 거짓이기 때문에 A는 number 타입!
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 2. 객체 타입 비교

```text
type ObjA = { // 슈퍼 타입
  a: number;
};

type ObjB = { // 서브 타입
  a: number;
  b: number;
};

type B = ObjB extends ObjA ? number : string; // 참이기 때문에 B는 number 타입!
```

### 3. 제네릭 조건부 타입

```typescript
// 제네릭과 조건부 타입
type StringNumberSwitch<T> = T extends number ? string : number; // T에 string이 들어오면 조건문이 거짓이 되어 StringNumberSwitch가 number 타입이 됨.
// T에 number이 들어오면 조건문이 거짓이 되어 StringNumberSwitch가 string 타입이 됨.

let varA: StringNumberSwitch<number>; // varA: string

let varB: StringNumberSwitch<string>; // varB: number

function removeSpaces<T>(text: T): T extends string ? string : undefined; // T가 string이면 removeSpaces도 string 타입. 아닐 경우 undefined 타입 -> 오버로드 시그니처

function removeSpaces(text: any) {
  if (typeof text === "string") {
    return text.replaceAll(" ", ""); // " "을 모두 찾아서, ""으로 바꿈
  } else {
    return undefined;
  }
}

let result = removeSpaces("hi im winterlood"); // result: string
result.toUpperCase();

let result2 = removeSpaces(undefined); // result2: undefined
```

제네릭을 사용하면 입력 타입에 따라 결과 타입이 동적으로 바뀌어 재사용성과 안전성이 높아짐

### 4. 조건부 타입 적용 (with 오류 발생)

```typescript
function removeSpaces<T>(text: T): T extends string ? string : undefined {
  if (typeof text === "string") {
    return text.replaceAll(" ", "") as any; // ⛔ 타입 안전성 손상
  } else {
    return undefined as any;
  }
}
```

as any를 사용하면 오류는 사라지지만, 타입 안전성이 사라짐

### 5. 안전한 방법: 함수 오버로딩 사용

```typescript
function removeSpaces<T>(text: T): T extends string ? string : undefined;
function removeSpaces(text: any) {
  if (typeof text === "string") {
    return text.replaceAll(" ", "");
  } else {
    return undefined;
  }
}

let result = removeSpaces("hi im winterlood"); // string
let result2 = removeSpaces(undefined);         // undefined
```

오버로딩을 이용하면 타입 추론도 정확하고 타입 안정성도 유지할 수 있음

### 6. 분산 조건부 타입 (Distributive Conditional Types)

조건부 타입에 유니언 타입을 넣으면 각 타입별로 개별적으로 조건 평가 후 다시 합침

```text
// 분산적인 조건부 타입
type StringNumberSwitch0<T> = T extends number ? string : number;

let a0: StringNumberSwitch0<number>; // a: string
let b0: StringNumberSwitch0<string>; // b: number

let c0: StringNumberSwitch0<number | string>; // c: string | number -> number 만 나와야할 거 같은데?? 왜??
// -> <number | string> 가 동시에 T에 들어가는 것이 아니라, 분산적으로 number랑 string이 따로 들어가서 묶이는 것!
// StringNumberSwitch<number> | StringNumberSwitch<string> -> c0: number 이렇게 작동함!

let d0: StringNumberSwitch0<boolean | number | string>; // d0: string | number
// 1 단계
// StringNumberSwitch<boolean> | StringNumberSwitch<number> | StringNumberSwitch<string>

// 2 단계
// number | string | number

// 결과
// number | string

// 실용적인 예제
type Exclude<T, U> = T extends U ? never : T; // T가 U로 확장된다면 never 아니라면 T 타입

type A = Exclude<number | string | boolean, string>;
// 1 단계
// Exclude<number, string> | Exclude<string, string> | Exclude<boolean, string>

// 2 단계
// number | never | boolean -> never는 공집합과 같은 것이기 때문에 사라짐

// 결과
// number | boolean

type Extract<T, U> = T extends U ? T : never;

type B = Exclude<number | string | boolean, string>; // B = number | boolean

// 분산적인 조건부 타입 사용 안하기
type StringNumberSwitch<T> = [T] extends [number] ? string : number; // 이렇게 할 경우 분산하지 않고 넘겨줌 -> 분산적인 조건부 타입을 막음
let c: StringNumberSwitch<number | string>; // <number | string> 자체를 T로 넘김
// c : number

let d: StringNumberSwitch<boolean | number | string>; // d: number
```

### 7. infer 키워드 사용법

infer는 조건부 타입 안에서 특정 타입을 추론하는 데 사용

```text
// infer
// inference -> 추론하다 -> R을 추론해라
type FuncA = () => string;

type FuncB = () => number;

type ReturnType0<T> = T extends () => string ? string : never; // 함수의 반환값이 string인지만 검사 가능

type A0 = ReturnType0<FuncA>; // A0 = string
// T에 () => string가 들어감 -> 참이므로 string

type B0 = ReturnType0<FuncB>; // B0 = never
// T에 () => number가 들어감 -> 거짓이므로 never

type ReturnType<T> = T extends () => infer R ? R : never; // 함수의 반환값이 string인지 number인지 모두 검사 가능
// T extends () => infer R 가 참이 되는 R 타입을 찾아서 R 타입을 반환

type A = ReturnType<FuncA>; // A = string -> T에 FuncA가 들어감. FuncA 타입이 () => infer R 가 되는 R을 찾아 R 반환

type B = ReturnType<FuncB>; // B = number -> T에 FuncB가 들어감. FuncB 타입이 () => infer R 가 되는 R을 찾아 R 반환

type C = ReturnType<number>; // C = never -> T에 number가 들어감. number 타입이 () => infer R 가 되는 R이 없기 때문에 never 반환
```

### 8. Promise 타입에서 결과 추출하기

```text
// 예제
type PromiseUnpack<T> = T extends Promise<infer R> ? R : never; // T 가 Promise<infer R> 인가? 확인
// 1. T는 프로미스 타입이어야 한다.
// 2. 프로미스 타입의 결과값 타입을 반환해야 한다.

type PromiseA = PromiseUnpack<Promise<number>>; // T에 Promise<number>을 전달
// number

type PromiseB = PromiseUnpack<Promise<string>>; // T에 Promise<string>을 전달
// string
```

### 9. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section9

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작|[TypeScript] TypeScript와 타입 조작]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 유틸리티 타입|[TypeScript] TypeScript와 유틸리티 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
