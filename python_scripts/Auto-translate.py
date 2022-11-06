import pyautogui
import time

title1 = "test notion"
title2 = "Google Translate - Google Chrome"

x = int(input())

# x = x.split(', ')

# print(len(x))

# for i in x:
#     print(i)

for i in range(x):
    pyautogui.getWindowsWithTitle(title1)[0].maximize()
    time.sleep(1)
    pyautogui.moveTo(700, 410)
    pyautogui.click(interval=0.1)
    with pyautogui.hold("ctrl"):
        pyautogui.press('a' ,interval=0.05)
        pyautogui.press('c', interval=0.05)
    pyautogui.getWindowsWithTitle(title1)[0].maximize()
    time.sleep(0.1)
    pyautogui.getWindowsWithTitle(title2)[0].maximize()
    time.sleep(0.5)
    pyautogui.moveTo(500, 400)
    pyautogui.click()
    with pyautogui.hold('ctrl'):
        pyautogui.press('a', interval=0.05)
        pyautogui.press('v', interval=0.05)
    time.sleep(1)
    pyautogui.click(1585, 530)
    pyautogui.getWindowsWithTitle(title2)[0].minimize()
    time.sleep(0.1)
    pyautogui.getWindowsWithTitle(title1)[0].maximize()
    time.sleep(0.3)
    # pyautogui.moveTo(970, 410)
    pyautogui.click(970, 410, clicks=2,interval=0.05)
    with pyautogui.hold('ctrl'):
        pyautogui.press('v', interval=0.05)
    pyautogui.press('esc', interval=0.1)
    pyautogui.scroll(-40)

    

# for i in x:
#     pyautogui.press("enter", interval=0.1)
#     pyautogui.write(i, interval=0.03)
#     pyautogui.press("enter", interval=0.1)
#     with pyautogui.hold("shift"):
#         pyautogui.press("enter")
#     print(i)

# pyautogui.getWindowsWithTitle(title)[0].minimize()
