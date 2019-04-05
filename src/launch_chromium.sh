#! /bin/bash
export DISPLAY=:0
chromium-browser 192.168.0.24:5000/ --kiosk --disable-infobars --aggressive-cache-discard --disable-notifications --disable-remote-fonts --disable-reading-from-canvas --disable-remote-playback-api --disable-shared-workers --disable-voice-input --enable-aggressive-domstorage-flushing 