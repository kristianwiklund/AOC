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

l = "".join(lines)
x = chunk(l)
s=eval(x)

print("A:",s)

def chunk2(l):

    a = l.split("don't()")
    #  print("a",a)

    ll=a[0]

    for x in a[1:]:
        b = x.split("do()",1)
        if len(b)>1:
            ll+=x.split("do()",1)[1]

    return(ll)

l = "".join(lines)

# remove dead code
y = chunk2(l)
# parses what remains
x = chunk(y)
s=eval(x)
print("B:",s)


    
