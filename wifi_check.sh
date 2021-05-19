#/bin/bash
#
# Raspberry Pi 4 WiFi dies daily
# https://www.raspberrypi.org/forums/viewtopic.php?t=271884
#
ping -c 1 8.8.8.8 > /dev/null 2>&1
up=$?

#logger "$0: checking wifi..."

if [ $up != 0 ]
then
	logger "$0: wifi down, restarting"
        sudo ifconfig wlan0 down
        sudo ifconfig wlan0 up
fi
