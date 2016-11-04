#!/bin/bash
xinput set-prop 'FT5406 memory based driver' 'Evdev Axes Swap' 1
xinput --set-prop 'FT5406 memory based driver' 'Evdev Axis Inversion' 0 1
sudo ifdown wlan0
sudo create_ap --no-virt -n -g 192.168.11.22 wlan0 zmj001 66341703