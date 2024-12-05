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

    arr = readblock(fd, lambda x:[int(x) for x in x.split("|")])
    barr = readblock(fd, lambda x:[int(x) for x in x.split(",")])

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
            # avoid the division
            c+=sum([y[i] if y[i]==y[::-1][i] else 0 for i in range(len(y))])
        else:
            d+=sum([y[i] if y[i]==y[::-1][i] else 0 for i in range(len(y))])
            
    print("A:", c)
    print("B:", d)
