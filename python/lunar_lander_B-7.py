# Holdraszállás 1.1
# Bevezetés a számítógép programozásba 90 perc alatt, Python nyelven
# Kutatók Éjszakája, 2020
# Készítette: <írd ide a neved>

# Ide írjuk majd a programunkat.
import turtle
import random
import math
import time      # amikor túl gyors, esetleg teszünk majd bele lassítást
import logging   # közbenső adatok kijrása konzolra

# A gravitáció hajítás paraméterei
g = 3.711          # gravitációs állandó. A Földön: 9.807 m/s², a Holdon: 1.622 m/s², a Marson: 3.711 m/s², A Jupiteren: 24.79 m/s². Tapasztalati érték, játssz vele!
ero = 8            # az urhajó rakétájának ereje
N = 5              # szimulációk száma
dt = 0.5           # szimulációs segédváltozó, idő gyakoriság (másodpercben)
felszin_y = -270   # a talaj magasságszintje

turtle.screensize(800,600)
turtle.bgcolor("grey")         # az ég színe a marson

def leszallas():
    urhajo = turtle.Turtle()
    urhajo.hideturtle()
    urhajo.penup()
    urhajo.shape("triangle")     # az ürhajó alakja
    urhajo.setheading(90)        # .. felfelé nézzen
    urhajo.pen(fillcolor="lightblue", pencolor="blue", pensize=5)

    # Az űrhajó kezdeti helye
    urhajo_x = random.randint(-400,-300)      # random.randint( int(-1* (turtle.window_width() /2)) , int(-3/4*(turtle.window_width() /2)) )
    urhajo_y = random.randint(0.75*300, 300)  # random.randint( int(3/4*(turtle.window_height()/2)) , int(   1*(turtle.window_height()/2)) )

    urhajo.goto(urhajo_x, urhajo_y)
    urhajo.showturtle()
    urhajo.pendown() # így ki is rajzolja a röppályát, nem csak az aktuális pozíciót

    # feladat
    v_x0 = random.randint(1,15)    # kezdeti oldalirányú sebesség (állandó)
    a_y0 = random.randint(-10,10)  # kezdeti zuhanási gyorsulás

    t = 0           # eltelt (relatív) idő
    a = a_y0        # kezdő zuhanó gyorsulás
    v_x = v_x0
    v_y = a_y0           # gyorsulás   a+ = g*dt 

    while urhajo_y >= felszin_y:    # -0.9*(turtle.window_height()/2):
        # első, naiv megközelítés: menjen "45 fokban",
        # azaz 1 pixelt jobbra, 1 pixelt le
        if urhajo_y > 0:
            urhajo.pencolor("green")
        elif urhajo_y >= -200: #-0.45*turtle.window_height()/2:
            urhajo.pencolor("yellow")
        else:   # -45% és -90% között van, a pálya utolsó szakaszában tartózkodik
            urhajo.pencolor("red")

        a = -g * dt # gravitáció, a másodperc törédékében (dt)
        # hajtóművek bekapcsolása
        if urhajo_y < 100 and v_y < -20: #-0.45*turtle.window_height()/2:
            urhajo.fillcolor("red")
            a += ero * dt
        else:
            urhajo.fillcolor("lightblue")

        v_y += a               # a sebesség változása, a zuhanás/gyorsulástól függően
        urhajo_x += v_x * dt   # oldalra mozgás (sodródás)
        urhajo_y += v_y * dt   # dt idő alatt megtett út
        
        urhajo.goto(urhajo_x, urhajo_y)
        print("  v:"+str(round(v_y,2))+" x:"+str(round(urhajo_x,2))+" y:"+str(int(urhajo_y))+" a:"+str(round(a,3))) 
        
        t += dt         # ha a mp felbontás túl gyors, akkor legyen 10x lassított felvétel
        time.sleep(dt/10)   # ha még mindig túl gyors, további lassítás altatással
        
        # ciklus vége
    urhajo.fillcolor("lightblue")
    urhajo.write("  v:" + str(round(v_y,2)) + " a:"+str(round(a/dt,3)), False) 
    # függvény vége
# ciklus utáni rész, ezt a kintebbi bekezdés jelzi

# Főprogram
i = 1
while i <= N:
    leszallas()
    i += 1

# Program vége, de némely könyezetben azonnal be is zárná az ablakot.
# Ezért megállítjuk, és a konzol ablakban leütött Enter-re várunk.
# input("Program vége, nyomj Enter-t...")
