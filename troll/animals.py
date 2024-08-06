import pyautogui as pg
import time
import keyboard
import sys

time.sleep(10)

txt = open('animals.txt','r')

a = 'Juan is a'

for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
    if keyboard.is_pressed('q'):
        sys.exit()

