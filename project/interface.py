from tkinter import *
import time


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clocklbl.config(text=hour + ":" + minute + ":" + second)
    clocklbl.after(1000, clock)


root = Tk()
root.geometry("1000x600")
root.title("ATTENDANCE REGISTER")
root.resizable(height=0, width=0)
root.iconbitmap("si_icon.ico")
root.configure(bg="#C7B198")


frame_1 = Frame(root, height=450, width=355)
frame_1.place(x=40, y=120)

entry_1 = Entry(frame_1, font=("Cambria", 20))
entry_1.grid(row=2, column=0, pady=30, padx=20)

signin_btn = Button(frame_1, text="Sign In!", font=("Cambria", 10), bg="#1A374D", fg="white", activebackground="#1A374D", activeforeground="white")
signin_btn.grid(row=3, column=0, pady=50)

login_btn = Button(root, text="Log In", font=("Cambria", 20), bg="grey", fg="white", activebackground="grey", activeforeground="white")
login_btn.place(x=80, y=400)

update_btn = Button(root, text="Update", font=("Cambria", 20), bg="grey", fg="white", activebackground="grey", activeforeground="white")
update_btn.place(x=75, y=500)

delete_btn = Button(root, text="Delete", font=("Cambria", 20), bg="grey", fg="white", activebackground="grey", activeforeground="white")
delete_btn.place(x=240, y=400)

logout_btn = Button(root, text="Log Out", font=("Cambria", 20), bg="grey", fg="white", activebackground="grey", activeforeground="white")
logout_btn.place(x=230, y=500)


frame_2 = Frame(root, height=500, width=400)
frame_2.place(x=500, y=50)

clocklbl = Label(root, text="", font=("Cambria", 30))
clocklbl.grid(row=0, column=0, padx=49, pady=20)


clock()
root.mainloop()