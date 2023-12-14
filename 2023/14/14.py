import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

def tiltn(arr):
    global dirs

    a = arr
    b = deepcopy(a)
    d = 0
    
    print(b)
    (dx,dy) = dirs[d]

    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x]=='O':
                if checkpos(b, x+dx, y+dy, lambda x:x=='.', outofbounds=False):
                    b[y+dy][x+dx]='O'
                    b[y][x]='.'

    return b

while True:
    a = tiltn(arr,0)
    if a==arr:
        break
    arr = a

#pprint(a)

v = [len(a)-y if a[y][x]=='O' else 0 for y in range (len(a)) for x in range(len(a[9]))]
#print(v)
print("Part 1:",sum(v))

