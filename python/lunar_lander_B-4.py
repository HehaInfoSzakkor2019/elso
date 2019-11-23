# Holdraszállás 1.1
# Bevezetés a számítógép programozásba 90 perc alatt, Python nyelven
# Kutatók Éjszakája, 2020
# Készítette: <írd ide a neved>

# Ide írjuk majd a programunkat.
import turtle
import random
import math
import time      # amikor túl gyors, esetleg teszünk majd bele lassítást

# A gravitáció hajítás paraméterei
g = 3.711          # gravitációs állandó. A Földön: 9.807 m/s², a Holdon: 1.622 m/s², a Marson: 3.711 m/s², A Jupiteren: 24.79 m/s². Tapasztalati érték, játssz vele!
dt = 1           # szimulációs segédváltozó, idő gyakoriság (másodpercben)
felszin_y = -270   # a talaj magasságszintje

turtle.screensize(800,600)
turtle.bgcolor("grey")         # az ég színe a marson


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
a = a_y0        # pillanatnyi gyorsulás
v_x = v_x0      # sebesség X tengelyen
v_y = 0      # pillanatnyi sebesség

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
    v_y += a               # a sebesség változása, a zuhanás/gyorsulástól függően
    urhajo_x += v_x * dt   # oldalra mozgás (sodródás)
    urhajo_y += v_y * dt   # dt idő alatt megtett út
    
    urhajo.goto(urhajo_x, urhajo_y)
    
    t += 1             # dt, ha a mp felbontás túl gyors, akkor legyen 10x lassított felvétel
    time.sleep(0.1)    # ha még mindig túl gyors, további lassítás altatással
    
    # ciklus vége
# ciklus utáni rész, ezt a kintebbi bekezdés jelzi

# Program vége, de némely könyezetben azonnal be is zárná az ablakot.
# Ezért megállítjuk, és a konzol ablakban leütött Enter-re várunk.
# input("Program vége, nyomj Enter-t...")
