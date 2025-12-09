import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely import contains

arr = readarray("input",split=",",convert=lambda x:int(x))

sl = SortedList(key = lambda x:-x[-1])
for x in range(len(arr)-1):
    for y in range(x+1,len(arr)):
        sl.add((arr[x],arr[y],distance(arr[x],arr[y]),(1+abs(arr[x][0]-arr[y][0]))*(1+abs(arr[x][1]-arr[y][1]))))

print("part 1:",sl[0][-1])

pg = Polygon(arr)

import matplotlib.pyplot as plt
import matplotlib.patches as pat

#fig,ax = plt.subplots()

# generate all possible rectangles between two dots

d = []

for a in arr:
    for b in arr:
        if not a==b:
            
            t=(abs(np.array(a)-np.array(b))+np.array([1,1]))
            
            d.append([t[0]*t[1],a,b])

d = sorted(d,key=lambda x:-x[0])

m=0
# find the largest rectangle that fits in the polygon of all dots
for i in d:
    cost,x,y = i

    l = [x,[x[0],y[1]],y,[y[0],x[1]]]
    p = Polygon(l)
    if contains(pg,p):
        if cost>m:
            m=cost
            #ax.add_patch(pat.Polygon(l))
            break


print("part 2:",m)
#x,y = pg.exterior.xy
#ax.plot(x,y,color="green")
#plt.savefig("ap.png")

