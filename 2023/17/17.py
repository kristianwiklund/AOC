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
#import scipy
from functools import cache, wraps
from cachetools import cached
from cachetools.keys import hashkey

arr = readarray("input",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)

print(arr)

arr=np.array(arr)
#barr=np.zeros_like(arr)

mini=None

#@cache
#@logged

@cached(cache={}, key=lambda p,x,y,d,st,acc: hashkey(p,x,y,st,acc))
def walk(p, x, y, d, st, acc):
    global E
    global arr
    global mini

    if mini and acc>=mini:
        return None

#    print("walk", (x,y)==E, x,y,d,p)
    if (x,y)==E:
#        print (walk.cache_info())
        print (acc,p)
        if mini==None or acc<mini:
            mini=acc
                
        return acc
    
    if st>=3:
#        print("3:", p)
        return None

    if str((x,y)) in p:
#        print("dup: ",p)
        return None


    
    t = checkallpos(arr, x, y, lambda x:x, outofbounds=False)

    dd=d

    a=None
    b=None
    c=None
    if t[dd]:
        dx = dirs[dd][0]
        dy = dirs[dd][1]
        a = walk(p+str((x,y)), x+dx, y+dy, dd, st+1, acc+t[dd])
        
    dd = (d+1)if d<3 else 0
    if t[dd]:
        dx = dirs[dd][0]
        dy = dirs[dd][1]
        b = walk(p+str((x,y)), x+dx, y+dy, dd, 0, acc+t[dd])

        
    dd = (d-1) if d>0 else 3
    if t[dd]:
        dx = dirs[dd][0]
        dy = dirs[dd][1]
        c = walk(p+str((x,y)), x+dx, y+dy, dd, 0, acc+t[dd])

    mi = [i for i in [a,b,c] if i!=None]
    mi = min(mi) if len(mi) else None

        
    return mi

print(walk("", B[0], B[1], 3, 0, 0))



