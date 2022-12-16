import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.short",split=" ")

G = nx.DiGraph()
valves = set()

for i in arr:
    rate=int(i[4].split("=")[1].strip(";"))
    if rate>0:
        G.add_node(i[1],rate=rate)
        print("Valve",i[1],"added with rate",rate)
        valves.add((i[1],rate))
        
for i in arr:
#    G.add_node(i[1],rate=rate)
    for j in i[9:]:
        j=j.strip(",")
        G.add_edge(i[1],j,weight=1)


start="AA"


# keep moving until either the time runs out
# or all valves are open

# this calculates the relative difference between node x and node y
def weighter(x,y):

    flowx=x[1]
    flowy=y[1]

    timex=x[2]
    timey=y[2]

    now = 30-y[3]
    
    # we sort based on opportunity cost

    if timex == timey:
        return cmp(flowx,flowy)

    rem = now
    remx = rem-timex
    remy = rem-timey
    
    print (x[0],"f",flowx,"t",(timex,remx),"r",remx*flowx,"--",y[0],"f",flowy,"t",(timey,remy),"r",remy*flowy)
    
    return cmp(remx*flowx,remy*flowy)

def cmp(a, b):
    return (a > b) - (a < b)

# ('HH', 22, 6, 0), ('CC', 2, 3, 0), ('EE', 3, 3, 0), ('JJ', 21, 3, 0), ('BB', 13, 2, 0), ('DD', 20, 2, 0)

def go(G, node, opened, valves, time):

    if time>=30 or len(valves)==0:
        print("Boom",opened)
        score=0
        for i in opened:
            score+=(30-i[2])*i[1]

        print("score",score)
        return
    
    SG = deepcopy(G)
    SG.remove_node(node)
    
    children = nx.descendants(G,node)
    if len(children)==0:
        print("The end",path)
        return

    # idea.
    # sort the remaining valves in order of benefit - magnitude vs "lost time"
    # (if it is too expensive to move, we have a problem)

    distance = [(x,y,len(nx.shortest_path(G,node, x))-1,time) for x,y in valves]

    from functools import cmp_to_key
    distance = sorted(distance, key=cmp_to_key(weighter),reverse=True)
    print("goodness",distance)
    print(valves)

    # the first one in the list is the best to pick

    path = list(nx.shortest_path(G,node,distance[0][0]))
    path.pop(0)
    for i in path:
        print("== Minute",time,"==")
        print ("You move to valve",i)
        time+=1
    print("== Minute",time,"==")
    print("You open the valve")
    opened.append((i,G.nodes[i]["rate"],time))
    valves = deepcopy(valves)
    valves.remove((distance[0][0],distance[0][1]))
    print("nv",valves)
    
    go(G,distance[0][0],opened,valves,time+1)

go(G,"AA",[],valves,1)

