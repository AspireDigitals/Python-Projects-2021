from tkinter import *
from tkinter import messagebox
from datetime import datetime

Window = Tk()
Window.geometry("300x400")
Window.configure(background="orange")
Window.title("Age Calculator")
image = PhotoImage(file="icon.png")
Window.iconphoto(False, image)

def myAge():
    if year_of_birth.get():
        current_age = datetime.now().year
        your_age = current_age - int(year_of_birth.get())
        messagebox.showinfo("Info", f"Your age is {your_age}")
    else:
        messagebox.showerror("Error", "Sorry, no input received")

name = Label(Window, text="AGE CALCULATOR", font=("Harabara", 20), bg="orange", fg="black")
name.pack(pady=20)

label = Label(Window, text="Enter Year of Birth", font=("Helvetica", 18), fg="white", bg="orange")
label.pack(pady=10)

year_of_birth = Entry(Window, font=("Helvetica", 18))
year_of_birth.pack(pady=5)

button = Button(Window, text="CALCULATE", font=("Helvetica", 16), bg="white", command=(myAge))
button.pack(pady=10)




Window.mainloop()