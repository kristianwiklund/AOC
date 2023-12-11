import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import copy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
import scipy.ndimage

#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:1 if x=='#' else 0)
#lines = readlines("input.short")

a =np.array(arr)
print(a)
print("---")
labels,  numl = scipy.ndimage.label(a, structure=[[0,0,0],[0,1,0],[0,0,0]])

#p=[]
#for v in labels:
#    if sum(v)==0:
#        p.append(v)
#    p.append(v)

#p=np.array(p)
#a=np.transpose(p)

#p=[]
#for v in a:
#    if sum(v)==0:
#        p.append(v)
#    p.append(v)

p=arr
a = np.array(p)
#print(p)

pts = [(x,y) for x in range(len(a[0])) for y in range(len(a)) if a[y][x]]
#print(pts)

cols=[]
for c in set([x[0] for x in pts]):
    cols.append(c)

rows=[]
for r in set([x[1] for x in pts]):
    rows.append(r)

#print(cols, rows)
ocols=copy(cols)
orows=copy(rows)
for i in range(len(cols)-1,-1,-1):
    d = cols[i]-cols[i-1]
    if d>1:
        cols[i]+=1000000*d
        

for i in range(len(rows)-1,-1,-1):
    d = rows[i]-rows[i-1]
    if d>1:
        rows[i]+=1000000*d        

#print(cols, rows)

trows = {orows[i]:rows[i] for i in range(len(rows))}
tcols = {ocols[i]:cols[i] for i in range(len(cols))}

print(trows, tcols)


s=0
for j in range(len(pts)-1):
    for i in range(j,len(pts)):
        print(pts[j],pts[i])
        s+=abs(tcols[pts[j][0]]-tcols[pts[i][0]])+abs(trows[pts[j][1]]-trows[pts[i][1]])

print(s)
