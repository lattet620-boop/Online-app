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

# SDK settings (GitHub standard လမ်းကြောင်းများကို တိုက်ရိုက် ညွှန်ပြခြင်း)
android.api = 31
android.minapi = 21
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.build_tools_version = 31.0.0
android.accept_sdk_license = 1
