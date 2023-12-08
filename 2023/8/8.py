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

def parse(s):
    s = s.split("=")
    print(s)
    s1 = s[0].strip()
    s2 = eval(s[1].replace("(","('").replace(", ","','").replace(")","')"))

    return (s1,s2)
    
with open("input") as fd:

    steps = list(readblock(fd)[0])
    print(steps)

    graph = readblock(fd, convert=parse)
    
    print(graph)

    g={}
    for k,v in graph:
        g[(k,'L')]=v[0]
        g[(k,'R')]=v[1]

    graph = g
    print (graph)
        

p = "AAA"
c = 0
while not p=="ZZZ":
    for d in steps:
        c+=1
        p = graph[(p,d)]
        if p=="ZZZ":
            break
        print(p)
        
print("Part 1:",c)
