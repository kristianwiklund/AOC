import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")
bots = [ints(l) for l in lines]

#Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall.

if len(lines) <= 12:
    BY=7
    BX=11
else:
    BX=101
    BY=103


def quack(bots):

    def ww(t,r):
        if t<r//2:
            v=-1
        elif t>r//2:
            v=1
        else:
            v=0

        return v

            
    sf = {(-1,1):0,(-1,-1):0,(1,-1):0,(1,1):0}
    
    for px,py,vx,vy in bots:
        s = [ww(px,BX),ww(py,BY)]
        
        #print((px,py),((BX//2),(BY//2)),s)
        if not 0 in s:
            sf[(s[0],s[1])]+=1
        #print("--")

#    print(sf)
    
    return sf
    

def tick(bots):

    def w(p,b):
        if p<0:
            return p+b
        elif p>=b:
            return p-b
        return p
    
    rots = []

    for px,py,vx,vy in bots:
        rots.append([w(px+vx,BX), w(py+vy,BY), vx, vy])

    return rots

def check(bots,t):
    m = {}
    t = True
    tt=0
    vots = [(x,y) for x,y,z,w in bots]
    
    for yy in range(BY):
        if (BX//2,yy) in vots:
            tt+=1

    if tt>=BY//2:
        return True
    else:
        return False

from clear_screen import clear

def printzor(bots,ttt):
    clear()
    vots = [(x,y) for x,y,z,w in bots]
    for y in range(BY):
        for x in range(BX):
            if not (x,y) in vots:
                print(" ",end="")
            else:
                print("*",end="")

        print("")
    print("---",ttt,"---")

mt=0

for ttt in range(100):
    bots = tick(bots)
    mt+=1
#    s = quack(bots)
#    if s[(-1,-1)]<s[(-1,1)]/5 and s[(1,-1)]<s[(1,1)]/5:
#        printzor(bots,ttt)
#    if check(bots,ttt):
#        printzor(bots,ttt)


s = quack(bots)
print(s)
vots = [(x,y) for x,y,z,w in bots]

if len(lines)<=12:
    c=0
    for y in range(BY):
        for x in range(BX):
            if not (x,y) in vots:
                if y==BY//2 or x==BX//2:
                    print(" ",end="")
                else:
                    print(".",end="")                
            else:
                print(sum([1 for (tx,ty) in vots if (tx,ty)==(x,y)]),end="")
                while (x,y) in vots:
                    vots.remove((x,y))
                c+=1
        print("")

    print(c,"printed",len(bots),"in list")
    print([(x,y) for x,y,z,w in bots])
    print(vots)
    
print(s[(-1,1)]*s[(-1,-1)]*s[(1,-1)]*s[(1,1)])
        
while True:
    bots = tick(bots)
    mt+=1
    s = quack(bots)
    if ttt>7800 and ttt<7900 and s[(-1,-1)]<s[(-1,1)]/2 and s[(1,-1)]<s[(1,1)]/2:
        print(s)
        printzor(bots,mt)
        
#    v=check(bots,ttt)
#    if v:
#        printzor(bots,ttt)
    ttt+=1

