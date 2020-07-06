from turtle import*
import math
import cmath
conf = True
tam =   int(input("Qual o tamanho da letra que gostaria?\n"))
larg =  int(input("Qual a largura da letra que gostaria?\n"))
def next_letter (x):
    pu()
    goto(x + 15, 0)
    pd()
    rt(90)
        
def penud(u,x,a):
    if u == 0:
        penup()
        fd(x)
        left(a)
    if u == 1:
        pendown()
        fd(x)
        left(a)

def letter (t1,t2,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16):
    h = math.hypot(t1,t2)
    penud(p1,t1/2,0)                                    #1 _    /2

    penud(p2,t1/2,90)                                   #2 _    /2
    x,y = pos()
    penud(p3,t2/2,0)                                    #3   |  /2
    penud(p4,t2/2,90)                                   #4   |  /2
    penud(p5,t1/2,0)                                    #5 -    /2
    penud(p6,t1/2,90)                                   #6 -    /2

    penud(p7,t2/2,0)                                    #7|     /2
    penud(p8,t2/2,180)                                  #8|     /2
    penud(0,t2/2,270)                                  
    penud(p9,t1/2,0)                                    #9 =    /2
    penud(p10,t1/2,90)                                 #10 =   /2
    penud(0,t2/2,90)
    penud(0,t1/2,90)
    penud(p11,t2/2,0)                                   #11 ||  /2
    penud(p12,t2/2,90)                                  #12 ||  /2
    penud(0,t1/2,math.degrees(math.atan(t1/t2) ) +90) 
    penud(p13,h/2,0)                                    #13 \    /2
    penud(p14,h/2,math.degrees(math.atan(t2/t1))-180)   #14 \    /2
    penud(0,t1,math.degrees(math.atan(t2/t1))-180)     
    penud(p15,h/2,0)                                    #15 /   /2
    penud(p16,h/2,math.degrees(math.atan(t1/t2))+180)   #16 /   /2
    pu()
    goto(0,0)
    pd()
    next_letter(x)

    
def A(a,l):
    letter(l,a,0,0,1,1,1,1,1,1 ,1,1,0,0 ,0,0,0,0)
def a(a,l):
    letter(l/2,a/2,1,1,1,1,1,1,0,1 ,1,1,0,0 ,0,0,0,0)
def B(a,l):
    letter(l,a,1,1,1,0,0,1,1,1 ,1,1,1,0 ,0,0,0,0)
def b(a,l):
    letter(l,a,1,0,0,0,0,0,1,1 ,1,0,0,1 ,0,0,0,0)
def C(a,l):
    letter(l,a,1,1,0,0,1,1,1,1 ,0,0,0,0 ,0,0,0,0)
def d(a,l):
    letter(l,a,1,0,0,0,0,0,0,1 ,1,0,1,1 ,0,0,0,0)
def E(a,l):
    letter(l,a,1,1,0,0,1,1,1,1 ,1,0,0,0 ,0,0,0,0)
def e(a,l):
    letter(l/2,a/2,1,1,0,1,1,1,1,1 ,1,1,0,0 ,0,0,0,0)
def F(a,l):
    letter(l,a,0,0,0,0,1,1,1,1 ,1,0,0,0 ,0,0,0,0)
def G(a,l):
    letter(l,a,1,1,1,0,1,1,1,1 ,0,1,0,0 ,0,0,0,0)
def ó (a,l):
    letter(l,a,0,0,0,0,0,0,0,0 ,0,0,1,1 ,0,0,0,0)
def i (a,l):
    letter(l,a,0,0,0,0,0,0,0,0 ,0,0,0,1 ,0,0,0,0)
def H (a,l):
    letter(l,a,0,0,1,1,0,0,1,1 ,1,1,0,0 ,0,0,0,0)
def h (a,l):
    letter(l,a,0,0,0,0,0,0,1,1 ,1,0,0,1 ,0,0,0,0)
def J (a,l):
    letter(l,a,1,0,0,0,1,1,0,0 ,0,0,1,1 ,0,0,0,0)
def K (a,l):
    letter(l,a,0,0,0,0,0,0,1,1 ,1,0,0,0 ,1,0,1,0)
def L (a,l):
    letter(l,a,1,1,0,0,0,0,1,1 ,0,0,0,0 ,0,0,0,0)
def M(a,l):
    letter(l,a,0,0,1,1,0,0,1,1 ,0,0,0,0 ,0,1,1,0)
def m (a,l):
    letter(l,a,0,0,1,0,0,0,0,1 ,1,1,0,1 ,0,0,0,0)
def N (a,l):
    letter(l,a,0,0,1,1,0,0,1,1 ,0,0,0,0 ,1,1,0,0)
def n (a,l):
    letter(l,a,0,0,0,0,0,0,0,1 ,1,0,0,1 ,0,0,0,0)
def O (a,l):
    letter(l,a,1,1,1,1,1,1,1,1 ,0,0,0,0 ,0,0,0,0)
def o (a,l):
    letter(l/2,a/2,1,1,1,1,1,1,1,1 ,0,0,0,0 ,0,0,0,0)
def P (a,l):
    letter(l,a,0,0,0,1,1,1,1,1 ,1,1,0,0 ,0,0,0,0)
def Q (a,l):
    letter(l,a,1,1,1,1,1,1,1,1 ,0,0,0,0 ,1,0,0,0)
def R (a,l):
    letter(l,a,0,0,0,1,1,1,1,1 ,1,1,0,0 ,1,0,0,0)
def r (a,l):
    letter(l,a,0,0,0,0,0,0,0,1 ,1,0,0,0 ,0,0,0,0)
def S(a,l):
    letter(l,a,1,1,1,0,1,1,1,0 ,1,1,0,0 ,0,0,0,0)
def T(a,l):
    letter(l,a,0,0,0,0,1,1,0,0 ,0,0,1,1 ,0,0,0,0)
def W (a,l):
    letter(l,a,0,0,1,1,0,0,1,1 ,0,0,0,0 ,1,0,0,1)
def U (a,l):
    letter(l,a,1,1,1,1,0,0,1,1 ,0,0,0,0 ,0,0
