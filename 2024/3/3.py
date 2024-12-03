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

def mul(x,y):
    if x<1000 and y<1000:
        return x*y
    else:
        return 0
        
def chunk(l):
    v = re.findall(r'mul\([0-9][0-9]*,[0-9][0-9]*\)',l)
    v = "+".join(v)
    return (v)

s=0
for l in lines:
    x = chunk(l)
    s+=eval(x)

print("A:",s)
