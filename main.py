# @mathew4STAR
# 15-9-2021
# program that checks the attendence
# alter the configuration file
# --------------------

import time
import tkinter as tk
import pyautogui as pg
from PIL import ImageGrab


def gotoscene2():#scene for adding classes
    scene1.forget()
    scene2.pack(fill="both", expand=True)


def gotoscene1():#main scene
    scene2.forget()
    scene1.pack(fill="both", expand=True)


def addclass(classs, div, data):#funciton for adding classes
    newclass = open(("data//classes//" + classs + div + ".txt"), "w+")
    newclass.write(data)
    newclass.close()
    newclassname = open("data//classes.txt", "a")
    newclassname.write("\n" + classs + div)


def check_attendance(configuration, target):#function for checking attendence
    time.sleep(int(configuration[0]))
    floc = configuration[1].split()
    sloc = configuration[2].split()
    firstloc = (int(floc[0]), int(floc[1]))
    secondloc = (int(sloc[0]), int(sloc[1]))
    pg.click(firstloc)
    pg.moveTo(secondloc)
    absent = []
    maybe_present = []
    participant = open("data//classes//" + target + ".txt", "r")
    participants = participant.readlines()
    class_strength = len(participants)
    for i in participants:
        i = i.strip("\n")
        num_of_backspace = len(i.split())
        #print(i)
        pg.write(i)
        image = ImageGrab.grab()
        color = image.getpixel(secondloc)
        if color == (255, 255, 255):
            absent.append(i)
        while num_of_backspace > 0:
            pg.hotkey("ctrl", "shift", "backspace")
            pg.hotkey("backspace")
            num_of_backspace -= 1
            if num_of_backspace == 1:
                image = ImageGrab.grab()
                color = image.getpixel(secondloc)
                if color != (255, 255, 255):
                    maybe_present.append(i)
    maybe_present_ = []
    for i in maybe_present:
        if i in absent:
            #print(i)
            maybe_present_.append(i)
    final = ""
    maybepresent = ""
    thebox.delete("1.0", "end")
    odds = []
    oddsy = ""
    for i in absent:
        if i not in maybe_present:
            odds.append(i)
    final = ",".join(absent)
    maybepresent = ",".join(maybe_present_)
    oddsy = ','.join(odds)
    finalfinal = (
        "STRENGTH: "
        + str(class_strength)
        + "\n"
        + "PRESENT: "
        + str(class_strength - len(odds))
        + "\n"
        + "DEFINETELY ABSENT(FIRST NAME NOT FOUND):"
        + "\n"
        + oddsy
        + "\n"
        + "-----------\n"
        + "MAYBE ABSENT(FULL NAME NOT FOUND):"
        + "\n"
        + final
    )
    thebox.insert(tk.END, finalfinal)

#gui----

root = tk.Tk()
root.geometry("960x540")
root.minsize(960, 540)
root.maxsize(960, 540)
root.title("Attendance bot")
bg = tk.PhotoImage(file="data//image3.png")
scene1 = tk.Canvas(root)
scene1.pack(fill="both", expand=True)
scene1.create_image(0, 0, image=bg, anchor="nw")
classes = open("data//classes.txt")
classess = []
for i in classes:
    classess.append(i.strip("\n"))
config = open("data//config.txt")
configuration = []
for i in config:
    configuration.append(i.strip("\n"))

attendance_btn_img = tk.PhotoImage(file="data//attendance_new.png")
attendance_initiate = tk.Button(
    scene1,
    image=attendance_btn_img,
    borderwidth=0,
    command=lambda: check_attendance(configuration, clicked.get()),
).place(x=110, y=230)


scene2 = tk.Frame(root)
scene2.pack(fill="both", expand=True)
scene_2_button = tk.Button(scene1, text="Edit classes list", command=gotoscene2)
scene_2_button.place(x=840, y=24)

scene_1_button = tk.Button(
    scene2, text="Back", command=gotoscene1, bg="#2D8CFF", fg="white"
)
scene_1_button.pack(anchor=tk.NW)

Heading = tk.Label(
    scene2,
    text="Add a class",
    bg="#2D8CFF",
    fg="white",
    height=2,
    width=10,
    font="bold",
)
Heading.pack()

classlabel = tk.Label(scene2, text="Class: ")
classlabel.place(x=70, y=120)

classentry = tk.Entry(scene2)
classentry.place(x=120, y=120)

sectionlabel = tk.Label(scene2, text="Section: ")
# sectionlabel.pack(anchor=tk.W, pady = (10, 0))
sectionlabel.place(x=70, y=150)

sectionentry = tk.Entry(scene2)
sectionentry.place(x=130, y=150)

children = tk.Text(scene2, height=10, width=70)
children.insert(tk.END, "Please Enter the children of the respective class here")
children.place(x=130, y=215)

classadder = tk.Button(
    scene2,
    text="Add this class",
    command=lambda: addclass(
        classentry.get(), sectionentry.get(), children.get("1.0", "end-1c")
    ),
)
classadder.place(x=420, y=450)

scene2.forget()
clicked = tk.StringVar()
clicked.set("T1")
check_class = tk.OptionMenu(scene1, clicked, *classess)
check_class.config(width=1, height=2, bg="#2D8CFF", fg="white")
check_class.place(x=270, y=230)

thebox = tk.Text(scene1, height=8, width=27)
thebox.insert(tk.END, "Attendance not calculated yet.")
thebox.bind("<Key>", lambda e: "break")
thebox.place(x=542, y=290)


root.mainloop()
