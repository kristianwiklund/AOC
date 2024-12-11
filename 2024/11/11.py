import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache

arr = readarray("input.short",split=" ",convert=lambda x:int(x))[0]
#lines = readlines("input.short")

class CLIST:
    def __CLIST__(self):
        self.tl=[]

    
def blink(arr):
    barr=[]

    for i in arr:
        if i==0:
            barr.append(1)                
        elif len(str(i))%2==0:
            s=str(i)
            barr.append(int(s[:len(s)//2]))
            barr.append(int(s[-len(s)//2:]))
        else:
            barr.append(i*2024)

    return barr

import collections

barr=len(arr)
pl=len(arr)
for i in range(25):
    arr=blink(arr)
    l=len(arr)
    print(arr[:10],1,pl,l-pl,l/pl,l/(i+1))
    pl=l

print("A:",len(arr))

# 1     0
# 1  -> 1
# 1  -> 2024
# 4  -> 2,0,2,4
# 4  -> 4048,1,4048,8096
# 7  -> 40,48,2024,40,48,80,96
# 12 -> 4,0,20,24,4,0,4,8,8,0,9,6
# 14 -> 8096,1,2,0,2,4,8096,1,8096,16192,16192,1,18216,12144

