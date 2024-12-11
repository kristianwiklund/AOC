import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache

arr = readarray("input",split=" ",convert=lambda x:int(x))[0]
#lines = readlines("input.short")

import collections
a = dict(collections.Counter(arr))
print(a)

for t in range(75):
    b = {}

    print(t,end=": ")
    pprint(str(a))
    
    for v in a:
        
        if v==0:
            c=a[v]
            if 1 in b:
                b[1]+=c
            else:
                b[1]=c
                
        elif len(str(v))%2 == 0:
            c = a[v]
            s= str(v)
            l = int(s[:len(s)//2])
            r = int(s[-len(s)//2:])
            if l in b:
                b[l]+=c
            else:
                b[l]=c
            if r in b:
                b[r]+=c
            else:
                b[r]=c
        else:
            c = a[v]
            if v*2024 in b:
                b[v*2+24]=c
            else:
                b[v*2024]=c
            
    a=b
    
print(sum(a.values()))
    
