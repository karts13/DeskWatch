import pygetwindow as gw
import time
import pyautogui
import pyperclip
import datetime

active_window = ""
activity_name = ""
start_time = datetime.datetime.now()
first_time = True

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]

try: 
    while True:
        current_window = gw.getActiveWindow().title

        if "Brave" in active_window:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)  # Wait for the clipboard to be updated
            url = pyperclip.paste()       
            print(url)
            current_window = url_to_name(url)

        if current_window != active_window:
            print(active_window)
            activity_name = active_window

            if not first_time:
                end_time = datetime.datetime.now()
                time_spent = end_time - start_time
                print(f"Time spent on {activity_name}: {time_spent}")
                start_time = datetime.datetime.now()

            first_time = False
            active_window = current_window

        time.sleep(1)

except KeyboardInterrupt:
    pass
