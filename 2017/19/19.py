import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x, strip=False)
#lines = readlines("input.short")
#printpath([], background=arr)

x = arr[0].index("|")
y = 0
dr = 2


step=[(0,-1),(1,0),(0,1),(-1,0)]

def check(arr,x,y,z):
    global step
    try:
        t = arr[y+step[z][1]][x+step[z][0]]
    except:
        return False

    return t!=" " 
        
    

def move(arr, x,y,dr,acc):
    global step
    
    x+=step[dr][0]
    y+=step[dr][1]

    try:
        c = arr[y][x]
    except:
        return None

    if c in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        acc.append(c)

    if c==" ":
        return None
        
    if c=="+":
        z = dr-1
        if z<0:
            z=3
        if check(arr,x,y,z):
            dr=z
        else:
            z = dr+1
            if z>3:
                z=0
                
            if check(arr,x,y,z):
                dr=z
            else:
                return None

    return (x,y,dr,acc)

p = [(x,y)]
acc = []
while True:
    v = move(arr,x,y,dr,acc)
    try:
        (x,y,dr,acc) = v
        p.append((x,y))
    except:
        break

printpath(p,background=arr)
print("Part 1:","".join(acc))
print("Part 2:",len(p))
