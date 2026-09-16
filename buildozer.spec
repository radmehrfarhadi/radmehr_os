[app]

title = Radmehr OS
package.name = radmehros
package.domain = org.radmehr

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,hash,ico

version = 1.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
