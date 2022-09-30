from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

wrapper_1 = LabelFrame(root)
wrapper_2 = LabelFrame(root)

mycanvas = Canvas(wrapper_1)
mycanvas.pack(side=LEFT)

yscroll = ttk.Scrollbar(wrapper_1, orient="vertical", command=mycanvas.yview)
yscroll.pack(side=RIGHT, fill="y")

myframe = Frame(mycanvas)

wrapper_1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper_2.pack(fill="both", expand="yes", padx=10, pady=10)
root.mainloop()