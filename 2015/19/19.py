#!/usr/bin/python3

from inputshort import input
from inputshort import tokens
import re
import networkx as nx
from functools import cache

G = nx.DiGraph()


def subit(s):
    bop = list()
    t = tokens()

    all = set()

    for i in tokens():
        r = t[i]

        for rr in r:
            all|=set([s[:m.start()] + rr + s[m.end():] for m in re.finditer(i,s)])

    return all

all = subit(input())
            
print(all)
print("Answer to 1: ",len(all))

m = "e"

@cache
def doit(m, target, depth=0):
    global tokens
    
    all = subit(m)

    mm = []
    
    for i in all:
        print(i)
        if i==target:
            return depth+1
        else:
            mm.append[doit(i, target, depth+1)]

        
    return min(mm)

print(doit("e","HOHOHO",0))
        
    
    
