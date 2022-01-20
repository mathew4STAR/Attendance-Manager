#@mathew4STAR
#15-9-2021
#program that checks the attendence
#alter the configuration file
#--------------------

import pyautogui as pg
from PIL import ImageGrab
import tkinter as tk
import time
import tkinter as tk


class LineNumbers(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)

        self.text_widget = text_widget
        self.text_widget.bind('<KeyPress>', self.on_key_press)

        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_press(self, event=None):
        final_index = str(self.text_widget.index(tk.END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))

        self.configure(state='normal', width=width)
        self.delete(1.0, tk.END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')


def addclass(classs, div, data):
    f = open(("data//" + classs + div + ".txt"), "w+")
    f.write(data)
    f.close()

def check_attendance(configuration, target):
    time.sleep(int(configuration[0]))
    strength = int(configuration[1])
    floc = configuration[2].split()
    sloc = configuration[3].split()
    firstloc = (int(floc[0]), int(floc[1]))
    secondloc = (int(sloc[0]), int(sloc[1]))
    pg.click(firstloc)
    pg.moveTo(secondloc)
    absent = []
    participants = open("data//classes" + target + ".txt")
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
root.geometry("960x540")
root.minsize(960, 540)
root.maxsize(960, 540)
bg = tk.PhotoImage(file = "data//image2.png")
scene1 = tk.Canvas(root)
scene1.pack(fill="both", expand = True)
scene1.create_image(0, 0, image = bg, anchor = "nw")
config = open("data//config.txt")
configuration = []
for i in config:
    configuration.append(i.strip("\n"))


attenddence_initiate = tk.Button(scene1, text= "START PROCESS",height=2, width=20 ,command= lambda: check_attendance(configuration, check_class.get())).place(x =100, y =210)

scene_2_button = tk.Button(scene1, text = "Edit classes list")
scene_2_button.place(x = 840, y = 24)

clicked = tk.StringVar()
clicked.set("10A")
check_class = tk.OptionMenu(scene1, clicked, "9B", "7D", "10B")
check_class.config(width=1, height = 2)
check_class.place(x = 280, y = 210)
#check_class.insert(0, "Please enter the class:")



#theclass = tk.Entry(scene1)
#theclass.insert(0, "Please enter the class if you want to add a new class to the database")
#thesection = tk.Entry(scene1)
#thesection.insert(0, "Please enter the section if you want to add a new class to the database")
#children = tk.Text(scene1, height=20, width=100)
#theclass.pack()
#thesection.pack()
#children.pack(expand= 1)

#classadder = tk.Button(root, text= "Add a class", command= lambda: addclass(theclass.get(), thesection.get(), children.get("1.0", "end-1c")))
#classadder.pack()

root.mainloop()