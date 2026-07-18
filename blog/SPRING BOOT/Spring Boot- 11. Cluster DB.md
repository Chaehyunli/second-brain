---
title: "[Spring Boot] 11. Cluster DB"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cluster", "DB", "spring boot"]
category: "SPRING BOOT"
published: 2026-05-20
source_url: https://ch010104.tistory.com/276
---

# [Spring Boot] 11. Cluster DB

## 원문

https://ch010104.tistory.com/276

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

데이터베이스를 "클러스터로 구성하여 사용한다"는 것은 물리적 혹은 가상으로 분리된 여러 대의 데이터베이스 서버를 네트워크로 묶어, 백엔드 애플리케이션 입장에서는 마치 하나의 단일 시스템처럼 작동하도록 설계하는 것을 의미합니다.

이러한 분산 아키텍처를 도입하는 핵심 목적은 크게 세 가지입니다.

## 원문 기반 개념 정리

### 1. 데이터베이스 클러스터링(Clustering)의 본질

### 1.1 Q. "클러스터로 쓴다"는 것의 정의와 핵심 목적

데이터베이스를 "클러스터로 구성하여 사용한다"는 것은 물리적 혹은 가상으로 분리된 여러 대의 데이터베이스 서버를 네트워크로 묶어, 백엔드 애플리케이션 입장에서는 마치 하나의 단일 시스템처럼 작동하도록 설계하는 것을 의미합니다.

이러한 분산 아키텍처를 도입하는 핵심 목적은 크게 세 가지입니다.

고가용성 (High Availability, HA): 단일 DB 장비가 고장 났을 때 발생하는 서비스 전체 마비(SPOF, Single Point of Failure)를 방지합니다. 주 장비가 다운되어도 예비 장비가 즉각 가동되어 무중단 운영을 보장합니다.

읽기 트래픽 부하 분산 (Read Scaling): 대용량 웹 서비스의 트래픽은 일반적으로 쓰기(10~20%)보다 읽기(80~90%)가 압도적입니다. 읽기 요청을 서브 데이터베이스로 적절히 분산하여 메인 데이터베이스의 연산 부하를 크게 덜어냅니다.

가성비 중심의 수평적 확장 (Scale-out): 무조건 서버 자체 스펙을 늘리는 수직적 확장(Scale-up)은 비용이 기하급수적으로 발생합니다. 저렴한 노드를 물리적으로 추가하는 수평적 확장(Scale-out)이 경제적이고 영리한 인프라 전략입니다.

### 1.2 Q. "개인 캡스톤 프로젝트나 소규모 환경에서도 가능할까요? Supabase에선 어떨까요?"

Supabase 환경 분석: Supabase는 백엔드 인프라가 완전히 추상화된 Managed(완전 관리형) PostgreSQL 서비스입니다. 내부적으로 가용성 관리나 데이터 백업이 내장되어 있습니다. 유료 플랜(Pro 플랜 이상)에서는 몇 번의 설정만으로 'Read Replicas(읽기 전용 복제본 노드)'를 클러스터에 손쉽게 추가할 수 있습니다. 하지만 무료 플랜에서는 다중 인스턴스를 활용한 직접적인 클러스터링 설정을 허용하지 않습니다.

캡스톤 디자인 포트폴리오 제언: 단순히 API만 호출하는 것보다, 데이터베이스 설계 및 분산 인프라 역량을 확실하게 증명하고 싶다면 Docker 환경에서 PostgreSQL 인스턴스 2대를 직접 띄우고 데이터 동기화와 클러스터를 수동 구축하는 경험을 갖는 것을 권장합니다. 기술 면접 및 평가관들에게 인프라 설계 능력을 매우 훌륭하게 어필할 수 있는 차별화 포인트가 됩니다.

### 2. PostgreSQL 복제(Replication) 구조와 내부 동작 원리

### 2.1 WAL 스트리밍 복제 (Streaming Replication)

PostgreSQL의 실시간 복제 기술은 WAL (Write-Ahead Log, 미리 쓰기 로그) 백업 매커니즘을 기반으로 수행됩니다.

로그 선기록: Primary(Master) 노드에 데이터 생성/수정/삭제(CUD) 요청이 수신되면, 실제 디스크 데이터 페이지에 쓰기 전 해당 이력을 WAL 세그먼트에 먼저 순차 기록합니다.

로그 전송: Primary 노드의 백그라운드 프로세스인 WAL Sender가 네트워크 소켓을 통해 변경 로그를 Secondary(Slave) 노드로 전송합니다.

로그 Replay: Secondary 노드의 WAL Receiver 프로세스가 전송받은 변경 이력을 가져와서 로컬 데이터에 한 줄씩 반영(Replay)하며 완벽한 정합성을 맞춥니다.

