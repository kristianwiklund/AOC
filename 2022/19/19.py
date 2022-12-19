import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.short",split=".",convert=lambda x:x)

bp=list()

for i in arr:
    print(i)
    # ['Blueprint 1: Each ore robot costs 4 ore', '  Each clay robot costs 2 ore', '  Each obsidian robot costs 3 ore and 14 clay', '  Each geode robot costs 2 ore and 7 obsidian', '']

    bp.append([int(i[0].strip().split(" ")[6]),
               int(i[1].strip().split(" ")[4]),
               (int(i[2].strip().split(" ")[4]), int(i[2].strip().split(" ")[7])),
               (int(i[3].strip().split(" ")[4]),int(i[3].strip().split(" ")[7]))])
    print(bp)

cache=dict()

def tick(bp, store, robots, time, mymax, seq):

    if time>24:
        #print(seq)
        return store["geode"]
    if str(time)+str(seq)+str(store)+str(robots) in cache:
        return cache[str(time)+str(seq)+str(store)+str(robots)]
    
    
    #print("=== Minute",time,"===")
    # diggy diggy hole
    for i in robots:
        store[i]+=robots[i]
#        if robots[i]:
#            print(robots[i],i+"-collecting robots collect",i+"; you now have",store[i],i+".")

    # then try various options

    mx=store["geode"] # what we have now
    
    bot=False
    v=dict()

    if store["ore"]>=bp["obsidian"][0] and store["clay"]>=bp["obsidian"][1]:
        ts=deepcopy(store)
        tr=deepcopy(robots)
        ts["ore"]-=bp["obsidian"][0]
        tr["obsidian"]+=1
        ts["clay"]-=bp["obsidian"][1]
        v["obsidian"] = tick(bp, ts, tr, time+1, mx, seq+["obsidian"])
        mx=max(mx,v["obsidian"])
        rx="obsidian"
        
    if store["ore"]>=bp["geode"][0] and store["obsidian"]>=bp["geode"][1]:
        ts=deepcopy(store)
        tr=deepcopy(robots)
        ts["ore"]-=bp["geode"][0]
        tr["geode"]+=1
        ts["obsidian"]-=bp["geode"][1]

        v["geode"] = tick(bp, ts, tr, time+1,mx, seq+["geode"])
        mx=max(mx,v["geode"])
        rx="geode"

    if store["ore"]>=bp["ore"]:
        ts=deepcopy(store)
        tr=deepcopy(robots)
        ts["ore"]-=bp["ore"]
        tr["ore"]+=1
        v["ore"] = tick(bp, ts, tr, time+1, mx, seq+["ore"])
        mx=max(mx,v["ore"])
        rx="ore"
        
    if store["ore"]>=bp["clay"]:
        ts=deepcopy(store)
        tr=deepcopy(robots)
        ts["ore"]-=bp["clay"]
        tr["clay"]+=1
        v["clay"] = tick(bp, ts, tr, time+1, mx, seq+["clay"])
        mx=max(mx,v["clay"])
        rx="clay"


    v["none"] = tick(bp,store,robots,time+1, mx, seq+["none"])
    mx=max(mx,v["none"])
    rx="none"
    # select the best path

    #if mx>mymax:
    #    print(" "*time+str(mx))
    cache[str(time)+str(seq+[rx])+str(store)+str(robots)]=mx
    return mx
        
    
def optimize(bp):

    needs={"ore":bp[0],
           "clay":bp[1],
           "obsidian":bp[2],
           "geode":bp[3]
           }
            
    store={"ore":0,"clay":0,"obsidian":0,"geode":0}
    robots={"ore":1,"clay":0,"obsidian":0,"geode":0}
    time=1
    
    # maximize the number of open geodes after 24 minutes
    #

    return tick(needs, deepcopy(store), deepcopy(robots), time,1,["none"])
    
print(optimize(bp[0]))
