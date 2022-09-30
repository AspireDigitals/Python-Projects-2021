from tkinter import *


root = Tk()

root.geometry("500x300")
root.title("Hello World App")

def showName():
    if MyInput.get():
        Mytext = MyInput.get()
        Mytext = Label(root, text = Mytext)
        Mytext.pack()
    else:
        Mytext = Label(root, text="Input can not be empty")
        

title = Label(root, text="Hello World")
title.pack(pady=20, padx=10)

username = Label(root, text="Enter user name: ")
username.pack()

MyInput = Entry(root, font=50)
MyInput.pack(pady=20)

PrintButton = Button(root, text="Print Name", command=(showName))
PrintButton.pack()


root.mainloop()