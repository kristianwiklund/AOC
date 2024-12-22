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

arr = readarray("input",split="",convert=lambda x:x)
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
barr = np.array(bfs(arr,B,E))
np.set_printoptions(linewidth=200, formatter={"all":lambda x:"{:4}".format(str("    " if x==(2**64) else x))})

end=barr[E[1]][E[0]]

# strykjärn

for y in range(len(barr)):
    for x in range(len(barr[y])):

        le = checkpos(barr,x-1,y,lambda x:x!="#")
        ri = checkpos(barr,x+1,y,lambda x:x!="#")
        up = checkpos(barr,x,y-1,lambda x:x!="#")
        do = checkpos(barr,x,y-1,lambda x:x!="#")
        v = barr[y][x]

        # remove easy dead ends
        if v>end:
            barr[y][x]=2**64
            continue
        
        try:
            if le and ri and v<2**32:
                if barr[y][x-1] < v and barr[y][x+1] < v:
                    barr[y][x] = (barr[y][x-1]+ barr[y][x+1])//2
        except TypeError:
            pass

        try:
            if up and do and v<2**32:
                if barr[y-1][x] < v and barr[y+1][x] < v:
                    barr[y][x] = (barr[y-1][x]+ barr[y+1][x])//2
        except TypeError:
            pass

print(barr)
p=droute(arr,barr,B,E)
printpath(p,background=arr)

front = SortedSet(key=lambda x:-barr[x[0]][x[1]])
front.add(E)
newc = barr[E[1]][E[0]]

def bfs2(barr, B, E):
    global front

    while len(front):
        
        (x,y) = front.pop();
        cost = barr[y][x]
        barr[y][x]=-1


        r = [B]
        
        v = checkallpos(barr,x,y,lambda x:x<cost and x!=-1 and x<2**32,outofbounds=False)
        i = sorted([i for i in range(4) if v[i]], key=lambda t:barr[y+dirs[t][1]][x+dirs[t][0]])
        i = [(x+dirs[t][0],y+dirs[t][1]) for t in i]
        i = [t for t in i if t not in r]
        print("i",i)
        for j,val in enumerate(i):
            if val:
                print("goff")
                nx,ny=val
            #    cost = 1
                if barr[ny][nx]<cost:
                    front.add((nx,ny))
                    r.append((x,y))
                    print("front:",front)
    return barr

barr=bfs2(barr,B,E)
print(barr)
v=(sum(sum(barr==-1))+1)
assert(v>492)

