#Label for text display
#Button for command
#Entry for input
#Checkbutton for check boxes

from tkinter import *
from datetime import datetime

container = Tk()
container.geometry("300x450")
container.title("Age Calculator")

def myAge():
    if yearEntry.get():
        label = datetime.now().year - int(yearEntry.get())
        label = Label(container, text=label)
        label.pack()


heading = Label(container, text="AGE CALCULATOR")
heading.pack(pady=20)


year_of_birth = Label(container, text="Enter your year of birth below:")
year_of_birth.pack(pady=20)

yearEntry = Entry(container, font="Helvetica")
yearEntry.pack(pady=10)

button = Button(container, text="Calculate Age !", command=(myAge))
button.pack(pady=20)




container.mainloop()