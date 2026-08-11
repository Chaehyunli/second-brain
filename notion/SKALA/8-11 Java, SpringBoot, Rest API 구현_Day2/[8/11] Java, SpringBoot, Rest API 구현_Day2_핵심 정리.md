---
title: "[8/11] Java, SpringBoot, Rest API 구현_Day2_핵심 정리"
notion_page_id: "3b91d84b-f68e-80c1-9653-d2884a4ea98d"
source_url: "https://app.notion.com/p/3b91d84bf68e80c19653d2884a4ea98d"
synced_at: "2026-08-12T00:08:11+09:00"
content_sha256: "b764663fdc589e53124ba6d7b6a09ff814cbe97f7e2d73f9fe2de16bc4b2aea7"
tags: [notion, skala, learning, java, spring-boot, rest-api]
---

# [8/11] Java, SpringBoot, Rest API 구현_Day2_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b91d84bf68e80c19653d2884a4ea98d) (2026-08-12 확인)

### JVM 구조
JVM(Java Virtual Machine)은 자바 소스 파일(.java)이 컴파일러(javac)를 거쳐 바이트코드(.class)로 변환된 후, ClassLoader를 통해 JVM 내부로 로드되어 실행되는 가상 머신임.

JVM 내부는 크게 공유 영역(Shared Area)과 스레드별 영역(Per Thread)으로 구분됨.
공유 영역에는 다음 세 구역이 존재함.
- Heap: 객체 인스턴스가 저장되는 공간. Young Generation(Eden, S0, S1)과 Old Generation(Tenured)으로 구성됨.
- Method Area: 클래스 메타데이터와 상수 풀(Runtime Constant Pool)이 저장됨.
- Code Cache: JIT 컴파일된 네이티브 코드가 저장됨.
스레드별 영역에는 각 Thread마다 독립적인 Stack(메서드 호출 및 지역변수 관리), PC Register, Native Method Stack이 존재함.
실행 엔진(Execution Engine)은 공유되며 Interpreter, JIT Compiler, Garbage Collector로 구성됨. JNI(Native Method Interface)를 통해 네이티브 코드와 연계됨.
GC 발생 시 모든 JVM 내 Thread가 중단되는 STW(Stop the World) 현상이 발생하여 성능 저하 및 처리 중단이 생김. JDK 15부터는 Z GC, 메모리 최적화, 동시 병렬처리(Thread 미 중단) 등을 활용해 이 문제를 최적화함.
---
### 자바와 JVM — 클래스 로더 & Metaspace
클래스 로더는 .class 파일을 로드하고 jar 파일 내 저장된 클래스를 JVM의 Metaspace(Heap 외부)에 탑재하는 역할을 담당함.
Metaspace는 Method Area의 구현체로, 다음 정보를 저장함.
- 클래스 메타데이터: 이름, 접근 제어자, 부모 클래스 이름, 인터페이스 이름 등 메타 정보
- 메서드 메타데이터: 이름, 반환 타입, 파라미터 타입, Bytecode
- 어노테이션 정보 및 필드/메서드의 구조적 레이아웃 정보
참고로 static variable과 constant는 Heap의 java.lang.Class 객체로 관리됨.
실행 엔진(Execution Engine)은 인터프리터와 JIT(Just In Time) 컴파일러, 그리고 가비지 컬렉터 기능을 포함함.
RunTime Data Area는 프로그램 수행을 위해 OS에서 할당받은 메모리 공간으로, 다음과 같이 구성됨.
- Method Area, Heap: 모든 스레드가 공유
- Java Stack, PC Register, Native Method Stack: 스레드별로 독립 존재
---
### \[참고\] JVM RunTime Data Area 상세
각 영역의 역할은 다음과 같음.
Method Area
- 클래스 수준 정보 저장소
- 클래스 메타데이터(클래스 이름, 필드, 메서드 시그니처)와 메서드 바이트코드를 보관함
Heap
- 객체(Object) 인스턴스 저장소
- new로 생성된 모든 객체 및 배열이 저장되며, 대부분의 메모리 사용량을 차지함
Stack
- 메서드 실행 단위 저장소
- 스레드별로 하나씩 존재하며, 메서드 호출 시마다 Stack Frame이 생성됨
PC Register(Program Counter)
- 현재 실행 중인 바이트코드의 위치(여러 명령줄의 index)를 기록함
- 각 스레드마다 독립적으로 존재하며 다음에 실행할 명령 주소를 가리킴
- 예시: `a = b + c;` 연산은 바이트코드 수준에서 `iload_2(b)`, `iload_3(c)`, `iadd`, `istore_1(a=결과)` 4개의 명령으로 순차 실행됨
Native Method Stack
- JNI 기반 네이티브 코드 실행용으로, C/C++로 작성된 메서드 호출 시 사용됨
- Java Stack과 유사한 구조를 가짐
---
### Heap 영역
Java 애플리케이션에서 생성된 객체와 배열이 저장되는 런타임 메모리 공간으로, Garbage Collector에 의해 관리되며 JVM 성능에 직접적인 영향을 미침.
JVM Heap은 다음 영역으로 구분됨.

| 영역 | 설명 | 특징 | GC 영향 |
| --- | --- | --- | --- |
| Eden | 새 객체가 생성되는 공간 | 대부분의 객체가 짧게 존재 | Minor GC 대상 |
| Survivor S0/S1 | Eden에서 살아남은 객체가 이동 | GC 후 번갈아 복사 | Minor GC 대상 |
| Old | 생존 시간이 긴 객체 저장 | 대형 객체, 오랜 객체 | Full GC 대상 |
| Metaspace | Method Area의 구현체 | Native 메모리 사용 | GC 미 대상 |
---
### 가비지 컬렉션 (Garbage Collection)
자바의 메모리 관리 방법 중 하나로, JVM Heap 영역에서 동적으로 할당했던 메모리 중 더 이상 필요 없게 된 메모리 객체(garbage)를 모아 주기적으로 제거하는 프로세스임.
Minor GC
- Young Generation 영역에서 발생하는 GC
- Young Generation은 Old 대비 객체 정보가 작기 때문에 객체를 찾아 제거하는 데 적은 시간이 소요됨
Major GC(Full GC)
- Old 영역에서 발생하는 GC
- Old 영역의 객체들은 Young Generation에서 살아남은 것들로, 대상 객체가 크고 많아 실행 속도가 느림
- 느린 이유: 여러 곳 참조, 참조구조 복잡, 여러 메모리에 분산된 접근, 객체 크기 증가
---
### \[참고\] 메모리 Stack vs Heap
메서드 내부의 변수가 어떤 메모리 영역에 저장되는지 시각적으로 이해할 수 있는 예시임.
```java
public void Method1() {
    int a = 10;         // Stack에 a=10 저장
    int b = 20;         // Stack에 b=20 저장
    class1 obj = new class1();  // Stack에 obj 참조값 저장, 실제 객체는 Heap에 저장
}
```
- 기본형(int, long 등) 지역변수는 Stack에 직접 값으로 저장됨
- 참조형(class, array 등) 변수는 Stack에 참조(reference)만 저장되고, 실제 인스턴스는 Heap에 위치함
---
### 상속 (Inheritance)
기존 클래스(부모 클래스, Superclass)의 상태(State)와 행위(Behavior)를 자식 클래스(Subclass)가 물려받아 재사용하고 확장할 수 있도록 하는 기법임. 기능을 물려받는 쪽을 자식 클래스, 물려주는 쪽을 부모 클래스라고 함.
하나의 Base Class를 여러 Child Class가 상속하는 구조로, Child class 1, 2, n처럼 여러 자식이 동일한 부모를 상속할 수 있음.
---
### 접근 제한자 (Access Modifiers)
클래스 내 멤버(Field, Method)는 접근 제한자에 따라 상속 여부가 결정됨.
| 접근 제한자 | 같은 패키지에서 접근 | 다른 패키지에서 접근 | 상속받은 자식 클래스에서 접근 가능 여부 |
| --- | --- | --- | --- |
| public | O | O | O |
| protected | O | O (상속받은 경우만) | O |
| (default) | O | X | X |
| private | X | X | X |
각 제한자의 특성은 다음과 같음.
- public: 어디서든 접근 가능. 자식 클래스에서도 사용 가능.
- protected: 같은 패키지에서는 자유롭게 접근 가능하며, 다른 패키지에서도 상속받은 경우 접근 가능.
- (default, 패키지 접근제한자): 같은 패키지에서는 접근 가능하지만, 다른 패키지에서는 접근 불가.
- private: 오직 해당 클래스 내부에서만 접근 가능. 자식 클래스에서도 직접 접근 불가.
---
### 접근 제한자 코드 예시
```java
// 부모 클래스
class Parent {
    public String publicField = "Public Field";
    protected String protectedField = "Protected Field";
    private String privateField = "Private Field";

    public void publicMethod() { System.out.println("Public Method"); }
    protected void protectedMethod() { System.out.println("Protected Method"); }
    private void privateMethod() { System.out.println("Private Method"); }
}

// 자식 클래스
class Child extends Parent {
    void accessParentMembers() {
// public 멤버 접근 가능
        System.out.println(publicField);
        publicMethod();

// protected 멤버 접근 가능
        System.out.println(protectedField);
        protectedMethod();

// private 멤버 접근 불가 (컴파일 오류 발생)
// System.out.println(privateField);  // 오류!
// privateMethod();                   // 오류!
    }
}
```
---
### 인터페이스의 구조
인터페이스는 클래스가 구현해야 하는 메서드의 규약(계약, contract)을 정의하는 참조 타입임. 메서드 시그니처(이름, 매개변수, 반환형)만 선언하고 실제 구현은 인터페이스를 구현한 클래스가 담당함.
```java
public interface Animal {
    void makeSound();
}
```
- class 키워드 대신 interface 키워드를 사용함
- 메서드의 정의만 해두고 구현체는 존재하지 않음
메서드 시그니처는 메서드 이름 + 파라미터 타입 목록으로 구성되며, 구체적으로는 메서드 이름, 파라미터의 개수, 파라미터의 순서, 파라미터의 타입을 포함함.
---
### 인터페이스 구현
```java
// 인터페이스 선언
interface Animal {
    void makeSound();
}

// 구현 클래스
public class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("멍멍!");
    }
}

public class Cat implements Animal {
    @Override
    public void makeSound() {
        System.out.println("야옹!");
    }
}

// Main 함수
public class AnimalSound {
    public static void main(String[] args) {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.makeSound(); // 출력: 멍멍!
        cat.makeSound(); // 출력: 야옹!

        handleAnimalSound(cat); // 메서드로 전달
    }

    static void handleAnimalSound(Animal animal) {
        animal.makeSound();
    }
}
```
- 구현 클래스는 implements 키워드를 사용하여 인터페이스를 구현함
- 변수 타입을 인터페이스(Animal)로 선언하면, 실제 구현 클래스(Dog, Cat)와 무관하게 동일한 방식으로 메서드를 호출할 수 있음(다형성)
---
### @Override Annotation 사용 이유
@Override는 필수가 아니지만 다음 세 가지 이유로 사용이 권고됨.
1. 컴파일러 체크 기능
	- 부모 클래스(또는 인터페이스)의 메서드를 정확하게 재정의했는지 컴파일러가 검사함
	- 오타가 있거나 부모 클래스에서 메서드가 삭제되었을 경우, 컴파일 오류가 발생하여 실수를 방지함
2. 가독성 향상
	- @Override가 있으면 "이 메서드는 부모의 메서드를 재정의한 것이다"라는 정보를 명확하게 전달할 수 있어 코드 가독성이 높아짐
3. 리팩토링 안정성
	- 부모 클래스의 메서드 시그니처가 변경될 경우, @Override가 없으면 오류가 발생하지 않아 실행 시 문제가 생길 수 있음
	- @Override가 있으면 컴파일러가 문제를 감지하고 수정하도록 지원함