### 2.2 Q. "docker-compose의 depends_on 설정 때문에 자동으로 동기화와 고장 대체가 되는 건가요?"

depends_on의 명확한 역할: 절대 아닙니다. Docker Compose 파일에서 depends_on은 오직 컨테이너의 부팅 및 가동 순서(마스터를 먼저 완전히 띄우고 슬레이브를 가동함)만을 강제합니다.

실제 동기화의 주체: 동기화 처리는 컨테이너에 전달한 환경 변수 설정을 보고 구동되는 컨테이너 이미지 내부의 초기화 스크립트가 PostgreSQL의 스트리밍 복제 모듈을 직접 활성화했기 때문에 일어납니다.

Failover(고장 대체)의 부재: 마스터 노드가 죽었을 때 슬레이브가 이를 인지하고 자동으로 읽기 전용 상태에서 마스터(쓰기 가능) 상태로 신분을 상승시키는 Auto-Failover 메커니즘은 기본 Docker Compose 설정만으로는 작동하지 않으며, 감시 역할을 수행할 추가 도구(Patroni 등)가 필수적입니다.

### 3. Docker Compose 기반의 실습 클러스터 구축

### 3.1 docker-compose.yml 설정 파일

```text
version: '3.8'

services:
  # =========================================================================
  # 1. Primary (Master) Database Node
  # =========================================================================
  postgres-master:
    image: bitnami/postgresql:15
    container_name: postgres-master
    environment:
      - POSTGRESQL_REPLICATION_MODE=master
      - POSTGRESQL_REPLICATION_USER=repl_user
      - POSTGRESQL_REPLICATION_PASSWORD=repl_password
      - POSTGRESQL_USERNAME=myuser
      - POSTGRESQL_PASSWORD=mypassword
      - POSTGRESQL_DATABASE=mydb
      - ALLOW_EMPTY_PASSWORD=no
    ports:
      - "5432:5432"
    volumes:
      - postgres_master_data:/bitnami/postgresql

  # =========================================================================
  # 2. Secondary (Slave) Database Node
  # =========================================================================
  postgres-slave:
    image: bitnami/postgresql:15
    container_name: postgres-slave
    depends_on:
      - postgres-master # Master가 부팅된 이후 구동될 수 있도록 안전한 실행 순서 제어
    environment:
      - POSTGRESQL_REPLICATION_MODE=slave
      - POSTGRESQL_MASTER_HOST=postgres-master # 연결할 Master 컨테이너의 네트워크 호스트명
      - POSTGRESQL_MASTER_PORT_NUMBER=5432
      - POSTGRESQL_REPLICATION_USER=repl_user
      - POSTGRESQL_REPLICATION_PASSWORD=repl_password
      - POSTGRESQL_PASSWORD=mypassword # Master 비밀번호와 일치 필수
    ports:
      - "5433:5432" # 포트를 5433으로 충돌 방지 세팅
    volumes:
      - postgres_slave_data:/bitnami/postgresql

volumes:
  postgres_master_data:
  postgres_slave_data:
```

### 3.2 복제 및 동작 테스트 절차

가동: docker compose up -d

쓰기 테스트: Master DB(5432 포트)에 접속하여 가상 데이터를 생성합니다.

CREATE TABLE products (id SERIAL PRIMARY KEY, title VARCHAR(50)); INSERT INTO products (title) VALUES ('Database Guide Book');

동기화 확인: Slave DB(5433 포트)에 접속해 정상적으로 실시간 복제가 일어났는지 확인합니다.

SELECT * FROM products; -- 'Database Guide Book'이 출력되면 복제 성공!

읽기 전용 상태 확인: Slave DB(5433 포트)에서 무단으로 쓰기 동작을 시도합니다.

INSERT INTO products (title) VALUES ('Unpermitted Book'); -- 에러 발생 확인: "ERROR: cannot execute INSERT in a read-only transaction"

### 4. 백엔드(Java/Spring Boot) 다중 데이터소스 및 동적 라우팅 연동

### 4.1 Q. "이렇게 클러스터로 바꿨을 때 백엔드 코드의 DB 접근/작성 로직도 다 바뀌나요?"

"데이터 조작을 처리하는 백엔드의 자바 SQL 쿼리 코드나 레포지토리(Repository) 로직은 전혀 바꿀 필요가 없습니다."

애플리케이션이 구동될 때 트랜잭션의 속성에 따라 타겟 DB 장비를 알아서 교체해 주는 Dynamic Routing DataSource 구조를 추가하는 것입니다.

개발자는 쓰기 작업이 발생하는 서비스 레이어의 비즈니스 메서드에는 기존처럼 @Transactional을 명시하고, 읽기 연산만 필요한 단순 피드 조회, 정보 확인 등의 메서드에는 @Transactional(readOnly = true)를 붙여주기만 하면 스프링 프레임워크가 알아서 올바른 포트와 IP로 분기해 줍니다.

