---
title: "[모바일 프로그래밍] 뷰(View)와 기본 위젯"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-09-22
source_url: https://ch010104.tistory.com/137
---

# [모바일 프로그래밍] 뷰(View)와 기본 위젯

## 원문

https://ch010104.tistory.com/137

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

- 안드로이드에서 앱 실행 화면을 구성하는 모든 요소를 뷰(View)라고 부름

- 흔히 위젯(Widget)이라고도 하죠. 화면에 보이는 버튼, 텍스트, 이미지 등이 모두 뷰에 해당

## 원문 기반 개념 정리

### 1. 뷰(View)와 뷰그룹(ViewGroup)이란?

- 안드로이드에서 앱 실행 화면을 구성하는 모든 요소를 뷰(View)라고 부름

- 흔히 위젯(Widget)이라고도 하죠. 화면에 보이는 버튼, 텍스트, 이미지 등이 모두 뷰에 해당

뷰(View): - 화면 UI를 구성하는 기본 클래스 - 예를 들어, 화면에 보이는 버튼은 '버튼 위젯'이고, 코드에서는 'Button 클래스'로 다루게 됨

뷰그룹(ViewGroup): - 다른 뷰(위젯)들을 담을 수 있는 특별한 뷰임 - 뷰들을 체계적으로 배치하는 '레이아웃(Layout)'이 대표적인 뷰그룹에 속함

모든 위젯과 레이아웃은 View 클래스를 상속받아 만들어지기 때문에, 계층 구조를 가짐

### 2. 모든 위젯이 상속받는 공통 XML 속성

- 모든 위젯은 View 클래스로부터 공통된 속성을 물려받음 - ML 레이아웃 파일에서 위젯을 다룰 때 필수로 알아야 할 기본 속성들을 소개

id

각 위젯을 유일하게 식별하기 위한 고유 아이디를 지정

코드에서 특정 위젯에 접근할 때 이 id를 사용하게 됨

아이디를 새로 부여할 때는 "@+id/아이디명" 형식으로 지정함

사용 예시: 버튼 클릭과 같이 특정 동작이 필요한 위젯에는 id를 반드시 지정해야 함

하지만 화면에 텍스트를 보여주기만 하는 TextView처럼 특별한 동작이 없다면 id를 생략 가능

```html
<Button
    android:id="@+id/btn1"
    ... />
```

layout_width & layout_height

- 위젯의 너비와 높이를 지정하는 필수 속성

match_parent: 부모 요소(주로 레이아웃)의 크기에 꽉 채움

wrap_content: 위젯 안에 있는 내용물(텍스트, 이미지 등)의 크기에 맞게 설정

직접 크기 지정: 100dp와 같이 단위를 사용하여 직접 크기를 지정할 수도 있음

background

- 위젯의 배경 색상이나 이미지를 지정하는 속성 - 주로 #RRGGBB 형태의 16진수 색상 코드를 사용

```html
<Button
    android:background="#00ff00"
    ... />
```

padding

- 위젯의 경계선과 위젯 안의 내용(텍스트 등) 사이의 여백을 설정

- 주로 레이아웃의 경계와 그 안의 위젯들 사이에 여백을 주고 싶을 때 사용

layout_margin

- 위젯의 경계선 바깥쪽 여백을 설정

- 이 속성을 사용하면 위젯과 위젯 사이에 간격을 만들 수 있음

visibility

- 위젯을 화면에 보여줄지 여부를 결정

visible: 화면에 보입니다 (기본값).

invisible: 화면에 보이지 않지만, 원래 차지하던 공간은 그대로 유지

gone: 화면에 보이지 않고, 차지하던 공간도 사라짐

enabled & clickable

enabled: - 위젯의 동작 여부를 결정 - false로 설정하면 위젯이 비활성화되어 보임

clickable: - 위젯의 클릭 가능 여부를 결정 - 두 속성 모두 true 또는 false 값을 가짐

rotation

위젯을 특정 각도만큼 회전시켜서 표시

```html
<Button
    android:rotation="45"
    ... />
```

### 3. 기본 위젯 다루기 - 텍스트뷰(TextView)

- 텍스트뷰는 화면에 문자열을 표시하는 가장 기본적인 위젯

- TextView 클래스는 View 클래스를 상속받으므로 공통 속성을 모두 사용할 수 있음

