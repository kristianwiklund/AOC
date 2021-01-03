#!/usr/bin/python3
import copy 
import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain
import functools

G = nx.DiGraph()

fd = open('input', 'r')
hl = sorted([int(x.strip("\n")) for x in fd.readlines()],key=int)
l = copy.deepcopy(hl)

start=min(hl)
stop=max(hl)

hl.append(stop+3)
hl.insert(0, 0)
hl = sorted(hl, key=int)

#print(start)
#print(stop)


while len(hl):

    p = hl.pop(0)
    c=0
    hl2 = copy.deepcopy(hl)
    while hl2!=[] and ((hl2[0]-p)<=3):
        G.add_edge(p,hl2[0])
        #print(str(p)+"-->"+str(hl2[0])+" = "+str((hl2[0]-p)))
        hl2.pop(0)

#pos = nx.kamada_kawai_layout(G)
#nx.draw_networkx(G, pos=pos, node_size=10, font_size=4, with_labels=True)
#plt.savefig("bags.pdf",format="pdf")

s = 1

def pathinator(Y,start,stop):

    c=0
    for path in nx.all_simple_paths(Y, source=start, target=stop):
        c=c+1
    return (c)

for Y in nx.biconnected_components(G.to_undirected()):
    start=min(list(Y))
    stop=max(list(Y))
    paths=pathinator(G.subgraph(Y),start,stop)
    s=s*paths

print(s)
