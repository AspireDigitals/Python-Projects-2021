from tkinter import *
import time


def clock():
  
    red.config(text="", font=("", 40), fg="red", padx=10, pady=10, bg="red")

def yellow():
    red.config(text="", font=("", 40), fg="red", padx=10, pady=10, bg="gold")

def green():
    red.config(text="", font=("", 40), fg="red", padx=10, pady=10, bg="green")

window = Tk()
window.title("T.L.A")
window.geometry("230x500")
window.resizable(width=False, height=False)
window.config(bg="black")

title = Label(window, text="Traffic", font=("Nexa Bold", 30), fg="white", bg="black")
title.place(x=50, y=10)

red = Label(window, text="", font=("", 40), fg="red", width=2, padx=10, pady=10, bg="black")
red.place(x=70, y=80)


x = red.after(5000, clock)
y = red.after(10000, yellow)
z = red.after(15000, green)


clock()
window.mainloop()