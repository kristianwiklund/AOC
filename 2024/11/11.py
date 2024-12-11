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

arr = readarray("input",split=" ",convert=lambda x:int(x))[0]
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

pl=len(arr)
for i in range(25):
    arr=blink(arr)
    l=len(arr)
    print(i,l,arr[:10])
#    print(collections.Counter([len(str(x)) for x in arr]))#, i,l,l-pl,l/pl, l/(i+1))

print(len(arr))
