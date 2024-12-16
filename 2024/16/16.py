import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache, lru_cache
import sys
sys.setrecursionlimit(3000)
from cachetools import cached,LRUCache
from cachetools.keys import hashkey

arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

B = findinarray(arr,"S")
E = findinarray(arr, "E")
arr[B[1]][B[0]]="."
arr[E[1]][E[0]]="."

barr = [[2**64]*len(x) for x in arr]
front = SortedSet(key=lambda x:barr[x[0][1]][x[0][0]])

def bfs(arr, B, E):
    global front

    while len(front):
        
        (x,y),d = front.pop();

        p = checkallpos(arr,x,y,lambda x:x==".",outofbounds=False)

        for i,v in enumerate(p):
            if v:
                nx=x+dirs[i][0]
                ny=y+dirs[i][1]
                cost = (1001 if i!=d else 1)+barr[y][x]
                if barr[ny][nx]>cost:
                    barr[ny][nx]=cost
                    front.add(((nx,ny),i))
                    
    print("barr:",barr[E[1]][E[0]])
    return barr


front.add((B,1))
barr[B[1]][B[0]]=0
barr = bfs(arr,B,E)

