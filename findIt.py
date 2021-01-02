from pyautogui import *
import pyautogui
import time
import cv2

im2 = pyautogui.screenshot('my_screenshot.png')
# Image searched for must be a PNG and MUST be on the primary monitor...  otherwise, 
# see: https://www.reddit.com/r/learnpython/comments/99fer7/pyautogui_with_multiple_monitors/
# which captures all of the screens but I don't know how that would then 
# map to pixels on an indivdual screen....

looking = 1

while looking:
    stage = pyautogui.locateOnScreen('opening.png', grayscale=True, confidence=.9)
    if stage != None:
        (left, top, width, height) = stage
        looking = False


"""     if  != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I can not see it...")
        time.sleep(0.5)
 """