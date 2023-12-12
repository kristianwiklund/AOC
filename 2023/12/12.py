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

arr = [[x[0],ints(x[1])] for x in readarray("input.short",split=" ",convert=lambda x:x)]
print(arr)

# 0 is the string of broken springs, # is broken, . is not broken, ? is unknown
# 1 is the list of numbers of broken springs in the order they appear

def ref(l):
    s=[]
    
    for i in l:
        s.append(i*"#")

    s="\.\.*".join(s)

    return s

print ([ref(x[1]) for x in arr])

    
