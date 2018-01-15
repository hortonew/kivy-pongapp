#!/bin/bash

# Remove old install
adb uninstall com.hortonew.pongapp

# New Build - will complain apk doesn't exist
buildozer android debug

# Copy to bin directory
cp .buildozer/android/platform/build/dists/pongapp/bin/PongApp-0.2-debug.apk bin/

# Push to device
adb install bin/PongApp-0.2-debug.apk bin/
