from tkinter import *


def submit():
    if nameentry.get():
        display = nameentry.get()
        display = Label(displayframe, text=display, font=("Helvetica", 30))
        display.grid(row=1, column=0)
    nameentry.delete(0, END)



main = Tk()
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

logout_btn = Button(entry_frame, text="LOG OUT", width=25, font=("Helvetica", 15))
logout_btn.grid(row=7, column=0, pady=20)


displayframe = Frame(main, width=200)
displayframe.grid(row=0, column=1)


main.mainloop()








