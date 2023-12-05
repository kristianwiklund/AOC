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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

them = dict()
with open("input.short") as fd:
    while fd:
        v = readblock(fd)
        if not v:
            break
        what = v[0].split(":")[0].split(" ")[0]
        if v[0].split(":")[1] =="":
            them[what] = v[1:]
        else:
            them[what] = [(v[0].split(":")[1]).strip()]+v[1:]

            
print(them)
