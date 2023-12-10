import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
import scipy.ndimage
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

#pprint(arr)

ttt= time.perf_counter_ns()


orr = ["|7F","-J7","|LJ","-LF"]
od = [(0,-1),(1,0),(0,1),(-1,0)]

def findstart(arr,x,y):
    global orr, od
    
    assert(arr[y][x]=='S')

    for i in range(len(od)):
        (dx,dy) = od[i]
        pp = orr[i]
        if checkpos(arr,x+dx, y+dy, lambda v:v in pp, outofbounds=False):
            return i


[(x,y)]=[(x,y) for x in range(len(arr[0])) for y in range(len(arr)) if arr[y][x]=='S']
        
d =  findstart(arr,x,y)
#print("Initial: ", d, x,y)

def findmove(arr, d, x, y):
    global orr, dd

    me = arr[y][x]

    # this can be done with an array
    match me:
        case "|":
            d = d # continue straight ahead
        case "-":
            d = d # continue straight ahead
        case "L":
            if d==2:
                d=1
            else:
                d=0
        case "F":
            if d==0:
                d=1
            else:
                d=2
        case "J":
            if d==1:
                d=0
            else:
                d=3
        case "7":
            if d==0:
                d=3
            else:
                d=2
    return d


ta=[['-', 'L', '|', 'F', '7'], ['7', 'S', '-', '7', '|'], ['L', '|', '7', '|', '|'], ['-', 'L', '-', 'J', '|'], ['L', '|', '-', 'J', 'F']]

assert(findmove(ta, 2, 1, 3)==1)
assert(findmove(ta, 3, 1, 3)==0)

def move(arr, d, x, y):
    global orr, od

    (dx,dy)=od[d]
    x+=dx
    y+=dy
    d=findmove(arr,d,x,y)

    return (d,x,y)


p=[(x,y)]

while len(p)==1 or arr[y][x]!='S':
    (d,x,y) = move(arr,d,x,y)
    p.append((x,y))

#print(p)

#printpath(p, background=arr)
print("Part 1:",int(len(p)/2)    )
#print(p)
print("Part 1 time:", (time.perf_counter_ns()-ttt)/1000000,"ms")
ttt=time.perf_counter_ns()

from matplotlib import path

pp = path.Path(p)
#print(pp)

r = [(x,y) for x in range(len(arr[0])) for y in range(len(arr)) if pp.contains_points([(x,y)])[0]]
#print(r)

g = np.zeros_like(arr,dtype=np.int8)
#print(g)
for x,y in r:
    g[y][x]=1

#print(g)
h = np.ones_like(arr,dtype=np.int8)
#print(h)
for i in range(len(p)-1):
    drawline(h,p[i][0],p[i][1],p[i+1][0],p[i+1][1],0)

#print(h*g)
#printpath([],background=arr)
print("Part 2:",sum(sum(h*g)))
print("Part 2 time:", (time.perf_counter_ns()-ttt)/1000000,"ms")

