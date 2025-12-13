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
lines = readlines("input.short")

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

    m[1] = [tf(x,len(m[2])) for x in m[1]]
    
    return m


lines=[pl(x) for x in lines]

a = np.array(lines[1][1])
pprint(a)
a = np.transpose(a)
b = np.array(lines[1][2])

for i,v in enumerate(a):
    print (v,"=",b[i])


