﻿# DeskWatch

## Description

> DeskWatch is a Python-based productivity program that helps users track and evaluate your computer usage patterns. DeskWatch gives users insights into everyday activities by analyzing the amount of time they spend on various websites and applications. This helps see patterns, manage time more effectively, and increase productivity.

## How to Use This Code

> 1. Clone this Repository:
> ```
> https://github.com/karts13/DeskWatch.git
> cd deskwatch
> ```
> 2. Install required Python Libraries:
> ```
> pip install pygetwindow pyautogui pyperclip
> ```
> 3. Do the necessary [customizations](https://github.com/karts13/DeskWatch/blob/main/README.md#customization).
> 4. Run deskwatch.py in your terminal:
> ```
> python deskwatch.py
> ```
> 5. DeskWatch will continuously monitor your activity in the background.
> 6. To stop DeskWatch and save activity logs, press `Ctrl + C.`
> 7. Activity logs will be saved in activity_log.json in the project directory.

## Customization

> 1. **Provide Multi-Browser Support:** At the moment, [deskwatch.py](https://github.com/karts13/DeskWatch/blob/main/deskwatch.py) only pulls URLs from the Brave browser. To make the code work with other browsers like Edge, Firefox, or Chrome, you could extend it. 
> 2. **Custom Activity Logging Format:** The result is initially displayed as [Output](https://github.com/karts13/DeskWatch/blob/main/README.md#sample-outputs),  you can modify the structure of the activity logs stored in the `activity_log.json` file.
> 3. **Multiple Platform Support:** Currently, this code is limited to Windows; in order to run it on Linux or Mac, additional libraries must be installed. (Refer [Python Docs](https://www.python.org/doc/)).

## Sample Outputs
> ![deskwatch.py](https://github.com/karts13/DeskWatch/assets/126340629/cd3366ec-6fd2-44b2-b740-35bbff46f3c6)
> :--:
> <b>Text Editor (deskwatch.py)</b>
>
> ![activity.py](https://github.com/karts13/DeskWatch/assets/126340629/2f515bf9-2444-4295-a4e7-2fc88b676b7d)
> :--:
> <b>Text Editor (activity.py)</b>
>
> ![activity_log.json](https://github.com/karts13/DeskWatch/assets/126340629/d81a0fc1-1fb5-4ced-b729-7a8637a47e2f)
> :--:
> <b>Output (activity_log.json)</b>

## Contribution
> If you find any issues or have suggestions for improvement, or bug fixes, please open an issue or create a pull request.