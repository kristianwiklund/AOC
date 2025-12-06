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
lines = readlines("input")

n = [ints(x) for x in lines[:-1]]
n = transpose([[str(y) for y in x] for x in n])

o = lines[-1].replace(" ","")

s=0
for i,x in enumerate(o):
    k=x.join(n[i])
    s+=eval(k)

print("part 1:",s)
