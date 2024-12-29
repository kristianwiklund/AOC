import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache

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

@cache
def run(bp, bots, inv, building, t, tl):
    global best
    
    ore, clay, obsidian, geode = 0,1,2,3

    bots=list(bots)
    inv=list(inv)
    tl=list(tl)
    
    if t>24:
#        print(inv[geode])
#        print(bots,inv)
#        print(inv[geode],tl)
        if inv[geode]>best:
            print("New best:", inv[geode])
            best=inv[geode]
        return (inv[geode], bots, tl)

    for i in range(4):
        inv[i]+=bots[i]

    if building:
        bots[building]+=1
        tl.append((t,building))

        
    print(t,": digging, now we have",inv,"ores and",bots,"bots")
        

        
    # try buying things

    mx = 0
    nx = None
    nt = ""
    b=None
    
    tl=tuple(tl)

    if inv[ore]>=bp[geode][0] and inv[obsidian]>=bp[geode][1]:
        #print("buy geode")
        px,bx,tx = run(bp, tuple(bots), (inv[ore]-bp[geode][0], inv[clay], inv[obsidian]-bp[geode][1], inv[geode]), geode, t+1,tl)
        if px>mx:
            mx=px
            nx=bx
            nt=tx
            b=geode
    if inv[ore]>=bp[obsidian][0] and inv[clay]>=bp[obsidian][1]:
        px,bx,tx = run(bp, tuple(bots), (inv[ore]-bp[obsidian][0],inv[clay]-bp[obsidian][1],inv[obsidian],inv[geode]),obsidian,t+1,tl)
        #print("buy obsidian")
        if px>mx:
            mx=px
            nx=bx
            nt=tx
            b=obsidian
    if inv[ore]>=bp[clay]:
        #print("buy clay")        
        px,bx,tx = run(bp, tuple(bots), (inv[ore]-bp[clay],inv[clay],inv[obsidian],inv[geode]),clay,t+1,tl)
        if px>mx:
            mx=px
            nx=bx
            nt=tx
            b=clay

    if inv[ore]>=bp[ore]:
        #print("buy ore")
        px,bx,tx = run(bp, tuple(bots), (inv[ore]-bp[ore],inv[clay],inv[obsidian],inv[geode]),ore,t+1,tl)
        if px>mx:
            mx=px
            nx=bx
            nt=tx
            b=ore
            

    #else:      
    px,bx,tx = run(bp, tuple(bots), tuple(inv),False,t+1,tl)
    if px>mx:
        mx=px
        nx=bx
        nt=tx
        b=None

#    if b and mx==best:
#        print(t+1,"bought",b,"inv=",inv)
        
    return (mx,nx,nt)


for i in bp:
    best=0
    print (i,":",run(bp[i],(1,0,0,0),(0,0,0,0),False,1,()))
