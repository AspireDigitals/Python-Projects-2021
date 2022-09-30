from tkinter import *
import sqlite3



def submit():
    db = sqlite3.connect("students.db")
    db_cursor = db.cursor()

    db_cursor.execute('INSERT INTO class_5 VALUES(:f_name, :s_name, :residence, :parent)',
                    {
                        'f_name' : f_nameentry.get(),
                        's_name' : s_nameentry.get(),
                        'residence' : residence_entry.get(),
                        'parent' : parents_nameentry.get()
                    }  )

    db.commit()
    db.close()


    f_nameentry.delete(0, END)
    s_nameentry.delete(0, END)
    residence_entry.delete(0, END)
    parents_nameentry.delete(0, END)

root = Tk()
root.title("Students Forms")
root.geometry("300x400")

db = sqlite3.connect("students.db")

db_cursor = db.cursor()


#db_cursor.execute('CREATE TABLE class_5 (first_name text, second_name text, residence text, parents_name text)')

f_namelbl = Label(root, text="First Name", padx=10, pady=10)
s_namelbl = Label(root, text="Second Name", padx=10, pady=10)
residencelbl = Label(root, text="Residence", padx=10, pady=10)
parents_namelbl = Label(root, text="Parents Name", padx=10, pady=10)

f_namelbl.grid(row=0, column=0)
s_namelbl.grid(row=1, column=0)
residencelbl.grid(row=2, column=0)
parents_namelbl.grid(row=3, column=0)


f_nameentry = Entry(root, width=30)
s_nameentry = Entry(root, width=30)
residence_entry = Entry(root, width=30)
parents_nameentry = Entry(root, width=30)

f_nameentry.grid(row=0, column=1)
s_nameentry.grid(row=1, column=1)
residence_entry.grid(row=2, column=1)
parents_nameentry.grid(row=3, column=1)

submit_btn = Button(root, width=30, text="Submit Form", pady=10, command=submit)
submit_btn.grid(row=4, column=0, columnspan=2)


db.commit()
db.close()



root.mainloop()