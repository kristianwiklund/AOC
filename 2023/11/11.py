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
import scipy.ndimage

#import scipy
#from functools import cache

arr = readarray("input.short",split="",convert=lambda x:1 if x=='#' else 0)
#lines = readlines("input.short")

a =np.array(arr)
print(a)
print("---")
labels,  numl = scipy.ndimage.label(a, structure=[[0,0,0],[0,1,0],[0,0,0]])

p=[]
for v in labels:
    if sum(v)==0:
        p.append(v)
    p.append(v)

p=np.array(p)
a=np.transpose(p)

p=[]
for v in a:
    if sum(v)==0:
        p.append(v)
    p.append(v)

a = np.array(p)
print(p)

pts = [(x,y) for x in range(len(a[0])) for y in range(len(a)) if a[y][x]]
print(pts)

s=0
for j in range(len(pts)-1):
    for i in range(j,len(pts)):
        s+=abs(pts[j][0]-pts[i][0])+abs(pts[j][1]-pts[i][1])

print(s)
