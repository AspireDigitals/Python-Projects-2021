from tkinter import *
import time
import tkinter as tk
from tkinter import ttk
import sqlite3


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    timelbl.config(text=hour + ":" + minute + ":" + second)

def reg():

    database = sqlite3.connect("appdb.db")
    cursor = database.cursor()

    cursor.execute("INSERT INTO staff VALUES(:first_name, :lastname, :staff_id, :time_reported)",
    {
        ':first_name' : firstname_entry.get(),
        ":last_name" : lastname_entry.get(),
        ":staff_id" : staffid_entry.get()
      
    })

    database.commit()
    database.close()

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    staffid_entry.delete(0, END)


root = Tk()
root.geometry('800x600')

#create database
database = sqlite3.connect("appdb.db")
cursor = database.cursor()

#create table
#cursor.execute("""CREATE TABLE staff(
    #firstname text,
    #lastname text,
    #staffid integer,
    #timereported integer
#)""")

#login form
login_frame = LabelFrame(root, text="Log In Here", font=("Tribuchette", 20), bg="Orange", fg="White")
login_frame.grid(row=0, column=0, padx=10, pady=20)


username_lbl = Label(login_frame, text="Enter Username", pady=10, bg="Orange", fg="White")
username_entry = Entry(login_frame, width=30, font=("Helvetica", 14))

pass_lbl = Label(login_frame, text="Enter Password", pady=10, bg="Orange", fg="White")
pass_entry = Entry(login_frame, width=30, font=("Helvetica", 14), show="*")


username_lbl.grid(row=0, column=0)
username_entry.grid(row=1, column=0, padx=5)

pass_lbl.grid(row=2, column=0)
pass_entry.grid(row=3, column=0)

login_btn = Button(login_frame, text="Log In", font=("Helvetica", 13), width=20)
login_btn.grid(row=4, column=0, pady=10)



#registration form

registrationframe = LabelFrame(root, text="Register Here", font=("Tribuchette", 20), bg="Black", fg="White")
registrationframe.grid(row=1, column=0, padx=10, pady=20)

timelbl = Label(registrationframe, text="", font=("Helvetica", 18), bg="Orange", fg="Black", pady=10, padx=10)
timelbl.grid(row=0, column=0)
timelbl.after(1000, clock)

clock()

firstname_lbl = Label(registrationframe, text="Enter Firstname", pady=10, bg="Black", fg="White")
firstname_entry = Entry(registrationframe, width=30, font=("Helvetica", 14))

lastname_lbl = Label(registrationframe, text="Enter Lastname", pady=10, bg="Black", fg="White")
lastname_entry = Entry(registrationframe, width=30, font=("Helvetica", 14))

staffid_lbl = Label(registrationframe, text="Enter Staff ID", pady=10, bg="Black", fg="White")
staffid_entry = Entry(registrationframe, width=30, font=("Helvetica", 14), show="*")


firstname_lbl.grid(row=1, column=0)
firstname_entry.grid(row=2, column=0, padx=5)

lastname_lbl.grid(row=3, column=0)
lastname_entry.grid(row=4, column=0, padx=5)

staffid_lbl.grid(row=5, column=0)
staffid_entry.grid(row=6, column=0)

login_btn = Button(registrationframe, text="Register", font=("Helvetica", 13), width=20, bg="Orange", fg="Black", command=reg)
login_btn.grid(row=7, column=0, pady=10)




#table frame

frm = LabelFrame(root, text="Data Table", font=("Tribuchette", 20), bg="Black", fg="White")
frm.grid(row=0,column=1)

table = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height=5)
table.grid(row=0,column=0)
table.heading(1, text="Firstname")
table.heading(2, text="Lastname")
table.heading(3, text="Staff ID")
table.heading(4, text="Time Reported")


database.commit()
database.close()
root.mainloop()