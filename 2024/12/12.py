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
#import numpy as np
#import scipy
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
    print(barr)
    
    c=0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if not isinstance(barr[y][x], int):
                floodfill(barr, x, y, c, b=arr[y][x])
                c+=1
        

    return barr

R = findregions(arr)

allregions = set([i for r in R for i in r])
print(allregions)

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

print(c)
    
            

