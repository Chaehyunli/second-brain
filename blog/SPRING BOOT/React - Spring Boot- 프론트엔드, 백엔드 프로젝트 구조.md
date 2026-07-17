---
title: "[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "backend", "frontend", "java", "react", "spring boot"]
category: "SPRING BOOT"
published: 2025-02-20
source_url: https://ch010104.tistory.com/3
---

# [React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조

## 원문

https://ch010104.tistory.com/3

## 노트 유형

`project`

## 배경·목표·적용 맥락

세션 기반의 로그인 프로젝트를 만들기 위한 프론트엔드, 백엔드의 구조를 정리해보았다.

context/AuthContext.js (전역 로그인 상태 관리)

## 구현·의사결정·결과

세션 기반의 로그인 프로젝트를 만들기 위한 프론트엔드, 백엔드의 구조를 정리해보았다.

1. 프론트엔드

```text
/src
  ├── api               # API 요청 관련 코드
  │   ├── authApi.js    # 로그인 및 로그아웃 API 요청
  │   ├── userApi.js    # 사용자 정보 조회 API 요청
  │
  ├── components        # 공통 UI 컴포넌트
  │   ├── InputField.js # 입력 필드 컴포넌트
  │
  ├── context           # 전역 상태 관리
  │   ├── AuthContext.js # 로그인 상태 관리
  │
  ├── pages             # 주요 페이지
  │   ├── LoginPage.js  # 로그인 페이지
  │   ├── HomePage.js   # 로그인 후 이동할 메인 페이지
  │
  ├── utils             # 공통 유틸 함수
  │   ├── axiosInstance.js # Axios 설정 (API 기본값 설정)
  │
  ├── App.js            # 메인 애플리케이션 (라우터 포함)
  ├── index.js          # React 진입점
```

context/AuthContext.js (전역 로그인 상태 관리)

```typescript
import { createContext, useState, useEffect } from "react";

// AuthContext 생성
export const AuthContext = createContext(null); // 초기값을 null로 하여 AuthContext 선언

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // 애플리케이션 시작 시 localStorage에서 사용자 정보 로드
  useEffect(() => {
    const storedUsername = localStorage.getItem("username");
    if (storedUsername) {
      setUser({ username: storedUsername });
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};
```

createContext란?

createContext는 React의 Context API를 활용하여 전역 상태를 관리할 수 있도록 하는 기능으로 여러 컴포넌트에서 공유할 수 있는 전역적인 상태(보통 로그인 상태와 같은 상태 저장에 사용)를 제공한다.

AuthProvider란?

AuthContext.Provider를 통해 모든 하위 컴포넌트에서 AuthContext에 접근할 수 있도록 한다. 앱이 실행되면 로컬 저장소에서 사용자 정보를 불러와 user 상태를 설정한다.

App.js

```typescript
import React from "react";
import { AuthProvider } from "./context/AuthContext";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/home" element={<HomePage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
```

App.js 에서 앱 전체를 AuthProvider로 감싸고, user 상태를 관리함.

이제 AuthProvider 내부의 모든 컴포넌트가 AuthContext를 사용할 수 있음.

utils/axiosInstance.js (Axios 설정)

```typescript
import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8080", // 백엔드 API 주소
  withCredentials: true, // 세션 기반 인증을 위해 필요
});

export default instance;
```

API 요청 시 세션 인증을 유지하도록 설정.

components/InputField.js (입력 필드 컴포넌트)

```typescript
import React from "react";

const InputField = ({ label, type, name, value, onChange }) => (
  <div>
    <label>{label}</label>
    <input type={type} name={name} value={value} onChange={onChange} required />
  </div>
);

export default InputField;
```

로그인 입력 필드를 재사용 가능하도록 구현. 이후 pages/에서 입력 필드를 재사용

pages/LoginPage.js

