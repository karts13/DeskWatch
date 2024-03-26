import pygetwindow as window_manager
import time
import pyautogui
import pyperclip
import datetime
import json

active_window_title = ""
activity_name = ""
start_time = datetime.datetime.now()
first_iteration = True

def extract_domain_name(url):
    url_segments = url.split('/')
    if len(url_segments) >= 3:
        return url_segments[2]
    else:
        return "Unknown"

def format_time_delta(delta):
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return {'hours': hours, 'minutes': minutes, 'seconds': seconds}

activity_logs = {}

try: 
    while True:
        current_window_title = window_manager.getActiveWindow().title

        if "Brave" in current_window_title:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1) 
            url = pyperclip.paste()       
            print(url)
            current_window_title = extract_domain_name(url)

        if current_window_title != active_window_title:
            if active_window_title:
                end_time = datetime.datetime.now()
                time_spent = end_time - start_time
                formatted_time_spent = format_time_delta(time_spent)
                if activity_name in activity_logs:
                    instance_number = len(activity_logs[activity_name]) + 1
                    activity_name_with_instance = f"{activity_name} Instance {instance_number}"
                else:
                    activity_name_with_instance = activity_name
                activity_logs.setdefault(activity_name, []).append({
                    'Start time': start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'End time': end_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'Time spent': formatted_time_spent
                })
                start_time = datetime.datetime.now()

            active_window_title = current_window_title
            activity_name = active_window_title

        time.sleep(1)

except KeyboardInterrupt:
    with open('activity_log.json', 'w') as json_file:
        json.dump(activity_logs, json_file, indent=4)