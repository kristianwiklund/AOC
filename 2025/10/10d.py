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
#import scipy
#import sympy
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.shortest",split="",convert=lambda x:x)
lines = readlines("input.short.3")

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

a = np.array(lines[0][1])
#print(a)
a = np.transpose(a)
b = np.array(lines[0][2])

#print(a,b)

e = []
from sympy import solve, solve_linear, solve_linear_system, Symbol, reduce_inequalities

sy=[]
for i,x in enumerate(a[0]):
    sy.append(Symbol("B"+str(i)))
#    e.append(sy[i]>0)
#print(sy)

for i,v in enumerate(a):
    s=[]
    for x,w in enumerate(v):
        if w:
            s.append("sy["+str(x)+"]")
    
    e.append(eval("+".join(s)+"-"+str(b[i])))

#print(e)
e.append(sy[2])
kossan=None

for i,s in enumerate(sy):
#    print("dropping button",i)
    e.pop(-1)
    e.append(sy[i])

    try:
        ap = solve(e,sy)
        x = sum([1 for x in ap if ap[x]>=0])
        if x==len(ap):
            v = sum([ap[x] for x in ap])
            if not kossan or v<kossan:
                kossan = v

    except:
        pass

print(kossan)

#s = solve(e,sy)
#print(s)



