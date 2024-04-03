#
#   main.py
#
#   Created on: 2024/4/4
#
#   Author: onlydcx
#

from picamera2 import Picamera2
import time

camera = Picamera2()
camera.start()

time.sleep(1)

camera.capture_file("cap.jpg")
