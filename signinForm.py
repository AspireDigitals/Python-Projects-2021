from tkinter import messagebox
from tkinter import *
import sqlite3
from datetime import datetime
from turtle import color


def login():
    db = sqlite3.connect("login.db")
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    db.execute("INSERT INTO login(username, password) VALUES('admin', 'admin')")
    Cursor = db.cursor()
    Cursor.execute("SELECT * FROM login where username=? AND password=?", (name_entry.get(), password_entry.get()))
    row = Cursor.fetchone()
    if row:
        msg = messagebox.showinfo("Success", "User signed in successful")
        new = Tk()
        new.geometry("300x200")
        new.mainloop()
    else:
        messagebox.showerror("Error", "Sorry, user not found")
    Cursor.connection.commit()
    db.close()


root = Tk()
root.geometry("400x400")
root.title("Login")

name_entry = StringVar()
mail_entry = StringVar()
password_entry = StringVar()

namelbl = Label(root, text="Username", padx=20, pady=20, font=("Tribuchet", 15))
nameentry = Entry(root, width=35, textvariable=name_entry)

mail = Label(root, text="Email", padx=20, pady=20, font=("Tribuchet", 15))
mailentry = Entry(root, width=35, textvariable=mail_entry)

password = Label(root, text="Password", padx=20, pady=20, font=("Tribuchet", 15))
passwordentry = Entry(root, width=35, textvariable=password_entry, show="*")


signinBtn = Button(root, text="Sign In", padx=20, pady=10, font=("Tribuchet", 15), command=login)


namelbl.grid(row=0, column=0)
nameentry.grid(row=0, column=1)

mail.grid(row=1, column=0)
mailentry.grid(row=1, column=1)

password.grid(row=2, column=0)
passwordentry.grid(row=2, column=1)

signinBtn.grid(row=3, column=1)

root.mainloop()