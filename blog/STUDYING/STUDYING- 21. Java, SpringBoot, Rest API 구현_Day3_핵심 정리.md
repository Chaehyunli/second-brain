---
title: "[STUDYING] 21. Java, SpringBoot, Rest API 구현_Day3_핵심 정리"
created: 2026-08-13
updated: 2026-08-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-12
source_url: https://ch010104.tistory.com/338
---
# [STUDYING] 21. Java, SpringBoot, Rest API 구현_Day3_핵심 정리

## 원문

https://ch010104.tistory.com/338

## 노트 유형

`guide`

## 적용 목적과 전제조건

객체의 생성 과정을 추상화하여, 시스템이 구체적인 클래스에 의존하지 않고 객체를 만들 수 있게 해주는 패턴군임.

시스템 전체에서 단 하나의 인스턴스만을 제공하며, 어디서든 동일한 객체에 접근할 수 있도록 보장하는 패턴임.

## 구현 절차·검증·주의점

### 객체 생성 패턴 (Creational Patterns) 개요

객체의 생성 과정을 추상화하여, 시스템이 구체적인 클래스에 의존하지 않고 객체를 만들 수 있게 해주는 패턴군임.

### Singleton

시스템 전체에서 단 하나의 인스턴스만을 제공하며, 어디서든 동일한 객체에 접근할 수 있도록 보장하는 패턴임.

장점: 메모리 절약, 전역 상태 공유, 인스턴스 생명주기 관리 용이

단점: 테스트 어려움, 과도한 공유로 결합도 증가, 멀티스레드 환경에서는 동기화 필요

```java
public class Singleton {
// 클래스 로딩 시점에 인스턴스를 미리 생성 (Eager Initialization)
    private static final Singleton instance = new Singleton();

    private Singleton() {}  // 외부에서 new 불가

    public static Singleton getInstance() {
        return instance;  // 항상 동일한 객체 반환
    }

    public void sayHello() {
        System.out.println("Hello, Singleton!");
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance();
        Singleton s2 = Singleton.getInstance();
// s1 == s2 → 동일한 인스턴스
        s1.sayHello();
    }
}
```

스프링에서는 @Component, @Service, @Repository로 클래스를 선언하면 Spring IoC 컨테이너가 자동으로 싱글톤 객체로 관리함 → 직접 구현 없이 싱글톤 보장됨.

### Factory Method (1/2) — 구조

객체 생성 코드를 별도의 factoryMethod에 위임하여, 객체 생성 로직과 처리 로직을 분리하는 패턴임. 상위 클래스(Creator)는 어떤 객체를 만들지 모르고, 하위 클래스(ConcreteCreator)가 결정함.

장점: 코드의 결합도 감소, 확장성 및 유지보수성 증가

단점: 클래스 수 증가, 코드 구조가 복잡해질 수 있음

UML 구조: Creator(abstract) → ConcreteCreator가 상속, Product(abstract) → ConcreteProduct가 상속. ConcreteCreator의 factoryMethod()가 ConcreteProduct를 생성해 반환함.

```java
// 상위 추상 Creator — 생성 방식은 모름, 인터페이스만 선언
abstract class Creator {
    public abstract Product factoryMethod();
}

// 하위 ConcreteCreator — 실제 생성 담당
class ConcreteCreator extends Creator {
    @Override
    public Product factoryMethod() {
// 복잡한 사전 설정, 여러 구현체 중 선택,
// 생성 제어(캐싱, 풀링, 재사용, 권한 체크) 등
        return new ConcreteProduct();
    }
}

// 상품 인터페이스
public abstract class Product {
    public abstract void use();
}

// 구체적 상품 구현체
public class ConcreteProduct extends Product {
    @Override
    public void use() {
        System.out.println("ConcreteProduct 사용!");
    }
}
```

### Factory Method (2/2) — 처리 로직 분리

처리 로직(ProductProcessor)은 구체적인 구현체를 전혀 알지 못하고, Creator 인터페이스만 의존함. 실제로 어떤 객체가 생성되는지는 외부에서 주입받은 Creator가 결정함 → "How는 포함되어 있지 않음".

```text
// 처리 로직 — 생성과 완전히 분리
class ProductProcessor {
// 구현을 고려하지 않고 사용 및 절차/프로세스만 구성
// (구현 객체에 대한 명시적 호출이 없음)
    public void process(Creator creator) {
        Product product = creator.factoryMethod();  // How는 포함되어 있지 않음
        product.use();
    }
}
```

```text
// 생성 로직 — 구체적인 대상 생성 및 업캐스팅
ProductProcessor processor = new ProductProcessor();
processor.process(new ConcreteCreator());  // 실제 구현체 전달
```

ProductProcessor는 ConcreteProduct를 직접 참조하지 않으므로, 나중에 다른 ConcreteCreator로 교체해도 처리 로직을 수정할 필요가 없음.

### Abstract Factory — 구조

관련성 있는 여러 종류의 객체군(패밀리)을 생성하는 인터페이스를 제공하는 패턴임. Factory Method가 단일 객체 생성에 집중한다면, Abstract Factory는 연관된 객체들의 집합 전체를 묶어서 생성함.

장점: 관련된 객체들을 일관되게 생성, 객체군(팩토리) 교체가 쉬움

단점: 새로운 제품(Product 종류) 추가가 어려움, 구조가 복잡해질 수 있음 → AbstarctFactory 클래스에 새로운 메소드로 CreateProductC 가 추가될 경우 하위의 ConcreteFactory 클래스에도 메소드를 추가해야함

UML 구조:

AbstractFactory: CreateProductA(), CreateProductB() 메서드 선언

ConcreteFactory1 / ConcreteFactory2: 각각 다른 계열의 ProductA, ProductB를 생성

AbstractProductA / AbstractProductB: 각 제품군의 인터페이스

Client는 AbstractFactory만 바라보고, 어떤 ConcreteFactory인지 신경 쓰지 않음

### Abstract Factory — 코드 예시

```text
// 추상 팩토리 인터페이스 — 어떤 계열의 객체를 만들지 선언
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// 각 OS별 구체 팩토리 — 동일 계열 객체를 묶어서 생성
class WindowsFactory implements GUIFactory { ... }
class MacFactory implements GUIFactory { ... }
```

```text
// 사용 예시 — 런타임 OS에 따라 팩토리를 교체, 클라이언트 코드는 동일
GUIFactory factory;
String osName = System.getProperty("os.name").toLowerCase();
if (osName.contains("mac")) {
    factory = new MacFactory();     // Mac 계열 객체군 선택
} else {
    factory = new WindowsFactory(); // Windows 계열 객체군 선택
}
Application app = new Application(factory);
app.renderUI();
```

Application은 GUIFactory 인터페이스만 알고, 내부에서 createButton()/createCheckbox()를 호출함 → 팩토리만 교체하면 전체 UI 계열이 바뀜.

### Builder

복잡한 객체를 단계별로 생성할 수 있게 도와주는 패턴임. 각 단계는 메서드 체이닝 방식으로 구현됨.

장점: 객체 생성 과정 분리, 불변 객체 생성 가능, 가독성 향상

단점: 클래스 구조가 복잡해질 수 있음

참고: 중첩 클래스 간에는 private 속성에 서로 접근 가능함 → Builder가 User의 private 생성자를 호출할 수 있는 이유임

