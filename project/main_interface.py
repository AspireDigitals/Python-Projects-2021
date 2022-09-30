from tkinter import *
import time
import sqlite3

main = Tk()
main.title("ATTENDANCE REGISTER")
main.geometry("900x500")
main.resizable(height=0, width=0)
main.iconbitmap("si_icon.ico")
main.config(bg="cyan")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clocklbl.config(text=hour + ":" + minute + ":" + second)
    clocklbl.after(1000, clock)


stafftitle = Label(main, text="STAFF", font=("Cambria",10), bg="cyan", fg="brown")
stafftitle.place(x=270, y=7)

staff_Lable = Label(main, text="Enter Name", font=("Cambria", 15), bg="cyan", fg="brown")
staff_Lable.place(x=10, y=30)

staff_Entry = Entry(main, width=30, font=("Cambria", 15))
staff_Entry.place(x=130, y=30)

submit_btn = Button(main, text="Submit", font=("Cambria", 12), padx=17, bg="brown", fg="white")
submit_btn.place(x=130, y=70)

stafflogout_btn = Button(main, text="Log Out", font=("Cambria", 12), padx=17, bg="brown", fg="white")
stafflogout_btn.place(x=237, y=70)

Allentries_btn = Button(main, text="All Entries", font=("Cambria", 12), padx=15, bg="brown", fg="white")
Allentries_btn.place(x=350, y=70)

admintitle = Label(main, text="ADMIN", font=("Cambria",10), bg="cyan", fg="brown")
admintitle.place(x=260, y=177)

admin_Lable = Label(main, text="Delete Entry", font=("Cambria", 15), bg="cyan", fg="brown")
admin_Lable.place(x=10, y=200)

staff_Entry = Entry(main, width=30, font=("Cambria", 15))
staff_Entry.place(x=130, y=200)

adminlogin_btn = Button(main, text="Log In", font=("Cambria", 12), padx=10, bg="brown", fg="white")
adminlogin_btn.place(x=130, y=240)

adminsave_btn = Button(main, text="Save", font=("Cambria", 12), padx=10, bg="brown", fg="white")
adminsave_btn.place(x=216, y=240)

admindel_btn = Button(main, text="Delete", font=("Cambria", 12), padx=10, bg="brown", fg="white")
admindel_btn.place(x=293, y=240)

adminlogout_btn = Button(main, text="Log Out", font=("Cambria", 12), padx=10, bg="brown", fg="white")
adminlogout_btn.place(x=380, y=240)

clocklbl = Label(main, text="", font=("Cambria", 30), bg="cyan", fg="brown")
clocklbl.place(x=730, y=0)


clock()





main.mainloop()