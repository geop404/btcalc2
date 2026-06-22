[app]

# Application info
title = BTcalc
package.name = btcalc
package.domain = de.btcalc

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, .buildozer, .github, __pycache__

# Version
version = 1.0

# Requirements – only stdlib + kivy needed
requirements = python3,kivy==2.3.0

# Orientation
orientation = portrait

# No fullscreen (shows Android status bar)
fullscreen = 0

# App icon (optional – put icon.png in project root to use it)
# icon.filename = icon.png

# Presplash (optional)
# presplash.filename = presplash.png

#
# Android settings
#

# Target and minimum Android API
android.api = 34
android.minapi = 21

# NDK version – 25b is stable and well-tested with Kivy 2.3.x
android.ndk = 25b
android.ndk_api = 21

# Store source privately inside the APK
android.private_storage = True

# Automatically accept Android SDK licenses (required for CI)
android.accept_sdk_license = True

# Build for both modern (arm64) and older (armeabi-v7a) devices
android.archs = arm64-v8a, armeabi-v7a

# Allow Android auto-backup
android.allow_backup = True

# No special Android permissions needed (no network, no storage, no camera)
# android.permissions =

# Enable AndroidX (required for modern Android)
android.enable_androidx = True

#
# Python-for-Android
#

# Use the stable release branch
p4a.branch = master

#
# iOS settings (not used)
#
[buildozer]

# Log level: 0 = errors only, 1 = info, 2 = verbose
log_level = 2

# Warn when buildozer is run as root
warn_on_root = 1
