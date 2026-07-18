---
title: "[모바일 프로그래밍] Listener를 이용한 두 프래그먼트 간의 통신"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-11-17
source_url: https://ch010104.tistory.com/189
---

# [모바일 프로그래밍] Listener를 이용한 두 프래그먼트 간의 통신

## 원문

https://ch010104.tistory.com/189

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

텍스트 전달 앱: Fragment A의 EditText에 텍스트를 입력하고 "OK" 버튼을 누르면 해당 텍스트가 Fragment B의 EditText(혹은 TextView)에 표시됩니다. 이 통신은 양방향으로 구현됩니다.

카운터 앱: Fragment A의 "Inc." 버튼을 클릭할 때마다 Fragment B에 있는 "Count" 값이 1씩 증가합니다.

## 원문 기반 학습 정리

### 실습 목표 및 내용

텍스트 전달 앱: Fragment A의 EditText에 텍스트를 입력하고 "OK" 버튼을 누르면 해당 텍스트가 Fragment B의 EditText(혹은 TextView)에 표시됩니다. 이 통신은 양방향으로 구현됩니다.

카운터 앱: Fragment A의 "Inc." 버튼을 클릭할 때마다 Fragment B에 있는 "Count" 값이 1씩 증가합니다.

### 1. 텍스트 전달 앱: Interface를 이용한 통신

이 실습에서는 Interface(인터페이스)를 사용하여 프래그먼트와 액티비티 간의 통신을 구현

데이터 흐름은 [Fragment A] → [Activity] → [Fragment B] 순서

### 1. 송신 측 (Fragment A)

리스너 인터페이스 정의: 데이터를 보내는 Fragment A 내부에 리스너 인터페이스(예: FragmentAListener)를 정의

콜백 메서드 정의: 이 인터페이스에는 데이터를 전달할 콜백 메서드(예: onInputASent(input: CharSequence))가 포함

리스너 등록 (onAttach): onAttach() 콜백에서 context(즉, 호스팅 Activity)가 이 리스너 인터페이스를 구현했는지 확인

구현했다면, 해당 context를 프래그먼트의 리스너 멤버 변수에 저장

구현하지 않았다면, RuntimeException을 발생시켜 개발자에게 알림

데이터 전송 (이벤트 발생 시): 사용자가 버튼을 클릭하면 , 저장된 리스너의 콜백 메서드(예:listener.onInputASent(...))를 호출하여 데이터를 Activity로 전송

### 2. 중재자 (Host Activity)

인터페이스 구현: MainActivity는 Fragment A (그리고 Fragment B)에서 정의한 리스너 인터페이스(예: FragmentAListener)를 implements

콜백 메서드 구현: 인터페이스의 콜백 메서드(예: onInputASent)를 override하여 Fragment A로부터 데이터를 수신

데이터 전달: 수신한 데이터( input )를 Fragment B로 전달해

FragmentManager를 사용해 Fragment B의 인스턴스를 찾음 (예: findFragmentById).

찾아낸 Fragment B 인스턴스의 공개 메서드(예: updateEditText(input))를 호출하여 데이터를 전달

### 3. 레이아웃 (XML)

MainActivity 레이아웃: activity_main.xml 파일에는 Fragment A와 Fragment B를 각각 담을 수 있는 2개의 FragmentContainerView가 포함

Fragment 레이아웃: fragment_a.xml (및 fragment_b.xml)에는 각 프래그먼트의 UI(예: EditText 1개와 Button 1개)가 정의

```text
// MainActivity.kt
package com.cookandroid.fragementcommunicationexcercise

import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.fragment.app.FragmentTransaction
import com.cookandroid.fragementcommunicationexcercise.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity(), FragmentA.FragmentAListner, FragmentB.FragmentBListner {
    private lateinit var bindingMain : ActivityMainBinding
    private lateinit var fragmentA: FragmentA
    private lateinit var fragmentB: FragmentB

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

        fragmentA = FragmentA()
        fragmentB = FragmentB()

        val transaction : FragmentTransaction = supportFragmentManager.beginTransaction()

        transaction.add(R.id.container_a, fragmentA)
        transaction.add(R.id.container_b, fragmentB)
        transaction.addToBackStack(null)
        transaction.commit()
    }

//    fun onRecievedFromFragA(input : CharSequence){
//        Log.i("프래그먼트간 데이터 전달", "Recieved msg: $input")
//        val fragmentManager : androidx.fragment.app.FragmentManager = supportFragmentManager
//        val fragB : FragmentB = fragmentManager.findFragmentById(R.id.container_b) as FragmentB
//        fragB.updateEditText(input)
//    }

    override fun onInputASent(input: CharSequence) {
        Log.i("프래그먼트간 데이터 전달", "Recieved msg: $input")
        val fragmentManager : androidx.fragment.app.FragmentManager = supportFragmentManager
        val fragB : FragmentB = fragmentManager.findFragmentById(R.id.container_b) as FragmentB
        fragB.updateEditText(input)
    }

    override fun onInputBSent(input: CharSequence) {
        Log.i("프래그먼트간 데이터 전달", "Recieved msg: $input")
        val fragmentManager : androidx.fragment.app.FragmentManager = supportFragmentManager
        val fragA : FragmentA = fragmentManager.findFragmentById(R.id.container_a) as FragmentA
        fragA.updateEditText(input)
    }
}
```

