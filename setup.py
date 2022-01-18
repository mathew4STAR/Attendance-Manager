from ctypes import alignment
import tkinter as tk
from turtle import color


print("welcome to setup")

root = tk.Tk()

root.size((1920, 1080))

label = tk.Label(root, text="hello welcome to the setup")
label.pack()

start = tk.Button(root, text= "START SETUP", anchor="center")
start.pack()

root.mainloop()