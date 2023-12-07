import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split=" ",convert=lambda x:x)
#lines = readlines("input.short")

def rank(s):
    unique_values, counts = np.unique(s, return_counts=True)

    print (unique_values, counts)

v = [rank(list(x[0])) for x in arr]
print(v)
