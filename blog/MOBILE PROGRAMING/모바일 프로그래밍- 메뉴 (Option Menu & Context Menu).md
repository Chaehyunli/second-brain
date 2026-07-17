---
title: "[모바일 프로그래밍] 메뉴 (Option Menu & Context Menu)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-10-13
source_url: https://ch010104.tistory.com/158
---

# [모바일 프로그래밍] 메뉴 (Option Menu & Context Menu)

## 원문

https://ch010104.tistory.com/158

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

옵션 메뉴는 액티비티의 주 메뉴로, 보통 앱 바(App Bar)에 표시

메뉴 XML 파일 생성: - res/menu 폴더에 메뉴 항목을 정의하는 XML 파일을 생성 - 각 메뉴 항목은 <item> 태그를 사용하며, id와 title 속성을 가짐

## 원문 기반 학습 정리

### 옵션 메뉴 (Option Menu)

옵션 메뉴는 액티비티의 주 메뉴로, 보통 앱 바(App Bar)에 표시

XML을 이용한 생성 과정

```html
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/itemId1"
        android:title="항목1 제목"/>
    <item
        android:id="@+id/itemId2"
        android:title="항목2 제목"/>
</menu>
```

메뉴 XML 파일 생성: - res/menu 폴더에 메뉴 항목을 정의하는 XML 파일을 생성 - 각 메뉴 항목은 <item> 태그를 사용하며, id와 title 속성을 가짐

```text
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    super.onCreateOptionsMenu(menu)
    val menuInflater: MenuInflater = getMenuInflater()
    menuInflater.inflate(R.menu.menu_xml_file, menu)
    return true
}
```

onCreateOptionsMenu() 오버라이딩: - 액티비티가 시작될 때 메뉴를 생성하기 위해 이 메소드를 오버라이딩 - MenuInflater를 사용해 XML 파일을 실제 메뉴 객체로 만듬

```text
override fun onOptionsItemSelected(item: MenuItem): Boolean {
    when (item.itemId) {
        R.id.itemId1 -> { /* 항목1 선택 시 실행할 코드 */ }
        R.id.itemId2 -> { /* 항목2 선택 시 실행할 코드 */ }
    }
    return super.onOptionsItemSelected(item)
}
```

onOptionsItemSelected() 오버라이딩: - 메뉴 항목을 클릭했을 때의 동작을 정의 - when 문을 사용해 선택된 아이템의 ID를 확인하고 해당 코드를 실행

실습

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
    android:gravity="center"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="오른쪽 위 매뉴를 클릭하세요"/>

    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="button1"/>

</LinearLayout>
```

```html
// menu1.xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/itemRed"
        android:title="배경색(빨강)"
        />

    <item
        android:id="@+id/itemGreen"
        android:title="배경색(초록)"
        />

    <item
        android:id="@+id/itemBlue"
        android:title="배경색(파랑)"
        />

    <item android:title="버튼 변경 >>">
        <menu>
            <item
                android:id="@+id/subitemRotate"
                android:title="버튼 45도 회전"/>

            <item
                android:id="@+id/subitemzOOM"
                android:title="버튼 Zoom in"/>
        </menu>
    </item>

</menu>
```

```text
// MainActivity.kt
package com.cookandroid.optionmenuexcercise

