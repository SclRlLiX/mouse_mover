import pyautogui
import time 

starttime=time.time()
while True: 
    pyautogui.moveRel(10,10, duration=2)
    print("moving now")
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