```typescript
import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/authApi";
import { AuthContext } from "../context/AuthContext";
import InputField from "../components/InputField";

const LoginPage = () => {
    const navigate = useNavigate();
    const { setUser } = useContext(AuthContext); // AuthContext에서 상태 관리
    const [formData, setFormData] = useState({ username: "", password: "" });
    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const result = await login(formData.username, formData.password);
            setUser(result.data); // 전역 상태 업데이트
            localStorage.setItem("username", result.data.username); // 로컬 저장
            navigate("/home"); // 로그인 성공 후 이동
        } catch (error) {
            setMessage("로그인 실패: " + error.message);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>로그인</h2>
            <InputField label="아이디" type="text" name="username" value={formData.username} onChange={handleChange} />
            <InputField label="비밀번호" type="password" name="password" value={formData.password} onChange={handleChange} />
            <button type="submit">로그인</button>
            {message && <p style={{ color: "red" }}>{message}</p>}
        </form>
    );
};

export default LoginPage;
```

const { setUser } = useContext(AuthContext); 를 통해 전역에서 사용자 로그인 상태를 관리.

api/ 의 로그인 요청 await login( formData.username, formData.password ) 로 로그인을 성공하면 사용자의 아이디를 localStorage에 저장(이전에 CreateContext에서 사용자 아이디로 로그인 상태를 관리)

api/authApi.js (로그인 및 로그아웃 API)

```typescript
import axios from "../utils/axiosInstance";

// 로그인 요청
export const login = async (username, password) => {
  const response = await axios.post("/auth/login", { username, password });
  return response.data; // { message, data: { userId, username, name } }
};

// 로그아웃 요청
export const logout = async () => {
  await axios.post("/auth/logout");
};
```

pages/ 나 components/ 에서 요청하는 함수를 정의. login 함수를 요청하면 /auth/login 에 post 요청을 보냄. 이후에 백엔드에서 /auth/login 의 post 요청에서 로그인을 수행하고 json 형식의 사용자의 로그인 정보를 반환.

```text
{
  "message": "로그인 성공",
  "data": {
    "userId": 1,
    "username": "testUser",
    "name": "홍길동"
  }
}
```

pages/HomePage.js (홈 페이지)

```typescript
import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { logout } from "../api/authApi";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const { user, setUser } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    localStorage.removeItem("username"); // 로컬 저장소에서 제거
    setUser(null); // 상태 초기화
    navigate("/login"); // 로그인 페이지로 이동
  };

  return (
    <div>
      <h1>환영합니다, {user ? user.username : "Guest"}!</h1>
      <button onClick={handleLogout}>로그아웃</button>
    </div>
  );
};

export default HomePage;
```

HomePage에서 로그인 이후에 사용자의 로그인 정보를 확인하고, 로그아웃 기능도 제공. 로그아웃시 logout 요청을 보내고, localStorage에서 사용자의 이름을 제거함.

2. 백엔드

```text
/src/main/java/com/example/auth
  ├── controller       # API 요청 처리 (프론트엔드와 직접 통신)
  │   ├── AuthController.java
  │
  ├── dto              # 요청 및 응답 데이터 전송 객체 (Request/Response DTO)
  │   ├── LoginRequestDto.java
  │   ├── UserDto.java
  │
  ├── entity           # 데이터베이스 테이블과 매핑되는 클래스 (JPA 엔티티)
  │   ├── User.java
  │
  ├── repository       # 데이터베이스 접근 (JPA 사용)
  │   ├── UserRepository.java
  │
  ├── service          # 비즈니스 로직 처리 (핵심 기능)
  │   ├── AuthService.java
  │   ├── AuthServiceImpl.java
  │
  ├── config           # 보안, 세션 설정 및 전역 환경 설정
  │   ├── SecurityConfig.java
  │
  ├── exception        # 예외 처리 및 전역 에러 핸들링
  │   ├── GlobalExceptionHandler.java
  │
  ├── Application.java # Spring Boot 메인 실행 파일
```

