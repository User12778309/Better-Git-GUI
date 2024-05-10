# module/library
from tkinter import *

# set windows
win = Tk()
win.title("File extra directory")
win.iconbitmap("assets/icon.ico")
win.config(bg="#D5D5D5")

# windows geometry
win.geometry("1080x720")

# set/pack option button frames
option_button_frames = Frame(width=1080,height=32.5,bg="grey")
option_button_frames.pack()

# set "File" option button
file_option_button = Menubutton(option_button_frames,text="File",width=42,bg="grey",bd=3,relief=RAISED,cursor="hand2",activebackground="orange",activeforeground="black")
file_option_button.pack(side=LEFT)
file_unfold_menu = Menu(file_option_button)
file_unfold_menu.add_command(label= str(" " * 29) + "Open file" + str(" " * 29))
file_option_button.configure(menu=file_unfold_menu)

# set "Edit" option button
edit_option_button = Menubutton(option_button_frames,text="Edit",width=42,bg="grey",bd=3,relief=RAISED,cursor="hand2",activebackground="orange",activeforeground="black")
edit_option_button.pack(side=LEFT)

# set "Navigate" option button
navigate_option_button = Menubutton(option_button_frames,text="Navigate",width=42,bg="grey",bd=3,relief=RAISED,cursor="hand2",activebackground="orange",activeforeground="black")
navigate_option_button.pack(side=LEFT)

# set "Help" option button
help_option_button = Menubutton(option_button_frames,text="Help",width=42,bg="grey",bd=3,relief=RAISED,cursor="hand2",activebackground="orange",activeforeground="black")
help_option_button.pack(side=LEFT)

# do loop
win.mainloop()