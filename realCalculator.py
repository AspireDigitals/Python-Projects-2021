from tkinter import *


root =Tk()
root.geometry("300x500")
root.title("Real Calculator")

entry = Entry(root)
entry.grid(row=0, columnspan=4)

button_1 = Button(root, text="1", font=("Impact", 15))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", font=("Impact", 15))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", font=("Impact", 15))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", font=("Impact", 15))
button_4.grid(row=1, column=3)

button_5 = Button(root, text="5", font=("Impact", 15))
button_5.grid(row=2, column=0)

button_6 = Button(root, text="6", font=("Impact", 15))
button_6.grid(row=2, column=1)

button_7 = Button(root, text="7", font=("Impact", 15))
button_7.grid(row=2, column=2)

button_8 = Button(root, text="8", font=("Impact", 15))
button_8.grid(row=2, column=3)


button_9 = Button(root, text="9", font=("Impact", 15))
button_9.grid(row=3, column=0)

button_0 = Button(root, text="0", font=("Impact", 15))
button_0.grid(row=3, column=1)

button_add = Button(root, text="+", font=("Impact", 15))
button_add.grid(row=3, column=2)

button_subtract = Button(root, text="-", font=("Impact", 15))
button_subtract.grid(row=3, column=3)

button_multiply = Button(root, text="*", font=("Impact", 15))
button_multiply.grid(row=4, column=0)

button_division = Button(root, text="/", font=("Impact", 15))
button_division.grid(row=4, column=1)

button_clear = Button(root, text="X", font=("Impact", 15))
button_clear.grid(row=4, column=2)

button_equal = Button(root, text="=", font=("Impact", 15))
button_equal.grid(row=4, column=3)





root.mainloop()