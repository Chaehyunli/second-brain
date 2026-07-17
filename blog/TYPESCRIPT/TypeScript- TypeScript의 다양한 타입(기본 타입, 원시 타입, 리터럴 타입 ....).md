---
title: "[TypeScript] TypeScript의 다양한 타입(기본 타입, 원시 타입, 리터럴 타입 ....)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-24
source_url: https://ch010104.tistory.com/104
---

# [TypeScript] TypeScript의 다양한 타입(기본 타입, 원시 타입, 리터럴 타입 ....)

## 원문

https://ch010104.tistory.com/104

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

주의: strictNullChecks: true일 경우 null은 다른 타입에 할당 불가!

https://github.com/Chaehyunli/typescript_study/tree/main/section2

## 원문 기반 학습 정리

### 🛠️ 1. 실습 환경 설정하기

```text
mkdir section2 && cd section2
npm init -y
npm i @types/node
```

1) tsconfig.json 설정:

```text
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "outDir": "dist",
    "strict": true,
    "moduleDetection": "force"
  },
  "ts-node": {
    "esm": true
  },
  "include": ["src"]
}
```

2) 테스트 코드:

```text
// src/index.ts
console.log("Hello New Project");
```

3) 컴파일 후 실행:

```text
tsc
node dist/index.js
```

4) tsx로 직접 실행:

```text
tsx src/index.ts
```

### 🧱 2. 기본 타입 (Primitive Types)

1) number

```text
let num1: number = 123;
let num2: number = -123;
let num3: number = 0.123;
let num4: number = Infinity;
let num5: number = NaN;
```

2) string

```text
let str1: string = "hello";
let str2: string = `template ${str1}`;
```

3) boolean

```text
let bool1: boolean = true;
let bool2: boolean = false;
```

4) null / undefined

```text
let nullVal: null = null;
let undefVal: undefined = undefined;
// null 값이외의 다른 값은 담을 수 없음

// let numA: number = null;
// number 타입 변수에는 원래는 null을 넣을 수 없음
// tsconfig.json에서 "strictNullChecks": false 하면 가능
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

주의: strictNullChecks: true일 경우 null은 다른 타입에 할당 불가!

### 🔠 3. 리터럴 타입 (Literal Types)

```text
// 리터럴 타입 -> 타입스크립트에서만 있는 타입임
let numA: 10 = 10; // 변수의 타입을 그 값(10) 자체로 선언
// numA = 12; 이런 건 불가능하게 됨

let strA: "hello" = "hello";
let boolA: true = true;
```

### 📦 4. 배열 (Array)

1) 기본 선언 방식

```text
// 배열
// 길이와 원소의 타입이 자유
let nums: number[] = [1, 2, 3];
let strs: string[] = ["a", "b", "c"];
```

2) 제네릭 방식

```text
let bools: Array<boolean> = [true, false];  // 이 방식으로도 가능
```

3) 유니온 타입 배열

```text
// 배열에 들어가는 요소들의 타입이 다양한 경우
let mixed: (number | string)[] = [1, "two"];
```

4) 2차원 배열

```text
// 다차원 배열의 타입을 정의하는 방법
let grid: number[][] = [
  [1, 2],
  [3, 4]
];
```

### 📌 5. 튜플 (Tuple)

```text
// 튜플
// 길이와 타입이 고정된 배열
let tup1: [number, string] = [1, "one"];

// tup1 = [1,2,3];
// tup1 = ["1","2"];
// 모두 불가능

let tup2: [number, string, boolean] = [1,"2", true];
// tup2 = ["2",1,true]; 불가능!!

tup1.push(1);
tup1.pop();
tup1.pop();
tup1.pop();
// ts의 튜플을 js로 변환을 하면 튜플을 그냥 배열로 보니 때문에, 배열 메서드로 값을 넣을 수 있음.
// 따라서 튜플에 배열 메서드를 사용하는 경우 조심해야함.

const users : [string, number][] = [
    ["A", 1],
    ["B", 2],
    ["C", 3],
    ["D", 4],
    // [5, "E"], 이와 같은 입력은 튜플을 통해 방지 가능
]
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

튜플도 배열이라서 push 가능하지만 주의

### 🧍 6. 객체 타입 (Object)

1) object 타입 (비추천)

```text
let user: object = { id: 1, name: "홍길동" };
// user.id; // object 타입은 속성으로 무엇이 있는지 알 수 없기에 에러가 발생
```

2) 객체 리터럴 타입 (추천)

```text
let dog: {
  name: string;
  color: string;
} = {
  name: "돌돌이",
  color: "brown",
};

let user2: {
    // 객체 리터럴 타입으로 속성의 타입도 선언해야함.
    id?:number; // 이 속성이 있을수도 있고 없을 수도 있음
    name: string;
} = {
    id: 1,
    name: "임채현",
}

user2.id; // 가능!!

user2 =  {
    name: "홍길동", // id? 이기 때문에 이것도 가능
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### ✅ 7. 선택적(Optional) & 읽기 전용(Readonly) 프로퍼티

```text
let user: {
  id?: number;
  readonly name: string;
} = {
  name: "이정환",
};
user.name = "홍길동"; // ❌ readonly 에러


let config: {
    readonly apiKey: string; // 외부에서 변경하지 못하게 함
} = {
    apiKey: "My API KEY",
}

// config.apiKey = "hacked"; // 변경 불가!!
```

### 🏷 8. 타입 별칭 (Type Alias)

```typescript
type User = {
  id: number;
  name: string;
  nickname: string;
};

