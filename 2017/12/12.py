import networkx as nx
# usage
import sys
sys.path.append("../..")
from utilities import *

a = readarray("input.txt")
G = nx.Graph()

for i in a:
    f = i[0]    
    for t in i[2:]:
        G.add_edge(f,t.strip(","))

print("Part 1:",len(nx.node_connected_component(G,"0")))
sg = list(nx.connected_components(G))

print("Part 2:",len(sg))
