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
import sys
sys.setrecursionlimit(10000)

arr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

#print(arr)

barr=arr
arr=np.array(arr)
#barr=np.zeros_like(arr)

mini=1086

#@cache
#@logged

@cached(cache={}, key=lambda p,x,y,d,st,acc: hashkey(p, x,y,st,acc))
#@cache
def walk(p, x, y, d, st,acc):
    global E
    global arr
    global mini
    global barr
    
    if mini and acc>=mini:
        return None

#    print("walk", (x,y)==E, x,y,d,p)
    if (x,y)==E:
        print("\033c\033[3J", end='')
        printpath(eval("["+p+"]")+[(x,y)],background=barr)
        print(acc)
        if mini==None or acc<mini:
            mini=acc
        return arr[y][x]
    #        print (walk.cache_info())

    #        print (acc)

        
    
    if st>=3:
#        print("3:", p)
        return None

    if str((x,y)) in p:
#        print("dup: ",p)
        return None


    
    t = checkallpos(arr, x, y, lambda x:x, outofbounds=False)

    dd=d

    def canmove(i,d):
        if i==d:
            return True
        if i==d+1 or i==d-1:
            return True

        if d+1==4 and i==0:
            return True

        if d-1==-1 and i==3:
            return True

        return False
    
    
    pp = [i for i in range(4) if (t[i] and canmove(i,d))]
    pp = sorted(pp,key=lambda i:-t[i])
#    print(pp,t)
#    import sys
#    sys.exit()
    
    mi = []

    for dd in pp:
        
        dx = dirs[dd][0]
        dy = dirs[dd][1]
        if dd==d:            
            a = walk(p+","+str((x,y)), x+dx, y+dy, dd, st+1, acc+arr[y][x])
        else:
            # try a turn
            a = walk(p+","+str((x,y)), x+dx, y+dy, dd, 0, acc+arr[y][x])
                    
        if a:
            mi.append(a)
            
            #    mi = [i for i in [a,b,c] if i!=None]
    mi = min(mi) if len(mi) else None
    
    if mi:    
        return mi+arr[y][x]
    else:
        return None

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)

print(walk(str((-1,-1)), B[0], B[1], 1, 0,0))



