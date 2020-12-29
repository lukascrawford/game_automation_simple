from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

from sys import stdout


#pyautogui.displayMousePosition()

def click (x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(665, 1225)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 1.")
        click(665, 1225)
    if pyautogui.pixel(800, 1225)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 2.")
        click(888, 1225)
    if pyautogui.pixel(1191, 1225)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 3.")
        click(1191, 1225)
    if pyautogui.pixel(1272, 1225)[0] == 17:
        stdout.flush()
        stdout.write("Matched column 4.")
        click(1272, 1225)
