---
title: "[모바일 프로그래밍] Fragment와 생명 주기 + 실습"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing"]
category: "MOBILE PROGRAMING"
published: 2025-11-05
source_url: https://ch010104.tistory.com/180
---

# [모바일 프로그래밍] Fragment와 생명 주기 + 실습

## 원문

https://ch010104.tistory.com/180

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

도입 배경: Android 3.0 (API level 11)에서 태블릿과 같은 큰 화면에서 동적이고 유연한 UI 디자인을 지원하기 위해 도입

정의: 하나의 유저 화면을 여러 개로 나누거나 2, 액티비티의 레이아웃을 여러 개의 조각으로 나눔

## 원문 기반 학습 정리

### 디자인 철학 및 특징 (Design Philosophy & Characteristics)

도입 배경: Android 3.0 (API level 11)에서 태블릿과 같은 큰 화면에서 동적이고 유연한 UI 디자인을 지원하기 위해 도입

정의: 하나의 유저 화면을 여러 개로 나누거나 2, 액티비티의 레이아웃을 여러 개의 조각으로 나눔

호스팅 액티비티: 프래그먼트는 호스팅 액티비티와 연결되어 있음

구성 요소: 각 프래그먼트는 다음을 가짐:

자신만의 레이아웃

자신만의 라이프사이클과 콜백 함수

호스트 액티비티의 라이프사이클과 연동됨

호스팅 액티비티가 관리하는 백 스택

제공하는 기능:

모듈성 (Modularity): 액티비티의 레이아웃을 프래그먼트로 나눔

재사용성 (Reusability): 여러 액티비티에서 공유 가능

적응성 (Adaptability): 다른 화면 크기에 맞게 프래그먼트를 재구성

### 사용 예시 (Usage Examples)

### 프래그먼트 라이프사이클 (Fragment Lifecycle)

유사성: 프래그먼트 라이프사이클은 액티비티의 라이프사이클과 유사함

주요 단계 (한글): 초기화(initialized), 생성(created), 시작(started), 재개(resumed), 소멸(destroyed) 단계로 구분됨

콜백 함수 및 설명:

백 스택 동작: 프래그먼트가 백 스택에 추가된 후 제거/교체되거나 14사용자가 뒤로 탐색하거나 프래그먼트가 제거/교체되면 15onPause()로 진행됨16. 백 스택에서 레이아웃으로 복귀할 수도 있음17.

### 프래그먼트 구현 (Fragment Implementation)

생성 방법:

Fragment 클래스를 상속함 (Extend Fragment class)

ListFragment 19, PreferenceFragment 20또는 DialogFragment 21와 같은 다른 클래스를 상속받아 가능함

새 프래그먼트 추가: New > Fragment > Fragment(Blank)를 선택하여 추가할 수 있으며, 이 과정에서 .kt 파일과 fragment_my_color.xml 파일이 추가됨

onCreateView(): 프래그먼트 레이아웃 XML 파일에 대한 바인딩 객체를 이용하여 bindingFragment.root를 반환하여 레이아웃을 생성함

### 액티비티에 프래그먼트 추가 (Adding Fragment to Activity)

정적 추가 (Statically): 액티비티의 레이아웃 내부에 <android.fragment.FragmentContainerView> 태그를 사용하여 추가

동적 추가 (Dynamically): FragmentManager와 FragmentTransaction을 사용하여 코드로 추가

transaction.add(R.id.fragment_container, fragment)를 사용

replace()도 사용 가능함

transaction.commit()으로 변경 사항을 적용.

백 스택 관리: transaction.commit() 전에 addToBackStack()을 호출하여 커밋할 트랜잭션을 백 스택에 추가할 수 있으며, 이 유무에 따른 차이 관찰이 실습 목표 중 하나임.

### 데이터 전달 (Data Transfer)

액티비티에서 프래그먼트로 데이터 전송:

Bundle 객체 생성

data.put<type>(<key>, <value>) 형식으로 데이터 저장 (예: data.putString("COLOR", "green")).

프래그먼트 객체의 arguments에 Bundle 객체 할당 (fragment.arguments = data)

transaction.add() 등을 통해 프래그먼트 추가

프래그먼트에서 데이터 수신:

프래그먼트의 onCreate()에서 arguments를 통해 Bundle 객체를 얻음 (val rxData: Bundle? = arguments)

저장된 키로 데이터를 읽어옴 (예: val rxColor: String = rxData?.getString("COLOR") ?: "none")

### 실습 내용 (Practical Exercise)

목표: MainActivity의 FragmentContainerView 영역에 프래그먼트를 표시하고, 버튼 클릭에 따라 다른 배경색의 프래그먼트로 영역을 갱신

