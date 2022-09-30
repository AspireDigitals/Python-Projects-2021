from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Grid")

button_1 = Button(root, text="1")
button_1.grid(row=0, column=0)

button_2 = Button(root, text="2")
button_2.grid(row=1, column=0)

root.mainloop()