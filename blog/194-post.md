---
title: "[데이터베이스 설계] 트랜잭션 복구 및 데이터 접근"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "DATABASE DESIGN"
published: 2025-11-26
source_url: https://ch010104.tistory.com/194
archive_method: Tistory sitemap + HTML content extraction
---

# [데이터베이스 설계] 트랜잭션 복구 및 데이터 접근

> 원문: https://ch010104.tistory.com/194

## 본문

1. 원자성 및 복구 (Recovery and Atomicity)  목표: 시스템 실패에도 불구하고 원자성(Atomicity)과 내구성(Durability)을 보장 원칙: 데이터베이스 자체를 수정하기 전에, 수정 내용을 기술하는 정보를 먼저 안정된 저장 장치(stable storage)에 출력해야 함 Log-Based Recovery (로그 기반 복구):  Redo (복구): 커밋된 트랜잭션의 변경 내용 중 디스크에 미처 기록되지 못한 내용을 로그를 보고 다시 적용하여 영속성을 보장함 Undo (취소): 중단된/완료되지 않은 트랜잭션의 변경 내용을 로그의 이전 값(V1)을 보고 되돌려 원자성을 보장함   로그 파일: 안정된 저장 장치(stable storage)에 보관되며, 데이터베이스의 갱신 활동에 대한 정보를 유지하는 로그 레코드들의 연속체임   2. 로그 레코드 형식 (Log Record Format) 트랜잭션 T_i에 대한 로그 레코드 형식   트랜잭션 시작:   <Ti start>   데이터 쓰기 (갱신): T_i가 X에 쓰기 작업을 수행하기 전에 기록됨     <Ti, X, V1, V2>      V1: 쓰기 직전의 이전 값 (Old Value)8888. V2: 쓸 새 값 (New Value)  트랜잭션 커밋:    <Ti commit>   트랜잭션 중단:     <Ti abort>     중요 원칙: 갱신 로그 레코드(log record)는 데이터베이스 항목이 쓰이기 전에 안정된 저장 장치(stable storage)에 출력되어야 함  3. 데이터베이스 수정 방식 (Database Modification Schemes)  로그를 사용하는 두 가지 접근 방식이 있음  A. Immediate Database Modification (즉시 수정 방식)  특징: 커밋되지 않은 트랜잭션의 갱신 내용도 버퍼 또는 디스크 자체에 반영하는 것을 허용함. 디스크 반영 시점: 갱신된 블록의 디스크 출력은 트랜잭션 커밋 전후 언제든지 발생 가능함. 필요한 연산: Undo와 Redo 모두 필요함 (미커밋 변경 사항이 디스크에 기록되었을 수 있기 때문).  B. Deferred Database Modification (지연 수정 방식)  특징: 갱신을 트랜잭션이 커밋하는 시점에만 버퍼/디스크에 반영함 필요한 연산: Redo만 필요함 (미커밋 트랜잭션의 변경 사항이 디스크에 기록되지 않았음이 보장되기 때문) 본 자료의 초점: Immediate-modification scheme을 다룸.   4. Undo 및 Redo 연산 (Undo and Redo Operations)  Undo: 로그 레코드 <Ti, X, V1, V2>에 따라 X의 값을 이전 값 V1로 설정함.   트랜잭션 T_i의 undo(Ti): T_i가 갱신한 모든 데이터 항목의 값을 이전 값으로 복원하며, T_i의 마지막 로그 레코드부터 역순으로 진행함 Compensation Log Record (CLR): Undo 중 데이터 항목 X가 이전 값 V로 복원될 때, 특별한 로그 레코드 <Ti, X, V>를 로그에 기록함 (redo-only) Undo 완료 시, <Ti abort>를 로그에 기록함   Redo: 로그 레코드 <Ti, X, V1, V2>에 따라 $X의 값을 새 값 V2로 설정함  트랜잭션 T_i의 redo(Ti): T_i가 갱신한 모든 데이터 항목의 값을 새 값으로 설정하며, T_i의 첫 번째 로그 레코드부터 순방향으로 진행함 Redo 시에는 별도의 로깅을 하지 않음     5. 트랜잭션 커밋 (Transaction Commit)  트랜잭션의 커밋 로그 레코드가 안정된 저장 장치에 출력되었을 때, 해당 트랜잭션은 커밋된 것으로 간주됨 커밋 로그 레코드가 출력되기 전에, 해당 트랜잭션의 모든 이전 로그 레코드가 먼저 출력되어야 함 트랜잭션이 커밋된 후에도, 트랜잭션이 수행한 쓰기 작업은 버퍼에 남아있다가 나중에 출력될 수 있음   6. 시스템 실패 시 복구 (Recovery from Failure) 시스템 실패 후 복구 시, 트랜잭션의 상태에 따라 Redo 또는 Undo가 결정    로그 상태 필요한 복구 작업 사유     <Ti start>는 있지만, <Ti commit> 또는 <Ti abort>가 없음 Undo      트랜잭션이 완료되지 않고 시스템이 다운된 경우 (원자성 확보 필요)       <Ti start>와 <Ti commit> 또는 <Ti abort>가 모두 있음 Redo    커밋되었으나 디스크에 반영되지 않은 변경을 재반영하거나, Undo가 불완전했을 경, Repeating History 원칙에 따라 복구 알고리즘의 단순성/안정성을 확보함         Immediate Modification 복구 예시 다음은 T_0가 A=1000을 950으로, B=2000을 2050으로 변경하고, T_1이 C=700을 600으로 변경하는 상황에서 시스템 실패가 발생했을 때의 복구 행동  로그 상태 (a):복구 행동: undo(T0). B를 2000으로, A를 1000으로 복원하고, <T0, B, 2000>, <T0, A, 1000>, <T0 abort>를 로그에 기록함    <T0 start> <T0, A, 1000, 950> <T0, B, 2000, 2050>     로그 상태 (b):복구 행동: redo(T0) 및 undo(T1). A를 950, $를 2050으로 설정하고, C를 700으로 복원함. <T1, C, 700>, <T1 abort>를 로그에 기록함    <T0 start> <T0, A, 1000, 950> <T0, B, 2000, 2050> <T0 commit> <T1 start> <T1, C, 700, 600>     로그 상태 (c):복구 행동: redo(T0) 및 redo(T1). A를 950, B를 2050으로, C를 600으로 설정함    <T0 start> <T0, A, 1000, 950> <T0, B, 2000, 2050> <T0 commit> <T1 start> <T1, C, 700, 600> <T1 commit>
