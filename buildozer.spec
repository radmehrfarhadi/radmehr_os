[app]

title = Radmehr OS
package.name = radmehros
package.domain = org.radmehr

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,hash,ico

version = 1.0

# charset-normalizer 3.x currently produces an Android wheel that pip rejects
# in python-for-android's Python 3.14 target environment. 2.1.1 is pure Python
# and is compatible with requests on Android.
requirements = python3,kivy,requests,charset-normalizer==2.1.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
