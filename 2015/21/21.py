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
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

with open("shop.txt","r") as fd:

    wt = readblock(fd)[1:]
    at = readblock(fd)[1:]
    rt = readblock(fd)[1:]

    w={}
    
    for i in wt:
        t = i.split(" ")[0]
        m = ints(i)
        w[t]=m

        #    print(w)
        
    a={}
    
    for i in at:
        t = i.split(" ")[0]
        m = ints(i)
        a[t]=m

    a["naked"] = (0,0,0)
        
    r={}
    
    for i in rt:
        print(i)
        t = " ".join(i.split(" ")[0:2])
        m = ints(" ".join(i.split(" ")[2:]))
        r[t]=m

    r["no ring R"] = (0,0,0)
    r["no ring L"] = (0,0,0)
        
    def predict(player, boss):
        # we deal max(p.dam - b.armor, 1) damage per turn, meaning that we take down the boss in b.hp / max(p.dam - b.armor, 1) turns
        # likewise, the boss takes us down in p.hp/max(b.dam - p.armor,1) turns -> we need to have higher score than the boss
        
        pwinsin = boss["hp"]/max(player["damage"]-boss["armor"],1)
        bwinsin = player["hp"]/max(boss["damage"]-player["armor"],1)
        
        pprint (player)
        pprint (boss)
        
        
        ## who wins prediction
        
        if pwinsin <= bwinsin:
            print ("PLAYER will win in",pwinsin,"turns")
            print("---")

            return 1
        
        else:            
            print ("BOSS will win in",bwinsin,"turns")
            print("---")

            return -1
            

    def fight(player, boss):

        # player hits boss
        boss["hp"]-=max(1, player["damage"]-boss["armor"])
        if boss["hp"]<=0:
#            print ("player wins")
            return 1
        
        # boss hits player
        player["hp"]-=max(1, boss["damage"]-player["armor"])
        if player["hp"]<=0:
#            print ("boss wins")
            return -1

        return 0

    #pprint (player)
    #pprint (boss)


    def deathmatch(player, boss):
        while True:
            ap = fight(player,boss)
            if ap:
                return ap
       
    

    player = {"who":"player", "hp":8, "damage":5, "armor":5}
    boss = {"who":"boss", "hp":12, "damage":7, "armor":2}

    playerwins = predict(player, boss)

    while True:
        ap = fight(player,boss)
        if ap:
            break
        
        pprint (player)
        pprint (boss)
        print("---")


    if ap == playerwins:
        print("Prediction correct")
    else:
        print("Prediction false")


    # real data
    

    minsta = 239889238924
    mesta= 0 
    for i,ww in enumerate(w):
        for j,aa in enumerate(a):
            for k,rr in enumerate(r):
                for l,rl in enumerate(r):
                    if k==l:
                        continue

                    player = {"who":"player", "hp":100, "damage":0, "armor":0}
                    boss = {"who":"boss", "hp":104, "damage":8, "armor":1}



                    cost = w[ww][0]+a[aa][0]+r[rr][0]+r[rl][0]
                    armor = w[ww][2]+a[aa][2]+r[rr][2]+r[rl][2]
                    damage = w[ww][1]+a[aa][1]+r[rr][1]+r[rl][1]
                    

                    player["damage"]=damage
                    player["armor"]=armor

                    ap = deathmatch(player,boss)

                    if ap==-1:
                        if cost>mesta:
                            print("FAIL:", ww,"-",aa,"-",rr,"-",rl, "dam:", damage, "ac:", armor, "cost:",cost)                        
                            mesta=cost
                            
                    if ap==1:
                        if cost<minsta:
                            print("WIN:", ww,"-",aa,"-",rr,"-",rl, "dam:", damage, "ac:", armor, "cost:",cost)                        
                            minsta=cost



    print("cheapest win is",minsta)
    print("expensivest fail is",mesta)

    
