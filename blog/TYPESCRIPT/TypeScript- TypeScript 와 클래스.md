---
title: "[TypeScript] TypeScript 와 클래스"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontedn", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-28
source_url: https://ch010104.tistory.com/108
---

# [TypeScript] TypeScript 와 클래스

## 원문

https://ch010104.tistory.com/108

## 노트 유형

`guide`

## 적용 목적과 전제조건

문제점: 같은 구조의 객체를 반복해서 만들어야 하므로 코드 중복이 발생

타입스크립트에서는 클래스 필드와 메서드에 타입 주석을 추가하여 보다 안전한 객체 생성이 가능

## 구현 절차·검증·주의점

### 🎓 1. 자바스크립트에서의 클래스

1) 객체를 그대로 선언하면?

```text
// 클래스
let studentA = {
  name: "이정환",
  grade: "A+",
  age: 27,
  study() {
    console.log("열심히 공부 함");
  },
  introduce() {
    console.log("안녕하세요!");
  },
};

let studentB = {
  name: "홍길동",
  grade: "A+",
  age: 27,
  study() {
    console.log("열심히 공부 함");
  },
  introduce() {
    console.log("안녕하세요!");
  },
};
```

문제점: 같은 구조의 객체를 반복해서 만들어야 하므로 코드 중복이 발생

2) 클래스 선언하기

```typescript
class Student {
  // 필드
  name;
  grade;
  age;

  // 생성자
  constructor(name, grade, age) {
    this.name = name;
    this.grade = grade;
    this.age = age;
  }

  // 메서드
  study() {
    console.log("열심히 공부 함");
  }

  introduce() {
    console.log(`안녕하세요 ${this.name} 입니다!`);
  }
}

// 상속
class StudentDeveloper extends Student {
  // 필드
  favoriteSkill;

  // 생성자
  constructor(name, grade, age, favoriteSkill) {
    super(name, grade, age);
    this.favoriteSkill = favoriteSkill;
  }

  // 메서드
  programming() {
    console.log(`${this.favoriteSkill}로 프로그래밍 함`);
  }
}

const studentDeveloper = new StudentDeveloper("이정환", "B+", 27, "TypeScript");
console.log(studentDeveloper);
studentDeveloper.programming();
```

3) 객체 생성

```text
// 클래스를 이용해서 만든 객체 -> 인스턴스
// student 인스턴스
let studentB = new Student("홍길동", "A+", 27);
console.log(studentB);
studentB.study();
studentB.introduce();
```

### 🔐 2. 타입스크립트에서의 클래스

타입스크립트에서는 클래스 필드와 메서드에 타입 주석을 추가하여 보다 안전한 객체 생성이 가능

1) 필드 선언 + 초기값

```text
class Employee {
  name: string = "";
  age: number = 0;
  position: string = "";

  work() {
    console.log("일함");
  }
}
```

2) 생성자를 통한 초기화

```typescript
// 타입스크립트의 클래스
const employee = {
  name: "이정환",
  age: 27,
  position: "developer",
  work() {
    console.log("일함");
  },
};

class Employee { // 이렇게 만들어진 클래스는 타입의 역할도 할 수 있음.
  // 필드
  name: string;
  age: number;
  position: string;

  // 생성자 -> 클래스는 가지고 있는 속성에 대해서 생성자가 필요함
  constructor(name: string, age: number, position: string) {
    this.name = name;
    this.age = age;
    this.position = position;
  }

  // 메서드
  work() {
    console.log("일함");
  }
}
```

3) 선택적 프로퍼티

```text
class Employee {
  name: string;
  age: number;
  position?: string;

  constructor(name: string, age: number, position?: string) {
    this.name = name;
    this.age = age;
    this.position = position;
  }

  work() {
    console.log("일함");
  }
}
```

🔍4) 클래스는 타입이다!

```typescript
const employeeC: Employee = { // 클래스 Employee를 객체 타입으로 사용 가능
  name: "",
  age: 0,
  position: "",
  work() {},
};
```

