import pyautogui
import keyboard
import webbrowser
import win32api
import win32con
from time import sleep

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

sleep(5)

# START
pyautogui.click(539,387)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(447, 322, (0, 0, 0)):
        click(447, 322)
    if pyautogui.pixelMatchesColor(511, 322, (0, 0, 0)):
        click(511, 322)
    if pyautogui.pixelMatchesColor(571, 322, (0, 0, 0)):
        click(571, 322)
    if pyautogui.pixelMatchesColor(633, 322, (0, 0, 0)):
        click(633, 322)

