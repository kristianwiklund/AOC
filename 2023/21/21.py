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
#from functools import cache
np.set_printoptions(threshold=sys.maxsize)
arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")
barr = np.full_like(arr,fill_value=np.inf,dtype=np.double)
print(barr)

def doit(arr,barr, p):

    while len(p):

        p = sorted(p,key = lambda x:barr[x[1]][x[0]])
        print(len(p))
        
        (x,y)=p.pop(0)
#        print(x,y,arr[y][x])
        v = checkallpos(arr, x, y, lambda x:x==".",outofbounds=False)
        
        for i in range(len(v)):
            if v[i]:
#                p.append((x+dirs[i][0],y+dirs[i][1]))
#                print(p)
                if arr[y+dirs[i][1]][x+dirs[i][0]]==".":
#                    print("set",x+dirs[i][0],y+dirs[i][1],"to",arr[y][x]+1)
                    barr[y+dirs[i][1]][x+dirs[i][0]]=min(barr[y][x]+1, barr[y+dirs[i][1]][x+dirs[i][0]])
                    
y = [x for x in range(len(arr)) if "S" in arr[x]][0]
x = arr[y].index("S")

barr[y][x]=0
p = [(x,y) for x in range(len(arr[0])) for y in range(len(arr))]

doit(arr,barr,p)
pp = (barr==0)
for i in range(2,66,2):
    pp += (barr==i)

print(sum(sum(pp)))
print(max(max(barr)))
