[app]
# (str) Title of your application
title = Jusu AI

# (str) Package name
package.name = jusu_ai

# (str) Package domain (reverse DNS style)
package.domain = org.francis.jusu

# (str) Source code directory (relative to buildozer.spec)
source.dir = .

# (str) Application version
version = 0.1

# (str) Application entry point file
# Make sure this matches your main Python file
source.main = main.py

# (list) Application requirements
# Add all your Python dependencies here (Kivy, speechrecognition, pyttsx3, wikipedia, etc.)
requirements = python3,kivy,speechrecognition,pyttsx3,wikipedia

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash image (optional)
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Permissions to request on Android
android.permissions = INTERNET, RECORD_AUDIO

# (int) Android API to target (use 31 or above)
android.api = 33

# (int) Minimum Android API supported
android.minapi = 21
android.build_tools_version = 33.0.0
# (int) Android SDK version to compile against
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 23b

# (bool) Use Android X support libraries
android.use_androidx = True

# (bool) Copy library instead of linking (some fixes)
android.copy_libs = 1

# (str) Presplash color (if no presplash image)
#presplash.color = #FFFFFF

# (list) Include additional Java .jar files here (optional)
#android.add_jars =

# (list) Include additional Android .aar files here (optional)
#android.add_aars =

# (list) Android Java classes to add (optional)
#android.add_src =

# (str) Extra source folders to include (optional)
#source.include_exts = py,png,jpg,kv,atlas

# (bool) Android logcat filters to show (optional)
#android.logcat_filters = *:S python:D

# (int) Number of jobs to use for building (optional)
#jobs = 4

[buildozer]
# (str) Buildozer format (default is "json")
format = ini

# (bool) Whether to clean build when starting (optional)
#clean_build = false
