import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split=" ",convert=lambda x:x.replace(":",""))
#lines = readlines("input.short")

arr = {x[0]:x[1:] for x in arr}
print(arr)

G=nx.Graph()

for l in arr:
    for i in arr[l]:
        G.add_edge(l,i)

edge_labels = dict([((n1, n2), f'{n1}->{n2}')
                    for n1, n2 in G.edges])
#pos = nx.spring_layout(G)
#nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
        
#nx.draw(G, with_labels=True)
#plt.savefig("ap.png")

y = sorted(G.nodes(),key=lambda x:-len(G.edges(x)))
for p in y:
    print(p,len(G.edges(p)))

G.remove_edge("jll","lnf")
G.remove_edge("kkp","vtv")
G.remove_edge("qhd","cmj")

#nx.draw(G, with_labels=True)
#plt.savefig("bep.png")

wc = nx.connected_components(G)
for i in wc:
    print (len(i))
