# module/library
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

# create windows
win = Tk()

# set windows size
win.geometry("400x600")
win.maxsize(400,600)
win.minsize(400,600)

# transparent parametre

# load image
add_button_image = PhotoImage(file = "assets/add button.png",)

# create add_button
add_button = Button(image=add_button_image)

# pack add_button
add_button.pack(side=BOTTOM)

# do loop
win.mainloop()