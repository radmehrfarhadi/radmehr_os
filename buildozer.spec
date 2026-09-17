[app]

title = Radmehr OS
package.name = radmehros
package.domain = org.radmehr

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,hash,ico

version = 1.0

# Android uses android_modules/requests.py, a small urllib-based compatibility
# shim. Keeping requests/charset-normalizer out of the APK avoids the
# python-for-android Python 3.14 wheel compatibility failure.
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
