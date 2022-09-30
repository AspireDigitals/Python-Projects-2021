from tkinter import *
import time

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    clocklbl.config(text=hour + ":" + minute + ":" + second)
    clocklbl.after(1000, clock)

root = Tk()
root.geometry("400x500")


clocklbl = Label(root, text="", font=("", 30))
clocklbl.pack()



clock()
root.mainloop()