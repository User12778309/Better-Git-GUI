# library/module
from tkinter import filedialog
from tkinter import *

# set class
class File():
    # init variable
    def __init__(self,win):
        self.win = win

    # open file function
    def open_file(self):
        test_file = Label(self.win,text=filedialog.askopenfilename())
        test_file.pack()



