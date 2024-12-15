#!/usr/bin/python3

import sys
sys.path.append("../..")
from utilities import *

import re
import networkx as nx
from functools import cache

G = nx.DiGraph()

with open("input.short","r") as fd:
    tra = readblock(fd)
    tor = readblock(fd)

r=dict()
for l in tra:
    l = l.split(" => ")
    if l[0] in r:        
        r[l[0]].append(l[1])
    else:
        r[l[0]]=[l[1]]

tokens=r
input=tor[0]

from input import *

@cache
def subit(s):
    bop = list()
    
    all = set()
    t = tuckens
    
    for i in t:
        r = t[i]

        for rr in r:
            all|=set([s[:m.start()] + rr + s[m.end():] for m in re.finditer(i,s)])

    return all

tuckens = tokens
all = subit(input)
            
print(all)
print("Answer to 1: ",len(all))

# Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

bs={}
for m in tokens:
    for j in tokens[m]:
        if j in bs:
            bs[j].append(m)
        else:
            bs[j]=[m]

print(bs)
print(input)

#tuckens = bs

@cache
def desc(s,n,mn=1000000000000000000000000000000):
    global input
    
    if n>=mn:
        return mn+1

    if n>950:
        return 5001

    v = subit(s)
#    print(ss,v)
    for x in v:
        if x==input:
            print(input,ss)
            mn = n+1
        else:
            m = desc(x,n+1,mn)
            if m and m<mn:
                mn=m

    if mn:
        return mn
    else:
        return None

print(desc(input,0))