```typescript
// FragmentA.kt
package com.cookandroid.fragementcommunicationexcercise

import android.content.Context
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.cookandroid.fragementcommunicationexcercise.databinding.FragmentABinding

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [FragmentA.newInstance] factory method to
 * create an instance of this fragment.
 */
class FragmentA : Fragment() {

    private lateinit var bindingFragmentA : FragmentABinding

    private lateinit var listner : FragmentAListner

    public interface FragmentAListner {
        fun onInputASent(input : CharSequence)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)

        if(context is FragmentAListner){
            listner = context
        } else {
            throw RuntimeException("$context must implement FragmentAListner")
        }

    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        bindingFragmentA = FragmentABinding.inflate(inflater, container, false)
        return bindingFragmentA.root
    }

    public fun updateEditText(newText : CharSequence) {
        bindingFragmentA.editText.setText(newText)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        bindingFragmentA.buttonOk.setOnClickListener(object : View.OnClickListener{
            override fun onClick(v: View?) {
//                val mainActivity : MainActivity = activity as MainActivity
//                mainActivity.onRecievedFromFragA(bindingFragmentA.editText.text)

                listner.onInputASent(bindingFragmentA.editText.text)
                bindingFragmentA.editText.text.clear()
            }
        })
    }


//    companion object {
//        /**
//         * Use this factory method to create a new instance of
//         * this fragment using the provided parameters.
//         *
//         * @param param1 Parameter 1.
//         * @param param2 Parameter 2.
//         * @return A new instance of fragment FragmentA.
//         */
//        // TODO: Rename and change types and number of parameters
//        @JvmStatic
//        fun newInstance(param1: String, param2: String) =
//            FragmentA().apply {
//                arguments = Bundle().apply {
//                    putString(ARG_PARAM1, param1)
//                    putString(ARG_PARAM2, param2)
//                }
//            }
//    }
}
```

```typescript
// FragmentB.kt
package com.cookandroid.fragementcommunicationexcercise

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.cookandroid.fragementcommunicationexcercise.databinding.FragmentBBinding

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [FragmentB.newInstance] factory method to
 * create an instance of this fragment.
 */
class FragmentB : Fragment() {
    private lateinit var bindingFragmentB : FragmentBBinding
    // TODO: Rename and change types of parameters
//    private var param1: String? = null
//    private var param2: String? = null

//    override fun onCreate(savedInstanceState: Bundle?) {
//        super.onCreate(savedInstanceState)
//        arguments?.let {
//            param1 = it.getString(ARG_PARAM1)
//            param2 = it.getString(ARG_PARAM2)
//        }
//    }

    private lateinit var listner : FragmentBListner

    public interface FragmentBListner {
        fun onInputBSent(input : CharSequence)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)

        if(context is FragmentBListner){
            listner = context
        } else {
            throw RuntimeException("$context must implement FragmentAListner")
        }

    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
//        return super.onCreateView(inflater, container, savedInstanceState)
        bindingFragmentB = FragmentBBinding.inflate(layoutInflater)
        return  bindingFragmentB.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        bindingFragmentB.buttonOk.setOnClickListener(object : View.OnClickListener{
            override fun onClick(v: View?) {
//                val mainActivity : MainActivity = activity as MainActivity
//                mainActivity.onRecievedFromFragA(bindingFragmentA.editText.text)

                listner.onInputBSent(bindingFragmentB.editText.text)
                bindingFragmentB.editText.text.clear()
            }
        })
    }

    public fun updateEditText(newText : CharSequence) {
        bindingFragmentB.editText.setText(newText)
    }

//    companion object {
//        /**
//         * Use this factory method to create a new instance of
//         * this fragment using the provided parameters.
//         *
//         * @param param1 Parameter 1.
//         * @param param2 Parameter 2.
//         * @return A new instance of fragment FragmentB.
//         */
//        // TODO: Rename and change types and number of parameters
//        @JvmStatic
//        fun newInstance(param1: String, param2: String) =
//            FragmentB().apply {
//                arguments = Bundle().apply {
//                    putString(ARG_PARAM1, param1)
//                    putString(ARG_PARAM2, param2)
//                }
//            }
//    }
}
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
        android:id="@+id/container_a"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/container_b"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

</LinearLayout>
```

```html
// fragment_a.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="@android:color/holo_green_light"
    android:gravity="center_horizontal"
    tools:context=".FragmentA">

    <!-- TODO: Update blank fragment layout -->
    <EditText
        android:id="@+id/edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>

    <Button
        android:id="@+id/button_ok"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="OK"/>

</LinearLayout>
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

```html
// fragment_b.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center_horizontal"
    android:orientation="vertical"
    android:background="@android:color/holo_blue_bright"
    tools:context=".FragmentB">

    <!-- TODO: Update blank fragment layout -->
    <EditText
        android:id="@+id/edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>

    <Button
        android:id="@+id/button_ok"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="OK"/>

