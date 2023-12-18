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

mini=None

#@cache
#@logged

@cached(cache={}, key=lambda p,x,y,d,acc: hashkey(p, x,y,acc))
#@cache
def walk(p, x, y, d,acc):
    global E
    global arr
    global mini
    global barr

    
    if not checkpos(arr, x,y, lambda x:True, outofbounds=False):
        print("should not happen")
        return None
    
    if mini and acc>=mini:        
        return None

#    print("walk", (x,y)==E, x,y,p)
    if (x,y)==E:
        print("\033c\033[3J", end='')
        printpath(eval("["+p+"]")+[(x,y)],background=barr)
        print(acc)
        if mini==None or acc<mini:
            mini=acc
        return acc

    if str((x,y,d)) in p:
        return None


    # not optimal...
    t = checkallpos(arr, x, y, lambda x:x, outofbounds=False)

    dd=d

    def canmove(i,d):
        if i==d:
            return False
        if i==d+1 or i==d-1:
            return True

        if d+1==4 and i==0:
            return True

        if d-1==-1 and i==3:
            return True

        return False
    
    
    pp = [i for i in range(4) if (t[i] and canmove(i,d))]
    pp = sorted(pp,key=lambda i:-t[i])
    
    mi=[]
    for dd in pp:
        
        dx = dirs[dd][0]
        dy = dirs[dd][1]

        a = walk(p+str((x,y,d)),x+dx,y+dy,dd,acc+arr[y+dy][x+dx])
        mi.append(a)
        if checkpos(arr, x+2*dx,y+2*dy, lambda x:True, outofbounds=False):
            a = walk(p+str((x,y,d)),x+dx,y+dy,dd,acc+arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx])
            mi.append(a)
        if checkpos(arr, x+3*dx,y+3*dy, lambda x:True, outofbounds=False):
            a = walk(p+str((x,y,d)),x+dx,y+dy,dd,acc+arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx]+arr[y+3*dy][x+3*dx])
            mi.append(a)
        
    mi =[i for i in mi if i!=None]
    mi = min(mi) if len(mi) else None
    
    if mi:    
        return mi
    else:
        return None

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)

print(walk(str((-1,-1)), B[0], B[1], 1,0))



