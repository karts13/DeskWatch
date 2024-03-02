import pygetwindow as gw
import time
import pyautogui
import pyperclip

active_window = ""

while True:
    current_window = gw.getActiveWindow().title

    if current_window != active_window:
        active_window = current_window
        print(active_window)

        if "Brave" in active_window:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)  # Wait for the clipboard to be updated
            url = pyperclip.paste()       
            print(url)

    time.sleep(10)