- 다음과 같은 텍스트 관련 주요 속성들을 가짐

text: 화면에 표시할 문자열을 지정

textColor: 글자의 색상을 지정합니다 (#RRGGBB).

textSize: 글자의 크기를 지정합니다 (30sp, 16dp 등).

typeface: 글꼴을 지정합니다 (sans, serif, monospace 등).

textStyle: 글자에 스타일을 적용합니다 (bold, italic).

singleLine: 텍스트가 길어질 경우, 한 줄로만 표시하고 나머지는 '...'으로 처리

```html
<TextView
    android:text="안녕하세요, 안드로이드!"
    android:textSize="20sp"
    android:textColor="#FF0000"
    android:textStyle="bold|italic" />
```

### 4. 계산기 앱 구현

📝 코드 주요 기능 및 특징

UI 구성: 2개의 숫자 입력창(EditText), 4개의 연산 버튼(Button), 1개의 결과 표시창(TextView)으로 구성

뷰 바인딩(ViewBinding): findViewById 없이 XML 레이아웃의 뷰(View)에 직접 접근

이벤트 처리: 각 버튼에 클릭 리스너(setOnClickListener)를 설정하여, 버튼이 눌렸을 때 지정된 연산을 수행

예외 처리: - 숫자가 아닌 값을 입력하거나 비워뒀을 경우를 대비해 toDoubleOrNull()을 사용 - 0으로 나누는 경우를 방지하는 로직이 포함되어 있음

🎨 1. 화면 구성 (activity_main.xml)

- 사용자 인터페이스(UI)는 LinearLayout을 사용하여 위젯들을 수직으로 차례대로 쌓는 방식으로 만들어짐

<LinearLayout>: orientation="vertical" 속성을 통해 내부의 위젯들을 세로로 정렬

<EditText> (ID: Edit1, Edit2): 사용자가 숫자를 입력하는 두 개의 텍스트 필드

android:hint: 입력창이 비어있을 때 안내 문구를 보여줌

android:inputType="numberDecimal": 숫자(소수점 포함) 키패드가 나타나도록 설정

<Button> (ID: BtnAdd, BtnSub, BtnMul, BtnDiv): '더하기', '빼기', '곱하기', '나누기' 기능을 수행하는 4개의 버튼입.

<TextView> (ID: TextResult): 계산 결과를 보여주는 텍스트 뷰

android:textColor="#FF0000": 글자 색을 빨간색으로 지정

android:textSize="30dp": 글자 크기를 30dp로 지정

⚙️ 2. 핵심 로직 (MainActivity.kt)

- MainActivity.kt 파일은 화면의 실제 동작을 제어

뷰 바인딩 초기화

val binding = ActivityMainBinding.inflate(layoutInflater) 코드를 통해 XML 레이아웃 파일을 메모리에 로드하고, XML에 있는 뷰들에 직접 접근할 수 있는 binding 객체를 생성

setContentView(binding.root)를 통해 이 binding 객체가 관리하는 화면을 액티비티에 표시

버튼 클릭 이벤트 처리

각 버튼(예: binding.BtnAdd)에 setOnClickListener를 설정하여 클릭 이벤트를 감지

버튼이 클릭되면 다음과 같은 로직이 실행

binding.Edit1.text.toString(): 입력창의 텍스트를 가져옴

.toDoubleOrNull() ?: 0.0: 가져온 텍스트를 Double 타입(소수)으로 변환

만약 텍스트가 비어있거나 숫자가 아니어서 변환에 실패하면 null을 반환하는데, 이때 ?: 0.0(엘비스 연산자)를 통해 기본값 0.0을 사용

사칙연산을 수행한 후, binding.TextResult.text = "결과: $result" 코드로 결과 TextView의 내용을 업데이트

나누기 예외 처리

나누기 버튼의 로직에는 if (num2 != 0.0) 조건문이 포함되어 있음

이를 통해 두 번째 숫자가 0일 경우 나눗셈을 실행하지 않고 "0으로 나눌 수 없습니다"라는 메시지를 출력하여 앱이 비정상적으로 종료되는 것을 방지

🔧 3. 프로젝트 설정 (build.gradle)

- build.gradle 파일은 프로젝트의 빌드 환경을 설정합니다. 여기서 가장 중요한 부분은 뷰 바인딩 활성화

```text
android {
    // ...
    viewBinding.isEnabled = true
}
```

viewBinding.isEnabled = true 설정을 통해 프로젝트에서 뷰 바인딩 기능을 사용할 수 있게 됨

이 설정이 있어야 안드로이드 스튜디오가 ActivityMainBinding 같은 바인딩 클래스를 자동으로 생성

4. 실습 코드

```text
// MainActivity.kt
package com.example.helloandroid_60212232

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.helloandroid_60212232.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // === Project4_1: 계산기 구현 ===
        val binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // 더하기 버튼 클릭 이벤트
        binding.BtnAdd.setOnClickListener {
            val num1 = binding.Edit1.text.toString().toDoubleOrNull() ?: 0.0
            val num2 = binding.Edit2.text.toString().toDoubleOrNull() ?: 0.0
            val result = num1 + num2
            binding.TextResult.text = "결과: $result"
        }

        // 빼기 버튼 클릭 이벤트
        binding.BtnSub.setOnClickListener {
            val num1 = binding.Edit1.text.toString().toDoubleOrNull() ?: 0.0
            val num2 = binding.Edit2.text.toString().toDoubleOrNull() ?: 0.0
            val result = num1 - num2
            binding.TextResult.text = "결과: $result"
        }

        // 곱하기 버튼 클릭 이벤트
        binding.BtnMul.setOnClickListener {
            val num1 = binding.Edit1.text.toString().toDoubleOrNull() ?: 0.0
            val num2 = binding.Edit2.text.toString().toDoubleOrNull() ?: 0.0
            val result = num1 * num2
            binding.TextResult.text = "결과: $result"
        }

        // 나누기 버튼 클릭 이벤트
        binding.BtnDiv.setOnClickListener {
            val num1 = binding.Edit1.text.toString().toDoubleOrNull() ?: 0.0
            val num2 = binding.Edit2.text.toString().toDoubleOrNull() ?: 0.0
            if (num2 != 0.0) {
                val result = num1 / num2
                binding.TextResult.text = "결과: $result"
            } else {
                binding.TextResult.text = "0으로 나눌 수 없습니다"
            }
        }
    }
}
```

```html
// activity_main.xml
<?xml version="1.0" encoding="utf-8"?>

<!-- === Project4_1: 계산기 레이아웃 === -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp"
    tools:context=".MainActivity">

    <!-- 첫 번째 EditText -->
    <EditText
        android:id="@+id/Edit1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:hint="첫 번째 숫자"
        android:inputType="numberDecimal" />

    <!-- 두 번째 EditText -->
    <EditText
        android:id="@+id/Edit2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:hint="두 번째 숫자"
        android:inputType="numberDecimal" />

    <!-- 더하기 버튼 -->
    <Button
        android:id="@+id/BtnAdd"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:text="더하기" />

    <!-- 빼기 버튼 -->
    <Button
        android:id="@+id/BtnSub"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:text="빼기" />

    <!-- 곱하기 버튼 -->
    <Button
        android:id="@+id/BtnMul"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:text="곱하기" />

    <!-- 나누기 버튼 -->
    <Button
        android:id="@+id/BtnDiv"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:text="나누기" />

    <!-- 결과 TextView -->
    <TextView
        android:id="@+id/TextResult"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_margin="10dp"
        android:text="계산 결과"
        android:textColor="#FF0000"
        android:textSize="30dp"
        android:gravity="center"
        android:padding="20dp" />

</LinearLayout>
```

```text
// build.gradle.kts
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = "com.example.helloandroid_60212232"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.mjuce.mp.helloandroid_60212232"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    kotlinOptions {
        jvmTarget = "11"
    }

    viewBinding.isEnabled = true
}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    implementation(libs.androidx.activity)
    implementation(libs.androidx.constraintlayout)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
}
```

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 파운드 버튼과 이벤트 처리|[모바일 프로그래밍] 파운드 버튼과 이벤트 처리]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 코틀린(Kotlin)이란- ( 3 ) - 실습|[모바일 프로그래밍] 코틀린(Kotlin)이란? ( 3 ) - 실습]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 이미지뷰와 이미지버튼 실습|[모바일 프로그래밍] 이미지뷰와 이미지버튼 실습]]
