import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.short")

for line in lines:
    i = ints(line)
    if "value" in line:
        print(i)
        
