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
    P = 0
    for i in G.neighbors(n):
        
        if i == "end":
            P=P+1
            continue
        elif (not i in V):
            Z = visit(G,i,VV, twice)
        elif not twice and i!="start":
            Z = visit(G,i,VV, True)
        else:
            continue
        
        P=P+Z
    return (P)

def bolibompa(twice):
    
    c=0
    for i in G.neighbors("start"):
        T = visit(G, i, set(["start"]), twice)
        c+=T
    return c

print("Answer 1:",bolibompa(True))
print("Answer 2:",bolibompa(False))

