[app]
title = GPA CGPA Calculator
package.name = gpacgpa
package.domain = org.test
source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 0.1

requirements = python3,kivy,kivymd

orientation = portrait
fullscreen = 0

android.archs = armeabi-v7a, arm64-v8a

# Uncomment and set the SDK path to the location your CI installs Android SDK:
android.sdk_path = /opt/android-sdk

# Permissions if needed (e.g. for file access):
# android.permissions = INTERNET

# Buildozer Settings
log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1
