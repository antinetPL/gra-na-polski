from tkinter import messagebox
import questionsystem
import game

def anserw():
    if questionsystem.pytaniesprawdz>0:
        messagebox.showinfo("Okno pytające","Dobrze! Udało ci się przesunąć o wylosowaną liczbę pól!")
        #game.poleaktualne+= questionsystem.rzut
        
    else:
        messagebox.showerror("Okno pytające","Żle! Zostajesz w miejscu!")

