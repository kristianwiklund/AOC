import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.short",split=" ")

G = nx.DiGraph()

for i in arr:
    rate=int(i[4].split("=")[1].strip(";"))
    G.add_node(i[1],rate=rate)
    for j in i[9:]:
        j=j.strip(",")
        G.add_edge(i[1],j,capacity=0,weight=1)
#        G.add_edge(i[1],i[1]+"O",capacity=rate,weight=1)
#        G.add_edge(i[1]+"O",j,capacity=0,weight=1)

start="AA"

def go(G, node, cost, benefit, visited):

    c = nx.descendants(G, node)
    print(c, visited)

    # move costs 1
    cost+=1
    if cost>30:
        return None

    p = 0
    for i in c:
        if not i in visited:
            r = go(G, i, cost, visited+[i])
        

go(G, start, 0, 0, [])

