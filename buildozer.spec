[app]

title = Radmehr OS
package.name = radmehros
package.domain = org.radmehr

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,hash,ico

version = 1.0

# Android uses android_modules/requests.py, a small urllib-based compatibility
# shim. python-for-android's SDL2/Kivy stack still resolves requests internally.
# Pin charset-normalizer to a universal pure-Python wheel; newer 3.5.x Android
# cp314 wheels are currently rejected by p4a's install stage.
requirements = python3,kivy,charset-normalizer==3.4.3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
