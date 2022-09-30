from tkinter import *
import os
from tkinter import filedialog


def donothing():
    x = 0

def newFile():
    text.delete(1.0, END)


def openFile():
    oF = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open As", filetypes=(("File Types", "*.txt"), ("All Files", "*.*")))
    with open(oF, "r") as f:
        text.insert(1.0, f.read())


def saveFile():
    sF = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save As", filetypes=(("File Types", "*.txt"), ("All Files", "*.*")))
    t = text.get(1.0, END)
    with open(sF, "w+") as f:
        f.write(t)


def save():
    t = text.get(1.0, END)
    text.insert(END, t)

def setLayout():
    text.config(width=34, height=70)

def openWindow():

        
    
    nw = Tk()

    def newFile():
        text.delete(1.0, END)


    def openFile():
        oF = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open As", filetypes=(("File Types", "*.txt"), ("All Files", "*.*")))
        with open(oF, "r") as f:
            text.insert(1.0, f.read())


    def saveFile():
        sF = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save As", filetypes=(("File Types", "*.txt"), ("All Files", "*.*")))
        t = text.get(1.0, END)
        with open(sF, "w+") as f:
            f.write(t)


    def save():
        t = text.get(1.0, END)
        text.insert(END, t)
        image = PhotoImage(file="image.png")
        nw.iconphoto(True, image)

    def setLayout():
        text.config(width=34, height=170)

    menubar = Menu(nw)

    nw.title("Wordpad")

    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="New File", command=newFile)
    filemenu.add_command(label="Open File", command=openFile)
    filemenu.add_command(label="Save File As", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="New Window", command=openWindow)
    filemenu.add_command(label="Exit Wordpad", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)


    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo Changes", command=donothing)
    editmenu.add_command(label="Redo Changes", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Copy File", command=donothing)
    editmenu.add_command(label="Cut File", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Color", command=root.quit)
    menubar.add_cascade(label="Edit", menu=editmenu)




    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    nw.config(menu=menubar)

    text = Text(nw, font=("Nexa Light", 12))
    text.pack()

    nw.mainloop()





root = Tk()
image = PhotoImage(file="image.png")
root.iconphoto(True, image)

menubar = Menu(root)

root.title("Wordpad")

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save File As", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="New Window", command=openWindow)
filemenu.add_command(label="Layout", command=setLayout)
filemenu.add_command(label="Exit Wordpad", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo Changes", command=donothing)
editmenu.add_command(label="Redo Changes", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Copy File", command=donothing)
editmenu.add_command(label="Cut File", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Color", command=root.quit)
menubar.add_cascade(label="Edit", menu=editmenu)




helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


allfonts = [
    "Helvetica",
    "Harabara",
    "Georgia"
]

clicked = StringVar()
clicked.set(allfonts[0])
fonts = OptionMenu(root, clicked, *allfonts)
fonts.grid(row=0, column=0)


text = Text(root, font=("Nexa Light", 12), padx=40)
text.grid(row=1, column=1)




root.mainloop()