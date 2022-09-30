from tkinter import *
from tkinter import messagebox
from tkinter import ttk



def openMain():
    if username_entry.get() == "admin" and password_entry.get() == "admin":
        messagebox.showinfo("Success", "User Signed in successfully")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        main = Tk()
        def closeApp():
            main.quit()
        def submit():
                if nameentry.get():
                    display = nameentry.get()
                    table.insert(text=display)
                nameentry.delete(0, END)

        main.geometry("1800x900")
        main.title("Attendance Register - Database")
        main.resizable(width=0, height=0)
        main.iconbitmap("si_icon.ico")
        main.configure(bg="#C7B198")



        entry_frame = Frame(main, width=200)
        entry_frame.grid(row=0, column=0)

        time = Label(entry_frame, text="10:58:30", font=("Digital-7", 40), fg="#fff", bg="black")
        time.grid(row=0, column=0)

        namelbl = Label(entry_frame, text="Staff Name", font=("Helvetica", 15))
        namelbl.grid(row=1, column=0)

        nameentry = Entry(entry_frame, width=30, font=("Helvetica", 20))
        nameentry.grid(row=2, column=0, pady=10, padx=10)

        sub_btn = Button(entry_frame, text="Submit", width=25, font=("Helvetica", 15), command=submit)
        sub_btn.grid(row=3, column=0, pady=10)

        logout_btn = Button(entry_frame, text="LOG OUT", width=25, font=("Helvetica", 15), command=closeApp)
        logout_btn.grid(row=7, column=0, pady=20)


        displayframe = Frame(main, width=200)
        displayframe.grid(row=0, column=1)


        frm = Frame(main)
        frm.grid(row=1,column=0, columnspan=2)

        table = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height=15)
        table.grid(row=1,column=0)
        table.heading(1, text="Firstname")
        table.heading(2, text="Lastname")
        table.heading(3, text="Staff ID")
        table.heading(4, text="Time Reported")



        main.mainloop()







sign_in = Tk()
sign_in.geometry("1300x700")
sign_in.title("Attendance Register - Sign In")
sign_in.resizable(width=0, height=0)
sign_in.iconbitmap("si_icon.ico")
sign_in.configure(bg="#1A374D")

signin_frame = Frame(sign_in, pady=40)
signin_frame.place(x=360, y=150)


title = Label(signin_frame, text="WELCOME BACK - SIGN IN HERE!", font=("Helvetica", 20))
title.grid(row=0, column=0)

username_lbl = Label(signin_frame, text="USERNAME", font=("Helvetica", 20))
username_entry = Entry(signin_frame, font=("Helvetica", 35))

password_lbl = Label(signin_frame, text="PASSWORD", font=("Helvetica", 20))
password_entry = Entry(signin_frame, font=("Helvetica", 35), show="*")

signin_btn = Button(signin_frame, text="Sign In !", font=("Helvetica", 20), width=32, bg="#ECB365", activebackground="#ECB365", command=openMain)


username_lbl.grid(row=1, column=0)
username_entry.grid(row=2, column=0, pady=30, padx=20)

password_lbl.grid(row=3, column=0)
password_entry.grid(row=4, column=0)

signin_btn.grid(row=5, column=0, pady=20, padx=10)


sign_in.mainloop()