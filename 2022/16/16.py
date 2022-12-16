import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

# 1645 too low

arr = readarray("input.txt",split=" ")

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
cache = dict()

# keep moving until either the time runs out
# or all valves are open

# this calculates the relative difference between node x and node y
def weighter(x,y):

    flowx=x[1]
    flowy=y[1]

    timex=x[2]
    timey=y[2]

    now = y[3]
    
    # we sort based on opportunity cost

    if timex == timey:
        return cmp(flowx,flowy)

    rem = 30-now
    remx = rem-timex
    remy = rem-timey
    
    #print (x[0],"f",flowx,"t",(timex,remx),"r",remx*flowx,"--",y[0],"f",flowy,"t",(timey,remy),"r",remy*flowy)
    
    return cmp(remx*flowx,remy*flowy)

def cmp(a, b):
    return (a > b) - (a < b)

# ('HH', 22, 6, 0), ('CC', 2, 3, 0), ('EE', 3, 3, 0), ('JJ', 21, 3, 0), ('BB', 13, 2, 0), ('DD', 20, 2, 0)


hits=0
misses=0

def go(G, node, opened, valves, time):
    global hits
    global misses
    
    if node+str(opened) in cache:
        hits+=1
        if hits%100 == 0:
            print(hits,misses)
        return cache[node+str(opened)]

    misses+=1
    if misses%100 == 0:
        print(hits,misses)
    
    if time>=30 or len(valves)==0:
        #print("Boom",opened,valves,end=" ")
        score=0
        for i in opened:
            score+=(30-i[2])*i[1]

        #print("score",score)
        return score
    
#    SG = deepcopy(G)
#    SG.remove_node(node)
    
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
    #    print("goodness",distance)
    #    print(valves)

    # test the things in order
    otime=time
    smax=0
    bmax=None
    
    for v in range(len(distance)):
        time=otime
        path = list(nx.shortest_path(G,node,distance[v][0]))
        path.pop(0)
        #        for i in path:
        #            time+=1
        time+=len(path)
        
        nvalves = deepcopy(valves)
        nvalves.remove((distance[v][0],distance[v][1]))

        score=go(G,distance[v][0],opened+[(distance[v][0],G.nodes[distance[v][0]]["rate"],time)],nvalves,time+1)
        if score>smax:
            smax=score
            #print("win",score)
            bmax=v

    if bmax!=None:
        cache[node+str(opened)]=smax

        return smax
    
    print("didnae find anything for node",node,distance)
    return -1
    
score=go(G,"AA",[],valves,1)
#key = next(key for key, value in cache.items() if value == score)
#key = eval(key[2:-5])
print(score)