```text
class User {
    private String name;
    private int age;

// private 생성자 → Builder로만 객체 생성 가능
    private User(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
    }

    public static class Builder {
        private String name;
        private int age;

// 각 setter가 Builder 자신을 반환 → 체이닝 가능
        public Builder setName(String name) { this.name = name; return this; }
        public Builder setAge(int age)     { this.age = age;  return this; }

// 최종적으로 User 객체 생성
        public User build() { return new User(this); }
    }
}

// 사용: 체이닝으로 단계별 설정 후 build()로 확정
// new User.Builder().setName("홍길동").setAge(20).build();
```

Lombok의 @Builder 어노테이션을 이용하면 이 구조 전체를 자동 생성할 수 있음.

### SOLID 원칙이란?

유지보수성, 확장성, 재사용성을 높이고 결합도(coupling)를 낮추기 위한 OOP의 5대 설계 원칙임. Clean Architecture(지속 가능하고 튼튼한 소프트웨어 구조)를 구성하기 위한 핵심 기초 원리이기도 함.

SOLID를 큰 그림에서 보면:

객체 간의 결합도를 낮추고, 객체 내 응집도를 높이는 원칙

인터페이스와 추상화를 적극 활용해 What(사용)과 How(구현)를 분리

변경이 필요할 때 기존 코드 수정 없이 확장이 가능하도록 설계

코드 유지보수성과 테스트 용이성 향상

Clean Architecture는 관심사 분리(Separation of Concerns)를 기반으로 애플리케이션을 계층 별로 나누고, 각 계층이 자신의 역할에만 집중하도록 설계하는 아키텍처임. 비즈니스 규칙과 기술 세부사항을 분리하는 것이 핵심임.

SOLID는 객체지향에서 시작되었지만, 객체 뿐만 아니라 마이크로서비스와 API Level에까지 적용을 고려함.

### 1. SRP — 단일 책임 원칙

한 클래스가 변경되어야 할 이유는 오직 하나여야 함. 한 클래스가 여러 기능을 담당하면, 한 기능의 변경이 다른 기능에 부정적 영향을 줄 수 있음.

```text
// [나쁜 구조] Employee 하나가 조회·급여 계산 두 책임을 가짐
class Employee {
    public void getEmployeeInfo() { /* 직원 정보 조회 로직 */ }
    public void calculatePay()    { /* 급여 계산 로직 */ }
}
```

```text
// [좋은 구조] 책임을 클래스 단위로 분리
class Employee {
    public void getEmployeeInfo() { /* 직원 정보 조회 로직 */ }
}

class PayCalculator {
    public void calculatePay(Employee employee) { /* 급여 계산 로직 */ }
}
```

Spring Boot에서 Controller / Service / Repository를 분리하는 것이 SRP의 대표적인 적용 예시임. 각 계층은 각자 하나의 책임(요청 처리 / 비즈니스 로직 / 데이터 접근)만 담당함.

### 2. OCP — 개방-폐쇄 원칙 (1/2)

행위의 본질을 추상화(인터페이스, 규격)하고, 구체적인 세부 기능은 플러그인 형태로 갈아 끼울 수 있게 만드는 것임. 기존 코드(공통 흐름)는 변경하지 않고, 새로운 기능(세부 구현)만 추가할 수 있어야 함.

```text
// [확장이 어려운 구조] 새로운 결제 수단이 생길 때마다 PaymentService를 수정해야 함
enum PaymentType { KAKAO_PAY, CARD }

class PaymentService {
    public void processPayment(PaymentType type, int amount) {
        if (type == PaymentType.KAKAO_PAY) {
            System.out.println("카카오페이 " + amount + "원 결제 완료");
        } else if (type == PaymentType.CARD) {
            System.out.println("신용카드 " + amount + "원 결제 완료");
        }
// 새로운 결제 수단(NAVER_PAY)이 추가되면?
// 여기에 else if를 또 추가하고 이 클래스를 새로 컴파일해야 함!
    }
}
```

새로운 결제 수단이 생길 때마다 PaymentService 내부를 직접 수정해야 하므로, 기존 코드가 변경으로부터 열려 있는(=폐쇄되지 않은) 잘못된 구조임.

### 2. OCP — 개방-폐쇄 원칙 (2/2)

```text
// 1. 결제라는 행위를 인터페이스로 추상화 (공통 흐름)
interface Payment {
    void pay(int amount);
}

// 2. 구체적인 결제 구현체들을 분리 — 새 수단 추가 시 클래스만 추가하면 됨
class KakaoPay implements Payment {
    public void pay(int amount) { System.out.println("카카오페이 " + amount + "원 결제 완료"); }
}
class CardPay implements Payment {
    public void pay(int amount) { System.out.println("신용카드 " + amount + "원 결제 완료"); }
}

// 3. 결제 서비스는 인터페이스에만 의존 (변경에 닫힘)
class PaymentService {
    public void processPayment(Payment payment, int amount) {
        payment.pay(amount);  // 어떤 결제 수단이 들어오든 이 코드는 변하지 않음
    }
}
```

NaverPay를 추가하고 싶다면 Payment를 구현한 클래스만 새로 만들면 됨. PaymentService는 전혀 손대지 않아도 됨.

### 3. LSP — 리스코프 치환 원칙 (1/2)

자식 클래스는 언제나 부모 클래스의 역할을 대체할 수 있어야 함. 부모 클래스의 메서드를 호출하는 코드에서 자식 클래스로 교체하더라도 정상적으로 동작해야 함.

```text
// 직사각형(부모) — 가로를 바꿔도 세로는 유지될 것으로 이해
class Rectangle {
    protected int width;
    protected int height;

    public void setWidth(int width)   { this.width = width; }
    public void setHeight(int height) { this.height = height; }
    public int getArea() { return width * height; }
}

// 정사각형(자식) — 가로/세로가 같아야 하므로 부모의 메서드를 왜곡함 → LSP 위반
class Square extends Rectangle {
    @Override
    public void setWidth(int width) {
        this.width = width;
        this.height = width;   // 가로를 바꿨는데 세로도 바뀜
    }
    @Override
    public void setHeight(int height) {
        this.width = height;
        this.height = height;
    }
}
```

Rectangle 타입 변수에 Square를 넣고 setWidth(5) → setHeight(3)을 순서대로 호출하면, 직사각형이라면 넓이가 15여야 하지만 Square는 9가 됨. 부모의 계약(가로/세로 독립 변경)을 자식이 깨뜨린 것임.

### 3. LSP — 리스코프 치환 원칙 (2/2)

LSP를 지키는 올바른 방법은 억지로 상속하지 않고, 공통 인터페이스를 각자 독립적으로 구현하는 것임.

```text
// 1. 공통 규약을 인터페이스로 정의
interface Shape {
    int getArea();
}

// 2. 직사각형은 고유의 규칙대로 구현
class Rectangle implements Shape {
    private final int width;
    private final int height;
    public Rectangle(int width, int height) { this.width = width; this.height = height; }

    @Override
    public int getArea() { return width * height; }
}

// 3. 정사각형도 고유의 규칙대로 구현 (직사각형의 규격 요청을 고려할 필요 없음)
class Square implements Shape {
    private final int length;
    public Square(int length) { this.length = length; }

    @Override
    public int getArea() { return length * length; }
}
```

두 클래스 모두 Shape로 업캐스팅해서 사용 가능하며, 서로의 계약을 침범하지 않음.

### 4. ISP — 인터페이스 분리 원칙 (1/2)

클라이언트는 자신이 사용하지 않는 메서드에 의존하지 말아야 함(사용자/소비자 관점). 하나의 범용적인 인터페이스보다 여러 개의 구체적인 인터페이스를 만들어야 함.

