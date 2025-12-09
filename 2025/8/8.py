import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache
import math

arr = readarray("input",split=",",convert=lambda x:int(x))

G=nx.Graph()




for x in range(len(arr)):
    G.add_node(x)

def edistance(x,y):
#    print(x,y)
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2)

sl = SortedList(key = lambda x:x[2])
for x in range(len(arr)-1):
    for y in range(x+1,len(arr)):
        sl.add((x,y,edistance(arr[x],arr[y])))

#print(list(sl))


        
#print(sl)

for i in range(1000):
    x,y,z=sl.pop(0)
    G.add_edge(x,y)

u=sorted(list(nx.connected_components(G)),key = lambda x:-len(x))
#print(u)
u = [len(x) for x in u][:3]
print(math.prod(u))



    
