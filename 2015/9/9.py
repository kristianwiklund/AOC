import networkx as nx
import matplotlib.pyplot as plt
import sys
from pprint import pprint

G = nx.Graph()

def popaway(GG, what):


    if not GG.has_node(what):
        return GG
    
    import copy
    GG = copy.deepcopy(GG)
    GGG = nx.Graph(GG)

    GGG.remove_node(what)

    return GGG

with open("input.txt") as fd:

    for line in fd:
        line=line.rstrip()
        [a,_,b,_,dist] = line.split(" ")
        G.add_edge(a,b,weight=int(dist))

    nx.draw(G, with_labels=True)
    plt.savefig("maze.png")
        
# --

cache = {}

def shortest(G, current):
    global cache

    unused = "".join(list(G.nodes()))
    
    if current+unused in cache:
        return cache[current+unused] 

    N = list(G.neighbors(current))
    if N == []:
        return (0, [current])

    best = 7743949349347934
    bestpath = None
                
    GG = popaway(G, current)

    for n in N:
        (dist, path) = shortest(GG, n)

        if dist + G[current][n]["weight"] < best:
            best = dist + G[current][n]["weight"]
            bestpath = path
                
    cache[current+unused] = (best, [current] + bestpath)
    return (best, [current] + bestpath)

d=list()
for i in G.nodes():

    (ii,path) = shortest(G, i)
    print(i+": "+str(ii)+" -> "+str(path))
    d.append(ii)

print("Shortest: "+str(min(d)))
print("---------------")


def longest(G, current):
    global cache

    unused = "".join(list(G.nodes()))
    
    if current+unused in cache:
        return cache[current+unused] 

    N = list(G.neighbors(current))
    if N == []:
        return (0, [current])

    best = -7743949349347934
    bestpath = None
                
    GG = popaway(G, current)

    for n in N:
        (dist, path) = longest(GG, n)

        if dist + G[current][n]["weight"] > best:
            best = dist + G[current][n]["weight"]
            bestpath = path
                
    cache[current+unused] = (best, [current] + bestpath)
    return (best, [current] + bestpath)

d=list()
cache = {}
for i in G.nodes():

    (ii,path) = longest(G, i)
    print(i+": "+str(ii)+" -> "+str(path))
    d.append(ii)

print("Longest: "+str(max(d)))
