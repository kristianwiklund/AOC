#!/usr/bin/python3
import networkx as nx
G=nx.DiGraph()
import bop
import copy

bop.b(G)

p = list(G.nodes())
from itertools import permutations
cp = [p[:1]+list(perm) for perm in permutations(p[1:])]

#print(cp)

def score(G, P):
    u = copy.copy(P)
    P.append(P[0])
    p = P.pop(0)
    w = 0
    while P:
        n = P.pop(0)
        w = w + G[n][p]["weight"]
        w = w + G[p][n]["weight"]
        #        print(n,p, G[n][p]["weight"], G[p][n]["weight"])
        p=n
    return (w,u)

gl=list()
for x in cp:
#    print(score(G, x))
    gl.append(score(G,x))
#print(gl)
gl=sorted(gl, key=lambda x: -x[0])
print(gl[0])






