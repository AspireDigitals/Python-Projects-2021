from tkinter import *

Window = Tk()
Window.title("Hello World App")
Window.geometry("300x100")

def myClick():
    hello = "Hello", e.get()
    myLabel = Label(Window, text=hello)
    e.delete(0, "end")
    myLabel.pack(pady=10)



e = Entry(Window, width=50, font=("Helvetica", 20))
e.pack(padx=10, pady=10)

myButton = Button(Window, text="Enter your name", command=(myClick))
myButton.pack(pady=10)




Window.mainloop()