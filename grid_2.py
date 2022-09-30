from tkinter import *


root = Tk()
root.geometry("300x500")
root.title("Grid Calculator")

entry = Entry(root, width=46).grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_7 = Button(root, width=5, text="7", font=("Impact", 20)).grid(row=1, column=0)
button_8 = Button(root, width=5, text="8", font=("Impact", 20)).grid(row=1, column=1)
button_9 = Button(root, width=5, text="9", font=("Impact", 20)).grid(row=1, column=2)
button_add = Button(root, width=5, text="+", font=("Impact", 20)).grid(row=1, column=3)

button_4 = Button(root, width=5, text="4", font=("Impact", 20)).grid(row=2, column=0)
button_5 = Button(root, width=5, text="5", font=("Impact", 20)).grid(row=2, column=1)
button_6 = Button(root, width=5, text="6", font=("Impact", 20)).grid(row=2, column=2)
button_minus = Button(root, width=5, text="-", font=("Impact", 20)).grid(row=2, column=3)

button_1 = Button(root, width=5, text="1", font=("Impact", 20)).grid(row=3, column=0)
button_2 = Button(root, width=5, text="2", font=("Impact", 20)).grid(row=3, column=1)
button_3 = Button(root, width=5, text="3", font=("Impact", 20)).grid(row=3, column=2)
button_4 = Button(root, width=5, text="*", font=("Impact", 20)).grid(row=3, column=3)

button_divide = Button(root, width=5, text="/", font=("Impact", 20)).grid(row=4, column=0)
button_0 = Button(root, width=5, text="0", font=("Impact", 20)).grid(row=4, column=1)
button_clear = Button(root, width=11, text="Clear", font=("Impact", 20)).grid(row=4, column=2, columnspan=2)

button_clear = Button(root, width=23, text="=", font=("Impact", 20)).grid(row=5, column=0, columnspan=4)



root.mainloop()