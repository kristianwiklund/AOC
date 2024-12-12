import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
from scipy.ndimage import convolve
#from functools import cache
#from 
arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")


def getoftype(arr,t):
    return [[y==t for y in z] for z in arr]

# T =[[1,1,2],[2,0,0],[3,3,3]]
# print(getoftype(T,"O"))

# A = findinarray(arr, "O", all=True)
# print(A)

def perimeter(p, arr, w):
    s=0
    for i in p:
        t = checkallpos(arr, i[0], i[1], lambda x:x!=w, outofbounds=True)
        s+=sum(t)
    return s

# V = perimeter(A,arr,"O")
# print(V)



all = set([i for r in arr for i in r])
print(all)

# identify all regions

def findregions(arr):

    barr = deepcopy(arr)
#    print(barr)
    
    c=0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if not isinstance(barr[y][x], int):
                floodfill(barr, x, y, c, b=arr[y][x])
                c+=1
        

    return barr

R = findregions(arr)

allregions = set([i for r in R for i in r])
#print(allregions)

def cost(R, i):
    # list of all items in region i
    n = findinarray(R, i, all=True)
    
    a = len(n)
    p = perimeter(n, R, i)

    return (p*a)


c=0
for i in allregions:
    r = cost(R, i)
    c+=r

print("A:",c)

tv=[0,0,0]*(len(R[0])+2)
farr=[]
#farr.append(deepcopy(tv))
#farr.append(deepcopy(tv))
#farr.append(deepcopy(tv))

for y in range(len(R)):
    #knarr=[0,0,0]
    knarr=[]
    for x in range(len(R[y])):
        knarr.append(R[y][x])
        knarr.append(R[y][x])
        knarr.append(R[y][x])
 #   knarr.append(0)
 #   knarr.append(0)
 #   knarr.append(0)
    
    farr.append(deepcopy(knarr))
    farr.append(deepcopy(knarr))
    farr.append(deepcopy(knarr))

#farr.append(deepcopy(tv))
#farr.append(deepcopy(tv))
#farr.append(deepcopy(tv))

#pprint(farr)

def walk(arr, v, x,y,p,d,t):
    if (x,y) in p:
        return (t,p)
    arr[y][x]=0
    p.append((x,y))
    
    P=checkallpos(arr, x,y, lambda x:x==v, outofbounds=False)
#    print(P)

    for i in range(4):
        if P[i]:
            if (x+dirs[i][0],y+dirs[i][1]) not in p:
                if i!=d:
                    t.append(i)
    
                return walk(arr, v, x+dirs[i][0],y+dirs[i][1], p, i, t)
        
    return (t,p)

def pokemon(arr):

    s = []
    
    while True:

        n = findinarray(arr, 1)
        #        pprint(list(arr))
        #        print(n)
#        printpath([],background=list(arr))
        
        #print(arr,n)
        if not n:
            return s

        (x,y)=n
        
        (d,p) = walk(arr,1,x,y,[],None,[])
#        printpath(p,background=list(arr))
#        print (d,p)
        s+=d

    return s

#print(v)
#print(v)
#print(walk(v,1,0,0,[],None,[]))
#print(pokemon(v))

def allg(farr, g, R):
    p = np.array(farr)
    #print(p)
    # find the group
    tot = 0
    
    for i in g:
        q = (p==i).astype(int)
        # identify the core of the group
        v = [[sum(checkallpos(q,x,y,lambda x:x==1,outofbounds=False)) for x in range(len(q[y]))] for y in range(len(q))]
        # get the edges
        v = (np.array(v)!=4)
        v = v*q
        #print(v)

        y = pokemon(v)
        n = findinarray(R, i, all=True)        
        a = len(n)
        #       print(a*len(y))

        tot+=a*len(y)
        print(i,len(g),tot)
        
    return tot
print("B:",allg(farr,allregions, R))



    



