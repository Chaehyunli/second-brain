---
source: Notion Information
notion_url: https://app.notion.com/p/3b21d84bf68e800bbcc7e3098b3c6c24
notion_page_id: 3b21d84b-f68e-800b-bcc7-e3098b3c6c24
synced_at_utc: 2026-08-08T15:12:24Z
notion_content_sha256: 1cf316459ae7c8502e4d5af6bbfce091a55ecb372ac4738091a5bf99c99f5c17
---

### 전체 구조 이해
SPA 로그인 구조에서 각 도구의 역할은 다름.
```plain text
로그인 성공
  ├─ Pinia: 현재 화면을 즉시 로그인 상태로 바꿈
  ├─ localStorage: 새로고침 뒤에도 필요한 정보를 복원
  └─ Axios Interceptor: API 요청에 인증 정보를 실어 보냄

새로고침
  └─ localStorage / 쿠키 → Pinia 상태 복원 → UI 다시 반영

API 요청
  ├─ JWT + localStorage: Authorization 헤더에 토큰 직접 주입
  └─ 세션 / httpOnly 쿠키: 브라우저가 쿠키를 자동 전송
```
핵심 정리
- Pinia: 화면을 즉시 바꾸기 위한 반응형 상태 저장소
- localStorage: 새로고침 후에도 데이터를 남기기 위한 영구 저장소
- JWT / 세션 / 쿠키: 서버가 요청자를 인증하는 방식
- CSRF / XSS: 인증 정보를 어떤 방식으로 저장·전송하느냐에 따라 달라지는 보안 문제
- 인증 이후에도 서버는 해당 행동을 할 권한이 있는지 인가(Authorization)를 검사해야 함
---
### localStorage와 Pinia는 역할이 다름
#### localStorage란?
브라우저가 제공하는 영구 저장소임.
- 브라우저를 닫아도 데이터가 남음
- 새로고침해도 데이터가 유지됨
- 문자열 형태의 값을 저장함
- Vue의 반응성 시스템과 직접 연결되어 있지 않음
즉, localStorage는 단순한 보관함임.
```javascript
localStorage.setItem('token', token)
```
값이 바뀌어도 Vue 컴포넌트가 자동으로 다시 렌더링되지는 않음. localStorage만 바꿨다고 화면이 자동으로 바뀌지 않음.
---
### Pinia State란?
Vue 애플리케이션 안에서 사용하는 반응형 상태 관리 저장소임.
- 브라우저 메모리(RAM)에 존재함
- Pinia의 값이 바뀌면 해당 값을 사용하는 컴포넌트 UI가 즉시 갱신됨
- 새로고침하면 메모리가 초기화되므로 기본적으로 상태가 사라짐
```javascript
const token = ref(null)
const user = ref(null)
```
Pinia의 token, user, isLoggedIn 값이 바뀌면 헤더·메뉴·마이페이지 등 해당 상태를 사용하는 화면이 새로고침 없이 바로 바뀜.
---
### Pinia와 localStorage 비교
<table header-row="true">
<tr>
<td>항목</td>
<td>localStorage</td>
<td>Pinia State</td>
</tr>
<tr>
<td>저장 위치</td>
<td>브라우저 영구 저장소</td>
<td>브라우저 메모리</td>
</tr>
<tr>
<td>새로고침 후</td>
<td>유지됨</td>
<td>초기화됨</td>
</tr>
<tr>
<td>브라우저 종료 후</td>
<td>유지됨</td>
<td>사라짐</td>
</tr>
<tr>
<td>Vue 반응성</td>
<td>없음</td>
<td>있음</td>
</tr>
<tr>
<td>값 변경 시 UI</td>
<td>자동 갱신 안 됨</td>
<td>즉시 갱신됨</td>
</tr>
<tr>
<td>주 역할</td>
<td>영속 보관</td>
<td>현재 UI 상태 관리</td>
</tr>
</table>
localStorage는 저장을 위해 쓰고, Pinia는 화면 반응을 위해 씀.
---
### 로그인 후 SPA에서 Pinia가 필요한 이유
#### 로그인 뒤 헤더가 즉시 바뀌어야 하는 상황
예시: App.vue에 고정 헤더가 있을 때
```plain text
로그인 전: [안녕하세요 Guest님 | 로그인]
로그인 후: [안녕하세요 채현님 | 로그아웃]
```
로그인 성공 후 페이지 전체를 새로고침하지 않고 헤더만 즉시 바꿔야 함. localStorage에만 저장하면 App.vue는 이미 마운트된 상태이므로 localStorage가 바뀌었다는 사실을 자동으로 알지 못함.
```javascript
localStorage.setItem('token', token)
// → UI 자동 갱신 안 됨
```
---
### Pinia를 쓰면 어떻게 해결되는가
로그인 성공 시 Pinia 상태를 바꿈.
```javascript
authStore.login(token, user)
```
그러면 다음이 동시에 반응함.
- 헤더의 로그인/로그아웃 버튼
- 사용자 이름
- 권한별 메뉴
- 마이페이지 접근 상태
- 장바구니·좋아요·알림 같은 로그인 기반 UI
로그인 상태를 바라보는 모든 컴포넌트가 페이지 이동이나 새로고침 없이 즉시 바뀜.
---
### 실무 조합 패턴
```plain text
로그인 성공
  1. Pinia에 토큰·사용자 정보 저장
  2. localStorage에도 필요한 정보 백업
  3. 화면은 Pinia를 기준으로 즉시 갱신
```
```javascript
function login(token, user) {
  this.token = token
  this.user = user

  localStorage.setItem('token', token)
  localStorage.setItem('user', JSON.stringify(user))
}
```
새로고침할 때는 localStorage의 값을 읽어 Pinia를 복원함.
```javascript
const token = ref(localStorage.getItem('token') || null)
```
앱 시작 시 초기화 로직 예시.
```javascript
function restoreAuth() {
  const token = localStorage.getItem('token')
  const user = localStorage.getItem('user')

  if (token) {
    this.token = token
    this.user = user ? JSON.parse(user) : null
  }
}
```
---
#### Axios Interceptor는 인증 정보를 API 요청에 붙임
Pinia가 API 요청을 직접 보내는 것은 아님. Axios가 요청을 보내고, Axios Interceptor가 토큰을 꺼내 Authorization 헤더에 넣음.
```javascript
axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')

  if (token) {
    config.headers.Authorization = `Bearer${token}`
  }

  return config
})
```
```plain text
Pinia / localStorage
  ↓
Axios Interceptor가 토큰 조회
  ↓
Authorization: Bearer ***
  ↓
백엔드가 토큰 검증
```
Pinia는 현재 UI 상태 관리에 더 가깝고, localStorage는 새로고침 이후 토큰 복원에 더 가까움.
---
### 세션, JWT, 쿠키는 무엇이 다른가
#### 세션 + 쿠키
인증 정보의 핵심이 서버에 있는 방식임.
```plain text
브라우저
  └─ session_id 쿠키만 보관

서버
  └─ session_id를 기준으로 사용자 정보 조회
```
- 브라우저는 보통 session_id만 들고 있음
- 실제 사용자 정보나 로그인 상태는 서버 메모리·DB·Redis 등에 존재함
- 브라우저는 요청할 때 쿠키를 자동 전송함
- 서버는 세션 ID를 보고 사용자를 확인함
---
### JWT + localStorage
토큰 자체에 사용자 식별 정보·만료 시간 등이 담길 수 있는 방식임.
```plain text
브라우저
  └─ JWT를 localStorage 등에 저장

API 요청
  └─ Authorization: Bearer ***

서버
  └─ JWT 서명과 만료 시간 검증
```
- 브라우저가 토큰을 직접 저장함
- Axios가 Authorization 헤더에 직접 넣어 보냄
- 서버는 JWT 서명 검증을 통해 위조 여부를 확인함
- 세션처럼 매번 서버 세션 저장소를 조회하지 않는 구조를 만들 수 있음
---
### JWT + httpOnly 쿠키
JWT를 저장 위치를 httpOnly Cookie로 설정하는 방식임.
```plain text
브라우저
  └─ httpOnly 쿠키에 JWT 저장

요청
  └─ 브라우저가 쿠키 자동 전송

JavaScript
  └─ 쿠키 값을 직접 읽을 수 없음
```
JavaScript가 토큰에 접근할 수 없으므로 XSS 토큰 탈취 위험을 줄일 수 있음. 대신 쿠키 자동 전송 특성 때문에 CSRF 방어를 함께 설계해야 함.
---
### 세 가지 방식 비교
<table header-row="true">
<tr>
<td>항목</td>
<td>세션 + 쿠키</td>
<td>JWT + localStorage</td>
<td>JWT + httpOnly 쿠키</td>
</tr>
<tr>
<td>인증 정보 위치</td>
<td>서버 메모리 / DB / Redis</td>
<td>토큰 자체를 클라이언트 보관</td>
<td>토큰 자체를 쿠키에 보관</td>
</tr>
<tr>
<td>브라우저 자동 전송</td>
<td>가능</td>
<td>불가능, 헤더 직접 설정</td>
<td>가능</td>
</tr>
<tr>
<td>CSRF 위험</td>
<td>대응 필요</td>
<td>전통적 CSRF 위험은 낮음</td>
<td>대응 필요</td>
</tr>
<tr>
<td>XSS 토큰 탈취</td>
<td>JS 접근 불가라 낮음</td>
<td>JS 접근 가능하므로 높음</td>
<td>JS 접근 불가라 낮음</td>
</tr>
<tr>
<td>CORS / 모바일 활용</td>
<td>쿠키 정책 영향을 받음</td>
<td>상대적으로 유연</td>
<td>쿠키 정책 영향을 받음</td>
</tr>
<tr>
<td>프런트의 토큰 직접 관리</td>
<td>낮음</td>
<td>높음</td>
<td>낮음</td>
</tr>
</table>
---
### 왜 세션에서도 Pinia를 쓸 수 있는가
#### 오해: "세션은 Pinia를 못 쓰고 JWT만 된다"
Vue/Pinia에서 세션과 JWT는 둘 다 사용할 수 있음. Pinia는 인증 방식이 아니라 프런트엔드 UI 상태 관리 도구임.
세션 로그인이라도 로그인 성공 후 다음과 같은 정보를 Pinia에 저장할 수 있음.
```javascript
authStore.user = {
  id: 1,
  name: '채현',
  profileImage: '...'
}
```
그리고 헤더나 마이페이지 화면을 즉시 갱신할 수 있음.
---
### "세션은 매번 백엔드에 물어본다"의 정확한 의미
차이는 프런트엔드가 매번 백엔드에 요청하느냐의 문제가 아님.
- 세션 방식: 서버가 요청마다 세션 ID를 기준으로 DB·메모리·Redis 등에서 사용자 상태를 확인할 수 있음
- JWT 방식: 서버가 JWT의 서명과 만료 시간을 검증해, 경우에 따라 세션 저장소 조회를 생략할 수 있음
차이는 Pinia가 아니라 백엔드의 인증 검증 구조에 있음.
---
### 세션에서도 사용자 정보를 localStorage에 저장할 수 있는가
가능함. 세션 방식이라도 로그인 성공 시 서버가 기본 사용자 정보를 응답으로 줄 수 있음.
```json
{
  "id": 1,
  "name": "채현",
  "profileImage": "..."
}
```
이 정보는 Pinia에 저장해 UI에 쓰고, 필요하다면 localStorage에 저장해 새로고침 후 복원할 수도 있음.
저장 가능 여부 구분:
- 사용자 이름, 프로필 이미지, UI 표시용 권한 → 저장 가능
- 비밀번호, 민감 개인정보, 인증 비밀값 → 저장하면 안 됨
- 서버 권한 판단 → 프런트 저장값이 아니라 서버 인증 정보 기준으로 해야 함
---
### JWT Payload와 사용자 ID는 어디까지 믿을 수 있는가
#### JWT는 프런트에서 읽을 수 있음
JWT Payload는 암호화가 아니라 일반적으로 Base64URL 인코딩 형태임. 따라서 프런트엔드에서 토큰 내부 정보를 읽을 수 있음.
```json
{
  "userId": 1,
  "name": "채현",
  "role": "USER",
  "exp": 1234567890
}
```
이런 정보는 디코딩해 UI 표시에 활용할 수 있음. 다만 JWT Payload는 읽을 수는 있어도, 민감한 정보를 넣는 장소가 아님. 노출되어도 문제가 없는 최소한의 정보만 둬야 함.
---
### JWT의 내용을 바꾸면 어떻게 되는가
JWT는 일반적으로 `Header.Payload.Signature` 구조를 가짐. Payload는 볼 수 있어도 Signature는 서버의 비밀키로 생성됨.
해커가 Payload의 userId나 role을 바꾸면 Signature가 달라지고, 서버 검증에서 실패함.
```plain text
내용 수정
  ↓
서명 불일치
  ↓
서버가 위조 토큰으로 판단
  ↓
요청 거부
```
토큰 내용을 임의로 조작해 관리자 권한을 얻는 것은 정상적인 서명 검증이 있다면 불가능함.
---
### 사용자 ID가 URL에 노출돼도 되는가
사용자 ID는 식별자일 뿐, 인증 열쇠가 아님.
```plain text
POST /users/123/profile
```
공격자가 URL의 123을 다른 사람의 ID로 바꿔도 서버는 단순히 URL만 믿으면 안 됨. 서버는 반드시 두 단계를 확인해야 함.
- 1단계 인증(Authentication): 토큰 또는 세션으로 요청자가 누구인지 확인
- 2단계 인가(Authorization): 요청자 ID와 대상 사용자 ID를 비교
```plain text
토큰 속 로그인 사용자 ID = 10
URL의 대상 사용자 ID = 123

10 !== 123
→ 권한 없음, 요청 거부
```
프런트의 ID, URL의 ID, 요청 Body의 ID는 신뢰 대상이 아님. 최종 권한 판단은 서버가 인증 정보와 비교해서 해야 함.
---
### 쿠키와 CSRF
#### CSRF란?
사이트 간 요청 위조(Cross-Site Request Forgery)임.
사용자가 어떤 서비스에 로그인되어 있고 쿠키가 브라우저에 남아 있는 상태에서, 공격자가 만든 외부 사이트에 접속했다고 할 때 외부 사이트가 사용자의 브라우저를 이용해 다음과 같은 요청을 보내려 할 수 있음.
```html
<form action="https://bank.example.com/transfer" method="POST">
  ...
</form>
```
쿠키 방식에서는 브라우저가 대상 사이트 쿠키를 자동으로 붙일 가능성이 있음. 서버가 추가 검증을 하지 않으면 사용자가 의도하지 않은 송금·수정·탈퇴 요청이 처리될 수 있음.
---
### JWT + localStorage는 CSRF에 안전한가
JWT를 localStorage에 저장하고 Axios가 Authorization 헤더에 직접 넣는 구조는 전통적인 쿠키 기반 CSRF 공격에는 상대적으로 강함. 외부 사이트가 피해자 브라우저의 localStorage에서 토큰을 읽어 Authorization 헤더를 임의로 붙일 수 없기 때문임.
다만 정확한 표현은 다음과 같음.
- JWT + localStorage는 쿠키 자동 전송을 악용하는 전통적 CSRF 위험을 낮추지만, XSS까지 해결하는 방식은 아님
- XSS가 발생하면 악성 스크립트가 localStorage의 토큰을 훔치거나, 사용자의 브라우저 안에서 인증 요청을 보낼 수 있음
---
### 쿠키는 왜 위험할 수 있는가
쿠키는 JavaScript의 Axios 요청뿐 아니라 브라우저가 보내는 요청에 자동으로 포함될 수 있음.
- HTML `<form>` 제출
- 일부 링크 이동
- 이미지·리소스 요청
- 브라우저 자동 요청
그래서 인증 쿠키를 사용할 때는 서버가 "이 요청이 정말 우리 사이트에서 온 것인가"를 추가로 확인해야 함.
---
### 세션·쿠키 방식의 CSRF 방어 방법
① CSRF 토큰
서버가 예측하기 어려운 토큰을 발급하고, 요청마다 함께 보내게 함.
```plain text
정상 사이트  → CSRF 토큰을 알고 있음
공격 사이트  → CSRF 토큰을 알 수 없음
```
서버는 쿠키뿐 아니라 CSRF 토큰까지 맞아야 요청을 처리함.
---
② SameSite 쿠키 옵션
다른 사이트에서 들어온 요청에 쿠키를 어느 정도 보낼지 제어함.
```plain text
SameSite=Lax
```
- 같은 사이트 내부 요청: GET, POST, PUT, DELETE 모두 쿠키가 정상적으로 붙을 수 있음
- 외부 사이트에서 유도한 요청: 쿠키 전송이 제한될 수 있음
- Lax는 일부 최상위 페이지 이동 GET 같은 경우 쿠키를 허용할 수 있음
SameSite=Lax를 적용한다고 내 서비스 내부 POST·PUT 요청이 막히는 것은 아님.
---
③ 커스텀 헤더와 서버 검증
AJAX 요청에 커스텀 헤더를 요구하는 방식도 보조 수단이 될 수 있음.
```plain text
X-Requested-With
```
일반 HTML form은 임의의 커스텀 헤더를 붙이기 어려움. 다만 이것만으로 모든 CSRF를 해결한다고 보면 안 되고, CSRF 토큰·SameSite·Origin/Referer 검증과 함께 설계하는 것이 안전함.
---
### 외부 사이트에서 GET 요청은 왜 남길 수 있는가
#### 외부 GET을 모두 막지 않는 이유
외부 GET까지 모두 막으면 정상적인 사용자 경험이 나빠짐.
- 카카오톡 링크
- 구글 검색 결과
- 이메일 링크
- 블로그·뉴스 링크
이런 경로로 서비스에 들어올 때마다 로그인 상태가 깨지거나 접근이 어려워질 수 있음. 또한 HTTP 설계에서 GET은 원칙적으로 데이터를 읽는 요청이고, 서버 상태를 변경하면 안 됨. 중요한 변경 작업은 GET이 아니라 POST, PUT, PATCH, DELETE 같은 메서드로 설계해야 함.
---
### 민감한 GET 응답은 외부 사이트에 보이지 않는가
외부 사이트가 단순히 사용자를 특정 페이지로 이동시키는 것과, 외부 사이트 JavaScript가 응답 내용을 읽는 것은 다름.
일반적으로 브라우저의 SOP(동일 출처 정책)와 CORS 정책 때문에 외부 사이트 JavaScript는 다른 출처의 민감한 응답 본문을 마음대로 읽지 못함.
```plain text
외부 사이트 JavaScript
  └─ 다른 도메인의 민감 응답 읽기 시도
       └─ 브라우저가 SOP / CORS 정책으로 차단
```
다만 이것이 민감 GET 설계를 가볍게 해도 된다는 의미는 아님.
- 민감 데이터는 적절한 인증·인가가 필요함
- GET 요청은 서버 상태를 변경하면 안 됨
- URL Query String에 토큰·개인정보를 넣으면 안 됨
- 응답 데이터는 CORS 설정과 캐시 정책까지 고려해야 함
---
### localStorage + JWT의 진짜 위험: XSS
#### XSS가 무엇인가
공격자가 악성 JavaScript를 서비스 화면에서 실행시키는 공격임.
```html
<script>
// 악성 코드
</script>
```
이 코드가 내 서비스 도메인에서 실행되면 localStorage에 접근할 수 있음.
---
### 토큰이 탈취되면 Payload만 보이는 것이 아님
토큰의 내용을 수정하지 못해도, 정상 서명이 있는 원본 토큰 전체를 훔치면 공격자는 그 토큰을 그대로 사용할 수 있음. 공격자는 토큰을 계산하거나 위조할 필요가 없음.
```plain text
정상 사용자 JWT 탈취
  ↓
공격자가 JWT 원본을 Authorization 헤더에 넣음
  ↓
서버는 정상 서명이므로 피해자 요청으로 인식
  ↓
송금·수정·탈퇴 등 권한 범위의 요청이 가능할 수 있음
```
JWT Signature는 "토큰 위조"를 막지만, 토큰 탈취 후 재사용까지 막아주지는 않음.
---
### localStorage를 유지한다면
XSS 방어를 강하게 해야 함.
- v-html 사용을 최대한 피함
- 입력값을 검증·정화함
- 신뢰되지 않은 HTML을 렌더링해야 한다면 DOMPurify 같은 도구를 사용함
- CSP(Content Security Policy)를 설정함
- 외부 스크립트와 서드파티 의존성을 관리함
- 토큰 만료 시간을 짧게 둠
- 로그아웃·탈취 의심 시 토큰 폐기 전략을 마련함
---
### 더 안전한 실무 패턴: Access Token + Refresh Token
```plain text
Access Token
  └─ Pinia / 메모리 보관
  └─ 짧은 수명, 예: 15분

Refresh Token
  └─ httpOnly + Secure + SameSite 쿠키
  └─ 비교적 긴 수명, 예: 2주
```
흐름:
```plain text
1. 로그인 성공
2. Access Token은 메모리(Pinia)에 보관
3. Refresh Token은 httpOnly Cookie에 보관
4. Access Token 만료
5. Refresh Token으로 Access Token 재발급
6. 새 Access Token을 다시 Pinia에 저장
```
장점:
- Access Token을 JavaScript 영구 저장소에 오래 남기지 않음
- Refresh Token은 httpOnly Cookie라 JavaScript가 직접 읽기 어려움
- Access Token 탈취 피해 시간을 짧게 제한할 수 있음
다만 Refresh Token이 쿠키에 있으므로 CSRF, SameSite, CORS, 토큰 회전, 로그아웃 시 폐기 같은 설계를 함께 해야 함.
---
### 최종 결론
#### Pinia를 쓰는 이유
Pinia를 쓰는 핵심 이유는 반응형 UI 상태 관리임.
- Pinia 값 변경 → 화면 즉시 갱신
- localStorage 값 변경 → 화면 자동 갱신 안 됨
- Pinia는 백엔드 요청 횟수나 인증 보안을 직접 해결하는 도구가 아님
- Pinia는 현재 브라우저 탭의 애플리케이션 메모리 상태를 관리함
React에서도 이름만 다를 뿐 같은 역할의 도구가 있음.
- Redux
- Zustand
- Recoil
- Context API
- Jotai 등
Pinia는 Vue에서 사용하는 상태 관리 방식이고, React에도 같은 문제를 해결하는 도구들이 존재함.
---
### 로그인 때 새로고침하면 Pinia가 필요 없는가
기술적으로는 로그인 성공 후 강제 새로고침을 할 수 있음. 하지만 SPA에서는 권장하지 않음.
- 화면이 깜빡임
- SPA의 장점이 사라짐
- 작성 중인 입력 데이터가 날아갈 수 있음
- 장바구니·좋아요·알림·권한 메뉴 같은 실시간 상태를 자연스럽게 관리하기 어려움
- 사용자 경험이 나빠짐
따라서 실무에서는 새로고침 대신 Pinia 같은 상태 관리 도구로 UI를 반응형으로 갱신함.
---
### 한 문장 요약
localStorage는 상태를 오래 보관하기 위한 저장소이고, Pinia는 현재 화면을 즉시 바꾸기 위한 반응형 상태 저장소임. JWT·세션·쿠키는 서버 인증 방식이며, 실제 보안은 인증 이후의 인가 검증과 CSRF·XSS 대응까지 함께 설계해야 완성됨.
---
<empty-block/>