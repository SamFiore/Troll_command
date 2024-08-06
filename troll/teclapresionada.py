import keyboard
import sys
import time

time.sleep(3)
while True: 
    print('T')
    time.sleep(1)
    if keyboard.is_pressed('q'):
        sys.exit()

    


