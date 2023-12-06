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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

#r = [[7,9],
#     [15,40],
#     [30,200]]

r = [[50,242],
     [74,1017],
     [86,1681],
     [85,1252]]

factor = 1


def doit(r):
    sc=[]

    for x in r:
        a=0
        for t in range(x[0]+1):
            v = t*factor
            d = (x[0]-t)*v
            if d>x[1]:
                a+=1
        sc.append(a)

    print(sc,np.prod(sc))


doit(r)
#doit([[71530,940200]])
doit([[50748685,242101716911252]])
