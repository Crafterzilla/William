#!/bin/bash

xdotool search --onlyvisible --name "VLC" windowkill
lxterminal -e "vlc http://10.0.0.164:8080/audio.wav --network-caching=1"