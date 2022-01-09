from tkinter import *
from tkinter import messagebox
import run

def menu():
    global win
    win=Tk()
    win.geometry("100x100")
    z=Button(text="Graj",command=run.running).grid(row=0,column=0)
    win.mainloop()