</LinearLayout>
```

### 2. 카운트 앱: Interface를 이용한 통신

실습 목표: Fragment A의 버튼을 클릭하면 Fragment B의 숫자가 1씩 증가하도록 구현

UI 구성:

Fragment A: "Inc." (Increase) 버튼이 있음

Fragment B: "Count: [숫자]" 형태의 텍스트가 있음

구현 방식:

사용자가 Fragment A의 "Inc." 버튼을 클릭

Fragment A는 23~27페이지에서 배운 인터페이스 방식을 사용해 이 클릭 이벤트를 호스팅 Activity로 전달

Activity는 이 이벤트를 수신한 뒤, Fragment B의 참조를 찾아 "카운트를 증가시키라"는 신호(예: 공개 메서드 호출)를 보냄

Fragment B는 신호를 받아 내부의 카운트 변수 값을 1 증가시키고, 화면의 텍스트(TextView)를 갱신

```text
// MainActivity.kt
package com.cookandroid.fragmentexcercise3

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.FragmentTransaction
import com.cookandroid.fragmentexcercise3.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity(), FragmentA.FragmentAListner{

    private lateinit var bindingMain : ActivityMainBinding
    private lateinit var fragmentA: FragmentA
    private lateinit var fragmentB: FragmentB

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        bindingMain = ActivityMainBinding.inflate(layoutInflater)
        setContentView(bindingMain.root)

        // Fragment 초기화
        fragmentA = FragmentA()
        fragmentB = FragmentB()

        // Fragment를 컨테이너에 추가
        val transaction : FragmentTransaction = supportFragmentManager.beginTransaction()
        transaction.add(R.id.container_a, fragmentA)
        transaction.add(R.id.container_b, fragmentB)
        transaction.addToBackStack(null)
        transaction.commit()
    }

    // FragmentA의 버튼 클릭 시 호출되는 메서드
    override fun onButtonClicked() {
        // FragmentB의 카운트를 증가시킴
        fragmentB.incrementCount()
    }
}
```

```typescript
// FragmentA.kt
package com.cookandroid.fragmentexcercise3

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.cookandroid.fragmentexcercise3.databinding.FragmentABinding

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Use the [FragmentA.newInstance] factory method to
 * create an instance of this fragment.
 */
class FragmentA : Fragment() {

    private lateinit var bindingFragmentA : FragmentABinding

    private lateinit var listner : FragmentAListner

    public interface FragmentAListner {
        fun onButtonClicked()
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)

        if(context is FragmentAListner){
            listner = context
        } else {
            throw RuntimeException("$context must implement FragmentAListner")
        }

    }
    // TODO: Rename and change types of parameters
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
        bindingFragmentA = FragmentABinding.inflate(inflater, container, false)

        // 버튼 클릭 리스너 설정
        bindingFragmentA.BtnA.setOnClickListener {
            listner.onButtonClicked()
        }

        return bindingFragmentA.root
    }

    companion object {
        /**
         * Use this factory method to create a new instance of
         * this fragment using the provided parameters.
         *
         * @param param1 Parameter 1.
         * @param param2 Parameter 2.
         * @return A new instance of fragment FragmentA.
         */
        // TODO: Rename and change types and number of parameters
        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            FragmentA().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }
    }
}
```

```text
// FragmentB.kt
package com.cookandroid.fragmentexcercise3

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

class FragmentB : Fragment() {

    private var count = 0
    private lateinit var tvCount: TextView

//    interface FragmentBListner {
//        // FragmentB에서 필요한 경우 MainActivity에 알릴 메서드를 여기에 추가
//    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_b, container, false)

        tvCount = view.findViewById(R.id.tvCount)
        updateCount()

        return view
    }

    // MainActivity에서 호출할 수 있는 public 함수
    fun incrementCount() {
        count++
        updateCount()
    }

    private fun updateCount() {
        tvCount.text = "Count: $count"
    }
}
```

```html
// activity_main.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/container_a"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/container_b"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

</LinearLayout>
```

```html
// fragment_a.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:background="@android:color/holo_green_light"
    tools:context=".FragmentA">

    <!-- TODO: Update blank fragment layout -->
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:textSize="24dp"
        android:text="FragmentA"/>

    <Button
        android:id="@+id/BtnA"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Inc"/>

</LinearLayout>
```

```html
// fragment_b.xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:background="@android:color/holo_blue_bright"
    android:orientation="vertical"
    tools:context=".FragmentB">

    <!-- TODO: Update blank fragment layout -->
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textStyle="bold"
        android:textSize="24dp"
        android:text="FragmentB"/>

    <TextView
        android:id="@+id/tvCount"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="24dp"
        android:text="Count: 0" />

</LinearLayout>
```

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(단방향)|[모바일 프로그래밍] Activity와 Intent(단방향)]]
