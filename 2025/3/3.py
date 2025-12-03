import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:int(x))
#lines = readlines("input.short")
#print(arr)

def bop(vv, a,o,m):

    for t in vv:
        try:
            p = a[o+1:-m].index(t)
            return p
        except:
            continue


s=0
for i,v in enumerate(arr):
    #    print (i,v)
    vv = sorted(v, reverse=True)
    #    print(v,vv)

    q = bop(vv,arr[i],-1,1)
    
    for t in vv:
        try:
            p = arr[i][:-1].index(t)
#            print(p,arr[i][p])
            break
        except:
            continue

    assert(p==q)

    for t in vv:
        try:
            pp = arr[i][p+1:].index(t)+p+1
            break
        except:
            continue

    print(i, arr[i][p], arr[i][pp],p,pp)
    s+=arr[i][p]*10+arr[i][pp]

print("part 1:",s)
    
