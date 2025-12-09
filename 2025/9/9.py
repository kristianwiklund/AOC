import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split=",",convert=lambda x:int(x))
#lines = readlines("input.short")

#print(arr)
sl = SortedList(key = lambda x:-x[-1])
for x in range(len(arr)-1):
    for y in range(x+1,len(arr)):
        sl.add((arr[x],arr[y],distance(arr[x],arr[y]),(1+abs(arr[x][0]-arr[y][0]))*(1+abs(arr[x][1]-arr[y][1]))))

print(sl[0])

