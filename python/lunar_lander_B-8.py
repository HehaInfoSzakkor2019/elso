# Holdraszállás
# Bevezetés a számítógép programozásba 90 perc alatt, Python nyelven
# Kutatók Éjszakája, 2017
# Készítette: <írd ide a neved>

# Ide írjuk majd a programunkat.
import turtle
import random
import math
import time     # amikor túl gyors, esetleg teszünk majd bele lassítást
import logging

N = 5

turtle.screensize(800,600)
                
turtle.bgcolor("grey")

def leszallas():
    urhajo = turtle.Turtle()
    urhajo.hideturtle()
    urhajo.penup()
    urhajo.shape("triangle")
    urhajo.setheading(90)
    urhajo.pen(fillcolor="lightblue", pencolor="blue", pensize=5)
    #urhajo.shape("raketa-B1.png")

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
    ero = 8

    # feladat
    dt = 0.5      # szimulációs idő gyakoriság
    felszin_y = -270

    v_x0 = random.randint(1,15)
    a_y0 = random.randint(-1,5)

    t = 0           # eltelt (relatív) idő
    a = a_y0        # kezdő zuhanó gyorsulás
    v_x = v_x0
    v_y = a_y0           # gyorsulás   a+ = g*dt 


    urhajo.goto(urhajo_x, urhajo_y)

    while urhajo_y >= felszin_y:    # -0.9*(turtle.window_height()/2):
        # első, naiv megközelítés: menjen "45 fokban",
        # azaz 1 pixelt jobbra, 1 pixelt le
        # urhajo_x = urhajo_x + 1
        # urhajo_y = urhajo_y - 1
        if urhajo_y > 0:
            urhajo.pencolor("green")
        elif urhajo_y >= -200: #-0.45*turtle.window_height()/2:
            urhajo.pencolor("yellow")
        else:   # -45% és -90% között van, a pálya utolsó szakaszában tartózkodik
            urhajo.pencolor("red")

        # hajtóművek bekapcsolása
        a = -g * dt # g/dt
        if urhajo_y < 100 and v_y < -20: #-0.45*turtle.window_height()/2:
            urhajo.fillcolor("red")
            a += ero * dt
        elif urhajo_y < 0 and v_y < -10: #-0.45*turtle.window_height()/2:
            urhajo.fillcolor("red")
            a += ero * dt
        else:
            urhajo.fillcolor("lightblue")

        v_y += a
        urhajo_x += v_x * dt
        urhajo_y += v_y * dt
        
        urhajo.goto(urhajo_x, urhajo_y)
        print("  v:"+str(round(v_y,2))+" x:"+str(round(urhajo_x,2))+" y:"+str(int(urhajo_y))+" a:"+str(round(a,3))) 
        
        t += dt         # ha a mp felbontás túl gyors, akkor legyen 10x lassított felvétel
        time.sleep(dt/10)   # ha még mindig túl gyors, további lassítás altatással
        #time.sleep(1)
        
        # ciklus vége
    urhajo.fillcolor("lightblue")
    urhajo.write("  v:" + str(round(v_y,2)) + " a:"+str(round(a/dt,3)), False) 
    # függvény vége
# ciklus utáni rész, ezt a kintebbi bekezdés jelzi

# Főprogram
i = 1
while i < N:
    leszallas()
    i += 1

# Program vége, de némely könyezetben azonnal be is zárná az ablakot.
# Ezért megállítjuk, és a konzol ablakban leütött Enter-re várunk.
# input("Program vége, nyomj Enter-t...")
