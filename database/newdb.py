from tkinter import *
import sqlite3
from tkinter import *

import tkinter as tk
from tkinter import ttk



def printDetails():
    data_base = sqlite3.connect('phone_book.db')
    db = data_base.cursor()

    db.execute('SELECT *, oid FROM contacts')
    details = db.fetchall()
    print_details = ""
    for detail in details:
        print_details += str(detail) + "\n"

    table.insert("", END, values=print_details)

    data_base.commit()
    data_base.close()


def submit():
    data_base = sqlite3.connect('phone_book.db')

    db = data_base.cursor()

    db.execute("""INSERT INTO contacts VALUES (:first_name, :second_name, :contact)""", 
    {'first_name' : f_nameentry.get(), 
    'second_name' : s_nameentry.get(), 
    'contact' : contact_entry.get()
    }
    )

    data_base.commit()
    data_base.close()

    f_nameentry.delete(0, END)
    s_nameentry.delete(0, END)
    contact_entry.delete(0, END)



root = Tk()

data_base = sqlite3.connect('phone_book.db')

db = data_base.cursor()

#db.execute('CREATE TABLE contacts (first_name text, second_name text, contact integer)')
#db.execute("""CREATE TABLE contacts (
    #first_name text, 
    #second_name text, 
    #contact integer)""")

f_namelbl = Label(root, text="first name")
s_namelbl = Label(root, text="second name")
contactslbl = Label(root, text="contacts")

f_namelbl.grid(row=0, column=0)
s_namelbl.grid(row=1, column=0)
contactslbl.grid(row=2, column=0)

f_nameentry = Entry(root, width=20)
s_nameentry = Entry(root, width=20)
contact_entry = Entry(root, width=20)

f_nameentry.grid(row=0, column=1)
s_nameentry.grid(row=1, column=1)
contact_entry.grid(row=2, column=1)

submitbtn = Button(root, text="submit", width=20, pady=10, command=submit)
submitbtn.grid(row=3, column=0, columnspan=2)

printbtn = Button(root, text="print", width=20, pady=10, command=printDetails)
printbtn.grid(row=4, column=0, columnspan=2)



frm = LabelFrame(root, text="Data Table", font=("Tribuchette", 20), bg="Black", fg="White")
frm.grid(row=5,column=0, columnspan=2)

table = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height=50)
table.grid(row=5,column=0, columnspan=2)
table.heading(1, text="Firstname")
table.heading(2, text="Lastname")
table.heading(3, text="Staff ID")
table.heading(4, text="Time Reported")

data_base.commit()
data_base.close()

root.mainloop()