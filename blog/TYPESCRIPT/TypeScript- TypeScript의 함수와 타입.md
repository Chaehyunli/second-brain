---
title: "[TypeScript] TypeScript의 함수와 타입"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-27
source_url: https://ch010104.tistory.com/106
---

# [TypeScript] TypeScript의 함수와 타입

## 원문

https://ch010104.tistory.com/106

## 노트 유형

`guide`

## 적용 목적과 전제조건

https://github.com/Chaehyunli/typescript_study/tree/main/section4

## 구현 절차·검증·주의점

### 1. 기본 함수 타입 정의

1) 자바스크립트 함수 예시

```typescript
function func(a, b) {
  return a + b;
}
```

2) 타입스크립트에서 타입 추가

```typescript
function func(a: number, b: number): number {
  return a + b;
}
```

3) 반환값 타입 생략 가능 (추론)

```typescript
// 함수 타입의 정의

// 함수를 설명하는 가장 좋은 방법
// 어떤 매개변수를 받고, 어떤 결과값을 반환하는지 이야기
// 어떤 [타입의] 매개변수를 받고, 어떤 [타입의] 결과값을 반환하는지 이야기
function func(a: number, b: number) {
  return a + b;
}
```

### 2. 화살표 함수의 타입 정의

```text
// 화살표 함수의 타입을 정의하는 방법
const add = (a: number, b: number) => a + b; // 함수의 반환 결과인 a + b의 타입을 보고 함수 add의 반환 값의 타입을 number로 추론
```

반환 타입은 생략해도 추론됨.

### 3. 매개변수 기본값 설정과 선택적 매개변수

```typescript
// 함수의 매개변수
function introduce(name = "이정환", age: number, tall?: number) { // 매개변수 name을 string | undefined 로 추론, 또한 선택적 매개변수 tall?을 age보다 항상 뒤에 배치해야함.
  console.log(`name : ${name}`);
  // tall 이 여기에서는 number | undefined 이므로 console.log(`tall : ${tall + 10}`); 을 하면 에러가 발생!!
  if (typeof tall === "number") { // 타입 좁히기로 tall을 number로 좁힘
    console.log(`tall : ${tall + 10}`);
  }
}

introduce("이정환", 27, 175);
introduce(undefined, 25); // name을 undefined로 넘겨주면, 기본값으로 설정한 "이정환을 가져감"
introduce("이정환", 27);
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 4. 나머지 매개변수(Rest Parameters)

```typescript
function getSum(...rest: number[]) { // ...rest 인수는 몇 개의 인자가 들어올지 모를 경우, 고정 매개변수 외의 나머지를 배열로 묶어 받기 위해 사용 -> 항상 마지막에 위치해야함
  let sum = 0; // 만약 매개변수의 수를 고정하고 싶을 경우, ...rest: [number, number, number] 로 해야함(매개변수를 3개로 고정).
  rest.forEach((it) => (sum += it)); // it은 rest 배열의 각 요소를 나타냄.(파이썬의 for i in rest: 랑 개념적으로 유사)

  return sum;
}

getSum(1, 2, 3); // 6
getSum(1, 2, 3, 4, 5); // 15
```

### 5. 함수 타입 표현식 (Function Type Expression)

```text
//함수 타입 표현식
type Operation = (a: number, b: number) => number; // type으로 함수의 반환값 타입을 지정할 수 있음 (타입 별칭)

const add: (a: number, b: number) => number = (a, b) => a + b;
const add1: Operation = (a, b) => a + b; // 같은 기능, 타입 별칭이기 때문에, Operation 부분에 (a: number, b: number) => number 를 그대로 넣어도 가능함

const sub: Operation = (a, b) => a - b;
const multiply: Operation = (a, b) => a * b;
const divide: Operation = (a, b) => a / b;
```

### 7. 호출 시그니처 (Call Signature)

하이브리드 타입으로 확장도 가능

```typescript
// 호출 시그니쳐 (콜 시그니쳐)
type Operation2 = { // 함수도 객체임
  (a: number, b: number): number;
  // name: string;
};

const add2: Operation2 = (a, b) => a + b;
const sub2: Operation2 = (a, b) => a - b;
const multiply2: Operation2 = (a, b) => a * b;
const divide2: Operation2 = (a, b) => a / b;

add2(1,2);
// add2.name; // 함수도 객체이기 때문에, 이렇게 점 표기법으로 접근 가능!! 하지만, 아직 함수의 name 속성을 지정해준적이 없기 때문에 결과는 나오지 않음
```

### 8. 함수 타입의 호환성

📌 1) 기준 1: 반환값 타입 호환성

```text
// 함수 타입 호환성
// 특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단하는
// 1. 반환값의 타입이 호환되는가
// 2. 매개변수의 타입이 호환되는가

// 기준1. 반환값이 호환되는가
type A = () => number;
type B = () => 10;

let a: A = () => 10; // number 타입의 함수 a
let b: B = () => 10; // 10 리터럴 타입의 함수 b

a = b; // 업캐스팅!!
// b = a; // 다운캐스팅!! 오류!!
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

