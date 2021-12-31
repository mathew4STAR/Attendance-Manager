import time 
import pyautogui as pag

#change the buffer time in case you need more, or less
buffer = 5 

time.sleep(buffer)

locx, locy = pag.position()

print(str(locx) + ' ' + str(locy))