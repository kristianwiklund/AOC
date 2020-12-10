#!/usr/bin/python3
import copy 
import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain

G = nx.DiGraph()

fd = open('input', 'r')
hl = sorted([int(x.strip("\n")) for x in fd.readlines()],key=int)

start=min(hl)
stop=max(hl)

#print(start)
#print(stop)

#G.add_edge(start)
#G.add_edge(stop)

while len(hl):
    p = hl.pop(0)
    
    hl2 = copy.deepcopy(hl)
    while hl2!=[] and (hl2[0]-p)<=3:
        G.add_edge(p,hl2[0])
#        print(str(p)+"-->"+str(hl2[0]))
        hl2.pop(0)

pos = nx.kamada_kawai_layout(G)
nx.draw_networkx(G, pos, node_size=30, font_size=5, with_labels=True)
plt.savefig("bags.png")

i=0
print ("bopp")
#print(len(nx.all_simple_paths(G, start, stop)))
for path in nx.all_simple_paths(G, start, stop):
#    print(str(i)+": "+str(path))
    i=i+1

print(i)

    
    