구성 요소: activity_main.xml에 FragmentContainerView 1개와 버튼 3개 포함.

프래그먼트 구현:

fragment_my_color.xml: 프래그먼트 레이아웃 구현.

MyColorFragment.kt: 프래그먼트 클래스 구현

onCreate(): 사용자가 선택한 배경색 확인

onCreateView(): 레이아웃 파일을 이용하여 프래그먼트 레이아웃 생성

onViewCreated(): 선택한 색상으로 레이아웃 배경색 설정

```text
// MainActivity.kt

package com.cookandroid.fragmentexcercise

import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentTransaction
import com.cookandroid.fragmentexcercise.databinding.ActivityMainBinding

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

        Log.i("프래그먼트 실습", "MainActivity : onCreate")

        bindingMain.btnRed.setOnClickListener(object : View.OnClickListener {
            override fun onClick(p0: View?) {
                val fragment = MyColorFragment()

                val data : Bundle = Bundle()
                data.putString("COLOR", "red")
                fragment.arguments = data

                val fragmentManager : FragmentManager = supportFragmentManager
                val transaction : FragmentTransaction = fragmentManager.beginTransaction()
                // transaction.add(R.id.fragment_container_view, fragment)
                transaction.replace(R.id.fragment_container_view, fragment)
                transaction.addToBackStack(null) // 이전 fragment를 backStack에 저장되어 있음(사용자가 뒤로가기를 누르면, backStack에 저장되어 있던 fragment가 다시 나옴)
                transaction.commit()
            }
        })

        bindingMain.btnGreen.setOnClickListener(object : View.OnClickListener {
            override fun onClick(p0: View?) {
                val fragment = MyColorFragment()

                val data : Bundle = Bundle()
                data.putString("COLOR", "green")
                fragment.arguments = data

                val fragmentManager : FragmentManager = supportFragmentManager
                val transaction : FragmentTransaction = fragmentManager.beginTransaction()
                transaction.add(R.id.fragment_container_view, fragment)
                transaction.commit()

            }
        })

        bindingMain.btnBlue.setOnClickListener(object : View.OnClickListener {
            override fun onClick(p0: View?) {
                val fragment = MyColorFragment()

                val data : Bundle = Bundle()
                data.putString("COLOR", "blue")
                fragment.arguments = data

                val fragmentManager : FragmentManager = supportFragmentManager
                val transaction : FragmentTransaction = fragmentManager.beginTransaction()
                transaction.add(R.id.fragment_container_view, fragment)
                transaction.commit()
            }
        })
    }

    override fun onStart() {
        super.onStart()
        Log.i("프래그먼트 실습", "MainActivity : onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.i("프래그먼트 실습", "MainActivity : onResume")
    }

    override fun onPause() {
        super.onPause()
        Log.i("프래그먼트 실습", "MainActivity : onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.i("프래그먼트 실습", "MainActivity : onStop")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.i("프래그먼트 실습", "MainActivity : onDestroy")
    }

    override fun onRestart() {
        super.onRestart()
        Log.i("프래그먼트 실습", "MainActivity : onRestart")
    }
}
```

