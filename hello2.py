#Label for text display
#Button for command
#Entry for input
#Checkbutton for check boxes

from tkinter import *

container = Tk()
container.geometry("300x450")
container.title("Age Calculator")

def add():
    if nameEntry.get() and yearEntry.get():
        label = int(nameEntry.get()) + int(yearEntry.get())
        label = Label(container, text=label)
        label.pack()

def subtract():
    if nameEntry.get() and yearEntry.get():
        label = int(nameEntry.get()) - int(yearEntry.get())
        label = Label(container, text=label)
        label.pack()

    
def divide():
    if nameEntry.get() and yearEntry.get():
        label = int(nameEntry.get()) / int(yearEntry.get())
        label = Label(container, text=label)
        label.pack()

def multiply():
    if nameEntry.get() and yearEntry.get():
        label = int(nameEntry.get()) * int(yearEntry.get())
        label = Label(container, text=label)
        label.pack()


heading = Label(container, text="AGE CALCULATOR")
heading.pack(pady=20)

name = Label(container, text="Enter current year below:")
name.pack(pady=20)

nameEntry = Entry(container, font="Helvetica")
nameEntry.pack(pady=10)

year_of_birth = Label(container, text="Enter your year of birth below:")
year_of_birth.pack(pady=20)

yearEntry = Entry(container, font="Helvetica")
yearEntry.pack(pady=10)

additionbutton = Button(container, text="+", command=(add))
additionbutton.pack(pady=5)

subtractionbutton = Button(container, text="-", command=(subtract))
subtractionbutton.pack(pady=5)

divisionbutton = Button(container, text="/", command=(divide))
divisionbutton.pack(pady=5)

multiplicationbutton = Button(container, text="*", command=(multiply))
multiplicationbutton.pack(pady=5)




container.mainloop()