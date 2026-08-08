---
title: "[8/6] 데이터 분석을 위한 Python 이해_Day1_핵심 정리"
notion_page_id: "3b31d84b-f68e-8030-a278-cc239a08f44a"
source_url: "https://app.notion.com/p/3b31d84bf68e8030a278cc239a08f44a"
synced_at: "2026-08-08T23:32:50+09:00"
content_sha256: "14970b0a83f3c38cfcf6761a1df0db1343adf44df2aa2dce67c6b1e4ab7f674d"
tags: [notion, skala, learning, python, data-analysis]
---

# [8/6] 데이터 분석을 위한 Python 이해_Day1_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b31d84bf68e8030a278cc239a08f44a) (2026-08-08 확인)

### AI-Native 개발 환경 구성 — `uv`
**`uv`** 는 Astral이 개발한 Rust 기반의 차세대 Python 패키지 관리자임. `pip`, `virtualenv`, `poetry`, `pyenv`의 기능을 하나의 도구로 통합했으며, 기존 `pip` 대비 최대 **100배 빠른 속도**를 자랑함.
#### 기존 방식(pip + venv) vs 현대적 방식(uv)
| 작업 | 기존 방식 (pip + venv) | 현대적 방식 (uv) |
| --- | --- | --- |
| 패키지 설치 | `pip install requests` | `uv add requests` |
| 가상환경 생성 | `python -m venv .venv && source .venv/bin/activate` | `uv sync` (자동 가상환경 생성) |
| 의존성 파일 관리 | `requirements.txt` 수동 관리 | `pyproject.toml` + `uv.lock` 자동 관리 |
| 의존성 고정 | `pip freeze > requirements.txt` | `uv lock` (재현 가능한 잠금 파일) |
| 의존성 해결 속도 | 느림 (수십 초) | 초고속 (수 초 이하) |
| 도구 수 | 여러 도구 별도 설치 필요 | uv 하나로 모든 것 해결 |
---
### 변수 (Variable)
데이터를 저장하는 공간이며, **이름을 통해 저장된 값을 참조**할 수 있음. Python에서는 별도 타입 선언 없이 `변수명 = 값` 형태로 바로 선언 및 할당 가능함.
```python
x = 10          # 정수형 변수
name = "Alice"  # 문자열 변수
is_active = True  # 불리언 변수
```
---
#### 변수 이름 규칙
#### 사용 가능 문자 및 기본 규칙
| 항목 | 내용 |
| --- | --- |
| 사용 가능 문자 | 알파벳 소문자 `a-z`, 대문자 `A-Z`, 숫자 `0-9`, 언더스코어 `_` |
| 첫 글자 | 숫자로 시작 불가 → 문자 또는 `_`로만 시작 가능 |
| 대소문자 구분 | `myVar`와 `MyVar`는 서로 다른 변수로 취급됨 |
| 특수문자 | `_` 제외한 특수문자 사용 불가 |
#### 예약어 사용 금지
Python의 키워드(예약어)는 변수명으로 사용할 수 없음. 아래 코드로 전체 목록 확인 가능함.
```python
import keyword
print(keyword.kwlist)
```
#### 권장 명명 관습
- **의미 있는 이름** 사용: 데이터 내용과 관련된 이름이 유지보수에 유리함
- **명명 스타일**: 소문자 기반이 원칙이며, 복합 단어는 `snake_case` 또는 `camelCase` 사용
- **언더스코어로 시작하는 이름** 주의: Python 내부에서 특별한 의미를 가질 수 있어 일반 변수에는 피하는 것이 좋음
---
### Python 개요
**간결하고 가독성이 높은 문법을 가진 인터프리터 기반의 프로그래밍 언어**임.
#### 특징
- 문법이 쉽고 간결해 초보자도 배우기 쉬움
- **인터프리터 언어** → 코드를 한 줄씩 실행하며 테스트 가능
- 다양한 라이브러리 제공 → 데이터 분석, 인공지능, 웹 개발 등 폭넓게 활용 가능
- **객체 지향 프로그래밍(OOP)** 지원
- **멀티 패러다임** 지원 → 절차적, 객체 지향, 함수형 프로그래밍 모두 가능
- **플랫폼 독립적** → Windows, Mac, Linux 등 다양한 환경에서 실행 가능
#### 활용 분야
| 분야 | 대표 도구 |
| --- | --- |
| 웹 개발 | Django, Flask |
| 데이터 분석 | Pandas, NumPy, Matplotlib |
| 인공지능(AI) 및 머신러닝 | TensorFlow, PyTorch, Scikit-Learn |
| 자동화 및 스크립트 | 업무 자동화, 웹 스크래핑 |
| 게임 개발 | Pygame |
| 네트워크 프로그래밍 | socket 모듈 |
---
### Python의 한계 — 활용 불가(?) 영역
Python이 간결하고 강력한 언어이지만, 구조적 특성상 적합하지 않은 분야도 존재함.
| 분야 | 이유 |
| --- | --- |
| OS 및 저수준 시스템 프로그래밍 | 인터프리터 언어 특성상 메모리 직접 제어·하드웨어 접근이 어려움 |
| 모바일 앱 개발 | iOS, Android 네이티브 지원이 제한적 |
| 고성능 게임 개발 | CPU 사용량이 높아 성능 문제 발생 가능 |
| 실시간 시스템 및 하드웨어 제어 | **Garbage Collection**으로 인한 예측 불가 지연, **GIL(Global Interpreter Lock)** 이 걸리는 상황에서 오류 발생 가능성 높음 |
| 블록체인 개발 | 높은 보안성·효율성 요구에 부합하기 어려움 |
| 대형 Enterprise System (ERP 등) | 대규모 시스템에서 성능·안정성 한계 존재 |
| multithreading 기반 고성능 앱 | 멀티프로세스는 가능하나, **GIL로 인해 multithreading 성능은 낮음** |
---
### Python 문법 요약 — 수 데이터와 연산자
Python은 정수(`int`)와 실수(`float`) 데이터를 처리하는 다양한 문법을 제공함. 변수에 값을 할당할 때는 `=` 등호를 사용함.
#### 정수(int)
- 양의 정수, 0, 음의 정수로 구성되며, **소수점 이하 값이 없음**
- Python은 컴퓨터 메모리가 허용하는 한 **정수 크기에 제한이 없음**
#### 실수(float)
- 소수점 이하 값을 포함하는 데이터
- 실수와 정수 사이에서 연산을 수행하면 **자동으로 정수 → 실수로 형 변환**이 일어남
#### 산술 연산자
| 연산자 | 의미 |
| --- | --- |
| `+`, `-`, `*`, `/` | 사칙연산 |
| `//` | 몫 (정수 나눗셈) |
| `%` | 나머지 |
| `**` | 제곱 |
#### 문자열(str)
- 큰따옴표(`"`) 또는 작은따옴표(`'`)로 감쌈
- 문자열 안에 따옴표를 출력해야 할 경우 **역슬래시(****`\`****)** 사용
- 문자열끼리 `+` 연산을 수행하면 **두 문자열이 이어 붙여짐** (연결)
---
### Python 문법 요약 — 문자열 인덱싱, 리스트, 튜플
#### 문자열 인덱싱 & 슬라이싱
- 첫 번째 문자의 인덱스는 **0**부터 시작
- 슬라이싱 예시: `aa[:5]`(처음부터 4번째까지), `bb[3:]`(3번째부터 끝까지)
#### 리스트(list)
- **대괄호** `[]` 안에 원소들을 쉼표로 구분하여 저장
- 각 원소는 보통 같은 자료형이지만, **서로 다른 자료형도 함께 저장 가능**
- 인덱싱과 슬라이싱 모두 사용 가능
- 리스트끼리 `+` 연산 → **두 리스트를 이어 붙인 결과** 반환
- 다중 중첩(2중, 3중 리스트 등) 가능
- **가변(mutable)** 객체이므로 생성 후 원소 변경 가능
- 주요 메서드: `insert`, `append`, `remove`, `sort`
- 초기화 시 **list comprehension** 사용 시 효율적이고 간결함
#### 튜플(tuple)
- **소괄호** `()` 사용, 리스트와 달리 **불변(immutable)** 객체
- 값이 변경되면 안 되는 상황에서 사용하면 효과적임
---
### Python 문법 요약 — 딕셔너리, 집합, Bool
#### 딕셔너리(Dictionary)
- **Key-Value 쌍** 형태로 데이터를 저장할 때 사용
- `{key: value}` 형식이며, **각 키는 고유해야 함** (값은 중복 가능)
- **Python 3.7부터는 삽입 순서를 보장**
- 특정 원소의 존재 여부를 빠르게 확인하고 추가/삭제 가능
#### 집합(Set)
- **중복을 허용하지 않는** 고유한 요소들의 자료형
- `{요소1, 요소2, ...}` 형식으로 저장
- **순서가 없으며, 인덱스를 통한 접근 불가**
- 교집합, 합집합 등 **집합 연산**이 필요할 때 유용함
#### Bool 자료형
| 값 | 해당하는 경우 |
| --- | --- |
| `False` | `0`, 비어 있는 리스트/튜플/사전, `None` 등 |
| `True` | 이외의 실제 의미 있는 값들 |
---
### Python 문법 요약 — 파일 입출력
표준 입출력 프로그램은 키보드(입력장치)로부터 입력을 받아 모니터(출력장치)로 결과를 내보냄. 파일 I/O는 `open()`으로 파일 객체를 생성하고, 작업 완료 후 `close()`로 닫음. `with` 구문을 사용하면 블록 종료 시 자동으로 파일이 닫힘.
#### 파일 모드
| 모드 | 의미 |
| --- | --- |
| `r` | 읽기 (read) |
| `w` | 쓰기 (write) — 기존 내용 덮어씀 |
| `a` | 추가 (append) — 기존 내용 뒤에 이어씀 |
#### 주요 함수
- `write()` : 파일에 데이터 쓰기
- `read()` : 파일 전체 내용을 하나의 문자열로 반환
- `readline()` : 파일의 데이터를 **한 줄씩** 읽기
- `readlines()` : 파일의 **모든 줄을 읽어 리스트로 반환**. 각 줄에 줄바꿈 기호(`\n`)가 포함되어 있으므로, 출력 시 `strip()`으로 제거함
```python
# 파일 쓰기 예제
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Goodbye!")
```
---
### Python 문법 요약 — 파일 입출력 예제
```python
# 파일 읽기 예제
with open('example.txt', 'r') as file:
    contents = file.read()  # 파일의 모든 내용을 읽기
    print(contents)
```
```python
# 여러 줄을 파일에 쓰기 예제
lines = ["First line\n", "Second line\n", "Third line\n"]

with open('lines_example.txt', 'w') as file:
    file.writelines(lines)  # 리스트의 각 요소를 파일에 쓰기
```
---
#### Python 문법 요약 — 파일 입출력 예제 (계속)
python
```python
# 여러 줄 읽기 예제
with open('lines_example.txt', 'r') as file:
    lines = file.readlines()  # 파일의 모든 줄을 읽어 리스트로 반환

# 각 줄 출력
for line in lines:
    print(line.strip())  # 줄 끝의 개행 문자 제거하고 출력
```
```python
# 기존 파일에 추가 쓰기 예제
with open('example.txt', 'a') as file:
    file.write("\nThis line is added later.")
```
---
#### Python 문법 요약 — 함수
소스 코드를 기능별로 분리하여 작성하면 유지보수와 재사용이 용이함. `def` 키워드로 함수를 정의하며, 함수 내부에 docstring(`"""..."""`)을 작성해 기능을 문서화할 수 있음.
```python
def greet(name):
    """주어진 이름을 가진 사람에게 인사합니다."""
    return f"Hello,{name}!"

# 함수 호출
message = greet("Alice")
print(message)  # 출력: Hello, Alice!
```
---
#### Python 문법 요약 — 클래스와 인스턴스
**클래스**는 붕어빵 틀, **인스턴스**는 그 틀에서 찍어낸 붕어빵에 비유할 수 있음. 클래스는 속성(데이터)과 메서드(동작)를 하나로 묶는 설계도 역할을 함.
- `__init__()` : 인스턴스 생성 시 자동으로 호출되는 **초기화 메서드**. `self`는 생성된 인스턴스 자신을 참조함
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 name 초기화
        self.age = age    # 인스턴스 변수 age 초기화

    def introduce(self):
        return f"Hello, my name is{self.name} and I am{self.age} years old."

# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 메서드 호출
print(person1.introduce())  # Hello, my name is Alice and I am 30 years old.
print(person2.introduce())  # Hello, my name is Bob and I am 25 years old.
```
---
### Python 문법 요약 — 예외처리
런타임 오류가 발생했을 때 프로그램이 비정상 종료되지 않도록 **`try-except`**** 구문**으로 예외를 처리함. 여러 종류의 예외를 구분해서 `except`를 여러 개 사용할 수 있으며, `else` 블록은 **예외가 발생하지 않았을 때만 실행**됨.
```python
try:
    number = int(input("숫자를 입력하세요: "))
    result = 10 / number
except ValueError:
    print("유효하지 않은 숫자입니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과는{result}입니다.")  # 예외가 발생하지 않았을 때 실행
```
---
### Python이 데이터 분석의 표준 언어인 이유
| 특성 | 내용 |
| --- | --- |
| 인터프리터 언어 | 소스코드를 한 줄씩 읽어 즉시 실행. 대화형(REPL) 탐색이 가능해 데이터 분석에 최적 |
| 방대한 생태계 | NumPy, Pandas, scikit-learn, Polars, DuckDB 등 데이터 분석에 필요한 모든 것을 `pip`로 설치 가능 |
| 2026 AI/ML 표준 | TensorFlow, PyTorch, LangChain, RAG 파이프라인까지 Python 중심. 전체 커리큘럼의 기반 언어 |
| 읽기 쉬운 문법 | 들여쓰기 기반 블록 구조로, 분석 코드를 비전공자도 읽을 수 있을 만큼 간결함 |
---
### Python 실행 구조
Python은 **컴파일 언어가 아닌 인터프리터 언어**임. 사용자가 `.py` 파일로 작성한 코드를 한 줄씩 읽어 바로 실행하지만, 단순한 줄 단위 실행 구조가 아니라 중간에 **바이트코드(Bytecode)** 라는 중간 표현 단계를 거침.
#### 인터프리터 내부 처리 흐름
소스코드 → **파서(Parser)** → **AST(Abstract Syntax Tree)** → **바이트코드 생성기** → **Python Virtual Machine(PVM)**
```python
import dis

def add(x, y):
    return x + y

dis.dis(add)  # 바이트코드 출력
```
---
### Python 실행 흐름 — 소스코드에서 결과까지
| 단계 | 설명 |
| --- | --- |
| 소스코드 (`.py`) | 개발자가 작성한 Python 코드 |
| 파서 (Parser) | 소스코드를 읽어 문법 분석 |
| AST | 문법 구조를 추상 구문 트리(Abstract Syntax Tree) 형태로 변환 |
| 바이트코드 (`.pyc`) | 기계어 대신 PVM이 이해할 수 있는 중간 표현으로 변환 |
| PVM 실행 | Python Virtual Machine이 바이트코드를 해석하여 결과 출력 |
**CPython은 소스를 직접 기계어로 변환하지 않고 바이트코드를 거침** → 이를 통해 **이식성과 재사용성**을 확보함.
---
### AST와 dis — 실행 구조를 눈으로 확인하기
Python 내부 실행 구조를 `ast`와 `dis` 모듈을 통해 직접 확인할 수 있음.
- **AST**: 소스코드를 트리 구조로 추상화한 것. 린터, 포매터, 트랜스파일러 등이 내부적으로 AST를 사용함
- **`dis`**** 모듈**: 함수가 어떤 바이트코드로 컴파일되는지 출력해줌. `LOAD_FAST`, `BINARY_OP`, `RETURN_VALUE` 같은 명령어 구조를 눈으로 확인 가능
- list comprehension이 `for` 루프보다 빠른 이유도 바이트코드 수준에서 확인 가능함
```python
import ast, dis

# AST 분석
tree = ast.parse('x = a + b')
print(ast.dump(tree, indent=2))

# 바이트코드 분석
def add(x, y): return x + y
dis.dis(add)

# 출력:
# LOAD_FAST  0 (x)
# LOAD_FAST  1 (y)
# BINARY_OP  0 (+)
# RETURN_VALUE
```
---
### Python 실행 구조 — 바이트코드 명령어 상세
Python은 **컴파일 + 인터프리트 방식**을 혼합해 사용함. 소스코드는 바이트코드로 변환된 뒤 PVM(Python Virtual Machine)에서 실행되므로, **재사용성과 이식성이 높음**.
`dis.dis(add)`로 `add(x, y)` 함수의 바이트코드를 출력하면 아래와 같은 명령어 구조를 확인할 수 있음.
| 줄번호 | 바이트오프셋 | 명령어 | 인자 | 의미 |
| --- | --- | --- | --- | --- |
| 3 | 0 | RESUME | 0 | Python 3.11 이후 도입된 실행 초기화 명령어 (디버깅/프레임 시작용) |
| 4 | 2 | LOAD_FAST | 0(x) | 지역 변수 x를 스택에 Push |
|  | 4 | LOAD_FAST | 1(y) | 지역 변수 y를 스택에 Push |
|  | 6 | BINARY_OP | 0(+) | 스택에서 두 값을 pop한 후 + 연산 수행, 결과를 Push |
|  | 10 | RETURN_VALUE | - | 연산결과 반환 |
x와 y를 스택에 올리고 `x + y` 연산을 수행한 뒤 결과를 `return`하는 구조임.
---
### Python 실행 구조 — 전체 흐름 정리
Python의 실행은 단순한 한 줄씩 해석이 아니라 아래의 4단계 파이프라인을 거침.
소스코드 `.py` → 파싱(Parser) → **AST(Abstract Syntax Tree)** → 컴파일(Compile to Bytecode) → **Bytecode ****`.pyc`** → 실행(Python Virtual Machine) → **실행결과**
바이트코드는 기계어가 아닌 PVM이 이해할 수 있는 **중간 표현**이며, 이 구조 덕분에 플랫폼에 관계없이 동일한 `.pyc` 파일을 재사용할 수 있음.
---
#### \[참고\] AST(Abstract Syntax Tree)
AST는 소스코드의 **문법적 핵심 요소만 남겨 추상화한 트리 구조**임. 변수 선언, 연산, 함수 호출 등의 코드 의미 단위가 \*\*노드(node)\*\*로 구성되어 계층적 트리를 이룸. 컴파일 과정과 코드 분석 과정 모두에서 핵심적인 역할을 담당함.
#### AST 사용 목적
| 영역 | 내용 |
| --- | --- |
| 코드 분석 및 이해 | 코드의 구조를 명확하게 보여줌. 컴파일러·인터프리터가 코드 의미 분석 및 오류 검증에 활용 |
| 코드 변환 및 최적화 | 트리 구조를 조작해 더 효율적인 코드로 최적화. 다른 버전의 언어로 쉽게 변환(예: 최신 JS 문법 → 구형 문법) |
| 다양한 개발도구 활용 | 린터(Linter): 코드 문법 오류 수정 / 포매터(Formatter): 코드 스타일 통일 / 트랜스파일러(Transpiler): 최신 문법 변환 |
---
### \[참고\] AST 구조 예시
`const a = 10 + 5;` 라는 JavaScript 코드를 AST로 변환하면 아래와 같은 계층적 트리 구조가 생성됨. 코드의 각 요소(변수명, 연산자, 값)가 **노드 단위로 분리**되어 표현됨.
```plain text
- VariableDeclaration (변수 선언)
  - kind: const (상수)
  - declarations:
    - VariableDeclarator (변수 선언자)
      - id: Identifier (식별자)
        - name: "a"
      - init: BinaryExpression (이항 표현식)
        - left: Literal (리터럴)
          - value: 10
        - operator: "+"
        - right: Literal (리터럴)
          - value: 5
```
이처럼 AST는 소스코드를 **컴퓨터가 이해하기 쉬운 구조화된 형태**로 변환한 것이며, 이 트리를 기반으로 컴파일·최적화·분석이 이루어짐.
---
### Python 바이트코드
바이트코드는 Python 소스코드가 파싱된 후 생성되는 \*\*중간 표현(Intermediate Representation)\*\*임. `.pyc` 파일에 저장되며 PVM에서 실행됨.
- **실행 속도 향상**: 한 번 생성된 바이트코드는 재사용 가능하므로 반복 실행 시 파싱 비용이 절감됨
- **OS 독립적**: 추상화된 명령어 수준으로 동작하므로 플랫폼에 관계없이 동일하게 실행됨
```bash
python -m py_compile hello.py
# → __pycache__/hello.cpython-311.pyc 생성됨
```
---
### Python Virtual Machine (PVM)
PVM은 바이트코드를 하나씩 읽어 해석하고 실행하는 엔진임. **스택 기반 가상 머신** 구조로 동작하며, 각 명령어는 `opcode + 인자(argument)` 구조로 이루어짐.
- 명령어가 실행될 때마다 스택에 값을 push/pop하며 연산이 진행됨
- `dis.dis(함수명)` 으로 함수의 바이트코드 명령어 목록을 확인할 수 있음
---
### Python 실행 파이프라인 전체 정리
소스코드를 바이트코드로 컴파일한 뒤 PVM에서 실행하는 **하이브리드 방식**임. 이 과정을 이해하면 Python의 성능 특성과 `__pycache__` 가 왜 생성되는지에 대한 이유를 알 수 있음.
| 단계 | 처리 내용 | 관련 모듈 |
| --- | --- | --- |
| 1. 소스 코드 | `.py` 파일 → Lexer(어휘 분석) → Token 스트림 | 개발자가 만든 `.py` |
| 2. 파싱 | Token → AST() 생성, 문법 오류 감지 | `ast` 모듈 |
| 3. 컴파일 | AST → 바이트코드(`.pyc`) 생성, `__pycache__` 저장 | `py_compile` 모듈 |
| 4. PVM 실행 | 바이트코드를 opcode 단위로 해석/실행 (스택 기반) | CPython 인터프리터 |
| 5. 결과 반환 | 실행 결과 출력, 예외 처리 | 프로그램 종료 |
---
### Python 메모리 모델
Python의 모든 값은 **객체(object)** 로 표현됨. 각 객체는 내부적으로 `type`(자료형 정보), `refcount`(참조 수), `value`(데이터 값)의 메타정보를 포함함.
#### 메모리 관리 구조
| 영역 | 역할 |
| --- | --- |
| **Stack** | 함수 호출, 지역 변수 등 |
| **Heap** | 객체, 클래스 인스턴스, 리스트 등 |
| **Reference Counting + Garbage Collector** | 메모리 자동 해제 |
---
### Python 메모리 관리 전략
| 전략 | 설명 |
| --- | --- |
| **Reference Counting** | 객체마다 참조 수를 저장하며, 참조 수가 0이 되면 메모리에서 삭제 |
| **Cycle Detector** | 서로를 참조하는 순환 참조 탐지 후 수동 해제 |
| **GC 모듈** | `gc.collect()` 등으로 수동 개입 가능 |
---
### Python 시스템/성능 관련 팁
| 개념 | 설명 |
| --- | --- |
| `__pycache__` | 바이트코드 캐싱 디렉토리 |
| `sys.getrefcount()` | 특정 객체의 참조 수 확인 |
| `gc` 모듈 | 가비지 컬렉터 제어 |
| `dis` 모듈 | 바이트코드 분석 |
---
### 실행 구조 이해의 목적
Python 실행 구조를 이해하면 실무에서 마주치는 다양한 문제를 더 빠르고 정확하게 해결할 수 있음.
| 목적 | 내용 |
| --- | --- |
| 패키지 설치 오류 해결 | `pip install` 실패나 `ModuleNotFoundError` 발생 시, venv 활성화 여부와 인터프리터 경로를 알면 즉시 해결 가능 |
| 에러 메시지 독해력 | Traceback은 PVM 실행 스택을 보여주는 것임. 스택 구조를 알면 오류 원인을 파일·라인·표현식 단위로 추적 가능 |
| 성능 최적화의 출발점 | 바이트코드를 이해하면 왜 컴프리헨션이 빠른지, 왜 Polars가 Pandas보다 빠른지를 직관적으로 납득할 수 있음 |
| 후속 과목 연결 | LangChain, RAG, AI Agent는 모두 Python 런타임 위에서 동작함. 환경 격리(venv)와 의존성 관리가 기본 전제임 |
---
### 제어문 (Control Flow Statements)
#### 조건문 — if / elif / else
특정 조건에 따라 실행할 코드 블록을 결정하는 구문임. 콜론(`:`)으로 조건문을 마무리하고, **들여쓰기**로 코드 블록을 구분함.
```python
if condition1:
    # 실행 코드
elif condition2:
    # 다른 조건
else:
    # 위 조건들 모두 거짓일 때 실행
```
- 조건식은 **bool 평가 가능 객체로 자동 변환**됨
- `None`, `0`, `""`, `[]`, `{}` 는 모두 **False**로 평가됨
- 조건문 안에서는 **Short-circuit Evaluation** 이 발생함 → `x`가 `None`이면 `x > 0` 은 평가 자체가 건너뜀
---
### \[참고\] Short-circuit Evaluation
논리 연산자 `and`, `or` 사용 시, **왼쪽 피연산자만 보고 전체 결과를 결정할 수 있으면 오른쪽은 평가하지 않고 건너뜀**.
| 연산자 | 동작 방식 |
| --- | --- |
| `and` | 왼쪽이 False → 전체는 무조건 False (오른쪽 생략) |
| `or` | 왼쪽이 True → 전체는 무조건 True (오른쪽 생략) |
```python
def left():
    print("left")
    return False

def right():
    print("right")
    return True

print(left() and right())  # 'right' 출력 안 됨
# → left()가 False니까 and 연산 전체도 False → right()는 호출조차 안 됨
```
---
### \[참고\] Short-circuit Evaluation — 실제 활용
| 패턴 | 코드 예시 | 설명 |
| --- | --- | --- |
| 조건 + 안전한 연산 결합 | `if user and user.is_active:` | `user`가 `None`이면 `.is_active` 접근 시 `AttributeError` 발생 → 단락 평가로 방지 |
| 성능 최적화 | `if expensive_check() and cheap_check():` | 비용이 큰 함수를 앞에 놓으면 cheap_check()를 먼저 쓰는 것이 손해 → 순서 주의 |
| None 방지 / 기본값 처리 | `value = config.get("key") or "default"` | 값이 없거나 falsy이면 `"default"` 반환 |
---
### \[참고\] Short-circuit Evaluation — 주의!
`and`/`or`는 항상 `bool`이 아닌 **원래 값을 반환**함.
```python
print([] or [1])   # [1]
print([] and [1])  # []
```
`[]`는 Falsy이므로 `or`에서 오른쪽 값인 `[1]`이 반환되고, `and`에서는 왼쪽 값인 `[]`가 바로 반환됨. 이 특성 때문에 `or`를 이용한 **디폴트값 처리** 패턴이 자주 사용됨.
---
### 조건문 (if) — 기본 개념
특정 조건이 참(True)일 때만 코드 블록이 실행되는 제어문임. 조건이 거짓(False)이면 해당 블록은 실행되지 않음.
#### 작성 시 주의사항
- 콜론(`:`)으로 조건문을 마무리
- **들여쓰기**로 코드 블록을 구분 (Python에서 들여쓰기는 문법적으로 필수)
- 논리 연산자(`and`, `or`, `not`)로 복잡한 조건 구성 가능
- `in` 키워드로 포함 여부 확인 가능
```python
if 조건:
    실행할 코드
```
---
### 조건문 (if) — 다양한 형태
```python
# 기본 if 문
age = 20
if age >= 18:
    print("성인입니다.")  # 실행됨

# if-else 문
age = 16
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else 문
age = 10
if age >= 18:
    print("성인입니다.")
elif age >= 13:
    print("청소년입니다.")
else:
    print("어린이입니다.")
```
---
### 조건문 (if) — 심화 활용
```python
# and, or, not 복합 조건
if age >= 18 and money >= 5000:
    print("영화를 볼 수 있습니다.")

if age >= 18 or student_card:
    print("학생 할인 가능합니다.")

if not vip:
    print("VIP가 아닙니다.")

# in / not in
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("바나나가 있습니다.")
if "grape" not in fruits:
    print("포도가 없습니다.")

# 한 줄 조건부 표현식 (삼항 연산자)
status = "성인" if age >= 18 else "미성년자"

# pass 문 — 아직 코드를 작성하지 않았지만 오류 방지
if age >= 18:
    pass
```
---
### 조건문 (if) — 문법 요약
| 조건문 | 설명 |
| --- | --- |
| `if` | 조건이 참(True)일 때 실행 |
| `if-else` | 조건이 거짓(False)일 때 실행할 코드 포함 |
| `if-elif-else` | 여러 개의 조건을 처리할 때 사용 |
| `and, or, not` | 여러 조건을 조합할 때 사용 |
| `in, not in` | 리스트, 문자열에서 값이 포함되어 있는지 확인 |
| `if` 한 줄 쓰기 | `value = "값" if 조건 else "다른 값"` |
| `pass` | 실행할 코드가 없을 때 자리 표시용으로 사용 |
| 중첩 `if` | `if` 문 안에 또 다른 `if` 문 작성 가능 |
---
### 연산자
#### 산술 / 비교 / 논리 연산자
| 구분 | 연산자 | 설명 |
| --- | --- | --- |
| 산술 | `+`, `-`, `*`, `/` | 사칙연산 |
|  | `//` | 몫 |
|  | `%` | 나머지 |
|  | `**` | 제곱 |
| 비교 | `==` | 같음 |
|  | `!=` | 다름 |
|  | `>`, `<`, `>=`, `<=` | 초과, 미만, 이상, 이하 |
| 논리 | `and` | 두 조건이 모두 참이면 True |
|  | `or` | 둘 중 하나라도 참이면 True |
|  | `not` | 참이면 거짓, 거짓이면 참 |
#### 유의사항
- `a == b`는 **값 비교**, `a is b`는 **객체 ID 비교** (동일 객체 여부)
- 비트 연산은 메모리 구조/하드웨어 다룰 때 중요
- 정수는 내부적으로 **immutable** 이므로 연산 시 **새 객체가 생성**됨
```python
a = 10
b = a
print(a is b)  # True — 같은 객체를 참조
a += 1
print(a is b)  # False — a는 새 객체, b는 원래 객체
```
---
### 반복문 (Loops)
같은 코드를 여러 번 실행할 때 사용하는 제어 구문임. `for`와 `while`이 대표적임.
```python
for 변수 in 반복할_데이터:
    실행할 코드

while 조건:
    실행할 코드
```
- `for` 문: 리스트, 튜플, 문자열, `range` 객체, `zip`, `enumerate` 등 **iterable 객체**를 순회할 때 사용
- `while` 문: 조건이 False가 될 때까지 반복
- `break`, `continue`, `else` 문도 반복문 안에서 사용 가능
```python
# for-else: break 없이 루프가 정상 종료된 경우에만 else 실행
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("정상 종료")  # break 없이 끝나야 실행
```
---
### 반복문(for) — 사용법 및 예시
```python
# 기본 예제 — 리스트 순회
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print(fruit)

# range() 활용
for i in range(5):      # 0~4 반복 (5번)
    print(i)
for i in range(2, 6):   # 2~5
    print(i)
for i in range(1, 10, 2):  # 1~9, 2씩 증가
    print(i)

# for 문을 사용한 합 구하기
total = 0
for i in range(1, 6):  # 1부터 5까지 합
    total += i         # total = total + i 와 동일
print("합:", total)

# enumerate() — 인덱스와 값을 동시에 가져옴
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
---
### 반복문(while) — 사용법 및 예시
`while` 문은 **조건이 참인 동안 반복**하며, 조건이 False가 되면 루프를 빠져나옴. 루프 내에서 조건 변경 로직을 빠뜨리면 **무한 루프**에 빠질 수 있어 주의해야 함.
```python
# 기본 예제
count = 0
while count < 5:
    print(count)
    count += 1  # 이 줄이 없으면 무한 루프

# while 문을 사용한 합 구하기
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print("합:", total)  # 결과: 15
```
`for` 문과 결과는 동일하지만, `while`은 반복 횟수가 정해지지 않고 **조건에 따라 반복**할 때 적합함.
---
### 반복문 제어 — break / continue
```python
# break — 반복문 강제 종료
for i in range(10):
    if i == 5:
        break      # i가 5일 때 반복문 종료
    print(i)       # 0, 1, 2, 3, 4 출력

# continue — 해당 반복만 건너뛰고 계속 실행
for i in range(5):
    if i == 2:
        continue   # i가 2일 때만 건너뜀
    print(i)       # 0, 1, 3, 4 출력
```
---
### 반복문 (for, while) — 정리
| 개념 | 설명 |
| --- | --- |
| `for` 문 | 리스트, 문자열, `range()` 등을 순회할 때 사용 |
| `while` 문 | 특정 조건이 참일 동안 반복 |
| `break` | 반복문을 강제로 종료 |
| `continue` | 특정 조건에서만 해당 반복 건너뛰기 |
| `range(n)` | 0부터 n-1까지 숫자 생성 |
| `enumerate()` | 리스트에서 인덱스와 값을 동시에 가져옴 |
---
### 고급 반복 제어 기법
#### 리스트 컴프리헨션
반복문을 한 줄로 축약하는 문법임.
```python
squares = [x*x for x in range(10) if x % 2 == 0]
```
#### 제너레이터 기반 반복 (yield)
`yield`는 단순한 `return`과 달리 **제너레이터(generator)** 라는 특별한 객체를 만드는 핵심 개념임. 함수의 실행을 잠시 멈췄다가 나중에 다시 이어서 실행할 수 있게 만드는 키워드로, **함수 ↔ 반복 가능한 객체**로 변환시킴.
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```
---
### \[참고\] List Comprehension — 리스트 컴프리헨션
기본 `for` 문을 대괄호 `[]` 안에 축약하는 문법임. 조건 추가, 요소 변환, 중첩 `for` 문도 모두 한 줄로 표현 가능함.
```python
# 기본 for 문 vs 리스트 컴프리헨션
numbers = [i for i in range(1, 6)]  # [1, 2, 3, 4, 5]

# 조건 추가
even_numbers = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]

# 조건부 표현식 포함
result = ["짝수" if i % 2 == 0 else "홀수" for i in range(1, 6)]
# ['홀수', '짝수', '홀수', '짝수', '홀수']

# 요소 변환
upper_words = [word.upper() for word in ["apple", "banana", "cherry"]]
# ['APPLE', 'BANANA', 'CHERRY']

# 중첩 for 문 (이중 리스트)
pairs = [(x, y) for x in range(1, 3) for y in range(3, 5)]
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```
---
### \[참고\] Dictionary / Set Comprehension
#### 딕셔너리 컴프리헨션
```python
# 기본 생성
squares = {i: i ** 2 for i in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건 추가
even_squares = {i: i ** 2 for i in range(1, 6) if i % 2 == 0}
# {2: 4, 4: 16}

# 기존 딕셔너리 변형 (할인 적용)
fruit_prices = {"apple": 1000, "banana": 500, "cherry": 2000}
discount_prices = {fruit: price * 0.9 for fruit, price in fruit_prices.items()}

# 두 리스트를 딕셔너리로 변환 (zip 활용)
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
person = {k: v for k, v in zip(keys, values)}
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
```
#### 집합 컴프리헨션
리스트/딕셔너리 컴프리헨션과 유사하나, **중복을 자동으로 제거**함.
```python
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_squares = {num ** 2 for num in numbers}
# {1, 4, 9, 16, 25}
```
---
### 리스트 vs 딕셔너리 컴프리헨션 — 정리
| 개념 | 예제 | 설명 |
| --- | --- | --- |
| 리스트 생성 | `[i for i in range(5)]` | `[0, 1, 2, 3, 4]` |
| 리스트 + 조건 | `[i for i in range(10) if i % 2 == 0]` | `[0, 2, 4, 6, 8]` |
| 리스트 + 변환 | `[word.upper() for word in words]` | 모든 단어 대문자로 변환 |
| 딕셔너리 생성 | `{i: i**2 for i in range(5)}` | `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}` |
| 딕셔너리 + 조건 | `{i: i**2 for i in range(5) if i % 2 == 0}` | 짝수만 포함 |
| 딕셔너리 변환 | `{k: v*2 for k, v in dict.items()}` | 값 2배 증가 |
---
### list — 가변 순차 자료형
순서 있음, 중복 허용, 인덱싱/슬라이싱 가능, 요소 수정 가능한 **가변(mutable)** 자료형임. 내부 구조는 **동적 배열(array list)** 로 구현됨.
#### 시간 복잡도
| 연산 | 복잡도 |
| --- | --- |
| 접근 | O(1) |
| 중간 삽입/삭제 | O(n) |
| 맨 뒤에 삽입 (`append`) | O(1) amortized |
```python
a = [1, 2, 3]
a.append(4)      # O(1)
a.insert(1, 100) # O(n)
print(a[2])      # O(1)
```
---
### tuple — 불변 순차 자료형
리스트와 유사하지만 **불변(immutable)** 이므로 생성 후 요소 변경이 불가능함.
- 해싱 가능한 데이터로 사용 → **dict 키나 set 요소**로 활용 가능
- 메모리 사용량이 적고, 리스트보다 **빠른 시간 복잡도**
```python
b = (1, 2, 3)
# b[0] = 10  # 오류 발생
```
---
### set — 중복 불가, 순서 없는 집합
**해시 기반(hash table)** 자료구조로 중복을 자동 제거함.
- 주요 연산: 합집합 `|`, 교집합 `&`, 차집합
- 삽입/삭제/탐색 모두 **O(1)**
```python
s = {1, 2, 3}
s.add(4)      # O(1)
s.remove(2)   # O(1)
print(3 in s) # True
```
---
### dict — 키-값 쌍 해시맵
**해시 테이블** 기반의 Key-Value 자료구조임.
- 키는 **해시 가능한 객체(immutable)** 만 사용 가능
- **Python 3.7+부터 삽입 순서 보장**
- 조회 및 삽입: **O(1)**
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d['a'])  # O(1)
```
---
### deque (from collections) — 양방향 큐
`collections.deque`는 **리스트보다 양 끝 삽입/삭제가 빠른** 자료구조임. 큐(Queue), 스택(Stack), 슬라이딩 윈도우 등에 활용됨. 내부는 **Doubly Linked List** 구조로 구현됨.
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)      # 오른쪽에 추가
dq.appendleft(0)  # 왼쪽에 추가
dq.pop()          # 오른쪽 제거
dq.popleft()      # 왼쪽 제거
```
---
### \[참고\] Doubly Linked List vs Python deque 내부 구현
`deque`는 단순한 Doubly Linked List가 아니라 **"linked list of arrays"** 구조임. 각 블록이 일정 크기의 배열이고 이 블록들이 양방향으로 연결되어, **cache-friendly하면서도 O(1) 성능을 보장**함.
| 항목 | Doubly Linked List | Python deque 내부 구현 |
| --- | --- | --- |
| 구조 | node가 앞뒤로 연결 | 고정 크기의 배열 블록들을 앞뒤로 연결 |
| 구현 | Python 직접 구현 시 사용 | C로 구현된 deque object에서 실행 |
| 장점 | 삽입/삭제는 빠르나 접근은 느림 | 양쪽 O(1) 삽입/삭제 + 블록 기반으로 접근도 효율적 |
| 사용처 | 커스텀 자료구조 학습용 | 실전 성능 최적화된 Queue/Stack 용도 |
---
### 고급 자료구조 (Python Advanced Data Structures)
기본 자료구조(List, Tuple, Dictionary, Set)만으로 해결하기 어려운 경우, `collections` 모듈의 고급 자료구조를 활용하면 더 빠르고 효율적인 데이터 관리가 가능함.
주요 모듈: `Deque`, `Counter`, `OrderedDict`, `defaultdict`
---
### collections 모듈 활용 — deque / Counter
#### deque (빠른 삽입/삭제가 가능한 리스트)
리스트의 `append()`/`pop()`은 O(1)이지만, **앞쪽에서 삽입/삭제 시 O(n)** 의 성능 저하가 발생함. `deque`는 양쪽 끝에서 삽입/삭제가 O(1)으로 매우 빠름.
```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)      # 오른쪽 추가
queue.appendleft(0)  # 왼쪽 추가
queue.pop()          # 오른쪽 제거
queue.popleft()      # 왼쪽 제거
```
사용 사례: 웹 브라우저 뒤로 가기 기능
#### Counter (요소 개수 세기)
리스트, 튜플, 문자열에서 각 요소의 개수를 자동으로 세어주는 딕셔너리임.
```python
from collections import Counter

text = "hello world"
count = Counter(text)
# {'l': 3, 'o': 2, ' ': 1, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
```
사용 사례: 단어 빈도수 분석, 로그 데이터 분석
---
### collections 모듈 활용 — OrderedDict / defaultdict
#### OrderedDict (순서 유지하는 딕셔너리)
Python 3.6 이상에서는 기본 딕셔너리도 순서를 유지하지만, `OrderedDict`는 **모든 버전에서 순서 유지**를 보장함. 사용 사례: JSON 데이터 저장, 데이터 정렬.
```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['apple'] = 5
ordered_dict['banana'] = 2
ordered_dict['orange'] = 3
# OrderedDict([('apple', 5), ('banana', 2), ('orange', 3)])
```
#### defaultdict (기본값을 자동으로 설정하는 딕셔너리)
존재하지 않는 키를 조회할 때 `KeyError` 대신 **기본값을 자동으로 생성**함. 그룹핑, 카운팅, 그래프 알고리즘에 유용함.
```python
from collections import defaultdict

word_count = defaultdict(int)  # 기본값 0
word_count["apple"] += 1
word_count["banana"] += 2
# {'apple': 1, 'banana': 2}
```
---
### heapq (힙: 우선순위 큐)
**최소/최대 값을 빠르게 찾는** 자료구조임. `heapq`는 기본적으로 **최소 힙(min-heap, 최솟값이 루트)** 을 지원함. `heappush()`와 `heappop()`은 **O(log N)** 의 성능을 가짐.
```python
import heapq

# 최소 힙
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
print(heapq.heappop(heap))  # 1 (가장 작은 값)
print(heapq.heappop(heap))  # 2

# 최대 힙 (값을 음수로 저장)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -10)
print(-heapq.heappop(max_heap))  # 10
print(-heapq.heappop(max_heap))  # 5
```
최소 힙 사용 사례: 다익스트라 알고리즘(최단 경로), 우선순위 작업 스케줄링. 최대 힙 사용 사례: 가장 높은 점수 찾기, 데이터 정렬.
---
### bisect (이진 탐색을 활용한 정렬된 리스트 관리)
**정렬된 리스트에서 특정 값을 빠르게 찾거나 삽입**하는 라이브러리임. **O(log N)** 의 성능을 가지며 매우 빠른 탐색이 가능함.
```python
import bisect

numbers = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(numbers, 6)  # 6이 들어갈 위치 찾기
print(pos)  # 3 (index)

bisect.insort(numbers, 6)  # 리스트에 삽입 후 자동 정렬
print(numbers)  # [1, 3, 5, 6, 7, 9]
```
사용 사례: 정렬된 리스트에서 빠른 검색, 자동 정렬 데이터 저장.
---
### 고급 자료 구조 비교표
| 자료구조 | 모듈 | 특징 | 사용 예제 |
| --- | --- | --- | --- |
| `deque` | collections | 빠른 삽입/삭제 O(1) | 웹 브라우저 기록 |
| `Counter` | collections | 요소 개수 카운팅 | 단어 빈도 분석 |
| `OrderedDict` | collections | 삽입 순서 유지 | JSON 데이터 처리 |
| `defaultdict` | collections | 기본값 자동 설정 | 그래프 알고리즘 |
| `heapq` | heapq | 우선순위 큐 O(log N) | 다익스트라 알고리즘 |
| `bisect` | bisect | 정렬된 리스트 이진 탐색 O(log N) | 빠른 검색 |
| `set` | 내장 | 중복 제거, 집합 연산 | 데이터 필터링 |
---
### defaultdict (from collections) — 초기값을 자동 제공하는 딕셔너리
존재하지 않는 키 접근 시 **KeyError 대신 기본값을 자동으로 생성**함. 그룹핑, 카운팅 등에 유용함.
```python
from collections import defaultdict

dd = defaultdict(list)        # list() → 기본값은 빈 리스트 []
dd['a'].append(1)             # 'a'가 없으므로 dd['a'] = [] 후 append
dd['a'].append(2)             # dd['a']는 이제 [1], 거기에 2 추가 → [1, 2]
print(dd)
# defaultdict(<class 'list'>, {'a': [1, 2]})
```
---
### Counter (from collections) — 요소 개수 세기
**dict 기반 빈도 수 계산** 자료구조임. 통계, 자연어 처리 등에 활용됨.
```python
from collections import Counter

cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(cnt)          # Counter({'a': 3, 'b': 2, 'c': 1})
print(cnt['a'])     # 3
print(cnt.most_common(2))  # [('a', 3), ('b', 2)]
```
`most_common(n)` 메서드는 **가장 많이 등장한 n개의 요소**를 `(요소, 개수)` 튜플의 리스트로 반환함.
---
### \[Why?\] 리스트 앞쪽 삽입/삭제 시 O(n) 성능 저하 이유
리스트는 **동적 배열(Dynamic Array)** 구조이므로 끝에서 추가/제거는 O(1)로 빠름. 그러나 앞쪽에서 삽입/삭제하면 **모든 요소가 한 칸씩 이동**해야 하므로 요소가 많을수록 성능이 크게 저하됨.
```python
my_list = [1, 2, 3]

# 끝 추가/삭제 → O(1)
my_list.append(4)   # 배열 끝에 바로 저장
my_list.pop()       # 마지막 요소 제거

# 앞쪽 추가/삭제 → O(n)
my_list.insert(0, 0)  # 모든 요소가 한 칸씩 뒤로 이동
my_list.pop(0)        # 모든 요소가 한 칸씩 앞으로 이동
```
`O(1)`은 입력 크기에 관계없이 연산 시간이 **일정한 상수 시간(Constant Time)** 을 의미함.
---
### \[참고\] deque는 양쪽 끝에서 삽입/삭제가 O(1)이다
`collections.deque`는 이중 연결 리스트 형태로 **양쪽 끝 삽입/삭제 시 O(1)** 을 유지함. 연결 리스트 구조이므로 요소 추가/삭제 시 다른 요소를 이동시킬 필요가 없음.
#### O(1) vs O(n) 비교
| 연산 | 수행시간 | 설명 |
| --- | --- | --- |
| `append()` | O(1) | 항상 리스트 끝에 추가하므로 실행시간 일정 |
| `pop()` | O(1) | 항상 리스트 끝에서 삭제하므로 실행시간 일정 |
| `insert(0, value)` | O(n) | 리스트 앞에 추가하면 모든 요소가 이동 |
| `pop(0)` | O(n) | 리스트 앞에서 삭제하면 모든 요소가 이동 |
---
### \[참고\] O(log N)
데이터의 크기(N)가 증가해도 연산 시간이 **아주 천천히 증가**하는 효율적인 알고리즘임. 매 단계마다 데이터 크기가 절반으로 감소하는 구조로, 이진 탐색, 힙, 균형 이진 트리(BST) 등이 대표적임.
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # 중간 값 찾기
        if arr[mid] == target:
            return mid             # 찾으면 위치 반환
        elif arr[mid] < target:
            left = mid + 1         # 오른쪽 탐색 (데이터 절반 제거)
        else:
            right = mid - 1        # 왼쪽 탐색 (데이터 절반 제거)
    return -1                      # 값이 없으면 -1 반환

