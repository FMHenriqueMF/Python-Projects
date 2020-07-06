from turtle import*
from random import *

def anda():
    forma = 1
    for t in range(1000000):
        x_inicial,y_inicial = pos()
        if (x_inicial < 100) and (x_inicial > -100) and (y_inicial < 100) and (y_inicial > -100):
            forward(7)
            right( randint(-90,90) )
            x_final,y_final = pos()
            if (x_final > 0 and x_inicial < 0) or (x_final < 0 and x_inicial > 0) or (y_final > 0 and y_inicial < 0) or (y_final < 0 and y_inicial > 0):
                if forma == 1:
                    shape("turtle")
                if forma == 2:
                    shape("circle")
                if forma == 3:
                    shape("square")
                if forma == 4:
                    forma = 0
                forma = forma + 1
            if t % 30 == 0:
                color( (randint(0,255),randint(0,255),randint(0,255)) )
        else:
            for _ in range(5):
                undo()
    
def limite(b,h,mc,mb
           ):
    goto(0,mc)
    goto(0,mb)
    pu()
    goto(mb,0)
    pd()
    goto(mc,0)
    pu()
    goto(-b/2,-h/2)
    pd()
    for _ in range(2):
        fd(b)
        left(90)
        fd(h)
        left(90)
    pu()
    goto(0,0)
    pd()
    
speed(0)
colormode(255) # para usar cores em RGB
limite(200,200,100,-100)
anda()
