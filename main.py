import customtkinter
import os

def clone():
    git_entry_value = git_entry.get()
    os.system("git clone " + git_entry_value)

app = customtkinter.CTk()
app.title("Better Git GUI")
app.geometry("400x150")
app.iconbitmap("assets/icon.ico")

git_entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter your git link ")
git_entry.pack(padx=20, pady=10)

clone_button = customtkinter.CTkButton(app, text="Clone", command=clone)
clone_button.pack(padx=20, pady=20)

app.mainloop()