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
lines = readlines("input")

def pl(l):
    x,y=l.split("]")
    y,z=y.split("{")
    #    print(x,y,z)

    m = [list(x.replace("[","")),eval("("+y.lstrip().rstrip().replace(" ",",")+")"),eval("["+z.strip().replace("}","]"))]
    #    m = [list(x.replace("[","")),eval("["+y.lstrip().rstrip().replace(" ",",").replace("(","[").replace(")","]")+"]"),eval("["+z.strip().replace("}","]"))]
    return m

lines=[pl(x) for x in lines]

@cache
def clickzor(jolts, button, target, buttons, depth=0,  vom=100):

    if depth>=vom:
        return False

    jolts = list(jolts)
    ac=[]
    for x in range(len(jolts)):
        if isinstance(buttons[button],int):
            b=[buttons[button]]
        else:
            b=buttons[button]

#        print(b)
        if x in list(b):
#            print(x,"-",jolts,"-",b,jolts[x])
            y = jolts[x]+1
            ac.append(y)
            if ac[-1]>target[x]:
                return False
        else:
 #           print(x)
            ac.append(jolts[x])
            
    jolts=tuple(ac)
    if jolts==target:
        return depth
    
    for i in range(len(buttons)):
        if i==button:
            continue

        res = clickzor(jolts, i, target, buttons, depth+1, vom)
        if res and res<vom:
            vom=res

 #   print("JT",jolts,target)
    return vom


# run through the problems, flip them off...
s=0
for m in lines:
    print("---",m,len(m[0]))
    v = tuple([0]*len(m[0]))
#    print(v)
    r = sorted(map(lambda x:clickzor(v, x, tuple(m[2]),tuple(m[1]), depth=1), range(len(m[1]))))
    s+=r[0]
#    print(r)
print("part 1:",s)