📦 5) 상속 + 생성자에서 super

```typescript
class ExecutiveOfficer extends Employee {
  // 필드
  officeNumber: number;

  // 생성자
  constructor(
    name: string,
    age: number,
    position: string,
    officeNumber: number
  ) {
    super(name, age, position);
    this.officeNumber = officeNumber;
  }
}

const employeeB = new Employee("이정환", 27, "개발자");
console.log(employeeB);
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

🔐 6) 접근 제어자

예시

```typescript
// 접근 제어자 -> ts에서만 제공
// access modifier
// public private proteced
class Employee {
  // 필드
  private name: string;
  protected age: number;
  public position: string;

  // 생성자
  constructor(name: string, age: number, position: string) { // 아무것도 쓰지 않으면 기본적으로 public으로 설정됨
    this.name = name; // class 내에서만 해당 속성에 접근 가능, 외부에서는 접근 자체가 불가!! 쓰기는 물론, 읽기도 제한!!
    this.age = age; // 외부에서는 해당 속성에 접근이 불가능!!,
    this.position = position; // 모든 곳에서 해당 속성에 접근 가능
  }

  // 메서드
  work() {
    console.log(`${this.name} 일함`);
  }
}

class ExecutiveOfficer extends Employee {
  // 필드
  officeNumber: number;

  // 생성자
  constructor(
    name: string,
    age: number,
    position: string,
    officeNumber: number
  ) {
    super(name, age, position);
    this.officeNumber = officeNumber;
  }

  // 메서드
  func() {
    this.age; // 파생 클래스 내부에서는 속성에 접근 가능
    // this.name; // private은 파생 클래스 내부에서도 접근이 불가!!
  }
}

const employee = new Employee("이정환", 27, "developer");
// employee.name = "홍길동"; -> name은 private이기 때문에 외부에서 접근 불가
// employee.age = 30;
employee.position = "디자이너";

console.log(employee);
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

✨ 7) 생성자 매개변수에서 필드 자동 선언

```text
// 접근 제어자 -> ts에서만 제공
// access modifier
// public private proteced
class Employee {
  // 필드

  // 생성자
  constructor( // 아무것도 쓰지 않으면 기본적으로 public으로 설정됨 -> 생성자에서 속성의 타입을 선언하면, 앞의 필드에서는의 내용을 지워야함.
    private name: string, // class 내에서만 해당 속성에 접근 가능, 외부에서는 접근 자체가 불가!! 쓰기는 물론, 읽기도 제한!!
    protected age: number, // 외부에서는 해당 속성에 접근이 불가능!!,
    public position: string, // 모든 곳에서 해당 속성에 접근 가능
  ) {}

  // 메서드
  work() {
    console.log(`${this.age} ${this.name} 일함`); // 클래스 내부에서는 private, protected 모두 접근 가능
  }
}
```

생성자 매개변수에 접근 제어자를 붙이면 필드 선언 + 초기화를 한 줄로 끝낼 수 있어 코드가 훨씬 깔끔해짐

🧩 8) 인터페이스를 구현하는 클래스

```text
// 인터페이스와 클래스
interface CharacterInterface { // 설계도와 유사
  name: string;
  moveSpeed: number;
  move(): void;
}

class Character implements CharacterInterface { // Character 클래스는 CharacterInterface 클래스를 구현한다는 의미
  constructor(
    public name: string, // interface를 통해 받은 속성은 무조건 public 이어야함.
    public moveSpeed: number,
    private extra: string // 추가적인 속성은 이렇게 extra로 추가!! 이 속성에 대해서는 private나 protected가 가능함
  ) {}

  move(): void {
    console.log(`${this.moveSpeed} 속도로 이동!`);
  }
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

implements를 사용하면 인터페이스 구조를 강제할 수 있음

### 3. 깃허브 코드 내용

https://github.com/Chaehyunli/typescript_study/tree/main/section6

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 인터페이스|[TypeScript] TypeScript와 인터페이스]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript의 함수와 타입|[TypeScript] TypeScript의 함수와 타입]]
