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

arr = readarray("input",split="",convert=lambda x:int(x))
#lines = readlines("input.short")
#print(arr)

def bop(vv, a,o,m):

    for t in vv:
        try:
            if m:
                p = a[o+1:-m].index(t)
            else:
                p = a[o+1:].index(t)
                
            return p+o+1
        except:
            continue


s=0
for i,v in enumerate(arr):
    #    print (i,v)
    vv = sorted(v, reverse=True)
    #    print(v,vv)

    q = bop(vv,arr[i],-1,1)
    
    for t in vv:
        try:
            p = arr[i][:-1].index(t)
#            print(p,arr[i][p])
            break
        except:
            continue

    assert(p==q)

    for t in vv:
        try:
            pp = arr[i][p+1:].index(t)+p+1
            break
        except:
            continue

#    print(i, arr[i][p], arr[i][pp],p,pp)
    s+=arr[i][p]*10+arr[i][pp]
    
    q = bop(vv,arr[i],p,0)
#    print (pp,q)
    assert(pp==q)
    
print("part 1:",s)
os=s

s=0
for i,v in enumerate(arr):
    vv = sorted(v, reverse=True)

    ss=0
    pp=-1
    for g in range(2):
        ss*=10
        p = bop(vv,arr[i],pp,1-g)
#        print(i,arr[i][p])
        ss+=arr[i][p]
        pp=p

    s+=ss
    
print("Alternate 1:",s)

assert(os==s)

s=0
for i,v in enumerate(arr):
    vv = sorted(v, reverse=True)

    ss=0
    pp=-1
    for g in range(12):
        ss*=10
        p = bop(vv,arr[i],pp,11-g)
#        print(i,arr[i][p])
        ss+=arr[i][p]
        pp=p

    s+=ss

print("Answer 2:",s)
