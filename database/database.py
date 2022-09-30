from tkinter import *
import sqlite3


def clicked(number):
    first_Number = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(first_Number) + str(number))

def clear():
    entry.delete(-1, 1)

def quit():
    root.quit()

def composeSMS():
    compose = Tk()
    compose.title("Compose Message")
    compose.geometry("300x200")

    sender_label = Label(compose, text="Sender ID")
    sender_number = Entry(compose)

    sender_label.grid(row=0, column=0)
    sender_number.grid(row=0, column=1)

    receiver_label = Label(compose, text="Receiver ID")
    receiver_number = Entry(compose)

    receiver_label.grid(row=0, column=2)
    receiver_number.grid(row=0, column=3)

    sms = Text(compose)
    sms.grid(row=1, column=0, columnspan=4)
    compose.mainloop()

root = Tk()
root.geometry("360x600")
root.resizable(width=0, height=0)

menubar = Menu(root)

messagemenu = Menu(menubar, tearoff=0)
messagemenu.add_command(label="New Message", command=composeSMS)
messagemenu.add_command(label="Inbox")
messagemenu.add_command(label="Sent")
messagemenu.add_command(label="Outbox")
messagemenu.add_command(label="Draft")
messagemenu.add_separator()
messagemenu.add_command(label="Settings")
menubar.add_cascade(label="Messages", menu=messagemenu)

callmenu = Menu(menubar, tearoff=0)
callmenu.add_command(label="All Calls")
callmenu.add_command(label="Dialed Calls")
callmenu.add_command(label="Received Calls")
callmenu.add_command(label="Missed Calls")
menubar.add_cascade(label="Call History", menu=callmenu)

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Alarm")
toolsmenu.add_command(label="Clock")
menubar.add_cascade(label="Tools", menu=toolsmenu)

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Display Settings")
settingsmenu.add_command(label="Audio Settings")
settingsmenu.add_command(label="Call Settings")
settingsmenu.add_command(label="Security Settings")
settingsmenu.add_separator()
settingsmenu.add_command(label="Restore Factory Settings")
menubar.add_cascade(label="Settings", menu=settingsmenu)




data = sqlite3.connect("Address.db")

db = data.cursor()

#db.execute("""CREATE TABLE phoneDetails(
    #contact_name text,
   # home_address text,
    #office_address text,
   # home_contact integer,
   # office_contact integer)"""
   # )


entry = Entry(root, width=30, font=("Helvetica", 15))
entry.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

menu = Button(root, text="Menu", width=15, padx=5, pady=5)
up = Button(root, text="Up", width=15, padx=5, pady=5)
contacts = Button(root, text="Contacts", width=15, padx=5, pady=5)

menu.grid(row=1, column=0)
up.grid(row=1, column=1)
contacts.grid(row=1, column=2)

left = Button(root, text="Left", width=15, padx=5, pady=5)
okay = Button(root, text="Okay", width=15, padx=5, pady=22)
right = Button(root, text="Right", width=15, padx=5, pady=5)

left.grid(row=3, column=0)
okay.grid(row=3, column=1, rowspan=2)
right.grid(row=3, column=2)

send = Button(root, text="Send", width=15, padx=5, pady=5)
down = Button(root, text="Down", width=15, padx=5, pady=5)
quit = Button(root, text="Quit", width=15, padx=5, pady=5, command=quit)

send.grid(row=4, column=0)
quit.grid(row=4, column=2)

btn_233 = Button(root, text="+233", width=15, padx=5, pady=5, command=lambda: clicked('+233 '))
down = Button(root, text="Down", width=15, padx=5, pady=5)
clear = Button(root, text="Clear", width=15, padx=5, pady=5, command=clear)

btn_233.grid(row=5, column=0)
down.grid(row=5, column=1)
clear.grid(row=5, column=2)

btn_1 = Button(root, text="1", width=15, padx=5, pady=20, command=lambda: clicked(1))
btn_2 = Button(root, text="2", width=15, padx=5, pady=20, command=lambda: clicked(2))
btn_3 = Button(root, text="3", width=15, padx=5, pady=20, command=lambda: clicked(3))

btn_1.grid(row=6, column=0)
btn_2.grid(row=6, column=1)
btn_3.grid(row=6, column=2)

btn_4 = Button(root, text="4", width=15, padx=5, pady=20, command=lambda: clicked(4))
btn_5 = Button(root, text="5", width=15, padx=5, pady=20, command=lambda: clicked(5))
btn_6 = Button(root, text="6", width=15, padx=5, pady=20, command=lambda: clicked(6))

btn_4.grid(row=7, column=0)
btn_5.grid(row=7, column=1)
btn_6.grid(row=7, column=2)

btn_7 = Button(root, text="7", width=15, padx=5, pady=20, command=lambda: clicked(7))
btn_8 = Button(root, text="8", width=15, padx=5, pady=20, command=lambda: clicked(8))
btn_9 = Button(root, text="9", width=15, padx=5, pady=20, command=lambda: clicked(9))

btn_7.grid(row=8, column=0)
btn_8.grid(row=8, column=1)
btn_9.grid(row=8, column=2)

btn_star = Button(root, text="*", width=15, padx=5, pady=20, command=lambda: clicked('*'))
btn_0 = Button(root, text="0", width=15, padx=5, pady=20, command=lambda: clicked(0))
btn_hash = Button(root, text="#", width=15, padx=5, pady=20, command=lambda: clicked('#'))

btn_star.grid(row=9, column=0)
btn_0.grid(row=9, column=1)
btn_hash.grid(row=9, column=2)

data.commit()
data.close()

root.config(menu=menubar)
root.mainloop()