---
### 인터페이스 메서드 접근 제어자
인터페이스의 메서드는 기본적으로 public이지만, Java 9부터 다른 접근 제어자도 지원함.
```java
interface Animal {
    void eat(); // public abstract 메서드 (기본값)

// Java 9부터 가능한 private 메서드
    private void helperMethod() {
        System.out.println("This is a private method");
    }

// default 메서드에서 private 메서드 호출 가능
    default void sleep() {
        helperMethod();
        System.out.println("Sleeping...");
    }
}

// static 메서드 예시
interface MathUtil {
    static int square(int x) {
        return x * x;
    }
}

int twoSquare = MathUtil.square(2); // 객체 생성 없이 인터페이스 이름으로 직접 호출
```
라이브러리나 API 인터페이스에 새로운 메서드를 추가하면 기존 모든 구현 클래스에서 컴파일 에러가 발생하여 하위 호환성이 깨짐. 이를 해결하기 위해 default 메서드 구현을 제공하거나, 중복되는 내부 로직 재사용을 위한 private 메서드를 추가함(외부 구현 클래스에서는 호출 불가).
static 메서드는 클래스처럼 인터페이스도 자기 자신만의 유틸리티 메서드를 지원할 수 있게 해주며, 객체 생성 없이 인터페이스 명으로 직접 호출 가능함(예: `Collections.sort(list)`).
---
### 다중 상속
자바는 클래스의 다중 상속을 지원하지 않으며, 대신 인터페이스를 활용하여 다중 상속 효과를 구현함.
클래스 다중 상속이 불가능한 이유는 동일한 시그니처의 메서드를 가진 두 부모 클래스를 동시에 상속하면 어느 쪽의 구현을 사용할지 알 수 없는 다이아몬드 문제(Diamond Problem)가 발생하기 때문임.
```java
// 다중 상속 지원 시 문제 예시 (자바에서는 컴파일 오류)
class C extends A, B { }
C printWhat = new C();
c.print() // A? B? → 모호함

// 인터페이스를 통한 다중 상속 해결
interface Flyable { void fly(); }
interface Swimmable { void swim(); }

abstract class Bird {
    public void moving() { System.out.println("움직입니다!"); }
    public void fly();
}

// 하나의 클래스가 두 인터페이스를 모두 구현
class Duck extends Bird implements Flyable, Swimmable {
    @Override
    public void fly() { System.out.println("오리가 하늘을 납니다!"); }

    @Override
    public void swim() { System.out.println("오리가 물 위를 헤엄칩니다!"); }
}

Duck duck = new Duck();
duck.fly();
duck.swim();
duck.moving();
```
인터페이스는 구현체가 없는 메서드 시그니처만 정의하므로 어느 쪽을 선택할지 모호함이 없고, 구현 클래스에서 반드시 직접 구현하도록 강제함. 이로써 다중 상속의 이점(다양한 타입 역할 수행)을 안전하게 활용할 수 있음.
---
### 추상 클래스 (Abstract Class)
추상 클래스는 Concrete Class(일반 클래스)와 Interface의 중간 형태로, 다음과 같은 특성을 가짐.
- 최소 하나의 추상 메서드를 포함하면 추상 클래스이며, 직접 객체화(인스턴스 생성) 불가
- 공통 기능은 추상 클래스 내에서 직접 구현하고, 클래스별 개별 기능은 하위 클래스에서 구현하도록 강제함
```java
// 일반 부모 클래스
class Human {
    public String name;

    Human(String name) {
        this.name = name;
    }
}

// 추상 클래스 (Human을 상속)
abstract class Programmer extends Human {
    void introduce() {
        System.out.println("my name is " + this.name); // 공통 기능 직접 구현
    }

    abstract void writeCode(); // 하위 클래스에서 반드시 구현해야 하는 추상 메서드
}
```
---
### 추상 클래스 예시
```java
// 추상 클래스 정의
abstract class Animal {
    String name;

    public Animal(String name) {
        this.name = name;
    }

// 하위 클래스에서 반드시 구현해야 함
    abstract void makeSound();

// 공통 기능 — 모든 하위 클래스가 그대로 사용 가능
    public void sleep() {
        System.out.println(name + " is sleeping...");
    }
}

// 구현 클래스 Cat
class Cat extends Animal {
    public Cat(String name) {
        super(name); // 부모 생성자 호출
    }

    @Override
    void makeSound() {
        System.out.println(name + " says: Meow~");
    }
}

// 구현 클래스 Dog
class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    void makeSound() {
        System.out.println(name + " says: Woof!");
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        Animal dog = new Dog("Buddy");
        Animal cat = new Cat("Kitty");

        dog.makeSound(); // Buddy says: Woof!
        cat.makeSound(); // Kitty says: Meow~

        dog.sleep();     // Buddy is sleeping...
        cat.sleep();     // Kitty is sleeping...
    }
}
```
- 변수 타입을 추상 클래스(Animal)로 선언하여 다형성을 활용함
- sleep()은 공통 구현이므로 추상 클래스에서 제공하고, makeSound()는 클래스마다 다른 동작이므로 추상 메서드로 강제함
---
### 다형성 (Polymorphism)
하나의 타입(클래스 또는 인터페이스)으로 여러 형태의 객체를 다룰 수 있는 능력임. 동일한 메서드 호출이 실행 시점에 실제 객체 타입에 따라 다르게 동작함.
오버라이딩과 오버로딩이 다형성을 구현하는 두 가지 핵심 방법임.
오버라이딩 (Overriding) — "기존의 것을 덮어쓰다"
- 부모 클래스의 메서드를 자식 클래스가 동일한 시그니처로 다시 구현하는 행위
- 활 시위 하나를 당기면 화살 하나가 날아가듯, 메서드 호출은 하나지만 실제 동작은 객체 타입에 따라 달라짐
오버로딩 (Overloading) — "over(초과하여) + load(짐을 싣다)"
- 입력 파라미터가 다른 경우에 동일한 이름으로 메서드를 여러 개 만들 수 있음
- 파라미터를 다르게 정의하고 리턴값도 다르게 적용 가능
- 단, 리턴값만 다르게 설정하는 것은 불가. Method Signature 구조는 리턴을 관리하지 않기 때문에 리턴만 다른 경우 Conflict가 발생함
---
### 메서드 오버라이딩(Overriding) 예시
```java
// 부모 클래스
class Human {
    String name;

    public Human(String name) {
        this.name = name;
    }

    void introduce() {
        System.out.println("저의 이름은 " + name + "입니다.");
    }
}

// 자식 클래스 — introduce() 오버라이딩
class Student extends Human {
    String studentId;

    public Student(String name, String studentId) {
        super(name); // 부모 생성자 호출
        this.studentId = studentId;
    }

    @Override
    void introduce() {
        System.out.println("저의 이름은 " + name + "이고, 학생 ID는 " + studentId + "입니다.");
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        Human person  = new Human("홍길동");
        Student student = new Student("김철수", "S12345");

        person.introduce();  // 저의 이름은 홍길동입니다.
        student.introduce(); // 저의 이름은 김철수이고, 학생 ID는 S12345입니다.
    }
}
```
- super(name)으로 부모 생성자를 호출하여 부모 필드를 초기화한 뒤, 자식 고유 필드(studentId)를 추가로 초기화함
- @Override로 introduce()를 재정의하면 같은 메서드 호출이라도 실제 객체 타입에 따라 다른 출력이 나옴
---
### 메서드 오버로딩(Overloading) 예시
```java
class HighSchoolStudent extends Student {
    String highSchool;
    String subject;

    public HighSchoolStudent(String name, String studentId,
                             String highSchool, String subject) {
        super(name, studentId); // Student 생성자 호출
        this.highSchool = highSchool;
        this.subject = subject;
    }

    @Override
    void introduce() {
        System.out.println("저의 이름은 " + name + "이고, 학생 ID는 "
            + studentId + "입니다. 고등학교는 " + highSchool + "입니다.");
    }

// introduce 메서드 오버로딩 — 파라미터가 다른 동명 메서드
    void introduce(String message) {
        introduce(); // 위의 introduce() 호출
        System.out.println("제 전공은 " + subject + "입니다. 나는 " + message + "을 추가하고 싶습니다");
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        HighSchoolStudent highStudent = new HighSchoolStudent(
            "John", "S9876", "DEF 고등학교", "수학");

        highStudent.introduce("안녕하세요"); // 파라미터 있는 버전 호출
        highStudent.introduce();            // 파라미터 없는 버전 호출
    }
}
```
- 같은 이름 introduce()를 파라미터 유무로 구분해 두 개 정의함. 이것이 오버로딩임
- 오버로딩은 컴파일 시점에 어떤 메서드를 호출할지 파라미터 타입/개수로 결정됨(정적 바인딩)
- 반면 오버라이딩은 실행 시점에 실제 객체 타입으로 결정됨(동적 바인딩)
---
### 컬렉션의 종류 (Collection Type)
Java에서 데이터의 집합을 다루기 위한 표준화된 인터페이스와 클래스들의 집합으로, 데이터를 저장·검색·수정·삭제하는 공통 동작을 제공함.
| 유형 | 목적 | 주요 특징 | 대표 용도 |
| --- | --- | --- | --- |
| List | 순서가 있는 요소 집합 저장 | 중복 허용, 인덱스 접근, 순서 유지 | 이름 목록, 순차 처리 데이터 |
| Set | 중복 없는 요소 집합 저장 | 중복 불허 | 회원 ID, 태그 목록 |
| Map | 키-값 쌍 저장 | 키 중복 불허, 값 중복 가능, 키로 빠른 검색 | 사용자 정보(아이디 → 사용자 객체) |
| Queue | FIFO 방식의 요소 처리 | 먼저 들어온 것이 먼저 나감 | 프린터 작업 큐, 이벤트 처리 |
| Stack | LIFO 방식의 요소 처리 | 나중에 들어온 데이터가 먼저 나감 | 되돌리기(Undo), 재귀 호출, 브라우저 뒤로 가기 |
---
### 컬렉션 클래스 계층 구조
Collection 인터페이스는 Iterable을 상속하며, 그 하위에 List, Queue, Set 인터페이스가 존재함. Map은 Collection 계층과 별도로 독립적인 계층을 이룸.

주요 구현체는 다음과 같음.
- List 계열: ArrayList, LinkedList, Vector → Vector의 하위에 Stack이 존재
- Queue 계열: PriorityQueue, Deque(ArrayDeque)
- Set 계열: HashSet, LinkedHashSet, SortedSet → TreeSet
- Map 계열: HashMap, LinkedHashMap, Hashtable, SortedMap → TreeMap
LinkedList는 List와 Deque를 동시에 구현하여 두 계층에 모두 속함.
---
### 리스트 (List)
순서가 있는 데이터를 저장하는 것을 목적으로 하며, 순차적인 데이터 관리와 인덱스로의 접근 기능을 제공함. 구현체로는 ArrayList, Vector(thread-safe), LinkedList 등이 있음.
```java
// List<String> list = new Vector<>(); 또는 new LinkedList<>() 도 가능
List<String> list = new ArrayList<>();

list.add("A");
list.add("B");
list.add("C");
list.add("A"); // 중복 허용

// forEach 문으로 순회
for (String item : list) {
    System.out.println(item);
}

// for 문으로 인덱스 접근
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}

// Iterator 사용
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```
---
### List 주요 메서드
| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| add(E e) | 요소 추가 | list.add("A") |
| add(int index, E e) | 특정 위치에 요소 추가 | list.add(1, "B") |
| get(int index) | 인덱스 위치의 요소 반환 | list.get(0) |
| set(int index, E e) | 인덱스 위치의 요소 변경 | list.set(0, "Z") |
| remove(int index) | 인덱스 위치 요소 제거 | list.remove(1) |
| remove(Object o) | 특정 요소 제거 | list.remove("A") |
| size() | 요소 개수 반환 | list.size() |
| contains(Object o) | 요소 존재 여부 확인 | list.contains("B") |
| isEmpty() | 비어있는지 확인 | list.isEmpty() |
| clear() | 모든 요소 삭제 | list.clear() |
---
### \[참고\] Collection 구현체 타입
대부분의 Collection 구현체는 3가지 유형의 확장으로 만들어짐.