numbers = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numbers, 7))   # 3 (index)
```
---
### \[참고\] zip()
여러 개의 리스트(또는 튜플)를 **하나의 튜플 묶음으로 반환**하는 내장 함수임.
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# 두 리스트 묶기
zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# for 문과 함께 사용
for name, age in zip(names, ages):
    print(f"{name}의 나이는{age}살입니다.")
```
---
### \[참고\] zip()을 활용한 다양한 예제
```python
# 딕셔너리 생성
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
person = dict(zip(keys, values))
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}

# 언패킹 — zip(*리스트)로 튜플을 다시 개별 리스트로 분리
pairs = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*pairs)
# names: ('Alice', 'Bob', 'Charlie'), ages: (25, 30, 35)

# 점수 기준 학생 정렬
students = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 95]
sorted_students = [name for name, _ in sorted(zip(scores, students), reverse=True)]
# ['Charlie', 'Alice', 'Bob']
```
---
### \[참고\] zip() 사용 시 주의 사항 — 길이가 다른 리스트
`zip()`은 **짧은 리스트 기준으로 맞춰** 짝이 맞는 요소까지만 묶으며, 나머지는 버림.
```python
a = [1, 2, 3]
b = ["one", "two"]
print(list(zip(a, b)))  # [(1, 'one'), (2, 'two')] ← 3은 짝이 없어서 제외됨
```
부족한 값을 채우고 싶다면 `itertools.zip_longest()` 사용함.
```python
from itertools import zip_longest
print(list(zip_longest(a, b, fillvalue="없음")))
# [(1, 'one'), (2, 'two'), (3, '없음')]
```
---
### \[참고\] zip() 핵심 정리
| 기능 | 사용법 | 결과 |
| --- | --- | --- |
| 리스트 묶기 | `zip([1, 2], ['a', 'b'])` | `[(1, 'a'), (2, 'b')]` |
| `for` 문과 사용 | `for x, y in zip(a, b):` | 여러 리스트 동시 순회 |
| 딕셔너리 변환 | `dict(zip(keys, values))` | `{key: value, ...}` |
| 언패킹 | `zip(*zipped_list)` | 리스트 다시 분리 |
| 정렬 | `sorted(zip(scores, names))` | 특정 기준으로 정렬 |
| 길이 맞추기 | `zip_longest(a, b, fillvalue=0)` | 부족한 값 fillvalue로 채움 |
---
### \[참고\] zip_longest()
`zip()`의 확장 버전으로, **리스트 길이가 다를 때 짧은 리스트를 fillvalue로 자동으로 채워줌**. `itertools` 모듈에서 제공하므로 `import itertools` 필요함.
```python
from itertools import zip_longest

zip_longest(리스트1, 리스트2, ..., fillvalue=채울값)
```
---
### \[참고\] zip() vs zip_longest() 차이점
| 기능 | `zip()` | `zip_longest()` |
| --- | --- | --- |
| 리스트 길이 다를 때 | 짧은 리스트 기준으로 맞춤 | 긴 리스트 기준으로 맞추고 부족한 부분 채움 |
| 기본 동작 | `zip([1,2,3], ['a','b'])` → `[(1,'a'),(2,'b')]` | `zip_longest([1,2,3], ['a','b'], fillvalue='X')` → `[(1,'a'),(2,'b'),(3,'X')]` |
| `fillvalue` | 없음 | 기본값 설정 가능 |
| 딕셔너리 변환 | `dict(zip(keys, values))` | `dict(zip_longest(keys, values, fillvalue='Unknown'))` |
---
### \[참고\] zip_longest() 다양한 활용
```python
from itertools import zip_longest

# 여러 리스트를 같은 길이로 맞추기
names = ["Alice", "Bob"]
scores = [90, 85, 80]
result = list(zip_longest(names, scores, fillvalue="정보 없음"))
# [('Alice', 90), ('Bob', 85), ('정보 없음', 80)]

# 딕셔너리 변환 시 활용
keys = ["name", "age"]
values = ["Alice"]
person = dict(zip_longest(keys, values, fillvalue="Unknown"))
# {'name': 'Alice', 'age': 'Unknown'}
```
---
### \[참고\] zip_longest() 다양한 활용 — CSV 데이터 정렬
데이터가 일부 비어 있는 경우, `zip_longest()`를 사용하면 자동으로 `None` 또는 기본값을 채울 수 있음.
```python
from itertools import zip_longest

columns = ["이름", "나이", "도시"]
rows = [
    ["Alice", 25],
    ["Bob", 30, "Seoul"],
    ["Charlie"]
]

formatted_rows = [list(zip_longest(columns, row, fillvalue="정보 없음")) for row in rows]
for row in formatted_rows:
    print(dict(row))

# {'이름': 'Alice', '나이': 25, '도시': '정보 없음'}
# {'이름': 'Bob', '나이': 30, '도시': 'Seoul'}
# {'이름': 'Charlie', '나이': '정보 없음', '도시': '정보 없음'}
```
---
### \[참고\] zip_longest() 핵심 정리
| 기능 | `zip()` | `zip_longest()` |
| --- | --- | --- |
| 리스트 길이 다를 때 | 짧은 리스트 기준으로 맞춤 | 긴 리스트 기준으로 맞추고 부족한 부분 채움 |
| 기본 동작 예시 | `[(1,'a'),(2,'b')]` | `[(1,'a'),(2,'b'),(3,'X')]` |
| `fillvalue` | 없음 | 기본값 설정 가능 (`fillvalue="없음"`) |
| 딕셔너리 변환 | `dict(zip(keys, values))` | `dict(zip_longest(keys, values, fillvalue='Unknown'))` |
---
### 문자열 슬라이싱 (Slicing)
인덱스를 사용하여 문자열의 특정 부분을 추출하는 방법임. `str[start:end:step]` 형태로 사용하며, **끝 인덱스(end)는 결과에 포함되지 않음**.
```python
text = "Hello, Python!"

print(text[0:5])   # 'Hello'       (0번~4번 인덱스)
print(text[:5])    # 'Hello'       (처음부터 5번째까지)
print(text[7:])    # 'Python!'     (7번째부터 끝까지)
print(text[:])     # 'Hello, Python!'  (전체 복사)
print(text[::2])   # 'Hlo yhn'    (2칸씩 건너뛰기)
print(text[::-1])  # '!nohtyP ,olleH'  (문자열 뒤집기)
```
---
### 문자열 포맷팅 (Formatting)
변수나 값을 문자열에 삽입하는 방법으로, 세 가지 방식이 있음.
```python
name = "Alice"
age = 25

# % 연산자 (옛날 방식) — %s: 문자열, %d: 정수, %f: 실수
print("이름:%s, 나이:%d" % (name, age))

# format() 메서드 (Python 3부터)
print("이름:{}, 나이:{}".format(name, age))
print("이름:{0}, 나이:{1}".format(name, age))   # 인덱스 사용
print("이름:{name}, 나이:{age}".format(name=name, age=age))  # 키워드 사용

# f-string (가장 현대적인 방법, Python 3.6 이상)
print(f"이름:{name}, 나이:{age}")
```
---
### 슬라이싱 기본 문법 및 Formatting 상세
#### f-string 고급 활용 (Python 3.6 이상)
간단한 연산, 소수점 자리수 지정, 정렬/공백 추가가 모두 가능함.
```python
# 연산 삽입
a, b = 5, 3
print(f"5 + 3 ={a + b}")  # 5 + 3 = 8

# 소수점 자리 지정
pi = 3.14159
print(f"파이 값:{pi:.2f}")  # 파이 값: 3.14

# 정렬/공백 지정
text = "Python"
print(f"[{text:>10}]")  # 오른쪽 정렬 (10칸)
print(f"[{text:<10}]")  # 왼쪽 정렬 (10칸)
print(f"[{text:^10}]")  # 가운데 정렬 (10칸)
```
---
### 제너레이터 — 대용량 메모리 효율 처리
**제너레이터**는 `yield` 키워드를 사용해 값을 하나씩 생성하고 일시 중단함. 전체 데이터를 한꺼번에 메모리에 올리지 않으므로, **CSV 수백만 행 스트리밍 처리**에 핵심적으로 활용됨.
```python
# 제너레이터 함수 — CSV 행 단위 처리
def read_rows(path):
    with open(path) as f:
        next(f)  # 헤더 스킵
        for line in f:
            yield line.strip().split(',')

# 메모리 절약: 한 번에 한 행씩
for row in read_rows('large.csv'):
    process(row)

# generator expression — () 괄호 사용
total = sum(float(r[2]) for r in read_rows('f.csv'))

# 리스트 vs 제너레이터 메모리 비교
import sys
lst = [x**2 for x in range(10_000_000)]  # 400MB+
gen = (x**2 for x in range(10_000_000))  # ~120 byte
```
`itertools.islice` / `chain` 등과도 조합 가능함.
---
### dataclass · TypedDict — 데이터 레코드 모델링
#### dataclass
`@dataclass` 데코레이터를 사용하면 클래스 보일러플레이트(`__init__`, `__repr__`, `__eq__`)를 **자동으로 생성**함. `field()`로 기본값 및 팩토리를 설정할 수 있음.
#### TypedDict
`dict`에 **타입 힌트를 추가**하여 Pandas DataFrame 행을 타입 안전하게 표현할 때 활용함.
```python
from dataclasses import dataclass, field
from typing import TypedDict, Optional

@dataclass
class SalesRecord:
    date: str
    region: str
    amount: float
    tags: list = field(default_factory=list)

r = SalesRecord('2024-01', '서울', 1500.0)
print(r)  # SalesRecord(date='2024-01', ...)

# TypedDict: dict에 타입 힌트
class Row(TypedDict):
    region: str
    sales: float
    category: Optional[str]
```
---
### 자료구조가 데이터 분석 코드의 기반인 이유
| 연결 | 내용 |
| --- | --- |
| DataFrame은 dict의 확장 | Pandas DataFrame 내부는 `dict[컬럼명 → numpy 배열]` 구조임. `dict`를 이해하면 Pandas 동작 원리가 보임 |
| 컴프리헨션 = 빠른 전처리 | 필터링·변환을 한 줄로 표현 가능. Pandas `apply` 대비 간단한 변환은 컴프리헨션이 더 빠를 때도 있음 |
| Counter로 value_counts 대체 | Pandas 없이도 `Counter` 하나로 빈도 집계 가능. 스크립트 레벨 분석에서 의존성 최소화 |
| 제너레이터 = 스트리밍 파이프라인 | 수백만 행 CSV를 한꺼번에 올리지 않고 행 단위로 처리. 메모리 한계를 극복하는 핵심 패턴 |
---
### 함수 정의와 호출
- 함수(function)란 특정 작업을 수행하는 코드 블록으로, 한 번 정의해두면 필요할 때마다 재사용할 수 있음.
#### 기본 문법
`def` 키워드로 함수를 정의하며, 구조는 아래와 같음.
```python
def 함수이름(매개변수):
    # 함수 내용
    return 결과
```
정의한 함수는 `함수이름(인자)` 형태로 호출함. 호출 시 반환값을 변수에 받아 활용할 수 있음.
```python
def greet(name):
    return f"안녕하세요,{name}님!"

message = greet("철수")
print(message)  # 출력: 안녕하세요, 철수님!
```
---
#### 매개변수와 반환값
#### 매개변수 (Parameters)
함수는 \*\*매개변수(parameter)\*\*를 통해 외부에서 값을 입력받아 동작함. 호출 시 전달하는 값이 매개변수에 바인딩됨.
```python
def greet(name):
    return f"안녕하세요,{name}님!"

print(greet("철수"))  # 출력: 안녕하세요, 철수님!
# name이라는 매개변수를 받아서 문자열을 반환하는 함수
```
#### 반환값 (Return Value)
`return` 키워드로 함수 실행 결과를 외부로 내보낼 수 있음. **반환값이 없으면 기본값으로 ****`None`****이 반환됨.**
```python
def add(a, b):
    return a + b  # 결과 반환

result = add(3, 5)
print(result)  # 출력: 8
# return을 사용하면 함수의 결과값을 외부에서 활용 가능
```
---
#### 매개변수의 기본값 설정
함수 정의 시 매개변수에 \*\*기본값(default value)\*\*을 지정할 수 있음. 호출 시 해당 인자를 생략하면 기본값이 자동으로 사용됨.
```python
def introduce(name, age=20):
    print(f"이름:{name}, 나이:{age}")

introduce("영희")        # 출력: 이름: 영희, 나이: 20
introduce("철수", 25)    # 출력: 이름: 철수, 나이: 25
# age=20이 기본값이므로 introduce("영희")처럼 호출해도 정상 작동
```
#### 기본값 인자의 위치 규칙
기본값이 있는 인자는 **반드시 뒤쪽에** 위치해야 함. 앞에 오면 SyntaxError가 발생함.
```python
# 오류 발생! (기본값 있는 인자는 뒤에 와야 함)
def wrong_example(age=20, name):
    print(f"이름:{name}, 나이:{age}")

# 올바른 예시: 기본값 있는 인자를 마지막에 배치
def correct_example(name, age=20):
    print(f"이름:{name}, 나이:{age}")
```
---
#### 함수 고급 패턴 — `args`, `*kwargs`, 클로저
| 패턴 | 설명 |
| --- | --- |
| `*args` | 가변 위치 인자 — 여러 개의 값을 **튜플**로 받음 |
| `**kwargs` | 가변 키워드 인자 — 여러 개의 키=값 쌍을 **딕셔너리**로 받음 |
| 클로저 | 내부 함수가 외부 함수의 변수를 기억하는 구조 |
| `lambda` | 한 줄짜리 간단한 익명 함수 |
| `functools.partial` | 기존 함수의 인자 일부를 고정해 새 함수를 생성 |
```python
# *args, **kwargs 동시 사용
def agg(*args, **kwargs):
    print(f'값:{args}')    # tuple
    print(f'옵션:{kwargs}') # dict
agg(1, 2, 3, method='mean')

# 클로저: 외부 변수 기억
def make_multiplier(n):
    def multiply(x): return x * n  # n 기억
    return multiply
double = make_multiplier(2)
double(5)  # 10

# partial: 인자 고정
from functools import partial
def scale(x, factor): return x * factor
double2 = partial(scale, factor=2)
list(map(double2, [1,2,3,4]))  # [2,4,6,8]
```
---
#### 가변 인자 — `args` (위치 기반)
함수를 호출할 때 몇 개의 인자를 받을지 미리 정할 수 없을 때 \*\*`*args`\*\*를 사용함. 전달된 인자들은 모두 \*\*튜플(tuple)\*\*로 묶여서 함수 내부에 전달됨.
python
```python
def sum_numbers(*args):  # 여러 개의 숫자를 받을 수 있음
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 출력: 15
print(sum_numbers(10, 20))          # 출력: 30
# sum_numbers(1, 2, 3, 4, 5) → args = (1, 2, 3, 4, 5) 튜플로 저장
```
`for` 문으로 `*args`를 순회 처리할 수 있음.
```python
def print_names(*args):
    for name in args:
        print(f"이름:{name}")

print_names("철수", "영희", "민수")
# 이름: 철수 / 이름: 영희 / 이름: 민수
```
#### 가변 인자 — `*kwargs` (키워드 기반)
- \*`*kwargs`\*는 키워드 인자(`키=값` 형태)를 여러 개 받아 **딕셔너리**로 저장함.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_info(name="철수", age=25, hobby="축구")
# kwargs = {'name': '철수', 'age': 25, 'hobby': '축구'} 딕셔너리로 저장
```
- `*kwargs`도 `for key, value in kwargs.items():`로 순회 처리 가능함.
---
#### `args`와 `*kwargs` 혼합 사용
- `args`가 먼저, `*kwargs`가 나중에 오는 순서는 **반드시 지켜야 함**. 인자 선언 순서는 아래와 같음.
> 일반 인자 → `*args` → `**kwargs`
```python
def mix_example(a, b, *args, **kwargs):
    print(f"a:{a}, b:{b}")
    print(f"args:{args}")    # 튜플
    print(f"kwargs:{kwargs}") # 딕셔너리