```typescript
// MyColorFragment.kt

package com.cookandroid.fragmentexcercise

import android.content.Context
import android.graphics.Color
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.cookandroid.fragmentexcercise.databinding.FragmentMyColorBinding

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [MyColorFragment.newInstance] factory method to
 * create an instance of this fragment.
 */
class MyColorFragment : Fragment() {

    private lateinit var rxColor: String

    override fun onAttach(context: Context) {
        super.onAttach(context)
        Log.i("프래그먼트 실습", "MyColorFragement : onAttach")
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val rxData : Bundle? = arguments // mainActivity로부터 넘겨 받은 bundle 객체를 받음
        rxColor = rxData ?.getString("COLOR") ?:"white"

        Log.i("프래그먼트 실습", "MyColorFragement : onCreate : " + rxColor)
    }

//    // TODO: Rename and change types of parameters
//    private var param1: String? = null
//    private var param2: String? = null
//
//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        arguments?.let {
//            param1 = it.getString(ARG_PARAM1)
//            param2 = it.getString(ARG_PARAM2)
//        }
//    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        // return super.onCreateView(inflater, container, savedInstanceState)
        Log.i("프래그먼트 실습", "MyColorFragment : onCreateView : " + rxColor)
        val bindingFragmentMyColor : FragmentMyColorBinding = FragmentMyColorBinding.inflate(layoutInflater)
        return bindingFragmentMyColor.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        when(rxColor){
            "red" -> {
                view.setBackgroundColor(Color.RED)
                Log.i("프래그먼트 실습", "MyColorFragment : onViewCreated : " + rxColor)
            }
            "green" -> {
                view.setBackgroundColor(Color.GREEN)
                Log.i("프래그먼트 실습", "MyColorFragment : onViewCreated : " + rxColor)
            }
            "blue" -> {
                view.setBackgroundColor(Color.BLUE)
                Log.i("프래그먼트 실습", "MyColorFragment : onViewCreated : " + rxColor)
            }
            else -> {
                view.setBackgroundColor(Color.WHITE)
                Log.i("프래그먼트 실습", "MyColorFragment : onViewCreated : " + rxColor)
            }
        }
    }

    override fun onStart() {
        super.onStart()
        Log.i("프래그먼트 실습", "MyColorFragement : onStart : " + rxColor)
    }

    override fun onResume() {
        super.onResume()
        Log.i("프래그먼트 실습", "MyColorFragement : onResume : " + rxColor)
    }

    override fun onPause() {
        super.onPause()
        Log.i("프래그먼트 실습", "MyColorFragement : onPause : " + rxColor)
    }

    override fun onStop() {
        super.onStop()
        Log.i("프래그먼트 실습", "MyColorFragement : onStop : " + rxColor)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        Log.i("프래그먼트 실습", "MyColorFragement : onDestroyView : " + rxColor)
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.i("프래그먼트 실습", "MyColorFragement : onDestroy : " + rxColor)
    }

    override fun onDetach() {
        super.onDetach()
        Log.i("프래그먼트 실습", "MyColorFragement : onDetach : " + rxColor)
    }

//    companion object {
//        /**
//         * Use this factory method to create a new instance of
//         * this fragment using the provided parameters.
//         *
//         * @param param1 Parameter 1.
//         * @param param2 Parameter 2.
//         * @return A new instance of fragment MyColorFragment.
//         */
//        // TODO: Rename and change types and number of parameters
//        @JvmStatic
//        fun newInstance(param1: String, param2: String) =
//            MyColorFragment().apply {
//                arguments = Bundle().apply {
//                    putString(ARG_PARAM1, param1)
//                    putString(ARG_PARAM2, param2)
//                }
//            }
//    }
}
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
        android:theme="@style/Theme.FragmentExcercise">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

```html
// fragement_my_color.xml

<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="@android:color/white"
    tools:context=".MyColorFragment">

    <!-- TODO: Update blank fragment layout -->
    <TextView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:text="MyColor" />

</FrameLayout>
```

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
    tools:context=".MainActivity">

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/fragment_container_view"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:name="com.cookandroid.fragmentexcercise.MyColorFragment"
        />

    <LinearLayout
        android:id="@+id/linerLayout1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:layout_gravity="bottom">

        <Button
            android:id="@+id/btnRed"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_margin="10dp"
            android:text="RED"/>

        <Button
            android:id="@+id/btnGreen"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_margin="10dp"
            android:text="GREEN"/>

        <Button
            android:id="@+id/btnBlue"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:layout_margin="10dp"
            android:text="BLUE"/>

    </LinearLayout>

</LinearLayout>
```

### 실습 분석 : fragement 생명주기

```text
// MainActivity.kt -> onCreate()

        bindingMain.btnRed.setOnClickListener(object : View.OnClickListener {
            override fun onClick(p0: View?) {
                val fragment = MyColorFragment()

                val data : Bundle = Bundle()
                data.putString("COLOR", "red")
                fragment.arguments = data

                val fragmentManager : FragmentManager = supportFragmentManager
                val transaction : FragmentTransaction = fragmentManager.beginTransaction()
                // transaction.add(R.id.fragment_container_view, fragment)
                // transaction.replace(R.id.fragment_container_view, fragment)
                // transaction.addToBackStack(null) // 이전 fragment를 backStack에 저장되어 있음(사용자가 뒤로가기를 누르면, backStack에 저장되어 있던 fragment가 다시 나옴)
                transaction.commit()
            }
        })
```

1. transaction.add 사용 시 (중첩)

addToBackStack(null) 사용 시

'Green' 프래그먼트 추가: MyColorFragement : onAttach부터 MyColorFragement : onResume : green까지 로그가 찍히며 'green' 프래그먼트가 'white' 프래그먼트 위에 추가

```text
MyColorFragement : onAttach
MyColorFragement : onCreate : white
MainActivity : onCreate
MyColorFragment : onCreateView : white
MyColorFragment : onViewCreated : white
MyColorFragement : onStart : white
MainActivity : onStart
MainActivity : onResume
MyColorFragement : onResume : white
MyColorFragement : onAttach
MyColorFragement : onCreate : green
MyColorFragment : onCreateView : green
MyColorFragment : onViewCreated : green
MyColorFragement : onStart : green
MyColorFragement : onResume : green
MyColorFragement : onPause : green // (뒤로 가기 버튼 눌림!!)
MyColorFragement : onStop : green
MyColorFragement : onDestroyView : green
MyColorFragement : onDestroy : green
MyColorFragement : onDetach : green
```

