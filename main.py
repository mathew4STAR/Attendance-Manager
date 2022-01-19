#@mathew4STAR
#15-9-2021
#program that checks the attendence
#alter the configuration file
#--------------------

import pyautogui as pg
from PIL import Image, ImageGrab
import tkinter as tk

def addclass(classs, div, data):
    f = open(("data//" + classs + div + ".txt"), "w+")
    f.write(data)
    f.close()

def check_attendance(configuration, target):
    #time.sleep(int(configuration[0]))
    strength = int(configuration[1])
    floc = configuration[2].split()
    sloc = configuration[3].split()
    firstloc = (int(floc[0]), int(floc[1]))
    secondloc = (int(sloc[0]), int(sloc[1]))
    pg.click(firstloc)
    pg.moveTo(secondloc)
    absent = []
    participants = open("data//" + target + ".txt")
    for i in participants:
        i = i.strip("\n")
        pg.write(i)
        image = ImageGrab.grab()
        color = image.getpixel(secondloc)
        if color == (255, 255, 255):
            absent.append(i)
        pg.hotkey('ctrl', 'shift', 'backspace')
        
    print("STRENCTH:", strength)
    print("PRESENT:", strength - len(absent))
    print("ABSENT:", len(absent))
    print("Absentees")
    print(absent)
    final = ""
    for i in absent:
        final = final + i + " "
    children.insert(tk.END, final)
    

root = tk.Tk()
intro = tk.Label(root, text="hello welcome to this program")
intro.pack()
config = open("data//config.txt")
configuration = []
for i in config:
    configuration.append(i.strip("\n"))

check_class = tk.Entry(root)
check_class.insert(0, "Please enter the class:")
check_class.pack()

attenddence_initiate = tk.Button(root, text= "START PROCESS", command= lambda: check_attendance(configuration, check_class.get()))
attenddence_initiate.pack()

theclass = tk.Entry(root)
theclass.insert(0, "Please enter the class if you want to add a new class to the database")
thesection = tk.Entry(root)
thesection.insert(0, "Please enter the section if you want to add a new class to the database")
children = tk.Text(root, height=20, width=100)
theclass.pack()
thesection.pack()
children.pack()

classadder = tk.Button(root, text= "Add a class", command= lambda: addclass(theclass.get(), thesection.get(), children.get("1.0", "end-1c")))
classadder.pack()
root.mainloop()