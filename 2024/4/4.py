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
import numpy as np
#import scipy
from scipy.ndimage import rotate
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")

# horizontal
a = " ".join(lines).count("XMAS")
b = " ".join(lines).count("SAMX")
#print(" ".join(lines))

def transpose(lines):
    return ["".join(list(x)) for x in list(zip(*lines))]

# transpose and search again

x = " ".join(transpose(lines))
#print("x:",x)
c = x.count("XMAS")
d = x.count("SAMX")


# rotate the array clock-wise
y = []
for t in range(len(lines)):
    y.append(" "*(len(lines)-t) + lines[t] + " "*t)

y = " ".join(transpose(y))
#print(y)

e = y.count("XMAS")
f = y.count("SAMX")

# rotate the array counter-clock-wise
y = []
for t in range(len(lines)):
    y.append(" "*t + lines[t] + " "*(len(lines)-t))

y = " ".join(transpose(y))
#print(y)

g = y.count("XMAS")
h = y.count("SAMX")



print("A:",a+b+c+d+e+f+g+h)
