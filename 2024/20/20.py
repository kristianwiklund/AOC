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

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

hc={}
vc={}
start=findinarray(arr,"S")
stop =findinarray(arr,"E")
arr[start[1]][start[0]]="."
arr[stop[1]][stop[0]]="."
for y,l in enumerate(arr):
    for x,v in enumerate(l):

        if arr[y][x]=="#":
            m = checkallpos(arr,x,y,lambda x:x==".",outofbounds=False)
            if m[1] and m[3]:
                hc[(x,y)] = True
            if m[0] and m[2]:
                vc[(x,y)] = True
        if (x,y)==(6,7):
            print(checkallpos(arr,x,y,lambda x:x==".",outofbounds=False))
#print(hc)
#print(vc)


r = dijkstra(arr,start,stop=stop)
if r:
    (barr,p)=r
    printpath(p,background=arr)

print("full time",len(p))

tp = {p[x]:x for x in range(len(p))}
#print(tp)

c={}
ck=0
for x,y in hc:
    if (x-1,y) in tp and (x+1,y) in tp:
        sa = abs(tp[(x-1,y)]-tp[(x+1,y)])
 #       print("cheat",(x,y),"win",abs(tp[(x-1,y)]-tp[(x+1,y)]),"a",(x-1,y),tp[(x-1,y)],"b",(x+1,y),tp[(x+1,y)])
        if sa-2 >=100:
            ck+=1
            if sa-2 in c:
                c[sa-2].append((x,y))
            else:
                c[sa-2]=[(x,y)]
    else:
        print("no cheat",(x,y)) 


for x,y in vc:
#    print (x,y)
    if (x,y-1) in tp and (x,y+1) in tp:
        sa = abs(tp[(x,y-1)]-tp[(x,y+1)])
#        print("cheat",(x,y),"win",abs(tp[(x,y-1)]-tp[(x,y+1)]),"a",(x,y-1),tp[(x,y-1)],"b",(x,y+1),tp[(x,y+1)])
        if sa-2 >=100:
            ck+=1
            if sa-2 in c:
                c[sa-2].append((x,y))
            else:
                c[sa-2]=[(x,y)]
    else:
        print("no cheat",(x,y)) 

#pprint(c)
cn={x:len(c[x]) for x in c}
#print(hc)
#print(vc)
#print(checkallpos(arr,2,2,lambda x:x==".",outofbounds=False))
print(ck)
print(sum(cn.values()))
assert(ck!=5653)
