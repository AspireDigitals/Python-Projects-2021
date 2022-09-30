from tkinter import *
from datetime import datetime
from tkinter import messagebox
from tkinter.font import Font

Window = Tk()
Window.geometry("500x400")
Window.configure(background="grey")
Window.title("Age Calculator")

icon = PhotoImage(file="icon.png")
Window.iconphoto(False, icon)


def myAge():
    if my_entry.get():
        current_age = datetime.now().year
        age = current_age - int(my_entry.get())
        messagebox.showinfo("Info", f"Your age is {age}")
    else:
        messagebox.showerror("Error", "Sorry, No input received")


label = Label(Window, text="AGE CALCULATOR", font=("Helvetica", 20), bg="grey", fg="white")
label.pack(pady=20)

yob = Label(Window, text="Enter Year of Birth", font=("Helvetica", 20), bg="grey", fg="white")
yob.pack(pady=10)

my_entry = Entry(Window, font=("Helvetica", 16))
my_entry.pack(pady=10)

calc = Button(Window, text="Calculate", font=("Helvetica", 18), command=myAge)
calc.pack(pady=10)

Window.mainloop()