```text
// [ISP 위반] 거대하고 뚱뚱한 인터페이스 (Fat Interface)
interface SmartPrinter {
    void print();
    void copy();
    void fax();
}

// ISP 위반! 보급형 프린터는 '복사'나 '팩스'를 못 하는데도 억지로 메서드를 구현해야 함
class BasicPrinter implements SmartPrinter {
    @Override
    public void print() { System.out.println("문서를 출력합니다."); }

    @Override
    public void copy() {
        throw new UnsupportedOperationException("복사 기능을 지원하지 않습니다.");
    }

    @Override
    public void fax() {
        throw new UnsupportedOperationException("팩스 기능을 지원하지 않습니다.");
    }
}
```

구현할 수 없는 메서드에 예외를 던지는 것 자체가 ISP 위반의 증거임.

### 4. ISP — 인터페이스 분리 원칙 (2/2)

```text
// 1. 역할을 잘게 쪼갠 작고 구체적인 인터페이스들
interface Printer { void print(); }
interface Copier  { void copy();  }
interface Fax     { void fax();   }

// 2. 보급형 프린터는 출력 인터페이스만 구현
class BasicPrinter implements Printer {
    @Override
    public void print() { System.out.println("보급형 프린터: 문서를 출력합니다."); }
}

// 3. 최신형 고급 복합기는 필요한 모든 인터페이스를 선택해서 구현
class AdvancedSmartPrinter implements Printer, Copier, Fax {
    @Override public void print() { System.out.println("고급 복합기: 출력합니다."); }
    @Override public void copy()  { System.out.println("고급 복합기: 복사합니다."); }
    @Override public void fax()   { System.out.println("고급 복합기: 팩스를 보냅니다."); }
}
```

각 클래스는 자신에게 필요한 인터페이스만 골라서 구현하므로, 불필요한 메서드와의 결합이 사라짐.

### 5. DIP — 의존 역전 원칙 (개요)

고수준 모듈은 저수준 모듈에 의존하면 안 되며, 둘 다 추상화에 의존해야 함. 추상화는 구체적인 것에 의존해서는 안 되고, 구체적인 것이 추상화에 의존해야 함.

고수준 모듈: 비즈니스 정책, 흐름 (process, service)

저수준 모듈: 세부 구현, 기술, 라이브러리

추상화: Interface, abstract class

나쁜 구조는 Computer(고수준)가 유선 키보드, 모니터(저수준 구현체)를 직접 참조하는 형태임. 무선 키보드나 프로젝션을 추가하면 Computer 클래스를 수정해야 함.

좋은 구조는 Computer가 input device, display라는 추상화된 인터페이스만 바라보고, 저수준 모듈들이 그 인터페이스를 구현하는 형태임. 새 장치를 추가해도 Computer는 수정 불필요함.

### 5. DIP — 의존 역전 원칙 (1/2) — 위반 구조

```text
// 저수준 구현체를 직접 참조
class Keyboard { public void type() { System.out.println("키보드를 사용하여 입력"); } }
class Monitor  { public void display() { System.out.println("모니터에 화면을 출력"); } }

class Computer {
    private Keyboard keyboard;  // 구체 클래스에 직접 의존
    private Monitor  monitor;

    public Computer() {
        this.keyboard = new Keyboard();  // 생성도 내부에서 직접 함
        this.monitor  = new Monitor();
    }

    public void operate() {
        keyboard.type();
        monitor.display();
    }
}
```

강한 결합(Tight Coupling) 문제:

Computer가 Keyboard와 Monitor의 구체 구현에 직접 의존

새로운 입력 장치(Mouse)가 추가되면 Computer 클래스를 수정해야 함

Keyboard를 WirelessKeyboard로 교체하려 해도 Computer를 직접 수정해야 하며, OCP도 동시에 위반함

### 5. DIP — 의존 역전 원칙 (2/2) — 준수 구조

```java
// 추상화된 인터페이스 정의
interface InputDevice  { void type();    }
interface OutputDevice { void display(); }

// 저수준 구현체가 인터페이스에 의존
class Keyboard implements InputDevice {
    @Override public void type()    { System.out.println("키보드를 사용하여 입력"); }
}
class Monitor implements OutputDevice {
    @Override public void display() { System.out.println("모니터에 화면을 출력"); }
}

// 고수준 모듈은 인터페이스만 바라봄
class Computer {
    private final InputDevice  inputDevice;
    private final OutputDevice outputDevice;

// 생성자 주입 — 어떤 구현체가 들어올지 외부에서 결정
    public Computer(InputDevice inputDevice, OutputDevice outputDevice) {
        this.inputDevice  = inputDevice;
        this.outputDevice = outputDevice;
    }

    public void operate() {
        inputDevice.type();
        outputDevice.display();
    }
}

public class Main {
    public static void main(String[] args) {
// 조립(Composition Root)에서만 구현체를 선택
        InputDevice  keyboard = new Keyboard();
        OutputDevice monitor  = new Monitor();
        Computer computer = new Computer(keyboard, monitor);
        computer.operate();
    }
}
```

새로운 입력 장치(마우스)나 출력 장치(프로젝터)를 추가해도 Computer 클래스는 수정 불필요함. 실행 시점에 원하는 구현체를 주입할 수 있으므로, 코드 수정 없이 다양한 장치를 사용할 수 있음. 이 패턴이 Spring의 의존성 주입(DI) 의 기반 원리임.

### 네트워크 참조 모델

네트워크 통신을 설명하는 두 가지 대표 참조 모델이 있음.

OSI 7 Layer: 국제 표준화 기구(ISO)에서 발표한 네트워크 통신 기준 참조 모델

TCP/IP 4 Layer: 미 국방성 연구에서 시작되어 발전한 사실상의 업계 표준 참조 모델

프로토콜은 참조 모델 계층의 구현체임.

IP (Internet Protocol): 데이터를 목적지(IP 주소)까지 전송

TCP (Transmission Control Protocol): 데이터 전송의 신뢰성 보장 → 패킷 손실 시 재전송, 순서 보장

UDP (User Datagram Protocol): 실시간 스트리밍 등의 빠른 데이터 전송 (신뢰성보다 속도 우선)

응용 계층 프로토콜: HTTP, DNS, FTP, SMTP 등

### OSI 7계층 vs TCP/IP 4계층 vs HTTP 매핑

TCP/IP 모델에서 L3~L4는 OS Kernel이 담당하고, L1~L2는 NIC(Network Interface Card) 하드웨어가 담당함.

### [참고] OSI 레이어별 역할과 장비

OSI 계층 별로 서버 간 연결 방식과 담당 장비가 다름.

데이터 전송 시 송신 측은 상위 계층 → 하위 계층 순으로 헤더를 붙여 내려보내고(캡슐화), 라우터를 거쳐 수신 측에서 하위 → 상위 순으로 헤더를 벗겨냄(역캡슐화). Ingress, L7 G/W, AI Service 등이 수신 측 최상단에 위치하여 HTTP 레벨에서 트래픽을 처리함.

### [참고] Transport Layer — Port 기반 통신

전송 계층(Transport Layer)은 패킷 흐름 제어와 오류 제어를 담당하며, 포트 번호를 통해 같은 호스트 내의 어느 애플리케이션으로 패킷을 전달할지 결정함.

하나의 호스트가 여러 애플리케이션을 동시에 실행하더라도, 전송 계층이 포트 번호를 보고 올바른 프로세스로 패킷을 배분함.

IP 주소가 건물 주소라면, 포트 번호는 건물 내 특정 방 번호에 해당함. IP만으로는 호스트를 찾고, 포트까지 있어야 그 위에서 실행 중인 구체적인 애플리케이션까지 찾아갈 수 있음.

