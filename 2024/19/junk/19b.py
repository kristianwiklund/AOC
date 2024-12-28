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

pat = sorted(lines[0].replace(" ","").split(","), key=len)
#print(pat)
lines = lines[2:]
#print(lines)

bpo = "|".join(pat)
bpo=r"(?p)(?:"+bpo+")+"
#print(bpo)

import regex
print("a")
pa=regex.compile(bpo)
print("b")
n=0
c=0
for i in lines:
    s=regex.sub(bpo,"",i)
    if s=="":
        n+=1
        print(c,n,i)
    else:
        print(c,n)

    c+=1
    
print(n)