### 4.2 application.properties 설정 파일

스프링 부트 애플리케이션 접속 정보를 정의하는 application.properties 파일입니다. YAML 방식을 완전히 배제한 표준 포맷입니다.

```text
# =========================================================================
# 1. Master DB DataSource (CUD - Create, Update, Delete)
# =========================================================================
spring.datasource.master.jdbc-url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.master.username=myuser
spring.datasource.master.password=mypassword
spring.datasource.master.driver-class-name=org.postgresql.Driver
# HikariCP 커넥션 풀 성능 최적화 세팅
spring.datasource.master.hikari.pool-name=Master-HikariPool
spring.datasource.master.hikari.maximum-pool-size=10
spring.datasource.master.hikari.minimum-idle=5
spring.datasource.master.hikari.idle-timeout=30000
spring.datasource.master.hikari.connection-timeout=20000

# =========================================================================
# 2. Slave DB DataSource (R - Read-Only)
# =========================================================================
spring.datasource.slave.jdbc-url=jdbc:postgresql://localhost:5433/mydb
spring.datasource.slave.username=myuser
spring.datasource.slave.password=mypassword
spring.datasource.slave.driver-class-name=org.postgresql.Driver
# HikariCP 커넥션 풀 성능 최적화 세팅
spring.datasource.slave.hikari.pool-name=Slave-HikariPool
spring.datasource.slave.hikari.maximum-pool-size=10
spring.datasource.slave.hikari.minimum-idle=5
spring.datasource.slave.hikari.idle-timeout=30000
spring.datasource.slave.hikari.connection-timeout=20000
```

### 4.3 동적 데이터소스 라우팅 (Dynamic Routing) 자바 구현 소스 코드

### 1) Routing Enum 정의

```text
public enum DataSourceType {
    MASTER, SLAVE
}
```

### 2) RoutingDataSource 상속 구현체

현재 실행되고 있는 스레드의 트랜잭션이 읽기 전용(readOnly = true) 상태인지 스프링 동기화 매니저를 통해 수시 검증하여 알맞은 DataSourceType Key를 반환합니다.

```java
import org.springframework.jdbc.datasource.lookup.AbstractRoutingDataSource;
import org.springframework.transaction.support.TransactionSynchronizationManager;

public class RoutingDataSource extends AbstractRoutingDataSource {
    @Override
    protected Object determineCurrentLookupKey() {
        boolean isReadOnly = TransactionSynchronizationManager.isCurrentTransactionReadOnly();
        return isReadOnly ? DataSourceType.SLAVE : DataSourceType.MASTER;
    }
}
```

### 3) Configuration 빈(Bean) 등록 설정

```java
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.jdbc.datasource.LazyConnectionDataSourceProxy;

import javax.sql.DataSource;
import java.util.HashMap;
import java.util.Map;

@Configuration
public class DataSourceConfig {

    @Bean(name = "masterDataSource")
    @ConfigurationProperties(prefix = "spring.datasource.master")
    public DataSource masterDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "slaveDataSource")
    @ConfigurationProperties(prefix = "spring.datasource.slave")
    public DataSource slaveDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "routingDataSource")
    public DataSource routingDataSource(
            @Qualifier("masterDataSource") DataSource masterDataSource,
            @Qualifier("slaveDataSource") DataSource slaveDataSource) {

        RoutingDataSource routingDataSource = new RoutingDataSource();

        Map<Object, Object> dataSourceMap = new HashMap<>();
        dataSourceMap.put(DataSourceType.MASTER, masterDataSource);
        dataSourceMap.put(DataSourceType.SLAVE, slaveDataSource);

        routingDataSource.setTargetDataSources(dataSourceMap);
        routingDataSource.setDefaultTargetDataSource(masterDataSource); // 트랜잭션이 정의되지 않았을 때의 기본 세팅

        return routingDataSource;
    }

    // 💡 핵심 가이드: 스프링은 기본적으로 트랜잭션 수립 시점에 바로 DataSource 커넥션을 영속하려 시도합니다.
    // LazyConnectionDataSourceProxy 대리자를 거쳐야 실제 쿼리가 호출되는 런타임 타이밍에 라우팅 분기가 온전히 성사됩니다.
    @Bean
    @Primary
    public DataSource dataSource(@Qualifier("routingDataSource") DataSource routingDataSource) {
        return new LazyConnectionDataSourceProxy(routingDataSource);
    }
}
```

### 5. 대규모 엔터프라이즈 환경에서의 Multi-Master 아키텍처 논의

### 5.1 Q. "읽기도 2개, 쓰기도 2개의 다중 마스터 서버로 확장하려면 어떻게 해야 하나요?"

