from tkinter import *
import sqlite3


root = Tk()
root.geometry("300x400")

CreateDatabase = sqlite3.connect('Students.db')
insert = CreateDatabase.cursor()

InsertData = insert.execute("""CREATE TABLE classlist (
            first_name text,
            last_name text,
            home text,
            contact integer)""")

CreateDatabase.commit()
CreateDatabase.close()

root.mainloop()