mix_example(1, 2, 3, 4, 5, name="철수", age=30)
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'name': '철수', 'age': 30}
```
순서를 어기면 SyntaxError가 발생함.
```python
# 오류 발생!
def wrong_example(a, b, **kwargs, *args):  # ❌
    pass
```
---
#### \[정리\] `args`, `*kwargs`
| 구분 | 설명 및 예시 |
| --- | --- |
| `*args` | 여러 개의 인자를 튜플(tuple)로 묶어서 함수에 전달. 개수 제한 없음 |
| `**kwargs` | 여러 개의 키워드 인자를 딕셔너리로 전달 |
- `args`는 정의뿐 아니라 **리스트/튜플 언패킹**에도 활용 가능함. 호출 시 `리스트`로 전달하면 요소가 각 위치 인자로 분해되어 전달됨.
```python
# 일반 *args — 튜플로 저장
def print_numbers(*args):
    print(args)

print_numbers(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)

# 리스트 언패킹으로 활용
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
result = multiply(*numbers)  # *numbers → 요소 각각을 a, b, c에 전달
print(result)  # 24
```
고정 인자와 `*args`를 함께 쓰면, 앞 인자가 먼저 채워지고 나머지가 `*args` 튜플로 들어감.
```python
def greet(message, *names):
    for name in names:
        print(f"{message},{name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# "Hello" → message, 나머지 → names = ("Alice", "Bob", "Charlie") 튜플
```
- `args`와 `*kwargs`를 함께 사용하면 위치 인자는 튜플로, 키워드 인자는 딕셔너리로 각각 분리되어 저장됨.
```python
def example_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 25}
```
---
### `def`와 일급 객체 (First-class Object)
Python의 함수는 일급 객체(First-class Object)임. 이는 함수를 일반 값처럼 다룰 수 있다는 의미로, 구체적으로는 아래 세 가지가 가능함.
- 변수에 할당 가능
- 다른 함수의 인자로 전달 가능
- 함수의 리턴값으로 사용 가능
```python
def add(a, b):
    return a + b

