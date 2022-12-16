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

print(nx.simple_cycles(G))
