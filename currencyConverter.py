from tkinter import *
from tkinter import messagebox

Window =Tk()

def convertion():
    if entry.get():
        rate = 6.5
        results = int(entry.get()) / rate
        messagebox.showinfo("Info", f"Your amount is {results} in dollars")
    else:
        messagebox.showerror("Error", "Sorry, No input received")

label = Label(Window, text="Enter currency in cedis")
label.pack(pady=10)

entry = Entry(Window, font=("Helvetica", 18))
entry.pack(pady=10)


button = Button(Window, text="Convert", font=("Helvetica", 20), command=convertion)
button.pack(pady=20)
Window.mainloop()