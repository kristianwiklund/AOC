import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import copy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
import scipy.ndimage
z

#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:1 if x=='#' else 0)
#lines = readlines("input.short")

a = arr

pts = [(x,y) for x in range(len(a[0])) for y in range(len(a)) if a[y][x]]

cols = list(SortedSet([x[0] for x in pts]))
rows = list(SortedSet([x[1] for x in pts]))

#print(cols,rows)
ocols=[0]+[cols[x+1]-cols[x]-1 for x in range(len(cols)-1)]
orows=[0]+[rows[x+1]-rows[x]-1 for x in range(len(rows)-1)]

tc = {cols[i]:ocols[i] for i in range(len(cols)) if ocols[i]}
tr = {rows[i]:orows[i] for i in range(len(cols)) if orows[i]}

def boffe(tx, p, mf):
    
    v = sum([tx[x]*mf for x in tx if x<=p])
    return v

#print(tc,tr)
#print(boffe(tc,6,1))

s=0
mf=1000000-1
for j in range(len(pts)-1):
    for i in range(j,len(pts)):
        (x1, y1) = pts[j]
        (x2, y2) = pts[i]

        x1+=boffe(tc,x1,mf)
        x2+=boffe(tc,x2,mf)

        y1+=boffe(tr,y1,mf)
        y2+=boffe(tr,y2,mf)

        s+=abs(x1-x2)+abs(y1-y2)
        
        

print("Part 2:",s)
