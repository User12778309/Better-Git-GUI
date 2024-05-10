# library/module
from tkinter import filedialog
from tkinter import *
from pathlib import Path

# set class
class File():
    # init variable
    def __init__(self,win):
        self.win = win

    # open file function
    def open_file(self):
        self.file_open = filedialog.askopenfilename()
        Label(self.win,text=Path(self.file_open).name).pack()
        print(self.file_open.split(".")[1])




