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

print(B,E)



COSTLIMIT=124549 #132516 #124548 124548

mc=COSTLIMIT

@cached(cache=LRUCache(maxsize=3000000), key = lambda current, E, visited, cost, d:hashkey(current,cost,visited,d))
#@cache
def dfs(current, E, visited, cost, d):
    global arr
    global mc
    global COSTLIMIT
    
    #132515 is too high
    if cost>COSTLIMIT: #132515
#        print(len(visited))
        
        return False
    
#    print (current, visited)
    if current==E:
        #        print("The End",cost,visited+str(current))
        if not mc or cost < mc:
            print(cost)
            mc = cost
            
        return (cost, visited+","+str(current))
   
    # don't eat your own tail
    if str(current) in visited:
        return False

     
    x,y=current
    visited+=","+str(current)

    p = checkallpos(arr, x, y, lambda x:x==".", outofbounds=False)

    bc=False
    bp=""


    # walk straight ahead first, cheapest
    # if p[d]:
    #     if not mc or cost+1<mc:
    #         zy = dfs((x+dirs[d][0], y+dirs[d][1]), E, visited, cost+1, d)
    #         if zy:
    #             bc,bp=zy
            
    for i,v in enumerate(p):
        if v:
            if not i == d:
                if not mc or cost+1001 < mc:
                    zy = dfs((x+dirs[i][0], y+dirs[i][1]), E, visited, cost+1001, i)
                    if zy:
                        nc,np=zy
                    else:
                        continue
                else:
                    continue
            else:
                if not mc or cost+1 < mc:
                    zy = dfs((x+dirs[i][0], y+dirs[i][1]), E, visited, cost+1, i)
                    if zy:
                        nc,np=zy
                    else:
                        continue
                else:
                    continue                
                
                #                print(nc,np)
            if nc and (not bc or (nc<bc)):
                bc=nc
                bp=np

    return (bc,bp)

bc, bp = dfs(B, E, "", 0, 1)
bp=bp[1:]
bp = eval(bp)
print(bp)
printpath(bp,background=arr)
print(bc)
