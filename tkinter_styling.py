from tkinter import *

root = Tk()
root.title("CALCULATOR")

root.configure(bg="black")

logo = PhotoImage(file="icon.png")
root.iconphoto(True, logo)



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



entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)

one = PhotoImage(file="one.png")

#designing buttons

button_1 = Button(root, text="1", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(1))
button_2 = Button(root, text="2", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(2))
button_3 = Button(root, text="3", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(3))
button_4 = Button(root, text="4", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(4))
button_5 = Button(root, text="5", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(5))
button_6 = Button(root, text="6", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(6))
button_7 = Button(root, text="7", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(7))
button_8 = Button(root, text="8", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(8))
button_9 = Button(root, text="9", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(9))
button_0 = Button(root, text="0", bg="black", fg="white", padx=40, pady=20, command=lambda: myClick(0))
button_equal = Button(root, text="=", bg="orange", fg="white", padx=86, pady=20, command=equalTo)
button_add = Button(root, text="+", bg="orange", fg="white", padx=40, pady=20, command=addNumbers)
button_clear = Button(root, text="c", bg="orange", fg="white", padx=86, pady=20, command=clearScreen)

button_minus = Button(root, text="-", bg="orange", fg="white", padx=40, pady=20, command=subtractNumbers)
button_divide = Button(root, text="/", bg="orange", fg="white", padx=40, pady=20, command=divideNumbers)
button_multiplication = Button(root, text="*", bg="orange", fg="white", padx=40, pady=20, command=multiplyNumbers)

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

