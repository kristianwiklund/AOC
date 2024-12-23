import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

G=nx.Graph()
arr = readarray("input",split="-",convert=lambda x:x)
#lines = readlines("input.short")
for a,b in arr:
    G.add_edge(a,b)

from itertools import combinations,permutations

print(G)

u = list(G.nodes())
#for i in u:
#    if len(G.edges(i))<3:
#        G.remove_node(i)
#print(G)

ts = [x for x in G.nodes() if x.startswith("t")]
#ts = G.nodes()
#print(topp)
gopp = {x:list(G[x])+[x] for x in ts}
#print(gopp)
gopp={x:list(combinations(gopp[x],3)) for x in gopp}
#print(gopp)
gopp=flatten(gopp.values())
#print(gopp)
gopp=set([tuple(sorted(x)) for x in gopp])
#print(gopp)
#print("LG",len(gopp))

hopp=set()
for x,y,z in gopp:
    if x in G[y] and x in G[z] and y in G[z]:
        hopp.add((x,y,z))

print("HB-3-connected",len(hopp))
#pprint(hopp)

bopp=set()
for x,y,z in hopp:
    if x.startswith("t") or y.startswith("t") or z.startswith("t"):
        bopp.add(tuple(sorted(list((x,y,z)))))
 #       print(x,y,z)

#nx.draw(G, with_labels = True)
#plt.show()
        
c=len(bopp)
#print(bopp)
print("A:",c)

# bopp is the starter set of nodes connected to each other
# walk through the set, find more nodes, add nodes connected to all nodes


ts = [x for x in G.nodes()]
gopp = {x:list(G[x])+[x] for x in ts}
gopp={x:list(combinations(gopp[x],3))for x in gopp}
hopp=flatten(gopp.values())
print(hopp)

klopp=set()
for x,y,z in hopp:

    a = [x,y,z]

    f = True
    
    while f:
        p = set(flatten([list(G[t]) for t in a]))
        p = p - set(a)
        f = False
        
        for i in p:
            # check if i is connected to every node in a
            v = all([i in G[x] for x in a])
            
            if v:
                a.append(i)
                klopp.add(tuple(list(sorted(a))))
                f=True
                continue
        if f:
            continue

klack=max([len(x) for x in klopp])
klopp=set([x for x in klopp if len(x)==klack])

print(klopp)
print(klack)
    
