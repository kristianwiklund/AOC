import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import copy
from pprint import pprint

arr = readarray("input.txt",split=" ")

G = nx.DiGraph()

for i in arr:
    rate=int(i[4].split("=")[1].strip(";"))
    if rate>0:
        G.add_node(i[1],rate=rate)

for i in arr:
#    G.add_node(i[1],rate=rate)
    for j in i[9:]:
        j=j.strip(",")
        G.add_edge(i[1],j,weight=1)



start="AA"
print(G)

# calculate the score for a series of opened valves vs the clock
def scoreme(a, clock):
    s=0
    for i in a:
        elapsed = clock-i[0]+1
        s+=elapsed*i[1]
    return (s)


assert(scoreme([(3,20),(6,13),(10,21),(18,22),(22,3),(25,2),],30)==1651)

cache = dict()

def go(G, node, clock, bleedtime, visited):

    clock+=1
    if clock > 30:
        print("timeout",bleedtime,visited)
        return (bleedtime, visited)

    sg = G.subgraph(i)
    if str(sg) in cache:
        return cache[str(sg)]
    
    children = set(nx.descendants(G, node))
    children-=set(visited)
    
    if children==[]:
        print("Hit the bottom, returning",bleedtime,visited)
        return (bleedtime, visited)
    
    highscore=0
    highpath=visited
    highbleed=bleedtime

    print ("== Minute",clock,"==")
    print ("Valves:",bleedtime)
    
    for child in children:

        if child in visited or child[0:2] in visited:
            continue

        d = G.get_edge_data(node, child)

        print ("Try valve",child[0:2],"which never is visited in",visited)
        result = go(G, child, clock, bleedtime, visited+[child[0:2]])
        
        score = scoreme(result[0], clock)
        
        if score>highscore:
            highscore=score
            highpath=result[1]
            highbleed=result[0]


    if "rate" in G.nodes[node]:
        for child in children:

            if child in visited or child[0:2] in visited:
                continue

            d = G.get_edge_data(node, child)
        
            
            print ("Turn on",node,"and try valve",child[0:2],"which never is visited in",visited)
            bt = copy(bleedtime)
            bt.append((clock+1,G.nodes[node]["rate"]))

            print("BT is now",bt)
            
            result = go(G, child, clock+1, bt, visited+[child[0:2]])
            
            score = scoreme(result[0], clock)
            
            if score>highscore:
                highscore=score
                highpath=result[1]
                highbleed=result[0]

    if highbleed != []:
        print("res",scoreme(highbleed,clock))

    cache[str(sg)]=(highbleed, highpath)
        
    return(highbleed, highpath, highscore)
        

print(go(G,"AA",0,[],["AA"]))