LinkedList 구조
- 각 노드가 실제 데이터(item), 다음 노드 주소(next), 이전 노드 주소(prev)를 함께 보관하는 이중 연결 리스트 구조임
- 노드를 포인터로 연결하기 때문에 삽입/삭제 시 앞뒤 포인터만 변경하면 되어 O(1)로 빠르지만, 특정 인덱스 조회 시 처음부터 순회해야 하여 O(n)으로 느림
ArrayList 구조
- 내부적으로 배열을 사용하며, 현재 크기(Current Size)와 배열 용량(Current Capacity)이 별도로 관리됨
- 용량이 초과되면 더 큰 배열로 자동 복사(resize)함. 인덱스로 바로 접근 가능하여 조회가 O(1)로 빠름
Vector 구조
- ArrayList와 구조는 동일하나, add() 메서드에 synchronized 키워드가 붙어 멀티스레드 환경에서 동기화를 지원함
- 동기화 비용이 있어 단일 스레드 환경에서는 ArrayList보다 느림
---
### \[참고\] 리스트 구현체 비교
| 비교 항목 | ArrayList | LinkedList | Vector |
| --- | --- | --- | --- |
| 구조 | 동적 배열 | 이중 연결 리스트 | 동적 배열 (동기화 지원) |
| 조회 속도 | O(1) 빠름 | O(n) 느림 | O(1) 빠름 |
| 삽입/삭제 속도 | O(n) 느림 | O(1) 빠름 | O(n) 느림 |
| 동기화 | 미지원 | 미지원 | 지원 |
| 멀티스레드 환경 | 비추천 | 비추천 | 추천 |
| 메모리 사용량 | 적음 | 많음 (노드 참조 필요) | 적음 |
| 적합한 경우 | 조회가 빈번한 경우 | 삽입/삭제가 빈번한 경우 | 멀티스레드 환경 |
---
### List 활용하기 — 주요 메서드 사례
```java
package skalajava;

import java.util.ArrayList;
import java.util.List;

public class ListExample {
    public static void main(String[] args) {
// 1. 리스트 생성
        List<String> fruits = new ArrayList<>();

// 2. 요소 추가: add()
        fruits.add(e:"사과");
        fruits.add(e:"바나나");
        fruits.add(e:"체리");

// 3. 리스트의 크기 출력: size()
        System.out.println("과일의 개수: " + fruits.size()); // 과일의 개수: 3

// 4. 특정 요소에 접근: get()
        System.out.println("첫 번째 과일: " + fruits.get(index:0)); // 첫 번째 과일: 사과

// 5. 요소 수정: set()
        fruits.set(index:1, element:"오렌지");
        System.out.println("수정된 리스트: " + fruits); // [사과, 오렌지, 체리]

// 6. 요소 삭제: remove()
        fruits.remove(o:"체리");
        System.out.println("삭제된 리스트: " + fruits); // [사과, 오렌지]

// 7. 모든 요소 반복: forEach()
        fruits.forEach(System.out::println); // 사과 / 오렌지

// 8. 리스트가 비어있는지 확인: isEmpty()
        System.out.println("리스트가 비었나요? " + fruits.isEmpty()); // false

// 9. 모든 요소 삭제: clear()
        fruits.clear();
        System.out.println("모든 과일 삭제 후 리스트: " + fruits); // []

// 10. 요소 다시 추가
        fruits.add(e:"망고");
        fruits.add(e:"키위");
        System.out.println("다시 추가된 리스트: " + fruits); // [망고, 키위]
    }
}
```
- forEach()는 람다 또는 메서드 참조(System.out::println)와 함께 간결하게 사용 가능함
- remove(Object o)는 값으로 요소를 찾아 삭제하고, remove(int index)는 인덱스로 삭제함. 같은 이름의 오버로딩 메서드임
---
### 셋 (Set)
중복이 허용되지 않는 데이터를 관리하는 컬렉션임. 구현체로는 HashSet, LinkedHashSet, TreeSet 등이 있음.
```java
// Set<String> set = new LinkedHashSet<>(); 또는 new TreeSet<>() 도 가능
Set<String> set = new HashSet<>();

set.add("A");
set.add("B");
set.add("C");
set.add("A"); // 중복 무시 — 실제로는 A, B, C 세 개만 저장됨

// forEach 순회
for (String item : set) {
    System.out.println(item);
}

// Iterator 사용
Iterator<String> iterator = set.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```
---
### Set 주요 메서드
| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| add(E e) | 요소 추가 (중복 허용 안됨) | set.add("A") |
| remove(Object o) | 요소 제거 | set.remove("A") |
| contains(Object o) | 요소 존재 여부 확인 | set.contains("B") |
| size() | 요소 개수 반환 | set.size() |
| isEmpty() | 비어있는지 확인 | set.isEmpty() |
| clear() | 모든 요소 삭제 | set.clear() |
| iterator() | Iterator 반환 | set.iterator() |
---
### Set 구현체 비교

| 구현체 | 중복 허용 | 순서 유지 | 정렬 지원 | 적합한 경우 |
| --- | --- | --- | --- | --- |
| HashSet | X | X | X | 빠른 검색/삽입/삭제가 필요할 때 |
| LinkedHashSet | X | O (삽입 순서 유지) | X | 순서를 유지하면서 빠른 성능이 필요할 때 |
| TreeSet | X | O (정렬된 순서 유지) | O (오름차순/사용자 정의) | 정렬된 집합이 필요할 때 |
내부 구조 관점에서 보면, HashSet은 키 값을 해시 함수로 변환하여 배열 인덱스에 매핑하고 충돌 시 LinkedList로 연결하는 해시 테이블 구조를 사용함. TreeSet은 이진 탐색 트리(Red-Black Tree) 구조로 요소를 정렬된 상태로 유지함.
---
### Map
키(Key)와 값(Value) 쌍을 저장하는 데이터 구조임. 구현체로는 HashMap, LinkedHashMap, TreeMap 등이 있으며 주요 메서드로는 put(), get(), entrySet(), keySet(), values(), containsKey() 등이 있음.
```java
// HashMap 생성 (키: String, 값: String)
Map<String, String> map = new HashMap<>();

// 데이터 추가
map.put("1", "A");
map.put("2", "B");
map.put("3", "C");
map.put("4", "A"); // 값 중복 가능 (Key만 유일하면 됨)

// 1. forEach 문 (Key, Value 동시 사용)
for (Map.Entry<String, String> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " : " + entry.getValue());
}

// 2. KeySet 이용 (Key로 값 조회)
for (String key : map.keySet()) {
    System.out.println(key + " : " + map.get(key));
}

// 3. Iterator 사용
Iterator<Map.Entry<String, String>> iterator = map.entrySet().iterator();
while (iterator.hasNext()) {
    Map.Entry<String, String> entry = iterator.next();
    System.out.println(entry.getKey() + " : " + entry.getValue());
}
```
Map 순회 방법은 세 가지임.
- entrySet() + forEach: Key와 Value를 Map.Entry 객체로 동시에 접근하는 가장 일반적인 방법
- keySet() + get(): Key 집합을 먼저 꺼낸 뒤 get()으로 Value를 조회하는 방법. entrySet()보다 get() 호출이 추가되어 상대적으로 비효율적임
- Iterator: entrySet()에서 Iterator를 꺼내어 순회하는 방법. 순회 중 remove()가 필요한 경우에 유용함
---
### Map 주요 메서드
| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| put(K key, V value) | 키-값 쌍 추가/변경 | map.put("1", "A") |
| get(Object key) | 키에 해당하는 값 반환 | map.get("1") |
| remove(Object key) | 키로 엔트리 제거 | map.remove("1") |
| containsKey(Object key) | 특정 키 존재 여부 | map.containsKey("1") |
| containsValue(Object value) | 특정 값 존재 여부 | map.containsValue("A") |
| size() | 엔트리 수 반환 | map.size() |
| isEmpty() | 비어있는지 확인 | map.isEmpty() |
| clear() | 모든 엔트리 삭제 | map.clear() |
| keySet() | 키 집합 반환 | map.keySet() |
| values() | 값 컬렉션 반환 | map.values() |
| entrySet() | 키-값 엔트리 집합 반환 | map.entrySet() |
---
### Map 구현체 비교
| 구현체 | 내부 구조 | 순서 유지 | 목적 | 비고 |
| --- | --- | --- | --- | --- |
| HashMap | 해시 테이블 (체이닝 + JDK8부터 버킷 트리화) | X | 빠른 검색/삽입/삭제 | 메모리 효율 좋고 전반적으로 가장 빠름 |
| LinkedHashMap | HashMap + 이중 연결 리스트 | O (기본: 삽입 순서, 옵션: 접근 순서) | 순서를 보장하면서 빠른 성능 지원 | 순서 유지 비용 약간 증가 |
| TreeMap | Red-Black Tree (균형 이진 탐색 트리) | O (정렬된 순서) | 정렬이 필요할 때 | 정렬/범위 질의에 유리 |
선택 기준 요약.
- 빠른 검색/삽입/삭제가 필요하다면 → HashMap
- 순서를 유지하면서도 빠른 성능을 원한다면 → LinkedHashMap
- 정렬이 필요하다면 → TreeMap
---
### 큐 (Queue)
데이터의 in-out을 FIFO(First In First Out) 방식으로 관리하는 컬렉션임. 구현체로는 ArrayDeque(속도 가장 빠름), LinkedList(검색 기능), PriorityQueue 등이 있음.
```java
Queue<String> queue = new LinkedList<>();

queue.offer("A");
queue.offer("B");
queue.offer("C");
queue.offer("A"); // 중복 허용

// forEach 순회 (제거 없이 읽기만 함)
for (String item : queue) {
    System.out.println(item);
}

// poll() 사용 — FIFO 순서로 꺼내기 (꺼내면 제거됨)
while (!queue.isEmpty()) {
    System.out.println(queue.poll()); // A → B → C → A 순서
}

// Iterator 사용
Iterator<String> it = queue.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```
---
### Queue 주요 메서드
| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| offer(E e) | 요소 추가 (실패 시 false 반환) | queue.offer("A") |
| add(E e) | 요소 추가 (실패 시 IllegalStateException) | queue.add("B") |
| poll() | 첫 요소 제거 후 반환 (없으면 null) | queue.poll() |
| remove() | 첫 요소 제거 후 반환 (없으면 예외) | queue.remove() |
| peek() | 첫 요소 조회 (없으면 null) | queue.peek() |
| element() | 첫 요소 조회 (없으면 예외) | queue.element() |
| size() | 요소 개수 반환 | queue.size() |
| isEmpty() | 비어있는지 확인 | queue.isEmpty() |
| clear() | 모든 요소 삭제 | queue.clear() |
offer/poll은 실패 시 예외 대신 false/null을 반환하므로 일반적으로 add/remove보다 안전함.
---
### 큐 (Queue) 구현체 비교