import android.graphics.Color
import android.os.Bundle
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import com.cookandroid.optionmenuexcercise.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //        enableEdgeToEdge()
        //        setContentView(R.layout.activity_main)
        //        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
        //            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
        //            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
        //            insets
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        super.onCreateOptionsMenu(menu)
        val menuInflater: MenuInflater = getMenuInflater()
        menuInflater.inflate(R.menu.menu1, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.itemRed -> {
                binding.main.setBackgroundColor(Color.RED)
                return true
            }

            R.id.itemGreen -> {
                binding.main.setBackgroundColor(Color.GREEN)
                return true
            }

            R.id.itemBlue -> {
                binding.main.setBackgroundColor(Color.BLUE)
                return true
            }

            R.id.subitemRotate -> {
                binding.button1.rotation = 45.0f
                return true
            }

            R.id.subitemzOOM -> {
                binding.button1.scaleX = 2.0f
                return true
            }
        }
        return super.onOptionsItemSelected(item)
    }
}
```

### 컨텍스트 메뉴 (Context Menu)

- 컨텍스트 메뉴는 특정 위젯(버튼, 텍스트 뷰 등)을 길게 클릭(long-click)했을 때 나타나는 메뉴

XML을 이용한 생성 과정

메뉴 XML 파일 생성: - 옵션 메뉴와 동일한 방식으로 필요한 메뉴 XML 파일을 생성 - 각 위젯마다 다른 메뉴를 연결할 수 있음

```text
// onCreate() 내부
registerForContextMenu(button1)
registerForContextMenu(button2)
```

위젯 등록: - onCreate() 메소드 안에서 registerForContextMenu()를 호출하여 특정 위젯에 컨텍스트 메뉴를 등록

```text
override fun onCreateContextMenu(menu: ContextMenu?, v: View?, menuInfo: ContextMenu.ContextMenuInfo?) {
    super.onCreateContextMenu(menu, v, menuInfo)
    val mInflater = menuInflater
    when (v?.id) {
        R.id.widget1 -> mInflater.inflate(R.menu.menu1, menu)
        R.id.widget2 -> mInflater.inflate(R.menu.menu2, menu)
    }
}
```

onCreateContextMenu() 오버라이딩: - 위젯을 길게 클릭했을 때 호출 - 이 메소드 안에서 클릭된 위젯 ID(v?.id)를 확인하여 각기 다른 메뉴 XML을 등록

onContextItemSelected() 오버라이딩: - 메뉴 항목을 클릭했을 때의 동작을 코딩 _ 옵션 메뉴의 onOptionsItemSelected()와 유사하게 작동

### 실습

```html
// activity_main.wml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="베경색 변경"/>

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="버튼 변경"/>

</LinearLayout>
```

```html
// menu1.xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/itemRed"
        android:title="배경색(빨강)"
        />

    <item
        android:id="@+id/itemGreen"
        android:title="배경색(초록)"
        />

    <item
        android:id="@+id/itemBlue"
        android:title="배경색(파랑)"
        />
</menu>
```

```html
//menu2
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/itemButton1"
        android:title="버튼 변경1"
        />

    <item
        android:id="@+id/itemButton2"
        android:title="버튼 변경2"
        />

</menu>
```

```text
// MainActivity.kt
package com.cookandroid.contextmenuexcercise

import android.graphics.Color
import android.os.Bundle
import android.view.ContextMenu
import android.view.MenuInflater
import android.view.MenuItem
import android.view.View
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.cookandroid.contextmenuexcercise.databinding.ActivityMainBinding
import kotlinx.coroutines.selects.RegistrationFunction

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        enableEdgeToEdge()
//        setContentView(R.layout.activity_main)
//        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
//            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
//            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
//            insets
//        }

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        registerForContextMenu(binding.button1)
        registerForContextMenu(binding.button2)
    }

    // context 매뉴가 보여지는 부분
    override fun onCreateContextMenu(menu: ContextMenu?, v: View?, menuInfo: ContextMenu.ContextMenuInfo?) {
        super.onCreateContextMenu(menu, v, menuInfo)
        val mInflater: MenuInflater = getMenuInflater()
        when (v?.id) {
            R.id.button1 -> {
                var headerTitle = menu?.setHeaderTitle("배경색 변경")
                mInflater.inflate(R.menu.menu1, menu)
            }
            R.id.button2 -> {
                var headerTitle = menu?.setHeaderTitle("버튼 변경")
                mInflater.inflate(R.menu.menu2, menu)
            } else -> {}
        }
    }

    // context 매뉴가 눌렸을 때 발생하는 이밴트 부분
    override fun onContextItemSelected(item: MenuItem): Boolean {

        when(item.itemId){
            R.id.itemRed -> {
                binding.main.setBackgroundColor(Color.RED)
                return true
            }

            R.id.itemGreen -> {
                binding.main.setBackgroundColor(Color.GREEN)
                return true
            }

            R.id.itemBlue -> {
                binding.main.setBackgroundColor(Color.BLUE)
                return true
            }

            R.id.itemButton1 -> {
                binding.button2.rotation = 45.0f
                return true
            }

            R.id.itemButton2 -> {
                binding.button2.scaleX = 2.0f
                return true
            }

        }

        return super.onContextItemSelected(item)
    }

}
```

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 테이블레이아웃과 그리드레이아웃|[모바일 프로그래밍] 테이블레이아웃과 그리드레이아웃]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 토스트(Toast)와 대화 상자(AlertDialog)|[모바일 프로그래밍] 토스트(Toast)와 대화 상자(AlertDialog)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- LinearLayout 안드로이드 레이아웃|[모바일 프로그래밍]  LinearLayout 안드로이드 레이아웃]]