let user1: User = {
  id: 1,
  name: "홍길동",
  nickname: "hong"
};

// 타입 별칭
type User = {
    id: number;
    name: string;
    nickname: string;
    birth: string;
    bio: string;
    location: string;
}

let user: User = {
    id:1,
    name: "임채현",
    nickname: "chaehyun",
    birth: "2001/01/04",
    bio: "안녕하세요",
    location: "수원시"
}

let user2: User = {
    id:2,
    name: "홍길동",
    nickname: "chaehyun",
    birth: "2001/01/04",
    bio: "안녕하세요",
    location: "수원시"
}

// 함수 내에서는 User 타입을 아래의 것으로 사용
function func(){
    type User = {

    };
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 🔑 9. 인덱스 시그니처 (Index Signature)

```text
// 인덱스 시그니처
type CountryCodes = {
    //Korea: string;
    //UnitedState: string;
    //UnitedKinfdom: string;
    [key : string] : string; // String : String 인 속성을 모두 허용
}

let codes: CountryCodes = {
  Korea: "ko",
  USA: "us",
  UK: "uk"
};

type CountryNumberCodes = {
    //Korea: string;
    //UnitedState: string;
    //UnitedKinfdom: string;
    [key: string]: number; // 빈 속성도 허용
    // 하지만 Korea라는 속성은 무조건 있어야 해!! 라고 하면 이렇게 지정
    Korea: number; // 이 속성의 타입은 위의 number와 일치시켜줘야 함.
};

let countryNumberCodes: CountryNumberCodes = {
   Korea: 410 , // Korea: number; 이기 때문에 이 줄이 없으면 에러 발생!!!
};
```

### 📋 10. 열거형 타입 (Enum)

1) 숫자형 Enum

```typescript
// 열거형 타입(enum 타입)
// 여러가지 값들에 각각 이름을 부여해 열거해주고 사용하는 타입
// enum은 컴파일 결과 js로 바뀌어도 사라지지 않음(자바크립트의 객체로 변환  됨)

enum Role {
  ADMIN,
  USER,
  GUEST,
}

const user1  = {
    nmae : "임채현",
    role : Role.ADMIN, // 0 <- 관리자
    language: Language.Korean, // 문자형 enum
};

const user2  = {
    nmae : "아무개",
    role : Role.GUEST // 1 <- 일반 회원
};

const user3  = {
    nmae : "홍길동",
    role : Role.USER // 2 <- 게스트
};

console.log(user1, user2, user3);
// { nmae: '임채현', role: 0, language: 'ko' } { nmae: '아무개', role: 2 } { nmae: '홍길동', role: 1 }
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

2) 문자열 Enum

```typescript
enum Language {
  Korean = "ko",
  English = "en"
}

const setting = {
  lang: Language.Korean // "ko"
};
```

### 🧨 11. any 타입 (비추천)

```typescript
// any
// 특정 변수의 타입을 확실히 모를 때

let anyVar: any = 10; // js처럼 어떤 타입이든 저장할 수 있게 함
anyVar = "hello"; // string
anyVar = true; // boolean
anyVar = {}; // 객체
anyVar = () => {}; // 함수

// anyVar.toUpperCase();
// 사용 가능. 하지만 js처럼 runtime에서는 에러가 발생함

let num: number = 10;
num = anyVar; // 모든 타입의 변수에 any 타입의 변수를 넣을 수도 있음.
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 🔍 12. unknown 타입

```typescript
// unknown
let unknownVar: unknown;

unknownVar = ""; // 이 부분은 any와 동일
unknownVar = 1;
unknownVar = () => {};

// num = unknownVar; // 모든 타입의 변수에 unknown 타입의 변수를 넣을 수 없음
// unknownVar.toUpperCase() // 불가

// 이런 식으로만 가능
if (typeof unknownVar === "number") {
  num = unknownVar;
}

// 그래서 일반적으로 특저 변수이 타입을 확실히 모를 때는 any보단 unkown이 더 안전함.
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 🙅‍♀️ 13. void 타입

```typescript
// void 타입
// void -> 공허 -> 아무것도 없다.
// void -> 아무것도 없음을 의미하는 타입

function func1(): string{
    return "hello";
}

function func2(): void{
    console.log("hello");
}

let a: void;
// void 타입의 변수에는 undefined만 담을 수 있음.
// 하지만, tsconfig.ts에서 "strictNullChecks": false 로 하면 가능
// a= 1;     에러!
// a "hello" 에러!
// a ={}     에러!
a = undefined
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 🚫 14. never 타입

```typescript
// never 타입
// never -> 존재하지 않은
// 불가능한타입

// 이 경우와 같이, 이 함수에 반환값이 있을 수가 없다. 있는 것이 모순이다!! never 사용!!
function func3(): never{
    while(true){

    }
}

function func4(): never {
  throw new Error();
}

let anyVar: any;

let b: never;
// never 타입에서는 어느 타입의 변수도 담을 수 없음!!
// "strictNullChecks": false 로 해도 불가능!!

// b = 1;           에러!
// b = {};          에러!
// b = "";          에러!
// b = undefined;   에러!
// b = null;        에러!
// b = anyVar;      에러!
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 13. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section2

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript란-- + 컴파일러 옵션 설정하기|[TypeScript] TypeScript란?? + 컴파일러 옵션 설정하기]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript는 집합이다|[TypeScript] TypeScript는 집합이다]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript의 함수와 타입|[TypeScript] TypeScript의 함수와 타입]]
