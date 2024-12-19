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
lines = readlines("input.short")
from multiprocessing import Pool

pat = lines[0].replace(" ","").split(",")
print(pat)
lines = lines[2:]
print(lines)

def match(pat, line):

    fr=[]
    for i in pat:
        if line.startswith(i):
            fr.append((i, line[len(i):]))

    return fr

tp = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']

#@cache
def make(pile):
    global pat
    o,c,l = pile

    v = match(pat,c)

    newp = [(o,y,l+[x]) for x,y in v if len(y)]
    nawp = [(o,y,l+[x]) for x,y in v if not len(y)]
    return (newp, nawp)

X=[]
for l in lines:
#    X.append(("brwrr","brwrr",[]))
    X.append((l,l,[]))

poss = set()
ppo = 0

vis = set()

pool = Pool()


while len(X):
#    p = X.pop()
    #print(len(X))
    
#    (x,y) = make(pat,p)

#    print("X:",X)
    res = pool.map(make, X)
    X=[]
#    print(res)
    
    for R in res:
#        print("R:",R)
        (x,y)=R
#        print(x)
#        print(y)
        for a,b,c in x:
            if not b+","+str(c) in vis and not a in poss:
                X.append((a,b,c))
                vis.add(b+","+str(c))
                
                if not len(vis)%10000:
                    print(len(vis), len(poss),"/",len(lines))
        if len(y):
            if len(poss)>ppo:
                print(len(poss),"/",len(lines))
                ppo=len(poss)
            for z in y:
                poss.add(z[0])

    
print(poss)
print(len(poss))
    
