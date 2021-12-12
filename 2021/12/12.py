#!/usr/bin/python3

#import networkx as nx
import g as nx
import sys
from pprint import pprint
#import vmprof

#fd = open("apa.prof","w+b")
#vmprof.enable(fd.fileno())

f = [t.strip().split("-") for t in sys.stdin]
G = nx.Graph()

for l in f:
    G.add_edge(l[0],l[1])
        
def visit(G, n, V, twice):
    
    VV = V if n[0].isupper() else V|set([n])
    
    P = []

    if n=="end":
        return [["end"]]
    
    for i in G.neighbors(n):

        if (not i in V):
            Z = visit(G,i,VV, twice)
        elif (i!="start") and not twice:
            Z = visit(G,i,VV, True)
        else:
            continue
        
        for x in Z:
            P.append([i]+x)
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

