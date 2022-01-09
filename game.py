import pygame
from tkinter import messagebox
from random import *
import questionsystem


def play():
    global poleaktualne

    m='Kliknij spację by losować numer'

    g=pygame.init()
    screen= pygame.display.set_mode((1920,1080))

    color=(100,100,100)
    color_red = (255,0,0)
    color_black = (0, 0, 0)
    color_szary = (47,79,79)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render(m , True , color)
    box=pygame.Rect(10,10,50,50)
    x=400
    y=150
    szer=50
    wys=50
    plansza_szer = 1900
    plansza_wys = 1000
    margines=5
    poleaktualne=-1
    polepoprzednie=-2
    #rzad1 = [[0,0],[100,0],[200,0],[300,0],[400,0],[500,0],[600,0],[700,0],[800,0],[900,0]]
    rzad1=[]
    #rzad2 = [[0,100],[100,100],[200,100],[300,100],[400,100],[500,100],[600,100],[700,100],[800,100],[900,100]]
    rzad2=[]
    rzad3=[]
    rzad4=[]
    rzad5=[]
    rzad6=[]
    rzad7=[]
    rzad8=[]
    rzad9=[]
    rzad10=[]
    rzad11=[]
    pierwszepole = 0
    ostatniepole = 112

    krok_x = x + margines
    krok_y = y+margines+4
    for j in range(0,18):
        rzad1.append([krok_x,krok_y])
        krok_x = krok_x + szer + margines
   
    krok_x=krok_x - szer - margines
    krok_y=krok_y + wys + 2* margines + 8
    rzad2.append([krok_x,krok_y])

    krok_y=krok_y + wys + 2* margines + 8
    for j in range(0,18):
        rzad3.append([krok_x,krok_y])
        krok_x = krok_x - szer - margines

    krok_x = x + margines
    krok_y=krok_y + wys + 2* margines + 8
    rzad4.append([krok_x,krok_y])

    krok_y=krok_y + wys + 2* margines + 8
    for j in range(0,18):
        rzad5.append([krok_x,krok_y])
        krok_x = krok_x + szer + margines

    krok_x=krok_x - szer - margines
    krok_y=krok_y + wys + 2* margines + 8
    rzad6.append([krok_x,krok_y])

    krok_y=krok_y + wys + 2* margines + 8
    for j in range(0,18):
        rzad7.append([krok_x,krok_y])
        krok_x = krok_x - szer - margines

    krok_x = x + margines
    krok_y=krok_y + wys + 2* margines + 8
    rzad8.append([krok_x,krok_y])

    krok_y=krok_y + wys + 2* margines + 8
    for j in range(0,18):
        rzad9.append([krok_x,krok_y])
        krok_x = krok_x + szer + margines

    krok_x=krok_x - szer - margines
    krok_y=krok_y + wys + 2* margines + 8
    rzad10.append([krok_x,krok_y])

    krok_y=krok_y + wys + 2* margines + 8
    for j in range(0,18):
        rzad11.append([krok_x,krok_y])
        krok_x = krok_x - szer - margines


    plansza = rzad1 + rzad2+ rzad3+rzad4+rzad5+rzad6+rzad7+rzad8+rzad9+rzad10+rzad11
    #print(plansza)
     
    # kreski poziome
    krok = y
    for i in range(1,13):
        m=pygame.draw.rect(screen,color_szary, (x,krok,(szer+2*margines)*19-19*8+4,4))
        krok = krok + wys + 2*margines+8
    
    # kreski pionowe
    krok_y = y
    for j in range(1,7):
        krok = x
        for i in range(1,20):
            m=pygame.draw.rect(screen,color_szary, (krok,krok_y,4,wys+margines*2+8))
            krok = krok + szer + margines
        krok_y=krok_y+2*(wys+2*margines)+16
    
    # kwadraty brakujące prawa
    krok = x + (szer+2*margines)*15 + 32
    krok_y =y + (wys+2*margines) + 12
    for i in range(1,4):
        m=pygame.draw.rect(screen,color_szary, (krok,krok_y,4,wys+margines*2+4))
        m=pygame.draw.rect(screen,color_szary, (krok+(szer+2*margines),krok_y,4,wys+margines*2+4))
        krok_y = krok_y+2*(2*(wys+2*margines)+16)
    
    # kwadraty brakujące lewa
    krok = x
    krok_y =y + 3*((wys+2*margines)+8)
    for i in range(1,3):
        m=pygame.draw.rect(screen,color_szary, (krok,krok_y,4,wys+margines*2+8))
        m=pygame.draw.rect(screen,color_szary, (krok+(szer+margines),krok_y,4,wys+margines*2+8))
        krok_y = krok_y+2*(2*(wys+2*margines)+16)
    
    while True:
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:  
                e=messagebox.askyesno("game.exe","Chcesz wyjść z gry?")     
                if e>0:                              
                    pygame.quit()
                
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            polepoprzednie=poleaktualne
            poleaktualne = poleaktualne+questionsystem.ask() 
            if poleaktualne==polepoprzednie:
                polepoprzednie=-1
        


        if poleaktualne < pierwszepole:
           poleaktualne = pierwszepole

        if poleaktualne >= ostatniepole:
            poleaktualne = ostatniepole
   
        if keys[pygame.K_ESCAPE]:
            ee=messagebox.askyesno("game.exe","Chcesz wyjść z gry?") 
            if ee>0:                              
                pygame.quit()
            
        m=pygame.draw.rect(screen,color_red, (plansza[poleaktualne][0],plansza[poleaktualne][1],szer,wys))
        if (polepoprzednie>=pierwszepole) and (polepoprzednie<=ostatniepole):
            m=pygame.draw.rect(screen,color_black, (plansza[polepoprzednie][0],plansza[polepoprzednie][1],szer,wys))

        if poleaktualne >= ostatniepole:
            messagebox.showinfo('game.exe','udało ci się ukończyć grę')
            pygame.quit()
        
        screen.blit(text , (width/2.54,height/39))
        
        pygame.display.update()