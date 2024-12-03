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

arr = readarray("input",split="  ",convert=lambda x:int(x))
#lines = readlines("input.short")

x,y=unzip(arr)
x=sorted(x)
y=sorted(y)
print (sum([abs(x-y) for (x,y) in list((zip(x,y)))]))
