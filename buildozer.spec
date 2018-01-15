[app]

# (str) Title of your application
title = PongApp

# (str) Package name
package.name = pongapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.hortonew

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.2

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = kivy

# (str) Supported orientation (one of landscape, portrait or all)
orientation = all

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.2

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1