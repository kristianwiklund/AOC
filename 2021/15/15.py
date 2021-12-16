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

G = nx.DiGraph()

Mx=len(M[0])
My=len(M)

def w(M,x,y):
    lx=len(M[0])
    ly=len(M)
    nx=x%lx
    ny=y%ly
    wx=x // lx
    wy=y // ly
#    print(x,y,nx,ny,wx,wy,M[ny][nx]+wx+wy)
    return M[ny][nx]+wx+wy if M[ny][nx]+wx+wy <= 9 else M[ny][nx]+wx+wy-9
    
for y in range(len(M)*5):
    for x in range(len(M[0])*5):
        if x<len(M[0]*5)-1:
            G.add_edge(str(x)+","+str(y),str(x+1)+","+str(y),weight=w(M,x+1,y))
            G.add_edge(str(x+1)+","+str(y),str(x)+","+str(y),weight=w(M,x,y))
        if y<len(M)*5-1:
            G.add_edge(str(x)+","+str(y),str(x)+","+str(y+1),weight=w(M,x,y+1))
            G.add_edge(str(x)+","+str(y+1),str(x)+","+str(y),weight=w(M,x,y))
        
P=nx.single_source_dijkstra(G,"0,0",str(len(M)*5-1)+","+str(len(M[0])*5-1))
print("Answer 2:",P[0])

