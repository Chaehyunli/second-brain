---
title: "[Java/Python] 타입 확인 및 replace"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "codingtest", "java", "Python"]
category: "CODINGTEST"
published: 2026-05-08
source_url: https://ch010104.tistory.com/272
---

# [Java/Python] 타입 확인 및 replace

## 원문

https://ch010104.tistory.com/272

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

파이썬은 문자열 객체 안에 자체적인 판별 메서드가 내장되어 있어 매우 편리합니다.

data = 10 if isinstance(data, int): print("이 변수는 숫자형입니다.")

## 원문 기반 개념 정리

### 타입 확인

### 1. 핵심 요약 비교표

### 2. 언어별 상세 코드 (조건문 예시)

### 🐍 파이썬 (Python)

파이썬은 문자열 객체 안에 자체적인 판별 메서드가 내장되어 있어 매우 편리합니다.

변수의 타입 자체를 확인

data = 10 if isinstance(data, int): print("이 변수는 숫자형입니다.")

문자열 내용물이 숫자인지 확인 (isdigit)

s = "12345" if s.isdigit(): print("문자열이지만 숫자로만 구성되어 있어 변환이 가능합니다.") # "12.3" 처럼 소수점이 있으면 False를 반환하므로 주의!

### ☕ 자바 (Java)

자바의 String 클래스에는 isdigit() 같은 단일 메서드가 없어서 보통 정규표현식을 사용합니다.

변수의 타입 자체를 확인

Object data = "123"; if (data instanceof String) { System.out.println("이 변수는 문자열 타입입니다."); }

문자열 내용물이 숫자인지 확인

String s = "12345"; // 정규식 사용: \\d(숫자)가 +(1개 이상) 있는지 확인 if (s != null && s.matches("\\\\d+")) { System.out.println("문자열 내용이 숫자로만 구성되어 있습니다."); }

### 3. [심화] 내용물 판별 시 주의사항

### 파이썬의 isdigit(), isnumeric(), isdecimal() 차이

파이썬은 숫자를 판별하는 메서드가 세분화되어 있습니다.

isdigit(): 가장 흔히 사용. 일반 숫자 및 지수(²) 등 판별.

isdecimal(): 오직 0-9까지의 정수만 판별.

isnumeric(): 분수, 로마자 숫자 등 더 넓은 범위의 숫자 형태 인정.

공통점: 음수("-")나 소수점(".")은 False를 반환합니다. (이때는 try-except로 float() 변환을 시도하는 것이 일반적입니다.)

### 자바에서 숫자를 판별하는 다른 방법들

반복문 사용: 문자열의 각 문자가 Character.isDigit()인지 일일이 확인.

Try-Catch 활용 (가장 확실함):

try { Integer.parseInt(s); // 숫자 변환 성공 시 로직 } catch (NumberFormatException e) { // 숫자가 아닐 때 로직 }

### Replace

### 1. 파이썬 (Python)

파이썬의 replace는 사용법이 매우 간단하며, 원본 문자열을 직접 바꾸지 않고 치환된 새로운 문자열을 반환합니다.

문법: 문자열.replace(찾을값, 바꿀값)

특징: 별도의 정규식 없이도 모든 일치 항목을 한꺼번에 바꿉니다.

### 📝 파이썬 문제 풀이 예시

```python
def solution(s): words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i, word in enumerate(words):
    # 영단어를 그 인덱스(i)의 문자열 형태로 치환
    s = s.replace(word, str(i))

return int(s)`
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### ☕ 2. 자바 (Java)

자바는 replace와 replaceAll 두 가지가 있는데, 이 문제처럼 단순히 글자를 바꿀 때는 성능이 더 빠른 replace를 권장합니다.

문법: 문자열.replace("찾을값", "바꿀값")

특징: 자바의 String은 불변(Immutable)이므로, 반드시 s = s.replace(...)와 같이 결과값을 다시 변수에 담아줘야 합니다.

### 📝 자바 문제 풀이 예시

```text
class Solution { public int solution(String s) {
    String[] words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (int i = 0; i < words.length; i++) {
            // String.valueOf(i)는 int i를 문자열로 바꿔줍니다.
            s = s.replace(words[i], String.valueOf(i));
        }

    return Integer.parseInt(s);
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### ⚖️ 한눈에 비교하기 (파이썬 vs 자바)

## 관련 글

- [[blog/CODINGTEST/index|CODINGTEST]]
- [[blog/CODINGTEST/코딩테스트- 현대오토 2026-04-05 회고|[코딩테스트] 현대오토 2026-04-05 회고]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 6. 로그인처리1 - 쿠키, 세션|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션]]
