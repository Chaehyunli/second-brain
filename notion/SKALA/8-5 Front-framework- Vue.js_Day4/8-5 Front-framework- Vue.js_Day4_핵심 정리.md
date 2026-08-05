---
title: "[8/5] Front-framework: Vue.js_Day4_핵심 정리"
notion_page_id: "3b21d84b-f68e-8077-81d1-ece6eae0d4d3"
source_url: "https://app.notion.com/p/3b21d84bf68e807781d1ece6eae0d4d3"
synced_at: "2026-08-06T08:00:00+09:00"
content_sha256: "eef35bd03a8eeec58f5ab6c15b9e9eecf34e7488bfd5b55873baed89d311a707"
tags: [notion, skala, learning, vue, frontend, element-plus, javascript]
---

# [8/5] Front-framework: Vue.js_Day4_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b21d84bf68e807781d1ece6eae0d4d3) (2026-08-06 확인)
>
> 맥락: [[notion/SKALA/8-4 Front-framework- Vue.js_Day3/8-4 Front-framework- Vue.js_Day3_핵심 정리|Vue.js Day3]]의 Router·Pinia·HTTP 통신을 바탕으로, Vue UI 라이브러리와 Modern JavaScript·정적 분석·빌드 도구를 연결한다.

### UI 라이브러리 (UI Library)
웹 애플리케이션 UI 구축에 필요한 공통 컴포넌트(Button, Input, Form, Dialog, Table 등)를 **Vue 3 컴포넌트 단위로 모듈화**하여 제공하는 오픈소스 소프트웨어 패키지임.
#### 사용 효과
- 개발 리소스 절감: CSS 스타일시트·HTML 마크업을 직접 작성하는 대신 완성된 컴포넌트 태그를 호출하므로 UI 구현 속도가 향상됨
- 크로스 브라우징 및 반응형 대응: Chrome, Safari, Firefox 등 다양한 브라우저와 Mobile·Tablet·Desktop 해상도별 미디어 쿼리가 내부적으로 최적화되어 있음
- 웹 표준 및 접근성(WAI-ARIA) 준수: 스크린 리더 인식, 키보드 포커스 제어 등 접근성 가이드라인이 컴포넌트 레벨에서 사전 구현되어 있음
---
### Vue 3 생태계 주요 UI 라이브러리 비교
| 비교 항목 | Vuetify | Element Plus | PrimeVue |
| --- | --- | --- | --- |
| 기반 디자인 명세 | Google Material Design | Enterprise Desktop View | Multi-Theme & Flex CSS |
| TypeScript 지원 | 지원 완료 | 완전 기본 내장 (최상) | 지원 완료 |
| 스타일 격리/커스텀 | SASS 변수 수정 방식 | CSS 변수 수정 방식 | Unstyled 모드 지원 (최상) |
| 특화 컴포넌트 | Mobile V-App Layout | Data Table, Form Validation | Advanced Chart, Tree Table |
| 전용 컴포넌트 태그 예시 | `<v-btn>` | `<el-button>` | `<Button>` |
- Global 시장에서는 PrimeVue와 Vuetify의 점유율이 높으며, 국내에서는 Element Plus의 점유율이 높음
- Element Plus의 학습 난이도가 가장 낮음
---
### Element Plus - 둘러보기
공식 사이트: [https://element-plus.org/](https://element-plus.org/)
세 가지 진입점을 제공함.
- Guide: 디자인 가이드라인을 이해하고 논리적으로 구조화된 컴포넌트를 설계하는 방법을 안내함
- Component: 컴포넌트 데모를 통해 상호작용 세부사항을 직접 체험하고 캡슐화된 코드를 활용할 수 있음
- Resource: 페이지 프로토타입·비주얼 초안 제작을 위한 디자인 리소스를 다운로드할 수 있음
---
### Element Plus - Installation
#### 설치 명령
```bash
# skala-vue 프로젝트 디렉터리에서 실행
npm install element-plus
```
설치 완료 시 21개 패키지가 추가되며 취약점 0건임을 확인할 수 있음.
#### 설치 확인 (package.json)
```json
"dependencies": {
  "axios": "^1.18.1",
  "element-plus": "^2.14.2",
  "pinia": "^3.0.4",
  "vue": "^3.5.32",
  "vue-router": "^5.0.4"
}
```
`element-plus` 항목이 dependencies에 추가되었음을 확인하면 정상 설치된 것임.
---
### Element Plus - Quick Start
#### 전역 설정 주입 (src/main.js)
```javascript
// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

// Element Plus 모듈 및 필수 CSS 장부 파일 Import
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus) // Vue 앱에 Element Plus 사용 등록

app.mount('#app')
```
- `ElementPlus`를 import한 뒤 **`app.use(ElementPlus)`** 로 플러그인 등록해야 전역에서 컴포넌트를 사용할 수 있음
- CSS 파일(`element-plus/dist/index.css`)도 반드시 함께 import해야 스타일이 적용됨
---
### Element Plus Component - Basic
화면 구조를 잡고 Text·Button 등 가장 기본적인 컴포넌트 모음임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Button | `<el-button>` | 다양한 색상, 크기, 비활성화 등을 지원하는 실무 표준 버튼 컴포넌트 |
| Border | (CSS Utility) | 컴포넌트의 테두리 둥글기(Radius)와 두께 표준 디자인 시스템 규격 |
| Color | (CSS Utility) | 브랜드 메인 컬러, 성공, 실패 등 Element Plus가 규정한 색상 세트 |
| Container | `<el-container>` | 레이아웃 외곽을 잡는 부모 컨테이너 (`<el-header>`, `<el-aside>` 등과 결합) |
| Icon | `<el-icon>` | 시스템 아이콘(화살표, 검색 등)을 손쉽게 주입하는 전용 아이콘 시스템 |
| Layout | `<el-row>`, `<el-col>` | 24분할 기반의 정밀한 반응형 그리드(Grid) 레이아웃 배치 시스템 |
| Link | `<el-link>` | 스타일 처리와 밑줄, 아이콘 결합이 내장된 텍스트 하이퍼링크 부품 |
| Text | `<el-text>` | 크기, 두께, 말줄임표(Truncate) 처리가 손쉬운 표준 텍스트 컴포넌트 |
| Scrollbar | `<el-scrollbar>` | 브라우저 기본 스크롤바 대신 세련된 커스텀 스크롤바를 씌우는 부품 |
| Space | `<el-space>` | 자식 컴포넌트들 간의 가로/세로 여백(Gap)을 균일하게 통제하는 인프라 |
| Splitter | `<el-splitter>` | 화면을 좌우/상하로 분할하고 마우스 드래그로 너비를 조절하는 레이아웃 부품 |
| Typography | (CSS Utility) | 웹 서비스 전체의 표준 글자 폰트, 크기, 행간 명세 장부 |
---
### Element Plus Component - Configuration
애플리케이션 전체의 글로벌 설정을 중앙 통제하는 레이어임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Config Provider | `<el-config-provider>` | 프로젝트 전체의 다국어 언어팩(Locale), 컴포넌트 기본 크기, z-index를 일괄 제어 |
---
### Element Plus Component - Form
회원가입, 조건 검색 등 데이터를 입력하고 검증하는 컴포넌트임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Autocomplete | `<el-autocomplete>` | 사용자가 입력 시 백엔드 추천 검색어 목록을 아래에 즉시 띄워주는 인풋창 |
| Cascader | `<el-cascader>` | 시/도 → 구/군 → 동처럼 계층 구조의 데이터를 단계별로 선택하는 창 |
| Checkbox | `<el-checkbox>` | 다중 선택(체크박스) 및 그룹화 기능 컴포넌트 |
| Color Picker | `<el-color-picker>` | 마우스 클릭으로 웹 표준 컬러차트에서 색상을 선택하는 부품 |
| Date Picker | `<el-date-picker>` | 실무 빈도 최상. 달력이 팝업되어 날짜 또는 기간 범위를 선택하는 부품 |
| DateTime Picker | `<el-date-time-picker>` | 날짜 선택과 동시에 몇 시 몇 분 초(시간)까지 통합 정밀 선택하는 달력 |
| Form | `<el-form>`, `<el-form-item>` | 입력창들을 감싸서 실시간 데이터 검증(Validation) 및 경고 메시지를 뿜는 통제소 |
| Input | `<el-input>` | 기본 텍스트, 비밀번호(눈 아이콘), 한 번에 지우기(X) 등을 지원하는 필수 인풋 |
| Input Number | `<el-input-number>` | 오직 숫자만 입력받으며 +, - 버튼으로 수량을 조절하는 전용 인풋 |
| Input Tag | `<el-input-tag>` | 키워드를 입력하고 엔터를 치면 블록 태그 형태로 칩을 생성해 주는 입력창 |
| Input OTP | `<el-input-otp>` | 금융 앱이나 인증 번호 4\~6자리를 한 칸씩 입력하도록 쪼개놓은 보안 인증 박스 |
| Mention | `<el-mention>` | @나 #를 타이핑하면 슬랙이나 디스코드처럼 사용자 멘션 창을 띄워주는 부품 |
| Radio | `<el-radio>` | 여러 단일 선택지 중 무조건 1개만 고르도록 통제하는 라디오 버튼 |
| Rate | `<el-rate>` | 쇼핑몰 별점 점점(★)을 마우스 드래그나 클릭으로 입력하는 부품 |
| Select | `<el-select>` | 화살표를 누르면 하부 옵션 목록이 슬라이딩 드롭다운되는 표준 선택 상자 |
| Virtualized Select | `<el-select-v2>` | 셀렉트 박스 안에 옵션이 수만 개일 때 화면 버벅임 없이 렌더링하는 가상 스크롤 버전 |
| Slider | `<el-slider>` | 바(Bar) 위의 볼륨 조절 슬라이더를 마우스로 밀어서 수치 범위를 지정하는 부품 |
| Switch | `<el-switch>` | ON/OFF, 토글 모드, 다크모드 스위칭을 시각적으로 변환하는 버튼 |
| Time Picker | `<el-time-picker>` | 특정 시각을 시\:분\:초 단위로 롤링하여 정밀 선택하는 스크롤 피커 |
| Time Select | `<el-time-select>` | 09:00, 09:30 등 미리 지정된 정시 타임라인 목록 중 하나를 선택하는 박스 |
| Transfer | `<el-transfer>` | 왼쪽 바구니의 대량 목록 중 선택한 아이템들을 오른쪽 바구니로 이동시키는 검수기 |
| TreeSelect | `<el-tree-select>` | 조직도나 폴더 트리 구조 형태를 품고 있는 고급형 드롭다운 선택 상자 |
| Upload | `<el-upload>` | 마우스 클릭 혹은 드래그 앤 드롭으로 파일을 첨부해 백엔드로 전송하는 인프라 |
---
### Element Plus Component - Data
백엔드에서 전달받은 데이터 등을 표나 리스트로 가공해 뿌리는 컴포넌트임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Avatar | `<el-avatar>` | 유저 프로필 사진을 동그라미 혹은 사각형으로 이쁘게 크롭해 주는 부품 |
| Badge | `<el-badge>` | 알림 아이콘 우측 상단에 빨간색 숫자 \[9+\] 배지를 달아주는 알림 카운터 |
| Calendar | `<el-calendar>` | 화면 전체에 큼직한 월간 달력 판을 깔아서 스케줄을 기록 및 렌더링하는 컴포넌트 |
| Card | `<el-card>` | 외곽 새도우 펜스를 치는 만능 레이아웃 블록 |
| Carousel | `<el-carousel>` | 광고 배너나 이미지들이 좌우로 슬라이딩 서커스하며 롤링되는 슬라이더 뷰어 |
| Collapse | `<el-collapse>` | 질문을 누르면 하부 답변 내용이 아코디언처럼 아래로 슥 펼쳐지는 접이식 메뉴 |
| Countdown | `<el-countdown>` | 타임세일, 시험 종료 시간 등을 실시간 초 단위로 마이너스 카운팅하는 시계 |
| Descriptions | `<el-descriptions>` | 회원 정보 조회 화면처럼 이름:홍길동 / 나이:20 구조의 정갈한 명세서 표 |
| Empty | `<el-empty>` | "조회된 검색 결과가 없습니다" 라는 안내 이미지와 안내 문구를 자동 배치 |
| Image | `<el-image>` | 로딩 실패 시 대체 이미지 처리 및 클릭 시 확대(Viewer) 기능이 내장된 이미지 태그 |
| Infinite Scroll | `v-infinite-scroll` | 인스타그램처럼 스크롤을 맨 아래로 내리면 다음 데이터를 알아서 계속 이어 붙이는 장치 |
| Pagination | `<el-pagination>` | 데이터가 많을 때 \[1\] \[2\] \[3\] ... \[다음\] 구조로 페이지를 쪼개주는 네비게이터 |
| Progress | `<el-progress>` | 진행률이나 다운로드 게이지 바를 퍼센트(%) 애니메이션 그래프로 보여주는 바 |
| Result | `<el-result>` | 결제 성공(Green 체크), 실패(Red 엑스) 화면을 아이콘과 함께 통째로 그려주는 완성판 |
| Skeleton | `<el-skeleton>` | 실제 데이터가 오기 전, 회색빛 유령 레이아웃을 띄워 유저의 체감 속도를 높이는 버퍼 |
| Table | `<el-table>` | 실무 점유율 1위. 정렬, 필터, 열 고정, 합계 연산이 탑재된 끝판왕 그리드 표 |
| Statistic | `<el-statistic>` | 매출액 1,500,000처럼 숫자에 콤마를 달고 강조해 주는 통계 전용 텍스트 부품 |
| Tag | `<el-tag>` | 키워드나 상태값(맑음, 비, 완료)을 색상 배지 형태로 강조하는 칩 태그 |
| Timeline | `<el-timeline>` | 1일차 → 2일차 → 3일차처럼 시간 흐름순 이력을 수직선 그래프로 정렬하는 카드 |
| Tour | `<el-tour>` | 신규 유저 진입 시 "여기를 클릭하세요" 하고 가이드를 돌며 팝업 팁을 안내하는 튜토리얼 |
| Tree | `<el-tree>` | 폴더 구조나 부서 조직도 데이터를 계층형 아코디언 구조로 트리화하는 컴포넌트 |
| Watermark | `<el-watermark>` | 기업 대외비 문서 화면 뒤쪽에 로그인 유저 이메일을 투명하게 도배하는 보안 부품 |
| Upload | `<el-upload>` | 마우스 클릭 혹은 드래그 앤 드롭으로 파일을 첨부해 백엔드로 전송하는 인프라 |
---
### Element Plus Component - Navigation
화면 경로 이동 및 조종과 관련된 컴포넌트임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Anchor | `<el-anchor>` | 긴 스크롤 문서의 목차를 우측에 띄워 클릭 시 해당 섹션 위치로 고속 워프하는 링크 |
| Backtop | `<el-backtop>` | 스크롤을 한참 내렸을 때 화면 우측 하단에 뜨는 "맨 위로 이동(▲)" 마법 버튼 |
| Breadcrumb | `<el-breadcrumb>` | 현재 유저 위치 경로를 Dashboard \> Weather \> Suwon 형태로 정렬해 주는 텍스트 바 |
| Dropdown | `<el-dropdown>` | 마우스를 올리거나 클릭하면 하부 액션 메뉴 목록이 주르륵 내려오는 드롭다운 메뉴 |
| Menu | `<el-menu>` | 사내 시스템 좌측에 들어가는 정석적인 아코디언 사이드바 내비게이션 메뉴 시스템 |
| Page Header | `<el-page-header>` | 페이지 상단 뒤로가기 버튼과 현재 서브 타이틀을 잡아주는 표준 헤더 가이드라인 |
| Steps | `<el-steps>` | 정보입력 → 본인인증 → 가입완료 단계 진행 상태를 숫자로 시각화하는 바 |
| Tabs | `<el-tabs>` | 한 화면 안에서 1번 탭, 2번 탭을 누를 때마다 하부 본문만 스위칭해 주는 전환 탭 |
---
### Element Plus Component - Feedback
사용자에게 알림, 경로, 로딩, 확인 등의 신호를 보내는 컴포넌트임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Alert | `<el-alert>` | 화면 상단 고정 공간에 경고나 성공 공지사항 문구를 알림 띠 형태로 박아놓는 부품 |
| Dialog | `<el-dialog>` | 화면 중앙에 어두운 딤드(Dimmed) 처리를 하고 팝업창을 띄우는 정석 모달창 |
| Drawer | `<el-drawer>` | 스마트폰 앱 메뉴처럼 화면 우측이나 좌측에서 거대한 서랍장이 스르륵 열리는 슬라이드 창 |
| Loading | `v-loading` (Directive) | 태그에 이 지시어만 적어주면 데이터 수신 중일 때 예쁜 회전 스피너와 막을 쳐주는 사양 |
| Message | `ElMessage` (JS Call) | 화면 상단 중앙에 2초간 "저장 완료" 토스트 알림을 띄우고 하늘로 사라지는 일시 알림창 |
| MessageBox | `ElMessageBox` | 브라우저 구식 alert(), confirm()을 완벽히 대체하는 세련된 최종 확인 팝업창 |
| Notification | `ElNotification` | 화면 우측 구석탱이에서 윈도우 알림처럼 상세 메시지 카드를 띄워주는 고급 알림창 |
| Popconfirm | `<el-popconfirm>` | 삭제 버튼을 누르면 버튼 바로 위에 조그맣게 "진짜 지울래?" 말풍선 팝업을 띄우는 팝업 확인창 |
| Popover | `<el-popover>` | 마우스를 특정 단어에 올리면 상세 가이드 백과사전 설명창을 풍선처럼 띄워주는 부품 |
| Tooltip | `<el-tooltip>` | 아이콘에 마우스를 대면 위/아래에 "검색하기" 같은 툴팁 힌트 글자를 출력해 주는 기능 |
---
### Element Plus Component - Others
기타 특수 유틸리티 시각 요소 및 기능과 관련된 컴포넌트임.
| 컴포넌트명 | 전용 태그 | 기능 설명 |
| --- | --- | --- |
| Affix | `<el-affix>` | 스크롤을 내려도 특정 메뉴나 버튼이 화면 최상단에 껌딱지처럼 계속 고정되어 따라오는 장치 |
| Animate | (CSS Utility) | 컴포넌트들이 화면에 나타나거나 사라질 때 주는 내장 애니메이션 효과 세트 |
| Segmented | `<el-segmented>` | 라디오 버튼을 가로형 슬라이딩 스위치 바 탭 형태로 모던하게 진화시킨 제어 컨트롤러 |
---
### Modern JavaScript - History
JavaScript의 역사는 4세대로 구분됨.
- 1세대 — ECMAScript 탄생 (1995\~1999): Netscape(1995)에서 브라우저 동적 기능을 위해 JavaScript를 설계함. Microsoft IE가 유사한 JScript를 탑재하자 브라우저마다 코드가 달라지는 문제가 생겨, ECMA 국제 표준기구에서 **ECMAScript(ES)** 표준 규격을 정의함(1997)
- 2세대 — Web의 한계와 jQuery (2000\~2008): IE 독점으로 표준화(ES4)가 무산되고 JS는 가벼운 Visual Script 취급을 받음. 이후 브라우저별 코드 차이 문제를 해결한 **jQuery**가 등장해 시장을 지배함
- 3세대 — ES5의 표준 (2009\~2014): Chrome 탄생과 함께 V8 엔진이 공개되고, 이를 기반으로 **Node.js**가 탄생하여 JS가 서버 환경에서도 실행 가능해짐. ES5가 표준으로 제정되며 `'use strict'`, `forEach`, `map`, `filter` 등 도입
- 4세대 — Modern JavaScript (2015\~): ES6(ECMAScript 2015)에서 문법·기능이 대규모 개편됨. 이후 매년 소규모 업데이트를 발표하는 연례 정책이 정착되었으며, 이를 통칭해 **Modern JavaScript**라 부름
---
### Modern JavaScript - Browser Support
#### 브라우저별 ECMAScript 반영 현황 (2026년 기준)
- ES6\~ES11 (2015\~2020): `let/const`, Arrow Function, Promise, `async/await`, Optional Chaining(`?.`) 등은 데스크톱·모바일 브라우저 모두 100% 네이티브 지원
- ES12\~ES15 (2021\~2024): `replaceAll()`, Logical Assignment(`&&=`, `||=`), `Array.prototype.toReversed()` 등 최신 메서드도 모던 브라우저 점유율 기준 96% 이상 지원
- ES16+ (2025\~2026): Stage 3\~4 제안 단계이거나 막 통과된 문법들은 Chrome 카나리 버전에 선반영되어 실험적으로 동작하며, 브라우저 버전업에 따라 순차적으로 자동 탑재됨
---
### Core Syntax - let & const
| 특성 | var (구시대의 유산) | let (변수) | const (상수) |
| --- | --- | --- | --- |
| 스코프 | 함수 레벨 스코프 | 블록 레벨 스코프 (`{}`) | 블록 레벨 스코프 (`{}`) |
| 재선언 | 가능 (버그의 원인) | 불가능 | 불가능 |
| 재할당 | 가능 | 가능 | **불가능** |
| 호이스팅 | 발생 (undefined로 초기화) | 발생 (TDZ로 인해 에러 발생) | 발생 (TDZ로 인해 에러 발생) |
#### 재선언/재할당 예시
```javascript
// var: 재선언 가능 → 버그 원인
var name = "철수";
var name = "영희";
console.log(name); // 출력결과: 영희

// const: 재선언 불가
const name = "철수";
const name = "영희"; // 에러: Identifier 'name' has already been declared

// let: 재할당 가능, 재선언 불가
let name = "철수";
name = "영희";
console.log(name); // 출력결과: 영희

// const: 재할당 불가
const name = "철수";
name = "영희"; // 에러: Assignment to constant variable
```
---
### Core Syntax - Arrow Function
#### 함수 선언 방식 비교
| 비교 항목 | Function Declaration | Function Expression | Arrow Function |
| --- | --- | --- | --- |
| Syntax | `function foo(arg1, ...) { return; }` | `const foo = function(arg1, ...) { return; }` | `const foo = (arg1, ...) => { return; }` |
| Hoisting | 함수 전체가 호이스팅됨 (선언문 전에도 호출 가능) | 변수만 호이스팅됨 (초기화 전 호출 시 에러) | 변수만 호이스팅됨 (초기화 전 호출 시 에러) |
| 주요 용도 | 전통적인 전역 / 유틸리티 함수 정의 | 클로저(Closure) 구현, 콜백 함수 | **모던 프레임워크(Vue/React)**, 메서드 내부 비동기 콜백 함수 |
#### Arrow Function 특징
- 함수 내부 코드가 한 줄이면 `return` 문 생략 가능
```javascript
const sum = (num1, num2) => num1 + num2;
```
- 매개변수가 1개이면 소괄호 생략 가능
```javascript
const pow = x => x * x;
```
- 화살표 함수를 매개변수로 전달 가능 (고차 함수 활용)
```javascript
const calculate = (num1, num2, operation) => {
  return operation(num1, num2); // 배달받은 화살표 함수를 여기서 대신 실행
};
const addResult = calculate(10, 5, (a, b) => a + b);
console.log(`더하기 결과:${addResult}`); // 출력: 15
const multiplyResult = calculate(10, 5, (a, b) => a * b);
console.log(`곱하기 결과:${multiplyResult}`); // 출력: 50
```
---
### Core Syntax - Template Literals
ES6에서 도입된 문자열 표기법으로, 문자열 내부에 변수나 연산 결과를 동적으로 주입하고 줄바꿈을 자유롭게 허용함. 일반 따옴표(`'`, `"`)가 아닌 **Backtick(****`\``****)** 기호를 사용함.
- `${변수명}` 또는 `${연산식}`으로 문자열 보간 처리
```javascript
const city = '수원';
const temp = 24;
// 기존 방식
const message = '현재 ' + city + '의 기온은 ' + temp + '도입니다.';
// 템플릿 리터럴 방식
const message = `현재${city}의 기온은${temp}도입니다.`;
```
- 백틱 안에서 Enter를 치는 대로 줄바꿈이 그대로 반영됨 (기존의 `\n` 불필요)
```javascript
// 기존 방식
const htmlTemplate = '<div>\n' + '  <h1>Hello</h1>\n' + '</div>';

// 템플릿 리터럴 방식
const htmlTemplate = `
  <div>
    <h1>Hello</h1>
  </div>
`;
```
---
### Core Syntax - Destructuring Assignment
Array나 Object의 구조를 분해하여 내부 값들을 개별 변수에 직접 할당하는 표현식임. 인덱스 접근(`arr[0]`)이나 점 표기법(`obj.key`) 반복을 제거하고 코드를 획기적으로 단축함.
#### Object Destructuring
객체의 key를 기준으로 매칭하여 추출함. **순서는 상관없으며 이름만 맞으면** 값이 할당됨.
```javascript
const user = { name: '홍길동', age: 20, role: 'admin' };

// 기존 방식
const name = user.name;
const age = user.age;

// 구조분해 할당
const { name, age } = user;
```
#### Array Destructuring
- Index 위치(순서)를 기준으로 대칭 할당됨.
```javascript
const coords = [37.5, 127.0];

// 기존 방식
const latitude = coords[0];
const longitude = coords[1];

// 구조분해 할당
const [latitude, longitude] = coords;

// 특정 위치를 건너뛰고 싶을 때: 쉼표 공백 배치
const colors = ['red', 'green', 'blue'];
const [first, , third] = colors; // green은 건너뛰고 'red'와 'blue'만
```
---
### Core Syntax - Spread Operator (`...`)
배열이나 객체 앞에 마침표 3개(`...`)를 붙여, 내부 요소를 **하나하나 날개로 순서대로 펼쳐서(전개하여) 흩뿌려주는** 연산자임. 복잡한 반복문 없이 대량의 데이터를 복사하거나 결합할 수 있음.
#### Array에서의 활용
```javascript
// 배열 병합
const frontEnd = ['HTML', 'CSS', 'Vue'];
const backEnd = ['Java', 'Spring'];
const fullStack = [...frontEnd, ...backEnd, 'Git'];
console.log(fullStack); // ['HTML', 'CSS', 'Vue', 'Java', 'Spring', 'Git']

// 배열 복사 (얕은 복사)
const original = [1, 2, 3];
const cloneWrong = original;        // 단순 대입(=)은 주소값만 복사 → 원본도 깨짐
const cloneRight = [...original];   // 스프레드: 원본과 주소가 완전히 분리된 독립적인 새 복사본 생성

cloneRight.push(99);
console.log(original);   // [1, 2, 3] (원본 안전 보존)
console.log(cloneRight); // [1, 2, 3, 99]
```
#### Object에서의 활용
기존 객체의 속성을 그대로 유지하면서 특정 데이터만 수정하거나 추가된 새로운 객체를 리턴할 때 사용함. Vue의 상태 관리나 백엔드 요청 바디를 만들 때 필수 문법임.
```javascript
const baseConfig = { theme: 'dark', language: 'ko', version: 1.0 };

const newConfig = {
  ...baseConfig,
  version: 2.0,    // 동일한 key가 있으면 뒤에 적힌 값이 앞의 값을 덮어씀 (Override)
  author: 'Graves' // 새로운 key-value 추가
};

console.log(newConfig);
// { theme: 'dark', language: 'ko', version: 2.0, author: 'Graves' }
```
#### 문자열·함수 인수 전개
```javascript
// 문자열을 문자 하나씩 쪼개서 전개
const str = `Hello`;
const charArray = [...str];
console.log(charArray); // ['H', 'e', 'l', 'l', 'o']

// 배열을 함수 인수로 전개
function sum(a, b, c) { return a + b + c; }
const numbers = [1, 2, 3];
const result = sum(...numbers); // 6이 할당됨
```
---
### Core Syntax - Rest 문법 (`...`)
똑같이 `...` 기호를 쓰지만 **Spread가 값을 전개하는 데 활용**된다면, **Rest는 나머지 값을 처리하는 데 활용**됨.
#### Destructuring Assignment에서의 REST
몇 개만 빼고 남은 속성을 한데 묶어 별도의 객체나 배열로 보존함.
```javascript
const employee = { name: 'Graves', age: 35, role: 'Instructor', team: 'Edu-Tech', location: 'Seoul' };

// name과 age만 개별 변수로 꺼내고, 나머지 속성들은 restInfo 객체에 담아라!
const { name, age, ...restInfo } = employee;
console.log(name);     // 'Graves'
console.log(age);      // 35
console.log(restInfo); // { role: 'Instructor', team: 'Edu-Tech', location: 'Seoul' }
```
#### 함수 매개변수에서의 Rest (나머지 매개변수)
```javascript
// 앞의 두 개는 1등, 2등 변수에 담고, '나머지(Rest)' 참가자들은 한꺼번에 others 배열 주머니에 수집
const printMedalList = (gold, silver, ...others) => {
  console.log(`금메달:${gold}`);            // 금메달: 수원
  console.log(`은메달:${silver}`);          // 은메달: 서울
  console.log(`나머지 참가자 명단:`, others); // ['부산', '대구', '제주', '광주']
};

printMedalList('수원', '서울', '부산', '대구', '제주', '광주');
```
---
### Core Syntax - Promise
JavaScript 엔진에서 비동기 연산의 최종 완료 또는 실패와 그 결과 값을 나타내는 표준 객체임. ES6 이전에는 비동기 처리 후 실행할 로직을 Callback 함수 인자로 전달하는 방식을 사용했으며, 이는 **Callback Hell**을 유발했음.
#### Promise의 3가지 상태
| 상태 | 설명 |
| --- | --- |
| Pending (대기) | 초기 상태. 작업이 시작되었으나 아직 완료/실패되지 않은 상태 |
| Rejected (거부/실패) | 작업이 실패했고 에러 이유가 존재하는 상태 |
| Fulfilled (이행/성공) | 작업이 성공적으로 완료되었고 결과 값이 존재하는 상태 |
#### Promise Chains (`.then` / `.catch`)
Promise 객체 뒤에 메서드를 체인 형태로 엮어서 성공과 실패 파이프라인을 통제함.
```javascript
fetchWeatherData()                         // fetchWeatherData는 Promise 객체를 return
  .then((data) => {
    console.log('서버 통신 성공:', data);  // Fulfilled 상태일 때 실행: 성공 데이터 가공
  })
  .catch((error) => {
    console.error('네트워크 에러 발생:', error); // Rejected 상태일 때 실행: 에러 예외 처리
  })
  .finally(() => {
    console.log('비동기 통신 프로세스 완전 종료'); // 성공/실패 무관하게 무조건 마지막에 실행 (예: 로딩 스피너 종료)
  });
```
---
### Core Syntax - async / await
ES8(2017)에서 도입됨. Promise를 기반으로 작동하되, 비동기 흐름(Chaining) 대신 **동기식 코드 구조**로 작성할 수 있게 해줌.
- **async**: "이 함수 안에서 비동기 처리를 할 거야!"라고 선언하는 키워드. async 함수는 항상 Promise를 반환함.
- **await**: "비동기 작업이 끝날 때까지 다음 줄로 넘어가지 말고 기다려!"라고 명령하는 키워드
```javascript
async function hello() {
  return "안녕하세요!";
}
console.log(hello()); // Promise {<fulfilled>: '안녕하세요!'}
hello().then(res => console.log(res)); // 안녕하세요!
```
```javascript
async function handleData() {
  try {
    const result = await fetchData();             // 첫 번째 비동기 기다림
    const saveResult = await saveToDatabase(result); // 두 번째 비동기 기다림
    console.log("저장 성공!", saveResult);
  } catch (error) {
    console.log("에러 발생!", error);
  }
}
```
---
### Core Syntax - Array Methods
ES6 이후 도입된 주요 Array 메서드 정리.
| 도입 버전 | 메서드명 | 예시 코드 | 핵심 요약 |
| --- | --- | --- | --- |
| ES6 (2015) | `Array.from()` | `Array.from(arguments)` | 유사 배열 객체(Arguments, DOM NodeList)를 순수 배열로 변환하여 배열 내장 고차 함수를 쓸 수 있게 유도 |
| ES6 (2015) | `find()` | `arr.find(item => item.id === 3)` | 조건식을 만족하는 최초의 '아이템 알맹이 자체'를 반환 (없으면 undefined) |
| ES6 (2015) | `findIndex()` | `arr.findIndex(item => item.id === 3)` | 조건식을 만족하는 최초의 '인덱스 숫자'를 반환 (없으면 -1) |
| ES7 (2016) | `includes()` | `arr.includes('수원')` | 배열 내 특정 값이 있는지 여부를 **true / false**만 반환. 구식 indexOf 전면 대체 |
| ES10 (2019) | `flat()` | `[1, [2, 3]].flat()` | 다차원 중첩 배열을 지정한 깊이만큼 1차원 배열로 펴주는 부품 |
| ES13 (2022) | `at()` | `arr.at(-1)` | **음수 인덱스(-1)** 를 지원하여 맨 뒤의 요소를 쉽게 역추적하는 메서드 |
| ES14 (2023) | `toReversed()` `toSorted()` `toSpliced()` | `const newArr = arr.toSorted()` | **\[최신 실무 표준\]** 원본을 변형(Mutate)시키던 구형 메서드들과 달리, **원본을 안전하게 보존하면서 정렬/반전된 '새로운 복사본 배열'을 리턴**하는 불변성 메서드 세트 |
---
### Core Syntax - Object
ES6 이후 도입된 주요 Object 기능 명세.
| 도입 버전 | 기능 | 예시 | 핵심 요약 |
| --- | --- | --- | --- |
| ES6 (2015) | 단축 속성명 (Property Shorthand) | `const user = { name, age }` | key 이름과 대입할 변수명이 같다면, `name: name`처럼 중복 작성 없이 이름만 한 번 적어도 자동으로 매핑 |
| ES6 (2015) | 계산된 속성명 (Computed Property) | `const obj = { [keyName]: value }` | 객체의 key 자리에 고정된 문자열이 아닌, **대괄호****`[]`****를 써서 변수나 연산식의 결과를 실시간 key 명으로 박아넣는** 기술 |
| ES6 (2015) | 메서드 축약 표현 (Method Shorthand) | `const obj = { greet() {} }` | 객체 내부에서 함수를 정의할 때 `function` 키워드를 완전히 생략하고 **함수명() \{\}** 형태로 선언 |
| ES6 (2015) | `Object.assign()` | `Object.assign(target, src)` | 여러 객체의 속성들을 하나의 대상 객체로 병합하거나 복사할 때 쓰던 메서드. 현재는 스프레드 연산자에 밀려 빈도 감소 |
| ES8 (2017) | `Object.keys()` `Object.values()` `Object.entries()` | `Object.entries(user)` | 객체의 \*\*\[key 배열\], \[value 배열\], \[\[key, value\] 쌍의 2차원 배열\]\*\*을 각각 추출하여 배열로 변환 |
| ES11 (2020) | Optional Chaining (`?.`) | `user?.profile?.address` | **\[실무 빈도 극상\]** 깊숙한 객체를 참조할 때 중간에 데이터가 비어 있어도(null/undefined) 에러로 뻗지 않고, 안전하게 **undefined를 뱉으며 프로그램을 보호**하는 문법 |
#### Object Example
```javascript
// Property Shorthand & Method Shorthand
const title = 'Vue 3 특강';
const price = 99000;

// 구식 방식 (ES5)
const courseOld = { title: title, price: price, getInfo: function() { return 'ES5 스타일'; } };

// 모던 방식 (ES6+)
const courseModern = { title, price, getInfo() { return 'ES6 스타일'; } };
```
```javascript
// Computed Property Name (동적인 Key 입력이 필요할 때)
const inputType = 'email';
const userForm = {
  name: '홍길동',
  [inputType]: 'hong@email.com' // 변수 inputType의 값인 'email'이 실시간으로 key 이름에 이식됨
};
console.log(userForm.email); // 'hong@email.com' 출력
```
```javascript
// Object.entries(): 객체를 [[key, value] 쌍의 2차원 배열]로 전환
const scoreBoard = { math: 90, english: 80, science: 100 };

// 객체를 [['math', 90], ['english', 80], ['science', 100]] 이라는 2차원 배열로 쪼개줌
const entries = Object.entries(scoreBoard);

// 배열이 되었으니 모던 배열 메서드로 자유롭게 순회 및 비구조화 할당 가능!
entries.forEach(([subject, score]) => {
  console.log(`과목:${subject}, 점수:${score}`);
});
```
```javascript
// Optional Chaining (?.)
// .왼쪽에 있는 대상이 null이거나 undefined이면, 다음 하위 속성으로 진입하지 않고 에러 없이 undefined를 반환

const user1 = { name: 'Graves', profile: { address: { city: 'Suwon' } } }; // 모든 정보 완벽
const user2 = { name: '홍길동' }; // profile 속성이 물리적으로 존재하지 않는 상태 (undefined)

const cityModern1 = user1?.profile?.address?.city;
const cityModern2 = user2?.profile?.address?.city;

console.log(cityModern1); // 출력: 'Suwon'
console.log(cityModern2); // 출력: undefined (에러 없이 안전하게 통과!)

// 옵셔널 체이닝(?.) 뒤에 Null 병합 연산자(??)를 붙여 안전장치 이중 락을 걸 수 있음
const finalCity = user2?.profile?.address?.city ?? '등록된 주소 없음';
console.log(finalCity); // 출력: '등록된 주소 없음' (유저 친화적 UI 구현 완벽 가능)
```
---
### Core Syntax - Nullish Coalescing Operator (`??`)
ES11(ECMAScript 2020)에서 도입된 **Null 병합 연산자**임. 좌항의 피연산자가 `null`이거나 `undefined`일 때만 우항의 기본값을 반환하고, 그 외의 값이면 좌항의 값을 그대로 유지하는 연산자임.
기존의 `||`(논리합) 연산자는 null/undefined뿐만 아니라 자바스크립트가 false로 취급하는 모든 Falsy 값(`0`, `""`, `false`)까지 전부 카운트하여 우항의 기본값으로 덮어버리는 버그를 유발했음.
```javascript
const userSetting = {
  alertCount: 0,
  nickname: "" // 닉네임을 아직 입력 안 해서 빈 문자열인 상황
};

// 구식 OR (||) 방식의 버그
const countOld = userSetting.alertCount || 10;
const nameOld = userSetting.nickname || '익명';
console.log(countOld); // 출력: 10 (버그: 유저는 분명 0회 알림을 원했는데 10회로 조작됨)
console.log(nameOld);  // 출력: '익명' (버그: 유저가 닉네임을 공백으로 비워두고 싶었어도 강제 변환됨)

// 모던 Nullish (??) 방식
// 오직 null이나 undefined일 때만 우항으로 넘어간다. 숫자 0이나 빈 문자열은 '데이터'로 인정한다.
const countModern = userSetting.alertCount ?? 10;
const nameModern = userSetting.nickname ?? '익명';
console.log(countModern); // 출력: 0  (안전 보존: 유저가 의도한 0이 정확히 살아남음)
console.log(nameModern);  // 출력: "" (안전 보존: 빈 문자열 데이터 유지)
```
---
### ESLint - Overview
**ESLint**는 ECMAScript 코드에서 발견되는 고유 패턴을 식별하고 보고하는 오픈소스 정적 코드 분석 도구(Static Analysis Tool)임.
- 정적 분석(Static Analysis): 런타임 환경에서 코드를 실제로 실행하지 않고, 소스코드를 파싱하여 추상 구문 트리(Abstract Syntax Tree)라는 구조물로 변환한 뒤, 등록된 규칙(Rules)과 대조하여 문법 오류 및 잠재적 런타임 에러를 사전에 검출하는 기술
#### 정적 분석이 필요한 이유
- Interpreter 언어의 구조적 한계: Java, C# 등 Compile 기반 언어는 빌드 단계에서 구문 오류를 강제 검출하므로 결함 있는 코드가 배포 단계에 진입하는 것이 원천 차단됨. 반면 JavaScript는 인터프리터 언어이므로 구문 오류가 포함된 상태로 배포가 가능하며 해당 라인이 실행되는 시점에 애플리케이션이 Crash를 일으킴.
- 동적 타이핑과 느슨한 문법 규칙의 부작용: JavaScript는 변수의 데이터 타입을 동적으로 결정하고 세미콜론 자동 삽입(ASI) 등을 지원하는 등 문법적 허용 범위가 넓음. 이러한 특성은 개발 초기 속도를 높이지만, 대규모 코드베이스에서는 예측 불가능한 Side Effect와 메모리 누수, 가독성 저하를 유발함.
#### 프로젝트 표준화 및 CI/CD 연동 효과
- 코드 일관성(Consistency) 유지: 개발자 개인의 성향에 따라 파편화되는 소스코드 구조를 하나의 통합된 규칙 세트(Rule Set)로 획기적으로 일관화함.
- 배포 파이프라인 자동 검수: 지속적 통합(CI/CD) 프로세스에 eslint 명령어를 포함시켜, 정적 검사를 통과하지 못한 결함 코드가 상용 서버에 배포(Production Deployment)되는 프로세스를 자동 차단함.
---
### ESLint - 주요 점검 항목
#### Syntax Errors
```javascript
// 개발자의 단순 오타 상황
const myLocation = 'Suwon';
console.log(myLocatoin); // 변수명 오타! ESLint가 없으면 배포되어 사용자가 이 라인을 실행할 때 화면이 죽음.
```
#### Dead Code Elimination (Unused Variables)
```javascript
// 선언만 해두고 안 쓰는 변수, import만 해두고 쓰지 않는 파일들
const secretToken = 'xyz123'; // 보안 위협 및 메모리 낭비
// ESLint는 사용하지 않는 코드(Dead Code)를 적발하여 소스코드를 경량화 상태로 유지함.
```
#### Anti-Pattern Prevention
```javascript
// 런타임 암묵적 타입 변환 버그 유발 구문
if (userAge == 20) { ... }
// [ESLint 검출]: Expected '===' and instead saw '=='.
// 엔진 내부의 예기치 못한 형변환을 차단하고 엄격한 비교(Strict Equality) 강제.
```
---
### ESLint - Installation
Vite 프로젝트 초기 생성 시 Option으로 설치됨. ESLint는 개발할 때만 감시용으로 쓰고, 최종 배포(Production) 코드에는 포함될 필요가 없으므로 \*\*`devDependencies`\*\*에 등록됨.
최초 생성 시 Option으로 미 설치한 경우 수동 설치 명령:
```bash
# Vite 프로젝트 환경에 맞는 eslint 및 Vue 전용 플러그인 설치
npm install -D eslint eslint-plugin-vue
```
---
### ESLint - Configuration
#### eslint.config.js 주요 설정 항목
```javascript
// eslint.config.js
import { defineConfig, globalIgnores } from 'eslint/config'
import globals from 'globals'
import js from '@eslint/js'
import pluginVue from 'eslint-plugin-vue'
import pluginOxlint from 'eslint-plugin-oxlint'
import skipFormatting from 'eslint-config-prettier/flat'

export default defineConfig([
  { // ① 설정이 적용되는 소스코드 파일을 지정
    name: 'app/files-to-lint',
    files: ['**/*.{vue,js,mjs,jsx}'],
  },

  globalIgnores(['**/dist/**', '**/dist-ssr/**', '**/coverage/**']), // ② 검사 제외 대상 폴더

  { // ③ JavaScript 실행 환경의 전역 변수를 등록
    languageOptions: {
      globals: {
        ...globals.browser, // window, document, localStorage 같은 브라우저 객체를 정식 변수로 인정
      },
    },
  },

  js.configs.recommended,
  ...pluginVue.configs['flat/essential'], // ④ 표준 추천 규칙: essential은 필수 문법 에러만 잡음

  ...pluginOxlint.buildFromOxlintConfigFile('.oxlintrc.json'), // ⑤ 기존 ESLint보다 최대 50~100배 빠른 초고속 린터 엔진(Oxlint)을 JavaScript 설정과 동기화

  skipFormatting, // ⑥ 줄바꿈, 따옴표, 들여쓰기 등 시각적 스타일 규칙은 ESLint에서 Off하고 Prettier에 전권 위임
])
```
---
### ESLint - Custom Rules
JavaScript 배열은 하단에 위치할수록 앞서 로드된 기본 규칙을 덮어씀. Custom 규칙은 **`skipFormatting`**** 바로 직전**에 설정함.
```javascript
// eslint.config.js 내 커스텀 규칙 추가 위치
js.configs.recommended,
...pluginVue.configs['flat/essential'],
...pluginOxlint.buildFromOxlintConfigFile('.oxlintrc.json'),

{ // 커스텀 규칙 설정 객체
  name: 'app/custom-rules', // 규칙 묶음의 식별자 이름 (옵션)
  rules: {
    'no-unused-vars': 'warn',              // 선언 후 사용하지 않은 변수는 경고 처리
    'no-console': 'off',                   // 개발 편의를 위해 console.log 허용
    'vue/multi-word-component-names': 'off', // 단일 단어로 된 컴포넌트명 허용
  },
},

skipFormatting,
```
---
### ESLint - 실시간 피드백
소스 코드 내 실시간으로 문법 오류를 점검하며 세 가지 방식으로 피드백을 제공함.
- 빨간색/노란색 물결 밑줄: 코드에 마우스를 올리면 `[no-unused-vars]`처럼 위반한 ESLint 규칙명과 함께 원인 메시지가 Tooltip으로 표시됨.
- 파일 이름 색상 변경: 에러가 있는 파일은 탐색기(Sidebar) 창에서 이름이 빨간색(Error) 또는 노란색(Warning)으로 변경되며 옆에 위반 개수가 표시됨.
- Problems Tab: 에디터 하단에 프로젝트 전체 파일의 ESLint 위반 리스트가 파일명, 라인 번호와 함께 일괄 정렬됨.
---
### ESLint - 일괄 점검
터미널에 `npm run lint`를 통해 프로젝트 소스 일괄 점검을 진행할 수 있음.
```bash
npm run lint
# 결과 예시
# EcmaScript.vue 49:27 error  'fetchUserId' is not defined    no-undef
# EcmaScript.vue 52:28 error  'fetchUserProfile' is not defined  no-undef
# EcmaScript.vue 56:12 warning  'error' is defined but never used  no-unused-vars
# 3 problems (2 errors, 1 warning)
```
---
### Prettier - Overview
ESLint가 문법적 에러(Bug)를 잡는다면, **Prettier는 띄어쓰기, 줄바꿈, 따옴표 종류 등 코드의 시각적 스타일(Formatting)만 전문적으로 교정**함.
여러 명이 협업할 때 들여쓰기 칸 수나 세미콜론 유무 등의 차이가 발생하고, 이는 Git에서 불필요한 코드 충돌(Conflict)을 유발하기도 함. Prettier는 파일 저장 순간 팀이 정한 규칙대로 코드를 강제 정렬함.
---
### Prettier - Installation
Prettier도 devDependencies에만 등록됨. 최초 생성 시 미 설치한 경우:
```bash
npm install -D prettier
```
---
### Prettier - Configuration
프로젝트 루트 디렉토리에 `.prettierrc.json` 파일을 생성하고 가독성 옵션을 주입함.
```json
{
  "$schema": "https://json.schemastore.org/prettierrc",
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 200
}
```
- `"$schema"`: JSON 파일이 준수해야 하는 규격 명세서(JSON Schema)의 위치(URL)을 지정하는 메타데이터
- `"semi": false`: 문장 끝에 세미콜론(`;`)을 붙이지 않도록 규격화함.
- `"singleQuote": true`: 문자열을 감쌀 때 쌍따옴표(`"`) 대신 홑따옴표(`'`)를 강제함.
- `"tabWidth": 2`: 들여쓰기(Tab) 너비를 Vue 3 표준인 2칸 공간으로 고정함.
- `"printWidth": 200`: 한 줄이 200자를 넘어가면 가독성을 위해 자동으로 줄바꿈을 처리함.
---
### Prettier - 일괄수정
터미널에 `npm run format`을 통해 프로젝트 소스 일괄 수정을 진행할 수 있음.
```bash
npm run format
# prettier --write --experimental-cli src/
# 수정된 파일 목록이 출력됨
```
---
### Vite Configuration
#### vite.config.js
Vite 빌드 도구의 컴파일러 동작, 개발 서버 환경, 빌드 및 번들링 파이프라인의 명세를 정의하는 Configuration File임. `defineConfig()`는 객체 형식으로 설정을 작성할 때 사용하는 내장 래퍼 함수임.
#### 주요 속성
- `plugins`: 브라우저가 직접 해석할 수 없는 `.vue` 확장자의 파일을 표준 JavaScript 모듈 객체로 트랜스파일(Transpile)하는 컴파일러 플러그인
- `resolve.alias`: 프로젝트 루트 디렉토리의 `src` 폴더 물리 경로를 `@` 기호로 매핑하여 모듈의 절대 경로 참조 체계를 설정
```javascript
// vite.config.js
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
```
---
### Vite Configuration - Custom 추가
실무 환경에서 빈번하게 추가되는 속성.
- `server`: 로컬 개발 서버의 속성
- `build`: 컴파일 완료된 산출물 사양 제어
```javascript
server: {
  port: 3000,   // 개발 서버의 네트워크 포트를 3000번으로 고정 명세
  open: true,   // 프로세스 기동(npm run dev) 시 기본 웹 브라우저를 자동 실행
},
build: {
  outDir: 'dist', // 최종 정적 리소스(HTML, JS, CSS)가 저장될 출력 디렉토리명 지정
},
```
속성 추가 후 `npm run dev` 실행 시 개발 서버가 지정한 포트(`localhost:3000`)에서 구동됨.
---
### Environment Variables
소스코드 내부에 하드코딩된 동적 설정값들을 운영체제나 빌드 스크립트 레벨의 환경 변수(Environment Variables)로 이관하여 격리하는 개발 방법임.
- 보안성 확보: API 보안 토큰, 데이터베이스 접속 정보 등 민감 데이터를 소스코드(Git)에 노출하지 않고 안전하게 관리함.
- 환경별 유연성: 소스코드를 수정하지 않고, 빌드 명령어 조합 변경만으로 검증용(Staging) 서버와 실제 상용(Production) 서버의 API 엔드포인트를 스위칭할 수 있음.
#### 작성 규칙
- Vite는 루트 디렉토리에 존재하는 `.env` 파일들을 자동 로드함.
- Vite 엔진은 오직 **`VITE_`****로 시작하는 환경 변수만** 프론트엔드 클라이언트 코드 내부로 노출시킴.
```bash
# .env.staging
VITE_API_URL=https://api-staging.skala.co.kr
VITE_APP_MODE=Staging Mode

# .env.production
VITE_API_URL=https://api.skala.co.kr
VITE_APP_MODE=Production Mode
```
#### 활용 Example
```javascript
<script setup>
// Vite 환경 변수 참조 (런타임 시 빌드 모드에 따라 값이 동적으로 주입됨)
const currentApiUrl = import.meta.env.VITE_API_URL
const currentMode = import.meta.env.VITE_APP_MODE

console.log('현재 주입된 API 서버 주소:', currentApiUrl)
</script>
```
#### 빌드 명령어 구성
빌드 명령어 뒤에 `--mode` 옵션을 명시하여 필요한 환경 변수를 사용하여 빌드함.
```json
"scripts": {
  "dev": "vite",
  "build:staging": "vite build --mode staging",
  "build:production": "vite build --mode production"
}
```
---
### Bundling and Build
#### Bundling
웹 애플리케이션을 구성하는 수십, 수백 개의 파일(Vue, JS, CSS, Image 등) 간의 의존성 흐름을 정적으로 분석하여, 브라우저가 로드하기 최적화된 **최소한의 파일 개수군으로 묶고 압축하는 과정**임.
Vite는 개발단계에서는 ES Modules(ESM) 기반의 초고속 런타임 방식을 취하지만, 최종 프로덕션 빌드 단계에서는 **Rollup 번들러 엔진**을 기동하여 최적화된 정적 자산을 생성함.
```bash
npm run build
# 1664 modules transformed.
# dist/index.html, dist/assets/*.js, dist/assets/*.css 등 생성됨
```
#### dist 폴더
빌드가 완료되면 프로젝트 루트 디렉토리에 **`dist/`****(Distribution)** 라는 배포 전용 폴더가 생성됨.
- dist 폴더 내부에는 더 이상 `.vue` 파일이나 개발용 모듈이 존재하지 않고 오직 웹 브라우저가 해석할 수 있는 **순수 html, js, css 파일만** 남음.
- 해시(Hash) 이름 식별자: 파일명 뒤에 동적으로 붙는 고유 문자열은 파일의 Hash 값임. 파일 내용이 수정되면 이 해시값이 바뀜. 이는 브라우저가 과거의 구형 코드를 캐싱(Caching)하여 화면 갱신이 안 되는 버그를 방지하기 위한 웹 배포 표준 사양임.
- 이 완제품 dist 폴더 자체를 AWS S3, Nginx, Netlify, Vercel 등 정적 웹 호스팅 서버에 그대로 Upload하면, **웹 서비스 배포 파이프라인이 최종 완결**됨.
---
<empty-block/>
