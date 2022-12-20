import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
from functools import cache,lru_cache
arr = readarray("input.short",split=".",convert=lambda x:x)

bp=list()

for i in arr:
    print(i)
    # ['Blueprint 1: Each ore robot costs 4 ore', '  Each clay robot costs 2 ore', '  Each obsidian robot costs 3 ore and 14 clay', '  Each geode robot costs 2 ore and 7 obsidian', '']

    bp.append((int(i[0].strip().split(" ")[6]),
               int(i[1].strip().split(" ")[4]),
               (int(i[2].strip().split(" ")[4]), int(i[2].strip().split(" ")[7])),
               (int(i[3].strip().split(" ")[4]),int(i[3].strip().split(" ")[7]))))
    print(bp)


cnt=0

@cache
def tick(bp, store, robots, time):
    global cnt

    cnt+=1
    if not cnt % 1000:
        print(cnt)
    
    if time>=23:
        #print(seq)
        return store[3]

    store = list(store)
    
    #print("=== Minute",time,"===")
    # diggy diggy hole
    for i in range(len(robots)):
        store[i]+=robots[i]
        #        if robots[i]:
        #            print(robots[i],i+"-collecting robots collect",i+"; you now have",store[i],i+".")
    store=tuple(store)
    # then try various options

    mx=store[3] # what we have now
    
    bot=False
    v=dict()

        
    if store[0]>=bp[3][0] and store[2]>=bp[3][1]:
        ts=list(store)
        tr=list(robots)
        ts[0]-=bp[3][0]
        tr[3]+=1
        ts[2]-=bp[3][1]

        v["geode"] = tick(bp, tuple(ts), tuple(tr), time+1)
        mx=max(mx,v["geode"])
        rx="geode"

    elif store[0]>=bp[2][0] and store[1]>=bp[2][1]:
        ts=list(store)
        tr=list(robots)
        ts[0]-=bp[2][0]
        tr[2]+=1
        ts[1]-=bp[2][1]
        v["obsidian"] = tick(bp, tuple(ts), tuple(tr), time+1)
        mx=max(mx,v["obsidian"])
        rx="obsidian"
        
    else:
        if store[0]>=bp[1]:
            ts=list(store)
            tr=list(robots)
            ts[0]-=bp[1]
            tr[1]+=1
            v["clay"] = tick(bp, tuple(ts), tuple(tr), time+1)
            mx=max(mx,v["clay"])
            rx="clay"

        if store[0]>=bp[0]:
            ts=list(store)
            tr=list(robots)
            ts[0]-=bp[0]
            tr[0]+=1
            v["ore"] = tick(bp, tuple(ts), tuple(tr), time+1)
            mx=max(mx,v["ore"])
            rx="ore"
        

        v["none"] = tick(bp,store,robots,time+1)
        mx=max(mx,v["none"])
        rx="none"
        # select the best path


    return mx
        
    
def optimize(bp):

    store=(0,0,0,0)
    robots=(1,0,0,0)
    time=1
    
    # maximize the number of open geodes after 24 minutes
    #

    return tick(bp, store, robots, time)
    
print(optimize(bp[0]))

# hypothesis
# the optimal construction of robots is to maximize the construction of geode robots
# that is, we can construct a tree leading up to what we need to construct such a thing

# geode = A*ore + B*obsidian
# obsidian = C*ore + D*clay
# clay = E*ore
# ore = F*ore

# pattern

# geode = 2*ore+7*obsidian
# obsidian = 3*ore + 14*clay
# clay = 2*ore
# ore = 4*ore

# question: How do we maximize geode and minimize waste?

# 24 cycles

