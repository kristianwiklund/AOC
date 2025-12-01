import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache
from cachetools import cached,LRUCache
from cachetools.keys import hashkey

arr = readarray("input.short",split=".",convert=lambda x:x)

bp={}

for ii,i in enumerate(arr):
    print(i)
    # ['Blueprint 1: Each ore robot costs 4 ore', '  Each clay robot costs 2 ore', '  Each obsidian robot costs 3 ore and 14 clay', '  Each geode robot costs 2 ore and 7 obsidian', '']

    bp[ii] = (int(i[0].strip().split(" ")[6]),
             int(i[1].strip().split(" ")[4]),
             (int(i[2].strip().split(" ")[4]), int(i[2].strip().split(" ")[7])),
             (int(i[3].strip().split(" ")[4]),int(i[3].strip().split(" ")[7])))
    print(bp)

best=0
firstgeode=1000

front=SortedSet(key=lambda x:(x[2][0]+x[2][1]*10+x[2][2]*100+x[2][3]*1000))

def mkstr(t,inv,bots,buy):
    return ""
    return str(t)+":"+str(inv)+" "+str(bots)+buy+"\n"
    

prune=0
gobbabobb={}


@cached(cache=LRUCache(maxsize=20000000),key=lambda bp,bots,inv,t,tl,**kwargs:hashkey(bp,bots,inv,t))
#@cached(cache={},key=lambda bp,bots,inv,t,tl:hashkey(bp,bots,inv,t))
def diggy(bp, bots, inv, t, tl,limit=24,bobarob=None):
    global best
    global firstgeode
    global prune
    
    ore, clay, obsidian, geode = 0,1,2,3

    bots=list(bots)
    inv=list(inv)

#    print(t,inv,bots)
    
    # mining
#¤    for i in range(4):
#        inv[i]+=bots[i]

    # check if we are done
    if t>=limit:
        if inv[geode]+bots[geode]>best:
            print("NB:",inv[geode]+bots[geode],"limit:",limit,"\ntl:",tl)
            print("------------------------")
            best=inv[geode]+bots[geode]
            return best
        else:
            return 0

#    if limit==32:
#        if bots[geode]==0 and t>bobarob:
#            prune+=1
#            return 0
        
    if bots[geode]==0 and firstgeode<t:
        prune+=1
        return 0
        
    om = 0

    if inv[ore]>=bp[geode][0] and inv[obsidian]>=bp[geode][1]:
        ap = (bots[0],bots[1],bots[2],bots[3]+1)

        if t+1<firstgeode:
            print("first geode at",t+1,"old=",firstgeode)
            firstgeode=t+1
            
        nm=diggy(bp, ap, (inv[ore]-bp[geode][0]+bots[ore], inv[clay]+bots[clay], inv[obsidian]-bp[geode][1]+bots[obsidian], inv[geode]+bots[geode]), t+1,tl+mkstr(t,inv,bots,"geode"),limit=limit)
        #        print("bpt")
        om = max(nm,om)
        
    if inv[ore]>=bp[obsidian][0] and inv[clay]>=bp[obsidian][1]:
        ap = (bots[0],bots[1],bots[2]+1,bots[3])
        nm=diggy(bp, ap, (inv[ore]+bots[ore]-bp[obsidian][0],inv[clay]+bots[clay]-bp[obsidian][1],inv[obsidian]+bots[obsidian],inv[geode]+bots[geode]),t+1,tl+mkstr(t,inv,bots,"obs"),limit=limit)
        #        print("bpt2")
        om = max(nm,om)
        
    if inv[ore]>=bp[clay]:
        ap = (bots[0],bots[1]+1,bots[2],bots[3])
        nm=diggy(bp, ap, (inv[ore]+bots[ore]-bp[clay],inv[clay]+bots[clay],inv[obsidian]+bots[obsidian],inv[geode]+bots[geode]),t+1,tl+mkstr(t,inv,bots,"clay"),limit=limit)
        #       print("bpt3")
        om = max(nm,om)
                
    if inv[ore]>=bp[ore]:
#        if t==3:
#            print(inv[ore],bp[ore])
#            sys.exit()
        ap = (bots[0]+1,bots[1],bots[2],bots[3])
        nm=diggy(bp, ap, (inv[ore]+bots[ore]-bp[ore],inv[clay]+bots[clay],inv[obsidian]+bots[obsidian],inv[geode]+bots[geode]),t+1,tl+mkstr(t,inv,bots,"ore"),limit=limit)
        #        print("bpt4")
        om = max(nm,om)
        
    nm=diggy(bp, tuple(bots), (inv[ore]+bots[ore],inv[clay]+bots[clay],inv[obsidian]+bots[obsidian],inv[geode]+bots[geode]),t+1,tl+mkstr(t,inv,bots,""),limit=limit)
    #    print("bpt5")
    om = max(nm,om)

    return om
    
#front.add((bp[1],(1,0,0,0),(0,0,0,0),1,""))

#ql=0
#for x in bp.keys():
#    print("Running",x)
#    best=0
#    prune=0
#    firstgeode=23298039823
#    diggy.cache.clear()
#    
#    a=diggy(bp[x],(1,0,0,0),(0,0,0,0),1,"")
#    ql+=(1+x)*a
#    print(x,"got",a,"pruned",prune)
#    gobbabobb[x]=firstgeode
    
#print("A:",ql)
#if len(bp)>10:
#    assert(ql==1092)

ql=0
for x in bp.keys():
    print("Running",x)
    best=0
    prune=0
    firstgeode=23298039823
    diggy.cache.clear()
    
    a=diggy(bp[x],(1,0,0,0),(0,0,0,0),1,"",limit=32)
    ql+=(1+x)*a
    print(x,"got",a,"pruned",prune)
    gobbabobb[x]=firstgeode
    
print("B:",ql)
