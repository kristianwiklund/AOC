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

bl = lines[0][1]
targ = lines[0][2]

#print(bl)


print(targ)
pprint(bl)


