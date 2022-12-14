from tkinter import *


def donothing():
   x = 0
   
root = Tk()

menubar = Menu(root)

root.title("Menu")

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Redo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Edit", menu=editmenu)




helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()