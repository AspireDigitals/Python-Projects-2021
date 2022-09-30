#tkinter
#importing the tkinter module
from tkinter import *

room = Tk()

name = Label(room, text="Hello World")
name.pack()

my_input = Entry(room, font=("Helvetica", 20))
my_input.pack()

My_checkbox = Checkbutton(room)
My_checkbox.pack()

button = Button(room, text="my button")
button.pack()

room.mainloop()