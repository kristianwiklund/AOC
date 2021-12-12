#!/usr/bin/python3
import g as nx
import sys
f = [t.strip().split("-") for t in sys.stdin]
G = nx.Graph()

for l in f:
    G.add_edge(l[0],l[1])

def visit(G, n, V, twice):

    VV = V if n[0].isupper() else V|{n}
        
    P = 0
    for i in G.neighbors(n):
        
        if i == "end":
            P+=1
        elif (not i in V):
            P+= visit(G,i,VV, twice)
        elif not twice and i!="start":
            P+= visit(G,i,VV, True)

    return (P)

def bolibompa(twice):
    
    c=0
    Q={"start"}
    for i in G.neighbors("start"):
        T = visit(G, i, Q, twice)
        c+=T
    return c

print("Answer 1:",end='')
print(bolibompa(True))
print("Answer 2:",end='')
print(bolibompa(False))


