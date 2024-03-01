import pygetwindow as gw
import time

active = ""
while True:
    new = gw.getActiveWindow().title

    if active != new:
        active = new
        print(active)

    time.sleep(10)