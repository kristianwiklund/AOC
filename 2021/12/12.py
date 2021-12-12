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

    for i in G.neighbors(n):

        if i == "end":
            P.append(["end"])
            continue
        elif (not i in V):
            Z = visit(G,i,VV, twice)
        elif not twice and i!="start":
            Z = visit(G,i,VV, True)
        else:
            continue
        
        for x in Z:
            #x.append(i)
            #P.append(x)
            P.append("end")
    return (P)

def bolibompa(twice):
    
    P=[]
    c=0
    for i in G.neighbors("start"):
        T = visit(G, i, set(["start"]), twice)
        for x in T:
            c+=1
    return c

print("Answer 1:",bolibompa(True))
print("Answer 2:",bolibompa(False))

