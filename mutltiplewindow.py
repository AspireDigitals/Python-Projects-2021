from tkinter import *
from tkinter.ttk import Treeview

root = Tk()
root.geometry("300x400")

def openWindow():
    container = Tk()
    container.geometry("300x400")
    container.title("New Container")
    openBtn = Button(container, text="open new window", command=openWindow)
    openBtn.pack()

    container.mainloop()

openBtn = Button(root, text="open new window", command=openWindow)
openBtn.pack()

tv = Treeview(root, columns=(1,2,3), show="headings", height=5)
tv.pack()

tv.heading(1, text="First Name")
tv.heading(2, text="last Name")
tv.heading(2, text="Address")

root.mainloop()