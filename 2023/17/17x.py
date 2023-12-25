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

arr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)
print(E)
(barr,p) = dijkstra(arr, (0,0),f=lambda x:True)
a=np.array(arr)
b=np.array(barr)
c=a+b
print(c)

# backtrace through c
p = droute(arr,c,B,E,f=lambda x:True)
printpath(p,background=arr)
