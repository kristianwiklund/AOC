import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache
from functools import cmp_to_key

arr = readarray("input",split=" ",convert=lambda x:x)
#lines = readlines("input.short")

def hand(c):

    c = sorted(c,reverse=True)

    if c[0]==5:
        return 7
    if c[0]==4:
        return 6
    if c[0]==3 and c[1]==2:
        return 5
    if c[0]==3:
        return 4
    if c[0]==2 and c[1]==2:
        return 3
    if c[0]==2:
        return 2

    return 1

T = {'A':14,'K':13,'Q':12,'J':11,'T':10}

def rank(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    unique_values1, counts1 = np.unique(s1, return_counts=True)
    unique_values2, counts2 = np.unique(s2, return_counts=True)

    h1 = hand(counts1)
    h2 = hand(counts2)

    if h1!=h2:
        return h1-h2

    s1 = np.array([int(x) if x.isdigit() else T[x] for x in s1])
    s2 = np.array([int(x) if x.isdigit() else T[x] for x in s2])
    t = s1-s2

    for x in t:
        if x==0:
            continue
        return x
    return 0
    

v = [x[0] for x in arr]
v = sorted(v,key=cmp_to_key(rank))

hands= {}


for x in arr:
    print(x)
    hands[x[0]]=int(x[1])

print(hands)

s=0
for i in range(len(v)):
    print(i+1,v[i],hands[v[i]])
    s+=(i+1)*hands[v[i]]

print("Part 1:",s)
