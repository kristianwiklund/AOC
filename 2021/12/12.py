#!/usr/bin/python3

import networkx as nx
import sys
#import matplotlib.pyplot as plt
from pprint import pprint

f = [t.strip().split("-") for t in sys.stdin]
G = nx.Graph()

for l in f:
    G.add_edge(l[0],l[1])

def fop(x):
    return x.isupper() or x=="end"

#nx.draw(G,with_labels=True)
#plt.savefig("nw.png")
        
def visit(G, n, V, twice):
    
    if n=="end":
        return []

    VV = V if n.isupper() else V|set([n])
    
    P = []

    for i in G.neighbors(n):
        if (not i in V):
            Z = visit(G,i,VV, twice)
        elif (not i=="start") and not twice:
            Z = visit(G,i,VV, True)
        else:
            Z = None
        if not Z:
            P.append([i])
        else:
            for x in Z:
                Y = [i] + x
                P.append(Y)
    return (P)

def bolibompa(twice):
    
    P=[]
    for i in G.neighbors("start"):
        T = visit(G, i, set(["start"]), twice)
        for x in T:
            Y = ["start",i] + x
            if "end" in Y:
                P.append(Y)
    
    return len(P)

print("Answer 1:",bolibompa(True))
print("Answer 2:",bolibompa(False))