| 구현체 | 인터페이스 | 내부 구조 | 스레드 안전 | 주요 특징 |
| --- | --- | --- | --- | --- |
| LinkedList | Queue, Deque | 이중 연결 리스트 | X | 가장 단순한 큐, 학습/간단한 큐 |
| ArrayDeque | Queue, Deque | 원형 배열 | X | 가장 빠른 일반 큐/스택, LinkedList 대체 권장 |
| PriorityQueue | Queue | 힙(Heap) | X | 우선순위 큐 (정렬 기준 처리) |
| ConcurrentLinkedQueue | Queue | Lock-free 링크 구조 | O | 고성능 비차단 큐 (멀티스레드) |
| ConcurrentLinkedDeque | Deque | Lock-free | O | 멀티스레드 Deque |
ArrayDeque는 Queue와 Deque 인터페이스를 모두 구현하여, FIFO 큐와 양방향 큐 양쪽으로 사용 가능함. LinkedList는 중간 삽입/삭제가 빠르지만, ArrayDeque는 접근 속도 및 탐색이 더 빠름.
---
### Deque (Double-Ended Queue)
양쪽에서 넣고 양쪽에서 빼는 자료구조임. Queue는 한쪽 끝(Rear)에서만 삽입하고 반대쪽(Front)에서만 꺼내지만, Deque는 양쪽 모두에서 삽입/삭제가 가능함.
```java
// Queue로 사용 (FIFO)
Queue<Integer> q = new ArrayDeque<>();
q.offer(1);
q.offer(2);
q.offer(3);
System.out.println(q.poll()); // 1
System.out.println(q.poll()); // 2

// Deque로 사용 (양방향)
Deque<Integer> d = new ArrayDeque<>();
d.offerLast(1);   // 뒤에 삽입
d.offerLast(2);   // 뒤에 삽입
d.offerFirst(0);  // 앞에 삽입 → [0, 1, 2]

System.out.println(d.pollFirst()); // 0
System.out.println(d.pollLast());  // 2
```
Deque의 주요 메서드는 방향(First/Last)을 접미사로 구분함. offerFirst/offerLast로 삽입하고 pollFirst/pollLast로 꺼냄.
---
### 스택 (Stack)
데이터의 in-out을 LIFO(Last In First Out) 방식으로 관리하는 컬렉션임. ArrayDeque(속도가 가장 빠름)와 Stack(Thread-safe이지만 성능 느림) 등이 있음.
```java
Stack<String> stack = new Stack<>();

stack.push("A");
stack.push("B");
stack.push("C");
stack.push("A");

// forEach 순회
for (String item : stack) {
    System.out.println(item);
}

// pop() 사용 — LIFO 순서로 꺼내기
while (!stack.isEmpty()) {
    System.out.println(stack.pop()); // A → C → B → A 순서
}

// Iterator 사용
Iterator<String> it = stack.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```
---
### Stack 주요 메서드
| 메서드 | 설명 | 예시 |
| --- | --- | --- |
| push(E e) | 스택에 요소 삽입 | stack.push("A") |
| pop() | 맨 위 요소 제거 후 반환 | stack.pop() |
| peek() | 맨 위 요소 조회 (제거 없음) | stack.peek() |
| search(Object o) | 요소 위치 반환 (1부터 시작) | stack.search("A") |
| empty() | 비어있는지 확인 | stack.empty() |
| size() | 요소 개수 반환 | stack.size() |
| clear() | 모든 요소 삭제 | stack.clear() |
---
### Collection\<E\>
Java Collection에서 제공하는 최상위 인터페이스이며, List, Set, Queue 등 자료구조들의 공통 메서드 집합체임.
```java
public interface Collection<E> extends Iterable<ED> { ... }
public interface List<E> extends Collection<E> { ... }
```
Collection\<E\>가 제공하는 두 가지 핵심 역할은 다음과 같음.
공통 메서드 표준화
- List, Set, Queue는 내부 동작 방식이 달라도, 요소 추가(add), 삭제(remove), 포함 여부 확인(contains) 같은 공통 기능은 모두 Collection에 정의되어 있음
다형성 제공
- 코드 작성 시 특정 구현체(ArrayList, HashSet 등)가 아닌 Collection\<E\> 타입으로 변수를 선언하면 자료구조를 교체하기 쉬워짐
---
### Collection 주요 메서드
| 메서드 | 설명 |
| --- | --- |
| add(E e) | 요소 추가 |
| addAll(Collection\<? extends E\> c) | 다른 컬렉션의 모든 요소 추가 |
| remove(Object o) | 요소 제거 |
| removeAll(Collection\<?\> c) | 특정 컬렉션의 모든 요소 제거 |
| clear() | 모든 요소 삭제 |
| contains(Object o) | 포함 여부 확인 |
| isEmpty() | 비어있는지 여부 |
| size() | 요소 개수 |
| iterator() | 순회용 Iterator 반환 |
---
### Collection\<E\> 사용 방법
Collection 타입으로 변수를 선언하는 것이 유리한 세 가지 상황임.
```java
// 1. 자료구조 종류에 상관없이 공통된 처리만 할 때
//    → 파라미터 타입을 Collection으로 받으면 List, Set, Queue 모두 전달 가능
public void printAll(Collection<String> collection) {
    for (String item : collection) {
        System.out.println(item);
    }
}

// 2. 구현체를 유연하게 교체할 필요가 있을 때
//    → 선언 타입이 Collection이면 구현체를 바꿔도 사용 코드 변경 불필요
Collection<String> names = new ArrayList<>(); // 처음에는 ArrayList
names.add("Alice");
names.add("Bob");
names = new HashSet<>(names); // 나중에 HashSet으로 변경

// 3. 공통 메서드만 필요할 때
Collection<Integer> numbers = new LinkedList<>();
numbers.add(1);
numbers.add(2);
System.out.println(numbers.contains(2)); // true
numbers.remove(1);
```
---
### 제네릭 (Generic) 이란?
타입별로 중복 코드를 작성하는 것을 막아서 코드 재사용성을 높이기 위한 방식임. 클래스나 메서드에서 사용할 데이터 타입을 컴파일 시점에 결정함.
```java
// 제네릭 클래스 정의
class Box<T> {
    private T item;

    public void set(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }
}

// 사용 — 구체적인 타입으로 지정
public class Main {
    public static void main(String[] args) {
        Box<String> stringBox = new Box<>();
        stringBox.set("Hello");
        System.out.println(stringBox.get()); // Hello

        Box<Integer> integerBox = new Box<>();
        integerBox.set(100);
        System.out.println(integerBox.get()); // 100
    }
}
```
T는 타입 매개변수(Type Parameter)이며, 사용할 때 구체적인 타입으로 지정함. 컴파일 후에는 타입 정보가 소거(Type Erasure)되어 내부적으로 캐스팅 코드(`(String) stringBox.get()`)로 변환됨.
---
### 관용적인 제네릭 타입 매개변수
제네릭 타입 매개변수의 이름은 꼭 T일 필요는 없으나 관례적으로 T를 많이 사용함. 가독성과 의미 전달을 위해 다음 약어들을 권고함.
| 타입 매개변수 | 의미 | 사용 예시 |
| --- | --- | --- |
| T | Type (일반적인 타입) | class Box\<T\> |
| E | Element (컬렉션 요소용) | List\<E\> |
| K | Key (Map의 키) | Map\<K, V\> |
| V | Value (Map의 값) | Map\<K, V\> |
| R | Return Type (반환 타입) | Converter\<T, R\> |
| ? | 와일드 카드 (불특정 타입) | List\<?\> |
```java
// K, V 두 개의 타입 매개변수를 사용하는 Pair 클래스 예시
class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}

// 사용
Pair<String, Integer> stockPair = new Pair<>("SKALA-AI", 10000);
System.out.println("종목: " + stockPair.getKey() + ", 가격: " + stockPair.getValue());
```
---
### 제네릭 타입의 제한
상속 관계가 있는 클래스들 사이에서 타입 안정성을 유지하면서 코드의 범용성을 높이는 데 필수적인 도구임.
상한 제한 (Upper Bound — extends)
```java
// T extends Number: T가 Number 또는 그 하위 클래스(Integer, Double, Float 등)만 허용
class NumberBox<T extends Number> {
    private T value;

    public void printDouble() {
        System.out.println(value.doubleValue()); // Number의 메서드 사용 가능
    }

    public void setValue(T value) {
        this.value = value;
    }
}

NumberBox<Integer> intBox = new NumberBox<>();
intBox.setValue(100);
intBox.printDouble(); // 100.0
```
하한 제한 (Lower Bound — super)
```java
// <? super Integer>: Integer의 상위 타입만 허용 → [Integer, Number, Object]
public static void addIntegers(List<? super Integer> list) {
    list.add(1);
    list.add(2);
// list.get()은 Object로만 얻을 수 있음 (하한이므로 타입 정보가 모호)
}
```
- `<? extends Number>` → Number, Integer, Double 허용 (읽기 전용에 유리)
- `<? super Integer>` → Integer, Number, Object 허용 (쓰기에 유리)
- 하한 제한은 제네릭 클래스 정의에는 사용하지 않고, 메서드 매개변수나 와일드카드에서만 사용함
---
### 제네릭 와일드카드 : \<? extends T\> (1/2)
T 타입 또는 T의 하위(자식) 타입이라면 무엇이든 사용 가능하다는 의미로, 상한 와일드카드(Upper Bounded Wildcard)라고 함. 이미 요소가 채워진 리스트를 받아서 읽기 전용으로 사용하기 위한 타입임.
List\<T\>를 사용하는 경우의 문제와 와일드카드 해결책 비교.
```java
// List<T> 사용 — 에러 발생
// List<Fruit> 자리에 List<Apple>을 넣을 수 없음 (제네릭은 공변이 아님)
public void printFruit(List<Fruit> fruits) { ... }
List<Apple> apples = new ArrayList<>();
printFruit(apples); // 컴파일 오류!

// <? extends Fruit> 와일드카드 사용 — 해결
public void printFruit(List<? extends Fruit> fruits) {
    for (Fruit f : fruits) {
        System.out.println(f.getName()); // 읽기는 OK
    }
}

List<Apple> apples = new ArrayList<>();
apples.add(new Apple());
printFruit(apples); // 에러 없이 컴파일 및 실행 성공

List<Banana> bananas = new ArrayList<>();
bananas.add(new Banana());
printFruit(bananas); // 바나나 리스트도 똑같은 메서드로 처리
```
get할 때와 add할 때의 동작 차이.
- get: 어떤 구체 타입인지 몰라도 최소한 Number(또는 T)라는 건 확실하므로 리턴 타입을 T로 받는 것은 안전함
- add: 컴파일러 입장에서 실제 타입이 List\<Integer\>, List\<Double\>, List\<BigDecimal\>일 수 있으므로 add는 컴파일 오류 발생
```java
void printNumbers(List<? extends Number> nums) {
    for (Number n : nums) {
        System.out.println(n); // 읽기는 OK
    }
// nums.add(10); // 불가 — 쓰기 금지
}
```
---
### 제네릭 와일드카드 : \<? super T\>
T 타입 이상의 상위 타입을 받도록 하여 리스트에 값을 넣기(write) 위한 타입임.
```java
// <? super Integer>: Integer의 상위 타입 중 하나
List<? super Integer> list;

// add할 때: OK
// list가 실제로 어떤 리스트인지 몰라도, 최소 Integer를 담을 수 있는 리스트라는 건 확실
list.add(Integer.valueOf(10)); // OK

// get할 때: 컴파일 오류
// 실제 타입이 List<Integer>, List<Number>, List<Object>일 수 있으므로 정확한 타입을 알 수 없음
Integer obj = list.get(0); // 컴파일 오류
Object obj  = list.get(0); // OK — Object로만 얻을 수 있음

// 실제 사용 예
List<Object> objects = new ArrayList<>();
List<? super Integer> list2 = objects;
list2.add(100); // OK
list2.add(200); // OK
Object o = list2.get(0); // 읽기는 Object
```
---
### \[참고\] static method에 제네릭 타입
static 메서드는 클래스가 인스턴스화되기 전에 호출될 수 있으므로, 클래스의 제네릭 타입 T를 그대로 쓰지 않고 메서드 자체에 별도의 제네릭 타입을 선언해야 함.
```java
import java.util.List;

class Box<T> {
    private T value;

    public Box(T value) {
        this.value = value;
    }

// 인스턴스 메서드: 클래스 제네릭 T를 활용
    public void showValue() {
        System.out.println("Box contains: " + value);
    }

// static 메서드: 메서드 자체 제네릭 U를 활용 (클래스 T와 독립)
    public static <U extends Number> void process(List<U> list) {
        for (U item : list) {
            System.out.println("Processing: " + item);
        }
    }
}
```
static 메서드는 클래스 레벨 제네릭(T)에 접근할 수 없으므로, 반환 타입 앞에 `<U>`처럼 메서드 자체 제네릭을 별도로 선언함.
---
### 제네릭 활용 사례
```java
public class GenericMethodExample {
// 제네릭 메서드 정의 — T[] 배열을 받아 출력
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }

    public static void main(String[] args) {
        Integer[] intArray    = {1, 2, 3, 4, 5};
        String[]  stringArray = {"Hello", "World"};

        System.out.println("Integer Array:");
        printArray(intArray);    // Integer 배열 출력

        System.out.println("\nString Array:");
        printArray(stringArray); // String 배열 출력
    }
}
```
하나의 printArray 메서드가 Integer 배열과 String 배열 모두를 처리할 수 있음. 제네릭 메서드는 호출 시 전달되는 인수의 타입을 보고 T를 자동으로 추론함.
---
### 함수형 프로그래밍 (Functional Programming)
Java의 함수형 프로그래밍은 함수를 일급 객체(First-Class Citizen)로 취급하여, 불변성(immutability)과 순수 함수(pure function)를 기반으로 프로그램을 작성하는 방식임.
함수를 일급 객체(First-Class Citizen)로 사용
- 함수를 변수에 저장, 전달, 반환할 수 있음
- 함수 자체를 데이터처럼 다루는 방식
순수 함수 (Pure Function)
- 같은 입력 → 같은 출력
- 외부 상태를 변경하지 않음 (Side Effect 없음)
불변성 (Immutability)
- 함수 내부에서 외부 변수를 변경하지 않는 구조
- 병렬 처리에서 안정성과 예측 가능성이 높아짐
선언형 스타일 (Declarative Style)
- 어떻게가 아니라 무엇을 할지에 집중
- 시스템이 실행 흐름을 알아서 처리
- Stream, Optional 등이 대표적인 예
---
### 일급 함수
함수를 값처럼 취급할 수 있는 언어 특성임. Python 예시로 4가지 특성을 확인할 수 있음.
```python
# 1. 함수를 변수에 할당
def say_hello():
    print("Hello")

say_hello_var = say_hello   # 함수를 변수에 할당
say_hello_var()             # 변수를 통해 함수 실행

# 2. 함수를 인자로 전달
def execute(fn):
    fn()  # 전달된 함수를 실행

execute(lambda: print("Executed"))  # 람다(익명 함수)를 인자로 전달하며 execute 실행

# 3. 함수를 반환 (return)
def make_adder(x):
    def adder(y):
        return x + y    # 클로저: x를 기억함
    return adder

add5 = make_adder(5)
print(add5(3))  # 출력: 8

# 4. 객체의 속성(properties)으로 사용
calculator = {
    "add": lambda a, b: a + b
}
print(calculator["add"](2, 3))  # 출력: 5
```
---
### 순수 함수 (Pure Function)
동일한 입력에는 항상 동일한 출력을 반환하며, 함수 외부 변수의 상태를 변경하지 않는 함수임.
```python
# 비순수 함수 — 외부 상태(count)를 변경하여 같은 호출에도 결과가 달라짐
count = 0

def increase_and_get():
    global count
    count += 1   # 외부 상태를 변경 (Side Effect)
    return count

print(increase_and_get())  # 출력: 1
print(increase_and_get())  # 출력: 2 (다른 출력)

# 순수 함수 — 외부 상태에 무관하게 같은 입력 → 같은 출력
def square(x):
    return x * x

print(square(4))  # 출력: 16
print(square(4))  # 출력: 16 (항상 동일)
```
---
### 순수 함수 특징
순수 함수를 유지해야 하는 이유는 다음과 같음.
| 장점 | 설명 |
| --- | --- |
| 예측 가능성 | 같은 입력 → 같은 출력, 디버깅이 쉬움 |
| 테스트 용이 | 외부 의존 없이 독립적으로 테스트 가능 |
| 병렬 처리 안전 | 외부 상태를 건드리지 않으니 race condition 없음 |
| 캐싱 가능 | 결과를 재활용(Memoization) 가능 |
| 리팩토링 안정성 | 의존성 적어서 코드 변경 영향 최소화 |
---
### 익명 클래스 (Anonymous Class)
클래스 기반 언어인 Java 환경에서 함수형 프로그램을 지원하기 위한 방식임.
익명 클래스란 이름이 없는 클래스로, 한 번만 사용할 목적으로 정의하며, 클래스를 선언하면서 동시에 인스턴스를 생성함. 주로 인터페이스나 추상 클래스를 구현할 때 사용함.
```java
// Single Abstract Method Interface
@FunctionalInterface
public interface Runnable {
    public void run();
}

// 메서드 호출 시 익명 클래스 전달
executeTask(new Runnable() {
    @Override
    public void run() {
        System.out.println("작업 실행 중...");
    }
});

static void executeTask(Runnable task) {
    task.run();
}
```
문제점: 너무 장황하고, 가독성이 감소하며, 함수 전달을 위한 최소 표현이 아님.
---
### 람다 표현식 (Lambda Expression)
익명 클래스를 간결하게 표현하기 위한 문법으로, 함수형 인터페이스를 인스턴스로 생성하는 가장 짧은 방식임.
```java
// 익명 클래스 방식
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println(" TEST ");
    }
};

// 람다 표현식으로 동일하게 표현
// ( ) → 는 "파라미터 없음 → 다음 코드를 실행"을 의미
Runnable r = () -> System.out.println(" TEST ");

r.run();
```
람다 문법 구조: `(Method arguments) -> Method body`
- `>` 는 lambda 또는 Arrow operator
- 괄호 안은 파라미터, 화살표 이후는 실행할 코드(메서드 바디)
배경.
- Java 8(2014) 이전: Java는 순수 객체지향 언어로, 메서드도 반드시 클래스의 일부여야 함
- Java 8: 람다, Stream API, java.util.function 패키지 도입 → 코드를 값처럼 전달하고 선언적·함수형 스타일 코딩이 가능해짐
| 목적 | 설명 | 예시 |
| --- | --- | --- |
| 코드 간결화 | 익명 클래스 작성의 반복 코드 제거 | list.forEach(item -\> System.out.println(item)) |
| 함수형 프로그래밍 지원 | 함수를 값처럼 전달 | stream.filter(x -\> x \> 10) |
| 병렬/선언형 처리 | Stream API와 결합하여 병렬 연산 지원 | list.parallelStream().map(...).reduce(...) |
---
### 람다 표현식 방식 비교
```java
// 방식 1: 일반적인 클래스 생성
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("별도의 스레드에서 실행");
    }
}

Runnable myRunnable = new MyRunnable();
Thread thread1 = new Thread(myRunnable);
thread1.start();

// 방식 2: 람다 표현식 사용 (요즘 더 일반적임)
Runnable lambdaRunnable = () -> System.out.println("별도 스레드에서 실행");
Thread thread2 = new Thread(lambdaRunnable);
thread2.start();
```
---
### \[참고\] 익명 클래스 vs Lambda 비교
```java
// 익명 클래스
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello");
    }
};

// 람다식
Runnable r = () -> System.out.println("Hello");
```
| 항목 | 익명 클래스 | 람다식 |
| --- | --- | --- |
| 목적 | 객체(클래스) 생성 | 함수 전달(행위 전달) |
| 코드 길이 | 길고 반복적 | 매우 간결 |
| 의미 | 객체지향적 해결 | 함수형 프로그래밍 해결 |
| 실행 구조 | 내부적으로 클래스 생성 | 함수형 인터페이스 구현체 생성 |
| 사용성 | 가독성 낮음 | 가독성·유지보수 높음 |
---
### 함수형 인터페이스
단 하나의 추상 메서드(abstract method)만을 가지는 인터페이스임. 람다 표현식은 바로 이 함수형 인터페이스의 익명 구현 객체로 생성됨. @FunctionalInterface 어노테이션은 함수형 인터페이스임을 명시적으로 나타내며, 추상 메서드가 2개 이상이면 컴파일 오류를 발생시켜 강제함.
```java
@FunctionalInterface
interface Calculator {
    int operate(int a, int b);
}

public class LambdaExample {
    public static void main(String[] args) {
        Calculator add      = (a, b) -> a + b;  // 람다로 구현체 생성
        Calculator multiply = (a, b) -> a * b;

        System.out.println("덧셈: " + add.operate(10, 5));       // 15
        System.out.println("곱셈: " + multiply.operate(10, 5));  // 50
    }
}
```
---
### 표준 함수형 인터페이스
java.util.function 패키지에서 자주 쓰이는 입출력 형태를 미리 정의한 함수형 인터페이스를 제공함.
| 인터페이스 | 추상 메서드 | 설명 | 예시 |
| --- | --- | --- | --- |
| Runnable | void run() | 인자와 반환값이 없는 실행용 작업 | () -\> System.out.println("Hello") |
| Supplier\<T\> | T get() | 값을 반환하지만 매개변수는 없음 | () -\> "SKALA" |
| Consumer\<T\> | void accept(T t) | 값을 소비하지만 반환값은 없음 | s -\> System.out.println(s) |
| Function\<T,R\> | R apply(T t) | 하나의 인자를 받아서 값을 반환 | x -\> x.length() |
| Predicate\<T\> | boolean test(T t) | 조건식(참/거짓)을 평가 | x -\> x.startsWith("S") |
| Comparator\<T\> | int compare(T o1, T o2) | 두 값 비교 작업에 사용 | (a, b) -\> a.length() - b.length() |
---
### 함수형 인터페이스 — Runnable
run()이라는 단 하나의 메서드를 가진 매우 간단한 인터페이스임. 매개변수를 받지도 않고, 값을 반환하지도 않으며, 동시에 실행될 수 있는 작업을 나타내기 위해 설계됨. 보통 별도의 스레드(thread)에서 실행될 코드 블록으로 구성됨.
```java
public class Main {
    public static void main(String[] args) {
        Runnable lambdaRunnable = () -> System.out.println("별도의 스레드에서 실행");
        Thread thread2 = new Thread(lambdaRunnable);
        thread2.start();
    }
}
```
---
### 함수형 인터페이스 — Predicate
단일 값을 매개변수로 받아 true 또는 false를 반환하는 간단한 함수임. 주로 데이터를 필터링하는 데 사용하며, 특정 조건을 기반으로 객체 리스트를 필터링할 때 활용함.
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// 문자열이 "A"로 시작하는지 테스트하는 Predicate 생성
Predicate<String> startsWithA = (s) -> s.startsWith("A");

