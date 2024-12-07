import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")
#print(arr)

def findinarray(arr,what):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x]==what:
                return (x,y)
    return None        

def tick(arr, x, y, d):
    x+=dirs[d][0]
    y+=dirs[d][1]

    v=checkpos(arr, x, y, lambda x:x)
 #   print(x,y,d,v)
    
    # done
    if not v:
        return False

    # turn
    if v=="#":
        x-=dirs[d][0]
        y-=dirs[d][1]

        d+=1
        if d>3:
            d=0
            
    return ((x,y),d)

def bonkabonka(arr, start=None, cc=0,dd=0):

    if not start:
        v=findinarray(arr,"^")
        #    print (v)
        (x,y)=v
        d=0
    else:
        (x,y,d)=start

    p=[(x,y,d)]
    q=[(x,y,d)]

        
    while True:
        n = tick(arr,x,y,d)

        if not n:
            q.append((x,y,d))
            return (p,q)

        od=d
        (r,d) = n

        if od!=d and (r[0],r[1],d) not in q:
            q.append((r[0],r[1],d))
            
        if (r[0],r[1],d) in p:
            if r[0]!=x or r[1]!=y:
#                print(cc,"/",dd,"Cyclic")
                return True
            
        p.append((r[0],r[1],d))    
        x,y=r
#        print(p)

(p,q) = bonkabonka(arr)
        
printpath(p,background=arr)    
#print(len(p),len(set(p)))
#print(p)

te = len(set([(p[0],p[1]) for p in p]))
print("A:",te)

# this is the possibly most inefficient way to solve the problem, but it works
# takes roughly 2hrs on my NUC during which time I was playing portal.

c=0

#iterate over all locations, and test them one by one...

for yy in range(len(arr)):
    for xx in range(len(arr[yy])):

 #       print(yy,xx)
        
        if checkpos(arr, xx,yy, lambda x:x!="#"):
            s = arr[yy][xx]
            if s=="^" or s=="#":
                break
        
            arr[yy][xx]="#"
            v=bonkabonka(arr)
            #        print(v)
            if v==True:
                c+=1
            arr[yy][xx]=s

print("B:", c+1)
