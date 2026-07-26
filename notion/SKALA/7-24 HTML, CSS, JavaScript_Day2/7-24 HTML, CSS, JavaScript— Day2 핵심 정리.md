---
title: "[7/24] HTML, CSS, JavaScript— Day2 핵심 정리"
notion_page_id: "3a71d84b-f68e-80b1-b034-fddb65ed734b"
source_url: https://app.notion.com/p/3a71d84bf68e80b1b034fddb65ed734b
synced_at: "2026-07-25T15:07:18.532549+00:00"
content_sha256: "9cc32876abc4cf12ddaaef90b329fad03bd1334d09127fa75985bbd0ad29110a"
---

# [7/24] HTML, CSS, JavaScript— Day2 핵심 정리

> 원본: [[7/24] HTML, CSS, JavaScript— Day2 핵심 정리](https://app.notion.com/p/3a71d84bf68e80b1b034fddb65ed734b)

[[notion/SKALA/index|SKALA 학습 노트]]

## CSS Layout 구성 방식
웹 페이지에서 요소를 배치하는 방법은 시대에 따라 발전해 왔으며, 현재는 **Flexbox와 Grid가 표준적인 선택지**임. 이전 방식(float, inline-block)은 원래 레이아웃 전용 기능이 아니었기에 부작용이 따름.
#### 4가지 방식 비교
| 방식 | 설명 | 장점 | 단점 | 사용 시기 |
| --- | --- | --- | --- | --- |
| **float** | `float: left/right`로 요소를 띄워 배치 | 간단한 구조에 적합 | 요소 겹침 발생 | 구버전 브라우저 호환 목적 |
| **inline-block** | `display: inline-block`으로 요소를 나란히 배치 | float보다 자연스럽고 텍스트 흐름에 따라 배치 | **여백(space) 문제** 발생 | 간단한 레이아웃 |
| **Flexbox** | **1차원(가로 또는 세로)** 정렬에 특화된 현대적 방식 | 정렬·중앙정렬·비율 지정에 강력 | 2차원 배치에 제한 | 공간 **내부 요소** 정렬 |
| **Grid** | **2차원(행과 열)** 레이아웃을 구성하는 최신 방식 | 복잡한 레이아웃도 간결하게 구성 | 1차원 구성은 오히려 복잡 | **페이지 전체** 레이아웃 |
#### 각 방식의 문제점 이해
- **float의 요소 겹침**: float된 요소는 일반 문서 흐름에서 빠져나오기 때문에, 부모 요소가 자식의 높이를 인식하지 못해 레이아웃이 무너짐. 이를 막으려면 `clear` 처리나 clearfix 기법이 별도로 필요함.
- **inline-block의 여백 문제**: HTML 소스상의 **줄바꿈·공백이 실제 렌더링에서 공백 문자로 해석**되어 요소 사이에 의도치 않은 4px 내외의 간격이 생김. 태그를 붙여 쓰거나 부모의 `font-size: 0` 같은 우회책이 필요함.
- **Flexbox의 1차원 한계**: 주축(main axis) 하나를 기준으로만 정렬하므로, 행과 열을 동시에 맞춰야 하는 격자형 배치에는 부적합함.
#### 실무 조합 전략
**일반적으로 Flexbox와 Grid를 함께 사용함.**
- **페이지 전체 골격(헤더/사이드바/본문/푸터)** → **Grid**로 2차원 영역 분할
- **각 영역 내부의 요소 정렬(버튼 나열, 아이콘+텍스트 정렬 등)** → **Flexbox**로 1차원 정렬
즉 둘은 대체 관계가 아니라 **적용 범위가 다른 상호 보완 관계**로 이해해야 함.
---
### float 속성
`float`는 요소를 컨테이너 내부에서 **좌우 한쪽으로 띄워(부유시켜) 배치**하는 속성임. 원래는 이미지 옆에 텍스트를 흐르게 하는 용도로 설계됐으나, Flexbox·Grid 등장 이전에는 전체 레이아웃 구성에 폭넓게 쓰였음.
#### 값의 종류
| 값 | 동작 |
| --- | --- |
| `left` | 요소를 컨테이너의 **왼쪽**으로 띄움 |
| `right` | 요소를 컨테이너의 **오른쪽**으로 띄움 |
| `none` | **기본값**. 부유하지 않고 원래 문서 흐름상의 위치에 그대로 표시됨 |
| `inherit` | 부모 요소의 float 값을 그대로 상속받음 |
#### 예제 코드 해석
```html
<style>
  div  { float: left; padding: 15px; }
  .div1 { background: red; }
  .div2 { background: yellow; }
  .div3 { background: green; }
</style>

<h2>Float Next To Each Other</h2>
<p>In this example, the three divs will float next to each other.</p>
<div class="div1">Div 1</div>
<div class="div2">Div 2</div>
<div class="div3">Div 3</div>
```
- `div`는 원래 **블록 요소**이므로 아무 설정이 없으면 세로로 한 줄씩 쌓임.
- 세 div 모두에 `float: left`를 주면 각 요소가 왼쪽부터 차례로 붙어 **가로로 나란히 배치**됨. 결과 화면에서 빨강(Div 1) → 노랑(Div 2) → 초록(Div 3) 순으로 이어지는 이유임.
- `padding: 15px`는 내부 여백이며, 각 박스의 배경색 영역이 글자보다 넓게 보이는 원인임.
---
### display 기본값과 inline-block
모든 HTML 요소는 종류에 따라 **기본 ****`display`**** 값**을 가지며, 크게 **Block**과 **Inline** 두 가지로 나뉨. 레이아웃을 다루려면 이 기본 성격을 먼저 이해해야 함.
#### Block vs Inline
| 구분 | 배치 | 크기 지정 | 대표 태그 |
| --- | --- | --- | --- |
| **Block** | 혼자서 **한 줄 전체**를 차지 (앞뒤로 줄바꿈) | `width`/`height` 지정 가능 | `<div>`, `<p>`, `<h1>`\~`<h6>`, `<ul>`, `<li>` |
| **Inline** | 줄바꿈 없이 **다른 요소와 같은 줄**에 배치 | `width`/`height` **무시됨** | `<span>`, `<a>`, `<strong>`, `<em>` |
#### inline-block의 성격
`display: inline-block`은 두 성격을 **섞어 놓은 값**임.
- **배치는 Inline처럼** → 다른 요소와 같은 줄에 나란히 놓임
- **성격은 Block처럼** → `width`, `height`, 상하 `padding`/`margin`이 정상 적용됨
즉 "**가로로 나란히 두면서도 크기는 마음대로 조절하고 싶을 때**" 쓰는 값임.
#### 예제 코드 해석
```html
<style>
  .nav    { background-color: lightgray; list-style-type: none; margin: 0; padding: 0; }
  .nav li { display: inline-block; font-size: 18px; padding: 15px; }
</style>

<ul class="nav">
  <li><a href="#home">Home</a></li>
  <li><a href="#about">About Us</a></li>
  <li><a href="#clients">Our Clients</a></li>
  <li><a href="#contact">Contact Us</a></li>
</ul>
```
- `<li>`는 기본이 Block이므로 원래는 목록이 **세로로 쌓임**. 여기에 `display: inline-block`을 주어 **가로 내비게이션 메뉴**로 전환한 것임.
- `list-style-type: none`으로 목록 앞의 불릿 점을 제거하고, `<ul>`의 기본 `margin`/`padding`을 `0`으로 초기화해 브라우저 기본 여백을 없앰.
- `<li>`에 준 `padding: 15px`가 실제로 적용되는 점이 핵심임. 만약 순수 Inline이었다면 좌우 padding만 반영되고 상하 크기는 제대로 잡히지 않음.
- 결과적으로 회색 배경(`lightgray`)의 가로 메뉴바 안에 Home / About Us / Our Clients / Contact Us가 나란히 놓임.
---
### Flexbox (Flexible Box Layout)
기존의 float나 inline-block만으로 전체 레이아웃을 잡으려면 clearfix, 여백 보정 등 부수 처리가 많아 **구조가 복잡해짐**. Flexbox는 **가로 또는 세로 방향 정렬을 효율적으로 구성**하기 위해 도입된 레이아웃 모듈임.
#### 핵심 용어
| 용어 | 설명 |
| --- | --- |
| **Flex Container** | `display: flex`가 적용된 **부모 요소** |
| **Flex Item** | Flex Container의 **직계 자식 요소들** |
| **Main Axis (메인 축)** | Flex Item이 배치되는 중심 방향. **row(가로, 기본값)** 또는 **column(세로)** |
| **Cross Axis (교차 축)** | Main Axis의 **수직 방향** |
여기서 중요한 것은 Flexbox가 **부모–자식 관계 기반**으로 동작한다는 점임. 컨테이너에 `display: flex`를 선언하는 순간 그 **직계 자식들만** Flex Item이 되며, 손자 요소에는 영향이 없음.
#### 기본 선언
```html
<style>
.container {
  display: flex;
  background-color: DodgerBlue;
}
</style>
```
- 부모에 `display: flex` 한 줄만 주면, 원래 세로로 쌓이던 블록 자식들이 **즉시 가로로 나란히 배치**됨.
- 이때 자식에게는 별도 속성을 줄 필요가 없음. float 방식과 달리 **부모 쪽에서 배치를 통제**하는 것이 Flexbox의 특징임.
#### 두 축(Axis) 개념 이해

다이어그램은 컨테이너 안의 Flex-item 1, 2, 3이 놓이는 기준선을 보여줌.
- **Main Axis**: 아이템이 나열되는 방향. 기본값 `row`에서는 **왼쪽(Main-Start) → 오른쪽(Main-End)** 으로 흐름.
- **Cross Axis**: Main Axis와 직교하는 방향. `row`일 때는 **위(Cross-Start) → 아래(Cross-End)** 방향임.
- **Main Size / Cross Size**: 각 축 방향으로 컨테이너가 차지하는 크기를 의미함.
정렬 속성이 이 축 개념과 직결되므로 반드시 짝지어 기억할 것.
- `justify-content` → **Main Axis 방향** 정렬
- `align-items` → **Cross Axis 방향** 정렬
### Flex Container 속성
Flex Container(부모)에 지정할 수 있는 속성들임. **아이템 각각이 아니라 컨테이너 쪽에서 전체 배치를 통제**한다는 점이 Flexbox의 핵심 사고방식임.
#### 속성 정리
| 속성 | 값 | 설명 |
| --- | --- | --- |
| **flex-direction** | `row`(기본), `column`, `row-reverse`, `column-reverse` | 아이템 **배치 방향** 지정 |
| **flex-wrap** | `nowrap`(기본), `wrap`, `wrap-reverse` | 넘치는 아이템의 **줄바꿈 여부** |
| **justify-content** | `flex-start`(기본), `center`, `flex-end`, `space-around`, `space-between`, `space-evenly` | **메인 축** 정렬 방식 |
| **align-items** | `normal`(기본), `stretch`, `center`, `flex-start`, `flex-end`, `baseline` | **교차 축**에서 **한 줄** 정렬 방식 |
| **align-content** | `stretch`(기본), `center`, `flex-start`, `flex-end`, `space-between`, `space-around` 등 | **여러 줄**일 때 교차 축 처리 |
#### align-items vs align-content 구분
두 속성이 가장 헷갈리는 지점이므로 반드시 구분할 것.
- **align-items** → 한 줄 안에서 아이템들이 교차 축 방향 어디에 놓일지 결정
- **align-content** → `flex-wrap: wrap`으로 **줄이 2개 이상 생겼을 때**, 그 **줄 뭉치 전체**를 교차 축에서 어떻게 분배할지 결정
즉 줄이 한 줄뿐이면 `align-content`는 사실상 효과가 없음.
#### flex-wrap 동작 비교

다이어그램은 컨테이너 폭보다 아이템 4개의 원래 크기(original size)가 클 때의 처리 차이를 보여줌.
- **`nowrap`****(기본)**: 줄바꿈하지 않고, 아이템들이 **강제로 축소(shrink)** 되어 한 줄에 다 들어감. 원래 크기가 유지되지 않는 것이 핵심임.
- **`wrap`**: 넘치는 아이템이 **다음 줄로 내려감**. 1·2가 첫 줄, 3·4가 둘째 줄에 배치됨.
- **`wrap-reverse`**: 줄바꿈은 하되 **줄이 쌓이는 방향이 반대**임. 3·4가 위, 1·2가 아래로 배치됨.
#### 예제 코드 해석
```css
.container {
  display: flex;
  height: 200px;
  background-color: #f1f1f1;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
```
- `justify-content: space-between` → 첫 아이템은 맨 왼쪽, 마지막 아이템은 맨 오른쪽에 붙고 **남는 공간이 사이사이에 균등 분배**됨.
- `align-items: center` → 높이 200px 안에서 아이템들이 **세로 중앙**에 정렬됨. 컨테이너에 명시적 `height`가 있어야 세로 정렬 효과가 눈에 보임.
- `flex-wrap: wrap` → 아이템이 넘칠 경우 축소되지 않고 다음 줄로 넘어감.
#### Flex Item 속성
앞의 Flex Container 속성이 **전체 배치**를 통제했다면, 여기서는 **개별 아이템 자신**에게 지정하는 속성들임. 컨테이너 규칙을 따르되 특정 아이템만 다르게 처리하고 싶을 때 사용함.
#### 속성 정리
| 속성 | 기본값 | 설명 |
| --- | --- | --- |
| **order** | `0` | **HTML 코드 순서와 무관하게** 시각적 배치 순서를 지정 |
| **flex-grow** | `0` | 부모 안에 **남는 공간이 있을 때**, 자식들이 그 공간을 얼마나 나눠 가질지(비율) 결정 |
| **flex-shrink** | `1` | 부모가 자식들 총합보다 **작아질 때**, 얼마나 줄어들지 결정 |
| **flex-basis** | `auto` | 자식 요소의 **기본 크기** 설정. `width`와 유사하나 flex 환경에 최적화됨 |
| **flex** | — | `flex-grow`, `flex-shrink`, `flex-basis`를 **한 번에 쓰는 축약형** |
| **align-self** | — | 컨테이너의 `align-items` 규칙을 **무시하고 이 아이템만** 다르게 정렬 |
#### 기본값이 의미하는 동작
기본값을 알아야 왜 그렇게 렌더링되는지 설명할 수 있음.
- **`flex-grow: 0`****이 기본** → 아무 설정도 하지 않으면 아이템은 **남는 공간이 있어도 커지지 않음**. 컨테이너 오른쪽이 비어 보이는 이유임.
- **`flex-shrink: 1`****이 기본** → 반면 공간이 부족하면 **자동으로 줄어듦**. 앞서 `flex-wrap: nowrap`에서 아이템이 강제 축소되던 것이 이 기본값 때문임.
즉 Flexbox는 기본적으로 **"늘어나지는 않지만 줄어들기는 한다"** 는 성질을 가짐.
#### 예제 코드 해석
```css
.item {
  flex-grow: 1;        /* 남은 공간 비율로 커짐 */
  flex-shrink: 1;      /* 줄어드는 비율 */
  flex-basis: 100px;   /* 기본 크기 */
  flex: 1 1 100px;     /* 위 3개의 축약형 */
  align-self: center;  /* 개별 정렬 */
  order: 2;            /* 순서 변경 */
}
```
---
### Grid (CSS Grid Layout)
Flexbox가 **1차원 레이아웃**이라면, Grid는 **행(row)과 열(column)을 동시에 다루는 2차원 레이아웃**임.
- 페이지 **전체 구조**(헤더/사이드바/본문/푸터) 설계에 적합
- 갤러리, 대시보드처럼 **격자 기반 UI**에 적합
#### 핵심 용어
| 용어 | 설명 |
| --- | --- |
| **Grid Container** | `display: grid`가 선언된 **부모 요소** |
| **Grid Item** | Grid Container의 **직계 자식 요소** |
| **Grid Line** | 행과 열을 **나누는 선** |
| **Grid Track** | 두 선 사이의 공간, 즉 **행(row) 또는 열(column)** 하나 |
| **Grid Cell** | 하나의 셀. **row와 column이 만나는 최소 단위 공간** |
| **Grid Area** | **여러 셀을 묶은 영역** |
용어 간 위계는 **Line → Track → Cell → Area** 순으로 이해하면 됨. 선이 트랙을 만들고, 트랙이 교차해 셀이 되며, 셀을 묶으면 영역이 됨. 특히 **Grid Line은 번호로 지정**되며, 아이템 배치 시 `grid-column: 1 / 3` 같은 방식으로 **선 번호를 기준**으로 위치를 잡는다는 점이 중요함.
#### 예시 레이아웃 해석
우측 그림은 전형적인 **Holy Grail 레이아웃**을 Grid로 구성한 예시임.
- **My Header** → 상단에서 **가로 전체를 차지**함. 여러 열에 걸쳐 있으므로 하나의 **Grid Area**로 묶인 상태임.
- **Link 1\~3(사이드바) + Lorem Ipsum(본문)** → 가운데 행에서 **좌우 2개 열**로 분리됨. 각각 별도의 Grid Cell임.
- **Footer** → 하단에서 다시 가로 전체를 차지함.
이처럼 **"어떤 요소가 몇 번째 행·열에 놓이고, 몇 칸을 차지하는가"를 부모에서 한 번에 설계**할 수 있는 것이 Grid의 강점임. 동일한 구조를 float로 만들면 clear 처리와 폭 계산이 필요하고, Flexbox로 만들면 행마다 컨테이너를 중첩해야 함.
#### Grid Container 속성
Grid Container(부모)에 지정하는 속성들임. **격자 자체의 뼈대(행·열·간격)를 부모에서 한 번에 설계**하는 것이 핵심임.
#### 속성 정리
| 구분 | 속성 | 예시 값 | 설명 |
| --- | --- | --- | --- |
| **Grid Tracks** | `grid-template-columns` | `200px 1fr 2fr` | **열의 개수와 너비** 정의 |
|  | `grid-template-rows` | `100px auto` | **행의 개수와 높이** 정의 |
| **Grid Gaps** | `gap`, `row-gap`, `column-gap` | `10px` | 행과 열 **사이 간격** 설정 |
| **Grid Align** | `justify-items` | `start`, `end`, `center`, `stretch` | 각 셀 내부 요소의 **수평 정렬** |
|  | `align-items` | `start`, `end`, `center`, `stretch` | 각 셀 내부 요소의 **수직 정렬** |
#### fr 단위
**fr(Fraction)** 은 Grid 전용 단위로, Grid Container에 **남은 유연한 공간을 비율로 나눠 갖는** 상대 단위임.
- `grid-template-columns: 200px 1fr 2fr` → 첫 열은 **200px 고정**, 나머지 공간을 2·3번째 열이 **1:2 비율**로 분할함.
- 고정 단위와 섞어 쓸 수 있다는 점이 실용적임. `px`로 고정할 곳은 고정하고, 나머지를 `fr`로 유연하게 채우는 방식이 일반적임.
- `1fr 1fr 1fr`처럼 반복되면 `repeat(3, 1fr)`로 축약 가능함.
#### 트랙 정의 방식의 사고 전환
`grid-template-columns`에 **나열한 값의 개수가 곧 열의 개수**가 됨. 즉 "몇 개의 열을 만들까"를 따로 선언하는 것이 아니라, **각 열의 크기를 나열하면 개수는 자동으로 결정**되는 구조임. 행도 동일함.

#### 예제 코드 해석
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr;   /* 열 정의 */
  grid-template-rows: auto 100px;   /* 행 정의 */
  gap: 10px;                        /* 셀 사이 간격 */
  justify-items: center;            /* 셀 내부 가로 정렬 */
  align-items: center;              /* 셀 내부 세로 정렬 */
}
```
- 열은 2개이며 폭이 **1:2**로 나뉨. 행은 2개로, 첫 행은 **내용 높이만큼(****`auto`****)**, 둘째 행은 **100px 고정**임.
- `gap: 10px`은 셀 사이에만 간격을 주며, **컨테이너 바깥 테두리에는 적용되지 않음**. 좌우 여백이 필요하면 `padding`을 별도로 줘야 함.
- `justify-items` / `align-items`는 **트랙 자체가 아니라 셀 안에 놓인 콘텐츠**의 정렬을 다룸. 이 둘을 `center`로 두면 각 셀의 내용물이 정중앙에 놓임.
#### Grid Item 속성
Grid Container가 격자의 뼈대를 만들었다면, Grid Item 속성은 **개별 아이템이 그 격자의 어느 구역을 차지할지** 지정하는 역할임.
#### 지정 방식 3가지
| 목적 | 속성 |
| --- | --- |
| **그리드 라인 번호**로 위치 지정 | `grid-column-start`, `grid-column-end`, `grid-column`, `grid-row-start`, `grid-row-end`, `grid-row` |
| Container가 **지정한 이름**에 배치 | `grid-area` |
| Container 정렬 규칙을 무시하고 **개별 정렬** | `justify-self`, `align-self` |
#### 핵심: 셀이 아니라 "선" 번호 기준
Grid는 **칸(셀)의 개수가 아니라, 칸을 나누는 선(Grid Line)의 번호를 기준으로 구역을 잡음.**
- 열이 2개면 선은 **3개**(왼쪽 끝 1번, 가운데 2번, 오른쪽 끝 3번)임. 즉 **선의 개수 = 트랙 개수 + 1**임.
- `grid-column: 1 / 3`은 "1번 열부터 3번 열까지"가 아니라 **"1번 선에서 시작해 3번 선에서 끝난다"** 는 뜻임. 결과적으로 **2칸을 차지**함.
- 이 오해가 Grid 학습에서 가장 흔한 실수이므로, **"칸을 세지 말고 선을 세라"** 로 기억할 것.
#### 예제 코드 해석
```css
.item {
  grid-column: 1 / 3;    /* 1번 선부터 3번 선까지 열 병합 */
  grid-row: 2 / 4;       /* 2번 선부터 4번 선까지 행 병합 */
  justify-self: center;  /* 개별 요소 수평 정렬 */
  align-self: end;       /* 개별 요소 수직 정렬 */
}
```
- `grid-column: 1 / 3` → **가로로 2칸**을 차지함. `grid-column-start: 1; grid-column-end: 3;`의 축약형임.
- `grid-row: 2 / 4` → **세로로 2칸**을 차지함. 두 속성을 함께 쓰면 **2×2 크기의 Grid Area**가 됨.
- `justify-self` / `align-self` → 컨테이너의 `justify-items` / `align-items` 규칙을 **이 아이템에서만 덮어씀**. Flexbox의 `align-self`와 같은 역할이지만, Grid에서는 **수평·수직 두 방향 모두 개별 지정**이 가능함.
#### 속성 이름 대응 정리
| 적용 대상 | 수평 | 수직 |
| --- | --- | --- |
| Container(전체) | `justify-items` | `align-items` |
| Item(개별) | `justify-self` | `align-self` |
- **`items`****는 부모가 전체에게, ****`self`****는 자식이 자기 자신에게** 적용한다는 규칙으로 외우면 혼동이 줄어듦.
---
## CSS Transform
`transform` 속성은 요소에 **2D 또는 3D 변형(transformation)** 을 적용하는 속성임. 요소를 **회전, 크기 조정, 이동, 기울이기** 하는 데 사용함.
여기서 쓰이는 `rotate()`, `scale()` 등을 **Transform Functions(변형 함수)** 라고 부름. 즉 `transform`은 속성 이름이고, 실제 동작은 값으로 넘기는 함수가 결정하는 구조임.
#### 2D Transform 함수
| 함수 | 동작 | 단위 |
| --- | --- | --- |
| `rotate()` | 요소를 **회전** | `deg`(각도) |
| `scale()` | 요소의 **크기 조정** | 배율(숫자) |
| `translateX()` / `translateY()` | X축 / Y축 방향으로 **이동** | `px`, `%` 등 |
| `skew()` | 요소를 **기울임** | `deg`(각도) |
```css
transform: rotate(45deg);     /* 45도 회전 */
transform: scale(1.2);        /* 크기 1.2배 */
transform: translateX(50px);  /* X축으로 50px 이동 */
```
- `rotate(45deg)` → 시계 방향 45도 회전. 음수 값이면 반시계 방향임.
- `scale(1.2)` → 원래 크기의 1.2배. `1`보다 작으면 축소임.
- `translateX(50px)` → 오른쪽으로 50px 이동. `translateY()`는 아래쪽이 양의 방향임.
#### 3D Transform
`rotateX()`, `rotateY()`, `rotateZ()` 함수를 통해 **X축, Y축, Z축을 기준으로** 요소를 회전시킬 수 있음. 화면은 평면이지만, 원근감을 부여하면 입체적으로 회전하는 것처럼 보임.
| 속성 | 설명 |
| --- | --- |
| **transform** | 요소에 2D 또는 3D 변형을 적용 |
| **transform-origin** | 변형이 일어나는 **기준점 위치**를 변경 |
| **transform-style** | **중첩된 자식 요소**를 3D 공간에서 렌더링할지 지정 |
| **perspective** | 3D 요소를 바라보는 **원근감(시점 거리)** 지정 |
| **perspective-origin** | 3D 요소를 바라보는 **시점의 위치** 지정 |
| **backface-visibility** | 요소의 **뒷면이 화면을 향할 때** 보이게 할지 여부 |
- **`perspective`****가 핵심임.** 이 값이 없으면 `rotateY(45deg)`를 줘도 입체감 없이 단순히 납작하게 눌린 것처럼 보임. 값이 **작을수록 원근이 과장**되고, 클수록 평면에 가까워짐.
- `transform-origin`의 기본값은 요소의 **중앙(****`50% 50%`****)** 임. `top left` 등으로 바꾸면 회전축 자체가 이동함.
- `backface-visibility: hidden`은 **카드 뒤집기 UI**를 만들 때 필수임. 앞면과 뒷면 요소를 겹쳐 두고 뒷면이 비치지 않게 처리함.
#### transform 사용 시 유의점
- **`transform`****은 하나의 속성이므로, 여러 줄로 나눠 쓰면 마지막 선언만 적용됨.** 동시에 적용하려면 **공백으로 이어 붙여** 한 줄에 써야 함.
```css
transform: rotate(45deg) scale(1.2) translateX(50px);
```
- 여러 함수는 **왼쪽부터 순서대로 적용**되며, 순서가 바뀌면 결과도 달라짐.
- `transform`으로 인한 변형은 **주변 요소의 레이아웃에 영향을 주지 않음.** 원래 차지하던 공간은 그대로 유지되므로 다른 요소와 겹칠 수 있음.
---
#### CSS Transition
`transform` 속성은 요소에 **2D 또는 3D 변형(transformation)** 을 적용하는 속성임. 요소를 **회전, 크기 조정, 이동, 기울이기** 하는 데 사용함.
여기서 쓰이는 `rotate()`, `scale()` 등을 **Transform Functions(변형 함수)** 라고 부름. 즉 `transform`은 속성 이름이고, 실제 동작은 값으로 넘기는 함수가 결정하는 구조임.
#### 2D Transform 함수
| 함수 | 동작 | 단위 |
| --- | --- | --- |
| `rotate()` | 요소를 **회전** | `deg`(각도) |
| `scale()` | 요소의 **크기 조정** | 배율(숫자) |
| `translateX()` / `translateY()` | X축 / Y축 방향으로 **이동** | `px`, `%` 등 |
| `skew()` | 요소를 **기울임** | `deg`(각도) |
```css
transform: rotate(45deg);     /* 45도 회전 */
transform: scale(1.2);        /* 크기 1.2배 */
transform: translateX(50px);  /* X축으로 50px 이동 */
```
- `rotate(45deg)` → 시계 방향 45도 회전. 음수 값이면 반시계 방향임.
- `scale(1.2)` → 원래 크기의 1.2배. `1`보다 작으면 축소임.
- `translateX(50px)` → 오른쪽으로 50px 이동. `translateY()`는 아래쪽이 양의 방향임.
#### 3D Transform
`rotateX()`, `rotateY()`, `rotateZ()` 함수를 통해 **X축, Y축, Z축을 기준으로** 요소를 회전시킬 수 있음. 화면은 평면이지만, 원근감을 부여하면 입체적으로 회전하는 것처럼 보임.
| 속성 | 설명 |
| --- | --- |
| **transform** | 요소에 2D 또는 3D 변형을 적용 |
| **transform-origin** | 변형이 일어나는 **기준점 위치**를 변경 |
| **transform-style** | **중첩된 자식 요소**를 3D 공간에서 렌더링할지 지정 |
| **perspective** | 3D 요소를 바라보는 **원근감(시점 거리)** 지정 |
| **perspective-origin** | 3D 요소를 바라보는 **시점의 위치** 지정 |
| **backface-visibility** | 요소의 **뒷면이 화면을 향할 때** 보이게 할지 여부 |
- **`perspective`****가 핵심임.** 이 값이 없으면 `rotateY(45deg)`를 줘도 입체감 없이 단순히 납작하게 눌린 것처럼 보임. 값이 **작을수록 원근이 과장**되고, 클수록 평면에 가까워짐.
- `transform-origin`의 기본값은 요소의 **중앙(****`50% 50%`****)** 임. `top left` 등으로 바꾸면 회전축 자체가 이동함.
- `backface-visibility: hidden`은 **카드 뒤집기 UI**를 만들 때 필수임. 앞면과 뒷면 요소를 겹쳐 두고 뒷면이 비치지 않게 처리함.
#### transform 사용 시 유의점
- **`transform`****은 하나의 속성이므로, 여러 줄로 나눠 쓰면 마지막 선언만 적용됨.** 동시에 적용하려면 **공백으로 이어 붙여** 한 줄에 써야 함.
```css
transform: rotate(45deg) scale(1.2) translateX(50px);
```
- 여러 함수는 **왼쪽부터 순서대로 적용**되며, 순서가 바뀌면 결과도 달라짐.
- `transform`으로 인한 변형은 **주변 요소의 레이아웃에 영향을 주지 않음.** 원래 차지하던 공간은 그대로 유지되므로 다른 요소와 겹칠 수 있음.
---
#### CSS Transition
CSS **속성 값이 변할 때, 그 변화가 진행되는 효과(전환)** 를 설정하는 속성임. 값이 즉시 바뀌는 대신 지정한 시간에 걸쳐 **부드럽게 보간(interpolation)** 됨.
#### 예제 코드 해석
```css
div {
  width: 100px;
  height: 100px;
  background-color: red;
  transition: width 2s, height 4s, background-color 3s;
}
div:hover {
  width: 300px;
  height: 300px;
  background-color: orange;
}
```
- `div:hover` 상태가 되면 크기와 배경색이 바뀌는데, `transition` 덕분에 **각각 다른 속도로** 변화함.
- 쉼표로 구분해 **속성별로 개별 시간 지정**이 가능함. width는 2초, height는 4초, 배경색은 3초에 걸쳐 변함. 결과적으로 가로가 먼저 늘어나고 세로가 뒤늦게 따라오는 연출이 됨.
- **`transition`****은 변화 전 상태(기본 상태)에 선언해야 함.** `:hover` 쪽에 쓰면 마우스를 올릴 때만 효과가 적용되고, 뗄 때는 즉시 원복되어 어색해짐.
---
#### CSS Transition Timing
전환 효과를 세부 제어하는 속성들임. 앞의 `transition`은 아래 4개를 묶은 축약형임.
| 속성 | 설명 |
| --- | --- |
| **transition-property** | transition 효과를 부여할 **CSS 속성** 지정 |
| **transition-duration** | 효과가 **진행되는 시간** 지정 |
| **transition-timing-function** | 효과가 진행되는 **속도의 형태** 지정 |
| **transition-delay** | transition이 **시작되기 전 지연 시간** 지정 |
#### 개별 선언과 축약형
```css
div {
  transition-property: width;
  transition-duration: 2s;
  transition-timing-function: linear;
  transition-delay: 1s;
}
```
위 4줄은 아래 한 줄과 완전히 동일함.
```css
div {
  transition: width 2s linear 1s;
}
```
**축약형의 값 순서는 ****`property duration timing-function delay`** 임. 특히 시간 값이 두 개(`2s`, `1s`) 나올 때, **먼저 나온 것이 duration, 나중이 delay**라는 규칙을 기억할 것.
#### timing-function 값
속도의 "형태"란 시간 대비 진행률의 곡선을 의미함.
- `linear` → 처음부터 끝까지 **일정한 속도**
- `ease`(기본값) → 느리게 시작 → 빨라짐 → 느리게 끝남
- `ease-in` → 느리게 시작
- `ease-out` → 느리게 끝남
- `cubic-bezier(n,n,n,n)` → 곡선을 **직접 정의**
---
### CSS Animations
Transition과 Animation의 차이가 핵심임.
- **CSS Transition** → element의 **전후(시작과 종료) 두 상태**만 부드럽게 연결함. 상태 변화를 유발하는 트리거(`:hover` 등)가 필요함.
- **CSS Animation** → 시작과 종료뿐 아니라 **중간 상태까지 고려**하여 더 복잡하고 다양한 효과를 제공함. 트리거 없이 **자동 재생·반복**도 가능함.
#### animation 속성 목록
| 속성 | 의미 | 기본값 |
| --- | --- | --- |
| **animation-name** | **@keyframes의 이름** | `none` |
| **animation-duration** | **지속 시간** | `0s` |
| **animation-delay** | 대기 시간 | `0s` |
| **animation-timing-function** | 타이밍 함수 | `ease` |
| **animation-iteration-count** | 반복 횟수 | `1` |
| **animation-direction** | 반복 방향 | `normal` |
| **animation-fill-mode** | 전후 상태 | `none` |
| **animation-play-state** | 재생과 정지 | `running` |
앞의 4개는 transition과 이름·역할이 거의 동일하며, 뒤의 4개가 **Animation에만 있는 반복·상태 제어 속성**임.
#### @keyframes로 각 단계 설정
`@keyframes`는 **애니메이션의 각 단계를 설정**하는 규칙임. 여기서 중간 상태를 정의하기 때문에 transition보다 표현력이 높음.
```css
@keyframes slide {
  0%   { transform: translateX(0); }
  50%  { transform: translateX(100px); }
  100% { transform: translateX(0); }
}

