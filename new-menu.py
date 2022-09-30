from tkinter import *

from click import command



root = Tk()



menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File")
filemenu.add_command(label="New Window")
filemenu.add_command(label="Open File")
filemenu.add_command(label="New Folder")
filemenu.add_separator()
filemenu.add_command(label="New Folder")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="New File")
editmenu.add_command(label="New Window")
editmenu.add_command(label="Open File")
editmenu.add_command(label="New Folder")
editmenu.add_separator()
editmenu.add_command(label="New Folder")
menubar.add_cascade(label="Edit", menu=editmenu)


root.config(menu=menubar)
root.mainloop()