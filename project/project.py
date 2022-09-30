from tkinter import *
import sqlite3

def signup():
    database = sqlite3.connect('staff.db')
    bd = database.cursor()

    bd.execute('INSERT INTO register VALUES(:name_entry, :passentry)',
                {
                    ':name_entry' : name_entry.get(),
                    ':passentry' : passentry.get()
                })

    print(bd)


    database.commit()
    database.close()

def submit():
    pass

main = Tk()
main.geometry("1800x900")
main.title("Attendance Register - Database")
main.resizable(width=0, height=0)
main.iconbitmap("si_icon.ico")
main.configure(bg="#C7B198")


database = sqlite3.connect('staff.db')

bd = database.cursor()

#bd.execute("""CREATE TABLE signup(
    #firstname text,
   # secondname text,
    #contact integer,
    #gender text,
    #locationaddress text
#)""")


#bd.execute("""CREATE TABLE register(
    #firstname text,
   #passw integer
#)""")




entry_frame = Frame(main, width=300)
entry_frame.place(x=1000, y=200)


namelbl = Label(entry_frame, text="Staff Name", font=("Helvetica", 15))
namelbl.grid(row=1, column=0)

name_entry = Entry(entry_frame, width=30, font=("Helvetica", 20))
name_entry.grid(row=2, column=0, pady=10, padx=10)

passlbl = Label(entry_frame, text="Staff Name", font=("Helvetica", 15))
passlbl.grid(row=3, column=0)

passentry = Entry(entry_frame, width=30, font=("Helvetica", 20))
passentry.grid(row=4, column=0, pady=10, padx=10)

sub_btn = Button(entry_frame, text="Submit", width=25, font=("Helvetica", 15), command=signup)
sub_btn.grid(row=5, column=0, pady=10)


database.commit()
database.close()

main.mainloop()