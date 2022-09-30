from tkinter import *
from tkinter import messagebox
import sqlite3
import time


def submit():
    database = sqlite3.connect("people.db")


    db = database.cursor()

    db.execute('INSERT INTO register VALUES(:f_name)',
    {
        'f_name' : entry.get()
    })

    database.commit()
    database.close()

    entry.delete(0, END)

def query():
    database = sqlite3.connect("people.db")

    db = database.cursor()

    db.execute('SELECT *, oid FROM register')
    records = db.fetchall()

    display_records = ""
    for record in records:
        display_records += str(record) + "\n"

    all_entries = Label(frame, text=display_records)
    all_entries.grid(row=3, column=0)
    
    records = Label(frame, text=records)
    records.grid(row=3, column=0)

    database.commit()
    database.close()

def delete():
    database = sqlite3.connect("people.db")


    db = database.cursor()

    db.execute('DELETE FROM register WHERE oid= ' + deleteentry.get())

    database.commit()
    database.close()

    deleteentry.delete(0, END)

root = Tk()
root.title("Attendance Register")
root.geometry("1000x700")

frame = Frame(root)
frame.place(x=300, y=100)


database = sqlite3.connect("people.db")


db = database.cursor()

#db.execute("CREATE TABLE register(f_name text)")

database.commit()
database.close()

title = Label(frame, text="Attendance Register")
title.grid(row=0, column=0, pady=20)

entry = Entry(frame, width=30, font=("", 20))
entry.grid(row=1, column=0, columnspan=4)

btn = Button(frame, text="Submit", width=20, padx=5, pady=5, command=submit)
btn.grid(row=2, column=0, padx=10, pady=20)

btn = Button(frame, text="Log Out", width=20, padx=5, pady=5)
btn.grid(row=2, column=1, padx=10, pady=20)

btn = Button(frame, text="All Entries", width=20, padx=5, pady=5, command=query)
btn.grid(row=2, column=2, padx=10, pady=20)

title = Label(frame, text="Administrator")
title.grid(row=4, column=0, pady=20)

title = Label(frame, text="Delete Entry")
title.grid(row=5, column=0, pady=20)

deleteentry = Entry(frame, width=30, font=("", 20))
deleteentry.grid(row=5, column=1, columnspan=4)

btn = Button(frame, text="Log in", width=5, padx=10, pady=5)
btn.grid(row=6, column=0, padx=2, pady=20)

btn = Button(frame, text="Save Entries", width=10, padx=5, pady=5)
btn.grid(row=6, column=1, padx=2, pady=20)

btn = Button(frame, text="Delete", width=10, padx=5, pady=5, command=delete)
btn.grid(row=6, column=2, padx=2, pady=20)

btn = Button(frame, text="Log Out", width=10, padx=5, pady=5)
btn.grid(row=6, column=3, padx=2, pady=20)

root.mainloop()