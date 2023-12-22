import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache, wraps
from cachetools import cached
from cachetools.keys import hashkey

barr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

B=(0,0)
E=(len(barr[0])-1,len(barr)-1)

us=[(x,y) for x in range(len(barr[0])) for y in range(len(barr))]
print(us)

D={i:np.inf for i in us}
print(us)

D[B]=0

while len(us):
    us=sorted(us, key=lambda x:D[x])
    n = us.pop(0)
    for d in dirs.values():
        if checkpos(barr, d[0]+n[0], d[1]+n[1], lambda x:True, outofbounds=False):
#            print ( d[0]+n[0], d[1]+n[1], checkpos(barr, d[0]+n[0], d[1]+n[1], lambda x:x, outofbounds=False))
#            print(D)
            if barr [d[1]+n[1]] [d[0]+n[0]] +D[n] < D[(d[0]+n[0],d[1]+n[1])]:
                D[(d[0]+n[0],d[1]+n[1])]=barr[d[1]+n[1]][d[0]+n[0]]+D[n]

print(np.array(D))
A=np.zeros_like(barr)
for y in range(len(barr)):
    for x in range(len(barr[0])):
        A[y][x]=D[(x,y)]
print(A)

p=(0,0)
us=[(x,y) for x in range(len(barr[0])) for y in range(len(barr))]

    

