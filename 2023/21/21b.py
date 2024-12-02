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
arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")
arr = [["." if y=="S" else y for y in x]+x+["." if y=="S" else y for y in x] for x in arr]
arr = [["." if y=="S" else y for y in x] for x in arr]+ arr + [["." if y=="S" else y for y in x] for x in arr]

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




barr = np.full_like(arr,fill_value=np.inf,dtype=np.double)
barr[y][x]=0
print(barr)

p = [(x,y) for x in range(len(arr[0])) for y in range(len(arr))]


doit(arr,barr,p)
pp = (barr==0)
for i in range(2,50,2):
    pp += (barr==i)

nf = lambda x:0 if x==np.inf else x
noinf = np.vectorize(nf)

print("Ans:",sum(sum(pp)))

barr=noinf(barr)
#print(barr.max())

np.set_printoptions(linewidth=200)
print(barr)
