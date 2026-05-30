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

# --- ဒီအပိုင်းကို အသစ်တိုးပြီး ဖြည့်စွက်ပေးထားပါတယ် ဆရာ ---
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0
