import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

fn="input"

G = nx.DiGraph()

arr = readarray(fn,split="",convert=lambda x:x)
#lines = readlines("input.short")

th = findinarray(arr,"0",all=True)
ts = findinarray(arr,"9",all=True)

#printpath( [], background=arr)

if fn=="input.short":
    assert(th==[(3,0)])
    assert(ts==[(0,6),(6,6)])
elif fn=="input.short.2":
    print(th,ts)
    assert(th==[(1,0),(5,6)])

for i in th+ts:
    G.add_node(i)
    
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x]!=".":
            p = checkallpos(arr, x, y, lambda x:x.isnumeric(), outofbounds=False)
            for d in range(4):
                if p[d]:
                    if int(arr[y+dirs[d][1]][x+dirs[d][0]])-int(arr[y][x]) == 1:
                        G.add_edge((x,y),(x+dirs[d][0],y+dirs[d][1]))

c=0
for h in th:
    x = sum ([nx.has_path(G,h,s) for s in ts])
    #    print(h,"has score",x)
    c+=x

if fn=="input.short.3":
    assert(c==36)
    
print("A:",c)

#print(th,ts)

c=0
for h in th:
    p = [len(list(nx.all_simple_paths(G,h,s))) for s in ts]
    x=sum(p)
    #    print(h,"has score",x)
    c+=x

print("B:",c)
    
if fn=="input.short.4":
    assert(c==3)
elif fn=="input.short.5":
    assert(c==13)
elif fn=="input.short.6":
    assert(c==227)
    


