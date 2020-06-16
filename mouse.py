from pynput.mouse import Button, Controller 
import time 

mouse = Controller()

starttime=time.time()
changePosition = 1
while True: 
    if changePosition == 1: 
        mouse.position = (1000,1000)
        changePosition = 0
    elif changePosition == 0: 
        mouse.position = (500,500)
        changePosition = 1
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
