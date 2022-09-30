from tkinter import *

root = Tk()
root.title("CALCULATOR")

root.resizable(width=0, height=0)


def myClick(number):
    first_Number = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(first_Number) + str(number))


def clearScreen():
    entry.delete(0, END)

def addNumbers():
    first_number = entry.get()
    global fm
    global math
    math = "addition"
    fm = int(first_number)
    entry.delete(0, END)

def subtractNumbers():
    first_number = entry.get()
    global fm
    global math
    math = "subtraction"
    fm = int(first_number)
    entry.delete(0, END)

def divideNumbers():
    first_number = entry.get()
    global fm
    global math
    math = "division"
    fm = int(first_number)
    entry.delete(0, END)

def multiplyNumbers():
    first_number = entry.get()
    global fm
    global math
    math = "multiplication"
    fm = int(first_number)
    entry.delete(0, END)

def equalTo():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, fm + int(second_number))
    if math == "subtraction":
        entry.insert(0, fm - int(second_number))


logo = PhotoImage(file="icon.png")
root.iconphoto(True, logo)


entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)

#designing buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: myClick(1), bg="orange", fg="white")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: myClick(2), bg="orange", fg="white")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: myClick(3), bg="orange", fg="white")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: myClick(4), bg="orange", fg="white")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: myClick(5), bg="orange", fg="white")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: myClick(6), bg="orange", fg="white")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: myClick(7), bg="orange", fg="white")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: myClick(8), bg="orange", fg="white")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: myClick(9), bg="orange", fg="white")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: myClick(0), bg="orange", fg="white")
button_equal = Button(root, text="=", padx=86, pady=20, command=equalTo, bg="black", fg="white")
button_add = Button(root, text="+", padx=40, pady=20, command=addNumbers, bg="orange", fg="white")
button_clear = Button(root, text="c", padx=86, pady=20, command=clearScreen, bg="black", fg="white")

button_minus = Button(root, text="-", padx=40, pady=20, command=subtractNumbers, bg="orange", fg="white")
button_divide = Button(root, text="/", padx=40, pady=20, command=divideNumbers, bg="orange", fg="white")
button_multiplication = Button(root, text="*", padx=40, pady=20, command=multiplyNumbers, bg="orange", fg="white")

#putting the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiplication.grid(row=6, column=2)

root.mainloop()

