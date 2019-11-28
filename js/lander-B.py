#python3
# # Holdraszállás
# Bevezetés a számítógép programozásba 90 perc alatt, Python nyelven
# Kutatók Éjszakája, 2017
# Készítette: <írd ide a neved>

# Ide írjuk majd a programunkat.

import turtle
import random
import math
import time     # amikor túl gyors, esetleg teszünk majd bele lassítást

turtle.screensize(800,600)
turtle.bgcolor("grey")

def leszallas():
    urhajo = turtle.Turtle()
    urhajo.hideturtle()
    urhajo.penup()
    urhajo.shape("circle")
    urhajo.pen(fillcolor="pink", pencolor="blue")
    turtle.addshape("")
    urhajo.shape()

    # Az űrhajó mozgását leíró változók
    urhajo_x = random.randint(-400,-300) # random.randint( int(-1* (turtle.window_width() /2)) , int(-3/4*(turtle.window_width() /2)) )
    urhajo_y = random.randint(0.75*300, 300)  # random.randint( int(3/4*(turtle.window_height()/2)) , int(   1*(turtle.window_height()/2)) )
    urhajo_sebesseg = 7     # tapasztalati érték, játssz vele!

    urhajo.goto(urhajo_x, urhajo_y)
    urhajo.showturtle()
    urhajo.pendown() # így ki is rajzolja a röppályát, nem csak az aktuális pozíciót

    # A ferde hajítás paraméterei
    g = 3.711       # gravitációs állandó. A Földön: 9.807 m/s², a Holdon: 1.622 m/s², a Marson: 3.711 m/s², A Jupiteren: 24.79 m/s². Tapasztalati érték, játssz vele!
    szog_fok = 30   # légkörbe belépés szöge, tapasztalati érték, játssz vele!

    # feladat
    dt = 1      # szimulációs idő gyakoriság
    felszin_y = -270
    

    t = 0           # eltelt (relatív) idő
    a = 0           # gyorsulás   a+ = g*dt 
    v = 0           # sebesség

    urhajo.goto(urhajo_x, urhajo_y)

    while urhajo_y >= felszin_y:    # -0.9*(turtle.window_height()/2):
        
        # első, naiv megközelítés: menjen "45 fokban",
        # azaz 1 pixelt jobbra, 1 pixelt le
        # urhajo_x = urhajo_x + 1
        # urhajo_y = urhajo_y - 1
        a += g # g/dt
        v += a * dt
        urhajo_x += dt
        urhajo_y -= v*dt
        
        if urhajo_y > 0:
            urhajo.pencolor("green")
        elif urhajo_y >= 200: #-0.45*turtle.window_height()/2:
            urhajo.pencolor("yellow")
        else:   # -45% és -90% között van, a pálya utolsó szakaszában tartózkodik
            urhajo.pencolor("red")
        
        t += dt         # ha a mp felbontás túl gyors, akkor legyen 10x lassított felvétel
        time.sleep(dt/10)   # ha még mindig túl gyors, további lassítás altatással
        
        # ciklus vége
    # függvény vége
# ciklus utáni rész, ezt a kintebbi bekezdés jelzi

# Főprogram
leszallas()
#leszallas()
#leszallas()

# Program vége, de némely könyezetben azonnal be is zárná az ablakot.
# Ezért megállítjuk, és a konzol ablakban leütött Enter-re várunk.
# input("Program vége, nyomj Enter-t...")
