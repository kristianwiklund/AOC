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

arr = readarray("input",split=" ",convert=lambda x:x)
#lines = readlines("input.short")

x=0
y=0
dd="URDL"

c=[1,2,3,0]
arr = [(c[int(x[2][-2])],int(x[2][2:-2],16)) for x in arr]
#print(arr)

p=[]

tl=0
for i in arr:
   x+=dirs[i[0]][0]*i[1]
   y+=dirs[i[0]][1]*i[1]
   p.append((x,y))
   tl+=i[1]
   
o=poff(p)
p=[(i[0]+o[0],i[1]+o[1]) for i in p]
#print(p)

mx=max([i[0] for i in p])+1
my=max([i[1] for i in p])+1

mxx = mx*my

import shapely.geometry
#print(pp)
pp=[(i[0],i[1]) for i in p]
sp = shapely.geometry.Polygon(pp)
area = sp.area
print(area,tl,area+tl/2+1)
