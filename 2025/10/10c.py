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
import scipy
import sympy
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
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
b = np.array(lines[0][2])

#pprint(a)
#pprint(b)

#print(len(a),len(a[0]), len(b))
#print(scipy.linalg.solve(a,b))


pp = itertools.combinations(list(range(len(a))),len(b))
#print(list(pp))

for n in pp:
    v = [a[x] for x in range(len(a)) if x in n]
    #print(v)
    # print(len(v),len(b))
    try:
        x = scipy.linalg.solve(v, b)
        #       if (x>0).all():
        print("x:",x)
    except:
        pass


