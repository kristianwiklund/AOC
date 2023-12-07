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
from functools import cache
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

T = {'A':14,'K':13,'Q':12,'J':1,'T':10}

def jokerize(s,n=0):
    
    if len(s)==0:
        return [""]

    v = []
    p = jokerize(s[1:],n=n+1)
    
    if s[0]=="J":
        for j in ["J",2,3,4,5,6,7,8,9,"T","Q","K","A"]:
            for i in p:
                v.append(str(j)+i)
    else:
        for i in p:
            v.append(s[0]+i)

    return v
    

@cache
def chand(s1,s2,s3,s4,s5):

    s = [s1,s2,s3,s4,s5]
    s = sorted(s)

    v = jokerize(s)
    mh = 0
    for s in v:
        unique_values, counts = np.unique(list(s), return_counts=True)
        h= hand(counts)
#        print(s,counts,h)
        if h>mh:
            mh = h

    return mh
    

def rank(s1,s2):
    ss1 = sorted(list(s1))
    ss2 = sorted(list(s2))

    h1 = chand(ss1[0],ss1[1],ss1[2],ss1[3],ss1[4])
    h2 = chand(ss2[0],ss2[1],ss2[2],ss2[3],ss2[4])

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
#print(v)
hands= {}

#print("jokerizing")
#print("T55J5",chand("T","5","5","J","5"))

for x in arr:
    [s1,s2,s3,s4,s5] = sorted(list(x[0])) 
#    print(x[0], chand(s1,s2,s3,s4,s5))
    hands[x[0]]=int(x[1])

#print(hands)

s=0
for i in range(len(v)):
    s+=(i+1)*hands[v[i]]

assert(jokerize("12345")==["12345"])
assert(jokerize("J2345")==['J2345', '22345', '32345', '42345', '52345', '62345', '72345', '82345', '92345', 'T2345', 'Q2345', 'K2345', 'A2345'])

print("Part 2:",s)