### 웹(WWW)이란?

인터넷 = 네트워크 인프라 (하드웨어, 라우터, IP 등)

WWW = 인터넷 위에 구현된 정보 공간 (문서, 이미지, 비디오 등 하이퍼링크로 연결된 정보들의 집합)

웹 문서는 HTML, 웹 서버는 HTTP 프로토콜, 사용자 인터페이스는 브라우저

### 응용 계층 프로토콜: HTTP(S)

웹에서 데이터를 주고받기 위한 통신 규약(프로토콜)임. 응용 계층(Application Layer) 내부에서 처리되며, 클라이언트(웹 브라우저 등)가 서버에 요청을 보내면 서버는 해당 요청에 대한 응답을 돌려주는 방식임. 웹 페이지, 이미지, 영상 등 다양한 형태의 데이터를 전송하는 데 사용됨.

동작 예시:

요청: POST /login?u=foo&p=bar → 클라이언트가 서버로 전송

응답: HTTP/1.1 200 OK + Set-Cookie: s=01a4b873 → 서버가 클라이언트로 반환

### HTTPS (HTTP Secure)

HTTP의 보안 버전으로, SSL(Secure Sockets Layer) / TLS(Transport Layer Security) 암호화를 사용하여 데이터를 보호함. HTTPS는 현재 웹사이트의 기본 표준이며, Google 크롬 같은 브라우저는 HTTPS를 사용하지 않는 웹사이트에 대해 "보안 위험 경고"를 표시함.

### URL

URL(Uniform Resource Locator)은 네트워크 상에서 통합 자원의 위치를 나타내기 위한 규약임. 웹사이트 주소 + 컴퓨터 네트워크 상의 자원을 가리킴.

```text
<scheme>://<user>:<password>@<host>:<port>/<path>?<query>#<fragment>
```

### Request / Response 예시

### GET Request Message

```text
GET /api/user/12345 HTTP/1.1          ← Start Line
Host: api.example.com                 ← Header
Authorization: Bearer eyJhbG...      ← JWT 토큰 등
Accept: application/json             ← JSON 응답을 요청
User-Agent: Mozilla/5.0
Connection: keep-alive
```

### GET Response Message

```text
HTTP/1.1 200 OK                       ← Status Line
Content-Type: application/json        ← Header
Content-Length: 85
Date: Fri, 26 Jul 2025 04:40:00 GMT
Connection: keep-alive

{                                     ← Body (JSON)
  "id": 12345,
  "name": "홍길동",
  "email": "hong@example.com",
  ...
}
```

### HTTP Method

CRUD 작업(Create, Read, Update, Delete)을 나타내며 기본적인 데이터 처리 기능을 의미함.

### HTTP Message 구조

HTTP 메시지는 Metadata(Header + Properties)와 Payload(Body) 두 부분으로 구성됨. Payload(페이로드)는 실제로 전송되는 데이터를 의미하며, 함께 전달되는 헤더나 속성은 페이로드에 포함되지 않음.

### 요청 헤더 (Request Headers) 주요 필드

Host: 요청을 처리할 서버의 도메인

User-Agent: 클라이언트 정보 (브라우저, OS 등)

Accept: 클라이언트가 원하는 응답의 MIME 타입 (예: application/json)

Authorization: 인증 정보 (예: Bearer token)

Content-Type: 요청 본문이 어떤 데이터 형식인지 지정 (예: application/json)

### 응답 헤더 (Response Headers) 주요 필드

Content-Type: 응답 데이터의 MIME 타입 (예: text/html)

Content-Length: 응답 바디의 크기

Set-Cookie: 클라이언트에 설정할 쿠키 정보

Cache-Control: 캐싱 관련 정책

### Custom Headers 예시

```text
X-Correlation-ID: 12345abcd   ← 분산 트랜잭션을 추적하기 위한 ID
X-Request-ID: abcdefg-67890   ← 특정 요청을 식별하기 위한 ID
X-App-Version: 1.0.3          ← 애플리케이션 버전 정보
```

X- 접두사는 표준 헤더가 아닌 커스텀 헤더임을 나타냄. 마이크로서비스 환경에서 요청 추적, 디버깅 등에 활용됨.

### 응용 계층 프로토콜: DHCP와 NAPT

DHCP(Dynamic Host Configuration Protocol)는 공유기(DHCP 서버)와 Client PC(DHCP Client) 사이에서, PC의 내부 네트워크 상에서 사용 가능한 IP를 동적으로 할당받기 위한 프로토콜임. 서버는 67번 포트, 클라이언트는 68번 포트를 사용함.

NAPT(Network Address and Port Translation)는 여러 내부 기기가 하나의 공인 IP를 공유하여 인터넷에 접속하는 방식임. 내부 사설 IP(예: 192.168.1.42, 192.168.1.23)를 가진 기기들이 공유기를 통해 공인 IP(203.0.113.57)에 서로 다른 포트 번호(:2001, :2002)를 붙여 인터넷으로 나가는 구조임.

명령어 ipconfig(Windows) / ifconfig(Linux·Mac)으로 현재 할당된 IP를 확인할 수 있음

### Application Layer 진입점: 소켓(Socket)

소켓은 OS 커널이 제공하는, 프로세스가 네트워크(IP/Port)를 통해 통신하기 위한 추상화된 통신 엔드포인트임. OS Kernel 객체 + Socket API(유저 공간)로 구성됨.

커널이 연결 유지, Socket file Descriptor 관리, 포트 바인딩을 담당하고, 응용 프로그램이 socket API를 통해 통신함

소켓은 특정 포트 번호와 연결되어 있어서, TCP에서 데이터를 보낼 응용 프로그램을 식별하는 역할을 함

동작 예시: 웹 브라우저(소켓 포트 4289) → 인터넷 → 웹 서버(소켓 포트 80)

### 클라이언트와 서버 연결 흐름

소켓 기반 클라이언트-서버 연결은 3단계로 이루어짐.

서버는 서버 소켓으로 들어오는 연결 요청을 기다림 (listen 상태)

클라이언트가 서버에게 연결 요청을 보냄 (클라이언트 포트 → 서버 포트로 연결 요청)

서버가 연결 요청을 수락하고 새로운 소켓을 만들어 클라이언트와 연결을 생성함 → 기존 listen 소켓은 계속 새 연결을 기다리고, 개별 클라이언트와의 통신은 새로 만들어진 소켓이 담당함

### InetAddress Class

java.net.InetAddress는 IP 주소 + 호스트 이름(도메인)을 표현하는 클래스임. DNS 조회, 로컬 호스트 정보 조회 등에 사용됨.

주요 역할:

도메인 이름 → IP 주소 변환

IP 주소 → 도메인 이름 역방향 조회

로컬 머신의 IP/호스트명 조회

주요 메서드:

InetAddress.getByName(String host): "www.naver.com" → 해당 서버의 IP 정보 반환

InetAddress.getLocalHost(): 현재 실행 중인 로컬 컴퓨터의 InetAddress 인스턴스 정보

getHostAddress(): String 형태의 IP 주소 리턴 (예: "192.168.0.10")

getHostName(): 호스트 이름(도메인명) 리턴

```text
InetAddress address = clientSocket.getInetAddress();

String clientIp = address.getHostAddress(); // "192.168.1.100"
String hostname = address.getHostName();    // "client-pc.local"
```

참고: InetAddress를 통해 Domain Name으로 IP를 찾을 때, 실제로는 OS Kernel의 glib resolver에게 IP를 찾도록 요청함 (/etc/resolv.conf 참조).

