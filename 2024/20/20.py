import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

fn="input.short"

arr = readarray(fn,split="",convert=lambda x:x)
#lines = readlines("inputshort")

if len(arr)<50:
    tosave=20
    tosave2=50
else:
    tosave=100
    tosave2=100
    
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


try:
    import pickle
    with open(fn+".pickle","rb") as fd:
        p=pickle.load(fd)

except:
    import pickle
    r = dijkstra(arr,start,stop=stop)
    if r:
        (barr,p)=r
        printpath(p,background=arr)

    with open(fn+".pickle","wb") as fd:
        pickle.dump(p,fd)
    

        
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
        if sa-2 >= tosave:
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
print("PArt 1:", ck)
#print(sum(cn.values()))
assert(ck!=5653)

# to find all potential shortcuts we need to follow the path and find
# locations to end which are within 20 steps from the normal path
# the furthest this can be is 20 manhattan distances away

# "Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds (but can still only end when the program is on normal track)"

sneak={}
op = set()
xox=0
pox=0

#arr[0]="-"*len(arr[0])
#arr[len(arr)-1]="-"*len(arr[0])
#for i in range(1,len(arr)-1):
#    l=arr[i]
#    l[0]="-"
#    l[-1]="-"
#    arr[i]=l
    
for i,a in enumerate(p):
    for j,b in enumerate(p[i:]):

        if a==b:
            continue
        
        if distance(a,b)>21: 
            continue

        # find start points. check if they are in the done set

        v = checkallpos(arr,a[0],a[1],lambda x:x=="#",outofbounds=False)
        for i,v in enumerate(v):
            
            if not v:
                continue
            na = (a[0]+dirs[i][0],a[1]+dirs[i][1])
            if (na,b) in op:
                continue
            
            if distance(na,b)>21:
                continue

            op.add((na,b))
            
            pox+=1
            
            kossan=tp[stop]-(tp[a]+(tp[stop]-tp[b])+distance(a,b)-1)
        
            if kossan>=tosave2 and kossan<=ck:
                xox+=1
            
                if kossan in sneak:
                    sneak[kossan]+=1
                else:
                    sneak[kossan]=1
            
print(".......")

c=sum(sneak.values())
#pprint(sneak)
print("B",c,xox)
assert(c<1112786)
assert(c<998210)
#"print(len(p))
#pprint(sneak)
