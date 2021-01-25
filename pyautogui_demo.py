from pyautogui import *
import pyautogui
import keyboard
import time
from sys import stdout
import cv2
import win32api, win32con

def click (x, y):
   win32api.SetCursorPos((x,y))
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
   time.sleep(0.01)
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Image searched for must be a PNG and MUST be on the primary monitor...  otherwise, 
# see: https://www.reddit.com/r/learnpython/comments/99fer7/pyautogui_with_multiple_monitors/
# which captures all of the screens but I don't know how that would then 
# map to pixels on an indivdual screen....

stage = {}
looking = 1

while looking:
    opening_screen = pyautogui.locateOnScreen('opening.png', grayscale=True, confidence=.9)
    if opening_screen != None:
        (stage["left"], stage["top"], stage["width"], stage["height"]) = opening_screen
        looking = False
    else:
        print("I can not find the stage.  Please make sure that ")
        print("http://tanksw.com/piano-tiles is loaded on the primary screen.")
        print("Sleeping for 5 seconds before looking, again...\n\n\n")
        time.sleep(5)

# We know the stage is 1050 tall and each block is 260 tall so we want to find the 
# bottom of the 2nd row since that is where the game starts.
coly = int(stage["top"] + stage["height"] - (stage["height"]/4) - 10)

# The stage is 700 wide so each column is 175 across... so
colx = {}
colx[1] = int(stage["left"] + 5)
colx[2] = int(stage["left"] + 175 + 5)
colx[3] = int(stage["left"] + (175*2) + 5)
colx[4] = int(stage["left"] + (175*3) + 5)

print(colx)
print(coly)

# We also know the "black" color for Rush is 17, 17, 17
# So, let's play...

starty = int(stage["top"] + (stage["height"]/2))
startx = int(stage["left"] + (stage["width"] * .75))

click(startx, starty)


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(colx[1], coly)[0] == 17:
        click(colx[1], coly + 5)
    if pyautogui.pixel(colx[2], coly)[0] == 17:
        click(colx[2], coly + 5)
    if pyautogui.pixel(colx[3], coly)[0] == 17:
        click(colx[3], coly + 5)
    if pyautogui.pixel(colx[4], coly)[0] == 17:
        click(colx[4], coly + 5)