### Socket Class

java.net.Socket은 TCP 클라이언트를 표현하는 클래스임. 특정 서버(IP, Port)에 접속해서 데이터를 송수신함.

주요 역할:

서버에 TCP 연결 시도 (new Socket(host, port))

연결된 후 입출력 스트림을 통해 데이터 송·수신

연결 종료 (close())

주요 메서드:

### ServerSocket Class

java.net.ServerSocket은 TCP 서버를 표현하는 클래스임. 특정 포트에서 클라이언트 연결을 기다리고(리스닝), 연결되면 Socket을 하나 만들어 반환함.

주요 역할:

서버 포트 바인딩 (new ServerSocket(port))

accept() 호출로 클라이언트 연결 대기 (블로킹)

연결이 들어오면 Socket 인스턴스를 반환 → 이 Socket으로 실제 데이터 송·수신

주요 메서드:

ServerSocket은 연결 수락 전담이고, 실제 데이터 통신은 accept()가 반환한 Socket이 담당함. 이 구조 덕분에 서버는 여러 클라이언트와 동시에 각각 독립된 소켓으로 통신할 수 있음.

### 웹 애플리케이션 개요

웹 애플리케이션이란 클라이언트(사용자)와 서버 사이에서 HTTP 프로토콜을 통해 데이터를 주고받으며 동작하는 프로그램임. 웹 브라우저를 통해 접속하는 것이 특징임.

구성 요소는 크게 클라이언트(프론트엔드)와 서버(백엔드)로 나뉨.

클라이언트: HTML, CSS, JavaScript로 구현하며, Angular / React / Vue.js 같은 프레임워크를 사용함

서버: Java, Node.js, Python 등으로 구현하며, Spring Boot / Express / Django 등의 프레임워크를 사용함

### 요청·응답 흐름

```text
Client (브라우저·모바일 앱)
  → Web Server
    → WAS (Web Application Server)
      → DB
```

요청은 왼쪽에서 오른쪽으로 전달되고, 응답은 역방향으로 되돌아옴. Client가 Web Server에 요청을 보내면, Web Server는 동적 처리가 필요한 경우 WAS에 위임하고, WAS는 DB와 통신해 데이터를 가져온 뒤 응답을 생성해 반환하는 구조임.

### [참고] Web Server vs WAS

Web Server와 WAS는 모두 HTTP 요청을 처리하지만, 담당하는 역할의 성격이 다름.

핵심 구분: Web Server는 이미 완성된 파일을 그대로 돌려주는 역할이고, WAS는 요청마다 로직을 실행해 결과를 만들어내는 역할임. 실무에서는 Web Server(Nginx 등)를 앞단에 두고 정적 리소스를 처리한 뒤, 동적 요청만 WAS로 넘기는 방식을 흔히 사용함.

### REST (Representational State Transfer) 란?

REST는 웹을 거대한 공유 자원 저장소로 바라보고, 그 자원을 전달하기 위한 다양한 표현(XML, JSON, FILE 등)을 주고받는 아키텍처 스타일임. 로이 필딩(Roy Fielding)이 2000년 박사 학위 논문에서 처음 정립한 개념임.

### Resource (자원)

REST에서 자원이란 서버가 제공하고 클라이언트가 조작할 수 있는 모든 대상을 의미함. 데이터 그 자체가 아니라 데이터가 의미하는 개념이 자원이며, 항상 명사로 정의함.

예: User, Product, Article, Order, Review, Image, SensorData

### REST 핵심 3대 요소

### REST 핵심 구성요소: Resource Identifier (자원의 식별자)

모든 자원은 고유하게 식별될 수 있어야 하며, REST에서는 이를 URI로 표시함.

URI: "어떤 자원이냐"를 표현

HTTP Method: "그 자원을 무엇을 할 것이냐"를 표현

URI는 반드시 명사형으로만 자원을 지정하며, 동사를 URI에 포함하는 것은 잘못된 설계임.

```text
# 올바른 예 (명사형으로 리소스 지정)
GET    /users/10         # 10번 사용자 조회
PUT    /users/10         # 사용자 정보 전체 수정
PATCH  /users/10         # 부분 수정
DELETE /users/10         # 삭제
GET    /users/10/orders  # 특정 사용자의 주문 목록 조회

# 잘못된 예
/createUser, /updateUser
# 동작(create, update)은 URI가 아니라 HTTP Method로 표현해야 함
```

### [참고] URI vs URL

URI와 URL은 혼용되기 쉬운 개념이나 포함 관계가 다름.

추가로 URN(Uniform Resource Name)은 URI의 하위 개념으로, 리소스의 "이름"에 초점을 맞춘 식별자임.

### REST 핵심 구성요소: 자원의 행위 (HTTP Method)

자원을 조회·생성·수정·삭제(CRUD)하는 행위는 URI가 아니라 HTTP 메서드를 통해 서버에 전달함.

### REST 핵심 구성요소: Representation (자원의 표현)

클라이언트는 자원 자체를 받는 것이 아니라, 자원을 표현한 데이터 형태(Representation)를 받음. 예를 들어 서버에 User라는 자원이 존재하더라도 클라이언트는 User 객체 자체가 아닌 User를 JSON으로 표현한 데이터를 받음.

대표적인 Representation 형태: JSON (REST 기본), XML, YAML, HTML, Text, Image (jpg·png), Binary (file), PDF 등

### REST 설계 원칙 (6가지)

REST는 단순한 API 스타일이 아니라, 웹의 확장성과 단순성을 유지하도록 설계된 제약조건(Constraints) 기반의 아키텍처 스타일임. 6가지 원칙을 모두 만족할 때 비로소 RESTful한 시스템으로 정의함.

### 원칙 1: 클라이언트-서버 분리

클라이언트(UI)와 서버(비즈니스 로직·데이터 저장) 역할을 분리함. 서로 API라는 계약만 공유하며, 내부 구현은 독립적으로 유지함.

클라이언트: 화면 구성과 사용자 경험에만 집중

서버: 데이터 저장·처리·비즈니스 규칙에만 집중

효과: Vue/React와 Spring Boot를 독립 개발 가능, 서버 교체·확장이 쉬움, 유지보수성과 개발 속도 증가

```text
# 클라이언트 요청
GET /users/10

# 서버 JSON 응답
{ "id": 10, "name": "홍길동" }
```

클라이언트는 이 데이터로 화면을 표현할 뿐이며, 서버가 DB를 MySQL에서 PostgreSQL로 바꿔도 클라이언트는 전혀 상관 없음.

### 원칙 2: 무상태성 (Stateless)

서버는 클라이언트의 세션 상태를 보관하지 않음. 각 요청은 완전히 독립적이며, 요청에는 인증·권한·처리에 필요한 모든 정보를 항상 포함해야 함 (Header, JWT, HTTP-Only Cookie 등).

효과: 상태를 보관하지 않으므로 서버 Scale-out이 매우 쉬워짐 (어떤 서버가 받아도 처리 가능), 시스템 단순화 및 오류 감소.

```text
# Stateful 방식 (세션 기반)
로그인 요청 → 서버가 세션 생성 → 이후 요청마다 서버 세션 기준으로 판단

# REST 방식 (JWT 사용)
GET /profile
Host: api.example.com
Authorization: Bearer eyJhbGci0i...
```

서버는 "이 사용자가 이전 요청에서 로그인했는지" 기억하지 않고, JWT를 확인만 진행함.

### 원칙 3: 캐시 가능 (Cacheable)

