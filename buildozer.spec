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

# SDK Settings (ဗားရှင်းဟောင်း တည်ငြိမ်သော ဆက်တင်များ)
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools_version = 31.0.0
android.accept_sdk_license = 1
