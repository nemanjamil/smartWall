#! /bin/bash
export DISPLAY=:0
chromium-browser 127.0.0.1:5000 \
    --kiosk \
    --incognito \
    --disable-infobars \
    --aggressive-cache-discard \
    --disable-notifications \
    --disable-remote-fonts \
    --disable-reading-from-canvas \
    --disable-remote-playback-api \
    --disable-shared-workers \
    --disable-voice-input \
    --enable-aggressive-domstorage-flushing \
    --enable-offline-auto-reload \
    --enable-ipv6