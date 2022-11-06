import pyautogui
import time

title = "Cycle 6 (Planet Issues)"
x = input()

x = x.split(', ')

# print(len(x))

# for i in x:
#     print(i)

pyautogui.getWindowsWithTitle(title)[0].maximize()
time.sleep(1)

for i in x:
    pyautogui.press("enter", interval=0.1)
    pyautogui.write(i, interval=0.03)
    pyautogui.press("enter", interval=0.1)
    with pyautogui.hold("shift"):
        pyautogui.press("enter")
    print(i)

pyautogui.getWindowsWithTitle(title)[0].minimize()
