
from tkinter import messagebox
from random import *
import anserw
import os
import game

os.chdir("C:/Users/Antek/OneDrive/Desktop/game/questionsystem/")

def ask():
    global pytaniesprawdz
    global rzut
    
    kostka=[1,2,3,4,5,6]
    rzut=choice(kostka)
    pytanieza="Pytanie za "

    if rzut==1:
        poprawnosc=" punkt:"
    if rzut>1 and rzut<5:
        poprawnosc=" punkty:"
    else:
        poprawnosc=" punktów:"
    
    pytania=['question1.ques','question2.ques','question3.ques','question4.ques','question5.ques','question6.ques','question7.ques','question8.ques','question9.ques','question10.ques','question11.ques','question12.ques','question13.ques','question14.ques','question15.ques','question16.ques','question17.ques','question18.ques','question19.ques','question20.ques','question21.ques','question22.ques','question23.ques','question24.ques','question25.ques','question26.ques','question27.ques','question28.ques','question29.ques','question30.ques','question31.ques','question32.ques','question33.ques','question34.ques','question35.ques','question36.ques','question37.ques','question38.ques','question39.ques','question40.ques','question41.ques','question42.ques','question43.ques','question44.ques','question45.ques','question46.ques','question47.ques','question48.ques','question49.ques','question50.ques','question51.ques','question52.ques','question53.ques','question54.ques','question55.ques']
    wyborpytan=choice(pytania)
    pytanie=open(wyborpytan, encoding = "utf-8")
    czytaniepytania=pytanie.read()
    zapisywanie=open("question.last","w+",encoding = "utf-8")
    zapisywanie.write(pytanieza)

    zapisywanie.write(str(rzut))
    zapisywanie.write(poprawnosc)
    zapisywanie.write("\n")
    zapisywanie.write(str(czytaniepytania))
    zapisywanie.close()
    aktualizacja=open("question.last","r",encoding = "utf-8")
    czytaniedwa=aktualizacja.read()


    pytaniesprawdz=messagebox.askyesno('Okno pytające',czytaniedwa)

    
    if (wyborpytan == 'question1.ques') or (wyborpytan == 'question2.ques') or (wyborpytan == 'question4.ques') or (wyborpytan == 'question5.ques') or (wyborpytan == 'question10.ques') or (wyborpytan == 'question12.ques') or (wyborpytan == 'question17.ques') or (wyborpytan == 'question18.ques') or (wyborpytan == 'question21.ques') or (wyborpytan == 'question22.ques') or (wyborpytan == 'question27.ques') or (wyborpytan == 'question32.ques') or (wyborpytan == 'question34.ques') or (wyborpytan == 'question37.ques') or (wyborpytan == 'question39.ques') or (wyborpytan == 'question40.ques') or (wyborpytan == 'question41.ques') or (wyborpytan == 'question42.ques') or (wyborpytan == 'question44.ques') or (wyborpytan == 'question49.ques') or (wyborpytan == 'question50.ques') or (wyborpytan == 'question52.ques') or (wyborpytan == 'question53.ques'):

    
        if pytaniesprawdz>0:
            messagebox.showinfo("Okno pytające","Dobrze! Udało ci się przesunąć o wylosowaną liczbę pól!")
            return rzut
         
        else:
            messagebox.showerror("Okno pytające","Żle! Zostajesz w miejscu!")
            return 0
    #elif wyborpytan == 'question2.ques':

     #   anserw.anserw()
     #   return rzut
    
    #elif wyborpytan == 'question4.ques':

     #   anserw.anserw()
     #   return rzut
    else:
        if pytaniesprawdz<1:
            messagebox.showinfo("Okno pytające","Dobrze! Udało ci się przesunąć o wylosowaną liczbę pól!")
            return rzut
        else:
            messagebox.showerror("Okno pytające","Żle! Zostajesz w miejscu!")
            return 0
 