// Predicate를 사용하여 리스트 필터링
List<String> namesStartingWithA = names.stream()
        .filter(startsWithA)
        .collect(Collectors.toList());
System.out.println(namesStartingWithA); // [Alice]

// filter 메서드에 직접 람다를 사용할 수도 있음
List<String> namesWithLength5 = names.stream()
        .filter(s -> s.length() == 5)
        .collect(Collectors.toList());
System.out.println(namesWithLength5); // [Alice, David]
```
---
### 함수형 인터페이스 — Function
단일 값을 매개변수로 받아 처리 결과를 반환하는 간단한 함수임. 데이터에 대한 값 변환을 위해 사용함.
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// 문자열을 대문자로 바꾸는 Function 생성
Function<String, String> toUpper = s -> s.toUpperCase();

// Function을 사용하여 리스트 변환
List<String> upperNames = names.stream()
        .map(toUpper)
        .collect(Collectors.toList());
// 출력: [ALICE, BOB, CHARLIE, DAVID]
```
---
### 함수형 인터페이스 — Comparator
객체 컬렉션의 사용자 정의 정렬 순서를 정하는 데 사용함. compare()라는 단 하나의 추상 메서드를 가지며, 동일한 타입의 두 객체를 받아 정수를 반환함.
- 음수: 첫 번째 객체가 두 번째보다 앞에 옴
- 0: 두 객체의 순서가 같음
- 양수: 첫 번째 객체가 두 번째보다 뒤에 옴
```java
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public int getAge() { return age; }

    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}

public class Main {
    public static void main(String[] args) {
        List<Person> people = Arrays.asList(
            new Person("Alice", 30),
            new Person("Bob", 25),
            new Person("Charlie", 35)
        );

// 나이순으로 정렬하는 Comparator 생성
        Comparator<Person> byAge = (p1, p2) -> Integer.compare(p1.getAge(), p2.getAge());

// Comparator를 사용하여 리스트 정렬
        Collections.sort(people, byAge);

        System.out.println(people); // [Bob (25), Alice (30), Charlie (35)]
    }
}
```
---
### 람다 표현식 개발 방식
람다를 직접 정의하고 활용하는 3단계 패턴임.
```java
// 1. 함수형 인터페이스 정의
@FunctionalInterface
public interface IAddable<T> {
    T add(T t1, T t2); // 두 개의 객체를 더하는 메서드
}

// 2. 함수형 인터페이스 기반 처리 함수
public static <T> void addGeneric(IAddable<T> adder, T a1, T a2) {
    System.out.println(adder.add(a1, a2));
}

// 3. Lambda 표현식을 이용한 Functional Interface 구현
// 문자열 결합
addGeneric((s1, s2) -> s1 + s2, "Hello, ", "World!"); // Hello, World!

// 정수 덧셈
addGeneric((i1, i2) -> i1 + i2, 10, 20); // 30

// Double 타입도 가능
addGeneric((d1, d2) -> d1 * d2, 3.5, 2.0); // 7.0
```
하나의 함수형 인터페이스(IAddable\<T\>)에 타입별로 다른 람다를 전달하는 것만으로 여러 연산을 처리할 수 있음. 제네릭과 람다를 결합하면 매우 범용적인 코드 작성이 가능함.
---
---
### 메서드 참조 (Method Reference)
람다 표현식을 더 간결하게 표현하는 문법으로, 기존 메서드를 그대로 전달하고 싶을 때 사용함.
기본 구조: `클래스명(or 객체명) :: 메서드명`
람다에서 파라미터를 받아서 그대로 메서드에 넘기기만 하는 경우, 파라미터와 화살표를 생략하고 메서드 참조로 축약할 수 있음.
```java
// 람다 표현식
list.forEach(x -> System.out.println(x));

// 메서드 참조 — x ->, (x) 제거
list.forEach(System.out::println);
```
유형별 변환 방법은 다음과 같음.
| 유형 | Lambda | Method Reference |
| --- | --- | --- |
| 정적 메서드 참조 | x -\> String.valueOf(x) | String::valueOf |
| 특정 객체의 인스턴스 메서드 참조 | x -\> System.out.println(x) | System.out::println |
| 특정 타입의 임의 객체 메서드 참조 | s -\> s.toUpperCase() | String::toUpperCase |
| 생성자 참조 | () -\> new ArrayList\<String\>() | ArrayList::new |
```java
List<String> stocks = List.of("SKALA AI", "SKALA 에듀", "K-테크");

// 람다 표현식
stocks.forEach(s -> System.out.println(s));

// 메서드 참조
stocks.forEach(System.out::println);
```
---
### 람다 표현식에서 외부 변수 사용하기
람다 표현식에서 사용하는 외부 변수는 함수 내 Capture 방식으로 사용되며, 사용되는 외부 변수는 final 또는 effectively final로 설정되어야 함.
```java
// OK — effectively final (선언 이후 한 번도 변경되지 않음)
int base = 10;
Function<Integer, Integer> adder = x -> x + base;
System.out.println(adder.apply(5)); // 15

// 컴파일 오류 — base가 람다 선언 전에 변경되면 effectively final이 아님
int base = 10;
base = base + 5; // 컴파일 오류
Function<Integer, Integer> adder = x -> x + base;

// 컴파일 오류 — 람다 내부에서 외부 변수를 변경하는 것도 불가
int base = 10;
Runnable r = () -> {
    base = base + 1; // 컴파일 오류
};
```
클로저(Closure)로 동작하는 이유는 다음 세 가지임.
- 외부 변수 시점과 람다 함수 호출 시점의 차이로 인한 데이터 불일치 문제 해소
- 스레드 안정성 (thread safety)
- 가비지 컬렉션 최적화
---
### \[참고\] effectively final 이란
effectively final은 변수 타입의 특성이 아니라 코드에서 실제로 값이 변경되었는지로 판단함.
코드에서 실제로 값이 한 번도 변경되지 않았다면 effectively final로 간주하여 람다에서 캡처 가능함.
```java
// effectively final — 변경 없음, 람다에서 사용 가능
int base = 10;
Function<Integer, Integer> adder = x -> x + base;
System.out.println(adder.apply(5)); // 15
```
변경할 수 있는 타입인지를 보지 않고, 코드에서 실제로 변경했나만 확인함.
```java
int base = 10; // 여기서는 effectively final

Function<Integer, Integer> adder = x -> x + base; // OK

System.out.println(adder.apply(5)); // 15

base = 20; // 이 순간 base가 변경되어, 위의 람다도 소급하여 컴파일 오류 발생
```
람다가 선언된 이후에 base를 변경하더라도, 컴파일러는 해당 변수 전체 스코프에서 변경 여부를 보기 때문에 람다 선언 시점과 무관하게 오류가 발생함.
---
### \[참고\] 람다함수가 순수 함수를 유지해야 하는 이유
순수 함수의 특성을 앞에서 다뤘지만, 람다 표현식 맥락에서 특히 중요한 이유를 정리하면 다음과 같음.
| 장점 | 설명 |
| --- | --- |
| 예측 가능성 | 같은 입력 → 같은 출력, 디버깅이 쉬움 |
| 테스트 용이 | 외부 의존 없이 독립적으로 테스트 가능 |
| 병렬 처리 안전 | 외부 상태를 건드리지 않으니 race condition 없음 |
| 캐싱 가능 | 결과를 재활용(Memoization) 가능 |
| 리팩토링 안정성 | 의존성 적어서 코드 변경 영향 최소화 |
람다는 effectively final 규칙과 결합하여, 외부 상태 변경을 구조적으로 막음으로써 이 순수 함수의 특성을 강제하는 방향으로 설계되어 있음.
---
---
### Stream API 란?
Java 8에서 도입된 기능으로 컬렉션(List, Set, Map 등)의 요소들을 선언적(Declarative)이고 함수형(Functional) 스타일로 처리할 수 있도록 지원하는 API임. 기존의 for-loop 또는 Iterator 기반의 반복적인 데이터 처리 코드를 간결하고 가독성 높게 작성하도록 지원함.
현행 구조(외부 반복자) vs Stream 구조(내부 반복자)의 차이는 다음과 같음.
- 외부 반복자: 개발자 코드가 next()를 직접 호출하며 컬렉션에서 요소를 하나씩 꺼내와 처리함. 개발자가 어떻게 반복할지를 직접 제어함
- 내부 반복자: 개발자는 처리 코드(무엇을 할지)만 제공하고, 반복 자체는 컬렉션(Stream)이 알아서 처리함. 선언형 스타일
Stream은 Intermediate Operations(중간 연산)와 Terminal Operation(최종 연산)으로 구성됨.

