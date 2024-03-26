import pygetwindow as window_manager
import pyautogui
import datetime
import json
import activity

active_window_title = ""
activity_name = ""
start_time = datetime.datetime.now()
first_iteration = True

activity_logs = {}

try: 
    while True:
        current_window_title = window_manager.getActiveWindow().title

        if "Brave" in current_window_title:
            url = activity.get_current_url()
            current_window_title = activity.extract_domain_name(url)

        if current_window_title != active_window_title:
            if active_window_title:
                start_time = activity.extract_activity_logs(activity_logs, active_window_title, activity_name, start_time)

            active_window_title = current_window_title
            activity_name = active_window_title

        pyautogui.sleep(1)  # Use pyautogui.sleep instead of time.sleep for consistency

except KeyboardInterrupt:
    with open('activity_log.json', 'w') as json_file:
        json.dump(activity_logs, json_file, indent=4)