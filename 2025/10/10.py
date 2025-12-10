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
#import numpy as np
#import scipy
from functools import cache
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.short")

def pl(l):
    x,y=l.split("]")
    y,z=y.split("{")
    #    print(x,y,z)

    m = [list(x.replace("[","")),eval("("+y.lstrip().rstrip().replace(" ",",")+")"),eval("["+z.strip().replace("}","]"))]
    #    m = [list(x.replace("[","")),eval("["+y.lstrip().rstrip().replace(" ",",").replace("(","[").replace(")","]")+"]"),eval("["+z.strip().replace("}","]"))]
    return m


@cache
def flipper(button, lamps):

    if isinstance(button,int):
        button=[button]
        
    flip = {"#":".", ".":"#"}

    bock=""
    for i in range(len(lamps)):
        if i in button:
           bock+=flip[lamps[i]]
        else:
            bock+=lamps[i]

    return bock

assert(flipper((),".....")==".....")
assert(flipper((2),".....")=="..#..")
assert(flipper((2),"..#..")==".....")

def pb(l):

    a,b,c = pl(l)
    print(b,c)

    ap=eval("0b"+"".join(a).replace(".","0").replace("#","1"))

    for i in b:
        #        print(i)
        v=flipper(i,"."*len(a))
#        print(v)
        bp=eval("0b"+"".join(v).replace(".","0").replace("#","1"))
        print(bp)



#lines = [pl(x) for x in lines]
lines = [pb(x) for x in lines]
#print(lines)

@cache
def clickzor(lamps, button, target, buttons, depth=0, seen="", vom=10000000):

    if depth>vom:
        return False

    lamps = lamps ^ buttons[button]

print("part 1:",s)

