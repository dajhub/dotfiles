#!/bin/sh
/usr/bin/v4l2-ctl -d /dev/video0 --set-fmt-video width=1920,height=1080,pixelformat=1
/usr/bin/v4l2-ctl -d /dev/video0 --set-parm 30
#/usr/bin/v4l2-ctl -d /dev/video0 --set-ctrl zoom_absolute=150
#/usr/bin/v4l2-ctl -d /dev/video0 --set-ctrl tilt_absolute=10800
/usr/bin/v4l2-ctl -d /dev/video0 --set-ctrl pan_absolute=-10800
/usr/bin/v4l2-ctl -d /dev/video0 --set-ctrl sharpness=150
/usr/bin/v4l2-ctl -d /dev/video0 --set-ctrl exposure_auto_priority=0
