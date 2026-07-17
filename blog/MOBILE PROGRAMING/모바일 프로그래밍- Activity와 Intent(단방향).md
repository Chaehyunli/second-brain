---
title: "[모바일 프로그래밍] Activity와 Intent(단방향)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-10-23
source_url: https://ch010104.tistory.com/169
---

# [모바일 프로그래밍] Activity와 Intent(단방향)

## 원문

https://ch010104.tistory.com/169

## 노트 유형

`guide`

## 적용 목적과 전제조건

액티비티는 안드로이드 앱에서 사용자가 상호작용하는 하나의 UI(사용자 인터페이스) 화면을 의미

예를 들어, 이메일 앱은 '이메일 목록을 보여주는 액티비티', '새 이메일을 작성하는 액티비티', '선택한 이메일을 읽는 액티비티' 등으로 나뉠 수 있음

## 구현 절차·검증·주의점

### 1. 안드로이드 앱의 주요 구성 요소: 액티비티 (Activity)

액티비티는 안드로이드 앱에서 사용자가 상호작용하는 하나의 UI(사용자 인터페이스) 화면을 의미

앱은 여러 개의 액티비티로 구성될 수 있음

예를 들어, 이메일 앱은 '이메일 목록을 보여주는 액티비티', '새 이메일을 작성하는 액티비티', '선택한 이메일을 읽는 액티비티' 등으로 나뉠 수 있음

### 2. 안드로이드 앱의 주요 구성 요소: 인텐트 (Intent)

- 인텐트는 한 액티비티에서 다른 액티비티를 호출할 때 필요한 핵심 요소

- 이는 액티비티 간에 데이터를 전달하는 '메신저' 역할을 수행

주요 기능:

다른 컴포넌트에게 특정 동작을 요청하거나 이벤트가 발생했음을 알림

액티비티를 호출할 때, 호출 대상이 되는 액티비티를 명시

대상 액티비티에게 데이터를 전달하는 데 사용될 수 있음

호출된 액티비티가 실행을 마친 후, 결과를 다시 회신하는 목적으로도 사용

예시: 연락처 앱의 액티비티를 실행하여 사용자가 특정 연락처를 선택하게 하고, 반환되는 인텐트에 선택된 연락처의 URI(경로)를 담아 돌려받는 경우가 있음

### 3. 인텐트의 종류: 명시적 인텐트와 암시적 인텐트

- 인텐트는 컴포넌트 간에 데이터를 주고받기 위한 메시지 객체입니다. 인텐트는 크게 두 가지로 구분

명시적 인텐트 (Explicit Intent): 인텐트를 전달받을 대상 컴포넌트(예: SecondActivity)를 명시적으로 정확하게 지정하는 방식

암시적 인텐트 (Implicit Intent): 대상 컴포넌트를 명시하지 않고, 수행할 'Action'(동작)(예: '전화 걸기', '웹페이지 열기')을 지정하면 안드로이드 시스템이 해당 동작을 수행할 수 있는 적절한 컴포넌트를 찾아 연결해주는 방식

### 4. 명시적 인텐트를 이용한 데이터 전달 (단방향)

- 명시적 인텐트는 SecondActivity::class.java와 같이 대상 액티비티의 클래스 참조 정보를 사용하여 인텐트 객체를 생성

액티비티 실행:

```text
// applicationContext에서 SecondActivity::class.java로 가는 인텐트 생성
val mIntent: Intent = Intent(applicationContext, SecondActivity::class.java)
// 생성한 인텐트를 시스템에 전달하여 액티비티 실행
startActivity(mIntent)
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

startActivity(intent)가 호출되면, 시스템은 인텐트에 명시된 SecondActivity를 실행시키고 이 인텐트를 SecondActivity에게 전달

데이터 송신 (Sending Activity)

```text
// "Message"라는 key로 msg 변수(String) 값을 추가
intent.putExtra("Message", msg)
// "Age"라는 key로 age 변수(int) 값을 추가
intent.putExtra("Age", age)
// "Names"라는 key로 names 변수(String 배열) 값을 추가
intent.putExtra("Names", names)
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

데이터 추가: 보내는 측(Caller)에서는 putExtra() 메소드를 사용하여 'key'-'value' 쌍의 형태로 인텐트에 데이터를 추가

데이터 수신 (Receiving Activity)

