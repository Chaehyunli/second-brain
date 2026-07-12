---
title: "[아키텍처] 제어 유니트(Control Unit) 란?"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "ARCHITECTURE"
published: 2025-04-09
source_url: https://ch010104.tistory.com/52
archive_method: Tistory sitemap + HTML content extraction
---

# [아키텍처] 제어 유니트(Control Unit) 란?

> 원문: https://ch010104.tistory.com/52

## 본문

1. 제어 유니트의 기능  명령어 코드의 해독 명령어 실행을 위한 제어 신호 생성     CPU 내에서 **명령어 사이클(인출 → 간접 → 실행 → 인터럽트)**이 순차적으로 수행되도록 제어 신호를 발생시킴.    마이크로연산(Micro-operation): 하나의 명령어 실행 과정에서 수행되는 가장 작은 동작 단위 (ex. MAR ← PC) 마이크로명령어(Microinstruction): 마이크로연산을 2진 비트로 표현한 것 (제어 단어) 마이크로프로그램(Microprogram): 마이크로명령어들의 집합 루틴(Routine): CPU 기능별로 정의된 마이크로프로그램 단위  즉, CPU 클록 주기마다 서로 다른 마이크로-연산이 수행됨.  2. 제어 유니트의 구조     구성 요소 기능 설명   명령어 해독기 IR의 연산 코드 해독 → 루틴 시작 주소 결정   CAR (제어 주소 레지스터) 현재 또는 다음 마이크로명령어의 주소 저장   제어 기억장치 (ROM) 마이크로프로그램 저장 공간   CBR (제어 버퍼 레지스터) 제어 기억장치에서 읽어온 마이크로명령어 임시 저장   SBR (서브루틴 레지스터) 서브루틴 호출 시 원래 CAR 값 저장   순서제어 모듈 마이크로명령어 실행 순서 결정       제어 기억장치는 ROM 형태이며, 마이크로명령어의 루틴들을 저장. 사상(Mapping): 연산 코드를 통해 실행 루틴의 시작 주소를 결정하는 방식⮕ 주소 형식: 1xxxx00 (최상위 비트는 1, 다음 4비트는 연산 코드)   3. 마이크로명령어 형식       필드 설명   연산 필드 1, 2 동시에 2개의 마이크로연산 수행 가능   조건 필드 (CD) 분기 조건 지정 (U, I, S, Z)   분기 필드 (BR) 분기 방식 (JMP, CALL, RET, MAP)   주소 필드 (ADF) 분기 시 이동할 주소 값     1) 연산 필드 1,2 의 마이크로-연산들 연산 필드 1  연산 필드 2   2) 조건 필드의 마이크로-연산들(CD)   3) 분기 필드의 마이크로-연산들(BR)    수직적 마이크로프로그래밍: 연산 필드 값은 코딩되어 있고, 디코더를 통해 제어 신호 확장 (용량 ↓, 속도 ↓) 수평적 마이크로프로그래밍: 연산 필드 값이 제어 신호와 1:1 대응 (속도 ↑, 용량 ↑)   4 마이크로프로그래밍 1) 인출 사이클 루틴 (Fetch Cycle Routine)   - 기억장치에서 명령어를 읽어와 IR에 적재하는 과정      마이크로명령어  CD(조건 필드) BR(분기 필드) ADF(주소 필드) 연산 내용   PCTAR U JMP NEXT MAR ← PC   READ, INCPC U JMP NEXT MBR ← M[MAR], PC ← PC + 1   BRTIR U MAP - IR ← MBR + 실행 루틴으로 분기      2) 간접 사이클 루틴 (Indirect Cycle Routine)     - 명령어에 포함된 주소가 실제 오퍼랜드의 주소가 아닌 포인터일 경우 → 유효 주소를 읽어오는 사이클          마이크로명령어   CD(조건 필드) BR(분기 필드) ADF(주소 필드) 연산 내용   IRTAR U JMP NEXT MAR ← IR(addr)   READ U JMP NEXT MBR ← M[MAR]   BRTIR U RET - IR(addr) ← MBR + 호출한 실행 루틴으로 복귀      3) 실행 사이클 루틴 (Execution Cycle Routine)     - 명령어에 따라 실제 연산이 수행되는 루틴      명령어별 시작 주소는 사상(MAP) 방식으로 결정됨(예: ADD → 76번지, LOAD → 68번지)  예시) X = A + B 연산이 있을 때:     명령어 설명   ADD AC ← AC + MBR   STORE M[X] ← AC   LOAD AC ← M[A]      4.5 마이크로프로그램의 순서제어       - 제어 유니트는 각 마이크로명령어의 분기 조건(CD), 분기 타입(BR), 주소 필드(ADF)를 기반으로 다음 실행 주소 결정         BR(분기 필드) CD(분기 조건 필드) MUX1 선택 SBR CAR로 적재한 주소 설명   00 0 0 - CAR ← CAR + 1 조건 불충족   00 1 1 - CAR ← ADF 조건 만족 시 분기   01 1 1 ✔ SBR ← CAR+1, CAR ← ADF 조건 만족 시 서브루틴 호출   10 - - - CAR ← SBR 서브루틴 복귀   11 - - - CAR ← 1XXXX00 사상(MAP) 주소로 분기
