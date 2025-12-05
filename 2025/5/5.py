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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

with open("input","r") as fd:
    fresh = readblock(fd, convert=lambda x:list(map(int, x.split("-"))))

#    print(fresh)

    pantry = readblock(fd, convert=lambda x:int(x))

#    print(pantry)

    fr = [range(x[0],x[1]+1) for x in fresh]

#    print(fr)

    v=[]
    for x in pantry:
        p = [x,sum([x in y for y in fr])]
        v.append(p)


    print(len([x for x in v if x[1]>0]))
    
    