응답은 명확히 캐시 가능 여부를 나타내야 하며, HTTP 캐시 기능(Cache-Control, ETag 등)을 활용하는 것이 REST의 원칙임.

효과: 빠른 성능, 서버 부하 감소

```text
# Cache-Control 사용 예
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=600
```

위 응답은 600초(10분) 동안 재사용(캐시) 가능함을 표시하며, 브라우저·CDN·Proxy 모두 이 헤더를 보고 캐싱을 수행함. 600초 후 캐시 만료 인식 시 서버에 재 요청을 발송함. 서버는 리소스의 캐시 가능 여부, 기간, 조건 등을 클라이언트에 지시함.

### 원칙 4: 일관된 인터페이스 (Uniform Interface)

모든 API가 동일한 규칙을 따라야 함. 4가지 세부 조건으로 구성됨.

자원의 식별 (URI 기반): URI는 동사가 아닌 명사 기반이어야 함

표준 메서드 사용: GET, POST, PUT, DELETE 등 HTTP 표준 메서드로 동작 표현

표준 문서 형태로 데이터 공유: 서버는 자원을 JSON, XML, YAML 등 표준 형태로 전달

자기서술적 메시지(Self-descriptive message): 요청/응답 메시지는 스스로 해석 가능해야 함

```text
# URI 올바른 예 (명사형)
GET /users/10
GET /orders/2025/items

# URI 잘못된 예 (동사 포함)
/getUserInfo
/doOrderCreate
```

```text
# 표준 메서드 사용 예
GET    /products      # 모든 상품 조회
GET    /products/1    # 특정 상품 조회
POST   /products      # 새로운 상품 생성
PUT    /products/1    # 상품 정보 전체 수정
PATCH  /products/1    # 상품 정보 일부 수정
DELETE /products/1    # 상품 삭제
```

자기서술적 메시지 예: 요청에 Content-Type: application/json을 포함하고, 응답에 HTTP/1.1 201 Created, Location: /users/10 등을 담아 메시지에 모든 의미가 담겨 문서 없이도 해석 가능해야 함.

### 원칙 5: 계층 구조 (Layered System)

클라이언트는 요청이 어느 서버 노드로 가는지 알 필요 없음. 로드밸런서, 게이트웨이, 인증 서버, 프록시 등이 중간 계층으로 존재할 수 있으며, 서버는 여러 계층으로 나뉠 수 있음.

```text
Client → API Gateway → Auth Server → Backend → Database
```

효과: 보안 강화(인증 서버 분리), 로드밸런싱·캐싱·API 게이트웨이 등 추가 기능 쉽게 도입, 구조 확장성 증가. 클라이언트는 백엔드 서버가 몇 개인지 알 필요가 없음.

### 원칙 6: Code-on-Demand (선택)

서버가 클라이언트에게 실행 가능한 코드를 내려보내고, 클라이언트는 이를 동적으로 실행하여 기능을 확장하는 방식임. 6가지 원칙 중 유일하게 선택 사항임.

효과: 클라이언트를 업데이트 없이도 서버가 클라이언트의 행동을 바꿀 수 있음.

브라우저에 새로운 JavaScript 파일을 내려보내면: UI 동작이 바뀌고, 새로운 Form 검증이 추가되고, 특정 페이지에서만 실행되는 맞춤 로직을 수행할 수 있음.

### 일관된 인터페이스: REST API 설계 규칙 정리

### REST API 설계 예시

사용자 관리와 게시판 관리를 REST 원칙에 따라 설계하면 아래와 같음.

사용자 관리

게시판 관리

계층적 URI 구조(/posts/10/comments)가 자원 간 포함 관계를 명확하게 표현하는 좋은 예임.

### Spring 개요

Java 기반 오픈소스 애플리케이션 프레임워크로, 엔터프라이즈급 애플리케이션 개발의 표준임. 복잡한 Java 개발을 단순화하는 컨테이너 역할을 함.

### Spring의 역사 및 Spring Boot 등장 배경

Spring은 2003년, 복잡한 Java EE의 대안으로 등장함. 그러나 전통적인 Spring 설정은 복잡한 XML 파일과 긴 환경 구축 시간이 문제였고, 이를 해결하기 위해 2014년 Spring Boot가 등장함.

Spring Boot 주요 특징 요약: 자동 설정(Auto-configuration), 내장 서버(Tomcat·Netty 등) JAR 실행, Starter 의존성 관리, YAML/Properties 기반 설정, 쉬운 배포(Docker 등).

### Spring 생태계

실제 현업에서는 Spring Boot + Spring Data JPA + Spring Security 조합이 가장 많이 쓰임.

### [참고] 전통적인 Spring vs Spring Boot

### 컴포넌트 스캔 (Component Scan)

스프링이 지정된 패키지 이하를 탐색하여 특정 어노테이션이 붙은 클래스를 찾아 스프링 빈(Bean)으로 자동 등록하는 기능임. 기본 스캔 범위는 @SpringBootApplication이 선언된 클래스의 하위 패키지 전체임.

@SpringBootApplication은 아래 3가지 어노테이션의 조합임.

스캔 범위를 제한할 때는 scanBasePackages 속성을 사용함.

```java
// com.skala.stock, com.sk.common 두 패키지만 스캔
@SpringBootApplication(scanBasePackages = {"com.skala.stock", "com.sk.common"})
public class StockApiApplication { ... }
```

### 컴포넌트 스캔 대상 어노테이션

스프링 부트의 스테레오타입(Stereotype) 어노테이션이 붙은 클래스들이 스캔 대상이 됨.

### Spring Boot main 진입점

Spring Boot 애플리케이션은 main 메서드에서 SpringApplication.run()을 호출하는 것으로 시작됨.

```java
// com/sk/skala/myapp/MyappApplication.java
package com.sk.skala.myapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyappApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyappApplication.class, args);
// MyappApplication.class → 이 클래스를 기준으로 컴포넌트 스캔 시작
    }
}
```

SpringApplication.run()에 전달하는 MyappApplication.class가 스캔 시작점이 됨. 이 클래스가 위치한 패키지(com.sk.skala.myapp) 및 그 하위 패키지 전체가 자동 스캔 범위가 됨.

### Spring 개요

Java 기반 오픈소스 애플리케이션 프레임워크로, 엔터프라이즈급 애플리케이션 개발의 표준임. 복잡한 Java 개발을 단순화하는 컨테이너 역할을 함.

### Spring의 역사 및 Spring Boot 등장 배경

Spring은 2003년, 복잡한 Java EE의 대안으로 등장함. 그러나 전통적인 Spring 설정은 복잡한 XML 파일과 긴 환경 구축 시간이 문제였고, 이를 해결하기 위해 2014년 Spring Boot가 등장함.

Spring Boot 주요 특징 요약: 자동 설정(Auto-configuration), 내장 서버(Tomcat·Netty 등) JAR 실행, Starter 의존성 관리, YAML/Properties 기반 설정, 쉬운 배포(Docker 등).

### Spring 생태계

실제 현업에서는 Spring Boot + Spring Data JPA + Spring Security 조합이 가장 많이 쓰임.

프로젝트 역할

### 컴포넌트 스캔 (Component Scan)

스프링이 지정된 패키지 이하를 탐색하여 특정 어노테이션이 붙은 클래스를 찾아 스프링 빈(Bean)으로 자동 등록하는 기능임. 기본 스캔 범위는 @SpringBootApplication이 선언된 클래스의 하위 패키지 전체임.

@SpringBootApplication은 아래 3가지 어노테이션의 조합임.

스캔 범위를 제한할 때는 scanBasePackages 속성을 사용함.

