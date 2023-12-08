import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from copy import copy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

import re

def parse(s):
    s = s.split("=")
  #  print(s)
    s1 = s[0].strip()
    s2 = eval(s[1].replace("(","('").replace(", ","','").replace(")","')"))

    return (s1,s2)
    
with open("input") as fd:

    steps = list(readblock(fd)[0])
 #   print(steps)

    graph = readblock(fd, convert=parse)
    
#    print(graph)

    g={}
    for k,v in graph:
        g[(k,'L')]=v[0]
        g[(k,'R')]=v[1]

    graph = g
#    print (graph)
        

p = "AAA"
c = 0

def step(graph, pos, steps, c):
    c+=1
    d = steps[0]
    steps = steps[1:]+[d]
    pos = graph[(pos,d)]
        
    return (pos, steps, c)
    
p = [x[0] for x in graph.keys() if x[0][2]=='A']
cnt=[0 for x in p]
stp=[copy(steps) for x in p]

t=[]

while len(t)!=len(stp):
    print(p)
    for i in range(len(p)):

        (p[i], stp[i], cnt[i]) = step(graph, p[i], stp[i], cnt[i])

        t = [p[i] for x in p if x[2]=='Z']

print(cnt)
    
