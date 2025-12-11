import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache
from functools import lru_cache
import itertools

#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")


def tf(button,ln):

    ack=[]
    for i in range(ln):
        ack.append(1 if i in button else 0)

    return (ack)

assert(tf([0,2],4)==[1,0,1,0])

def pl(l):
    x,y=l.split("]")
    y,z=y.split("{")
    #    print(x,y,z)

    #m = [list(x.replace("[","")),eval("("+y.lstrip().rstrip().replace(" ",",")+")"),eval("["+z.strip().replace("}","]"))]
    m = [list(x.replace("[","")),eval("["+y.lstrip().rstrip().replace(" ",",").replace("(","[").replace(")","]")+"]"),eval("["+z.strip().replace("}","]"))]

    m[1] = sorted([tf(x,len(m[2])) for x in m[1]],key=lambda x:-sum(x))
    
    return m


lines=[pl(x) for x in lines]

# pl[2] contains the target
# pl[1] contains the button list

#print(lines[0])

# this is a multi-dimensional knapsack problem
# Here, the weight of knapsack item i is given by a D-dimensional vector (the buttons)
# and the knapsack has a D-dimensional capacity vector


def clack(vr, vp, clicks, mnum, ack):

        
    # subtract the clicks from the target state
    vr = deepcopy(vr)
    vr-=vp*mnum
    clicks+=mnum

    if sum(vr)==0:
        return clicks

#    print(vr)

    #    print(vr, bl)
    # no solution in this branch
    
    if not bl:
        return None

    kossan=None

    for i in range(len(bl)):
        if not i in ack:
            kalven=pluck(vr, i, bl, clicks, ack+[i])
        
            if  kalven and (not kossan or kalven<kossan):
                kossan=kalven
            
    return kossan

    


def pluck(remains, button, bl, clicks,ack=None):

    vr = np.array(remains)
    vp = np.array(bl[button])


    # first match if we can match anything with this button
    vd = vr*vp
    vd = vd[vd != 0]

    # no solution will happen with this button, we match nothing
    if not len(vd):
        return None

    # check that we are not trying to subtract from zeros
    y = sum([vr[i]>0 for i in range(len(vr)) if vp[i]>0])
    if y<sum(vp):
        return None

    # then run a descent for all options of clicks from 1 to min(vd)

    kossan=None
    for i in range(min(vd),max(0,min(vd)-2),-1):
#        print(ack,"clacking",i)
        kalven = clack(vr, vp, clicks, i, ack)
        if kalven and (not kossan or kalven<kossan):
            kossan = kalven
 
    return kossan


s=0
for l in lines:
    bl = l[1]
    targ = l[2]

    #print(bl)
    
    
    #    print(targ)
    #    pprint(bl)
    
    m=None
    for i in range(len(bl)):
        print("clicking button",i)
        n = pluck(targ, i,bl,0,[i])

        if n and (not m or n<m):
#            print(n)
            m=n

    if m:
        s+=m
    else:
        print("no solution found:", l)

print(s)
assert(s<128003850)
assert(s<167000508)



