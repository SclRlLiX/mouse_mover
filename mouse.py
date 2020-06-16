import pyautogui
import time 



starttime=time.time()
while True: 
    pyautogui.moveRel(10,10, duration=2)
    time.sleep(300.0 - ((time.time() - starttime) % 300.0))
