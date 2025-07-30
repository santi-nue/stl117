[app]
# (str) Title of your application
title = MyServer

# (str) Package name
package.name = myserver

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code entry point file
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3

# (str) Main Python file (entry point of your app)
# If your main file is named main.py, this can be left as default
# but you can set it explicitly:
# main.py

# (int) Target Android API level
android.api = 33

# (int) Minimum Android API your app supports
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (str) Android NDK API level
android.ndk_api = 21

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the app should fullscreen
fullscreen = 1

# (str) Permissions to request from the device
android.permissions = INTERNET

# (str) Additional Java classes or jars to add
# android.add_jars = some.jar

# (str) Request to keep the screen on
android.wakelock = True

# (list) List of supported architectures
android.archs = armeabi-v7a

[buildozer]
# (str) Log level: 0 for debug, 1 for info only, etc.
log_level = 2

# (int) Number of threads for compilation
# (default: 1)
# jobs = 4
