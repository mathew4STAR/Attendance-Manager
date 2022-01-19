import tkinter as tk

print("welcome to setup")

root = tk.Tk()

root.size()

label = tk.Label(root, text="hello welcome to the setup")
label.pack()

start = tk.Button(root, text= "START SETUP", anchor="center")
start.pack()

root.mainloop()