# 변수에 할당
f = add
print(f(10, 5))  # 15

# 함수 인자로 전달
def operate(func, x, y):
    return func(x, y)

print(operate(add, 3, 4))  # 7
```
`f = add`는 함수 객체 자체를 변수에 바인딩하는 것이며, `f(10, 5)`처럼 그대로 호출할 수 있음. `operate`처럼 함수를 인자로 받는 패턴은 고차함수의 기초가 됨.
---
### 람다함수 (Lambda)
**람다함수**는 한 줄로 간단하게 쓸 수 있는 익명 함수임. 짧고 단순한 기능을 즉석에서 정의할 때 사용하며, 복잡한 로직이 필요한 경우에는 일반 `def` 함수를 쓰는 것이 적합함.
| 구분 | 일반 함수 | 람다함수 |
| --- | --- | --- |
| 함수 정의 | `def add(x, y): return x + y` | `add = lambda x, y: x + y` |
| 호출 | `print(add(2, 3))` | `print(add(2, 3))` |
| 출력 | 5 | 5 |
람다함수가 자주 쓰이는 상황은 `map()`, `filter()`, `sort()` 등과 함께 쓸 때임.
```python
# 리스트 정렬 — 점수 기준
students = [("철수", 90), ("영희", 80), ("민수", 95)]
students.sort(key=lambda x: x[1])  # 두 번째 요소(점수)로 정렬
# 출력: [('영희', 80), ('철수', 90), ('민수', 95)]

# map() — 리스트의 모든 값 변환
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# 출력: [1, 4, 9, 16, 25]

# filter() — 특정 조건만 남기기
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# 출력: [2, 4, 6]
```
---
### 고차함수 (Higher-order Function)
**고차함수**란 다른 함수를 인자로 받거나, 함수를 결과로 반환하는 함수임. Python의 `map()`, `filter()`, `reduce()`가 대표적임.
#### 함수를 인자로 받는 경우
```python
def apply_function(func, value):
    return func(value)

double = lambda x: x * 2
print(apply_function(double, 10))  # 20
# double 함수(람다)를 apply_function에 전달하여 실행
```
#### 함수를 반환하는 경우
```python
def make_multiplier(n):
    return lambda x: x * n  # 배수를 반환하는 람다 함수

times3 = make_multiplier(3)  # 3배수 함수 생성
print(times3(5))  # 15
# make_multiplier(3)이 새로운 함수(lambda x: x * 3)를 반환
```
#### `map()`, `filter()`, `reduce()` 활용
```python
# map(): 리스트의 각 요소를 변환
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter(): 조건에 맞는 요소만 선택
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6]

# reduce(): 리스트의 값을 하나로 합침 (두 개씩 연산하며 최종 결과 반환)
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15
```
`reduce()`는 `functools`에서 임포트해야 하며, 리스트 요소를 왼쪽부터 두 개씩 누적 연산해 단일 값으로 축약함.
---
### 클로저 (Closure)
**클로저**는 내부 함수가 자신이 선언된 외부 함수의 변수를 기억하는 구조임. 외부 함수가 실행을 마친 뒤에도 내부 함수가 그 환경(변수)을 참조할 수 있음.
```python
def multiplier(factor):
    def multiply(x):
        return x * factor  # 외부 변수 factor를 기억
    return multiply

double = multiplier(2)
print(double(10))  # 20
# multiplier(2) 실행이 끝났어도 multiply는 factor=2를 기억하고 있음
```
`double = multiplier(2)`를 호출하면 `multiply` 함수 객체가 반환되고, 이 객체는 `factor=2`라는 환경을 클로저로 보존함. 이후 `double(10)`을 호출하면 기억해둔 `factor`를 이용해 `10 * 2 = 20`을 반환함.
---
### 제너레이터(Generator)와 `yield`
**제너레이터**는 이터레이터를 생성하는 함수임. `return` 대신 `yield`를 사용하며, `yield`는 값을 하나 내보낸 뒤 함수 실행을 일시 중단하고 상태를 저장함. 다음 호출 시 중단된 지점에서 이어서 실행됨.
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
# 출력: 5 4 3 2 1
```
`yield n`을 만나면 현재 `n` 값을 내보내고 일시 정지함. `for` 루프가 다음 값을 요청할 때마다 `n -= 1`부터 재개하여 다음 `yield`까지 실행함.
#### Generator vs List Comprehension
| 비교 항목 | List Comprehension | Generator |
| --- | --- | --- |
| 메모리 사용 | 전체를 한 번에 메모리에 저장 | 필요할 때 하나씩 생성 (lazy) |
| 반환 형태 | 리스트 객체 | 제너레이터 객체 |
| 구문 예시 | `[x*x for x in range(10)]` | `(x*x for x in range(10))` |
데이터가 매우 많을 때 리스트는 전체를 메모리에 올리지만, 제너레이터는 요소를 하나씩 생성하므로 **메모리 효율이 높음**.
---
### 내장 함수 활용 (Built-in Functions)
- 내장 함수(Built-in Functions)란 별도의 설치나 임포트 없이 Python에서 바로 사용할 수 있는 함수임.
#### 기본 내장 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `print()` | 출력 | `print("안녕하세요!")` → 안녕하세요! |
| `type()` | 데이터 타입 확인 | `type(10)` → `<class 'int'>`, `type("문자")` → `<class 'str'>` |
| `id()` | 변수의 메모리 주소 확인 | `id(a)` → 실행마다 다른 값 출력 |
#### 숫자 관련 내장 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `abs()` | 절댓값 | `abs(-5)` → 5 |
| `pow(a, b)` | 거듭제곱 (a\^b) | `pow(2, 3)` → 8, `pow(5, 2)` → 25 |
| `round(n, d)` | 반올림 (d: 소수점 자리 수) | `round(3.14159, 2)` → 3.14, `round(7.6)` → 8 |
#### 리스트 & 튜플 관련 내장 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `len()` | 길이(개수) 확인 | `len([1,2,3,4])` → 4, `len("Hello")` → 5 |
| `max()` | 최대값 | `max(3,5,7,2)` → 7 |
| `min()` | 최소값 | `min(3,5,7,2)` → 2 |
| `sum()` | 합계 | `sum([1,2,3,4,5])` → 15 |
| `sorted()` | 정렬 (오름차순 기본) | `sorted(numbers)` → 오름차순, `sorted(numbers, reverse=True)` → 내림차순 |
`sorted()`는 원본 리스트를 변경하지 않고 새 리스트를 반환함. `reverse=True`를 주면 내림차순 정렬됨.
#### 문자열 관련 내장 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `ord()` | 문자 → 유니코드 정수 변환 | `ord('A')` → 65, `ord('가')` → 44032 |
| `chr()` | 유니코드 정수 → 문자 변환 | `chr(65)` → A, `chr(44032)` → 가 |
`ord()`와 `chr()`는 서로 역방향 관계임. 문자 비교나 암호화 등에서 유용하게 활용됨.
#### 형변환 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `int()` | 정수로 변환 | `int("10")` → 10, `int(3.7)` → 3 (소수점 버림) |
| `float()` | 실수로 변환 | `float("3.14")` → 3.14, `float(10)` → 10.0 |
| `str()` | 문자열로 변환 | `str(123)` → "123", `str(3.14)` → "3.14" |
`int(3.7)`은 반올림이 아니라 **소수점 이하를 버리는** 방식임에 유의해야 함.
#### 기타 유용한 내장 함수
| 함수 | 설명 | 예시 |
| --- | --- | --- |
| `enumerate()` | 리스트의 인덱스와 값을 함께 가져옴 | `for index, value in enumerate(fruits)` → `0 사과`, `1 바나나`, `2 체리` |
| `zip()` | 여러 리스트를 묶어 쌍으로 순회 | `for name, score in zip(names, scores)` → `철수 90`, `영희 85`, `민수 88` |
| `map()` | 리스트의 모든 요소에 함수 적용 | `list(map(lambda x: x**2, numbers))` → `[1, 4, 9, 16, 25]` |
| `filter()` | 조건을 만족하는 요소만 필터링 | `list(filter(lambda x: x%2==0, numbers))` → `[2, 4, 6]` |
`enumerate()`는 인덱스를 별도로 관리하지 않아도 되므로 루프에서 자주 활용됨. `zip()`은 두 리스트를 병렬로 순회할 때 유용하며, 길이가 다를 경우 짧은 쪽에 맞춰 종료됨.
---
### 모듈, 표준 라이브러리, 인터프리터
#### 모듈·라이브러리·패키지 개념
Python에서 코드를 재사용하는 단위는 크게 세 가지로 구분됨.
- **모듈(Module)**: 함수·클래스·변수 등을 담은 `.py` 파일 하나
- **라이브러리(Library)**: 여러 모듈을 모아둔 것
- **패키지(Package)**: 여러 모듈을 하나로 묶은 폴더
Python은 설치 시 기본 제공되는 표준 라이브러리(Standard Library)가 있으며, `import`로 바로 불러와 사용할 수 있음.
---
### 모듈 가져오기 (import)
import 방식은 네 가지가 있으며, 상황에 따라 적절히 선택함.
```python
# 1. 기본 import — 모듈명을 붙여서 사용
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

# 2. from 모듈 import 함수 — 특정 함수만 가져와 모듈명 생략 가능
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)        # 3.141592653589793

# 3. import 모듈 as 별칭 — 모듈명을 짧게 줄여서 사용
import numpy as np
import pandas as pd

# 4. from 모듈 import * — 모든 함수 가져오기 (비추천)
from math import *
print(sin(1))  # math.sin() 없이 바로 사용 가능
# → 이름 충돌 위험이 있어 권장하지 않음
```
`from 모듈 import *`는 어떤 함수가 어디서 왔는지 불분명해지므로 실무에서는 지양하는 것이 좋음.
---
###
#### `math` — 수학 계산
```python
import math

print(math.sqrt(25))      # 5.0  (제곱근)
print(math.factorial(5))  # 120  (5!)
print(math.gcd(12, 18))   # 6    (최대공약수)
print(math.pi)            # 3.141592653589793
```
#### `random` — 랜덤 숫자·요소 선택
```python
import random

print(random.randint(1, 10))                      # 1~10 사이의 랜덤 정수
print(random.random())                            # 0~1 사이의 랜덤 실수
print(random.choice(["사과", "바나나", "체리"]))   # 리스트에서 랜덤 선택

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)   # 리스트 섞기 (원본 수정)
print(numbers)
```
#### `datetime` — 날짜·시간 처리
```python
import datetime

now = datetime.datetime.now()       # 현재 날짜와 시간
today = datetime.date.today()       # 현재 날짜만
d = datetime.date(2025, 2, 13)      # 특정 날짜 생성
print(d)  # 2025-02-13
```
#### `os` — 파일·디렉토리 관리
```python
import os

print(os.getcwd())      # 현재 작업 디렉토리 확인
os.mkdir("새폴더")       # 새 폴더 생성
os.rmdir("새폴더")       # 폴더 삭제
```
#### `sys` — Python 인터프리터 관련
```python
import sys

print(sys.version)   # Python 버전 확인
print(sys.argv)      # 실행 시 입력된 인자 확인
sys.exit()           # 프로그램 종료
```
#### `time` — 시간 지연·현재 시간
```python
import time

print(time.time())   # 현재 시간 (유닉스 타임스탬프, 초 단위)
time.sleep(2)        # 2초 동안 프로그램 일시 정지
print("2초 후 실행됨")
```
#### `json` — JSON 데이터 읽기·쓰기
```python
import json

data = {"name": "철수", "age": 25}
json_string = json.dumps(data)         # 딕셔너리 → JSON 문자열 변환
print(json_string)

parsed_data = json.loads(json_string)  # JSON 문자열 → 딕셔너리 변환
print(parsed_data)
```
`dumps()`는 Python 객체를 JSON 문자열로, `loads()`는 JSON 문자열을 Python 객체로 변환함.
#### `re` — 정규표현식으로 문자열 패턴 검색
```python
import re

text = "My phone number is 010-1234-5678."
pattern = r"\d{3}-\d{4}-\d{4}"   # 전화번호 패턴
match = re.search(pattern, text)
if match:
    print(match.group())  # 출력: 010-1234-5678
```
---
### \[참고\] 인터프리터 vs 컴파일러
| 구분 | 인터프리터 (Python, JS) | 컴파일러 (C, C++, Java) |
| --- | --- | --- |
| 실행 방식 | 한 줄씩 실행 | 전체 코드를 번역 후 실행 |
| 속도 | 느림 (실시간 해석) | 빠름 (미리 번역) |
| 오류 발견 | 코드 실행 중 오류 발생 | 컴파일 단계에서 오류 발견 |
#### Python 인터프리터 종류
| 인터프리터 | 설명 |
| --- | --- |
| **CPython** | 기본 Python 인터프리터 (공식 버전) |
| **PyPy** | 빠른 실행속도를 위한 JIT 컴파일러 포함 |
| **Jython** | Java와 함께 사용할 수 있는 Python |
| **IronPython** | .NET 환경에서 실행 가능한 Python |
---
### 파일 읽기/쓰기 (File I/O)
파일을 열 때는 `open()` 함수를 사용하며, 두 번째 인자로 **파일 모드**를 지정함.
| 모드 | 설명 |
| --- | --- |
| `r` | 읽기 전용 (파일이 없으면 오류) |
| `w` | 쓰기 전용 (없으면 생성, 기존 내용 삭제) |
| `a` | 추가 모드 (없으면 생성, 기존 내용 유지) |
| `r+` | 읽기 + 쓰기 (기존 내용 유지) |
| `w+` | 읽기 + 쓰기 (기존 내용 삭제) |
#### 파일 쓰기 (`w`)
```python
file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.write("파일 입출력을 배우고 있어요!\n")
file.close()  # 반드시 닫아야 함
```
#### 파일 읽기 (`r`)
```python
# 전체 읽기
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# 한 줄씩 읽기 (readline)
file = open("example.txt", "r")
print(file.readline())  # 첫 번째 줄
print(file.readline())  # 두 번째 줄
file.close()

# 모든 줄을 리스트로 읽기 (readlines)
file = open("example.txt", "r")
lines = file.readlines()  # 각 줄이 리스트 원소로 반환
print(lines)
file.close()
```
#### 내용 추가 (`a`) / `with` 문
`with` 문을 사용하면 블록이 끝날 때 파일이 **자동으로 닫히므로** `close()`를 직접 호출할 필요가 없음. 실무에서 권장하는 방식임.
```python
# 내용 추가 ('a' 모드)
file = open("example.txt", "a")
file.write("새로운 내용을 추가합니다!\n")
file.close()

# with 문 — 파일 자동 닫힘
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
---
#### CSV 파일 다루기 (`csv` 모듈)
- CSV(Comma-Separated Values)는 쉼표(`,`)로 구분된 데이터 파일로, 엑셀과 비슷한 구조를 텍스트 형태로 저장함.
#### CSV 읽기 (`csv.reader`)
```python
import csv

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)      # CSV 읽기 객체 생성
    for row in reader:             # 한 줄씩 읽기
        print(row)
