[app]
title = UBT Korea Exam Q,M,G Shop
package.name = ubtkoreaqmgshop
package.domain = com.keec13
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius

# Android ဆက်တင်များ
orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
android.accept_sdk_license = 1

# SDK settings ကို ပုံမှန် အရင်အတိုင်း ပြန်ထားခြင်း
android.api = 31
android.minapi = 21
android.build_tools_version = 31.0.0
