[app]

# (str) Title of your application
title = JUSU AI

# (str) Package name
package.name = jusuai

# (str) Package domain (reverse DNS style)
package.domain = org.jusu

# (str) Source files to include (comma-separated extensions)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,speechrecognition,pyttsx3,wikipedia

# (str) Orientation
orientation = portrait

# (str) Android architecture
android.arch = arm64-v8a

# (int) Android API to use
android.api = 31

# (int) Minimum API your app supports
android.minapi = 21

# (int) Android SDK version
android.sdk = 31

# (str) Android NDK version (23b is stable)
android.ndk = 23b

# (list) Permissions required by your app
android.permissions = INTERNET

# (str) Application version
version = 0.1

# (str) The entry point python file of your app
# (set this if your main file is not main.py)
# Here assuming main.py
# entrypoint = main.py

# (bool) Whether to allow the app to be fullscreen
fullscreen = 0

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png
