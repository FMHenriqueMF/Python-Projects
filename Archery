from turtle import*
from random import*
from time import*
tempo = time()

###     shapes
sqr = "square"
cla = "classic"
cir = "circle"

###     colors
bla = "black"
red = "red"
yel = "yellow"

###     lists
turtles = []
arrows = []
score1 = []
score2 = []
score3 = []
bows = []


### turtles
w1 = Turtle()
w2 = Turtle()
w3 = Turtle()
t_winner1 = Turtle()
t_winner2 = Turtle()
t_winner3 = Turtle()
    
def obj_criation(l,s,x,y,c,f,a):
    delay(0)
    l.append(Turtle())
    r = l[-1]
    r.ht()
    r.pu()
    r.shape(f)
    r.shapesize(s)
    r.color(c)
    r.goto(x,y)
    r.st()
    r.seth(a)
    
def criation(c,x,y,s):
    ###     archers
    obj_criation(turtles,   s+0.2,  x,      y,  bla,    sqr,    0)
    obj_criation(turtles,   s,      x,      y,  c,      sqr,    0)  
    ###     bows
    obj_criation(turtles,   2.9,    x+49,   y,  bla,    cla,    0)
    bows.append(turtles[-1])
    obj_criation(turtles,   2.5,    x+45,   y,  c,      cla,    0)
    bows.append(turtles[-1])
    ###     targets
    obj_criation(turtles,   3.5,    x+500,  y,  bla,    cir,    0)  ###35
    obj_criation(turtles,   2.5,    x+500,  y,  yel,    cir,    0)  ###25
    obj_criation(turtles,   1.5,    x+500,  y,  red,    cir,    0)  ###15
criation("red",   -250,   200,    2)
criation("green", -250,   0,      2)
criation("blue",  -250,   -200,   2)

def new_arrow(x,y,a):
    obj_criation(arrows,   1,       x+49,   y,  bla,    cla,    a)
    
def calc_score(x1,x2,w,x3,x4,s,v):
    if w.ycor() >= x1 and w.ycor() < x2 or w.ycor() >= x3 and w.ycor() < x4:
        s.append(v)

def score(x,w,s,l):
    calc_score(x-82,     x-35,   w,  x+35,   x+82,   s,  0)
    calc_score(x-35,     x-25,   w,  x+25,   x+35,   s,  10)
    calc_score(x-25,     x-15,   w,  x+15,   x+25,   s,  50)
    calc_score(x-15,     x,      w,  x,      x+15,   s,  200)
           
def arrow_walk():
    global scor1
    global scor2
    global scor3
    while True:
        for w in arrows:
            w.speed(0)
            delay(0)
            if w.xcor() < 251:
                w.pd()
                w.fd(1)
            else:
                if w.ycor() > 118:
                    score(200,w,score1,"1")  
                if w.ycor() < -118:
                    score(-200,w,score3,"3")
                else:
                    score(0,w,score2,"2")
                w.clear()
                arrows.remove(w)                
        if len(arrows) <= 0:
            break
        
def written(w,x,y,s,p,t,n):
    w.reset()
    w.pu()
    w.ht()
    w.goto(x,y)
    w.write(p,True, align="left",font = ("Arial",n,"normal"))
    w.goto(x+45,y)
    if t == 1:
        w.write(sum(s),True,align="center")
    
def add_score_winner(l,s):
    l.append(sum(s))
    
def winner():
    count = 1
    score_all = []
    score_all_s = []
    add_score_winner(score_all,score1)
    add_score_winner(score_all,score2)
    add_score_winner(score_all,score3)
    add_score_winner(score_all_s,score1)
    add_score_winner(score_all_s,score2)
    add_score_winner(score_all_s,score3)
    score_all_s.sort()
    for x in score_all:
        if x == score_all_s[-1]:
            written(t_winner1,0,50,0,"O arqueiro ",0,8)
            written(t_winner2,60,50,0,count,0,10)
            written(t_winner3,73,50,0,"está ganhando!",0,8)
            
        else:
            count += 1
            
    
    
    del score_all
    del score_all_s


###     loop
while True:
    written(w1,150,200,score1,"Pts - ",1,8)
    written(w2,150,0,score2,"Pts - ",1,8)
    written(w3,150,-200,score3,"Pts - ",1,8)
    winner()
    r1 = uniform(10,-10)
    r2 = random()
    
    ###     archer 1
    new_arrow(-250,200,r1)
    bows[0].seth(r1)
    bows[1].seth(r1)
    
    ###     archer 2
    if time() > tempo + 1.5:
        new_arrow(-250,0,r2)
        tempo = time()
        bows[2].seth(r2)
        bows[3].seth(r2)
        
    ###     archer 3
    if time() > tempo + 1:
        rand = randint(0,1)
        if rand == 1: 
            new_arrow(-250,-200,r1)
            bows[4].seth(r1)
            bows[5].seth(r1)
        else:
            new_arrow(-250,-200,r2)
            bows[4].seth(r2)
            bows[5].seth(r2)
            
    arrow_walk()
    
    



