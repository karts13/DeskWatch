import pygetwindow as gw
import time
import pyautogui
import pyperclip
from datetime import datetime, timedelta

active_window = ""
start_time = None

try:
    while True:
        current_window = gw.getActiveWindow().title
        current_time = datetime.now()

        if current_window != active_window:
            if active_window:
                end_time = datetime.now()
                time_spent = end_time - start_time

                print("Activity:", active_window)
                print("Time Spent:", time_spent)
                print("Time Entry Details:")
                print("Start Time:", start_time)
                print("End Time:", end_time)
                print("Total Hours:", time_spent.total_seconds() // 3600)
                print("Total Minutes:", (time_spent.total_seconds() % 3600) // 60)
                print("Total Seconds:", time_spent.total_seconds())
                print("\n")

            active_window = current_window
            start_time = datetime.now()

        if "Brave" in active_window:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            url = pyperclip.paste()
            print("URL:", url)

        time.sleep(10)

except KeyboardInterrupt:
    print("Tracking stopped.")