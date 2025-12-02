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
import re

def invalid(x):
    x=str(x)

    for i in range(1,len(x)):
        s = x[:i]

        if len(x)%len(s):
            continue

        ex = "^("+s+")("+s+")+$"
        m = re.search(ex,x)
        if m:
#            print(m)
#            print(x,s,ex)
            return True
#        print(x,s,ex)        

    return False


#
#
#

assert(invalid("11"))
assert(not invalid("12"))
assert(invalid("999"))
assert(invalid("1010"))
assert(invalid("38593859"))
assert(invalid("565656"))
assert(invalid("2121212121"))

s=0
for i in arr[0]:
    ap = range(int(i[0]),int(i[1])+1)
    ap = filter(invalid,ap)
    s+=sum(ap)

print(s)
