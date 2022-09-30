from tkinter import *
from datetime import datetime
from tkinter import messagebox


window = Tk()
window.title("Age Calculator")
window.geometry("500x300")

image = PhotoImage(file="icon.png")

window.iconphoto(False, image)

def My_Age():
    if My_entry.get():
        current_year = datetime.now().year
        your_age = current_year - int(My_entry.get())
        messagebox.showinfo("Your Age", f"Your Age is {your_age}")
    else:
        messagebox.showerror("Error", "You have not entered year of birth")


My_label = Label(window, text="Enter Year of Birth", font=("Helvetica", 20), fg="red")
My_label.pack(pady=20)

My_entry = Entry(window, font=("Helvetica", 18))
My_entry.pack(pady=20)

My_button = Button(window, text="Calculate !", font=("Helvetica", 18), command=My_Age, bg="orange", border="10")
My_button.pack(pady=20)



window.mainloop()