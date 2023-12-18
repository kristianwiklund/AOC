import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache, wraps
from cachetools import cached
from cachetools.keys import hashkey

arr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)

#print(arr)

arr=np.array(arr)

G = nx.Graph()

for y in range(len(arr)):
    for x in range(len(arr[0])):

        for i in range(4):
            dx = dirs[i][0]
            dy = dirs[i][1]

            if checkpos(arr, x+dx, y+dy, lambda x:x, outofbounds=False):
                G.add_edge((x,y,0),(x+dx,y+dy,1),weight=arr[y+dy][x+dx], d=i, length=1)

                if checkpos(arr, x+dx*2, y+dy*2, lambda x:x, outofbounds=False):
                    G.add_edge((x,y),(x+2*dx,y+2*dy,2),weight=arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx], d=i, length=2)

                    if checkpos(arr, x+dx*3, y+dy*3, lambda x:x, outofbounds=False):
                        G.add_edge((x,y),(x+3*dx,y+3*dy,3),weight=arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx]+arr[y+3*dy][x+3*dx], d=i, length=3)



print(list(nx.shortest_path(G,B,E)))
        
    
    
        
