from tkinter import *



Cacu = Tk()
Cacu.title("CALCULATOR")

#Cacu.resizable(width=0, height=0)

Cacu.resizable(height=0, width=0)

#logo = PhotoImage(file="Cacus2.png")
#Cacu.iconphoto(True, logo)

Cacu.iconbitmap("Cacus1.ico")


def MyPunch(number):
    FirstNumber = CacuScreen.get()
    CacuScreen.delete(0, END)
    CacuScreen.insert(0, str(FirstNumber) + str(number))

def Clear():
    CacuScreen.delete(0, END)

def Addition():
    FirstNumber = CacuScreen.get()
    global fm
    global math
    math = "addition"
    fm = int(FirstNumber)
    CacuScreen.delete(0, END)

def Subtraction():
    FirstNumber = CacuScreen.get()
    global fm
    global math
    math = "subtraction"
    fm = int(FirstNumber)
    CacuScreen.delete(0, END)

def Multiplication():
    FirstNumber = CacuScreen.get()
    global fm
    global math
    math = "multiplication"
    fm = int(FirstNumber)
    CacuScreen.delete(0, END)

def Division():
    FirstNumber = CacuScreen.get()
    global fm
    global math
    math = "division"
    fm = int(FirstNumber)
    CacuScreen.delete(0, END)

def EqualTo():
    SecondNumber = CacuScreen.get()
    CacuScreen.delete(0, END)
    if math == "addition":
       CacuScreen.insert(0, fm + int(SecondNumber))
    if math == "subtraction":
       CacuScreen.insert(0, fm - int(SecondNumber))
    if math == "multiplication":
       CacuScreen.insert(0, fm * int(SecondNumber))
    if math == "division":
       CacuScreen.insert(0, fm / int(SecondNumber))




CacuScreen = Entry(Cacu, width=55, borderwidth=10)
CacuScreen.grid(row=0, column=0, columnspan=4)



#Buttons
Button1 = Button(Cacu, text="1", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(1))
Button2 = Button(Cacu, text="2", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(2))
Button3 = Button(Cacu, text="3", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(3))
ButtonMultiply = Button(Cacu, text="*", bg="orange", padx=40, pady=20, command=Multiplication)

Button4 = Button(Cacu, text="4", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(4))
Button5 = Button(Cacu, text="5", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(5))
Button6 = Button(Cacu, text="6", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(6))
ButtonDivide = Button(Cacu, text="/", bg="orange", padx=40, pady=20, command=Division)

Button7 = Button(Cacu, text="7", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(7))
Button8 = Button(Cacu, text="8", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(8))
Button9 = Button(Cacu, text="9", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(9))
ButtonAdd = Button(Cacu, text="+", bg="orange", padx=40, pady=20, command=Addition)

Button0 = Button(Cacu, text="0", bg="grey", fg="white", padx=40, pady=20, command=lambda: MyPunch(0))
ButtonEqual = Button(Cacu, text="=", bg="black", fg="white", padx=86.49, pady=20, command=EqualTo)
ButtonSubtract = Button(Cacu, text="-", bg="orange", padx=40, pady=20, command=Subtraction)

ButtonClear = Button(Cacu, text="Clear", bg="red", fg="white", activebackground="black", padx=170.5, pady=20, command=Clear)

#Griding Buttons
Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
ButtonAdd.grid(row=1, column=3)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
ButtonDivide.grid(row=2, column=3)

Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)
ButtonMultiply.grid(row=3, column=3)

Button0.grid(row=4, column=0)
ButtonEqual.grid(row=4, column=1, columnspan=2)
ButtonSubtract.grid(row=4, column=3)

ButtonClear.grid(row=5, column=0, columnspan=4)




Cacu.mainloop()
