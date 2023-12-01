import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
from scipy import ndimage

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")
from knot import Rope,convert,megatwist 

s=0
m=list()
for i in range(128):
#    k="flqrgnkx-"+str(i)
    k="vbqugkhl-"+str(i)
    r=megatwist(k)
    v=("0000000000000000"+(bin(int(r,16))[2:]))[-128:]
    s+=sum([int(x) for x in v])
    m.append([int(x) for x in v] )


print("1:",s)
#print(m)

labels,  numl = ndimage.label(np.array(m,dtype=int))
print("2:",numl)
