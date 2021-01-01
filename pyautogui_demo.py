from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

from sys import stdout

# Pretty good source: https://automatetheboringstuff.com/chapter18/
# https://automatetheboringstuff.com/chapter18/
# https://readthedocs.org/projects/pyautogui/downloads/pdf/latest/

# Works:
pyautogui.displayMousePosition()

"""
# Works:
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardIsnterrupt:
    print('\n')  
"""

def click (x, y):
   win32api.SetCursorPos((x, y))
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
   time.sleep(0.01)
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# Works:
# print(pyautogui.pixel(665, 1225)[0])

while keyboard.is_pressed('q') == False:
    if (pyautogui.pixel(600, 1129)[0]) == 17:
        stdout.flush()
        stdout.write("Matched column 1.")
        click(600, 1129)
    if pyautogui.pixel(700, 1129)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 2.")
        click(700, 1129)
    if pyautogui.pixel(900, 1129)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 3.")
        click(900, 1129)
    if pyautogui.pixel(1000, 1129)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 4.")
        click(1000, 1129)
