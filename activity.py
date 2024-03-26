import datetime
import pyautogui
import pyperclip

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

def get_current_url():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.sleep(1)
    return pyperclip.paste()

def extract_activity_logs(activity_logs, active_window_title, activity_name, start_time):
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
    return end_time