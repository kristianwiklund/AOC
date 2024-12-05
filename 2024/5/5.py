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
from functools import cmp_to_key

with open("input","r") as fd:
    #arr = readarray("input.short",split="|",convert=lambda x:int(x))
    #lines = readlines("input.short")

    arr = readblock(fd, lambda x:x.split("|"))
    barr = readblock(fd, lambda x:x.split(","))

    #    print (arr)
    #    print (barr)

    def cmp(a,b):
        global arr

        if [a,b] in arr:
            return -1
        if [b,a] in arr:
            return 1
        return 0

    c=0
    d=0
    for x in barr:
        y = sorted(x, key=cmp_to_key(cmp))
        if x==y:
            c+=int(y[int(len(y)/2)])
        else:
            d+=int(y[int(len(y)/2)])
            
    print("A:", c)
    print("B:", d)
