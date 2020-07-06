from turtle import*
from random import*
qtd_turtle = int(input("qtd de turtle\n"))
tts = []
delay(0)
cnt = 0
ang = 0
t = False
e = False
for c in range(qtd_turtle):
    tts.append( Turtle() )
    tts[c].speed(0)
    tts[c].seth(ang)
    tts[c].ht()
    ang = ang + 360/qtd_turtle

while True:
    r = randint(1,360)
    for a in tts:
        x,y = a.pos()
        if cnt == 10:
            a.left(r)
            t = True
        else:
            a.fd(10)
        if x > 400 or x < -400 or y >300 or y < -300:
            e = True
    cnt = cnt+1
    if t == True:
        cnt = 0
        t = False
    if e == True:
        for a in tts:
            a.goto(0,0)
        e = False
    


        