'뒤로 가기' 버튼: 'green' 프래그먼트만 종료됩

addToBackStack(null) 미사용 시

'Green' 프래그먼트 추가: onAttach부터 onResume : green까지 로그가 찍히며 'green' 프래그먼트가 'white' 프래그먼트 위에 추가됩니다.

```text
MyColorFragement : onAttach
MyColorFragement : onCreate : white
MainActivity : onCreate
MyColorFragment : onCreateView : white
MyColorFragment : onViewCreated : white
MyColorFragement : onStart : white
MainActivity : onStart
MainActivity : onResume
MyColorFragement : onResume : white
MyColorFragement : onAttach
MyColorFragement : onCreate : green
MyColorFragment : onCreateView : green
MyColorFragment : onViewCreated : green
MyColorFragement : onStart : green
MyColorFragement : onResume : green
MyColorFragement : onPause : white // (뒤로 가기 버튼 눌림!!)
MyColorFragement : onPause : green
MainActivity : onPause
MyColorFragement : onStop : white
MyColorFragement : onStop : green
MainActivity : onStop
MyColorFragement : onDestroyView : white
MyColorFragement : onDestroy : white
MyColorFragement : onDetach : white
MyColorFragement : onDestroyView : green
MyColorFragement : onDestroy : green
MyColorFragement : onDetach : green
MainActivity : onDestroy
```

'뒤로 가기' 버튼: 'white', 'green' 프래그먼트 및 MainActivity가 모두 종료

2. transaction.replace 사용 시 (교체)

addToBackStack(null) 미사용 시

```text
MyColorFragement : onAttach
MyColorFragement : onCreate : white
MainActivity : onCreate
MyColorFragment : onCreateView : white
MyColorFragment : onViewCreated : white
MyColorFragement : onStart : white
MainActivity : onStart
MainActivity : onResume
MyColorFragement : onResume : white
MyColorFragement : onPause : white // (Red 버튼을 눌렀을 때, white fragment 완전히 파괴)
MyColorFragement : onStop : white
MyColorFragement : onAttach
MyColorFragement : onCreate : red
MyColorFragment : onCreateView : red
MyColorFragment : onViewCreated : red
MyColorFragement : onStart : red
MyColorFragement : onDestroyView : white
MyColorFragement : onDestroy : white
MyColorFragement : onDetach : white
MyColorFragement : onResume : red
MyColorFragement : onPause : red // (뒤로 가기 버튼 누름)
MainActivity : onPause
MyColorFragement : onStop : red
MainActivity : onStop
MyColorFragement : onDestroyView : red
MyColorFragement : onDestroy : red
MyColorFragement : onDetach : red
MainActivity : onDestroy
```

'Red' 프래그먼트로 교체: 'white' 프래그먼트가 완전히 파괴되고 'red' 프래그먼트가 새로 생성

'뒤로 가기' 버튼: 'red' 프래그먼트와 MainActivity가 함께 종료됩니

addToBackStack(null) 사용 시

```text
MyColorFragement : onAttach
MyColorFragement : onCreate : white
MainActivity : onCreate
MyColorFragment : onCreateView : white
MyColorFragment : onViewCreated : white
MyColorFragement : onStart : white
MainActivity : onStart
MainActivity : onResume
MyColorFragement : onResume : white
MyColorFragement : onPause : white // (Red 버튼을 눌렀을 때, white fragment 완전히 파괴)
MyColorFragement : onStop : white
MyColorFragement : onAttach
MyColorFragement : onCreate : red
MyColorFragment : onCreateView : red
MyColorFragment : onViewCreated : red
MyColorFragement : onStart : red
MyColorFragement : onDestroyView : white
MyColorFragement : onResume : red
MyColorFragement : onPause : red // (뒤로 가기 버튼 누름)
MyColorFragement : onStop : red
MyColorFragment : onCreateView : white
MyColorFragment : onViewCreated : white
MyColorFragement : onStart : white
MyColorFragement : onDestroyView : red
MyColorFragement : onDestroy : red
MyColorFragement : onDetach : red
MyColorFragement : onResume : white
```

'Red' 프래그먼트로 교체: 'white' 프래그먼트의 View만 파괴되고 ('onDestroyView' 호출) 'red' 프래그먼트가 새로 생성

'뒤로 가기' 버튼: replace 트랜잭션이 "취소(undo)"됩니다. 'red'는 파괴되고 'white'는 View부터 다시 생성

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 프래그먼트 간 통신 실습|[모바일 프로그래밍] 프래그먼트 간 통신 실습]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
