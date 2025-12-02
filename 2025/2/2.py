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
#from functools import cache

arr = readarray("input",split=",",convert=lambda x:x.split("-"))
#lines = readlines("input.short")
#print(arr)

def invalid(x):
    x=str(x)
    return x[:len(x)//2]==x[len(x)//2:]


#
#
#

assert(invalid("11"))
assert(not invalid("12"))
assert(invalid("1188511885"))
assert(invalid("1010"))
assert(invalid("38593859"))

s=0
for i in arr[0]:
    ap = range(int(i[0]),int(i[1])+1)
    ap = filter(invalid,ap)
    s+=sum(ap)

print(s)
