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
#    G.add_node(i[1],rate=rate)
    for j in i[9:]:
        j=j.strip(",")
        G.add_edge(i[1],j,capacity=0,weight=1)
        G.add_edge(i[1],i[1]+"O",capacity=rate,weight=1)
        G.add_edge(i[1]+"O",j,capacity=0,weight=1)

start="AA"
print(G)

def scoreme(a, clock):
    s=0
    for i in a:
        elapsed = clock-i[0]
        s+=elapsed*i[1]
    return (s)

def go(G, node, clock, bleedtime, visited):

    clock+=1
    if clock > 30:
        print("timeout",bleedtime,visited)
        return (bleedtime, visited)

    children = nx.descendants(G, node)

    highscore=0
    highpath=visited
    highbleed=bleedtime
    
    for child in children:

        if child in visited:
            continue

        d = G.get_edge_data(node, child)
        if d and "capacity" in d:
            bleedtime.append((clock, d["capacity"]))
            #print(bleedtime)
            
        result = go(G, child, clock, bleedtime, visited+[child])
        score = scoreme(result[0], clock)

        if score>highscore:
            highscore=score
            highpath=result[1]
            highbleed=result[0]
            
    print("res",highpath, highscore)
    return(highbleed, highpath)
        

go(G,"AA",0,[],["AA"])