```java
List<String> result = names.stream()
        .filter(name -> name.startsWith("A")) // 중간 연산: Predicate<T> 사용
        .map(String::toUpperCase)              // 중간 연산: Function<T, R> 사용
        .limit(2)                              // 중간 연산: 최대 2개 요소로 제한
        .collect(Collectors.toList());         // 최종 연산
```
중간 연산은 Lazy Evaluation(지연 연산)으로 동작함. 즉, 최종 연산이 호출되기 전까지 실제로 실행되지 않음.
Stream Operation Flow: Stream Source(List, Map, Set, Arrays 등) → Intermediate Operations(map, filter, distinct, sorted, limit, peek 등) → Terminal Operation(min, max, sum, count, average, reduce, collect 등)
---
### Stream API 코드 비교
같은 문제(현재 판매 중이고 십만원 이하인 상품의 개수)를 두 방식으로 구현한 비교임.
```java
// 일반적인 for-each 코드 구조
public void filterBeforeJava8() {
    int count = 0;
    for (Product pd : products) {          // 상품목록에서 개별 상품을 구해서
        if (pd.isUsable() &&               // 현재 판매 중이고
            pd.getPrice() <= 100000) {     // 십만원 이하라면
            count++;                       // 개수를 1증가
        }
    }
    System.out.println("현재 판매 중이고 가격이 십만원 이하인 상품의 개수 : " + count + "개 ");
}

// Stream API 코드 구조
public void filterJava8() {
    long count = products.stream()            // 상품 중에서
            .filter(p -> p.isUsable())        // 판매 중이고
            .filter(p -> p.getPrice() <= 100000) // 십만원 이하인 상품의
            .count();                         // 개수를 구함
    System.out.println("현재 판매 중이고 가격이 십만원 이하인 상품의 개수 : " + count + "개 ");
}
```
Stream 코드는 각 단계가 "무엇을 할지"를 선언하는 방식으로, for-each보다 훨씬 가독성이 높음.
---
### Stream API 동작 방식 설명
stream()은 선언적 방식으로 동작함.
```java
long count = products.stream()               // Stream<Product> 반환
        .filter(p -> p.isUsable())           // Predicate<Product> 등록 → Stream<Product> 반환
        .filter(p -> p.getPrice() <= 100000) // Predicate<Product> 등록 → Stream<Product> 반환
        .count();                            // 최종 연산 → long 반환
```
- products.stream(): List를 Stream\<Product\>로 변환
- .filter(): Predicate\<Product\>를 등록하고 조건을 만족하는 요소만 통과시킨 새 Stream\<Product\>를 반환. 이 시점에서 실제 실행은 아직 일어나지 않음(Lazy)
- .count(): 최종 연산 호출 시점에 모든 중간 연산이 한꺼번에 실행되고 결과(long)를 반환함
---
### Java Stream API — 최종 연산(Terminal Operations)
최종 연산 중 하나가 호출되는 순간 스트림 파이프라인이 실행됨.
| 최종 연산 | 설명 | 반환값 |
| --- | --- | --- |
| collect() | 스트림을 리스트, 셋, 맵 등으로 수집 | List\<T\>, Set\<T\>, Map\<K,V\> |
| forEach() | 각 요소에 대해 특정 동작 수행 | void |
| reduce() | 모든 요소를 하나의 값으로 합침 (합계, 곱셈 등) | Optional\<T\> 또는 T |
| count() | 요소의 개수를 반환 | long |
| findFirst() | 첫 번째 요소를 반환 | Optional\<T\> |
| findAny() | 아무 요소나 반환 (병렬 스트림에서 유용) | Optional\<T\> |
| allMatch() | 모든 요소가 조건을 만족하는지 검사 | boolean |
| anyMatch() | 하나라도 조건을 만족하는지 검사 | boolean |
| noneMatch() | 모든 요소가 조건을 만족하지 않는지 검사 | boolean |
| toArray() | 스트림을 배열로 변환 | T\[\] |
---
### Stream API 사용 가능한 데이터 소스
Stream API를 사용할 수 있는 객체는 주로 java.util.stream.Stream을 생성할 수 있는 데이터 소스임.
```java
// List
List<String> names = List.of("SKALA", "JAVA", "STREAM");
names.stream().map(String::toLowerCase).forEach(System.out::println);

// 배열
int[] numbers = {1, 2, 3, 4, 5};
IntStream.of(numbers).forEach(System.out::println);

// Map — entrySet()으로 스트림 변환
Map<String, Integer> stock = Map.of("SKALA AI", 15000, "SKALA EDU", 12000);
stock.entrySet().stream()
        .filter(e -> e.getValue() > 13000)
        .forEach(e -> System.out.println(e.getKey()));

// Files.lines() — 파일 한 줄씩 읽기
Files.lines(Paths.get("data.txt"))
        .filter(line -> line.contains("SKALA"))
        .forEach(System.out::println);
```
---
### Method Chaining
한 메서드의 반환값이 다음 메서드를 호출할 수 있도록 설계되어 연속적으로 호출하는 방식임. 즉, 여러 개의 메서드를 한 줄로 연결하여 호출하는 프로그래밍 기법임.
Stream API가 대표적인 메서드 체이닝 예시임.
```java
// Stream API 메서드 체이닝
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.stream()
     .filter(name -> name.startsWith("A"))
     .map(String::toUpperCase)
     .forEach(System.out::println); // ALICE
```
일반 클래스에서도 `return this`를 활용하면 메서드 체이닝을 직접 구현할 수 있음.
```java
class Person {
    private String name;
    private int age;

    public Person setName(String name) {
        this.name = name;
        return this; // 자기 자신을 반환하여 체이닝 가능하게 만듦
    }

    public Person setAge(int age) {
        this.age = age;
        return this;
    }

    public void display() {
        System.out.println("이름: " + name + ", 나이: " + age);
    }
}

// 메서드 체이닝을 이용한 객체 생성 및 설정
Person person = new Person()
        .setName("홍길동")
        .setAge(30);
```
return this 패턴은 빌더(Builder) 패턴에서도 동일하게 활용되며, 객체 설정 코드를 간결하게 만드는 데 유리함.
---
### 주요 java.util 클래스 개요
`java.util` 패키지는 자바에서 가장 자주 사용하는 유틸리티 클래스들이 모여 있는 핵심 패키지임.
| 클래스명 | 주요 용도 |
| --- | --- |
| Collections | List, Set 등 컬렉션을 정렬·섞기 등 다양한 정적 유틸리티 메서드 제공 |
| Arrays | 배열 관련 유틸리티 제공 (sort, toString 등) |
| Optional\<T\> | 값이 있을 수도 없을 수도 있는 상황을 처리하는 컨테이너. null 체크를 대체하는 안전한 방식 |
---
### java.util – Collections
컬렉션(List, Set, Map 등)을 조작하기 위한 정적(static) 유틸리티 메서드 모음 클래스임. `java.util.Collection` 인터페이스와는 다른 개념임에 주의.
#### 주요 메서드
| 메서드 | 설명 |
| --- | --- |
| sort(List) | 리스트를 오름차순 정렬 |
| reverse(List) | 리스트의 요소 순서 반전 |
| shuffle(List) | 리스트 요소를 무작위로 섞기 |
| max(Collection) / min(Collection) | 최대값 / 최소값 찾기 |
| frequency(Collection, Object) | 특정 요소의 등장 횟수 계산 |
| replaceAll(List, oldVal, newVal) | 특정 값 일괄 치환 |
#### 사용 예시
```java
// Collections 예시: 가격 리스트 정렬 및 반전
List<Integer> prices = new ArrayList<>();
prices.add(18000);
prices.add(9500);
prices.add(12000);

// 오름차순 정렬
Collections.sort(prices);
System.out.println("오름차순: " + prices);  // [9500, 12000, 18000]

// 내림차순 정렬 (sort 후 reverse 적용)
Collections.reverse(prices);
System.out.println("내림차순: " + prices);  // [18000, 12000, 9500]
```
내림차순 정렬은 `sort()` 후 `reverse()`를 이어 호출하는 방식으로 구현함.
---
### java.util – Arrays
배열 관련 기능을 지원하는 정적(static) 메서드 유틸 클래스임. 배열은 Java의 기본 데이터 구조이지만 기능이 제한적이므로, Arrays 클래스를 통해 다양한 조작이 가능함.
#### 주요 메서드
| 메서드 | 설명 |
| --- | --- |
| sort(array) | 배열 정렬 (기본형, 참조형 모두 가능) |
| toString(array) | 배열을 문자열로 변환하여 출력 가능 |
| copyOf(array, length) | 배열 복사 (길이 지정 가능) |
| equals(array1, array2) | 배열 간 값 비교 |
| fill(array, value) | 배열을 동일한 값으로 초기화 |
| binarySearch(array, key) | 정렬된 배열에서 이진 탐색 수행 |
#### 사용 예시
```java
// StockArray.java
import java.util.Arrays;

public class StockArray {
    public static void main(String[] args) {
        int[] prices = {18000, 9500, 12000};

        Arrays.sort(prices);  // 오름차순 정렬

// 정렬된 주식 가격: [9500, 12000, 18000]
        System.out.println("정렬된 주식 가격: " + Arrays.toString(prices));
    }
}
```
배열을 그대로 출력하면 메모리 주소가 나오므로, `Arrays.toString()`을 사용해야 `[9500, 12000, 18000]` 형태로 읽을 수 있는 문자열을 얻을 수 있음.
---
### java.util – Optional\<T\>
null로 인해 발생할 수 있는 NullPointerException을 방지하기 위한 컨테이너 클래스임. 값이 존재할 수도, 없을 수도 있는 상황에서 null 여부를 명시적으로 표현하기 위해 사용함.
#### Optional 생성 방법
| 생성 방법 | 설명 |
| --- | --- |
| Optional.of(value) | 절대 null이 아닌 값 감싸기 (null이면 예외 발생) |
| Optional.ofNullable(value) | value가 null이면 Optional.empty() 리턴 |
| Optional.empty() | 비어 있는 Optional 생성 |
#### 주요 메서드
| 메서드 | 설명 |
| --- | --- |
| isPresent() | 값이 존재하는지 여부 (deprecated 경향) |
| ifPresent(Consumer) | 값이 존재하면 처리 수행 |
| get() | 값 반환. 값이 없으면 NoSuchElementException 발생하므로 권장하지 않음. orElse, orElseGet 사용을 권고함 |
| orElse(value) | 값이 없으면 기본값 반환 |
| orElseGet(Supplier) | 값이 없으면 지연된 로직으로 값 생성 |
| orElseThrow() | 값이 없으면 예외 발생 |
`get()` 대신 `orElse()` 또는 `orElseGet()`을 사용하는 것이 안전한 패턴임. `orElseGet()`은 Supplier를 받아 값이 없을 때만 로직이 실행되므로, 기본값 생성 비용이 클 때 유리함.
---
### Reflection 이란?
모르는 대상을 사용해야 할 때 대상에 대한 정보를 알려주고 사용할 수 있도록 도와주는 기술임. Runtime 시점에 클래스에 대한 정보를 검색해 클래스 또는 객체를 조작할 수 있도록 지원함.
특징
- 컴파일 시점이 아니라 런타임에 타입을 조작함
- private 포함 모든 속성/멤버에 접근 가능함
- 동적 객체 생성, 메소서 호출을 지원함
필요성
- 프레임워크 내부 동작 시: Spring DI는 `@Autowired` 필드에 리플렉션으로 값을 주입하고, ORM(JPA)은 엔티티 필드를 리플렉션으로 읽고 씀
- 유연한 코드 구조: 클래스 이름을 문자열로 전달받아 객체를 생성하거나, 플러그인 구조·확장 가능한 아키텍처를 제공하는 데 활용함
---
### Reflection 의미
메타데이터 저장소(메타스페이스, Metaspace)에 올려놓은 클래스의 구조를 읽어오고 조작할 수 있는 기능임. Reflection은 Metaspace 정보 조회/조작 도구이며, `java.lang.reflect` 패키지에 포함됨.
클래스 파일이 컴파일되면 Metaspace에 Class 메타 정보(Field, Method, Constructor)가 올라가고, 런타임 시점에 생성된 Object는 이 Class 정보를 참조하는 구조임.
#### Class와 Member 구성 요소
| 구성 요소 | 설명 | 코드 예시 |
| --- | --- | --- |
| Class | 클래스를 나타내며, Member를 가져오기 위해 클래스를 조회 | `Class<?> clazz = Class.forName("com.example.User");` |
| Constructor | 생성자를 나타내며, 이를 통해 Instance를 생성 가능 | `Object instance = clazz.getDeclaredConstructor().newInstance();` |
| Method | 메소드를 나타내며, 호출하여 사용 가능 | `clazz.getDeclaredMethod("get", String.class).invoke(instance, "Hi Reflection");` |
| Field | 속성을 나타내며, 필드 값을 조회/변경 가능 | `clazz.getDeclaredField("message").set(instance, "my message")` |
생성자 조회 메서드 비교
| 메서드 | 대상 생성자 | 상속 포함 |
| --- | --- | --- |
| getConstructor() | public 생성자만 | 포함 |
| getDeclaredConstructor() | 선언된 생성자 | 제외 |
`getDeclared*` 계열은 상속받은 것은 제외하고 해당 클래스에 직접 선언된 멤버만 조회함.
---
### Why Reflection (1/2) — 런타임 동적 로딩 및 어노테이션 기반 동작 제어
실행 시점에 객체가 결정되어야 하는 경우, 이를 위한 방법을 제공함. 클래스 이름·파라미터 유형으로 대상 객체를 자동 생성 및 실행하는 것이 대표적인 사례임.
1. 런타임 동적 로딩 및 조작
- 컴파일 시점이 아닌 실행 중에 객체 정보를 확인하거나 수정 가능함
- 클래스 이름이 동적으로 결정되거나, 조건에 따라 특정 메서드를 실행해야 할 때 사용함
```java
// 문자열로 클래스 로드 후 생성자를 통해 동적 객체 생성
Class<?> clazz = Class.forName("com.skala.myapp.domain.User"); // User.class로도 사용 가능
var ctor = clazz.getDeclaredConstructor(String.class, Integer.class);

ctor.setAccessible(true); // private 생성자도 접근 허용

Object obj = ctor.newInstance("홍길동", 20); // 인자 전달하여 인스턴스 생성
```
1. 어노테이션 기반 동작 제어
- 런타임에 어노테이션을 읽어서 특정 메서드나 필드에 대해 자동 동작을 수행함
- Spring의 `@Autowired`로 의존성 주입, `@RequestMapping`으로 URL-메서드 매핑이 대표적인 예임
```java
// 객체의 모든 메서드를 순회하며 특정 어노테이션이 붙은 메서드만 실행
Method[] methods = obj.getClass().getDeclaredMethods();
for (Method method : methods) {
// method에 @MyAnnotation이 붙어 있는지 확인
    if (method.isAnnotationPresent(MyAnnotation.class)) {
        method.invoke(obj); // 어노테이션이 붙은 메서드 실행, static method는 method.invoke(null)
    }
}
```
---
### Why Reflection (2/2) — 플러그인 시스템 및 동적 확장
1. 플러그인 시스템 및 동적 확장
- 실행 중에 플러그인을 추가하거나, 인터페이스를 구현하지 않은 클래스도 동적으로 실행 가능함
- 외부 패키지의 클래스를 런타임에 로드하여 확장 기능을 구현할 수 있음
- 다른 클래스를 로드하려면 해당 클래스가 존재하는 경로를 알 수 있는 ClassLoader가 필요함
```java
// ClassLoader를 통해 외부 플러그인 클래스를 동적으로 로드하고 인스턴스 생성
ClassLoader classLoader = MyClass.class.getClassLoader(); // this.class.getClassLoader() 가능
Class<?> dynamicClass = classLoader.loadClass("com.plugin.MyPlugin");
Object pluginInstance = dynamicClass.getDeclaredConstructor().newInstance();
```
---
### \[참고\] 새로운 Annotation 만들기
커스텀 어노테이션을 직접 정의하고, Reflection을 통해 해당 어노테이션이 붙은 메서드를 런타임에 자동 호출하는 패턴임.
어노테이션 생성 방법
```java
// @interface 키워드로 어노테이션 정의
// @Retention: 어노테이션 유지 범위 — SOURCE(Override 등), CLASS, RUNTIME(@Autowired)
// @Target: 어노테이션 적용 대상 — TYPE, FIELD, METHOD, CONSTRUCTOR 등
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface MyAnnotation {}

public class MyService {
    @MyAnnotation
    public void runTask() {
        System.out.println("태스크 실행");
    }

    public void normalMethod() {
        System.out.println("일반 메서드");
    }
}
```
Reflection을 통해 어노테이션 붙은 메서드만 선별 호출
```java
// MyService의 모든 메서드를 순회하여 @MyAnnotation이 붙은 것만 invoke
MyService obj = new MyService();
Method[] methods = obj.getClass().getDeclaredMethods();
for (Method method : methods) {
    if (method.isAnnotationPresent(MyAnnotation.class)) {
        method.invoke(obj); // "runTask() 실행" → "태스크 실행" 출력
    }
}
```
`@Retention(RUNTIME)`으로 설정해야 런타임에 `isAnnotationPresent()`로 어노테이션을 읽을 수 있음. `SOURCE`나 `CLASS`로 설정하면 런타임에는 어노테이션 정보가 사라짐.
---
### Reflection 클래스
`java.lang.reflect` 패키지에서 Reflection을 사용하기 위한 클래스 목록임.
| 클래스 이름 | 설명 |
| --- | --- |
| Class\<?\> | 클래스 자체를 나타내는 메타 정보 객체 |
| Constructor\<?\> | 생성자를 나타내는 객체 |
| Method | 클래스의 메서드를 나타내는 객체 |
| Field | 클래스의 필드를 나타내는 객체 |
| Parameter | 메서드나 생성자의 파라미터 정보를 나타내는 객체 |
| Modifier | 클래스, 메서드, 필드 등의 접근 제한자(public, private 등)를 나타내는 객체 |
---
### Reflection 핵심 클래스: Class\<?\> (1)
Reflection의 진입점임. 클래스 메타 정보를 담고 있으며, 이를 통해 생성자·필드·메서드에 모두 접근할 수 있음.
#### 클래스 획득 방법 3가지
```java
// 1) 클래스 리터럴 — 컴파일 타임에 클래스를 알고 있을 때
Class<Person> clazz1 = Person.class;

// 2) 객체에서 가져오기 — 이미 인스턴스가 있을 때
Person p = new Person();
Class<?> clazz2 = p.getClass();

// 3) 문자열로부터 로딩 (동적 로딩) — 클래스 이름이 런타임에 결정될 때
Class<?> clazz3 = Class.forName("com.example.Person");
```
#### 동적 객체 생성
```java
Class<?> clazz = Class.forName("com.example.Person");

// 기본 생성자 호출
Object obj = clazz.getDeclaredConstructor().newInstance();

// 파라미터 있는 생성자 (String 타입 인자)
Object obj2 = clazz.getDeclaredConstructor(String.class)
                    .newInstance("himang10");
```
#### 필드(Field) 접근
```java
Class<?> clazz = Class.forName("com.example.Person");
Object obj = clazz.getDeclaredConstructor().newInstance();

Field field = clazz.getDeclaredField("name");
field.setAccessible(true);  // private 필드 접근 허용

field.set(obj, "홍길동");                      // 값 설정
System.out.println(field.get(obj));            // 값 읽기
```
#### 메서드(Method) 호출
```java
Class<?> clazz = Class.forName("com.example.Person");
Object obj = clazz.getDeclaredConstructor().newInstance();

// sayHello(String name) 메서드 호출
Method method = clazz.getMethod("sayHello", String.class);
method.invoke(obj, "홍길동");
```
---
### Reflection 핵심 클래스: Class\<?\> (2)
#### 생성자 사용
```java
Class<?> clazz = Class.forName("com.example.Person");

// (String, int) 생성자 호출
Constructor<?> constructor = clazz.getConstructor(String.class, int.class);

Object obj = constructor.newInstance("홍길동", 20);
```
#### 모든 멤버 조회하기
한 클래스의 모든 필드·메서드·생성자를 배열로 한꺼번에 가져올 수 있음.
```java
Class<?> clazz = Person.class;

Field[] fields = clazz.getDeclaredFields();              // 모든 필드
Method[] methods = clazz.getDeclaredMethods();           // 모든 메서드
Constructor<?>[] constructors = clazz.getDeclaredConstructors(); // 모든 생성자
```
`getDeclared*` 메서드는 접근 제한자에 관계없이 해당 클래스에 선언된 모든 멤버를 가져오되, 상속받은 멤버는 포함하지 않음.
---
### Reflection의 한계와 주의 사항
강력한 기능이지만, 남용하면 심각한 문제를 야기할 수 있으므로 사용 시 다음 사항을 고려해야 함.
| 항목 | 설명 |
| --- | --- |
| 성능 저하 | 직접 접근보다 느림 (런타임 탐색 오버헤드) |
| 캡슐화 파괴 | private 접근 가능 → 설계 규칙 위반 위험 |
| 런타임 오류 증가 | 컴파일 시점 타입 체크가 어려움 |
일반적인 비즈니스 로직에는 사용하지 않으며, 프레임워크·라이브러리·플러그인 구조처럼 런타임 유연성이 필수적인 상황에서 제한적으로 활용함.
---
### Annotation 이란?
자바의 Annotation은 클래스, 메서드, 필드에 Hint를 붙이는 속성임. 실제 실행은 Reflection 등을 통해 별도로 이루어짐.
주석(`// comment`)은 사람이 읽기 위한 것이고, Annotation은 내부 프로그램이 읽고 동작을 바꾸기 위한 정보임. 해석하는 주체(컴파일러, JVM, Spring 같은 Framework)가 Reflection을 이용해 구조화된 메타 데이터를 제공하는 방식으로 동작함.
#### Annotation 유지 범위 (Retention)
어노테이션이 언제까지 살아남는지를 결정하는 3단계가 있음.
| Retention | 설명 | 예시 |
| --- | --- | --- |
| SOURCE | 소스 코드에만 존재, 컴파일 시 제거 | `@Override` |
| CLASS | 바이트코드(.class)에 포함, 런타임 접근 불가 (기본값) | `@Deprecated` |
| RUNTIME | 런타임에 리플렉션으로 접근 가능 | `@SpringBootApplication` |
실행 단계에서 코드에서 Reflection으로 읽으려면 반드시 RUNTIME으로 설정해야 함.
---
### Annotation 동작 방식
동작 흐름은 3단계임.
1. `@interface`로 Annotation 정의
2. 클래스/메서드/필드 등에 Annotation 적용
3. 적용 범위에 따라 해석 주체가 달라짐
	- 컴파일러가 해석하는 경우: `@Override`, `@Deprecated` 등
	- 프레임워크가 런타임에 리플렉션으로 읽는 경우: Spring의 `@Service`, `@GetMapping` 등
	- 직접 리플렉션/프로세서로 읽고 동작을 구현하는 경우