# 출력: ['이름', '나이', '도시'] / ['철수', '25', '서울'] / ...
```
#### CSV 쓰기 (`csv.writer`)
```python
import csv

with open("new_data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "나이", "도시"])  # 헤더 추가
    writer.writerow(["철수", 25, "서울"])
    writer.writerow(["영희", 30, "부산"])
    writer.writerow(["민수", 22, "대구"])
# newline="" 설정을 하지 않으면 빈 줄이 중간에 추가될 수 있음
```
---
### JSON 파일 다루기 (`json` 모듈)
- \*JSON(JavaScript Object Notation)\*\*은 데이터를 저장·전달하는 경량 형식으로, Python의 딕셔너리와 유사한 구조를 가짐. API 응답 데이터를 다룰 때 특히 자주 사용됨.
#### JSON 파일 저장 (`json.dump`)
```python
import json

data = {"이름": "철수", "나이": 25, "도시": "서울"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
# ensure_ascii=False → 한글이 깨지지 않도록 설정
# indent=4         → 들여쓰기로 보기 좋게 저장
```
#### JSON 파일 읽기 (`json.load`)
```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)  # {'이름': '철수', '나이': 25, '도시': '서울'}
# JSON 파일을 딕셔너리로 변환해서 바로 사용 가능
```
---
#### 파일 I/O 고급 — `pathlib`, `csv.DictReader`, Parquet
| 도구 | 설명 |
| --- | --- |
| `pathlib.Path` | 경로를 객체로 다루는 표준 방식. `/` 연산자로 경로 조합 가능 |
| `with` | 컨텍스트 매니저 — 블록 종료 시 파일 자동 닫힘 |
| `csv.DictReader` | CSV의 헤더 행을 키로 삼아 각 행을 딕셔너리로 읽음 |
| `json.load / json.dump` | 파일 객체와 직접 연동하여 JSON 읽기/쓰기 |
| **Parquet** | 컬럼형 저장 포맷. CSV 대비 약 10배 빠른 읽기 속도, pandas와 연동 |
```python
from pathlib import Path
import json, csv

data_dir = Path('data')

# JSON 읽기 (API 응답)
with open(data_dir / 'resp.json') as f:
    data = json.load(f)

# CSV 읽기 (DictReader — 헤더를 키로 사용)
with open(data_dir / 'sales.csv') as f:
    rows = list(csv.DictReader(f))

# Parquet 읽기/쓰기 (pandas 연동)
import pandas as pd
df = pd.read_parquet(data_dir / 'sales.parquet')
df.to_parquet(data_dir / 'out.parquet')  # 저장
```
`pathlib.Path`는 `data_dir / 'sales.csv'`처럼 `/` 연산자로 경로를 이어 붙일 수 있어 OS별 경로 차이를 신경 쓰지 않아도 됨. `csv.DictReader`는 첫 행을 헤더로 인식해 각 행을 `{'이름': '철수', '나이': '25', ...}` 형태의 딕셔너리로 반환하므로, 컬럼명 기반 접근이 간편함.
---
### 데코레이터 (Decorator)
**데코레이터**는 기존 함수의 코드를 직접 수정하지 않고 새로운 기능을 추가하는 방법임. 함수를 인수로 받아 새로운 함수(callable 객체)를 반환하는 **고차 함수**의 특성을 활용하며, `@` 기호로 함수 정의 위에 적용함. `*args`와 `**kwargs`를 사용해 다양한 인자와 반환값을 처리할 수 있어 유연하게 활용 가능함.
#### 기본 구조
```python
def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
# my_decorator가 greet를 감싸서 호출 전후에 메시지를 출력
```
`@my_decorator`는 `greet = my_decorator(greet)`와 동일한 의미임. 이후 `greet()`를 호출하면 실제로는 `wrapper()`가 실행됨.
#### 인자를 받는 함수에 대한 데코레이터
원래 함수가 인자를 받는 경우, `wrapper`에 `*args`, `**kwargs`를 선언하여 인자를 그대로 전달함.
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("함수 실행 전")
        result = func(*args, **kwargs)  # 원래 함수 실행 및 반환값 저장
        print("함수 실행 후")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))
# 출력: 함수 실행 전 → 함수 실행 후 → 8
```
실행 흐름: `add` → 내부의 `wrapper`로 대체 → `wrapper(3, 5)` 실행 → 실행 전 출력 → 원래 `add(3, 5)` 실행 → 실행 후 출력 → `result`(8) 반환.
---
### 실용적인 Decorator 예제
#### 실행 시간 측정 Decorator
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()                      # 시작 시간 기록
        result = func(*args, **kwargs)           # 원래 함수 실행
        end = time.time()                        # 종료 시간 기록
        print(f"실행 시간:{end - start:.4f}초") # 경과 시간 출력
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("작업 완료!")

slow_function()
# 출력: 작업 완료! / 실행 시간: 2.0025초
```
`slow_function()` 호출 시 실제로는 `wrapper`가 실행되며, `start` 저장 → 함수 실행 → `end` 저장 → 경과 시간 계산·출력의 순서로 동작함.
#### 로그인 검증 Decorator
```python
def require_login(func):
    def wrapper(user):
        if user.get("is_logged_in"):
            return func(user)         # 로그인 상태면 원래 함수 실행
        else:
            print("로그인이 필요합니다.")
    return wrapper

@require_login
def dashboard(user):
    print(f"{user['name']}님의 대시보드입니다.")

user1 = {"name": "Alice", "is_logged_in": True}
user2 = {"name": "Bob", "is_logged_in": False}

dashboard(user1)  # Alice님의 대시보드입니다.
dashboard(user2)  # 로그인이 필요합니다.
```
---
### 데코레이터와 클로저 — 클로저 심화
**클로저**는 내부 함수가 외부 함수의 지역 변수를 기억하고 사용할 수 있는 특성임. 외부 함수가 종료된 후에도 내부 함수는 외부 함수의 변수에 계속 접근할 수 있음.
#### 클로저 동작 특징
- 외부 함수 안에 내부 함수가 정의됨
- 내부 함수는 외부 함수의 변수에 접근 가능
- **외부 함수 종료 후에도** 내부 함수는 외부 변수를 기억하고 사용함
```python
def outer():
    x = 10  # 외부 함수의 변수

    def inner():
        print(x)  # 내부 함수에서 외부 변수에 접근
    return inner

closure = outer()   # outer() 실행 종료 → inner 함수 객체 반환
closure()           # 출력: 10 — outer가 끝났어도 x=10을 기억
```
클로저를 사용하면 외부 함수의 변수를 상태처럼 유지할 수 있어 **상태 저장** 및 **함수 커스터마이징**에 활용됨.
#### 클로저와 데코레이터의 관계
데코레이터는 내부적으로 클로저를 활용함. 데코레이터 안에 정의된 `wrapper` 함수가 바깥 `func` 변수를 기억하는 것 자체가 클로저 동작임.
```python
def outer_decorator(func):
    def wrapper(*args, **kwargs):          # wrapper는 func를 클로저로 기억
        print("함수 실행 전 처리")
        result = func(*args, **kwargs)
        print("함수 실행 후 처리")
        return result
    return wrapper

@outer_decorator
def add(a, b):
    return a + b

print(add(3, 4))
# 함수 실행 전 처리 / 함수 실행 후 처리 / 7
```
- **데코레이터**: 함수를 인자로 받아 새로운 함수로 반환하고, 기존 함수를 수정·확장하는 방법
- **클로저**: 내부 함수가 외부 함수의 지역 변수를 참조할 수 있는 특성
- 데코레이터는 클로저를 활용하여 구현된 고차 함수임
---
### 오류와 예외의 차이
| 구분 | 오류 (Error) | 예외 (Exception) |
| --- | --- | --- |
| 발생 시점 | 코드 실행 전 (문법 오류) | 코드 실행 중 |
| 대표 예시 | `SyntaxError` | `ZeroDivisionError`, `ValueError` |
| 해결 방법 | 개발자가 직접 수정해야만 해결 | `try-except`로 처리하여 프로그램 계속 실행 가능 |
---
### 예외 처리 구문 (try-except)
`try-except`를 사용하면 예외가 발생해도 프로그램이 중단되지 않고 계속 실행됨.
#### 기본 구조
```python
try:
    print(10 / 0)          # 0으로 나누기 → 예외 발생
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
```
#### 여러 예외 처리
```python
try:
    num = int(input("숫자를 입력하세요: "))  # 숫자 아닌 값 → ValueError
    result = 10 / num                       # 0 입력 → ZeroDivisionError
    print("결과:", result)
except ValueError:
    print("숫자만 입력해주세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
```
#### 예외 메시지 출력 (`as e`)
`except Exception as e`로 모든 예외를 잡을 수 있으며, `e`에 예외 메시지가 담김.
```python
try:
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
except Exception as e:  # 모든 예외 처리 가능
    print("예외 발생:", e)
# 출력 예시: 예외 발생: division by zero
```
#### `finally` — 예외 여부와 상관없이 항상 실행
파일·연결 등 반드시 닫아야 하는 자원을 처리할 때 사용함.
```python
try:
    file = open("test.txt", "r")  # 파일 없으면 예외 발생
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    print("프로그램 종료")       # 항상 실행됨
# 출력: 파일이 없습니다. / 프로그램 종료
```
---
### 사용자 정의 예외 작성
개발자가 직접 예외 클래스를 만들 수 있음. `Exception` 클래스를 상속받아 정의하고, `raise` 키워드로 강제 발생시킴.
#### 기본 사용자 정의 예외
```python
class MyError(Exception):  # Exception 클래스 상속
    pass

try:
    raise MyError           # 예외 발생
except MyError:
    print("사용자 정의 예외 발생!")
```
#### 메시지가 있는 사용자 정의 예외
```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomError:{self.message}"

try:
    raise CustomError("잘못된 입력입니다.")
except CustomError as e:
    print(e)
# 출력: CustomError: 잘못된 입력입니다.
```
#### `raise`로 특정 조건에서 예외 발생
```python
def check_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다.")
    print("나이:", age)

try:
    check_age(-5)           # 음수 입력 → 예외 발생
except ValueError as e:
    print("오류:", e)
# 오류: 나이는 0 이상이어야 합니다.
```
#### 예외 처리 — 파이프라인 안정성 패턴
실전에서는 `try-except-else-finally` 완전 구조 + 사용자 정의 예외 + `raise`를 함께 사용함.
```python
class DataValidationError(ValueError):
    def __init__(self, col, val):
        super().__init__(f'{col}={val} 검증 실패')

def safe_load(path):
    try:
        df = pd.read_parquet(path)
        if df.empty: raise DataValidationError('rows', '0')
        return df
    except FileNotFoundError:
        logger.error(f'파일 없음:{path}')
        return None
    except DataValidationError as e:
        logger.warning(str(e))
        return None
    finally:
        logger.info(f'로딩 시도:{path}')  # 항상 실행
```
---
### 왜 로깅이 필요한가?
`print()`는 디버깅용으로는 유용하지만, 실 서비스에서는 **출력 레벨 구분이 불가능하고 로그 관리가 안 됨**. 반면 `logging` 모듈을 사용하면 아래가 가능함.
- 운영 중 오류 추적 (트래픽 많을 때 발생한 문제 재현)
- 로그 레벨로 개발/운영/디버깅 로그를 구분
- 파일로 저장, 날짜별 회전(logging rotation), 알람 연계
#### 로그 레벨
| 레벨 | 설명 |
| --- | --- |
| `DEBUG` | 상세 정보 (디버깅용) |
| `INFO` | 정상 동작 정보 |
| `WARNING` | 경고, 문제가 될 수 있는 상황 |
| `ERROR` | 오류 발생 (실행은 계속됨) |
| `CRITICAL` | 치명적인 오류 (서비스 중단 가능성) |
#### `logging` 기본 사용법
```python
import logging

logging.basicConfig(level=logging.INFO)  # INFO 이상만 출력
logging.info("서비스 시작")
logging.warning("주의: 설정 값이 누락되었습니다.")
logging.error("에러 발생: 파일을 찾을 수 없습니다.")
```
`logging.basicConfig()`는 간단한 설정만 가능하며, 실무에서는 **한 번만 호출**해야 함.
---
### 로깅 구조 예시 (실무 패턴)
Logger → Handler 로 로그가 전달되며, 핸들러마다 레벨과 출력 대상을 다르게 설정할 수 있음.
```plain text
[Logger]
    ├── [ConsoleHandler]       → INFO 이상 콘솔 출력
    └── [FileHandler(app.log)] → DEBUG 이상 파일 저장
            └── [FileHandler(error.log)] → ERROR 이상만 저장
```
```python
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# 로그 디렉토리 생성
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 로거 생성
logger = logging.getLogger("MyApp")
logger.setLevel(logging.DEBUG)

# 1. 콘솔 핸들러 — INFO 이상 출력
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("[%(levelname)s]%(message)s")
console_handler.setFormatter(console_format)

# 2. 파일 핸들러 — DEBUG 이상, 자정마다 회전, 최근 7일 보관
file_handler = TimedRotatingFileHandler(
    filename=f"{log_dir}/app.log",
    when="midnight", interval=1, backupCount=7, encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter(
    "%(asctime)s |%(levelname)s |%(filename)s:%(lineno)d |%(message)s"
)
file_handler.setFormatter(file_format)

# 3. 에러 핸들러 — ERROR 이상만 별도 저장
error_handler = logging.FileHandler(f"{log_dir}/error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(file_format)

# 핸들러 등록
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(error_handler)

# 테스트
logger.debug("디버그 정보")
logger.info("정상 흐름")
logger.warning("경고 메시지")
logger.error("에러 발생")
logger.critical("치명적 오류")
```
`TimedRotatingFileHandler`는 `when="midnight"`으로 설정하면 자정마다 새 파일로 교체하며, `backupCount=7`로 최근 7일치 로그만 보관함. 분석 파이프라인 실전에서는 핸들러 포매터와 로거 등록을 리스트 컴프리헨션으로 간결하게 처리하기도 함.
```python
fmt = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')
[h.setFormatter(fmt) for h in [ch, fh]]
[logger.addHandler(h) for h in [ch, fh]]
```
---
### `.env` 파일과 환경변수
#### 왜 `.env` 파일이 필요한가?
코드에 DB 비밀번호나 API 키 같은 민감정보를 직접 하드코딩하면 GitHub 등에 실수로 올릴 경우 보안 사고가 발생할 수 있음. `.env` 파일을 사용하는 이유는 세 가지임.
- **보안**: 민감정보를 코드와 분리하여 저장
- **이식성**: 운영/개발/로컬 환경별 설정을 `.env` 파일 교체만으로 전환 가능
- **재현성**: `.env.example` 파일만 공유하면 다른 개발자도 동일한 환경 구성 가능
#### 환경변수란?
운영체제나 프로그램 실행 환경에서 설정된 전역 변수임. Linux/macOS에서는 `export` 명령으로 설정하고, Python에서는 `os.getenv()`로 읽어옴.
```bash
# Linux/macOS에서 환경변수 설정
export DB_USER=admin
export DB_PASS=secret123
```
```python
import os
print(os.getenv("DB_USER"))  # admin
```
#### `.env` 파일 형식
`키=값` 형태로 작성하며, `#`으로 주석을 달 수 있음. 값에 따옴표는 선택 사항임.
```plain text
# 환경설정 파일
DEBUG=True
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASS=mypassword
```
#### Python에서 `.env` 읽는 방법
`python-dotenv` 패키지를 설치하면 `.env` 파일을 자동으로 환경변수에 로드할 수 있음.
```bash
pip install python-dotenv
```
```python
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 자동 로드 (현재 경로 기준)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
print(f"DB 사용자:{db_user}, 비밀번호:{db_pass}")
```
`.env` 파일은 **현재 경로 기준으로 탐색**하므로, 프로젝트 루트 디렉토리 위치를 확인해야 함.
#### `.env` + Git 연동 시 주의사항
`.env` 파일은 반드시 **`.gitignore`****에 추가**하여 Git에 올라가지 않도록 해야 함. 대신 팀원에게는 `.env.example` 파일을 공유하여 키 목록만 전달함.
```plain text
# .gitignore에 추가
.env
.env.local
.env.production
```
```plain text
# .env.example — 값은 비워서 공유
DB_USER=
DB_PASS=
DEBUG=
```
팀원들은 이 파일을 복사해서 실제 값을 채워 `.env`로 사용함.
#### 보안 강화 팁
| 항목 | 설명 |
| --- | --- |
| `.env` 암호화 | `dotenv-vault` 같은 툴로 관리 |
| CI/CD 연동 | GitHub Actions의 Secrets로 대체 가능 |
| 다중환경 관리 | `.env.dev`, `.env.prod` 등으로 환경별 분리 |
#### `.env` 기반 환경변수 — 실전 패턴 정리
```python
# .env 파일 내용
# API_KEY=sk-xxxx
# DB_URL=postgresql://user:pass@host/db
# ENV=development

from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드

api_key = os.getenv('API_KEY')
db_url  = os.getenv('DB_URL')
env     = os.getenv('ENV', 'development')  # 기본값 설정 가능
```
`os.getenv('ENV', 'development')`처럼 두 번째 인자로 기본값을 지정하면, 환경변수가 없을 때 기본값이 사용되므로 안전하게 처리할 수 있음.
---
### 타입 힌트 (Type Hints)
**타입 힌트**는 변수나 함수의 매개변수·반환값에 타입을 명시하는 기능임. **런타임에는 영향을 미치지 않지만**, 에디터 자동완성과 `mypy`, `pyright` 같은 정적 검사 도구의 오류 탐지에 큰 도움이 됨.
#### 기본 타입 힌트
```python
def add(x: int, y: int) -> int:
    return x + y
# x: int → x는 정수 타입
# -> int  → 반환값도 정수 타입
```
---
### `typing` 모듈 — `List`, `Dict`, `Optional`
Python 3.9 이전에는 `typing` 모듈을 import해야 복합 타입 힌트를 사용할 수 있음.
#### `List`, `Dict`
```python
from typing import List, Dict

names: List[str] = ["Alice", "Bob"]              # 문자열 리스트
ages: Dict[str, int] = {"Alice": 25, "Bob": 30}  # 키: str, 값: int 딕셔너리
```
#### `Optional`
`Optional[X]`는 `Union[X, None]`과 동일한 의미임. `str` 또는 `None`이 올 수 있다는 뜻임.
```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f"Hello,{name}"
    return "Hello, anonymous"
```
`Optional`의 주요 사용 상황은 아래와 같음.
| 상황 | 예시 |
| --- | --- |
| 초기값이 없을 수 있음 | `def func(id: Optional[int])` |
| 파라미터 생략 가능 | `def send(msg: Optional[str] = None)` |
| 반환값이 있을 수도 없을 수도 (DB 조회) | `def find(id: int) -> Optional[User]` |
`Optional`은 타입만을 위한 표현이며 실제 동작에는 영향을 주지 않음. `mypy`, `pyright` 같은 정적 분석 도구가 있을 때만 오류로 탐지됨.
---
### `Union`, `Any`, `Literal`
```python
from typing import Union, Any, Literal
```
#### `Union[str, int]` — 여러 타입 중 하나 허용
```python
def parse(value: Union[str, int]) -> str:
    return str(value)

parse("hello")  # OK
parse(123)      # OK
parse(3.14)     # X — mypy 기준 타입 오류 (float은 허용 안 됨)
```
`Union[X, Y]`는 매개변수가 X 또는 Y 중 하나임을 명시함. 런타임에는 영향 없으며 `mypy` 같은 도구가 검사할 때만 유효함.
#### `Any` — 아무 타입이나 허용 (비추천)
```python
def log(data: Any):
    print(f"Logging:{data}")

log("hello")   # 문자열
log(123)       # 숫자
log([1, 2, 3]) # 리스트
log(None)      # None
```
`Any`는 타입 체크를 포기한 것과 같기 때문에 **유지보수성, 자동완성 기능 저하**를 유발하며 오타나 잘못된 인자도 통과됨. **필요할 때만 사용하고, 웬만하면 쓰지 말 것.**
#### `Literal["left", "right"]` — 딱 정해진 값만 허용
```python
def turn(direction: Literal["left", "right"]):
    print(f"Turning{direction}")

turn("left")   # OK
turn("right")  # OK
turn("up")     # X — mypy 등에서 오류
```
`Literal`은 매개변수 값을 고정된 선택지로 제한할 때 사용함. `enum`과 비슷한 조건 제어, 파라미터 값 제한에 유용함.
#### 요약
| 문법 | 의미 | 사용 목적 |
| --- | --- | --- |
| `Union[str, int]` | 둘 중 하나 허용 | 입력 타입 유연성 확보 |
| `Any` | 아무 타입이나 허용 | 타입 강제 해제 (비추천) |
| `Literal["A", "B"]` | 특정 값만 허용 | 고정된 선택지 강제 |
---
### Generic — 타입 안정성을 높이면서 재사용 가능한 구조
**Generic**은 Java/C++의 템플릿과 같은 개념으로, 타입을 파라미터처럼 받아 재사용 가능한 클래스나 함수를 만들 때 사용함.
| 키워드 | 의미 |
| --- | --- |
| `TypeVar("T")` | 타입 파라미터 T를 선언 |
| `Generic[T]` | 이 클래스는 "타입 T"를 파라미터로 받는 제네릭 클래스임을 선언 |
| `Stack[int]()` | T에 int를 넣은 인스턴스 (정수 전용 스택) |
| `Stack[str]()` | T에 str을 넣은 인스턴스 (문자열 전용 스택) |
```python
from typing import TypeVar, Generic, List

T = TypeVar("T")  # T는 어떤 타입이든 될 수 있음

class Stack(Generic[T]):  # Stack 클래스는 T 타입을 사용하는 제네릭 클래스
    def __init__(self):
        self._items: List[T] = []  # T 타입으로 이루어진 리스트

    def push(self, item: T) -> None:
        self._items.append(item)   # 같은 타입만 추가 가능

    def pop(self) -> T:
        return self._items.pop()   # 같은 타입을 꺼냄

s_int = Stack[int]()   # 정수 전용 스택
s_int.push(10)
print(s_int.pop())

s_str = Stack[str]()   # 문자열 전용 스택
s_str.push("hello")
```
사용 목적은 세 가지임. int, str, float 등 어떤 타입에도 사용할 수 있는 **공통 구조**를 만들고, `mypy`, `pyright` 등이 `push()` 시점에서 타입 오류를 탐지하는 **정적 타입 안전성 확보**, 그리고 `Stack[str]`이면 `.pop()`의 리턴값이 `str`로 **IDE 자동완성**되는 효과를 얻을 수 있음.
---
### Protocol — Duck Typing을 위한 정적 검사
**Protocol**은 실제 상속 없이도 인터페이스 기반 타입 체크가 가능하도록 함. **Duck Typing**(객체의 형(type)보다 행동(method)에 따라 처리하는 방식)을 정적으로 검사할 수 있게 해줌.
```python
from typing import Protocol

class SupportsWrite(Protocol):   # ① "write(str) 메서드를 가진 객체"를 정의
    def write(self, s: str) -> None: ...

def write_hello(writer: SupportsWrite) -> None:  # ② writer는 write를 지원해야 함
    writer.write("Hello\n")

class FileLike:   # ③ 실제 구현 클래스 (Protocol 상속 안 해도 OK)
    def write(self, s: str) -> None:
        print(f"Writing:{s}")

write_hello(FileLike())   # ④ FileLike는 write()가 있으므로 OK
```
| 특징 | 설명 |
| --- | --- |
| 타입 안정성 | 런타임 전에 `.write()` 없으면 오류로 감지 가능 |
| 유연성 유지 | `FileLike`는 Protocol 상속 없이도 동작 |
| 강제 인터페이스 선언 | Java/C++의 Interface와 같은 역할 |
| IDE 자동 완성 | 타입 추론이 정확해짐 |
다양한 객체들이 같은 인터페이스(`write`, `send` 등)를 지원할 때, 라이브러리 사용자에게 규약을 명확히 전달하고 싶을 때, `mypy`/`pyright`를 활용한 정적 타입 검사 강화 시 사용함.
---
### Callable — 함수 타입 정의
- \*`Callable`\*은 함수를 인자로 받는 함수에서 그 함수의 시그니처(인자 타입, 반환 타입)를 명확하게 정의할 때 사용함.
형식: `Callable[[ArgType1, ArgType2], ReturnType]`
```python
from typing import Callable

def compute(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

result = compute(3, 4, lambda a, b: a + b)  # op는 int 2개 받아 int 반환
```
`Callable[[str, float], bool]`은 문자열과 실수를 받아 bool을 반환하는 함수 타입을 의미함.
```python
from typing import Callable, List

def sort_by(data: List[int], key_func: Callable[[int], int]) -> List[int]:
    return sorted(data, key=key_func)

data = [3, 5, 1, 7]
print(sort_by(data, lambda x: -x))  # 내림차순 정렬
```
---
### 정적 타입 검사 도구 `mypy` 활용
`mypy`는 Python에서 타입 힌트를 정적으로 검사하는 도구임. 코드를 실행하지 않아도 타입 오류를 찾아줌.
```bash
pip install mypy
mypy test.py          # 특정 파일 검사
mypy src/             # 특정 폴더 검사
mypy --config-file mypy.ini  # 설정 파일 지정
```
```python
# test.py
def add(x: int, y: int) -> int:
    return x + y

add(1, 2)      # OK
add("a", "b")  # X — 타입 오류, 런타임에서는 실행됨
```
`mypy test.py` 실행 시 `add("a", "b")`에서 "Argument 1 to 'add' has incompatible type 'str'; expected 'int'" 오류를 런타임 없이 탐지함.
#### `mypy.ini` 설정 예시
```plain text
[mypy]
python_version = 3.11
strict = True                  # 가장 강력한 타입 검사 옵션
disallow_untyped_defs = True   # 모든 함수에 타입 힌트 강제
ignore_missing_imports = True
```
`mypy` 사용 이유는 버그 예방(코드 실행 전 타입 오류 조기 발견), 코드 자동완성 향상, 협업 시 명확한 Interface 규약 제공, 테스트 비용 감소(일부 오류를 사전 차단)임.
---
### 타입 힌트 전체 정리
| 문법 | 용도 |
| --- | --- |
| `List[str]`, `Dict[str, int]` | 컨테이너 타입 지정 |
| `Optional[int]` | int or None 허용 |
| `Union[str, int]` | 여러 타입 중 하나 허용 |
| `Generic[T]` | 타입 파라미터 일반화 |
| `Protocol` | 인터페이스 기반 구조 정의 |
| `Callable` | 함수의 시그니처 지정 |
| `mypy`, `pyright` | 정적 타입 체크 도구 |
---
### 타입 힌트 기초 — 분석 코드 가독성 향상
Python의 타입 힌트(type hint)는 변수·매개변수·반환값에 타입 정보를 명시해 코드 가독성을 높이는 기법임. 런타임 동작에는 전혀 영향을 미치지 않고, 일종의 주석 역할을 하며 정적 분석 도구가 이를 활용함.
#### 기본 타입
`str`, `int`, `float`, `bool`, `None` 다섯 가지가 가장 기본적으로 사용됨.
#### 컬렉션 타입
| 표기 | 의미 |
| --- | --- |
| `list[str]` | 문자열 원소로 이루어진 리스트 |
| `dict[str, Any]` | 문자열 키, 임의 값의 딕셔너리 |
| `tuple[int, ...]` | 정수 원소 튜플 |
#### 함수 시그니처 표기
매개변수 뒤에 `: 타입`, 반환값은 `->` 이후에 타입을 적음.
```python
# 타입 힌트 기초
from typing import Any

# 기본 타입 힌트
def clean_name(s: str) -> str:
    return s.strip().lower()

def compute_avg(values: list[float]) -> float:
    return sum(values) / len(values)

def lookup(d: dict[str, Any], key: str,
           default: float = 0.0) -> float:
    return float(d.get(key, default))

# 3.10+ 문법: | 사용 가능
def parse(val: str | int | None) -> str:
    return str(val) if val is not None else ""
```
- Python 3.10 이상에서는 `Union` 대신 `|` 연산자로 유니온 타입을 간결하게 표현 가능함.
- VS Code Pylance가 타입 힌트를 읽어 실시간으로 타입 오류를 하이라이팅함.
---
### Optional · Union · Literal · Any
`typing` 모듈에서 제공하는 고급 타입 표현들로, 더 정밀한 시그니처 정의가 가능함.
#### 주요 타입 요약
| 타입 | 의미 | 비고 |
| --- | --- | --- |
| `Optional[X]` | \`X | None\` — 결측치 허용 |
| `Union[X, Y]` | X 또는 Y 타입 허용 | 3.10+에서 \`X |
| `Literal[...]` | 특정 값만 허용 | enum 대안, 인자 범위 제한 |
| `Any` | 모든 타입 허용 | 사용 최소화 권장 |
| `Callable[[A], R]` | 인자 A를 받아 R을 반환하는 함수 | 함수를 인자로 넘길 때 사용 |
```python
# Optional·Union·Literal
from typing import Optional, Union, Literal, Callable

# Optional: 결측치 허용
def get_val(d: dict, key: str) -> Optional[float]:
    return d.get(key)  # None 반환 가능

# Literal: 특정 값만 허용
def fill_strategy(
    method: Literal['mean', 'median', 'drop']
) -> None: ...

# Callable: 함수를 인자로
def apply_fn(
    data: list[float],
    fn: Callable[[float], float]
) -> list[float]:
    return [fn(x) for x in data]
```
- `Literal`은 허용 값의 집합을 타입으로 표현하므로, 문자열 상수를 enum 없이 제한하고 싶을 때 유용함.
- `Any`는 타입 검사를 사실상 무력화하므로 꼭 필요한 경우에만 사용해야 함.
---
### Pydantic v2 — 데이터 검증과 직렬화
Pydantic은 Python 타입 힌트 기반으로 데이터 검증과 직렬화를 자동 처리하는 라이브러리임. v2부터 성능이 대폭 향상되었으며, `BaseModel`을 상속해 스키마를 정의하면 검증 로직을 직접 구현하지 않아도 됨.
#### 핵심 개념
| API | 역할 |
| --- | --- |
| `BaseModel` | 스키마 정의 + 자동 검증 |
| `Field(gt=..., lt=..., regex=..., description=...)` | 필드별 세부 제약 조건 설정 |
| `model_validate(dict)` | dict → 객체 변환 (검증 포함) |
| `model_dump()` | 객체 → dict / JSON 변환 |
| `ValidationError` | 검증 실패 시 어느 필드가 왜 틀렸는지 상세 제공 |
```python
# Pydantic v2 실전
from pydantic import BaseModel, Field
from typing import Optional

class SalesRecord(BaseModel):
    date: str
    region: str
    amount: float = Field(gt=0, description='양수')
    category: Optional[str] = None

# 검증 성공
r = SalesRecord(**{'date':'2024','region':'서울','amount':1500})
r.model_dump()  # dict 변환

# 검증 실패
try:
    SalesRecord(date='', region='서울', amount=-100)
except Exception as e:
    print(e)  # 어느 필드, 왜 실패했는지 상세
```
- `Field(gt=0)`은 amount가 0 초과여야 함을 강제함. `gt`(greater than), `lt`(less than), `ge`/`le`(이상/이하) 등 조합 가능함.
- `Optional[str] = None`으로 선언된 필드는 입력하지 않아도 검증을 통과함.
---
### mypy + VS Code Pylance — 정적 타입 검사 도구
런타임 전에 타입 오류를 잡는 두 가지 도구임. IDE(Pylance)와 CLI(mypy)를 동시에 활용하면, 개발 중과 CI/CD 파이프라인 양쪽에서 타입 안전성을 보장할 수 있음.
> 런타임 전 타입 오류를 IDE와 CLI에서 동시에 잡아낸다. CI에 통합하면 코드 품질 자동 게이트.
```python
# 타입 오류가 있는 코드
def compute_avg(values: list[float]) -> float:
    return sum(values) / len(values)

result = compute_avg(['a', 'b', 'c'])  # list[str] ← 오류!

# mypy 실행
$ mypy analysis.py

# analysis.py:4: error: Argument 1 has incompatible type
# 'list[str]'; expected 'list[float]'
```
- `list[str]`을 `list[float]`를 요구하는 함수에 넘기면 mypy가 라인 번호와 함께 오류를 출력함.
- 데이터 분석 코드에서 컬럼 타입 오류, 결측치 처리 누락 등을 사전에 차단하는 데 특히 유효함.
---
### Pydantic을 분석 파이프라인에 활용하기
CSV 처리나 API 응답 수신처럼 외부 데이터가 들어오는 구간에 Pydantic 검증을 결합하면, 잘못된 데이터가 파이프라인 깊숙이 들어오기 전에 차단할 수 있음.
#### 활용 패턴
- CSV 한 행씩 → `BaseModel`로 일괄 검증, 실패 행은 오류 목록에 집계
- API JSON 응답 → 스키마 검증 후 저장
- `model_json_schema()` → OpenAPI 스키마 자동 생성 (FastAPI 연동 시 동일한 구조)
```python
# 파이프라인 검증 패턴
from pydantic import BaseModel, ValidationError
import csv

class Record(BaseModel):
    date: str
    amount: float
    region: str

valid, errors = [], []

with open('sales.csv') as f:
    for i, row in enumerate(csv.DictReader(f)):
        try:
            valid.append(Record(**row))
        except ValidationError as e:
            errors.append({'row': i, 'error': str(e)})

print(f'유효:{len(valid)}건, 오류:{len(errors)}건')

# 오류 리포트 저장
import json
Path('errors.json').write_text(json.dumps(errors, ensure_ascii=False))
```
- 잘못된 행을 건너뛰는 것과 오류를 모아 리포트로 저장하는 것을 선택적으로 적용할 수 있음.
- `ensure_ascii=False`를 지정해야 한글 등 비 ASCII 문자가 유니코드 이스케이프 없이 저장됨.
---
### 타입 시스템이 데이터 분석 코드를 바꾸는 이유
타입 힌트와 Pydantic을 도입하면 코드 품질이 여러 차원에서 동시에 향상됨.
| 영역 | 효과 |
| --- | --- |
| 컬럼명 오타 사전 차단 | `amount` vs `Amount` 같은 오류를 ValidationError가 런타임 전에 잡음. 수백만 행 처리 후 발견보다 훨씬 나음 |
| 팀 협업 계약서 | 함수 시그니처에 타입이 있으면 teammate가 잘못된 인자를 전달하기 어려움. 별도 문서 없이도 인터페이스가 명확함 |
| IDE 자동완성 품질 향상 | 타입 정보 → Pylance가 정확한 자동완성과 오류 하이라이팅 제공. 개발 속도와 정확성이 동시에 향상됨 |
| 후속 과목 직접 연결 | FastAPI·SpringBoot 연동 시 JSON 스키마 정의가 필수인데, Pydantic BaseModel이 그 역할을 그대로 담당함 |
---
### 디버깅 — 개요 및 예외 타입
- 버그(Bug)란 프로그램이 예상대로 동작하지 않는 원인을 말하며, 입력 오류·논리 오류·실행 오류 등 다양한 유형이 존재함.
**디버깅(Debugging) 과정**은 아래 흐름을 따름:
문제 재현 → 원인 분석 → 해결 방법 탐색 및 적용 → 테스트 후 정상 작동 확인
#### 주요 예외 타입
| 예외 타입 | 설명 | 예제 |
| --- | --- | --- |
| `SyntaxError` | 문법 오류 | `print("Hello"` (괄호 닫힘 없음) |
| `NameError` | 정의되지 않은 변수 사용 | `print(x)` (x가 정의되지 않음) |
| `TypeError` | 잘못된 타입 사용 | `"2" + 2` (문자열과 숫자 연산) |
| `IndexError` | 리스트 인덱스 범위 초과 | `my_list[5]` (길이가 5 미만인 경우) |
| `KeyError` | 딕셔너리에서 존재하지 않는 키 접근 | `my_dict["없는키"]` |
| `ValueError` | 변환할 수 없는 값을 사용 | `int("hello")` |
| `AttributeError` | 존재하지 않는 속성에 접근 | `"hello".push()` |
| `ZeroDivisionError` | 0으로 나누기 | `10 / 0` |
---
### 디버깅 — print() vs logging 모듈
두 가지 방법 모두 실행 흐름과 변수 값을 추적하는 데 사용하지만, 규모와 목적에 따라 선택해야 함.
#### print()를 활용한 디버깅
중간중간 변수 값을 출력해 실행 흐름을 추적하는 가장 간단한 방법임.
```python
def add_numbers(a, b):
    print(f"DEBUG: a={a}, b={b}")  # 디버깅 출력
    return a + b

print(add_numbers(3, 5))
```
- 단점: 코드가 지저분해지고, 나중에 삭제해야 할 `print` 문이 많아질 수 있음.
#### logging 모듈을 활용한 디버깅
`print()` 대신 `logging`을 사용하면 실행 환경에 따라 출력 방식을 조정할 수 있음. 레벨별 메시지 구분이 가능해 실무에서 권장됨.
```python
import logging

logging.basicConfig(level=logging.DEBUG)  # 로그 레벨 설정
logging.debug("디버깅 메시지")
logging.info("정보 메시지")
logging.warning("경고 메시지")
logging.error("에러 메시지")
logging.critical("심각한 오류 메시지")
```
파일로 로그를 저장하려면 `filename` 인자를 추가함:
```python
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s -%(levelname)s -%(message)s"
)
logging.info("파일에 기록되는 로그 메시지")
```
---
### 디버깅 — traceback / pdb
#### traceback을 활용한 에러 로그 출력
예외 발생 시 단순히 메시지만 출력하는 것이 아니라, 전체 호출 스택 정보를 함께 출력할 수 있음.
```python
import traceback

try:
    result = 10 / 0
except Exception as e:
    print("에러 발생:", e)
    traceback.print_exc()  # 전체 오류 정보 출력
```
#### pdb(Python Debugger) 모듈을 활용한 디버깅
`pdb.set_trace()`를 삽입하면 해당 지점에서 실행이 멈추고, 대화형 프롬프트에서 코드를 단계별로 점검할 수 있음.
```python
import pdb

def divide(a, b):
    pdb.set_trace()  # 여기서 실행이 멈춤
    return a / b

print(divide(10, 2))
```
pdb 프롬프트에서 사용하는 주요 명령어:
| 명령어 | 설명 |
| --- | --- |
| `n` | 다음 줄 실행 |
| `s` | 함수 내부 이동 |
| `c` | 계속 실행 |
| `p 변수명` | 변수값 출력 |
| `q` | 디버깅 종료 |
---
### 디버깅 — assert 문 / 코드 스타일 검사
#### assert 문을 활용한 디버깅
`assert`는 코드 실행 중 특정 조건을 검사하는 데 유용함. 조건이 `False`이면 `AssertionError`를 발생시켜 문제를 즉시 알림.
python
```python
def divide(a, b):
    assert b != 0, "b는 0이 될 수 없습니다!"
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # AssertionError 발생
```
- 실무에서는 `assert` 단독보다 `if`문과 `raise Exception`을 함께 사용하는 방식을 권장함.
#### 코드 스타일 검사 — flake8, pylint
| 도구 | 특징 | 사용법 |
| --- | --- | --- |
| `flake8` | 불필요한 공백, 변수 명명 규칙, 들여쓰기 오류 등 스타일 위반 자동 검사 | `pip install flake8` → `flake8 my_script.py` |
| `pylint` | 코드 스타일뿐 아니라 코드 품질까지 분석. 점수(score)로 결과 제공 | `pip install pylint` → `pylint my_script.py` |
---
### 디버깅 — pylint 실행 결과 예시
pylint를 설치한 뒤, 환경에 따라 `pylint` 명령이 PATH에 등록되지 않는 경우가 있음. 이때는 전체 경로를 지정해 실행해야 함.
```plain text
/config/.local/bin/pylint myscript.py
```
실행 결과 예시: 파일명, 라인 번호, 오류 코드, 오류 내용이 함께 출력되며, 마지막에 전체 점수(예: `6.15/10`)가 표시됨. 출력되는 항목 예시:
- `C0304`: 파일 끝 개행 누락
- `C0114`: 모듈 docstring 없음
- `C0103`: 모듈명이 snake_case 규칙에 맞지 않음
- `C0116`: 함수/메서드 docstring 없음
---
### 프로젝트 디렉토리 구조 (예시)
테스트와 코드 품질 도구를 함께 사용하는 Python 프로젝트의 권장 디렉토리 구조임.
```plain text
my_project/
├── src/                        # 핵심 로직 디렉토리
│   └── mymodule/
│       ├── __init__.py
│       └── core.py             # 예: 주요 기능 함수 정의
├── tests/                      # 테스트 디렉토리
│   └── test_core.py            # pytest 기반 테스트 코드
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions 워크플로
├── .flake8                     # 스타일 검사 설정
├── .pre-commit-config.yaml     # Git pre-commit 자동 검사 설정
├── pyproject.toml              # black, mypy 공통 설정
├── requirements.txt            # 종속 패키지 목록
├── README.md                   # 프로젝트 설명
└── setup.cfg                   # 추가 설정 (필요 시)
```
---
### pytest — 테스트 자동화 기본
pytest는 Python의 대표적인 테스트 자동화 도구로, 함수 단위 테스트와 통합 테스트 모두를 지원하며 CI/CD 파이프라인에서 신뢰성 검증 도구로 활용됨.
#### 기본 동작 규칙
- 파일 이름: `test_*.py` 또는 `_test.py` 형식이어야 pytest가 인식함
- 함수 이름: `test_`로 시작해야 실행됨
- 현재 디렉토리 이하에서 재귀적으로 탐색 → pytest를 실행한 위치 기준으로 서브폴더까지 모두 검사함
#### 예시 구조 및 코드
```plain text
my_project/
├── src/
│   └── mymodule/
│       └── core.py
└── tests/
    └── test_core.py
```
```python
# src/mymodule/core.py
def add(a: int, b: int) -> int:
    return a + b
```
```python
# tests/test_core.py
from src.mymodule.core import add

def test_add():
    assert add(1, 2) == 3
```
프로젝트 루트에서 `cd my_project` 후 `pytest` 명령만으로 전체 테스트가 실행됨.
---
### pytest — 탐색 규칙 보충
pytest가 테스트를 탐색하는 세 가지 핵심 규칙임.
- 테스트 파일 또는 디렉토리 이름이 `test_` 접두어 또는 `_test` 접미어 형식을 따르지 않으면 **무시**됨
- 테스트 함수 이름이 `test_`로 시작하지 않으면 **실행되지 않음**
- `conftest.py` 같은 파일은 특별히 hook용으로 이름 규칙과 무관하게 **자동 탐지**됨
---
### pytest — 특별한 실행 옵션
특정 범위만 지정하여 테스트를 실행할 수 있음.
| 구분 | 예제 코드 |
| --- | --- |
| tests 디렉토리만 검사 | `pytest tests/` |
| src 내부도 검사 | `pytest src/` |
| 특정 파일만 | `pytest tests/test_core.py` |
| 강제로 특정 함수 실행 | `pytest tests/test_core.py::test_add` |
---
### pytest — 탐색 규칙 요약
| 항목 | 설명 |
| --- | --- |
| 기본 탐색 | 현재 디렉토리 하위 전체 |
| 기본 파일 이름 | `test_*.py`, `*_test.py` |
| 함수 이름 | `test_`로 시작 |
| 특정 위치 지정 | `pytest [디렉토리/파일 경로]` |
| 특정 함수 실행 | `pytest 파일.py::함수명` |
---
### pytest — pytest.ini 설정 (위치)
`pytest.ini`는 pytest의 동작을 프로젝트 단위로 설정하는 파일임. 보통 프로젝트 루트 디렉토리에 위치하며, pytest 실행 시 자동으로 탐지됨.
```plain text
my_project/
├── pytest.ini    ← 여기에 위치
├── tests/
└── src/
```
---
### pytest — pytest.ini 세부 설정
```plain text
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q --tb=short
testpaths =
    tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
```
#### 항목별 설명
| 항목 | 설명 |
| --- | --- |
| `minversion` | 최소 pytest 버전 요구 사항 |
| `addopts` | 기본 실행 옵션 지정 (명령어 입력 없이 자동 적용) |
| `testpaths` | 기본 테스트 폴더 지정 (예: tests만 검사) |
| `python_files` | 테스트로 인식할 파일 이름 패턴 지정 |
| `python_classes` | 테스트 클래스로 인식할 클래스 이름 패턴 |
| `python_functions` | 테스트 함수 이름 패턴 |
---
### pytest — pytest.ini addopts 상세
| 항목 | 세부 설명 |
| --- | --- |
| `addopts = -ra -q --tb=short` | `-rA`: 모든 요약 출력 (실패, 통과, 건너뜀 등) / `-q`: quiet 모드 (간결하게 출력) / `--tb=short`: traceback을 짧게 출력 |
| `testpaths = tests src/unittests` | 지정된 경로에서만 테스트를 검색. 루트 폴더에 `.py` 파일이 있어도 무시함 |
| `python_files = check_*.py` | `check_something.py` 파일만 테스트로 인식 |
pytest 실행 시 `pytest.ini`에 설정된 옵션이 자동으로 적용됨.
---
### pytest 기초 — 분석 함수 단위 테스트
데이터 분석 함수에 pytest를 적용하는 기본 패턴임.
- `test_*.py` 파일, `test_` 함수 자동 인식
- `assert` 문으로 기댓값 검증
- `fixture`: 공통 데이터·설정을 여러 테스트 함수에 공유
- `parametrize`: 여러 입력 케이스를 한 번에 테스트
- `pytest -v`: 상세 결과 출력 / `x`: 첫 실패 즉시 중단
```python
# pytest 분석 테스트
import pytest
import pandas as pd
from src.clean import clean_nulls

@pytest.fixture
def sample_df():
    return pd.DataFrame({'a': [1, None, 3], 'b': ['x', 'y', None]})

def test_clean_removes_nulls(sample_df):
    result = clean_nulls(sample_df, cols=['a'])
    assert result['a'].isna().sum() == 0

def test_shape_preserved(sample_df):
    result = clean_nulls(sample_df)
    assert result.shape[0] == 3  # 행 수 유지

# $ pytest tests/ -v
# $ pytest tests/ -x  # 첫 실패시 중단
```
- `@pytest.fixture`로 선언된 `sample_df`는 테스트 함수 인자로 넘기면 자동 주입됨.
- 분석 함수가 null을 올바르게 처리하는지, 원본 shape을 유지하는지 등을 단위 테스트로 명시적으로 검증할 수 있음.
---
### pytest-cov — 테스트 커버리지 측정
어떤 코드 경로가 테스트되지 않았는지 파악하는 도구로, MLOps 과목의 CI 파이프라인에서 필수 지표로 활용됨.
```bash
$ pip install pytest-cov

# 커버리지 포함 실행
$ pytest tests/ --cov=src --cov-report=term-missing
```
출력 예시:
```plain text
# Name             Stmts   Miss  Cover  Missing
# src/clean.py        25      3    88%  42-44, 67
# src/features.py     38      0   100%
# TOTAL               63      3    95%
```
- `Miss` 컬럼이 0이면 해당 파일은 100% 커버됨
- `Missing` 컬럼에 표시된 라인 번호가 테스트되지 않은 코드 경로임
- 커버리지 **80% 이상**을 목표로 설정하며, GitHub Actions CI와 동일한 설정으로 운용함
---
### black — 코드 포매터
black은 Python 코드의 스타일을 자동으로 정리하는 포매터임. PEP8을 기반으로 하지만 자체 규칙도 적용하며, 팀 간 코드 스타일 논쟁을 제거하고 git diff를 읽기 좋게 유지하는 것이 목적임.
> "당신의 스타일은 중요하지 않다. 일관성이 더 중요하다."
#### 설치 및 사용방법
```bash
pip install black
```
| 목적 | 명령 |
| --- | --- |
| 현재 디렉토리 하위 전체 `.py` 자동 정리 | `black .` |
| 특정 파일만 포매팅 | `black src/mymodule/core.py` |
| 수정 없이 변경 필요 여부만 확인 (check 모드) | `black --check src/` |
- `-check` 모드는 실제로 파일을 수정하지 않고 포맷 변경이 필요한지만 검사함. CI(GitHub Actions 등)에서 유용하게 쓰임.
- 프로젝트 전체에 적용할 경우 `requirements.txt` 또는 `pyproject.toml`에 추가해 관리함.
---
### black — 주요 포매팅 규칙
```python
# BEFORE
def my_func( a=1,b=2 ): return a+b

# AFTER (by black)
def my_func(a=1, b=2):
    return a + b
```
| 항목 | 설명 |
| --- | --- |
| 들여쓰기 | 공백 4칸 (PEP8과 동일) |
| 줄 길이 | 기본 88자 (PEP8의 79자보다 완화) |
| 괄호 감싸기 | 함수 인자가 길면 자동으로 줄바꿈 및 괄호 사용 |
| 문자열 | `'` 또는 `"` 중 하나로 통일 (보통 `'`) |
| 연산자 공백 | 연산자 앞뒤 공백 유지 (`a + b`) |
---
### black — pyproject.toml 설정
black은 설정 파일로 `pyproject.toml`을 사용함.
```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''
```
| 항목 | 설명 |
| --- | --- |
| `line-length` | 최대 줄 길이 |
| `target-version` | 지원하는 Python 버전 (예: py310) |
| `include` | 대상 파일 패턴 |
| `exclude` | 무시할 폴더/파일 정규식 |
---
### black — pre-commit / GitHub Actions 연동
#### pre-commit 연동
```yaml
# .pre-commit-config.yaml
- repo: https://github.com/psf/black
  rev: 24.3.0
  hooks:
    - id: black
```
`pre-commit install` 실행 후, git commit 전에 자동으로 포매팅이 적용됨.
#### GitHub Actions 연동
yaml
```yaml
# .github/workflows/ci.yml
- name: Run black
  run: black --check .
```
CI에서 `--check` 모드로 실행해 포맷이 맞지 않으면 파이프라인을 실패시킴.
---
### black — 장점 및 주의사항
| 구분 | 항목 | 설명 |
| --- | --- | --- |
| 장점 | 자동화 | 사람 개입 없이 스타일 정리 |
| 장점 | 일관성 | 누구나 같은 결과 |
| 장점 | 빠름 | 대규모 프로젝트도 빠르게 포매팅 |
| 장점 | 통합 | pre-commit, CI/CD에 쉽게 통합 가능 |
| 주의사항 | 커스터마이징 제한 | 스타일 규칙이 강제적이라 세부 조정 불가 |
| 주의사항 | flake8과 충돌 가능성 | 줄 길이 등 규칙 차이로 충돌이 생길 수 있음 |
| 주의사항 | 전체 변경 위험 | 기존 코드 스타일이 많으면 차이가 크게 발생할 수도 있음 |
---
### \[참고\] PEP8 (Python Enhancement Proposal)
- \*PEP(Python Enhancement Proposal)\*\*는 Python 언어에 새로운 기능, 스타일, 정책 등을 제안할 때 작성하는 공식 문서임.
주요 PEP 예시:
- **PEP 8** — Style Guide for Python Code (스타일 가이드)
- **PEP 7** — C 코드 스타일 가이드 (CPython C 코어 개발자용)
- **PEP 484** — 타입 힌트 제안
- **PEP 572** — 할당 표현식 (`:=`)
#### PEP 8이란
| 항목 | 설명 |
| --- | --- |
| 번호는 순번 | 8번째 제안서. 스타일 가이드 버전 8이 아님 |
| 2001년 발표 | Python 창시자 Guido van Rossum 외 여러 코어 개발자 공동 작성 |
| 목적 | "코드는 읽는 사람이 많고, 작성하는 사람보다 더 많다"는 원칙으로 일관되고 가독성 좋은 코딩 스타일 제안 |
| 기반 도구 | black, flake8, isort |
---
### pre-commit — 자동 검사 Hook
**pre-commit**은 Git의 커밋 전(pre-commit) 시점에 특정 검사를 자동 실행하는 도구임. Git은 커밋 전/후 등 특정 시점에 자동 실행되는 Hook 기능을 제공하는데, pre-commit은 그 중 커밋 직전에 코드 포매팅·린트·타입 검사·보안 검사 등을 실행해 문제 있는 코드의 커밋을 차단함.
> 코드 품질을 "Git 단계에서" 지키기 위한 자동 방어
#### 설치 및 실행
```bash
pip install pre-commit
pre-commit install
```
설치 후 `.git/hooks/pre-commit` 스크립트가 자동 생성되어 Git 커밋 전에 실행됨.
| 실행 방법 | 명령 |
| --- | --- |
| 전체 파일 한 번에 검사 | `pre-commit run --all-files` |
| 커밋 시 자동 실행 | `git add .` → `git commit -m "..."` |
커밋 시 black, flake8, mypy 등이 자동 실행되며, 실패 시 커밋이 중단됨.
---
### pre-commit — .pre-commit-config.yaml 구성
`.pre-commit-config.yaml`에 사용할 도구와 버전을 명시함.
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
```
| 키 | 설명 |
| --- | --- |
| `repo` | 도구의 Git 저장소 |
| `rev` | 사용할 버전 태그 |
| `hooks` | 사용할 검사 항목 (black, flake8, mypy 등) |
---
### pre-commit — 사용 흐름
```bash
# 1. 설정 파일 작성 (.pre-commit-config.yaml)
# 2. 설치
pre-commit install

# 3. 모든 파일 검사
pre-commit run --all-files

# 4. 커밋 시 자동 검사 실행됨
git commit -m "Initial commit"
```
- black, flake8, mypy를 pre-commit에 연결해두면, 오류가 나면 커밋이 차단되고 수정 후 다시 add/commit하면 됨.
---
### pre-commit — 추가 기능 및 장점
`pre-commit-hooks` 패키지를 통해 black/flake8 외 다양한 기본 검사도 추가할 수 있음.
```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.5.0
  hooks:
    - id: check-added-large-files
    - id: check-merge-conflict
    - id: check-yaml
    - id: debug-statements
```
- `debug-statements`는 `print()` 같은 디버깅 코드가 남아있을 경우 커밋을 차단함.
| 항목 | 설명 |
| --- | --- |
| 코드 품질 보장 | 린트, 포맷, 타입 검사를 자동 수행 |
| 협업 시 실수 방지 | 커밋 전에 자동 검사로 오류 방지 |
| 자동화 쉬움 | Git hook에 자동으로 붙음 |
| CI 연동 가능 | GitHub Actions와도 호환 |
---
### pre-commit · requirements.txt · 재현 환경
```python
# .pre-commit-config.yaml (Ruff 사용 예시)
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  hooks:
    - id: ruff
      args: [--fix]
    - id: ruff-format
```
```bash
$ pre-commit install   # git hook 등록
$ pre-commit run --all-files  # 전체 검사

# 환경 재현
$ pip freeze > requirements.txt
$ pip install -r requirements.txt

# .gitignore 필수 항목
# .venv/ .env __pycache__/ *.pyc .coverage
```
- `requirements.txt`: `pip freeze`로 현재 설치된 패키지 버전을 고정해 저장함. `pip install -r requirements.txt`로 동일 환경을 1분 내에 재현할 수 있음.
- `pyproject.toml`: 현대적 프로젝트 설정 방식으로, black·mypy 등 도구 설정을 한 파일에 통합 관리함.
- `.gitignore`에 가상환경·캐시 디렉토리를 반드시 추가해야 불필요한 파일이 저장소에 올라가지 않음.
---
### GitHub Actions CI 설정
`.github/workflows/ci.yml`에 작성하며, push 또는 pull_request 시 자동으로 품질 검사와 테스트가 실행됨.
```yaml
name: CI - Lint & Test
on: [push, pull_request]

jobs:
  quality-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run black
        run: black --check .

      - name: Run flake8
        run: flake8 .

      - name: Run mypy
        run: mypy src/

      - name: Run pytest
        run: pytest
```
- `requirements.txt`에 pytest, black, flake8, mypy, pre-commit이 포함되어 있어야 CI에서 설치됨.
- 각 step이 순서대로 실행되며, 하나라도 실패하면 이후 단계가 중단됨.
---
### 실전 적용 흐름 (예시)
코드 작성부터 CI까지의 전체 흐름을 단계별로 정리하면 아래와 같음.
1. 개발자는 `src/`와 `tests/` 디렉토리에 코드를 작성
2. `git commit` 시 black, flake8, mypy가 pre-commit hook으로 자동 실행
3. 로컬에서 `pytest`로 테스트 실행
4. GitHub에 Push → GitHub Actions로 품질 검사 및 테스트 자동 실행
---
### VS Code 연동 팁
`.vscode/settings.json`에 아래 설정을 추가하면 저장 시 자동 포맷·실시간 린트·타입 검사가 모두 활성화됨.
```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true
}
```
GitHub 프로젝트 초기 세팅 시 이 파일을 저장소에 포함시키면 팀 전체의 코드 품질과 협업 효율을 동시에 향상시킬 수 있음.
---
### Ruff — 2026 Python 린팅·포매팅 표준
Ruff는 flake8 + black + isort를 하나로 대체하는 통합 린터·포매터임. Rust로 작성되어 기존 도구 대비 10–100배 빠르며, 2026년 기준 Python 생태계의 사실상 표준으로 자리잡음.
#### 핵심 특징
- `-fix` 옵션으로 자동 수정 가능한 오류를 일괄 처리함
- `E·F·I·UP` 규칙 그룹: 에러·경고·임포트 정렬·업그레이드 권고
- VS Code 저장 시 자동 포맷 설정 가능
```bash
$ pip install ruff

# 린팅 검사
$ ruff check .

# 자동 수정 (가능한 항목)
$ ruff check --fix .

# 포매팅
$ ruff format .
```
```toml
# pyproject.toml
[tool.ruff]
line-length = 88
select = ['E','F','I','UP']
ignore = ['E501']  # 긴 줄 무시

[tool.ruff.format]
quote-style = 'double'
indent-style = 'space'
```
---
### VS Code 디버거와 코드 품질 도구 통합 활용
| 기능 | 방법 |
| --- | --- |
| 중단점(Breakpoint) 활용 | F9로 중단점 설정 → F5 실행 → 변수 인스펙터로 DataFrame 내용 실시간 확인. print 디버깅 불필요 |
| Ruff 저장 자동 포맷 | `settings.json`에 `editor.formatOnSave: true` + `editor.defaultFormatter: charliermarsh.ruff` 설정 |
| pytest Test Explorer | VS Code Python Test Explorer 확장 설치 → 사이드바에서 테스트 실행·결과 확인. TDD 워크플로에 유용 |
| Pylance 타입 검사 | `python.analysis.typeCheckingMode: basic` 설정 → 저장할 때마다 타입 오류를 빨간 밑줄로 즉시 표시 |
---
### 코드 품질 도구가 데이터 분석 팀에 필요한 이유
| 영역 | 이유 |
| --- | --- |
| 분석 코드도 팀이 공유한다 | 혼자 만든 분석 스크립트도 GitHub에 올리는 순간 팀 자산이 됨. Ruff·pytest가 없으면 리뷰가 어려움 |
| 재현 가능한 분석 = 신뢰 | 6개월 뒤 같은 결과가 나오는 분석이 좋은 분석. `requirements.txt` + 테스트가 재현성을 보장함 |
| MLOps CI/CD 기반 | DevOps·MLOps 과목에서 GitHub Actions로 pytest + Ruff를 자동 실행. 지금 배운 설정을 그대로 사용함 |
| 디버거 \> print() 탈출 | 데이터 분석에서 DataFrame 상태를 print로 찍는 건 비효율. 중단점으로 컬럼·타입·값을 즉시 확인하는 습관이 필요함 |
---
### 동시성 vs 병렬성 — 개념과 선택 기준
| 구분 | 동시성(Concurrency) | 병렬성(Parallelism) |
| --- | --- | --- |
| 도구 | asyncio + httpx | multiprocessing |
| 실행 방식 | 한 스레드, 대기 중 다른 작업 실행 | 여러 프로세스, 진짜 동시 실행 |
| 적합한 작업 | I/O bound: API 호출, 파일 읽기 | CPU bound: 수치 계산, 이미지 처리 |
| GIL 영향 | 영향 없음 (대기 중 전환) | GIL 우회 (별도 프로세스) |
| 데이터 분석 적용 | 공공 API 대량 수집, 비동기 DB 쿼리 | 대용량 파일 병렬 전처리, 모델 훈련 |
---
### 병렬처리 vs 병행처리 (Parallelism vs Concurrency)
| 구분 | 병렬처리(Parallelism) | 병행처리(Concurrency) |
| --- | --- | --- |
| 의미 | 동시에 여러 작업 실행 | 여러 작업을 빠르게 번갈아 실행 |
| 전제 | 멀티코어 필요 | 싱글코어도 가능 |
| 예시 | A와 B가 동시에 계산됨 | A를 하다가 B로 전환, 다시 A |
- 멀티코어 CPU가 있다면 `multiprocessing`으로 병렬처리 가능함
- 싱글코어 환경에서도 I/O 위주 작업은 `threading`으로 효율적 실행 가능함
---
### Python의 GIL(Global Interpreter Lock) — 개요
GIL은 Python(CPython)의 인터프리터에서 **하나의 스레드만 실행되도록 강제하는 락**임. CPU-bound 작업에서 병렬성 저하를 유발하지만, I/O-bound 작업에서는 큰 문제가 없음.
```python
import threading

def cpu_task():
    for _ in range(10**7):
        pass

threads = []
for _ in range(4):
    t = threading.Thread(target=cpu_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```
- 위 코드는 4개의 스레드를 만들지만 GIL 때문에 실질적으로는 하나씩 처리됨.
---
### GIL(Global Interpreter Lock) — 상세
| 구분 | 설명 |
| --- | --- |
| 개념 | Python의 단일 프로세스에서 한 번에 하나의 스레드만 실행할 수 있게 하는 잠금 |
| 목적 | 메모리 관리 동기화 보조, 여러 스레드가 동시에 같은 객체 접근·수정 시 데이터 충돌 방지. GIL을 통해 multithreading을 쉽게 구현하고 복잡한 동기화 문제를 처리함 |
| 동작원리 | 인터프리터 수준에서 동작. 여러 스레드를 사용하더라도 실제로 한 스레드만 CPU에서 실행됨. 주기적으로 실행 시간을 할당하고, 일정 시간 후 다음 스레드가 실행될 기회를 받음 |
| 작동 예시 | 4개의 스레드가 있으면, GIL은 그 중 한 스레드만 실행하고, 그 스레드가 멈추면 다른 스레드를 실행하는 방식으로 순차적으로 실행 |
---
### GIL — 문제점 및 회피 방법
#### 문제점
- 병렬성 제한: GIL 때문에 Python은 multithreading에서 진정한 병렬 실행이 불가함. CPU 집약 작업(수학적 계산, 데이터 처리, 암호화 등)에서 특히 성능 제한이 심함.
- 멀티코어 활용 불가: 여러 코어가 있어도 multithreading을 사용한 작업은 하나의 코어에서만 실행됨.
#### 회피 방법
- `multiprocessing` 사용: 각 프로세스가 독립적인 메모리 공간을 가지기 때문에 GIL 영향이 없어 병렬 처리 가능함.
- C 확장 모듈 사용: NumPy와 같이 C 언어로 작성된 고성능 라이브러리는 GIL을 해제하여 다중 코어에서 병렬 연산을 수행함.
---
### \[참고\] NumPy와 같은 라이브러리에서 GIL 해제
#### NumPy의 GIL 해제와 병렬 처리
배열 기반 연산을 C 레벨에서 처리하기 때문에 GIL을 해제하고 병렬 연산을 수행함.
```python
import numpy as np
import time

arr1 = np.random.rand(10000000)
arr2 = np.random.rand(10000000)

start_time = time.time()
result = arr1 + arr2  # NumPy가 내부적으로 최적화된 C 코드로 처리
end_time = time.time()
print(f"NumPy 배열 연산 시간:{end_time - start_time} 초")
```
#### NumPy의 병렬화와 BLAS 라이브러리
배열 연산에 BLAS(Basic Linear Algebra Subprograms) 라이브러리를 사용하며, OpenMP와 같은 라이브러리로 다중 스레드를 활용함.
```python
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)

start_time = time.time()
C = np.dot(A, B)  # NumPy 내부적으로 BLAS 라이브러리 사용
end_time = time.time()
print(f"행렬 곱셈 시간:{end_time - start_time} 초")
```
- `np.dot` 함수는 내부적으로 BLAS 라이브러리를 사용하여 병렬 연산을 수행하므로, 다중 코어 CPU를 활용해 연산이 훨씬 빠름.
---
### threading 모듈 (경량 병렬 처리, I/O-bound에 적합)
- 장점: 메모리 공유, 생성 빠름
- 단점: GIL로 인해 CPU-bound 작업에 비효율
```python
import threading

def worker(num):
    print(f"Thread{num} working")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
```
공유 변수 접근 시 `Lock`을 사용해 동기화해야 함.
```python
lock = threading.Lock()
shared = 0

def task():
    global shared
    for _ in range(100000):
        with lock:
            shared += 1
```
- `with lock:` 블록 안의 코드는 한 번에 하나의 스레드만 접근 가능함. 여러 스레드가 동시에 `shared`를 수정하면 데이터 오염이 발생하므로 Lock이 필수임.
---
### multithreading (Multithreading)
하나의 프로세스 내에서 여러 스레드를 사용하여 병렬적으로 작업을 처리하는 기법임. 스레드는 프로세스 내에서 실행되는 흐름으로, 같은 프로세스 내 메모리와 자원을 공유함.
```python
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```
- 두 스레드가 병렬로 실행되어 숫자와 알파벳을 동시에 출력함.
- `time.sleep(1)`로 각 스레드가 1초마다 일시 정지하도록 설정해 출력 순서를 확인할 수 있음.
- GIL 때문에 CPU 집약적인 작업에서는 성능 향상이 크지 않음. I/O 작업(파일 입출력, 네트워크 통신)에 주로 유리함.
---
### multiprocessing 모듈 (프로세스 기반 병렬처리)
각 프로세스는 별도 메모리 공간을 가지므로 GIL 회피가 가능하고, CPU-bound 작업에 유리함.
```python
from multiprocessing import Process

def task(name):
    print(f"{name} is working")

if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```
`Pool`을 사용하면 리스트를 여러 프로세스로 병렬 처리할 수 있음:
```python
from multiprocessing import Pool

def square(n):
    return n * n

with Pool(processes=4) as pool:
    result = pool.map(square, [1, 2, 3, 4])
    print(result)  # [1, 4, 9, 16]
```
- `if __name__ == "__main__":` 가드가 필수임. 없으면 자식 프로세스가 부모 코드를 재실행해 무한 생성될 수 있음.
---
### Multiprocessing — 상세
여러 개의 프로세스를 사용하여 작업을 병렬 처리하는 기법임. 각각의 프로세스는 독립된 메모리 공간과 자원을 갖고 실행되며, I/O 작업보다 CPU 집약적인 작업에서 유리함.
```python
import multiprocessing
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)

process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_letters)

process1.start()
process2.start()

process1.join()
process2.join()
```
- 두 프로세스가 완전히 독립적으로 실행되어 두 작업이 병렬로 실행됨.
- 각 프로세스는 별도의 메모리 공간을 갖기 때문에 서로 영향을 미치지 않음.
---
### queue vs multiprocessing.Queue
프로세스 간 데이터를 주고받으려면 일반 `queue.Queue`가 아닌 `multiprocessing.Queue`를 사용해야 함.
| 구분 | queue.Queue | multiprocessing.Queue |
| --- | --- | --- |
| 대상 | 스레드 간 | 프로세스 간 |
| 공유 가능 여부 | 메모리 공유 가능 | 메모리 공유 불가 (직렬화 필요) |
```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from child")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Hello from child
    p.join()
```
- 프로세스 간에는 메모리가 분리되어 있으므로, 데이터 전달을 위해 직렬화(pickling) 과정을 거쳐 Queue에 넣고 꺼내는 방식을 사용함.
---
### multithreading vs multiprocessing 비교
| 특징 | multithreading | multiprocessing |
| --- | --- | --- |
| 작업 단위 | 스레드 | 프로세스 |
| 메모리 공유 | 같은 프로세스 내에서 공유 | 별도의 메모리 공간을 가짐 |
| GIL(Python) | GIL로 인해 CPU 집약 작업에서 성능 향상 한계 | GIL 영향 받지 않음, CPU 집약 작업에서 성능 향상 |
| 적합한 작업 | I/O 작업 (파일 입출력, 네트워크 등) | CPU 집약적인 작업 (계산, 데이터 처리 등) |
| 자원 소비 | 프로세스 내에서 자원 공유, 상대적으로 적음 | 각 프로세스마다 독립적인 자원 사용, 더 많은 자원 소비 |
---
### Threading vs Multiprocessing 선택 기준
| 상황 | 추천 방식 |
| --- | --- |
| I/O-bound | threading |
| CPU-bound | multiprocessing |
| 많은 수의 작업 | `concurrent.futures.ThreadPoolExecutor` / `ProcessPoolExecutor` |
---
### multithreading vs multiprocessing 선택 기준 (상세)
| multithreading을 선택할 때 | multiprocessing을 선택할 때 |
| --- | --- |
| I/O 작업이 많은 경우 (파일 읽기/쓰기, 네트워크 요청) | CPU 집약적인 작업이 많은 경우 (복잡한 계산, 데이터 처리) |
| 스레드 간의 메모리 공유가 중요한 경우 | 작업이 독립적이고 메모리 공유가 필요 없는 경우 |
| GIL이 성능에 큰 영향을 미치지 않는 경우 (I/O 작업) | GIL을 회피하여 성능을 극대화하고 싶은 경우 |
---
### FastAPI, AI 모델 처리에서의 병렬처리 응용
#### FastAPI + BackgroundTasks
```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def process_file(file_id: int):
    # 병렬 처리할 작업
    ...

@app.post("/upload/")
def upload(file_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_file, file_id)
    return {"status": "processing"}
```
응답을 즉시 반환하고 무거운 처리는 백그라운드에서 수행하는 패턴임.
#### AI 모델 병렬 추론 (GPU or Multi-core CPU 기반)
```python
from torch.utils.data import DataLoader

loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)
```
- `num_workers=4`: 데이터를 미리 로딩하고 전처리하기 위한 서브 프로세스 수를 의미함.
- 딥러닝 모델은 빠른 연산이 가능하지만, 데이터를 CPU에서 로딩·전처리하는 속도가 느리면 GPU가 Idle(대기) 상태가 됨.
- `num_workers > 0`으로 설정하면 데이터 로딩을 다중 프로세스로 병렬화하여 GPU가 다음 데이터를 기다리지 않도록 미리 준비(pre-fetching)함.
---
### multiprocessing — CPU bound 병렬 처리
```python
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

def process_chunk(chunk):
    # CPU 집중 전처리
    return [transform(row) for row in chunk]

def split_chunks(data, n):
    size = len(data) // n
    return [data[i*size:(i+1)*size] for i in range(n)]

n_cores = mp.cpu_count()  # macOS M1: 8코어
chunks = split_chunks(all_data, n_cores)

with ProcessPoolExecutor(max_workers=n_cores) as exe:
    results = list(exe.map(process_chunk, chunks))
# 8코어: 이론상 8× 속도 향상
```
- `ProcessPoolExecutor`: `concurrent.futures` 모듈이 제공하는 간편한 병렬 처리 API임.
- `Pool.map` / `exe.map`: 리스트를 여러 프로세스로 병렬 처리하며, 순서를 보장함.
- `max_workers`를 CPU 코어 수 기준으로 설정함.
- chunk 분할: 대용량 데이터를 N등분해 각 프로세스에 할당함. 프로세스 간 데이터 전달에 직렬화 비용이 발생하므로 chunk 크기를 적절히 조절해야 함.
---
### GIL(Global Interpreter Lock) — Python 동시성의 핵심 제약
```python
import threading

# CPU bound — threading 효과 없음 (GIL 때문)
def cpu_task():
    return sum(range(10**7))

# I/O bound — threading 효과 있음
import time
def io_task():
    time.sleep(1)  # GIL 해제됨

# NumPy: GIL 해제로 병렬 연산
import numpy as np
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)
C = np.dot(A, B)  # BLAS: GIL 없이 멀티스레드
```
- CPython에서 한 번에 하나의 스레드만 Python 코드를 실행함.
- CPU-bound 작업에서 threading은 효과 없음. I/O-bound 작업은 대기 중 GIL이 해제되므로 threading이 효과적임.
- NumPy는 C 확장으로 GIL을 해제하여 병렬 연산을 수행함.
- Python 3.13+에서 GIL 옵션 제거 실험이 진행 중임.
---
### asyncio + httpx — 비동기 API 데이터 수집
```python
import asyncio, httpx

async def fetch(client, url):
    try:
        r = await client.get(url, timeout=10)
        return r.json()
    except Exception as e:
        return {'error': str(e)}

async def fetch_all(urls):
    async with httpx.AsyncClient() as c:
        tasks = [fetch(c, u) for u in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

# 실행: 100개 URL 동시 수집
urls = [f'https://api.example.com/data/{i}' for i in range(100)]
results = asyncio.run(fetch_all(urls))
# 순차: ~100초 → 비동기: ~2초
```
- `async def / await`: 비동기 함수 정의와 호출에 사용함.
- `asyncio.gather()`: 여러 태스크를 동시에 실행하고 모든 결과를 기다림.
- `httpx.AsyncClient`: 비동기 HTTP 클라이언트. 동기 `requests` 대신 사용함.
- `return_exceptions=True`: 일부 요청이 실패해도 전체가 중단되지 않고 예외를 결과로 반환함.
- `asyncio.run()`: 이벤트 루프를 시작하고 코루틴을 실행함.
---
### timeit · cProfile · memory_profiler — 성능 측정
```python
import timeit, cProfile, sys

# timeit: 반복 측정으로 정확도 향상
t = timeit.timeit(
    '"".join(my_list)',
    setup="my_list=['a']*1000",
    number=10000
)
print(f'{t:.4f}초')  # 평균 실행 시간

# cProfile: 전체 함수 호출 분석
cProfile.run('heavy_analysis(df)', sort='cumtime')

# sys.getsizeof: 메모리
lst = list(range(10000))
gen = (x for x in range(10000))
print(sys.getsizeof(lst))  # ~87KB
print(sys.getsizeof(gen))  # ~104B
```
- `timeit`: 코드 조각 실행 시간을 정밀 측정함. 반복 횟수(`number`)를 늘려 평균을 구함.
- `cProfile`: 함수별 호출 횟수와 소요 시간을 분석해 병목 함수를 찾음. `sort='cumtime'`으로 누적 시간 기준 정렬 가능함.
- `sys.getsizeof`: 객체의 메모리 크기를 shallow 방식으로 측정함. 리스트는 \~87KB, 제너레이터는 \~104B로 메모리 차이가 큼.
- `memory_profiler`: `@profile` 데코레이터로 라인별 메모리 사용량 추적 가능함.
- VS Code에서 cProfile 결과를 시각화하는 확장을 활용하면 병목 파악이 더 쉬움.
---
### 비동기·병렬 처리가 데이터 분석가에게 필요한 이유
| 영역 | 이유 |
| --- | --- |
| API 수집 속도 100× 향상 | 공공 API 100개를 순차 호출하면 100초, asyncio 동시 호출하면 \~2초 |
| 대용량 전처리 병렬화 | 수십 GB CSV를 multiprocessing으로 분할 처리. macOS M1 8코어 → 이론상 8× 속도 향상 |
| 병목 찾기 → 올바른 최적화 | 느리다고 느낌으로 최적화하면 안 됨. cProfile로 어느 함수가 느린지 먼저 측정한 후 최적화해야 함 |
| 후속 과목 기반 — 모두 async | LangChain·RAG·AI Agent 과목은 전부 async 기반 코드. 지금 개념 없이는 코드 구조 이해가 어려움 |
---
<empty-block/>
