import pygetwindow as gw
import time
import pyautogui
import pyperclip
import datetime
import json

active_window = ""
activity_name = ""
start_time = datetime.datetime.now()
first_time = True

def url_to_name(url):
    string_list = url.split('/')
    if len(string_list) >= 3:
        return string_list[2]
    else:
        return "Unknown"

def format_time_delta(delta):
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return {'hours': hours, 'minutes': minutes, 'seconds': seconds}

data = []

try: 
    while True:
        current_window = gw.getActiveWindow().title

        if "Brave" in active_window:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1) 
            url = pyperclip.paste()       
            print(url)
            current_window = url_to_name(url)

        if current_window != active_window:
            print(active_window)
            activity_name = active_window

            if not first_time:
                end_time = datetime.datetime.now()
                time_spent = end_time - start_time
                formatted_time_spent = format_time_delta(time_spent)
                data.append({
                    activity_name: {
                        'Start time': start_time.strftime("%Y-%m-%d %H:%M:%S"),
                        'End time': end_time.strftime("%Y-%m-%d %H:%M:%S"),
                        'Time spent': formatted_time_spent
                    }
                })
                start_time = datetime.datetime.now()

            first_time = False
            active_window = current_window

        time.sleep(1)

except KeyboardInterrupt:
    with open('activity_log.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
