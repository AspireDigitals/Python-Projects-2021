import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("800x500")
root.title("Text Editor")

def newDoc():
    txt.delete("1.0", END)


def saveDoc():
    fd = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    t = txt.get("1.0", END)
    with open(fd, "w+") as f:
        f.write(t)
    print("Saved")

def openDoc():
    fd = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(fd, "r") as f:
        txt.insert("1.0", f.read())

def editDoc():
    fd = filedialog.aske

menubar = Menu(root)
fmenu = Menu(menubar, tearoff=0)
fmenu.add_command(label="New", command=(newDoc))
fmenu.add_command(label="Save", command=(saveDoc))
fmenu.add_command(label="Open", command=(openDoc))
fmenu.add_separator()
fmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fmenu)

emenu = Menu(menubar, tearoff=0)
emenu.add_command(label="Undo", command=lambda: print("Undone"))
emenu.add_command(label="Redo", command=lambda: print("Redid"))
emenu.add_separator()
emenu.add_command(label="Copy", command=lambda: print("Copied"))
emenu.add_command(label="Cut", command=lambda: print("Cut"))
emenu.add_command(label="Paste", command=lambda: print("Pasted"))
menubar.add_cascade(label="Edit", menu=emenu)


root.config(menu=menubar)
txt = Text(root, font=("Helvetica", 15))
txt.pack()

root.mainloop()