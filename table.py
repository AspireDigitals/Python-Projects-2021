import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()
frm = Frame(root)
frm.grid(row=0,column=1)

table = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height=5)
table.grid(row=0,column=0)
table.heading(1, text="Firstname")
table.heading(2, text="Lastname")
table.heading(3, text="Staff ID")
table.heading(4, text="Time Reported")


root.mainloop()