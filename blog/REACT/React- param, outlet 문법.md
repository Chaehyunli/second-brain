---
title: "[React] param, outlet 문법"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "JavaScript", "react"]
category: "REACT"
published: 2025-03-05
source_url: https://ch010104.tistory.com/4
---

# [React] param, outlet 문법

## 원문

https://ch010104.tistory.com/4

## 노트 유형

`guide`

## 적용 목적과 전제조건

"react-router-dom" 의 useParams 를 import 해서 사용 가능하다.

/user/alice 와 같은 url 주소에서 내가 원하는 값을 추출하기 위해서 사용한다.

## 구현 절차·검증·주의점

1. param 문법

URL 경로에서 동적으로 값을 가져오는 방법

UseProfile.js

```typescript
import { useParams } from "react-router-dom";

const UserProfile = () => {
  let { username } = useParams(); // URL에서 username 추출
  return <h1>👤 {username}님의 프로필 페이지</h1>;
};

export default UserProfile;
```

"react-router-dom" 의 useParams 를 import 해서 사용 가능하다.

/user/alice 와 같은 url 주소에서 내가 원하는 값을 추출하기 위해서 사용한다.

/user/{username} 의 경우, username을 추출하기 위해 사용

어떤 parameter를 추출할지는 app.js에서 선언하는 것이 일반적이다.

App.js

```typescript
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import UserProfile from "./pages/UserProfile";

const App = () => {
  return (
    <Router>
      <Routes>
        {/* URL Parameter 예제 */}
        <Route path="/user/:username" element={<UserProfile />} />
      </Routes>
    </Router>
  );
};

export default App;
```

<Route path="/user/:username" element={<UserProfile />} /> 에서 "/user/:username" 의 주소를 렌더링 할 경우에 UserProfile.js 가 표시되도록 함. UserProfile.js 에서 param을 사용할 경우 :username의 값을 param으로 선언한 let {username} 으로 사용할 수 있다.

2. outlet 문법

중첩 라우트를 렌더링할 때 사용하는 컴포넌트. 부모 라우트가 존재할 때, 하위 라우트의 내용을 표시하는 역할을 한다. 즉, 화면에서 내가 위의 Nav바는 유지한채로 아래의 부분만 바뀌게 하고 싶다면?? outlet 사용!!

App.js

```typescript
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import DashboardHome from "./pages/DashboardHome"; // 기본 페이지
import Analytics from "./pages/Analytics";
import Settings from "./pages/Settings";

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Nested Route (Outlet 사용) + 기본 페이지 추가 */}
        <Route path="/dashboard" element={<Dashboard />}>
          <Route index element={<DashboardHome />} /> {/* 디폴트 페이지 */}
          <Route path="analytics" element={<Analytics />} />
          <Route path="settings" element={<Settings />} />
        </Route>
       </Routes>
    </Router>
  );
};

export default App;
```

"DashboardHome", "Analytics", "Settings" 가 "Dashboard"의 자식이 되는 것!. /dashboard 의 url만을 호출시 디폴트 페이지로 선언되어 있는 "DashboradHome" 이 자식으로 outlet부분에 렌더링 됨. 나머지 /dashboard/analytics, /dashboard/settings 등의 url을 호출시에 자식으로 outlet부분이 각각 렌더링 됨.

Dashboard.js

```typescript
import { Outlet, Link } from "react-router-dom";

const Dashboard = () => {
  return (
    <div>
      <h1>📊 대시보드</h1>
      <nav>
        <Link to="/dashboard">홈</Link> | <Link to="analytics">분석</Link> | <Link to="settings">설정</Link>
      </nav>
      <Outlet /> {/* 하위 라우트가 표시될 위치 */}
    </div>
  );
};

export default Dashboard;
```

<nav>에서 <Link> 로 주소를 이동하고 그에 따라 아래의 <Outlet /> 부분에 하위의 자식 라우트가 표시됨. App.js에서 선언했듯이 /dashboard 의 경우 디폴트 페이지가 호출되고 나머지 /dashboard/analytics, /dashboard/settings 호출시 각각 알맞은 페이지가 렌더링된다.

## 관련 글

- [[blog/REACT/index|REACT]]
- [[blog/REACT/React- state 문법이란-, useEffect 문법이란|[React] state 문법이란?, useEffect 문법이란?]]
- [[blog/REACT/React- CLERK을 이용한 토큰 로그인|[React] CLERK을 이용한 토큰 로그인]]
- [[blog/SPRING BOOT/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
