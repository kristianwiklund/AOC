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

sys.exit()





@cache
def clickzor(li,bu, m0,m1,de=0, seen=None,vom=100000,clickety=""):

    if de>=vom:
        return False
    
    # get which bits are manipulated with d
    d = m1[bu]

    # flip the bits
    li = flipper(d,li)

    # if already seen, no point in continuing
    if li in seen:
        return False

    # add to seen list
    seen+=li
    
    zor=[]
    # check if we have a match
    if li==m0:
#        print(clickety)
        return de,clickety
    
    for i in range(len(m1)):
        # pressing the same button will flip it back, don't go there
        if i==bu:
            continue

        # perss button i. 
        dum=clickzor(li,i,m0,m1,de+1,seen,vom,clickety+","+str(i))
        if dum:
            ge,zork = dum
            if ge and ge<vom:
                vom=ge
                zor=zork
            
    return vom,zor

# run through the problems, flip them off...
s=0
for m in lines:
    print("---",m)
    i = "."*len(m[0])
#    print("m0m1=",m[0],m[1])
    r = sorted(map(lambda x:clickzor(i, x, "".join(m[0]),m[1], de=1, seen=i,clickety=str(x))[0], range(len(m[1]))))
    s+=r[0]


print("part 1:",s)

