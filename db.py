from tkinter import *
import sqlite3


def submitAddress():

    conn = sqlite3.connect("address.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        contact integer,
        user_address text
        )""")

    conn.commit()
    conn.close()


root = Tk()


fname_lbl = Label(root, text="first name")
lname_lbl = Label(root, text="last name")
contact_lbl = Label(root, text="contact")
user_address = Label(root, text="address")



fname_entry = Entry(root, text="Helvetica")
lname_entry = Entry(root, text="Helvetica")
contact_entry = Entry(root, text="Helvetica")
address_entry = Entry(root, text="Helvetica")

fname_lbl.grid(row=0, column=0)
lname_lbl.grid(row=1, column=0)
contact_lbl.grid(row=2, column=0)
user_address.grid(row=3, column=0)

fname_entry.grid(row=0, column=1)
lname_entry.grid(row=1, column=1)
contact_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

btn = Button(root, text="submit", command=submitAddress)
btn.grid(row=4, column=1)


root.mainloop()