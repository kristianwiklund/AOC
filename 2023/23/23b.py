import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split="",convert=lambda x:x if x not in "><^v" else ".")
#lines = readlines("input.short")

#print(arr)

start=[x for x in range(len(arr[0])) if arr[0][x]=="."][0]
stop=list(reversed([x for x in range(len(arr[len(arr)-1])) if arr[len(arr)-1][x]=="."]))[0]
print(start,stop)

G=nx.Graph()

j=[(start,0),(stop,len(arr)-1)]
for y in range(len(arr)):
    for x in range(len(arr[0])):
        if arr[y][x]==".":
            z=checkallpos(arr,x,y,lambda x:x==".",outofbounds=False)        
            for i in range(4):
                if z[i]:
                    G.add_edge((x,y),(x+dirs[i][0],y+dirs[i][1]))
            if sum(z)>2:
                j.append((x,y))


def doit(j):
    f = j.pop(0)
    j=sorted(j,key=lambda x:len(nx.shortest_path(G,f,x)))

    return j

j=doit(j)
print(j)
