---
title: "[TypeScript] TypeScript와 타입 조작"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-30
source_url: https://ch010104.tistory.com/110
---

# [TypeScript] TypeScript와 타입 조작

## 원문

https://ch010104.tistory.com/110

## 노트 유형

`guide`

## 적용 목적과 전제조건

Post["author"]는 Post 타입에서 author 프로퍼티의 타입을 추출

keyof typeof person → "name" | "age"

## 구현 절차·검증·주의점

### 1. 인덱스드 엑세스 타입 (Indexed Access Types)

기존 객체, 배열, 튜플에서 특정 타입을 추출할 수 있음

1) 객체 타입에서 추출

```typescript
// 인덱스드 엑세스 타입 -> 객체 타입에서 특정 속성을 뽑아서 변수에 정의할 수 있게 해줌

// 객체에 사용
type Post = {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
};

const post0: Post= {
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "이정환",
    age: 27,
  },
};

function printAuthorInfo0(author: Post["author"]) { // Post에서 author 속성을 뽑아 사용
    // 여기서 "author" 은 값이 아니라 타입임!!! -> Post["author"]["id"] 와 같이도 사용 가능
    // const str = "author";
    // Post[str] - > 에러!! -> author은 string이 아니라 타입이기 떄문
    console.log(`${author.name}-${author.id}`);
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

Post["author"]는 Post 타입에서 author 프로퍼티의 타입을 추출

중첩 사용도 가능

2) 배열 요소 타입 추출

```typescript
// 배열에 사용
type PostList = {
  title: string;
  content: string;
  author: {
    id: number;
    name: string;
    age: number;
  };
}[];

// PostList[number] -> PostList[] 배열 타입으로부터 하나의 요소의 타입만 가져옴
function printAuthorInfo(author: PostList[number]["author"]) { // PostList에서 author 속성을 뽑아 사용 -> PostList의 속성이 변경되어도 자동으로 적용
    console.log(`${author.name}-${author.id}`);
}

const post: PostList[0] = { // PostList[0]을 PostList[number]로 바꾸어도 무관 -> 하지만, 여기서도 number는 타입임
  title: "게시글 제목",
  content: "게시글 본문",
  author: {
    id: 1,
    name: "이정환",
    age: 27,
  },
};

printAuthorInfo(post.author);
```

PostList[number]는 배열의 요소 타입을 의미

3) 튜플 요소 타입 추출

```text
// 튜플에 사용
type Tup = [number, string, boolean];

type Tup0 = Tup[0]; // number 타입

type Tup1 = Tup[1]; // string 타입

type Tup2 = Tup[2]; //boolean 타입

// type Tup3 = Tup[3]; -> index 범위 밖

type TupNum = Tup[number]; // Tup[0], Tup[1], Tup[2] 의 합집합 타입으로 TupNum을 [number, string, boolean] 으로 추론
```

### 2. keyof 연산자

객체 타입의 프로퍼티 key들을 유니온 타입으로 추출

```typescript
// keyof 연산자 -> 객체 타입에 적용하는 연산자
interface Person0 {
    name : string;
    age : number;
}

function getPropertyKey0(person: Person0, key: "name" | "age") { // key: string으로 하면 Person의 속성이 아닌 것에 접급하려하기 때문에 오류!!
  return person[key];
}

const person0:Person0 = {
  name: "이정환",
  age: 27,
};

getPropertyKey0(person0, "name");
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

keyof는 타입에만 사용할 수 있음

1) typeof + keyof 함께 사용

```typescript
const person = {
  name: "이정환",
  age: 27,
};

type Person = typeof person; // 아래의 person 객체에서 타입을 추론해서 Person 타입을 만듬

function getPropertyKey(person: Person, key: keyof typeof person) { // keyof person은 person 객체 타입의 모든 속성을 합집합 형태로 추출 -> "name" | "age" 와 동일
    // keyof 뒤에는 반드시 타입이 와야함. keyof person의 경우처럼 객체가 오면 오류 발생!! -> keyof Person 혹은 keyof typeof person 으로 해야함.
    return person[key];
}

getPropertyKey(person, "name"); // 이정환
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

typeof는 변수의 타입을 추론

keyof typeof person → "name" | "age"

### 3. 맵드 타입 (Mapped Types)

객체의 모든 프로퍼티를 반복하여 새로운 타입을 만들 수 있음

```typescript
// 맵드 타입 -> interface에서는 사용할 수 없고, 타입 별칭에서만 사용 가능!!
interface User {
  id: number;
  name: string;
  age: number;
}

type PartialUser = { // User 타입 중에 모든 속성이 없어도 되는, 일부 속성만 있어도 되는 타입 -> 수정 요청을 보낼 때, 수정하는 속성만 보내기 위함
  [key in "id" | "name" | "age"]?: User[key]; //  [key in "id" | "name" | "age"]? 는 User의 key가 어떤 값인지 정의, User[key] 는 value 값을 정의 -> ? 로 User의 모든 속성이 선택적 속성이 됨
}; // User[key] 는 key의 값이 "id", "name", "age"로 변할 때마다, 각각 number, string, number가 됨

type BooleanUser = {
  [key in keyof User]: boolean;
};

type ReadonlyUser = { // 모든 속성에 readonly 속성을 줌
  readonly [key in keyof User]: User[key];
};

// 한명의 유저 정보를 불러오는 기능
function fetchUser(): ReadonlyUser {
  // ... 기능
  return {
    id: 1,
    name: "이정환",
    age: 27,
  };
}

const user = fetchUser();
// user.id = 1; -> readonly이기 때문에 수정 x -> 에러!!

// 한명의 유저 정보를 수정하는 기능
function updateUser(user: PartialUser) {
  // ... 수정하는 기능
}

updateUser({
  //   id: 1,
  //   name: "이정환",
  age: 25,
});
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

모든 프로퍼티가 선택적(optional) 이 됨

### 4. 템플릿 리터럴 타입 (Template Literal Types)

템플릿 문자열을 사용해 문자열 패턴 기반 타입을 생성

예시

```text
// 템플릿 리터럴 타입
type Color = "red" | "black" | "green";

type Animal = "dog" | "cat" | "chicken";

type ColoredAnimal = `${Color}-${Animal}`; // "red-dog" | "red-cat" | "red-chicken" ... 과 같음
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

Color와 Animal을 조합해 가능한 문자열 리터럴들을 모두 생성

### 5. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section8

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입|[TypeScript] TypeScript와 조건부 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 유틸리티 타입|[TypeScript] TypeScript와 유틸리티 타입]]
