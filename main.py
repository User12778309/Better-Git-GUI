# module/library
from tkinter import *
from tkinter import ttk

# set windows
win = Tk()

# windows geometry
win.geometry("1080x720")

# set/pack option button frames
option_button_frames = Frame(width=1080,height=32.5,bg="red")
option_button_frames.pack()

# do loop
win.mainloop()