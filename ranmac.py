#!/usr/bin/python
import os
import time
while True:
	print(os.popen("service network-manager stop && ifconfig wlan0 down && macchanger wlan0 -r && ifconfig wlan0 up && service network-manager start").read())
    	time.sleep(10)
