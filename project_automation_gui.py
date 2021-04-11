import os
import tkinter as tk
from time import sleep

def create():
	os.mkdir(name.get())
	os.chdir(name.get())
	open("ReadMe.md", "w")
	open("ReadMe.md", "w").close()
	open(file.get(), "w")
	open(file.get(), "w").close()
	exit()

#    Window
window = tk.Tk()
name=tk.StringVar(window)
file=tk.StringVar(window)
window.title("Create Project")
window.geometry("200x200")

#    Label
title = tk.Label(text="New Project", font=(20))
title.grid(column=3, row = 0, padx=50, pady=10)

#	text Inputs
pname = tk.Label(text="Project Name")
pname.grid(column=3, row=1)
ProjectName = tk.Entry(window, textvariable=name)
ProjectName.grid(column=3, row=2, pady=5)

pname = tk.Label(text="File Name (with extension)")
pname.grid(column=3, row=3)
ProjectName = tk.Entry(window, textvariable=file)
ProjectName.grid(column=3, row=4, pady=5)

#  Button
button1 = tk.Button(text="Create", bg="grey", command=create)
button1.grid(column=3, row=5, pady=5)


window.mainloop()