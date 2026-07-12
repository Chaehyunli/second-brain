---
title: "[데이터베이스 설계] 회복 시스템(Recovery System)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "DATABASE DESIGN"
published: 2025-11-24
source_url: https://ch010104.tistory.com/192
archive_method: Tistory sitemap + HTML content extraction
---

# [데이터베이스 설계] 회복 시스템(Recovery System)

> 원문: https://ch010104.tistory.com/192

## 본문

1. 회복 시스템 개요 (Recovery System Overview)  기본 개념  컴퓨터 시스템은 디스크 충돌, 전원 차단, 소프트웨어 오류 등 다양한 원인으로 장애가 발생할 수 있음 데이터베이스 시스템은 원자성(Atomicity)과 지속성(Durability)을 보장하기 위한 조치를 취해야 함 회복 기법(Recovery scheme)을 통해 장애 발생 이전의 일관된(Consistent) 상태로 복구하고 고가용성(High Availability)을 제공함   회복 알고리즘의 구성  정상 수행 중 조치: 장애 복구를 위해 필요한 정보를 기록 장애 후 조치: 데이터베이스 내용을 원자성, 일관성, 지속성이 보장된 상태로 복구    2. 장애 유형 분류 (Failure Classification)  트랜잭션 실패 (Transaction Failure)  논리적 오류 (Logical errors): 잘못된 입력, 데이터 부재, 오버플로우 등 내부 로직 오류로 인해 트랜잭션 수행 불가 시스템 오류 (System errors): 트랜잭션 자체는 문제없으나 교착 상태(Deadlock) 등 DBMS의 문제로 인해 시스템이 트랜잭션을 중단시키는 경우   시스템 붕괴 (System Crash)  하드웨어 오작동, 소프트웨어 오류, 전원 문제 등으로 시스템이 멈추는 현상 Fail-stop 가정: 비휘발성 저장 장치의 내용은 손상되지 않았다고 가정함   디스크 실패 (Disk Failure)  헤드 충돌 등으로 디스크 저장 장치의 일부 또는 전체가 파괴되는 현상 체크섬(Checksum) 등을 통해 감지 가능하다고 가정함    3. 저장 장치 구조 (Storage Structure)  휘발성 저장 장치 (Volatile Storage)  시스템 붕괴 시 데이터가 손실됨 (예: 메인 메모리, 캐시 메모리)   비휘발성 저장 장치 (Non-volatile Storage)  시스템 붕괴 후에도 데이터가 유지되나, 디스크 실패 시 데이터 손실 가능 (예: 디스크, 테이프, 플래시 메모리)   안정 저장 장치 (Stable Storage)  어떤 장애에도 데이터가 손실되지 않는 이상적인 저장 장치 물리적으로 독립된 여러 비휘발성 매체에 복제본을 유지하여 근사적으로 구현    4. 안정 저장 장치 구현 (Stable-Storage Implementation)  데이터 전송 실패 유형  성공 (Successful completion): 정상적으로 정보가 전송됨 부분 실패 (Partial failure): 전송 중 장애로 인해 목적지 블록에 부정확한 정보가 기록됨 전체 실패 (Total failure): 목적지 블록이 전혀 업데이트되지 않음.   보호 기법 (블록 복제 방식)  각 블록의 복제본을 유지하며 다음과 같은 순서로 쓰기(output) 작업을 수행       1. 첫 번째 물리 블록에 정보를 쓴다. 2. 첫 번째 쓰기가 성공하면, 두 번째 물리 블록에 동일한 정보를 쓴다. 3. 두 번째 쓰기까지 성공해야 output 작업이 완료된 것으로 간주한다.      복구 알고리즘 (Recover from failure)  두 블록 간 불일치 발견 시 해결 방법:     1. 한쪽 복제본에 오류(Bad checksum)가 감지되면, 다른 쪽 정상 복제본으로 덮어쓴다. 2. 둘 다 오류는 없으나 내용이 다를 경우, 첫 번째 블록의 내용을 두 번째 블록에 덮어쓴다. (첫 번째 블록의 쓰기가 성공했다면 그것이 최신 데이터일 가능성이 높기 때문)       5. 데이터 접근 (Data Access)    블록 구조  물리 블록 (Physical blocks): 디스크에 존재하는 블록 시스템 버퍼 블록 (System buffer blocks): 메인 메모리에 임시로 존재하는 블록. 블록 이동 연산:     input(B): 물리 블록 B를 메인 메모리로 전송 output(B): 버퍼 블록 B를 디스크로 전송하고 교체      트랜잭션 작업 공간 (Private Work-Area)  각 트랜잭션 T_i는 접근하는 데이터 항목의 로컬 사본을 저장하는 개별 작업 공간을 가짐 x_i: 데이터 항목 $X$의 로컬 사본 (트랜잭션 내 변수) B_X: X를 포함하고 있는 블록 데이터 전송 연산:     read(X): 데이터 항목 X의 값을 로컬 변수 x_i에 할당 write(X): 로컬 변수 x_i의 값을 버퍼 블록의 데이터 항목 X에 할당      접근 규칙 및 절차  Read 동작 (read(X)):   블록 B_X가 메인 메모리에 없으면 input(B_X) 수행. 버퍼 블록에서 값을 가져와 x_i에 할당   Write 동작 (write(X)):   블록 B_X가 메인 메모리에 없으면 input(B_X) 수행 (쓰기 작업이라도 버퍼에 없으면 디스크에서 읽어와야 함). x_i의 값을 버퍼 블록 B_X의 X에 반영   실행 시점:  write(X)는 트랜잭션 커밋(Commit) 전 언제든 실행 가능. output(B_X) (디스크 기록)가 write(X) 직후에 수행될 필요는 없음 (시스템이 적절한 시점에 수행)