controller/AuthController.java

```java
package com.example.auth.controller;

import com.example.auth.dto.LoginRequestDto;
import com.example.auth.dto.UserDto;
import com.example.auth.service.AuthService;
import jakarta.servlet.http.HttpSession;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class AuthController {
    private final AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }

    @PostMapping("/login")
    public ResponseEntity<UserDto> login(@RequestBody LoginRequestDto requestDto, HttpSession session) {
        LoginResponseDto user = authService.login(requestDto);
        session.setAttribute("user", user); // 세션에 사용자 정보 저장
        return ResponseEntity.ok(user);
    }

    @PostMapping("/logout")
    public ResponseEntity<String> logout(HttpSession session) {
        session.invalidate(); // 세션 삭제
        return ResponseEntity.ok("로그아웃 성공");
    }
}
```

@RequestBody LoginRequestDto requestDto 에서 프론트엔드 받은 로그인 정보를 Dto 인 LoginRequestDto로 변환해서 받음.

HttpSession session 은 로그인 성공 시 세션을 생성하고 유지하는 역할. authServcie에서 requestdto와 함께 login 요청을 보내 LoginResponseDto를 응답 받음.

인증 성공하면 session.setAttribute("user", user);를 호출하여 세션에 사용자 정보를 저장. 이후, 세션 쿠키(JSESSIONID)가 자동으로 생성되어 브라우저에 저장됨.

dto/LoginRequestDto.java , dto/LoginResponseDto.java

```java
@Getter
@Setter
public class LoginRequestDto {
    private String username;
    private String password;
}
```

프론트엔드에서 username과 password를 보내면 이를 받아주는 DTO.

```java
@Getter
@Setter
@AllArgsConstructor
public class LoginResponseDto {
    private Long id;
    private String username;
    private String name;
}
```

사용자 정보 응답 시 비밀번호를 제외하고 id, username, name만 반환하는 DTO.

entity/User.java

```java
@Entity
@Table(name = "users")
@Getter
@Setter
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String password;

    private String name;
}
```

데이터베이스의 users 테이블과 매핑되는 entity. properties 설정에서

```text
spring.jpa.hibernate.ddl-auto=update
```

를 추가하면 필요할 때 entity에 맞게 자동으로 테이블을 생성해줌.

respository/UserRepository.java

```text
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}
```

사용자를 username으로 조회할 수 있도록 findByUsername() 메서드 추가

/service에서 로그인 로직을 수행할 때, findByUsername() 메서드로 사용자의 아이디로 비밀번호를 데이터베이스에서 찾아서 비교 후 로그인 승인

service/ AuthServiceImpl.java, service/ AuthService.java

```java
@Service
public class AuthServiceImpl implements AuthService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public AuthServiceImpl(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public LoginResponseDto login(LoginRequestDto requestDto) {
        User user = userRepository.findByUsername(requestDto.getUsername())
                .orElseThrow(() -> new RuntimeException("아이디 또는 비밀번호가 잘못되었습니다."));

        if (!passwordEncoder.matches(requestDto.getPassword(), user.getPassword())) {
            throw new RuntimeException("아이디 또는 비밀번호가 잘못되었습니다.");
        }

        return new LoginResponseDto(user.getId(), user.getUsername(), user.getName());
    }
}
```

비밀번호를 검증한 후, LoginResponseDto로 변환하여 반환. private final PasswordEncoder passwordEncoder 를 통해 해싱된 비밀번호를 matches 메소드를 이용하여 비교한 후 로그인.

```text
public interface AuthService {
    UserLoginResponseDto login(UserLoginRequestDto dto, HttpSession session);
}
```

AuthServiceImpl는 AuthService을 상속 받음.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
- [[blog/DOCKER/Docker- Docker를 사용해서 Spring boot + React 배포하기 ( 1 )|[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
