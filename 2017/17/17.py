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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

lock = [0]
pos = 0
v = 2017
s=301

for i in range(1,v+1):
    if v<2017:
        print(lock)
    pos = (pos+s)%len(lock)+1
    lock.insert(pos,i)
    
    
print("A=",lock[lock.index(2017)+1])


lock = [0]
pos = 0
v = 50000000
s=301
oiiv=0

l=0
for i in range(1,v+1):
    pos = ((pos+s)%i)+1
    if pos==1:
        l=i
        
print("B=",l)

