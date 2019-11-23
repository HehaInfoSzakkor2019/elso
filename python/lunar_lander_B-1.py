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
dt = 1             # szimulációs segédváltozó, idő gyakoriság (másodpercben)
felszin_y = -270   # a talaj magasságszintje

turtle.screensize(800,600)
turtle.bgcolor("grey")         # az ég színe a marson


urhajo = turtle.Turtle()
urhajo.hideturtle()
urhajo.penup()

# Az űrhajó kezdeti helye
urhajo_x = random.randint(-400,-300)      # random.randint( int(-1* (turtle.window_width() /2)) , int(-3/4*(turtle.window_width() /2)) )
urhajo_y = random.randint(0.75*300, 300)  # random.randint( int(3/4*(turtle.window_height()/2)) , int(   1*(turtle.window_height()/2)) )

urhajo.goto(urhajo_x, urhajo_y)
urhajo.showturtle()
urhajo.pendown() # így ki is rajzolja a röppályát, nem csak az aktuális pozíciót

# ciklus utáni rész, ezt a kintebbi bekezdés jelzi

# Program vége, de némely könyezetben azonnal be is zárná az ablakot.
# Ezért megállítjuk, és a konzol ablakban leütött Enter-re várunk.
# input("Program vége, nyomj Enter-t...")