```java
// 1) 선언
@interface RunMe { }

// 2) 적용
class MyTask {
    @RunMe
    public void task1() { ... }
}

// 3) 실행 코드 — Reflection으로 어노테이션 읽기
RunMe ann = clazz.getAnnotation(RunMe.class);
```
---
### Annotation : @interface
새로운 Annotation을 만들 때 `@interface` 키워드를 사용함. 속성(요소)은 메서드 모양으로 정의함.
```java
// 값이 없는 마커(Marker) Annotation — 존재 여부만으로 의미를 가짐
public @interface RunMe {
}
// 사용: @RunMe
public class JobRunner {
    public void run() {
        System.out.println("실행 대상 클래스");
    }
}

// 값이 1개 있는 Annotation — 필수 속성 지정
public @interface Author {
    String name();  // 필수 속성 (기본값 없음)
}
// 사용: @Author(name = "홍길동")
public class MyService { }

// 값과 기본값이 있는 Annotation
public @interface Hint {
    String value() default "no-hint";
    int level() default 1;
}
// 사용: @Hint(value = "강한 힌트", level = 5)
public class MyClass { }
```
속성이 하나이고 이름이 `value`이면 `@Hint("강한 힌트")`처럼 이름 생략이 가능함.
---
### Annotation : @Retention, @Target
#### @Target — 어디에 붙일 것인가?
어노테이션을 적용할 수 있는 대상 요소를 제한함
```java
import java.lang.annotation.*;

@Target(ElementType.METHOD)         // 메서드에만 사용
@Retention(RetentionPolicy.RUNTIME)
public @interface RunMe { }
```
| ElementType | 적용 대상 |
| --- | --- |
| TYPE | 클래스, 인터페이스, enum |
| FIELD | 필드 |
| METHOD | 메서드 |
| PARAMETER | 메서드 파라미터 |
| CONSTRUCTOR | 생성자 |
#### @Retention — 언제까지 살아남는가?
```java
@Retention(RetentionPolicy.SOURCE)   // 소스까지만 (컴파일 후 사라짐)
@Retention(RetentionPolicy.CLASS)    // .class 까지 (기본값)
@Retention(RetentionPolicy.RUNTIME)  // 런타임까지 (리플렉션으로 읽을 수 있음)
```
- 실행 단계에서 Reflection으로 읽으려면 RUNTIME으로 설정해야 함
- `RetentionPolicy.SOURCE`를 사용하려면 `AbstractProcessor`를 상속 후 `process` 메서드로 구현함
---
### Annotation 사용법: Class 레벨
클래스에 어노테이션을 적용하고 Reflection으로 읽는 전형적인 패턴임.
```java
// MyComponent.java — 어노테이션 정의
import java.lang.annotation.*;

@Target(ElementType.TYPE)           // 클래스, 인터페이스, enum
@Retention(RetentionPolicy.RUNTIME)
public @interface MyComponent {
    String value() default "";      // 이름 속성
}
```
```java
// OrderService.java — 어노테이션 적용
@MyComponent("orderService")        // value="orderService"와 동일
public class OrderService {
// ...
}
```
```java
// Main.java — Reflection으로 어노테이션 읽기
Class<?> clazz = OrderService.class;

if (clazz.isAnnotationPresent(MyComponent.class)) {
    MyComponent comp = clazz.getAnnotation(MyComponent.class);
    System.out.println("컴포넌트 이름 = " + comp.value());
}
```
### \[참고\] Spring Boot에서 사용하는 Class 레벨 Annotation
```java
// Class 레벨 Annotation 예시
@RestController
public class UserController { }

@Service
public class UserService { }

@SpringBootApplication
public class DemoApplication { }
```
Spring이 내부적으로 이 어노테이션들을 Reflection으로 읽어 빈 등록, 컨트롤러 매핑 등을 자동으로 수행함.
---
### Annotation 사용법: Field 레벨
필드에 어노테이션을 붙여 Reflection으로 의존성을 주입하는 패턴임. Spring의 `@Autowired` 동작 원리와 동일한 구조임.
```java
// Inject.java — 어노테이션 정의
import java.lang.annotation.*;

@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Inject { }
```
```java
// OrderController.java — 어노테이션 적용
public class OrderController {
    @Inject
    private OrderService orderService;  // 주입 대상
}
```
```java
// SimpleContainer.java — Reflection으로 @Inject 필드 탐지 후 주입
public class SimpleContainer {

    public static void injectDependencies(Object target) throws Exception {
        Class<?> clazz = target.getClass();

        for (Field field : clazz.getDeclaredFields()) {
            if (field.isAnnotationPresent(Inject.class)) {
// 인스턴스를 만들어서 주입 (아주 단순한 예)
                Object dependency =
                        field.getType().getDeclaredConstructor().newInstance();

                field.setAccessible(true);
                field.set(target, dependency);
            }
        }
    }
}
```
#### \[참고\] Spring에서 적용하는 코드: Field
```java
// Field 레벨 Annotation 예시
public class SampleFields {

    @Autowired
    private UserService userService;        // 빈 자동 주입

    @Value("${server.port}")
    private int serverPort;                 // 설정 파일 값 주입
}
```
---
### Annotation 사용법: Method 레벨
메서드에 어노테이션을 붙이고, 어노테이션 속성 값을 기준으로 정렬·실행하는 패턴임.
```java
// RunMe.java — 어노테이션 정의 (order 속성 포함)
import java.lang.annotation.*;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface RunMe {
    int order() default 0;
}
```
```java
// TaskRunner.java — 어노테이션 적용
public class TaskRunner {
    @RunMe(order = 2)
    public void taskB() { System.out.println("Task B"); }

    @RunMe(order = 1)
    public void taskA() { System.out.println("Task A"); }

    public void noAnnotation() { System.out.println("Ignore"); }
}
```
```java
// @RunMe가 붙은 메서드만 추출 후 order 순으로 정렬하여 실행
public static void main(String[] args) throws Exception {
    TaskRunner runner = new TaskRunner();
    Class<?> clazz = runner.getClass();

    Method[] methods = clazz.getDeclaredMethods();

// @RunMe가 붙은 메서드만 추출 후 order 순으로 정렬
    Arrays.stream(methods)
            .filter(m -> m.isAnnotationPresent(RunMe.class))
            .sorted(Comparator.comparingInt(m -> m.getAnnotation(RunMe.class).order()))
            .forEach(m -> {
                try {
                    m.invoke(runner);   // 메서드 호출 → Task A, Task B 순으로 출력
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
}
```
#### \[참고\] Spring에서 적용하는 코드: Method
```java
// Method 레벨 Annotation 예시
public class SampleMethods {

    @GetMapping("/users")
    public String getUsers() {
        return "users";                     // GET /users 요청 처리
    }

    @PostMapping("/users")
    public void createUser() { }            // POST /users 요청 처리

    @Transactional
    public void save() { }                  // 트랜잭션 자동 처리
}
```
---
### Annotation 사용법: Parameter 레벨
메서드 파라미터 각각에 어노테이션을 붙여 파라미터 이름이나 역할을 메타데이터로 표현하는 패턴임.
```java
// ParamName.java — 어노테이션 정의
import java.lang.annotation.*;

@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
public @interface ParamName {
    String value();
}
```
```java
// UserController.java — 어노테이션 적용
public class UserController {

    public void createUser(
            @ParamName("userName") String name,
            @ParamName("userAge") int age) {
// ...
    }
}
```
```java
// Reflection으로 파라미터 어노테이션 읽기
Method method = UserController.class
        .getMethod("createUser", String.class, int.class);

Parameter[] params = method.getParameters();

for (Parameter p : params) {
    ParamName ann = p.getAnnotation(ParamName.class);
    if (ann != null) {
        System.out.println("실제 파라미터 이름: " + p.getName()
                + ", Annotation 이름: " + ann.value());
    }
}
```
#### \[참고\] Spring에서 적용하는 코드: Parameter
```java
// Parameter 레벨 Annotation 예시
// GET /users/10?name=hong 요청 처리
public class SampleParameters {

    @GetMapping("/users/{id}")
    public void getUser(
            @PathVariable("id") Long id,      // /users/{id} 경로 값
            @RequestParam("name") String name  // ?name=hong 쿼리 파라미터
    ) { }

    public void createUser(
            @RequestBody User user             // POST body JSON → 객체 변환
    ) { }
}
```
`@PathVariable`, `@RequestParam`, `@RequestBody` 모두 Spring이 내부적으로 Reflection을 통해 파라미터 어노테이션을 읽고 HTTP 요청값을 자동으로 바인딩하는 방식으로 동작함.
---
<empty-block/>
