#!/usr/bin/python3

import sys
import networkx as nx

G = nx.DiGraph()

M=[]
for l in sys.stdin:
    w=[]
    for x in l.strip():
        w.append(int(x))
    M.append(w)

#print(M)

for y in range(len(M)):
    for x in range(len(M[y])):
        if x<len(M[y])-1:
            G.add_edge(str(x)+","+str(y),str(x+1)+","+str(y),weight=M[y][x+1])
            G.add_edge(str(x+1)+","+str(y),str(x)+","+str(y),weight=M[y][x])
        if y<len(M)-1:
            G.add_edge(str(x)+","+str(y),str(x)+","+str(y+1),weight=M[y+1][x])
            G.add_edge(str(x)+","+str(y+1),str(x)+","+str(y),weight=M[y][x])

#print(G.nodes())

P=nx.single_source_dijkstra(G,"0,0",str(len(M)-1)+","+str(len(M[0])-1))

print("Answer 1:",P[0])