데이터 추출: 받는 측(Callee)의 onCreate() 메소드 내에서 다음 과정을 통해 데이터를 추출

getIntent() 메소드를 호출하여 자신을 실행시킨 인텐트( rxIntent )를 받음

rxIntent.getExtras()를 통해 모든 추가 데이터가 담긴 Bundle 객체( extras )를 얻음

extras가 null이 아닌지 확인한 후, get<Type>() 메소드에 **데이터를 보낼 때 사용한 'key'**를 넣어 값을 추출

```text
// "Message" key에 해당하는 String 값을 추출
val rxMsg = extras.getString("Message")
// "Age" key에 해당하는 Int 값을 추출
val rxAge = extras.getInt("Age")
// "Names" key에 해당하는 String 배열 값을 추출
val rxNames = extras.getStringArray("Names")
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 5. Activity 및 Intent 구현 실습

기본 구조: 일반적으로 액티비티 하나는 레이아웃 XML 파일 1개와 Kotlin(코틀린) 클래스 파일 1개로 구성

클래스 상속: MainActivity.kt와 같은 코틀린 클래스 파일은 Activity 클래스 또는 호환성을 위한 AppCompatActivity 클래스를 상속받아 만들어짐

구현 과정:

build.gradle 파일에서 뷰 바인딩(View Binding) 기능을 활성화

SecondActivity가 사용할 레이아웃 파일 activity_second.xml과 클래스 파일 SecondActivity.kt를 추가하고 구현

MainActivity에서 SecondActivity를 호출하도록 MainActivity.kt를 구현

새로 추가한 SecondActivity를 시스템이 인식할 수 있도록 AndroidManifest.xml 파일에 등록

ainActivity에서 SecondActivity로 "John"이라는 문자열과 25라는 정수 값을 putExtra로 전달하고 , SecondActivity는 이 값들을 getIntent와 getExtras를 통해 받아 EditText에 출력(확장) - 단방향

```text
// MainActivity.kt

package com.cookandroid.activityexcercise

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.cookandroid.activityexcercise.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var bindingMain : ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        enableEdgeToEdge()
//        setContentView(R.layout.activity_main)
//        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
//            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
//            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
//            insets
//        }

        bindingMain = ActivityMainBinding.inflate(layoutInflater)
        setContentView(bindingMain.root)

        bindingMain.btn2ndActivity.setOnClickListener {
            val mIntent : Intent = Intent(applicationContext, SecondActivity::class.java)

            startActivity(mIntent)
        }
    }
}
```

```text
// SecondActivity.kt

package com.cookandroid.activityexcercise

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import com.cookandroid.activityexcercise.databinding.ActivitySecondBinding

class SecondActivity : AppCompatActivity() {

    private lateinit var bindingSecond : ActivitySecondBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        bindingSecond = ActivitySecondBinding.inflate(layoutInflater)
        setContentView(bindingSecond.root)

        val rxIntent: Intent = getIntent()

        val extras: Bundle? = rxIntent.getExtras()

        val rxName:String? = extras?.getString("Name") ?: null
        val rxAge = extras?.getInt("Age") ?: null

        bindingSecond.edit1.setText("Name: " + rxName + ", Age: " + rxAge.toString())

        // SecondActivity를 종료시켜서 자동으로 MainActivity로 돌아감
        bindingSecond.btnReturn.setOnClickListener(object: View.OnClickListener {
            override fun onClick(p0: View?){
                finish()
            }
        })
    }

}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

```html
// activity_main.xml

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="50dp"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/btn2ndActivity"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Start 2nd Activity"/>

</LinearLayout>
```

```html
// activity_second.xml

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:background="@android:color/holo_green_light"
    android:padding="50dp"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:id="@+id/btnReturn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Back to MainActivity"/>

    <TextView
        android:id="@+id/edit1"
        android:textColor="@color/black"
        android:layout_gravity="center_horizontal"
        android:textSize="20dp"
        android:hint="Intent name and email"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"/>

</LinearLayout>
```

```html
// AndroidManifest.xml

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.ActivityExcercise">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

		// 이전에 만든 SecondActivity에 대한 내용을 추가
        <activity android:name=".SecondActivity"
            android:exported="true"/>

    </application>

</manifest>
```

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 토스트(Toast)와 대화 상자(AlertDialog)|[모바일 프로그래밍] 토스트(Toast)와 대화 상자(AlertDialog)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