📌 2) 기준 2: 매개변수 타입 호환성

1) 매개변수 개수 같을 때

```typescript
// 기준2. 매개변수가 호환되는가
// 2-1. 매개변수의 개수가 같을 때
type C = (value: number) => void;
type D = (value: 10) => void;

let c: C = (value) => {};
let d: D = (value) => {};

// 반환값을 기준으로 호환성을 판단할 때와 다르게, 매개변수를 기준으로 호환성을 판단할 때는 업캐스팅은 허용이 안되고, 다운캐스팅이 허용이 됨.
// c = d; // 업캐스팅!!
d = c; // 다운캐스팅!!
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

2) 매개변수 개수가 다를 때

```typescript
// 2-2. 매개변수의 개수가 다를 때
type Func1 = (a: number, b: number) => void;
type Func2 = (a: number) => void;

let func1: Func1 = (a, b) => {};
let func2: Func2 = (a) => {};

func1 = func2; // 매개변수가 1개인 함수 func2에서 매개변수를 2개인 함수 func1으로으로 취급하는 건 가능!!
// func2 = func1; // 반대의 경우에는 불가능!!
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

3) 객체 타입 예시

```typescript
type Animal = { // 슈퍼 타입
  name: string;
};

type Dog = { // 서프 타입
  name: string;
  color: string;
};

let animalFunc = (animal: Animal) => {
  console.log(animal.name);
};

let dogFunc = (dog: Dog) => {
  console.log(dog.name);
  console.log(dog.color);
};

// animalFunc = dogFunc;  // 업캐스팅!!
dogFunc = animalFunc; // 다운캐시팅!!

let testFunc = (animal: Animal) => {
  console.log(animal.name);
  // console.log(animal.color); // 업캐스팅을 허용할 경우, Animal에서 Dog를 접근하려고 할 수 도 있기 때문에, 매개변수에서는 업캐스팅을 막아놓은 것!!
};

let testFunc2 = (dog: Dog) => {
  console.log(dog.name); // 다 타입이 공통으로 가지고 있는 속성에 대한 접근이기 때문에, 매개변수에서는 다운캐스팅이 허용됨.
};
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 9. 함수 오버로딩

```typescript
// 함수 오버로딩
// 하나의 함수를 매개변수의 개수나 타입에 따라
// 여러가지 버전으로 만드는 문법 -> JS에서는 허용이 안되고, TS에서만 가능

// 하나의 함수 func
// 모든 매개변수의 타입 number
// Ver1. 매개변수가 1개 -> 이 매개변수에 20을 곱한 값 출력
// Ver2. 매개변수가 3개 -> 이 매개변수들을 다 더한 값을 출력

// 버전들 -> 오버로드 시그니쳐 // func 라는 함수의 버전이 이렇게 2가지가 있다고 알려주는 것
function func(a: number): void;
function func(a: number, b: number, c: number): void;

// 실제 구현부 -> 구현 시그니쳐
// fuction func(){} 만 작성해도 func의 함수는 오버로드 시그니쳐 중에서 하나를 찾아서 따라감
function func(a: number, b?: number, c?: number) { // b와 c에서 ?가 없으면 func(a: number) 라는 오버로드 시그니쳐가 의미가 없이지기 때문에 오류 발생!!
    // 모든 오버로드 시그니쳐가 의미가 있도록 매개변수를 설정해준 후, 타입 좁히기를 사용해서 사용해야함
    if (typeof b === "number" && typeof c === "number") {
        console.log(a + b + c);
    } else {
        console.log(a * 20);
    }
}

func(1);
func(1, 2, 3);
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 10. 사용자 정의 타입 가드

```typescript
// 사용자 정의 타입가드
type Dog = {
  name: string;
  isBark: boolean;
};

type Cat = {
  name: string;
  isScratch: boolean;
};

type Animal = Dog | Cat;

function isDog(animal: Animal): animal is Dog { // 함수가 true를 리턴하면 animal 객체가 Dog 타입이다!! 라고 하는 것
  return (animal as Dog).isBark !== undefined; // animal as Dog가 없을 경우에는 타입이 좁혀지지 않은 상태이기 때문에 에러가 남!!
}

function isCat(animal: Animal): animal is Cat {
  return (animal as Cat).isScratch !== undefined;
}

function warning(animal: Animal) {
  if (isDog(animal)) {
    // 강아지
    animal; // animal is Dog에 의해서 animal을 Dog 타입으로 추론함 (저게 없을 경우에는 animal 타입으로 추론함)
  } else if ("isScratch" in animal) {
    // 고양이
    animal; // 위와 같은 방식으로 aniaml is Cat에 의해서 aniaml을 Cat 타입으로 추론함
  }
}
```

### 11. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section4

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript는 집합이다|[TypeScript] TypeScript는 집합이다]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 인터페이스|[TypeScript] TypeScript와 인터페이스]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript의 다양한 타입(기본 타입, 원시 타입, 리터럴 타입 ....)|[TypeScript] TypeScript의 다양한 타입(기본 타입, 원시 타입, 리터럴 타입 ....)]]