div {
  animation-name: slide;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}
```
- 단계는 **`0%`****\~****`100%`**** 백분율**로 지정하며, `from`(0%)과 `to`(100%)로 쓸 수도 있음.
- `animation-name`으로 `@keyframes`의 이름을 연결해야 실행됨. **이름이 일치하지 않으면 아무 일도 일어나지 않음.**
- **`animation-duration`****의 기본값이 ****`0s`** 이므로, 이 값을 지정하지 않으면 애니메이션이 보이지 않음. 동작하지 않을 때 가장 먼저 확인할 지점임.
#### 반복·상태 제어 속성 값
| 속성 | 주요 값 | 동작 |
| --- | --- | --- |
| `animation-iteration-count` | 숫자, `infinite` | `infinite`면 **무한 반복** |
| `animation-direction` | `normal`, `reverse`, `alternate`, `alternate-reverse` | `alternate`는 갈 때와 올 때 **방향을 번갈아** 재생 |
| `animation-fill-mode` | `none`, `forwards`, `backwards`, `both` | `forwards`면 **종료 후 마지막 프레임 상태를 유지** |
| `animation-play-state` | `running`, `paused` | `paused`로 바꾸면 **일시 정지** |
- **`animation-fill-mode: forwards`** 는 실무에서 자주 쓰임. 기본값 `none`에서는 애니메이션이 끝나는 순간 **원래 스타일로 되돌아가 깜빡이는 것처럼 보임**.
- `animation-direction: alternate` + `iteration-count: infinite` 조합은 왕복 운동 연출의 관용구임.
#### 축약형
```css
div {
  animation: slide 2s ease 1s infinite alternate;
}
```
**`name duration timing-function delay iteration-count direction`** 순으로 나열함. transition과 마찬가지로 **시간 값이 두 개일 때 먼저 나온 것이 duration, 나중이 delay**임.
---
### Responsive Web Design (반응형 웹 디자인)
**하나의 HTML 소스로 PC·태블릿·스마트폰 등 다양한 화면 크기에 맞춰 레이아웃이 자동 변형되도록** 하는 개발 방식임.
**핵심 기술 3가지**
- **Viewport ****`<meta>`**** tag** — 기기 화면 크기 인식
- **Media Queries** — 조건별 스타일 분기
- **Flexible Layout (Grid, Flex)** — 유연한 배치
브라우저가 감지하는 화면 정보: **width/height**(뷰포트 크기), **orientation**(portrait/landscape), **resolution**(dpi, dppx), color, aspect-ratio 등.
---
#### Viewport 메타 태그
반응형이 작동하려면 `<head>`에 **반드시** 넣어야 함.
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
- **`width=device-width`** — 기기의 실제 화면 너비에 맞춰 콘텐츠 폭 설정
- **`initial-scale=1.0`** — 초기 확대/축소 비율을 1(100%)로 설정
이 태그가 없으면 모바일 브라우저가 화면 폭을 데스크톱 기준(약 980px)으로 가정해 **페이지 전체가 축소되어 표시됨.** 미디어 쿼리를 아무리 잘 짜도 무용지물이므로 반응형의 첫 단추임.
---
#### Media Query
화면 크기·방향·해상도 등에 따라 **다른 스타일을 적용**하는 기술임. 레이아웃이 바뀌는 기준점을 **브레이크포인트(Breakpoint)** 라고 함.
```css
@media (max-width: 767px) { }                              /* 모바일 */
@media (min-width: 768px) and (max-width: 1023px) { }      /* 태블릿 */
@media (min-width: 1024px) and (max-width: 1439px) { }     /* 노트북/PC */
@media (min-width: 1440px) { }                             /* 대화면 데스크톱 */
```
- **`min-width`****는 "이상", ****`max-width`****는 "이하"** 이며, `and`로 묶어 구간 지정함.
- `767px` / `768px`처럼 **1px 차이로 경계를 두는 이유**는 조건이 겹쳐 두 블록이 동시 적용되는 것을 막기 위함임.
---
#### Grid View
많은 웹 페이지가 그리드 뷰 기반이며, 반응형 그리드는 보통 **6열 또는 12열**로 구성됨.
12열이 표준처럼 쓰이는 이유는 **2·3·4·6으로 나누어떨어져** 1/2, 1/3, 1/4 등 다양한 분할을 정수 열로 표현할 수 있기 때문임.
---
#### Mobile First
| 방식 | 작업 순서 | 사용 쿼리 |
| --- | --- | --- |
| **Mobile First** | 모바일부터 만들고 **커질 때 살을 붙임** | `min-width` |
| **Desktop First** | PC부터 만들고 **작아질 때 덜어냄** | `max-width` |
모바일 우선 사용 흐름에 맞춰 **Mobile First가 권장됨.**
| 항목 | 설명 |
| --- | --- |
| 설계 순서 | 모바일 → 태블릿 → 데스크탑 |
| 장점 | **핵심 기능에 집중**, 로딩 속도 최적화, 반응형 구현에 유리 |
| 기술적 구현 | **`min-width`**** 기반** 미디어 쿼리 |
좁은 화면부터 설계하면 꼭 필요한 요소만 남게 되어 **정보 우선순위가 자연스럽게 정리됨.** 반대로 Desktop First는 작은 화면에서 억지로 덜어내야 해 예외 처리가 늘어남.
---
### CSS Preprocessor — SCSS 장점
| 기능 | 설명 |
| --- | --- |
| **변수 (****`$variable`****)** | 색상, 폰트 크기 등을 변수로 지정해 재사용 (예: `$primary-color: #ff0000;`) |
| **중첩 (Nesting)** | 상위 선택자 반복을 줄여 **컴포넌트 단위 관리**가 편해짐 |
| **믹스인 (Mixins)** | 자주 쓰는 CSS 코드 블록을 정의해 두고 호출 (**함수와 유사**) |
| **모듈화 (Import)** | 스타일시트를 여러 파일로 쪼개 관리하고 하나로 합침 → **대규모 프로젝트에 필수적** |
```scss
$primary-color: #ff0000;

@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  color: $primary-color;
  @include flex-center;   // 믹스인 호출
}
```
- SCSS 변수는 **`$`**, CSS 변수는 **`-`** 로 구분됨. SCSS 변수는 컴파일 시점에 값이 확정되어 사라지고, CSS 변수는 **런타임에 남아 JS로 변경 가능**하다는 점이 결정적 차이임.
- 믹스인은 `@mixin`으로 정의하고 `@include`로 불러옴.
#### 트랜스파일링 (Transpiling)
SCSS/SASS 코드는 **브라우저가 직접 읽을 수 없으므로, 일반 CSS로 바꾸어주는 과정**이 필요함. 이 과정을 **트랜스파일링(Transpiling)** 이라고 함.
- **Vite, Webpack, Turbopack** 같은 Frontend Build 도구가 설정을 통해 **자동으로 변환**함.
- 따라서 개발자는 `.scss` 파일만 작성하고, 배포되는 것은 변환된 `.css`임.
- 중첩을 과도하게 깊게 쓰면 컴파일 결과 선택자가 길어져 **명시도(specificity)가 불필요하게 높아짐.** 3단계 이내로 유지하는 것이 권장됨.
---
##  JavaScript
#### JavaScript 개요 (Introduction to JavaScript)
**웹 브라우저와 서버 양쪽에서 모두 동작하는 프로그래밍 언어**로, 정적인 문서를 넘어 사용자와 상호작용(interactive)하는 웹 페이지·애플리케이션을 만들기 위해 사용됨.
#### 웹 개발 3대 핵심 기술에서의 위치
HTML·CSS와 함께 웹 개발의 핵심 축을 이루며, 각자 역할이 나뉨.
| 기술 | 담당 영역 |
| --- | --- |
| HTML | 구조(Structure) |
| CSS | 표현(Presentation) |
| **JavaScript** | **동적 제어와 논리(Behavior)** |
즉 자바스크립트는 "화면을 그리는" 역할이 아니라, 이미 그려진 화면을 **런타임에 바꾸는** 역할을 맡음. 구체적으로 아래 네 가지가 가능함.
- HTML **콘텐츠(내용)** 변경
- HTML **속성(attribute) 값** 변경
- HTML **스타일(CSS)** 변경
- HTML 요소의 **표시/숨김(Hide/Show)** 제어
#### 주요 기술적 특징
| 특징 | 설명 |
| --- | --- |
| **Interpreter Language** | 별도의 컴파일(빌드) 과정 없이, 브라우저가 코드를 위에서부터 한 줄씩 읽으며 즉시 실행함 |
| **Dynamic Typing** | 변수 선언 시 데이터 타입을 미리 지정하지 않고, **값이 할당되는 순간 타입이 자동 결정**됨 |
| **Single Thread** | 한 번에 하나의 작업만 처리하되, 사용자의 행동(이벤트)을 감지해 **비동기로 처리**함으로써 화면이 멈추지 않도록 제어함 |
- Interpreter 방식이므로 **코드의 작성 순서(위→아래)가 곧 실행 순서**가 되며, 실행 시점 전까지 문법·타입 오류가 드러나지 않는 경우가 많음.
- Single Thread임에도 화면이 멈추지 않는 이유는 **이벤트 기반 비동기 처리** 덕분임. 즉 "스레드가 하나"인 것과 "한 번에 한 가지 일만 기다리며 멈춰 있는 것"은 다른 이야기임.
---
#### JavaScript의 역사 (History) — 핵심만
- 자바스크립트의 공식 표준명은 ECMAScript(ES)임. 흔히 쓰는 "JavaScript"는 통칭이고, 문법 표준 자체는 ECMAScript로 관리됨.
- **2015년 ES6(ES2015) 문법 대개정**으로 현대적이고 강력한 기능들이 대거 도입됨.
- 따라서 Modern JavaScript라고 부르는 기준점이 바로 ES6(ES2015)임. ES6 이전/이후로 문법 스타일이 크게 갈린다고 이해하면 됨.
---
#### JavaScript 실행 방법 (How to Run)
JavaScript 코드는 **HTML 문서에 포함되어 실행**되며, 반드시 `<script>` \~ `</script>` 태그 사이에 작성되어야 함.
```html
<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>
```
#### 작성 위치
`<head>` 또는 `<body>` 어디에나 넣을 수 있으나, 위치에 따라 체감 성능이 달라짐.
| 위치 | 동작 |
| --- | --- |
| `<head>` | 스크립트 로드 중에는 HTML 요소가 렌더링되지 않아 **페이지가 늦게 표시됨** |
| `<body>` 끝 | 모든 콘텐츠가 먼저 렌더링된 후 실행되어 **사용자에게 더 빠른 경험 제공** |
#### External JavaScript
코드를 별도 `.js` 파일로 분리한 뒤 `src` 속성으로 불러오는 방식임. 절대 경로(URL), 루트 상대 경로, 파일명 단독 모두 사용 가능함.
```html
<script src="https://www.w3schools.com/js/myScript.js"></script>
<script src="/js/myScript.js"></script>
<script src="myScript.js"></script>
```
#### 브라우저별 JavaScript Engine
| Browser | JS Engine | 특징 |
| --- | --- | --- |
| Google Chrome | **V8** | 전 세계에서 가장 널리 쓰이는 오픈소스 엔진, 속도가 매우 빠름 |
| Apple Safari | JavaScriptCore | macOS·iOS 등 Apple 하드웨어 생태계에 최적화 |
| Mozilla Firefox | SpiderMonkey | 넷스케이프 시절 만들어진 **세계 최초의 자바스크립트 엔진** |
| Microsoft Edge | **V8** | 크롬과 동일한 V8 엔진을 탑재해 구동 |
---
#### JavaScript 출력 방법 (Output)
JavaScript가 데이터를 화면에 보여주는 방식은 크게 4가지임.
| 방식 | 출력 위치 |
| --- | --- |
| `innerHTML` / `innerText` | HTML 요소 내부에 직접 작성 |
| `document.write()` | HTML 출력 스트림에 작성 |
| `window.alert()` | 알림 창(alert box)에 표시 |
| **`console.log()`** | **브라우저 콘솔**에 출력 |
#### 개발자 도구 Console Tab
- 단축키: **Ctrl + Shift + I**
- `console.log()`의 출력 결과 확인 가능
- 자바스크립트 **에러 메시지 확인** 가능 (예: `Uncaught ReferenceError: consol is not defined` — 오타로 정의되지 않은 식별자를 호출한 경우, 에러 발생 위치가 `(index):11:9`처럼 파일·줄·열 번호로 함께 표시됨)
---
#### 구문과 주석 (Statements & Comments)
프로그램은 컴퓨터가 실행할 **"명령어(instructions)"의 목록**이며, 이 각각의 명령어를 \*\*statement(구문)\*\*라 부름. 구문은 **작성된 순서대로 하나씩** 실행되고, HTML 환경에서는 **웹 브라우저**가 이를 실행함.
#### JavaScript Statements
- 구문은 **Values, Operators, Expressions, Keywords, Comments**로 구성됨
- 세미콜론(`;`)으로 구문을 구분함
- **여러 개의 공백은 무시**되므로, 가독성을 위해 자유롭게 띄어쓰기·들여쓰기 사용 가능
- 중괄호 `{...}`로 구문들을 묶어 코드 블록으로 그룹화할 수 있음
- 키워드는 예약어(reserved words)이므로 변수명으로 사용할 수 없음
#### JavaScript Comments
| 종류 | 문법 |
| --- | --- |
| 한 줄 주석 | `// 내용` |
| 여러 줄 주석 | `/* 내용 */` |
---
#### JavaScript 변수 (Variables)
변수는 **데이터를 담는 컨테이너**이며, 각 변수는 식별자(identifier)라 부르는 고유한 이름으로 구분됨.
#### 변수 선언 방식
선언 방법은 네 가지이나, 실무에서는 **`let`****과 ****`const`****만 사용**하는 것이 권장됨.
- `let`으로 선언
- `const`로 선언
- 키워드 없이 자동 선언 (권장하지 않음)
- `var`로 선언 (권장하지 않음)
| Keyword | 범위(Scope) | 재선언 | 재할당 |
| --- | --- | --- | --- |
| `var` | 함수 범위(function scope) | O | O |
| `let` | **블록 범위(block scope)** | X | O |
| `const` | **블록 범위(block scope)**, 상수 | X | X |
#### 변수의 스코프 3종류
스코프란 **해당 변수에 접근할 수 있는 범위**를 뜻함.
**Global Scope** — 함수/블록 밖에서 선언된 변수로, 프로그램 어디서든 접근 가능함.
```javascript
let carName = "Volvo";
// code here can use carName

function myFunction() {
// code here can also use carName
}
```
**Block Scope** — `{ }` 블록 안에서 선언된 변수는 블록 밖에서 접근 불가함. **`let`****, ****`const`**** 선언에만 해당**됨.
```javascript
{
  let x = 2;
}
// x can NOT be used here
```
**Function Scope** — 함수 내부에서 선언된 변수는 `var`, `let`, `const` **모두** 함수 밖에서 접근 불가함.
```javascript
function myfunction() {
  var x = 1;
  let y = 2;
  const z = 3;
}
// x, y, z can NOT be used here
```
#### let
- ES6(2015)에서 도입된 키워드임
- **블록 스코프**를 가짐
- **사용하기 전에 반드시 선언**되어야 함
- **같은 스코프 내에서 재선언 불가**함 (다른 스코프라면 가능)
#### const
- ES6(2015)에서 도입된 키워드임
- **재선언 불가**, **재할당 불가**
- **블록 스코프**를 가짐
주의할 점은 `const`가 **"상수 값"이 아니라 "값에 대한 상수 참조(constant reference)"를 정의**한다는 것임. 따라서 객체나 배열을 `const`로 선언하면 그 **변수에 다른 객체를 다시 대입하는 것은 불가**하지만, **내부 속성이나 원소를 변경하는 것은 가능**함.
```javascript
const person = {
  name: "철수",
  age: 20
};

// ⭕ 가능: 객체 내부 속성 변경하기
person.age = 21;        // 나이를 21로 변경
person.city = "서울";   // 새로운 속성 추가
console.log(person);   // { name: "철수", age: 21, city: "서울" }

// ❌ 불가능: 변수에 아예 새로운 객체를 '재대입'하기
person = {
  name: "영희",
  age: 25
}; // 💥 Uncaught TypeError: Assignment to constant variable. (에러 발생!)
```
#### 호이스팅 (Hoisting)
**선언(declaration)이 스코프의 최상단으로 끌어올려지는** JavaScript의 기본 동작임. 핵심은 **선언만 올라가고 초기화(값 할당)는 올라가지 않는다**는 점임.
```javascript
// [작성된 코드]
console.log(a);
var a = 10;

// [실제 동작]
var a;             // 선언이 먼저 올라감 (호이스팅)
console.log(a);    // undefined (값이 아직 할당되지 않음)
a = 10;
```
- `var` — 선언이 올라가면서 **`undefined`****로 초기화**되므로, 선언 전 접근 시 에러 없이 `undefined`가 나옴
- `let`, `const` — 블록 최상단으로 **호이스팅되지만 초기화되지 않음**. 따라서 선언 전 접근 시 에러가 발생함 (TDZ, Temporal Dead Zone)
#### 실무 원칙: 변수는 항상 최상단에 선언할 것
호이스팅은 많은 개발자가 놓치기 쉬운 동작이라, 이를 모르면 **의도치 않은 ****`undefined`****나 버그**로 이어짐. 애초에 자바스크립트가 코드를 그렇게 해석하므로, **모든 스코프의 시작 부분에 변수를 선언**해 두는 것이 안전한 습관임.
---
### 데이터 타입 (Datatypes)
JavaScript의 자료형은 기본형(Primitive Data Type)과 객체형(Object / Reference / Non-Primitive Data Type)으로 나뉨.
- **Primitive** → Numeric Type(`Number`, `BigInt`) + Non-Numeric Type(`String`, `Boolean`, `Null`, `Undefined`, `Symbol`)
- **Object** → `Object`, `Array`, `Function`, `Date`, `RegExp`, `Set`, `Map`
| 구분 | 원시 타입 (Primitive) | 객체 타입 (Object) |
| --- | --- | --- |
| 값의 형태 | 단일 값 (단순함) | 속성(Key)과 값(Value)의 집합 (복합함) |
| 메모리 저장 | 변수 공간에 **실제 값**이 직접 저장 | 메모리(Heap) 주소를 가리키는 **참조값**이 저장 |
| 변경 가능성 | **불변성(Immutability)**: 값 수정 불가 | **가변성(Mutability)**: 내부 속성 변경 가능 |
| 속성/메서드 | 없음 (데이터 그 자체) | 있음 |
또한 JavaScript는 동적 타입(dynamic types)이므로, 같은 변수가 서로 다른 타입의 값을 담을 수 있음.
```javascript
let x;        // Now x is undefined
x = 5;        // Now x is a Number
x = "John";   // Now x is a String
```
#### String
- **Using Quotes** — 따옴표 안에 0개 이상의 문자를 넣어 생성함
- **Template Strings** — 백틱(`\``)으로 감싼 문자열
- **String Length** — 내장 `length` 속성으로 길이 확인
- **Escape Characters** — 역슬래시(`\`)로 특수문자를 일반 문자로 처리
- **Strings as Objects** — 보통은 리터럴로 만든 원시값이지만, `new` 키워드로 객체로도 생성 가능함
템플릿 문자열(Template Literals)의 장점은 네 가지임.
| 기능 | 내용 |
| --- | --- |
| Back-Tics Syntax | 따옴표 대신 백틱(` ` \`\`)으로 문자열 정의 |
| Multiline Strings | **여러 줄 문자열**을 그대로 작성 가능 |
| Interpolation | 문자열 안에 **변수를 간편히 삽입** (`${변수}`) |
| Expression Substitution | 변수뿐 아니라 **표현식**도 삽입 가능 |
#### String Methods
문자열은 원시 타입이자 불변(immutable)이므로, 모든 문자열 메서드는 **원본을 바꾸지 않고 새 문자열을 반환**함.
- **기본 메서드** — `concat()`, `substring()`, `substr()`, `toUpperCase()`, `trim()`, `replace()`, `split()` 등
- **검색 메서드** — `indexOf()`, `lastIndexOf()`, `search()`, `match()`, `matchAll()`, `includes()`, `startsWith()` 등
#### Wrapper Object (래퍼 객체)
원시 타입에는 원래 속성·메서드가 없는데도 `"gemini".toUpperCase()`가 동작하는 이유는, JavaScript 엔진이 **원시 타입의 속성/메서드에 접근하는 순간 그 값을 동명의 객체로 임시 변환**하기 때문임. 이 내부 메커니즘을 **Auto-Boxing**이라 부름.
```javascript
const primitiveStr = "hello";
const objectStr = new String("hello");   // 명시적으로 객체로 만듦

console.log(typeof primitiveStr);  // "string" (원시 타입)
console.log(typeof objectStr);     // "object" (객체)
```
| Primitive | Wrapper | 주의사항 |
| --- | --- | --- |
| String | String | 가장 빈번하게 자동 변환이 일어나는 래퍼 객체 |
| Number | Number | 숫자에 바로 마침표를 찍으면 소수점으로 인식하므로 `(10).`처럼 **괄호로 감싸야** 안전함 |
| Boolean | Boolean | `true`/`false`를 문자열 등으로 변환할 때 자동 박싱됨 |
| Symbol | Symbol | 래퍼는 존재하나 `new Symbol()`로 직접 생성은 **금지** |
| BigInt | BigInt | 마찬가지로 `new BigInt()` 직접 생성 **불가** |
| null, undefined | **없음 (예외)** | 래퍼 객체가 없으므로 `.`으로 접근 시 무조건 **TypeError** 발생 |
`new` 키워드로 String/Number 객체를 직접 만드는 것은 코드를 복잡하게 하고 실행 속도를 떨어뜨리므로 **권장하지 않음.**
#### Number
- **Number Types** — 다른 언어와 달리 integer, short, long, float 등을 **구분하지 않고 하나의 ****`Number`**** 타입**만 존재함
- **Integer Precision** — 소수점·지수 표기가 없는 정수는 **15자리까지 정확**함
- **Floating Precision** — 부동소수점 연산은 항상 100% 정확하지는 않음
- **Adding Numbers and Strings** — `+`가 **덧셈과 문자열 연결 양쪽**에 쓰임. 숫자끼리면 더하고, 문자열이 섞이면 이어붙임
- **NaN (Not a Number)** — 값이 정상적인 숫자가 아님을 나타내는 예약어
- **Infinity** — 표현 가능한 최댓값을 벗어나면 `Infinity`(또는 `Infinity`) 반환. \*\*0으로 나눠도 `Infinity`\*가 됨
- **Hexadecimal** — `0x`로 시작하는 숫자 상수는 16진수로 해석됨
- **Numbers as Objects** — `new` 키워드로 객체 생성이 가능하나 권장되지 않음
#### Number Methods and Properties
| 구분 | 목록 |
| --- | --- |
| 기본 메서드 | **`toString()`**, `toExponential()`, `toFixed()`, `toPrecision()`, **`valueOf()`** |
| 숫자 변환 | `Number()`, **`parseInt()`**, **`parseFloat()`** |
| Number 객체 메서드 | `Number.isInteger()`, `Number.isNaN()`, `Number.isFinite()`, `Number.isSafeInteger()`, `Number.parseInt()`, `Number.parseFloat()` |
| Number 객체 속성 | `Number.EPSILON`, `Number.MAX_VALUE`, `Number.MIN_VALUE`, `Number.MAX_SAFE_INTEGER`, `Number.MIN_SAFE_INTEGER`, `Number.POSITIVE_INFINITY`, `Number.NEGATIVE_INFINITY`, `Number.NaN` |
#### BigInt
`Number`의 안전 정수 범위(`Number.MAX_SAFE_INTEGER` \~ `Number.MIN_SAFE_INTEGER`)를 **초과하는 정수를 표현**하기 위한 타입임. 생성 방법은 두 가지임.
```javascript
let x = 12345678901234567890n;            // 정수 리터럴 뒤에 n 접미사
let y = BigInt("12345678901234567890");   // BigInt() 생성자 + 문자열
```
주의할 점은 **BigInt와 Number 간의 산술 연산이 금지**되어 있다는 것임.
```javascript
let x = 10n;
let y = 5;
let z = x + y;   // TypeError
```
#### undefined와 null
**undefined** — 변수 선언은 했으나 **값이 아직 할당되지 않은 상태**를 뜻하는 타입임. 다음 세 경우에 나타남.
```javascript
let something;
console.log(something);   // undefined

const person = {firstName:"John", lastName:"Doe"};
person.age;               // 존재하지 않는 객체 속성 접근 → undefined

function myFunction() { let x = 5; }
myFunction();             // 반환값 없는 함수 호출 → undefined
```
**null** — **"값이 없음"** 또는 "의도적으로 비어 있음"을 표현하는 별도 타입임. `undefined`가 "아직 값이 안 들어온 상태"라면, `null`은 "개발자가 비워둔 상태"라는 점에서 의미가 다름.
```javascript
let nothing = null;
console.log(nothing);   // null
```
#### Symbol
**고유하고 변경 불가능한 값**으로, 주로 **객체의 고유한 속성 키**로 사용됨.
- `Symbol()` 함수로 생성하며, **같은 입력값을 넣어도 결과값은 항상 다름**
- 문자열로 자동 변환되지 않고, `+` 연산도 불가함
```javascript
let sym1 = Symbol("id");
let sym2 = Symbol("id");
console.log(sym1 === sym2);   // false
```
#### Reference Data Types (참조형)
참조형은 데이터의 실제 값이 아닌, **그 값이 저장된 메모리 주소(참조값)를 변수에 저장**하는 타입임.
- **Heap Memory 저장** — 크기가 정해지지 않은 복잡한 데이터이므로 실제 데이터는 **힙(Heap)** 영역에 저장되고, 변수에는 그 위치를 가리키는 **주소만 복사**됨
- **가변성(Mutable)** — 값이 아니라 주소가 공유되므로, 객체 내부 프로퍼티를 변경하면 **같은 주소를 참조하는 다른 변수의 값도 함께 변경**됨
| 자료형 | 설명 | 예시 |
| --- | --- | --- |
| object | 키-값 쌍으로 이루어진 데이터 구조 | `const user = { name: "홍길동", age: 25 };` |
| array | 순서가 있는 값들의 집합 | `let items = [1, 2, 3];` |
| function | 실행 가능한 코드 블록 | `const greet = function() { ... };` |
| date | 날짜와 시간 객체 | `let today = new Date();` |
| Map | 키-값 쌍을 저장하는 컬렉션 (key는 다양한 타입 가능) | `const map = new Map();` |
| Set | 중복되지 않는 값의 집합 | `const set = new Set([1, 2, 3]);` |
| RegExp | 정규 표현식 | `const regex = /abc/i;` |
---
### 연산자 (Operators)
연산자(Operator)는 변수나 값을 대상으로 연산을 수행하여 새로운 값을 만들어내는 기호들임. 산술, 대입, 비교, 논리, 비트, 기타 연산자로 나뉨.
| 구분 | 연산자 | 설명 | 예제 | 결과 |
| --- | --- | --- | --- | --- |
| 산술 | `+` | 덧셈 (Addition) | `5 + 3` | `8` |
| 산술 | `-` | 뺄셈 (Subtraction) | `5 - 3` | `2` |
| 산술 | `*` | 곱셈 (Multiplication) | `5 * 3` | `15` |
| 산술 | `/` | 나눗셈 (Division) | `6 / 2` | `3` |
| 산술 | `%` | 나머지 (Modulus) | `5 % 2` | `1` |
| 산술 | `**` | 거듭제곱 (Exponentiation) | `2 ** 3` | `8` |
| 산술 | `++` | 1 증가 (Increment) | `let a = 1; a++;` | `a = 2` |
| 산술 | `--` | 1 감소 (Decrement) | `let a = 1; a--;` | `a = 0` |
| 대입 | `=` | 값 할당 | `let a = 5` | `a = 5` |
| 대입 | `+=` | 덧셈 후 할당 | `a += 2` | `a = 7` |
| 대입 | `-=` | 뺄셈 후 할당 | `a -= 2` | `a = 3` |
| 대입 | `*=` | 곱셈 후 할당 | `a *= 2` | `a = 10` |
| 대입 | `/=` | 나눗셈 후 할당 | `a /= 2` | `a = 2.5` |
| 대입 | `%=` | 나머지 후 할당 | `a %= 2` | `a = 1` |
| 비교 | `==` | 느슨한 비교, 값이 같으면 true | `5 == '5'` | `true` |
| 비교 | `===` | 엄격한 비교, 값과 타입이 같으면 true | `5 === '5'` | `false` |
| 비교 | `!=` | 느슨한 비교, 값이 다르면 true | `5 != '5'` | `false` |
| 비교 | `!==` | 엄격한 비교, 값 또는 타입이 다르면 true | `5 !== '5'` | `true` |
| 비교 | `<` `>` `<=` `>=` | 크기 비교 | `5 > 3` | `true` |
| 논리 | `&&` | 논리 AND | `true && false` | `false` |
| 논리 | `\|\|` | 논리 OR | `true \|\| false` | `true` |
| 논리 | `!` | 논리 NOT | `!true` | `false` |
| 비트 | `&` | 비트 AND | `5 & 1` → `0101 & 0001` | `0001` → `1` |
| 비트 | `\|` | 비트 OR | `5 \| 1` → `0101 \| 0001` | `0101` → `5` |
| 비트 | `^` | 비트 XOR | `5 ^ 1` → `0101 ^ 0001` | `0100` → `4` |
| 비트 | `~` | 비트 NOT | `~5` | `-6` |
| 비트 | `<<` `>>` `>>>` | 비트 시프트 | `5 >> 1` → `0101 >> 1` | `0010` → `2` |
| 기타 | `? :` | 삼항(조건부) 연산자 | `let result = (5 > 3) ? 'Yes' : 'No'` | `'Yes'` |
| 기타 | `typeof` | 데이터 타입 반환 | `typeof 42` | `'number'` |
| 기타 | `in` | 객체 속성 존재 여부 확인 | `"firstName" in person` | `true / false` |
| 기타 | `instanceof` | 객체의 인스턴스 여부 확인 | `cars instanceof Array` | `true / false` |
---
### 제어문 (Control Flow)
#### if / else / else if
조건에 따라 실행 흐름을 나누는 구문임. `if`는 조건이 참일 때, `else`는 조건이 거짓일 때, `else if`는 앞 조건이 거짓일 경우 새 조건을 검사할 때 사용함.
```javascript
if (country == "USA" && age >= 16) {
  text = "You can drive!";
}

if (time < 10) {
  greeting = "Good morning";
} else if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}
```
#### switch
하나의 값을 여러 case와 비교해 분기하는 구문임. 동작 순서는 다음과 같음.
- switch 표현식은 한 번만 평가됨
- 그 값을 각 case의 값과 차례로 비교함
- 일치하는 case가 있으면 해당 블록을 실행함
- 일치하는 case가 없으면 아무 코드도 실행되지 않음
```javascript
switch (new Date().getDay()) {
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
    break;
  default:
    text = "Looking forward to the Weekend";
}
```
| 키워드 | 역할 |
| --- | --- |
| `break` | 현재 case 블록을 종료하고 switch 문을 빠져나감. 없으면 다음 case 블록이 연속 실행됨 (fall-through) |
| `default` | 어떤 case와도 일치하지 않을 때 실행되는 블록. 선택 사항이며 생략 가능 |
---
#### 반복문 (Loops and Iterations)
반복문은 코드 블록을 여러 번 반복 실행하는 구문임.
| Loop Type | 대상 |
| --- | --- |
| `for` | 값과 표현식 기반 반복 |
| `while` | 조건 기반 반복 |
| `do...while` | 조건 기반 반복 (최초 1회 무조건 실행) |
| `for...in` | 객체의 속성(key) 반복 |
| `for...of` | 배열 등 반복 가능한 객체의 값 반복 |
| `forEach()` | 배열의 각 요소를 순회 |
#### for
`for (exp1; exp2; exp3)` 구조이며 각 표현식의 실행 시점이 다름.
- exp1: 코드 블록 실행 전에 한 번만 실행 (초기화)
- exp2: 코드 블록 실행 조건 (매 반복마다 검사)
- exp3: 코드 블록 실행 후 매번 실행 (증감)
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}

const arr = ["바나나", "사과", "자몽"];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```
#### while / do...while
둘 다 조건이 참인 동안 반복하지만, 조건 검사 시점이 다름. `while`은 먼저 조건을 검사하므로 조건이 처음부터 거짓이면 한 번도 실행되지 않고, `do...while`은 블록을 한 번 실행한 뒤 조건을 검사하므로 최소 1회는 실행됨.
```javascript
let count = 0;
while (count < 3) {
  console.log(count);
  count++;
}

let num = 0;
do {
  console.log(num);
  num++;
} while (num < 3);
```
#### break / continue
| 키워드 | 동작 |
| --- | --- |
| `break` | 특정 조건에서 반복문 자체를 즉시 종료 |
| `continue` | 특정 조건에서 이번 회차의 남은 코드만 건너뛰고 다음 반복으로 이동 |
```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) { break; }      // 반복문 종료
  console.log(i);
}

for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) { continue; }  // 짝수일 때는 건너뜀
  console.log(i);
}
```
#### for...in과 for...of
이름은 비슷하지만 순회 대상이 다름. `for...in`은 객체의 key를 돌고, `for...of`는 반복 가능한 객체(배열, 문자열 등)의 value를 돎.
```javascript
let obj = { name: '홍길동', age: 28, company: '활빈당' };
for (let key in obj) {
  console.log(key, obj[key]);
}

let arr = [10, 20, 30];
for (let value of arr) {
  console.log(value);
}
```
#### 중첩 반복문 (Nested Loop)
반복문 안에 반복문을 넣는 구조임.
```javascript
for (let i = 0; i < 3; i++) {        // 외부 반복문
  for (let j = 0; j < 3; j++) {      // 내부 반복문
    console.log(`i:${i}, j:${j}`);
  }
}
```
- 반복 횟수 관리: 실행 횟수가 곱으로 늘어나 기하급수적으로 커질 수 있으므로 조건과 횟수를 신중히 설정해야 함
- 가독성 유지: 중첩 깊이가 깊어지면 가독성이 떨어지므로, 깊이를 줄이거나 함수로 분리해 관리하는 것이 좋음
---
### 함수 (Functions)
함수는 특정 작업을 수행하도록 설계된 재사용 가능한 코드 블록임. 호출(call/invoke)될 때 실행되며, 한 번 작성해 여러 번 실행함으로써 코드를 재사용하고 작은 단위로 조직화할 수 있어 가독성과 유지보수성이 좋아짐.
```javascript
function name(p1, p2, ...) {
// code to be executed
}
```
- `function` 키워드, 함수명, 소괄호 `()`, 중괄호 `{}`로 정의함
- 실행하려면 함수명 뒤에 소괄호를 붙여 호출함
- 함수 내부에서 선언된 변수는 그 함수의 지역(LOCAL) 변수가 됨
- 함수는 변수처럼 취급되어 수식, 할당, 계산 어디에나 사용할 수 있음
#### 함수 호출 (Invocation)
- 함수 내부 코드는 무언가가 함수를 호출할 때 실행됨
- 함수가 값을 반환하면 그 값을 변수에 저장할 수 있음
- 같은 함수를 필요할 때마다 반복해서 호출할 수 있음
- 호출을 실제로 수행하는 것은 `()` 연산자임
- 다른 함수 안에서, 이벤트에서, 임의의 코드 블록 어디서든 호출 가능함
호출과 참조의 차이를 구분하는 것이 중요함.
```javascript
function sayHello() {
  return "Hello World";
}
let text = sayHello;    // 참조: 함수 자체를 가리킴
let text2 = sayHello(); // 호출: 함수의 실행 결과를 가리킴
```
| 표기 | 의미 |
| --- | --- |
| `sayHello` | 함수 자체를 참조. 함수 객체가 담김 |
| `sayHello()` | 함수를 호출. 실행 결과값이 담김 |
#### 매개변수 (Parameters)
값을 함수에 전달하는 통로임. 정의부에 나열된 이름이 매개변수(Parameters, 매개변수)이고, 호출 시 실제로 전달되는 값이 인수(Arguments, 인수)임.
JavaScript 함수의 매개변수 규칙은 느슨한 편임.
- 함수 정의에서 매개변수의 데이터 타입을 지정하지 않음
- 전달된 인수에 대해 타입 검사를 하지 않음
- 전달된 인수의 개수도 검사하지 않음
따라서 잘못된 인수로 호출해도 에러 없이 잘못된 결과가 반환될 수 있으므로 주의가 필요함. 인수가 전달되지 않은 경우를 대비해 기본값(Default Parameter Value)을 지정할 수 있으며, 이 값은 인수가 없을 때만 사용됨.
#### 반환 (return)
- `return`을 만나면 함수는 그 즉시 실행을 멈춤
- 대부분의 함수는 계산이나 연산의 결과를 반환함
- 반환값은 값이 필요한 어느 위치에서든 사용 가능함
- 숫자뿐 아니라 모든 타입의 값을 반환할 수 있음
- `return` 뒤에 작성된 코드는 실행되지 않음
- 반환값이 없으면 반환값은 `undefined`가 됨
- 조건에 따라 함수를 조기 종료시키는 용도로도 사용함
#### 함수 표현식 (Function Expression)
변수에 함수를 저장하는 방식임. 화살표 함수(Arrow Function)를 쓰면 더 짧게 표현할 수 있음.
```javascript
// Function Declaration (함수선언)
function multiply(a, b) {
  return a * b;
}

// Function Expression (함수표현식)
const multiply = function(a, b) {
  return a * b;
};

// Arrow Function
const multiply = (a, b) => a * b;
```
함수 표현식을 쓰는 이유는 두 가지임.
첫째, 함수 선언문은 함수 Hoisting이 발생해 코드 최상단으로 끌어올려지므로 선언 전에도 호출할 수 있음. 편해 보이지만 규모가 큰 프로젝트에서는 실행 흐름을 흐리고 엉뚱한 함수가 호출되는 버그를 유발함. 함수 표현식은 선언 전 호출이 불가능해 더 안전함.
```javascript
// 1. 함수 선언문: 선언 전 호출 가능 (혼란 유발)
sayHello(); // "Hello"
function sayHello() { console.log("Hello"); }

// 2. 함수 표현식: 선언 전 호출 불가능 (안전함)
sayHi(); // ReferenceError: Cannot access 'sayHi' before initialization
const sayHi = function() { console.log("Hi"); };
```
둘째, 함수 선언문은 엔진이 코드 실행 전 구문 분석 단계에서 미리 생성하므로 `if`문 같은 블록 안에서 유연하게 정의하기 까다로움. 반면 함수 표현식은 코드가 실행되는 시점(Runtime)에 평가되어 함수를 생성하므로, 상황에 따라 전혀 다른 함수를 변수에 할당할 수 있음.
```javascript
let guestWelcome;
const isVIP = true;
// 조건에 따라 변수에 할당되는 '함수 값'을 동적으로 결정
if (isVIP) {
  guestWelcome = function() { console.log("VIP 전용 라운지로 안내합니다."); };
} else {
  guestWelcome = function() { console.log("일반 대기실로 안내합니다."); };
}
guestWelcome(); // 실행 시점에 결정된 함수가 유연하게 호출됨
```
#### 함수의 인수 (Arguments)
인수(Arguments)는 함수에 실제로 전달되어 함수가 받는 값임.
- 인수는 나타난 순서대로 매개변수에 차례로 할당됨
- 인수 자리에는 리터럴 값뿐 아니라 변수도 올 수 있음
- 매개변수 개수보다 적은 인수로 호출하면, 빠진 값은 `undefined`가 됨
#### Call by Value와 Call by Sharing
JavaScript에서 인수 전달 방식은 값의 타입에 따라 체감 결과가 달라짐. 원시 타입은 값 자체가 복사되고, 참조 타입은 주소 값이 복사됨.
| 구분 | Call by Value (기본형 전달) | Call by Sharing (참조형 전달) |
| --- | --- | --- |
| 복사되는 대상 | 실제 데이터 값 (예: `10`, `"Hello"`) | 메모리 주소 값 (예: `0x00412`) |
| 함수 내부 수정 | 원본에 영향 없음 | 원본 객체의 프로퍼티 수정 시 영향 있음 |
```javascript
function changeValue(x) {
// 복사본을 수정함
  x = 20;
}

let a = 10;
changeValue(a);
console.log(a); // 10 (원본은 전혀 변하지 않음)
```
```javascript
function changeProperty(obj) {
// 주소를 타고 들어가 내부 속성을 수정함
  obj.name = "Lee";
}

let user = { name: "Kim" };
changeProperty(user);
console.log(user.name); // "Lee" (원본 객체가 변경됨)
```
---
### 배열 (Arrays)
배열은 데이터 모음(collection)을 저장하기 위해 설계된 객체 타입임. 주요 특징은 다음과 같음.
| 특징 | 내용 |
| --- | --- |
| Elements | 배열은 요소(element)라 부르는 값들의 목록임 |
| Ordered | 요소들은 인덱스를 기준으로 순서를 가짐 |
| Zero indexed | 첫 요소가 인덱스 0, 두 번째가 1로 시작함 |
| Dynamic size | 요소를 추가·제거함에 따라 크기가 늘거나 줄어듦 |
| Heterogeneous | 숫자, 문자열, 객체, 다른 배열 등 서로 다른 타입을 함께 담을 수 있음 |
```javascript
const cars = ["Saab", "Volvo", "BMW"];
```
#### 배열 생성과 접근
생성 방법은 두 가지이나, 배열 리터럴 `[]` 방식이 일반적으로 쓰임.
```javascript
// 배열 리터럴 : []
const cars = ["Saab", "Volvo", "BMW"];

// new 키워드
const cars = new Array("Saab", "Volvo", "BMW");
```
요소 접근과 변경은 인덱스 번호로 하며, `length` 속성으로 요소 개수를 얻음.
```javascript
let car = cars[0];      // 접근
cars[0] = "Opel";       // 변경

const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.length;   // 4
```
#### 기본 메서드 (Basic Array Methods)
전체 목록: `toString()`, `at()`, `join()`, `pop()`, `push()`, `shift()`, `unshift()`, `isArray()`, `delete()`, `concat()`, `copyWithin()`, `flat()`, `slice()`, `splice()`, `toSpliced()`
| 메서드 | 동작 | 예시 |
| --- | --- | --- |
| `toString()` | 요소들을 쉼표로 구분한 문자열로 반환 | `arr.toString()` |
| `pop()` | 맨 뒤 요소를 제거하고 그 요소를 반환 | `let last = arr.pop();` |
| `push()` | 맨 뒤에 새 요소를 추가 | `arr.push(4);` |
| `shift()` | 맨 앞 요소를 제거하고 그 요소를 반환 | `let first = arr.shift();` |
| `unshift()` | 맨 앞에 새 요소를 추가 | `arr.unshift(0);` |
| `at()` | 음수 인덱스 사용 가능. `arr[arr.length - 1]` 대신 간결하게 마지막 요소 접근 | `arr.at(-1);` |
| `join()` | 모든 요소를 지정한 구분자로 연결해 하나의 문자열로 합침 | `arr.join("-");` |
#### 검색 메서드 (Search Methods)
전체 목록: `indexOf()`, `lastIndexOf()`, `includes()`, `find()`, `findIndex()`, `findLast()`, `findLastIndex()`
| 메서드 | 동작 | 예시 |
| --- | --- | --- |
| `indexOf()` | 특정 값이 위치한 인덱스를 반환. 없으면 -1 | `arr.indexOf(5);` |
| `lastIndexOf()` | `indexOf()`와 같으나 마지막으로 등장한 위치를 반환 | `arr.lastIndexOf(5);` |
| `includes()` | 특정 값의 포함 여부를 true/false로 반환 | `arr.includes(5);` |
| `find()` | 조건에 맞는 첫 번째 요소 하나만 반환. 없으면 undefined | `const user = users.find(u => u.id === 3);` |
#### 정렬 메서드 (Sorting Methods)
| 메서드 | 동작 | 원본 변경 |
| --- | --- | --- |
| `sort()` | 배열을 사전순(알파벳순)으로 정렬 | 변경함 |
| `reverse()` | 요소 순서를 뒤집음 | 변경함 |
| `toSorted()` | 정렬된 새 배열을 반환 | 변경 안 함 |
| `toReversed()` | 뒤집힌 새 배열을 반환 | 변경 안 함 |
`sort()`는 기본적으로 문자열 기준 정렬이므로 숫자 배열을 정렬할 때는 비교 함수를 넘겨야 의도한 결과가 나옴.
#### 순회 메서드 (Iteration Methods)
전체 목록: `forEach()`, `map()`, `flatMap()`, `filter()`, `reduce()`, `reduceRight()`, `every()`, `some()`, `from()`, `keys()`, `entries()`, `with()`
| 메서드 | 동작 | 예시 |
| --- | --- | --- |
| `forEach()` | 모든 요소를 순회하며 콜백 함수를 실행. 반환값 없음 | `arr.forEach(item => console.log(item));` |
| `map()` | 모든 요소를 일정 규칙으로 가공해 같은 길이의 새 배열로 반환 | `const doubled = arr.map(item => item * 2);` |
| `filter()` | 조건에 맞는 요소들만 골라 새 배열로 반환 | `const evens = arr.filter(item => item % 2 === 0);` |
| `reduce()` | 모든 요소를 누적 계산해 하나의 결과값으로 만듦 | `const total = arr.reduce((sum, item) => sum + item, 0);` |
#### 전개 연산자 (Spread Operator, `...`)
배열을 개별 요소들로 펼쳐주는 연산자임.
```javascript
const numbers = [23, 55, 21, 87, 56];
let minValue = Math.min(...numbers);
```
`Math.min(...numbers)`는 실행 시 `Math.min(23, 55, 21, 87, 56)`으로 변환되어 처리됨. 배열을 인수 목록으로 풀어야 하는 상황이나 배열 복사·병합에도 널리 쓰임.
---
### 객체 (Objects)
객체는 프로퍼티(Property)와 메서드(Method)를 담는 컨테이너임.
- 프로퍼티는 `key: value` 쌍으로 저장되는 이름 붙은 값임
- 메서드는 `key: function()` 쌍으로 저장되는 함수임
```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
```
#### 객체 생성 방법
객체 리터럴 `{}` 방식이 가장 단순하고 일반적으로 쓰이는 방법임.
```javascript
// 객체 리터럴 {}
const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};

// new Object()
const person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";
```
#### 프로퍼티 접근과 조작
접근 방법은 세 가지임.
| 방식 | 예시 | 비고 |
| --- | --- | --- |
| 점 표기법 (Dot notation) | `person.age` | 권장되는 기본 방식 |
| 대괄호 표기법 (Bracket notation) | `person["age"]` | 키에 공백·특수문자가 있거나 변수로 키를 지정할 때 필요 |
| 표현식 (Expression) | `person[key]` | 대괄호 안에 계산 결과를 넣어 동적 접근 |
프로퍼티 추가·수정·삭제는 별도 문법 없이 할당과 `delete`로 처리함.
- 값 변경: 기존 키에 새 값을 할당하면 됨
- 새 프로퍼티 추가: 존재하지 않는 키에 값을 할당하면 자동으로 추가됨
- 삭제: `delete` 키워드로 프로퍼티를 제거함
- 존재 확인: `in` 연산자로 특정 프로퍼티가 객체에 있는지 검사함
또한 프로퍼티 값에는 다른 객체도 올 수 있으며, 이를 중첩 객체(Nested Objects)라 함.
#### 메서드와 this
객체 메서드 안에서 `this`는 그 메서드를 소유한 객체 자신을 가리킴. 앞선 예제의 `fullName`에서 `this.firstName`이 `person.firstName`을 의미하는 이유가 여기에 있음.
- 메서드를 호출하려면 이름 뒤에 소괄호 `()`를 붙임. 소괄호 없이 쓰면 함수 정의 자체가 반환됨
- 프로퍼티에 함수를 할당하는 것만으로 객체에 메서드를 추가할 수 있음
#### 객체 출력 (Display Objects)
객체를 그대로 출력하면 내용이 아니라 `[object Object]`가 표시됨. 내용을 보려면 다음 방법을 씀.
| 방법 | 설명 |
| --- | --- |
| 프로퍼티 개별 접근 | 필요한 프로퍼티를 직접 지정해 출력 |
| `for...in` 루프 | 객체의 프로퍼티들을 순회하며 수집 |
| `Object.values()` | 프로퍼티 값들로 배열을 생성 |
| `Object.entries()` | key-value 쌍 배열을 만들어 루프에서 다루기 쉽게 함 |
| `JSON.stringify()` | 객체를 문자열로 변환 |
#### 생성자 함수 (Constructors)
같은 형태의 객체를 여러 개 찍어내야 할 때는 객체 생성자 함수를 사용함. `new` 키워드로 호출하면 새 인스턴스가 만들어지고, 함수 내부의 `this`는 그 새 객체를 가리킴.
```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}

const myFather = new Person("John", "Doe", 50, "blue");
const myMother = new Person("Sally", "Rally", 48, "green");
const mySister = new Person("Anna", "Rally", 18, "green");
```
주의할 점은 이미 정의된 생성자에 나중에 프로퍼티나 메서드를 추가할 때임. 생성자 함수 자체에 직접 붙이는 것으로는 기존 인스턴스에 반영되지 않으며, 반드시 생성자 함수의 `prototype`에 추가해야 모든 인스턴스가 공유할 수 있음.
- 새 프로퍼티 추가: `Person.prototype.nationality = "English";`
- 새 메서드 추가: `Person.prototype.name = function() { ... };`
---
### 내장 객체 (Built-in Objects)
JavaScript 엔진(브라우저 또는 Node.js)이 실행 단계에서 기본으로 미리 생성해 제공하는 전역 객체들임. 개발자가 직접 정의하지 않아도 어디서든 바로 사용할 수 있음.
| 객체명 | 주요 목적 | 핵심 메서드/속성 | 인스턴스 생성 (new) |
| --- | --- | --- | --- |
| `Object` | 모든 객체의 기본 틀 | `Object.keys()`, `Object.values()` | 가능, 보통 `{}` 리터럴 사용 |
| `Array` | 순서가 있는 리스트 데이터 | `.push()`, `.map()`, `.filter()` | 가능, 보통 `[]` 리터럴 사용 |
| `String` | 문자열 데이터 조작 및 가공 | `.length`, `.slice()`, `.substring()` | 가능 (Auto-boxing), 보통 `""` 리터럴 사용 |
| `Math` | 수학적 연산 및 수치 처리 | `Math.random()`, `Math.floor()` | 불가능, 정적 메서드로 바로 호출 |
| `Date` | 날짜 및 시간 데이터 | `.getFullYear()`, `.getMonth()` | 필수, `new Date()`로 인스턴스 생성 후 사용 |
| `JSON` | 데이터 교환 형식(텍스트) 변환 | `JSON.stringify()`, `JSON.parse()` | 불가능, 정적 메서드로 바로 호출 |
| `RegExp` | 문자열 내 특정 패턴 검색 (정규식) | `.test()`, `.exec()` | 가능, 보통 `/패턴/` 리터럴 사용 |
#### Math
Math 객체는 정적(static)임. 인스턴스를 생성하지 않고 `Math.메서드명`으로 바로 호출함.
주요 상수: `Math.E`(자연상수 ≈ 2.718), `Math.PI`(원주율 ≈ 3.14159), `Math.SQRT2`(√2 ≈ 1.414) 등
정수 변환 메서드:
| 메서드 | 동작 |
| --- | --- |
| `Math.round(x)` | 반올림 |
| `Math.ceil(x)` | 올림 |
| `Math.floor(x)` | 내림 |
| `Math.trunc(x)` | 소수점 버림 (절삭) |
#### Date
날짜와 시간을 다루는 객체로, 반드시 `new` 키워드로 인스턴스를 생성해야 사용할 수 있음. JavaScript는 날짜를 1970년 1월 1일 00:00:00(UTC) 기준 밀리초 수로 저장함.
```javascript
const d = new Date();              // 현재 날짜와 시간
const d = new Date("2022-03-25"); // 날짜 문자열로 생성
```
날짜 표시 메서드: `toString()`, `toDateString()`, `toUTCString()`, `toISOString()`
#### JSON
JavaScript Object Notation의 약자. JavaScript 객체 형태의 데이터를 텍스트 문자열로 상호 변환해 주는 전역 유틸리티 객체임. 서버와 클라이언트 간 데이터를 주고받을 때 가장 많이 쓰이는 형식임.
`JSON.stringify()` — 직렬화(Serialization): 객체/배열을 JSON 문자열로 변환
```javascript
const user = { name: "홍길동", age: 15 };
const jsonString = JSON.stringify(user);
console.log(jsonString);         // '{"name":"홍길동","age":15}' (순수한 문자열 타입)
console.log(typeof jsonString);  // "string"
```
`JSON.parse()` — 역직렬화(Deserialization): JSON 문자열을 다시 실제 객체/배열로 복원
```javascript
const receivedData = '{"name":"홍길동","age":15}';
const obj = JSON.parse(receivedData);
console.log(obj.name);    // "홍길동" (실제 객체로 복원되어 접근 가능)
console.log(typeof obj);  // "object"
```
#### RegExp (정규 표현식)
정규 표현식은 검색 패턴을 이루는 문자들의 시퀀스임. 텍스트 검색, 텍스트 치환, 텍스트 유효성 검사에 사용됨.
문법: `/pattern/modifier flags`
- `pattern`: 검색할 패턴
- `modifier`: 검색 방식을 조정하는 플래그. 예: `i` — 대소문자 구분 없이 검색
```javascript
let n = text.search(/w3schools/i);

// 전화번호 유효성 검사 예시
const regex =/[0-9]{3}-[0-9]{4}-[0-9]{4}/;
const phone = "010-1234-5678";
console.log(regex.test(phone));  // true
```
#### Set
중복 없는(unique) 값의 모음임. 같은 값은 한 번만 저장되고 두 번 이상 들어가지 않음.
생성 방법은 두 가지임.
- 배열을 `new Set()`에 전달
- 빈 Set을 만든 후 `add()`로 값을 추가
#### Map
key-value 쌍을 저장하는 객체임. 일반 Object와 달리 key에 문자열뿐 아니라 어떤 타입이든 올 수 있음.
생성 방법은 두 가지임.
- 빈 Map을 만든 후 `Map.set()`으로 요소 추가
- 기존 배열을 `new Map()` 생성자에 전달
---
## DOM APIs (Document Object Model)
#### HTML DOM이란
웹 문서(HTML, XML)를 구조화하여 브라우저나 프로그래밍 언어에서 쉽게 접근하고 조작할 수 있도록 하는 표준화된 인터페이스임. W3C와 WHATWG에 의해 정의된 표준이며, DOM은 웹 문서를 트리 구조로 표현하고 각 요소를 객체로 간주함.
- 자바스크립트를 통해 DOM 요소를 실시간으로 변경 가능
- 클릭, 입력, 스크롤 같은 사용자 이벤트 처리 가능
웹 페이지가 로드되면 브라우저는 HTML 문서를 트리 형태로 변환함. 이 트리의 노드 유형은 Document(문서 전체), Element Node(`<html>`, `<head>`, `<body>` 등 태그), Attribute Node(`href` 같은 속성), Text Node(실제 텍스트 내용)로 나뉨.
#### DOM API
DOM API는 JavaScript가 HTML 요소의 내용, 구조, 스타일을 변경할 수 있도록 제공하는 메서드와 속성의 집합임.
```html
<p id="demo"></p>
<script>
  const myPara = document.getElementById("demo");
  myPara.innerHTML = "Hello World!";
</script>
```
- `document`: HTML 문서 자체를 나타내는 객체
- `getElementById()`: 문서 메서드로 특정 id를 가진 요소를 찾아 반환
- `innerHTML`: 요소의 내용을 읽거나 변경하는 속성
#### 요소 선택 (Selecting Elements)
HTML 요소를 찾는 방법은 다섯 가지임.
| 방법 | 메서드/방식 |
| --- | --- |
| id로 찾기 | `document.getElementById("id")` |
| 태그명으로 찾기 | `document.getElementsByTagName("p")` |
| 클래스명으로 찾기 | `document.getElementsByClassName("class")` |
| CSS 선택자로 찾기 | `document.querySelector()`, `document.querySelectorAll()` |
| HTML 객체 컬렉션으로 찾기 | `document.forms`, `document.images` 등 |
#### HTML 변경 (Changing HTML)
요소의 텍스트와 콘텐츠, 속성, 스타일을 JavaScript로 변경할 수 있음.
- `innerHTML`: HTML 요소의 내용을 가져오거나 교체
- `attribute`: HTML 속성의 값을 변경
- `style.property`: HTML 요소의 스타일을 변경
`document.write()`는 HTML 출력 스트림에 직접 쓸 수 있으나, 페이지 로드 후에 호출하면 문서 전체가 덮어씌워지므로 주의해야 함.
#### 이벤트 (Events)
이벤트는 HTML 요소에서 일어나는 일(버튼 클릭, 페이지 로드 완료, 마우스 이동, 키 입력, 입력 필드 변경 등)임. JavaScript는 이벤트가 감지됐을 때 코드를 실행할 수 있게 해줌.
```html
<!-- 직접 인라인으로 실행 -->
<button onclick="document.getElementById('demo').innerHTML=Date()">The time is?</button>

<!-- 함수 호출 방식 (더 일반적) -->
<button onclick="displayDate()">The time is?</button>
<script>
function displayDate() {
  document.getElementById("demo").innerHTML = Date();
}
</script>
```
#### 주요 이벤트 타입
| 이벤트 | 발생 시점 | HTML 속성 |
| --- | --- | --- |
| `click` | 요소를 클릭할 때 | `onclick` |
| `dblclick` | 요소를 두 번 클릭할 때 | `ondblclick` |
| `mouseover` | 마우스 포인터가 요소 위에 올려졌을 때 | `onmouseover` |
| `mouseout` | 마우스 포인터가 요소에서 벗어났을 때 | `onmouseout` |
| `keydown` | 키보드의 키가 눌릴 때 | `onkeydown` |
| `keyup` | 키보드에서 키가 떼어질 때 | `onkeyup` |
| `change` | 입력 값이나 선택 값이 변경될 때 | `onchange` |
| `focus` | 요소가 포커스를 받았을 때 | `onfocus` |
| `blur` | 요소의 포커스가 벗어났을 때 | `onblur` |
| `load` | 페이지나 이미지가 완전히 로드된 후 | `onload` |
| `unload` | 페이지가 언로드될 때 | `onunload` |
#### 이벤트 핸들러 등록 방식
| 방식 | 설명 | 비고 |
| --- | --- | --- |
| Inline Event Handler | HTML 태그 내부에 직접 이벤트 속성을 작성 | JS와 HTML의 역할 분리 원칙 위배. 권장하지 않음 |
| DOM Property | JS에서 DOM 요소의 이벤트 속성에 함수를 할당 | 핸들러 1개만 등록 가능. 덮어쓰기 충돌 위험. 권장하지 않음 |
| Event Listener | `addEventListener()`로 이벤트 핸들러를 등록 | 복수 핸들러 등록 가능, 버블링/캡처 제어 가능, 유지보수 우수. 권장 방식 |
```javascript
// Event Listener (권장)
const btn = document.getElementById("myBtn");
btn.addEventListener("click", function () {
  document.getElementById("demo").innerHTML = Date();
});
```
#### addEventListener 문법
```javascript
element.addEventListener(event, function, useCapture);
```
- `event`: 이벤트 타입 (예: `"click"`, `"mousedown"`)
- `function`: 이벤트 발생 시 호출할 함수
- `useCapture`: 버블링(`false`, 기본값) 또는 캡처링(`true`) 지정
한 요소에 동일한 이벤트 타입으로 여러 핸들러를 중복 등록할 수 있고, 다양한 이벤트 타입으로도 여러 핸들러를 중복 등록할 수 있음.
→ Event Listner 방식으로 구현을 해야, js 파일과 html 파일을 완전히 분리해서 관리가 가능(html 파일에서 js파일을 불러서 사용)
→ 기존, onClink() 등의 inline 방식은 이벤트가 바뀌면, html과 js 파일을 모두 변경해야함.(유지보수에 불리)
#### 이벤트 전파 (Event Propagation)
이벤트가 발생했을 때 요소의 처리 순서를 정의하는 방식임. `<div>` 안에 `<p>`가 있을 때 `<p>`를 클릭하면 어느 요소의 이벤트가 먼저 처리될지가 전파 방식에 따라 달라짐.
| 구분 | 이벤트 버블링 (Bubbling) | 이벤트 캡처링 (Capturing) |
| --- | --- | --- |
| 전파 방향 | 하위 → 상위 (자식에서 부모로) | 상위 → 하위 (부모에서 자식으로) |
| API 구현 | `addEventListener('click', fn)` — 3번째 인수 생략 또는 `false` | `addEventListener('click', fn, true)` — `true` 또는 `{ capture: true }` 전달 |
| 실무 활용도 | 매우 높음 (이벤트 위임 패턴의 핵심) | 낮음 (특수한 로그 수집, 이벤트 가로채기 등에만 사용) |
#### 이벤트 관리 메서드
| 분류 | 메서드 | 역할 | 주의사항 |
| --- | --- | --- | --- |
| Add | `addEventListener(type, handler)` | 특정 이벤트 발생 시 실행할 함수를 등록 | 동일 이벤트 타입에 여러 핸들러 중복 등록 가능 |
| Remove | `removeEventListener(type, handler)` | 이전에 등록했던 특정 이벤트 리스너를 제거 | 등록 시와 정확히 동일한 참조의 함수여야 제거됨 (익명 함수 불가) |
| Block | `event.stopPropagation()` | 이벤트 버블링(전파)을 즉시 중단 | 내 요소의 이벤트는 정상 실행되지만 부모 요소로 올라가지 않음 |
| Block | `event.stopImmediatePropagation()` | 현재 요소의 다른 리스너 실행까지 완전히 막고 전파도 차단 | 같은 요소에 등록된 2·3번째 이벤트도 실행 안 됨 |
| Block | `event.preventDefault()` | HTML 태그의 기본 동작을 취소 | `<a>` 클릭 시 이동, `<form>` submit 시 새로 고침 등 브라우저 기본 행동을 막아줌 |
---
### 비동기 자바스크립트 (Asynchronous JavaScript)
특정 작업(서버에서 데이터 가져오기, 타이머 기다리기 등)이 끝날 때까지 프로그램이 멈춰서 기다리지 않고, 다음 코드를 먼저 실행하는 핵심 효율화 메커니즘임. JavaScript는 Single Thread 언어이므로 비동기가 없다면 서버에서 이미지를 다운로드받는 동안 전체 웹페이지가 멈추게 되는데, 비동기가 이 문제를 해결해줌.
#### 비동기 처리 방식의 발전
| 세대 | 제어 방식 | 코드 구조 특징 | 장점/단점 |
| --- | --- | --- | --- |
| 1세대 | Callback | 함수 안에 함수를 계속 넣음 | 코드가 오른쪽으로 깊어지는 콜백 지옥(Callback Hell) 발생, 가독성 최악, 에러 처리 매우 힘듦 |
| 2세대 (ES6) | Promise | `.then()`과 `.catch()`로 연결 | 비동기 작업의 상태를 객체로 구조화해 콜백 지옥 해결. 다만 코드가 길어지면 `.then()` 체인이 복잡해지는 단점 존재 |
| 3세대 (ES8) | async / await | `await` 키워드로 동기식처럼 작성 | Promise 기반 위에 얹은 문법적 설탕(Syntactic Sugar). 비동기 코드를 마치 일반 동기식 코드처럼 직관적으로 읽히게 함 |
#### Promise
JavaScript 엔진에서 비동기 연산의 최종 완료 또는 실패와 그 결과 값을 나타내는 표준 객체임. 비동기 작업이 성공하거나 실패할 때 그 결과를 알려주겠다고 "약속"하는 객체라 할 수 있음.
Promise는 세 가지 상태를 가짐.
| 상태 | 설명 |
| --- | --- |
| Pending (대기) | 초기 상태. 작업이 시작됐지만 아직 완료도 실패도 아닌 상태 |
| Fulfilled (이행/성공) | 작업이 성공적으로 완료되어 값을 사용할 수 있는 상태 |
| Rejected (거부/실패) | 작업이 실패하여 이유(에러)를 사용할 수 있는 상태 |
#### Promise 생성
```javascript
let myPromise = new Promise(function(resolve, reject) {
// Code that may take some time
  resolve(value); // when successful
  reject(value);  // when error
});
```
Promise를 만들 때 `(resolve, reject) => { ... }` 함수를 인자로 넣음. `resolve`와 `reject`는 JavaScript 엔진이 제공하는 비동기 상태 변경용 함수임.
| 함수 | 의미 |
| --- | --- |
| `resolve` | "이 비동기 작업 성공했어! 이 value 가지고 `.then()`으로 가!" |
| `reject` | "이 작업 실패했어! 이 error 가지고 `.catch()`로 가!" |
`resolve`와 `reject`는 비동기 결과값만 저장해 둘 뿐, 함수의 실행 흐름 자체를 끊지는 않음. 따라서 `resolve()` 호출 뒤에 남은 코드도 계속 실행됨.
#### Promise 소비 코드 (Consuming Code)
하나의 Promise 안에는 생산 코드(producing code)와 소비 코드(consuming code)에 대한 호출이 함께 담김.
```javascript
let myPromise = new Promise(function(resolve, reject) {
// "Producing Code" (May take some time)
  resolve(value); // when successful
  reject(value);  // when error
});

// Consuming Code
myPromise
.then(function(value) {  // catch는 myPromise가 성공할 때 실행  
  console.log(value);
})
.catch(function(value) { // catch는 myPromise가 실패할 때 실행  
console.log(value);
});
```
초기 문법에서는 `.then()`의 첫 번째 인자가 성공 시, 두 번째 인자가 실패 시 실행할 콜백이었지만, 현재는 위 코드처럼 `.then().catch()` 체이닝 방식이 권장됨.
#### Promise Chains
세 개의 비동기 함수가 순서대로 호출되어야 하면, `.then()` 안에서 다음 단계를 `return`해 체인을 만듦.
```javascript
function step1() {
  return Promise.resolve("A");
}
function step2(value) {
  return Promise.resolve(value + "B");
}
function step3(value) {
  return Promise.resolve(value + "C");
}

step1()
.then(function(value) {
  return step2(value);
})
.then(function(value) {
  return step3(value);
})
.then(function(value) {
  myDisplayer(value);
});
```
`return`이 빠지면 실행 순서가 보장되지 않음. `return` 대신 `.then()` 안에 또 `.then()`을 중첩시키는 방식으로 짜면 가독성이 떨어지고 에러 처리도 까다로워짐.
#### async와 await
Promise 체인이 길어지는 문제를 해결하기 위해 도입된 문법임. 중첩을 줄이고 가독성을 높여줌.
```javascript
// async와 await를 이용한 구현
async function run() {
  let v1 = await step1();
  let v2 = await step2(v1);
  let v3 = await step3(v2);
  myDisplayer(v3);
}
```
**async** — "이 함수 안에서 비동기 처리를 할 거야!"라고 선언하는 키워드임.
- async 함수는 항상 Promise를 반환함
- 일반 값을 리턴하면 JavaScript가 자동으로 `Promise.resolve(값)`으로 감싸서 내보냄
```javascript
async function hello() {
  return "안녕하세요!";
}
console.log(hello());              // Promise {<fulfilled>: '안녕하세요!'}
hello().then(res => console.log(res)); // 안녕하세요!
```
**await** — "비동기 작업이 끝날 때까지 다음 줄로 넘어가지 말고 기다려!"라고 명령하는 키워드임. 반드시 async 함수 안에서만 사용 가능함.
```javascript
async function handleData() {
  try {
    const result = await fetchData();               // 첫 번째 비동기 기다림
    const saveResult = await saveToDatabase(result); // 두 번째 비동기 기다림
    console.log("저장 성공!", saveResult);
  } catch (error) {
    console.log("에러 발생!", error);
  }
}
```
#### async/await의 흐름 제어 (Flow Control)
비동기 호출 시 JavaScript 엔진 내부의 흐름 제어는 Event Loop와 Microtask Queue를 기반으로 이루어짐.
**Step 1 — await를 만나 함수가 일시 정지되는 순간**
- `await` 라인을 만나는 순간 그 뒤의 비동기 함수는 즉시 실행시키고, 해당 async 함수의 실행은 일시 정지(Pause)됨
- 이 함수 내부의 나머지 코드와 함수의 현재 상태(컨텍스트)를 통째로 떼어내어 메모리의 별도 대기 구역에 보관함
- 제어권은 이 async 함수를 호출했던 원래의 메인 실행 흐름(Call Stack)으로 반환되어, 그 아래에 남아있던 동기식 코드들을 실행함
**Step 2 — 메인 흐름이 실행되는 동안 비동기 작업이 완료된 순간 (핵심)**
- 메인 흐름의 남은 동기식 코드가 실행되는 도중, `await`하고 있던 비동기 작업(예: 서버 통신 완료)이 먼저 끝날 수 있음
- 이때 완료되었다고 해서 실행 중이던 메인 흐름을 강제로 끊고 중간에 끼어들지는 못함. JavaScript는 Single Thread 언어이므로 한 번에 하나의 코드만 실행할 수 있기 때문임
- 비동기 작업이 완료되면, 대기실에 있던 async 함수의 나머지 실행 후속 조치들이 JavaScript 엔진 내부의 최우선 대기 레일인 Microtask Queue라는 대기줄에 등록되어 순서를 기다림
**Step 3 — 메인 흐름이 완전히 종료된 직후 (흐름의 복귀)**
- 메인 실행 흐름에 있던 마지막 동기식 코드까지 전부 실행되어 호출 스택(Call Stack)이 완전히 비게 되는 순간, JavaScript의 감시자인 Event Loop가 가동함
- Event Loop는 Microtask Queue에서 대기 중이던 async 함수의 나머지 코드를 꺼내어 다시 메인 호출 스택에 올려놓음
- 흐름은 다시 async 함수 내부의 `await` 바로 다음 줄로 복귀하여, 서버에서 받아온 데이터를 가지고 남은 하부 로직을 순차적으로 끝까지 실행함
---
### 브라우저 API (Browser API)
Web API는 웹 기술을 사용하는 모든 곳에서 공통으로 지원하는 확장성을 담은 단어이며, 실행되는 환경과 주체에 따라 Browser API와 Server API로 나뉨. Browser API는 크롬, 사파리, 엣지 같은 웹 브라우저가 구동되면서 자바스크립트 엔진에게 상속해 주는 내장 도구들을 가리키는 표현임.
| 카테고리 | 대표 함수/객체 | 하는 일 |
| --- | --- | --- |
| DOM API | `document.querySelector()`, `element.addEventListener()` | HTML 태그 조작 및 클릭 이벤트 제어 |
| Timer API | `setTimeout(함수, 시간)`, `setInterval(함수, 시간)` | 특정 시간 뒤에 코드를 실행하거나, 일정 시간마다 반복 실행 (비동기) |
| Storage API | `localStorage.setItem()`, `sessionStorage.getItem()` | 브라우저에 로그인 토큰이나 설정 데이터를 영구 저장 |
| Network API | `fetch()` | 브라우저 새로고침 없이 서버와 데이터를 주고받는 통신 (비동기) |
#### Timer API
특정 시간이 지난 후 코드를 실행하거나 일정 시간마다 반복 실행하도록 예약하는 기능임. JavaScript 엔진 자체에는 타이머 기능이 없고, JavaScript가 브라우저에게 부탁하면 브라우저가 백그라운드에서 시간을 재고 있다가 정해진 시간에 함수를 실행해주는 원리임.
타이머 함수를 실행하면 브라우저는 해당 타이머의 고유 번호(Timer ID)를 반환함. 더 이상 타이머가 필요 없을 때 이 ID를 취소 메서드에 넘겨야 메모리 낭비나 버그를 막을 수 있음.
| 함수 | 핵심 역할 | 작동 방식 |
| --- | --- | --- |
| `setTimeout()` | 지정한 시간이 지난 후 딱 1번만 함수를 실행 | `setTimeout(콜백함수, 밀리초)` |
| `setInterval()` | 지정한 시간 간격마다 무한 반복하여 함수를 실행 | `setInterval(콜백함수, 밀리초)` |
```javascript
const bombId = setTimeout(function() {
  console.log("폭탄이 터졌습니다!");
}, 5000); // 5초 뒤에 폭탄이 터지는 타이머 예약 (ID를 변수에 저장)

button.addEventListener("click", function() {
  clearTimeout(bombId); // 5초가 지나기 전에 실행하면 폭탄은 영원히 터지지 않음
  console.log("안전하게 해제되었습니다.");
});
```
#### Storage API (Web Storage)
사용자의 브라우저에 데이터를 키-값(Key-Value) 쌍으로 저장할 수 있는 공간임. 과거에는 'Cookie' 기술을 주로 썼으나, 용량이 너무 작고 서버와 통신할 때마다 불필요하게 계속 전송되는 단점이 있었음.
| 구분 | LocalStorage | SessionStorage |
| --- | --- | --- |
| 데이터 유지 | 영구적 (브라우저를 닫거나 컴퓨터를 꺼도 유지) | 임시적 (탭이나 브라우저 창을 닫으면 즉시 삭제) |
| 만료 조건 | 코드로 지우거나 캐시를 날리면 삭제 | 현재 열려있는 탭(세션) 종료 시 자동 삭제 |
| 데이터 공유 | 같은 도메인이면 여러 창/탭에서 공유 가능 | 데이터를 저장한 그 탭 내부에서만 접근 가능 |
| 활용처 | 자동 로그인 토큰, "오늘 하루 열지 않음" 상태, 다크모드 설정 | 일시적 로그인 정보, 일회성 입력 폼 |
```javascript
localStorage.setItem("username", "홍길동");   // 데이터 저장: setItem(Key, Value)
localStorage.setItem("userAge", "25");        // 주의: 숫자를 넣어도 문자열 "25"로 저장됨

const name = localStorage.getItem("username"); // 데이터 가져오기: getItem(Key)
console.log(name);                              // 출력: 홍길동

localStorage.removeItem("userAge");             // userAge 데이터만 삭제됨
```
#### Network API — fetch()
서버에 데이터를 요청하는 현대적인 방식임. `fetch()`는 비동기적으로 동작하며 Promise를 반환함.
```javascript
fetch("data.json")
.then(function(response) {
  console.log(response);
});
```
**async/await와 함께 사용하기** — await는 단순히 기다리는 것을 넘어, Promise 객체의 내부 메커니즘과 상호작용하며 결과물을 처리해주는 특별한 기능을 가짐. `await fetch()`를 하면 서버와 통신한 결과를 가져와 response로 만들어줌.
```javascript
async function loadData() {
  let response = await fetch("data.json");
  let data = await response.json();
  console.log(data);
}

loadData();
```
---
#### 모듈 (Modules in JavaScript)
ES6부터 도입된 모듈은 다른 파일에서 함수, 객체, 변수 등을 가져오거나 내보낼 수 있게 해줌. 코드의 재사용과 관리를 쉽게 하기 위해 각 파일이나 코드 덩어리를 독립적인 유닛으로 분리하는 방식임.
#### Export / Import 기본
모듈 외부에서 사용할 변수, 함수, 클래스, 객체를 정의할 때 `export`를 사용하고, 다른 모듈에서 내보낸 요소를 가져와 사용할 때 `import`를 사용함.
```javascript
// math.js — Export
export function add(a, b) {
  return a + b;
}
```
```html
<script type="module">
// Import the add function
import { add } from './math.js';
let result = add(2, 3);
</script>
```
#### Export 방식 비교
| 방식 | 내보내는 방법 | 장점 | 단점 |
| --- | --- | --- | --- |
| Named Exports | `export const foo = ...;`<br>`export function bar() {}`<br>`import { foo, bar } from './module.js';` | 여러 개 내보내기 가능, 이름 기준 명확한 가져오기 | 이름을 정확히 기억해야 함, 이름 변경 시 수정 필요 |
| Default Exports | `export default function() {...}`<br>`const value = ...; export default value;`<br>`import anyName from './module.js';` | 이름을 자유롭게 지정 가능, 간결한 단일 내보내기 | 한 모듈에 하나만 가능, 실제 이름을 알기 어려움 |
| Combining Default + Named | `export const foo = ...;`<br>`export default bar;`<br>`import bar, { foo } from './module.js';` | 주요 기능은 default로, 보조 기능은 named로 구성 | 가독성이 떨어질 수 있음, 일관성 관리 어려움 |
#### Module vs. External JS
External JavaScript는 코드를 단순히 분리한 것에 불과하다면, JavaScript Module은 각 파일의 경계를 안전하게 격리하고 필요한 기능만 통로(import/export)로 주고받는 현대적 설계 체계임.
| 구분 | External JS (일반 외부 파일) | JavaScript Module (모듈 파일) |
| --- | --- | --- |
| HTML 로드 형태 | `<script src="file.js"></script>` | `<script type="module" src="file.js"></script>` |
| Scope | 전역 스코프 공유 (모든 파일이 소통함) | 모듈 스코프 격리 (독립된 공간) |
| 변수 충돌 위험 | 매우 높음 (이름이 같으면 버그 발생) | 없음 (완벽한 은닉화) |
| 소통 방식 | 전역 변수나 전역 함수를 통해 간접 소통 | `import`와 `export`를 통해 명확히 소통 |
| 실행 시점 | 태그를 만나는 순간 즉시 실행 (HTML 중단) | HTML을 끝까지 다 읽은 후 지연 실행 (defer) |
변수 충돌 위험 예시:
```javascript
// external-a.js
const count = 10;

// external-b.js
const count = 20; // 에러 발생! (같은 전역 스코프)
```
```javascript
// module-a.js
const count = 10; // 이 파일 안에서만 살아있음

// module-b.js
const count = 20; // 아무 문제 없음!
```
→ 보통은 아래와 같이 `as` 와 같은 별칭으로 구분해서 사용
```javascript
// main.js (불러오는 곳)
import { count as countA } from './module-a.js'; // 이름을 countA로 변경
import { count as countB } from './module-b.js'; // 이름을 countB로 변경

console.log(countA); // 10 (a의 count)
console.log(countB); // 20 (b의 count)
```
---
<empty-block/>
