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
from functools import cache
import sys
sys.setrecursionlimit(3000)
from cachetools import cached
from cachetools.keys import hashkey

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

B = findinarray(arr,"S")
E = findinarray(arr, "E")
arr[B[1]][B[0]]="."
arr[E[1]][E[0]]="."

print(B,E)

mc=False

@cache
def dfs(curre-
        nt, E, visited, cost, d):
    global arr
    global mc

    #132515 is too high
    if cost>50000: #132515
        return (False, visited)
    
#    print (current, visited)
    if current==E:
        #        print("The End",cost,visited+str(current))
        if not mc or cost < mc:
            print(cost)
            mc = cost
            
        return (cost, visited+","+str(current))
   
    # don't eat your own tail
    if str(current) in visited:
        return (False, visited)

     
    x,y=current
    visited+=","+str(current)

    p = checkallpos(arr, x, y, lambda x:x==".", outofbounds=False)

    bc=False
    bp=""


    for i,v in enumerate(p):
        if v:
            if i==d:
                #                print ("pos:", current,"testing: ", end="")
                #                print((x+dirs[i][0], y+dirs[i][1]),visited," ",end="")
                if not mc or cost+1<mc:
                    nc,np = dfs((x+dirs[i][0], y+dirs[i][1]), E, visited, cost+1, d)
                else:
                    continue
                #                print("(nc,np)=:",nc,np)
            else:
                #                print ("pos (turn):", current,"testing: ", end="")
                #                print((x+dirs[i][0], y+dirs[i][1]),"vis:", visited," ", end="")
                if not mc or cost+1001 < mc:
                    nc,np = dfs((x+dirs[i][0], y+dirs[i][1]), E, visited, cost+1001, i)
                else:
                    continue
                #                print(nc,np)
            if nc and (not bc or (nc<bc)):
                bc=nc
                bp=np

    return (bc,bp)

bc, bp = dfs(B, E, "", 0, -1)
bp=bp[1:]
bp = eval(bp)
print(bp)
printpath(bp,background=arr)
print(bc)
