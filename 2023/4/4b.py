import sys

sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache


@timer
def runme():
    arr = readarray("input.txt",split="|",convert=lambda x:x)
    #lines = readlines("input.short")

    yarr=SortedDict()

    for i in range(len(arr)):
        yarr[i] = 1

    for i in range(len(yarr)):
        n = yarr[i]
        l = arr[i]
        win = set(ints(l[0].split(":")[1]))
        have = set(ints(l[1]))
        ntick = len(have&win)

        for v in range(ntick):
            yarr[i+v+1]+=n

    print("Part B:",sum(list(yarr.values())))
    
runme()
    


