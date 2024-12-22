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
lines = [int(x) for x in readlines("input")]

def sauce(n):

    a=n
    b=((64*a)^a)%16777216
    c=((b//32)^b)%16777216
    d=((c*2048)^c)%16777216
    
    return d


assert(42^15==37)
assert(100000000%16777216==16113920)

tlist=[15887950,16495136,527345,704524,1553684,12683156,11100544,12249484,7753432,5908254]

sn=123

for i in range(10):
      sn=sauce(sn)
      assert(sn==tlist[i]) 
    

#--------------------

def bop(sn):
    for i in range(2000):
        sn=sauce(sn)

    return sn

assert(bop(1)==8685429)
assert(bop(10)==4700978)
assert(bop(100)==15273692)
assert(bop(2024)==8667524)

nums=[bop(x) for x in lines]
print(sum(nums))
