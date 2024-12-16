import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

B = findinarray(arr,"S")
E = findinarray(arr, "E")
arr[B[1]][B[0]]="."
arr[E[1]][E[0]]="."

print(B,E)

(barr,p) = dijkstra(arr, B, stop=E)
printpath(p,background=arr)
#print(barr)
# barr contains the unmodified cost matrix

# networkx collapses from this
# G=nx.Graph()

# for y,l in enumerate(arr):
#     for x,v in enumerate(l):
# #A        print (x,y)

#         p = checkallpos(arr,x,y,lambda x:x!="#", outofbounds=False)

#         for i,pv in enumerate(p):
#             if pv:
#                 G.add_edge((x,y),(x+dirs[i][0],y+dirs[i][1]))

# #print(G)

# P = nx.all_shortest_paths(G,B,E)
# print(len(list(P)))

