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
t_tgt_1 = Turtle()
t_tgt_2 = Turtle()
t_tgt_3 = Turtle()
t_winner1_2 = Turtle()
t_winner2_2 = Turtle()
t_winner3_2 = Turtle()
t_winner4_2 = Turtle()
t_winner5_2 = Turtle()

t_winner1_3 = Turtle()
t_winner2_3 = Turtle()
t_winner3_3 = Turtle()
t_winner4_3 = Turtle()
t_winner5_3 = Turtle()

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


t_tgt_1.ht()
t_tgt_2.ht()
t_tgt_3.ht()
t_tgt_1.pu()
t_tgt_2.pu()
t_tgt_3.pu()
t_tgt_1.goto(250,200)
t_tgt_2.goto(250,0)
t_tgt_3.goto(250,-200)

def new_arrow(x,y,a):
    obj_criation(arrows,   1,       x+49,   y,  bla,    cla,    a)
    
def calc_score(w,x1,x2,t,s,v):
    if w.distance(t) > x1 and w.distance(t) < x2:
        s.append(v)

def score(x,w,s,t):
    calc_score(w,  35,   82,    t,   s,  0)
    calc_score(w,  25,   35,    t,   s,  10)
    calc_score(w,  15,   25,    t,   s,  50)
    calc_score(w,  0,    15,    t,   s,  200)

def score_condition(w):
    if w.ycor() > 118:
        score(200,w,score1,t_tgt_1)  
    if w.ycor() < -118:
        score(-200,w,score3,t_tgt_3)
    else:
        score(0,w,score2,t_tgt_2)

def condition_walk(w,p,t):
    if w.distance(t) < 82 and randint(0,100) >= p:
        return True
    
def condition_walk_2(w,t):
    if w.distance(t) >= 118 and w.xcor() >= 250:
        return True
    
def condition_walk_3(w,p,t,g):
    if g == 1:
        if w.distance(t) > 10:
            score_condition(w)
            w.clear()
            arrows.remove(w)
    if condition_walk(w,p,t):
            w.fd(1)
    elif condition_walk_2(w,t):
        score_condition(w)
        w.clear()
        arrows.remove(w)
    else:
        score_condition(w)
        w.clear()
        arrows.remove(w)
    
def archer_arrow_walk(w,rand):
    if w.ycor() > 82:
        condition_walk_3(w,1,t_tgt_1,0)   
    if w.ycor() < -82:
        if rand == 1:
            condition_walk_3(w,1,t_tgt_3,0)
        else:
            condition_walk_3(w,0,t_tgt_3,1)

    if w.ycor() < 82 and w.ycor() > -82:
        condition_walk_3(w,0,t_tgt_2,1)
    
def arrow_walk(rand):
    while True:
        for w in arrows:
            w.speed(0)
            delay(0)
            w.pd()
            if w.distance(t_tgt_1) > 82 and w.xcor() < 250:
                w.fd(1)
            else:
                archer_arrow_walk(w,rand)
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
    
def winner():
    count = 1
    count_2 = 1
    count_3 = 1
    score_all = []
    score_all_s = []
    score_all.append(sum(score1))
    score_all.append(sum(score2))
    score_all.append(sum(score3))
    score_all_s.append(sum(score1))
    score_all_s.append(sum(score2))
    score_all_s.append(sum(score3))
    score_all_s.sort()
    for x in score_all:
        if x == score_all_s[-1]:
            written(t_winner1,-50,90,0,"O arqueiro ",0,8)
            written(t_winner2,10,90,0,count,0,10)
            written(t_winner3,23,90,0,"está ganhando!",0,8)
        else:
            count += 1
    for x in score_all:
        if x == score_all_s[1]:
            written(t_winner1_2,-50,60,0,"O arqueiro ",0,8)
            written(t_winner2_2,10,60,0,count_2,0,10)
            written(t_winner3_2,23,60,0,"está em segundo por :",0,8)
            written(t_winner4_2,150,60,0,score_all_s[-1]-x,0,10)
            written(t_winner5_2,190,60,0,"pontos",0,10)

        else:
            count_2 += 1
    for x in score_all:
        if x == score_all_s[0]:
            written(t_winner1_3,-50,30,0,"O arqueiro ",0,8)
            written(t_winner2_3,10,30,0,count_3,0,10)
            written(t_winner3_3,23,30,0,"está em terceiro por :",0,8)
            written(t_winner4_3,150,30,0,score_all_s[1]-x,0,10)
            written(t_winner5_3,190,30,0,"pontos",0,10)

        else:
            count_2 += 1

    del score_all
    del score_all_s

###     loop
while True:
    written(w1,50,200,score1,"Pts - ",1,8)
    written(w2,50,0,score2,"Pts - ",1,8)
    written(w3,50,-200,score3,"Pts - ",1,8)
    winner()
    r1 = uniform(10,-10)
    r2 = random()
    
    ###     archer 1
    new_arrow(-250,200,r1)
    bows[0].seth(r1)
    bows[1].seth(r1)
    
    ###     archer 2
    if time() > tempo + 2:
        new_arrow(-250,0,r2)
        tempo = time()
        bows[2].seth(r2)
        bows[3].seth(r2)
        
    ###     archer 3
    rand = randint(0,1)
    if time() > tempo + 1.2:
        if rand == 1: 
            new_arrow(-250,-200,r1)
            bows[4].seth(r1)
            bows[5].seth(r1)
        else:
            new_arrow(-250,-200,r2)
            bows[4].seth(r2)
            bows[5].seth(r2)
            
    arrow_walk(rand)
