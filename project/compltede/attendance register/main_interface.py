from tkinter import *
import time
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
import os


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    nt = clocklbl.config(text=hour + ":" + minute + ":" + second)
    nt.after(1000, clock)

def submitbtn():
    database = sqlite3.connect("Staff ID.db")

    db = database.cursor()

    db.execute('INSERT INTO staff_info VALUES (:staff_name, :reporting_time)',
    {
        'staff_name' : staff_Entry.get(),
        'reporting_time' : time_Entry.get()
    })

    db.execute('SELECT *, oid FROM staff_info')
    records = db.fetchall()

    records_display = ""
    for info in records:
        records_display += str(info[0]) + str(info[1]) + "\n"

    records = Label(main, text=records_display, font=("Cambria",10), bg="cyan", fg="brown")
    records.place(x=550, y=100)

    database.commit()
    database.close()

    staff_Entry.delete(0, END)

  

def allentriesbtn():
    database = sqlite3.connect("Staff ID.db")

    db = database.cursor()

    db.execute('SELECT *, oid FROM staff_info')
    records = db.fetchall()

    records_display = ""
    for info in records:
        records_display += str(info) + str(info[1]) + "\n"

    records = Label(main, text=records_display, font=("Cambria",10), bg="cyan", fg="brown")
    records.place(x=550, y=100)

    database.commit()
    database.close()


def stafflogoutbtn():
    database = sqlite3.connect("Staff ID.db")

    db = database.cursor()

    db.execute('DELETE FROM staff_info WHERE oid= ' + staff_Entry.get())

    staff_Entry.delete(0, END)

    database.commit()
    database.close()


def password():
    if adminpassword_Entry.get() == "admin":
        messagebox.showinfo("Success", "successfully signed in")


def adminlogout():
    if adminpassword_Entry.get() == "admin":
        main.quit()


def save():

    database = sqlite3.connect("Staff ID.db")

    db = database.cursor()
    db.execute('SELECT *, oid FROM staff_info')
    records = db.fetchall()


    records_display = ""
    for info in records:
        records_display += str(info) + "\n"

    fd = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    t = records
    with open(fd, "w+") as f:
        f.write(str(t))
    print("Saved")

    database.commit()
    database.close()

 
    

main = Tk()
main.title("ATTENDANCE REGISTER")
main.geometry("900x500")
#main.resizable(height=0, width=0)
#main.iconbitmap("si_icon.ico")
main.config(bg="cyan")

database = sqlite3.connect("Staff ID.db")

db = database.cursor()

db.execute('CREATE TABLE IF NOT EXISTS staff_info(staff_name text, reporting_time text)')

database.commit()
database.close()



clocklbl = Label(main, text="", font=("Cambria", 30), bg="cyan", fg="brown")
clocklbl.place(x=730, y=0)

stafftitle = Label(main, text="STAFF", font=("Cambria",10), bg="cyan", fg="brown")
stafftitle.place(x=270, y=7)

staff_Lable = Label(main, text="Enter Name", font=("Cambria", 15), bg="cyan", fg="brown")
staff_Lable.place(x=10, y=30)

staff_Entry = Entry(main, width=30, font=("Cambria", 15))
staff_Entry.place(x=130, y=30)

time_Lable = Label(main, text="Enter Time", font=("Cambria", 15), bg="cyan", fg="brown")
time_Lable.place(x=10, y=70)

time_Entry = Entry(main, width=30, font=("Cambria", 15), text=clocklbl)
time_Entry.insert(0, nt)
time_Entry.place(x=130, y=70)

submit_btn = Button(main, text="Submit", font=("Cambria", 12), padx=17, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=submitbtn)
submit_btn.place(x=130, y=120)

stafflogout_btn = Button(main, text="Log Out", font=("Cambria", 12), padx=17, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=stafflogoutbtn)
stafflogout_btn.place(x=237, y=120)

Allentries_btn = Button(main, text="All Entries", font=("Cambria", 12), padx=15, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=allentriesbtn)
Allentries_btn.place(x=350, y=120)

admintitle = Label(main, text="ADMIN", font=("Cambria",10), bg="cyan", fg="brown")
admintitle.place(x=260, y=177)

admin_password = Label(main, text="Password", font=("Cambria", 15), bg="cyan", fg="brown")
admin_password.place(x=10, y=200)

adminpassword_Entry = Entry(main, width=30, font=("Cambria", 15))
adminpassword_Entry.place(x=130, y=200)

adminsave_btn = Button(main, text="Save", font=("Cambria", 12), padx=10, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=save)
adminsave_btn.place(x=130, y=240)

#adminsave_btn = Button(main, text="Save", font=("Cambria", 12), padx=10, bg="brown", fg="white", activebackground="brown", activeforeground="white")
#adminsave_btn.place(x=216, y=240)

#admindel_btn = Button(main, text="Delete", font=("Cambria", 12), padx=10, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=deletebtn)
#admindel_btn.place(x=293, y=240)

adminlogout_btn = Button(main, text="Log Out", font=("Cambria", 12), padx=10, bg="brown", fg="white", activebackground="brown", activeforeground="white", command=adminlogout)
adminlogout_btn.place(x=380, y=240)




clock()





main.mainloop()