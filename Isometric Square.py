import subprocess  
import pyautogui
import time
import math

subprocess.Popen([r"C:\Windows\system32\mspaint.exe"])
time.sleep(0.5)
pyautogui.keyDown('alt')
pyautogui.press(' ')
pyautogui.keyUp('alt')
pyautogui.press('x')
pyautogui.click(x=283, y=84)
pyautogui.moveTo(x=200, y=543)
pyautogui.dragRel(0,100,duration=1)
pyautogui.dragRel(100*math.cos(math.radians(30)),100*math.sin(math.radians(30)),duration=1)
pyautogui.dragRel(0,-100,duration=1)
pyautogui.dragRel(-100*math.cos(math.radians(30)),-100*math.sin(math.radians(30)),duration=1) 
pyautogui.dragRel(100*math.cos(math.radians(30)),-100*math.sin(math.radians(30)),duration=1)
pyautogui.dragRel(100*math.cos(math.radians(30)),100*math.sin(math.radians(30)),duration=1)
pyautogui.dragRel(-100*math.cos(math.radians(30)),100*math.sin(math.radians(30)),duration=1)
pyautogui.dragRel(0,100,duration=0)
pyautogui.dragRel(100*math.cos(math.radians(30)),-100*math.sin(math.radians(30)),duration=1)
pyautogui.dragRel(0,-100,duration=1)