쓰기 기능이 작동하는 마스터 서버를 2대 이상(Multi-Master 혹은 Multi-Write) 두고 서로 실시간 교차 동기화를 시도하는 아키텍처는 기술적 난도가 극도로 올라갑니다.

동시에 양쪽 마스터 DB에서 동일한 식별자를 가진 유저의 닉네임을 변경하는 사건이 터졌을 경우, 분산 제어 합의가 없다면 데이터 충돌(Write Conflict) 현상으로 인해 데이터가 심각하게 깨지고 루프 현상이 걸리며 정합성이 완전히 붕괴됩니다.

### 5.2 PostgreSQL 진영의 해결 방안

Citus (시터스): 마이크로소프트 산하에서 분산 샤딩 데이터베이스 형태로 개발을 고도화하고 있는 PostgreSQL용 확장 플러그인입니다. Coordinator 노드들이 분산되어 들어오는 쓰기 쿼리를 분배하며 물리적인 Worker DB 노드들에 해시 기반 분산 적재(Sharding)를 처리함으로써 다중 쓰기 성능 병목을 해결합니다.

Bucardo (부카르도) / Spock: 트리거 기술을 활용해 마스터 노드끼리 변경 사항을 양방향 복제(Bi-directional Replication)하는 복제 전용 도구입니다. 동시성 데이터 마찰이 빚어질 시 이를 조율할 명확한 복구 알고리즘 및 우선순위 세팅을 세워야 합니다.

### 6. 인프라 레이어의 독립: HAProxy와 PgBouncer의 역할

### 6.1 Q. "HAProxy를 도입하면 결국 백엔드 코드가 프록시를 보도록 다 변경해야 하는 것 아닌가요?"

설정 파일의 주소 단일화: 네, 맞습니다. DB 접속을 가리키는 application.properties 설정 주소는 변경해 주어야 합니다.

백엔드 코드의 복잡성 보호: 하지만 이는 단순히 백엔드 내부 properties 설정에서 수많은 개별 DB의 복잡한 주소를 다 없애버리고, 오직 HAProxy 장비의 단 한 줄의 IP 주소만 바라보게 통합하는 혁신적인 설계입니다.

```text
# HAProxy 도입 이전: 개별 마스터, 슬레이브 노드들의 주소를 백엔드가 직접 하드코딩 형태로 전부 알았어야 함
# spring.datasource.master.jdbc-url=jdbc:postgresql://localhost:5432/mydb
# spring.datasource.slave.jdbc-url=jdbc:postgresql://localhost:5433/mydb

# HAProxy 도입 이후: 백엔드는 뒷단의 DB 대수나 물리 IP 변화와 무관하게 오직 HAProxy 주소 1개만 매핑함
spring.datasource.url=jdbc:postgresql://haproxy-loadbalancer-ip:5000/mydb
```

모든 로드 밸런싱(Load Balancing) 분배 처리와 특정 노드 장비 장애 시 서버 격리(Health Check)는 HAProxy 프록시 계층이 인프라 레벨에서 완수하기 때문에, 서비스가 확장되어 DB가 수십 대 규모로 불어나도 백엔드 코드는 수정과 재배포를 완전히 면제받습니다.

### 6.2 Q. "PgBouncer는 무엇이고 어떤 성능 문제를 해결해 주나요?"

PostgreSQL은 접속이 한 개 수립될 때마다 운영체제의 독립된 전용 프로세스를 일일이 생성(Process-per-connection)하는 독특한 아키텍처를 채택하고 있습니다.

프로세스 생성 부하의 한계: 백엔드 도커 컨테이너가 쏟아져 들어오는 세션을 받기 위해 동시 커넥션을 무제한 늘리기 시작하면, DB 서버 메모리가 프로세스 컨텍스트 스위칭 유지비 감당을 못하고 금세 다운되거나 마비됩니다.

PgBouncer의 압축 중개: PgBouncer는 백엔드와 데이터베이스의 사이에 입점하여 수많은 앱의 장기 연결 대기 상태를 가볍게 수집해 안고 있습니다. 그리고 실제 PostgreSQL 엔진을 상대로는 하드웨어 사양에 맞춰 사전에 조율된 소수(예: 30개)의 실질 물리 커넥션만을 공유합니다. 그리고 쿼리가 들어올 때만 짧게 진짜 통로를 대여해주고 환수하는 "돌려막기 방식"으로 DB 자원을 드라마틱하게 보호합니다.

### 6.3 HAProxy와 PgBouncer 핵심 개념 대조표

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 1. JDBC 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 1. JDBC 이해]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 2. 커넥션풀과 데이터소스 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 2. 커넥션풀과 데이터소스 이해]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 3. 트랜잭션 이해]]
