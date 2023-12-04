import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache


@timer
def runme():
    arr = readarray("input.txt",split="|",convert=lambda x:x)
    #lines = readlines("input.short")

    sum=0
    yarr=[]
    for l in arr:
        win = set(ints(l[0].split(":")[1]))
        have = set(ints(l[1]))
        points = 0 if len(have&win)==0 else 2**(len(have&win)-1)
        sum+=points
        #    print(win,have,points)

    print("Part 1:",sum)

runme()