```java
// com.skala.stock, com.sk.common 두 패키지만 스캔
@SpringBootApplication(scanBasePackages = {"com.skala.stock", "com.sk.common"})
public class StockApiApplication { ... }
```

### 컴포넌트 스캔 대상 어노테이션

스프링 부트의 스테레오타입(Stereotype) 어노테이션이 붙은 클래스들이 스캔 대상이 됨.

### Spring Boot main 진입점

Spring Boot 애플리케이션은 main 메서드에서 SpringApplication.run()을 호출하는 것으로 시작됨.

```java
// com/sk/skala/myapp/MyappApplication.java
package com.sk.skala.myapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyappApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyappApplication.class, args);
// MyappApplication.class → 이 클래스를 기준으로 컴포넌트 스캔 시작
    }
}
```

SpringApplication.run()에 전달하는 MyappApplication.class가 스캔 시작점이 됨. 이 클래스가 위치한 패키지(com.sk.skala.myapp) 및 그 하위 패키지 전체가 자동 스캔 범위가 됨.

### MVC 모델

MVC는 1970년대부터 이어진 전통적인 UI 아키텍처 패턴으로, 역할 분리 원칙을 따르는 구조임. Spring은 이 개념을 웹 애플리케이션 개발에 맞게 프레임워크로 구현함.

### Spring MVC 내부 처리 흐름

HTTP Request를 받아 Controller를 찾아 업무를 처리하고, 결과를 View와 Model로 반환하는 구조임. Tomcat 기반 동기방식으로 동작함.

전체 흐름 (DispatcherServlet 중심):

클라이언트 HTTP Request 수신 → Tomcat이 HttpServletRequest/HttpServletResponse 생성

DispatcherServlet이 요청을 받음 (Front Controller 역할)

HandlerMapping에 URL 매핑 정보 조회 → 처리할 Controller 메서드 검색

HandlerAdapter가 해당 Controller 메서드 호출

Controller → Service → Repository 순서로 비즈니스 로직 실행

결과(Model)를 ViewResolver에 전달 → View 렌더링 (MVC 방식) 또는 HTTPMessageConverter로 JSON 변환 (REST 방식)

응답을 HttpServletResponse로 작성, 톰캣이 클라이언트로 전송

### REST API 기반 Spring Boot MVC — MVC 방식과의 차이

REST API 기반 처리 흐름:

```text
HTTP Request
  → DispatcherServlet
    → HandlerMapping (URL → Controller 메서드 탐색)
      → HandlerAdapter (메서드 호출)
        → 사용자 컨트롤러 (객체 반환)
          → HTTPMessageConverter (JSON/XML 변환)
            → HTTP Response
```

Controller 내부 계층 호출 흐름:

```text
HandlerAdapter → Controller → Service → Repository
                ← 객체 반환   ← 객체 반환
← ResponseEntity / Object / List 반환
```

실제 프로젝트 패키지 구조는 controller / service / repository / model / config 등으로 역할별 분리함.

### [참고] Spring Boot MVC 주요 컴포넌트 정리

### [참고] Servlet 동작 구조

Tomcat(서블릿 컨테이너)과 DispatcherServlet의 역할 분담 구조임.

Servlet Container (Tomcat) 담당: TCP 소켓 관리, HTTP Parsing, HttpServletRequest/HttpServletResponse 생성, IoC Container 내부 DispatcherServlet 호출

DispatcherServlet 담당: Spring MVC 요청 처리, Controller 호출, HttpServletResponse 생성

동작 순서: 클라이언트가 TCP 포트(예: 8080)로 연결 → Tomcat이 HTTP 프로토콜을 해석해 HttpServletRequest/HttpServletResponse 생성 → URL 매핑에 따라 DispatcherServlet.service() 호출 → doGet()/doPost() 실행 → Spring MVC 처리 진행

### [참고] View Type

View 컴포넌트는 DispatcherServlet이 ViewResolver를 통해 찾은 객체임. render(model, request, response) 메서드를 실행하여 모델 데이터를 이용해 최종 응답을 만듦. HTML뿐 아니라 JSON, XML, PDF, 이미지 파일도 결과물이 될 수 있음.

### Controller의 역할

Controller는 클라이언트 요청을 가장 먼저 받아 해석하고 전체적인 흐름을 제어하는 통제소(Dispatcher) 역할을 함.

요청 접수 및 라우팅 (Request Mapping): HTTP 요청 진입점

요청 데이터 검증 및 변환 (Data Validation & Binding): Java 객체 변환 및 유효성 검증

비즈니스 로직 오케스트레이션 (Orchestration): Service 계층 호출 및 데이터 처리 위임

응답 구조화 및 반환 (Response Generation): JSON 데이터 변환 및 HTTP 상태코드 주입

컨트롤러를 지정하는 어노테이션은 @Controller와 @RestController 두 가지이며, 이 둘의 핵심 차이는 HTTP Response Body가 생성되는 방식임.

### @Controller vs @RestController

@Controller 사용 예 — View 반환과 JSON 반환 혼용:

```java
@Controller
public class TestController {
    private final TestService testService;

    public TestController(TestService testService) {
        this.testService = testService;
    }

// view 이름 반환 → resources/templates/test/view.html 을 전달
    @GetMapping(value = "/test/view")
    public String findView(Model model, @RequestParam String name) {
        Test result = testService.find(name);
        model.addAttribute("test", result);
        return "/test/view";
    }

// JSON 데이터 반환 → @ResponseBody 필요
    @GetMapping(value = "/test")
    public @ResponseBody ResponseEntity<Test> find(@RequestParam String name) {
        return ResponseEntity.ok(testService.find(name));
    }
}
```

@RestController 사용 예 — 모든 메서드가 자동으로 JSON 반환:

```java
@RestController
public class TestController {
    private final TestService testService;

    public TestController(TestService testService) {
        this.testService = testService;
    }

// JSON 데이터 반환
    @GetMapping(value = "/test")
    public ResponseEntity<Test> find(@RequestParam String name) {
        return ResponseEntity.ok(testService.find(name));
    }

// view 이름 반환 시 → JSON이 아닌 문자열 "/test/view" 자체가 반환됨 (주의)
    @GetMapping(value = "/test/view")
    public String findView(@RequestParam String name) {
        Test result = testService.find(name);
        return "/test/view";
    }
}
```

### @RestController — HTTP 메서드별 매핑 어노테이션

RESTful 웹 서비스를 만들 때 사용하는 핵심 어노테이션임. 클래스 내의 모든 메서드가 HTTP 요청을 받아 JSON, XML 등의 형태로 응답을 자동으로 반환함.

### [참고] @RequestMapping 활용

@RequestMapping은 Spring MVC에서 HTTP 요청 URL과 메서드/클래스를 매핑하는 가장 기본적인 어노테이션임. @GetMapping, @PostMapping 등은 @RequestMapping의 method 속성을 축약한 버전임.

```text
@RequestMapping(value="/test", method=RequestMethod.GET)  =  @GetMapping("/test")
```

클래스 레벨에 @RequestMapping을 선언하면 해당 컨트롤러의 모든 메서드 URL 앞에 공통 prefix로 적용됨.

```java
@RestController
@RequestMapping("/api") // 클래스 레벨에서 공통 prefix 설정
public class UserController {

// 실제 경로: GET /api/users
    @RequestMapping(value = "/users", method = RequestMethod.GET)
    public List<String> getUsers() {
        return List.of("홍길동", "이순신", "강감찬");
    }
}
```

### 파라미터 바인딩 어노테이션

