import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")
#print(arr)

barr=deepcopy(arr)

c=0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x]=='@' and countallaround(arr,x,y,lambda x:x=='@')<4:
#            print(x,y)
            c+=1
            barr[y][x]='x'

print("part 1:", c)

