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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

bz=[]

with open("input", "r") as fd:
    while True:
        bo=readblock(fd,convert=lambda x:[t for t in x])
        if not bo:
            break        
        bz.append(bo)

def unbo(z):
    z = transpose(z)
    z = ["".join(x) for x in z]
    return z
    
for i,x in enumerate(bz):
    bz[i]=unbo(x)
    
def cobo(x):

    p=[]
    for i in x:
        p.append(i.count("#")-1)

    return (0,p) if i[0]=="." else (p,0)

key=[]
lock=[]
for x in bz:
    (l,k)= cobo(x)
    key.append(tuple(k)) if k else lock.append(tuple(l))

def kko(l,k):

   return(len(l)==sum([(l[i]+v) <=5 for i,v in enumerate(k)]))

m=set()
print(".-.")

for k in key:
    for l in lock:
        if kko(l,k):
            m.add((l,k))
        else:
            print(l,k)

print("A:",len(m))
    