클라이언트가 보낸 HTTP 요청의 다양한 정보(URL 경로 변수, 쿼리 파라미터, 요청 본문 등)를 컨트롤러 메서드의 매개변수에 자동으로 연결(바인딩)해주는 어노테이션들임.

### @PathVariable

URL 경로에 포함된 값을 메서드 파라미터로 바인딩함. {변수명} 형태로 경로를 지정하고, 변수명이 같으면 어노테이션 내 이름 생략 가능함.

```text
// Client: GET <http://localhost:8080/users/100>

@GetMapping("/users/{id}")
public User getUser(@PathVariable("id") Long id) {
// /users/100  →  id = 100
}
```

### @RequestParam

쿼리스트링(?key=value) 또는 폼 데이터를 바인딩함. required, defaultValue 속성으로 필수 여부와 기본값을 지정할 수 있음.

```text
// Client: GET <http://localhost:8080/search?keyword=Spring>
@GetMapping("/search")
public List<User> search(@RequestParam("keyword") String keyword) {
// keyword = "Spring"
}

// Client: GET <http://localhost:8080/search?name=kim&age=20>
@GetMapping("/search")
public String search(@RequestParam String name, @RequestParam int age) {...}

// 필수 여부, 기본값 지정
@RequestParam(required=false, defaultValue="all") String type
```

배열/리스트 형식의 파라미터 전달도 지원함. Spring은 기본적으로 콤마(,)로 구분된 값을 리스트/배열로 자동 변환함.

```text
// 같은 이름 반복: ?category=java&category=spring&category=boot
@GetMapping("/search")
public String search(@RequestParam("category") String[] categories) {
// categories: ["java", "spring", "boot"]
}

// 콤마 구분: ?category=java,spring,boot
@GetMapping("/search")
public String search(@RequestParam("category") List<String> categories) {
// categories: ["java", "spring", "boot"]
}
```

### @RequestBody

HTTP 요청 본문(Body)에 담긴 JSON, XML 데이터를 자바 객체로 자동 변환(Mapping)함. 주로 POST, PUT, PATCH에서 사용함.

```text
// Client 요청 (curl)
// curl -X POST <http://localhost:8080/users> \
//      -H "Content-Type: application/json" \
//      -d '{"name": "홍길동", "email": "hong@example.com", "age": 30}'

@PostMapping("/users")
public User createUser(@RequestBody User user) {
// 요청 body의 JSON → User 객체 자동 매핑
}
```

JavaScript Fetch로 동일한 요청을 보낼 때는 아래와 같이 사용함.

```typescript
fetch('<http://localhost:8080/users>', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: '홍길동', age: 30 })
})
.then(res => res.json())
.then(data => console.log('등록된 사용자:', data))
.catch(err => console.error(err));
```

### @RequestHeader

HTTP 요청 헤더 값을 파라미터로 받음. 인증 토큰, Content-Type, User-Agent 등을 추출할 때 사용함.

```text
// Client 요청 헤더 예
// Authorization: Bearer eyJhbGci0i...
// Content-Type: application/json
// Origin: <https://app.example.com>

@GetMapping("/users/me")
public User getMe(
        @RequestHeader("Authorization") String token,
        @RequestHeader(value = "Content-Type", required = false) String contentType,
        @RequestHeader(value = "Origin", required = false) String origin
) {
// Authorization: Bearer eyJhbGci... → token 파라미터로 전달
}
```

### @CookieValue

요청 쿠키 값을 파라미터로 받음.

```text
// Client: Cookie: visitTime=2025-08-15T13:30:00

@GetMapping("/visit")
public String visit(@CookieValue("visitTime") String visitTime) {
// 쿠키에 저장된 visitTime 값 사용
}
```

### Repository의 역할

Repository는 비즈니스 도메인 객체(Entity)를 영구적으로 저장하고 관리하는 데이터베이스 연결 계층임.

데이터의 영속성 제공 (Persistence): 메모리 저장 객체를 데이터베이스에 영구 저장

DB 기술 및 쿼리 숨김 (Abstraction): 복잡한 SQL문이나 ORM(JPA, Hibernate, MyBatis 등)의 구체적인 사용법을 내부에 숨기고, 객체 지향적인 메서드 호출만으로 데이터를 획득/처리

영속성 컨텍스트 관리 및 데이터 매핑: Java 객체와 데이터 테이블 간 변환 및 변경 사항 감지/동기화

인프라 및 기술 환경과의 격리 (Decoupling): 특정 DB 기술에 직접 종속되지 않아 외부 환경 변화에 코드가 수정되지 않도록 구성

### Repository 구현

JpaRepository를 상속받은 인터페이스를 선언하면 자동 구현체가 생성됨. Spring Data JPA의 경우 메서드 네이밍만으로 SQL을 자동 생성함.

```text
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findByName(String name); // 추가 생성한 메서드 선언
}
```

JpaRepository가 자동으로 제공하는 기본 메서드: findAll(), findById(ID id), save(S entity) (insert or update), deleteById(ID id), delete(T entity)

### User Entity 만들기

Repository를 통해 Java Object와 DB Table 간 매핑하고 동기화하기 위해 User 객체를 Domain Entity로 선언해야 함 (JPA, ORM).

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
    private String email;

// 기본 생성자 (JPA 필수)
    public User() {}

// 기존 Constructor, Getter, Setter 유지
}
```

### Service의 역할

Service는 소프트웨어 본질인 핵심 비즈니스 규칙을 정의하고 트랜잭션의 단위를 관리하는 계층임. Controller와 Repository 사이의 중간다리 역할을 하며, 가급적 DB 접근 로직은 넣지 않고 순수한 비즈니스 로직만 구현해야 함.

핵심 비즈니스 로직 수행 (Core Business Logic)

트랜잭션 경계 설정 및 관리: DB 작업의 원자성(Atomicity)을 보장하는 트랜잭션 단위, @Transactional 어노테이션 선언 위치

Repository 오케스트레이션: 여러 Repository(데이터 접근 계층)를 조합하고 제어

인프라 및 기술 환경과의 격리: 웹 기술(HTTP, JSON, Controller)이나 특정 DB 기술에 직접 종속되지 않음

### Service 구현 예시

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(FileUserRepository userRepository) {
        this.userRepository = userRepository;
    }

// 이름 필터처럼 내부적 로직 처리는 가능하면 Service에서 처리
    public List<User> findAll(Optional<String> name) {
        Collection<User> all = userRepository.findAll();
        if (name.isPresent()) {
            String search = name.get();
            return all.stream()
                    .filter(u -> u.getName() != null && u.getName().equalsIgnoreCase(search))
                    .collect(Collectors.toList());
        }
        return new ArrayList<>(all);
    }

    public Optional<User> findById(long id) {
        return userRepository.findById(id);
    }
}
```

### 의존관계 자동 주입 (DI)

Controller, Service, Repository의 호출을 위해 @Autowire 어노테이션 또는 생성자 함수를 통해 자동 의존성 주입을 사용함. 생성자 주입 방식이 권장됨.

```java
@RestController
@RequestMapping("/api")
public class UserController {
    private final UserService userService;

// 생성자 주입 — Spring이 UserService 빈을 자동으로 주입
    public UserController(UserService userService) {
        this.userService = userService;
    }

// GET /api/users?name=홍길동 (name 없으면 전체 조회)
    @GetMapping("/users")
    public List<User> getAllUsers(@RequestParam Optional<String> name) {
        return userService.findAll(name);
    }

// GET /api/users/1
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUserById(@PathVariable long id) {
        log.info("getUserById called with id: {}", id);
        return userService.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
```

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
