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
from cachetools import cached
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

front=SortedSet(key=lambda x:-x[4]*(x[2][1]*2+x[2][2]*4+x[2][3]*8))

def mkstr(t,inv,bots,buy):
#    return ""
    return str(t)+":"+str(inv)+" "+str(bots)+"\n"
    

@cached(cache={},key=lambda bp,bots,inv,building,t,tl:hashkey(bp,bots,inv,t))
def diggy(bp, bots, inv, building, t, tl):
    global best
    
    ore, clay, obsidian, geode = 0,1,2,3

    bots=list(bots)
    inv=list(inv)

    # mining
    for i in range(4):
        inv[i]+=bots[i]

    # check if we are done
    if t>=24:
        if inv[geode]>best:
            print(inv[geode],tl)
            best=inv[geode]
            return inv[geode]
        else:
            return False


        
    

#    print(inv)
    


    if inv[ore]>=bp[geode][0] and inv[obsidian]>=bp[geode][1]:
        ap = (bots[0],bots[1],bots[2],bots[3]+1)
        front.add((bp, ap, (inv[ore]-bp[geode][0], inv[clay], inv[obsidian]-bp[geode][1], inv[geode]), geode, t+1,tl+mkstr(t,inv,bots,"geode")))
#        print("bpt")
        
    if inv[ore]>=bp[obsidian][0] and inv[clay]>=bp[obsidian][1]:
        ap = (bots[0],bots[1],bots[2]+1,bots[3])
        front.add((bp, ap, (inv[ore]-bp[obsidian][0],inv[clay]-bp[obsidian][1],inv[obsidian],inv[geode]),obsidian,t+1,tl+mkstr(t,inv,bots,"obs")))
        #        print("bpt2")

    if inv[ore]>=bp[clay]:
        ap = (bots[0],bots[1]+1,bots[2],bots[3])
        front.add((bp, ap, (inv[ore]-bp[clay],inv[clay],inv[obsidian],inv[geode]),clay,t+1,tl+mkstr(t,inv,bots,"clay")))
#       print("bpt3")
        
    if inv[ore]>=bp[ore]:
        ap = (bots[0]+1,bots[1],bots[2],bots[3])
        front.add((bp, ap, (inv[ore]-bp[ore],inv[clay],inv[obsidian],inv[geode]),ore,t+1,tl+mkstr(t,inv,bots,"ore")))
#        print("bpt4")
        
    front.add((bp, tuple(bots), tuple(inv),False,t+1,tl+mkstr(t,inv,bots,"")))
#    print("bpt5")
                  
front.add((bp[1],(1,0,0,0),(0,0,0,0),False,1,""))


while len(front):
    v = front.pop()
    (bp,bots,inv,building,t,tl) = v
    diggy(bp,bots,inv,building,t,tl)
    print(best,len(front))
print(best)

