# digital clock, real time


from tkinter import *

from time import strftime



root = Tk()
root.geometry("500x100")
root.title("Clock")
root.resizable(0, 0)


def time():
    string1 = strftime('%H:%M:%S %p')
    label.config(text=string1)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()