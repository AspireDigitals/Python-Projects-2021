from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("300x400")

x = sqlite3.connect('phonebook.db')
v = x.cursor()

#x.execute(
    #"""CREATE TABLE contacts (
       # first_name text,
        #last_name text,
        #email text,
       # contact integer
    #)""")
def submit():
    x = sqlite3.connect('address_book.db')
    first_nameEntry.delete(0, END)
    last_nameEntry.delete(0, END)
    emailEntry.delete(0, END)
    contactEntry.delete(0, END)


first_name = Label(root, text="First name")
first_name.grid(row=0, column=0)
last_name = Label(root, text="Last name")
last_name.grid(row=1, column=0)
email = Label(root, text="Email")
email.grid(row=2, column=0)
contact = Label(root, text="Contact")
contact.grid(row=3, column=0)

first_nameEntry = Entry(root, width=30)
first_nameEntry.grid(row=0, column=1, padx=20)
last_nameEntry = Entry(root, width=30)
last_nameEntry.grid(row=1, column=1, padx=20)
emailEntry = Entry(root, width=30)
emailEntry.grid(row=2, column=1, padx=20)
contactEntry = Entry(root, width=30)
contactEntry.grid(row=3, column=1, padx=20)

submitBtn = Button(root, text="Submit", width=35, command=submit)
submitBtn.grid(row=4, columnspan=2, pady=10, padx=10)




x.commit()
x.close()

root.mainloop()