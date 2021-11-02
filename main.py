#star-code6 
#program that checks the attendence
#alter the configuration file
#--------------------
import pyautogui as pg
from PIL import Image, ImageGrab
import time 

time.sleep(1)
strength = 31
firstloc = (1751, 118)
secondloc = (1893, 157)
pg.click(firstloc)
pg.moveTo(secondloc)
absent = []
participants = open("kids.txt")
for i in participants:
    i = i.strip("\n")
    pg.write(i)
    image = ImageGrab.grab()
    color = image.getpixel(secondloc)
    if color == (255, 255, 255):
        absent.append(i)
    pg.hotkey('ctrl', 'shift', 'backspace')
    
print("STRENCTH:31")
print("PRESENT:", strength - len(absent))
print("ABSENT:", len(absent))
print("Absentees")
print(absent)
input('Press enter to close the application')
