---
title: "[TypeScript] TypeScript와 인터페이스"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-27
source_url: https://ch010104.tistory.com/107
---

# [TypeScript] TypeScript와 인터페이스

## 원문

https://ch010104.tistory.com/107

## 노트 유형

`guide`

## 적용 목적과 전제조건

Person 인터페이스는 name, age 프로퍼티를 갖는 객체의 구조를 정의

호출 시그니처 방식은 오버로딩이 가능하지만, 함수 타입 표현식은 불가능

## 구현 절차·검증·주의점

### 📌1. 인터페이스 기본 사용법

```typescript
// 인터페이스 -> 상호 간에 약속된 규칙!!
// Type 설저과 비슷함
interface Person {
  readonly name: string;
  age?: number;
  sayHi(): void; // 호출 시그니처를 사용!!
  sayHi(a: number, b: number): void;
}

const person: Person = {
  name: "이정환",
  sayHi: function (a?:number, b?:number) { // 이것도 호출 시그니처를 이용하여 가능
    if(typeof a == "number" && typeof b == "number"){
        console.log(a + b );
    }else{
        console.log("Hi");
    }
  },
};
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

Person 인터페이스는 name, age 프로퍼티를 갖는 객체의 구조를 정의

타입 별칭(type)과 유사하지만 문법이 다름

### 2. 메서드 정의 방식

1) 함수 타입 표현식

```typescript
interface Person {
  sayHi: () => void;
}
```

2) 호출 시그니처

```text
interface Person {
  sayHi(): void;
}
```

호출 시그니처 방식은 오버로딩이 가능하지만, 함수 타입 표현식은 불가능

### 3. 메서드 오버로딩 (Method Overloading)

```text
// 인터페이스 -> 상호 간에 약속된 규칙!!
// Type 설저과 비슷함
interface Person {
  readonly name: string;
  age?: number;
  sayHi(): void; // 호출 시그니처를 사용!!
  sayHi(a: number, b: number): void;
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

동일한 함수 이름에 대해 다양한 파라미터 형태를 정의할 수 있음!

### 🌀 4. 하이브리드 타입 (Hybrid Type)

```typescript
interface Func2 {
  (a: number): string;
  b: boolean;
}

const func: Func2 = (a) => "hello";
func.b = true;
```

함수이자 속성을 가진 객체도 정의 가능

### ⚠ 5. 인터페이스의 한계점

인터페이스는 Union, Intersection 타입을 직접 표현할 수 없음.

```text
type Type1 = number | string; // ✅
type Type2 = number & string; // ✅

interface Person {
  name: string;
} | number // ❌ 오류
```

이런 경우 타입 별칭과 함께 사용해야 함.

```text
type Type1 = number | string | Person; // 이런식으로 합집합과 교집합에도 사용 가능
type Type2 = number & string & Person;
```

### 🔗 6. 인터페이스 확장 (extends)

중복되는 구조를 줄이기 위해 인터페이스를 상속할 수 있음

```typescript
// 인터페이스의 확장
type Animal = {
  name: string;
  color: string;
};

interface Dog extends Animal { // name, color 속성을 Animal에서 가져옴 -> 공통된 것을 따로 모야 빼는 것과 유사
    // name: "hello"; -> Interface로 name: string으로 하였지만, 이와 같이 Dog에서 hello string 리터럴 타입으로 다시 선언도 가능
    // 아무 타입으로나 다시 선언 가능한 것이 아니라, 다시 선언하는 타입이 이전 타입의 서브 타입이어야만 가능!!(name: number의 경우에는 허용 x)
    isBark: boolean;
}

const dog: Dog = {
    name: "", // Dog에서 hello string 리터럴 타입으로 다시 선언할 경우에는 여기에서 에러가 발생함!!
    color: "",
    isBark: true,
};
```

### 🔧 7. 프로퍼티 재정의

```typescript
// 인터페이스의 확장
type Animal = {
  name: string;
  color: string;
};

interface Dog extends Animal { // name, color 속성을 Animal에서 가져옴 -> 공통된 것을 따로 모야 빼는 것과 유사
    name: "hello"; -> Interface로 name: string으로 하였지만, 이와 같이 Dog에서 hello string 리터럴 타입으로 다시 선언도 가능
    // 아무 타입으로나 다시 선언 가능한 것이 아니라, 다시 선언하는 타입이 이전 타입의 서브 타입이어야만 가능!!(name: number의 경우에는 허용 x)
    isBark: boolean;
}

const dog: Dog = {
    // name: "", // Dog에서 hello string 리터럴 타입으로 다시 선언할 경우에는 여기에서 에러가 발생함!!
    color: "",
    isBark: true,
};
```

단, 기존 타입이 새로운 타입의 슈퍼타입이어야만 재정의가 가능!!

예: string → "hello" string 리터럴 타입은 가능하지만, string → number는 ❌

### 🧩 8. 타입 별칭 확장과 다중확장

```typescript
interface Cat extends Animal {
    isScratch: boolean;
}

interface Chicken extends Animal {
    isFly: boolean;
}

interface DogCat extends Dog, Cat {} // 이와 같이 2개의 interface를 확장 받을 수도 있음

const dogCat: DogCat = {
    name: "",
    color: "",
    isBark: true,
    isScratch: true,
};
```

타입 별칭으로 정의된 객체도 interface에서 extends로 확장할 수 있음.

### 📚 9. 선언 합침 (Declaration Merging)

인터페이스는 같은 이름으로 여러 번 선언하면 자동으로 합쳐짐

```typescript
// 선언 합침 -> 타입 별칭과 다르게 동일한 이름으로 선언된 인터페이스들 사이에 에러가 나지 않음
// 동일한 이름의 인터페이스들은 합쳐짐!!
// 하지만, 같은 속성에 대해서 타입이 충돌 나는 경우에는 에러!!
interface Person {
  name: string;
}

interface Person {
  name: string; // 만약에 nameL number를 하면 이전의 선언과 충돌이 발생해서 에러가 발생!!
  age: number;
}

interface Developer extends Person {
  name: "hello";
}

const person: Person = {
  name: "",
  age: 27,
};

// 모듈 보강 -> 보통 선언 합침은 이러한 모듈을 보강하는 역할로 사용함.
interface Lib {
  a: number;
  b: number;
}

interface Lib {
  c: string;
}

const lib: Lib = {
  a: 1,
  b: 2,
  c: "hello",
};
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

하지만 동일한 프로퍼티의 타입이 다르면 충돌이 발생

### 10. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section5

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript의 함수와 타입|[TypeScript] TypeScript의 함수와 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript는 집합이다|[TypeScript] TypeScript는 집합이다]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
