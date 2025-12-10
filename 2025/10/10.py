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
#from functools import cache
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.short")

def pl(l):
    x,y=l.split("]")
    y,z=y.split("{")
    #    print(x,y,z)

    m = [list(x.replace("[","")),eval("["+y.lstrip().rstrip().replace(" ",",").replace("(","[").replace(")","]")+"]"),eval("["+z.strip().replace("}","]"))]
    return m
    
lines = [pl(x) for x in lines]
#print(lines)


def flipper(button, lamps):

    flip = {"#":".", ".":"#"}

    bock=""
    for i in range(len(lamps)):
        if i in button:
           bock+=flip[lamps[i]]
        else:
            bock+=lamps[i]

    return bock

assert(flipper([],".....")==".....")
assert(flipper([2],".....")=="..#..")
assert(flipper([2],"..#..")==".....")



def clickzor(li,bu, m,de=0, seen=None,vom=100000):

    if de>=vom:
        return False
    
    # get which bits are manipulated with d
    d = m[1][bu]

    # flip the bits
    li = flipper(d,li)

    # if already seen, no point in continuing
    if "".join(li) in seen:
        return False

    # add to seen list
    seen=deepcopy(seen)
    seen.append("".join(li))

    zor=[]
    # check if we have a match
    if "".join(li)=="".join(m[0]):
        return de,seen
    
    for i in range(len(m[1])):
        # pressing the same button will flip it back, don't go there
        if i==bu:
            continue

        # perss button i. 
        dum=clickzor(li,i,m,de+1,seen,vom)
        if dum:
            ge,zork = dum
            if ge and ge<vom:
                vom=ge
                zor=zork
            
    return vom,zor

# run through the problems, flip them off...
for m in lines:
    print("---",m)
    for i in range(len(m[1])):
        print(i, clickzor(list("."*len(m[0])), i, m,de=1,seen=["."*len(m[0])]))

