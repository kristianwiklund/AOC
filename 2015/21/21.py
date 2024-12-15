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

    a={}
    
    for i in at:
        t = i.split(" ")[0]
        m = ints(i)
        a[t]=m

    r={}
    
    for i in rt:
        t = i.split(" ")[0]
        m = ints(i)
        r[t]=m


    def fight(player, boss):

        # player hits boss
        boss["hp"]-=max(1, player["damage"]-boss["armor"])
        if boss["hp"]<=0:
            print ("player wins")
            return 1
        
        # boss hits player
        player["hp"]-=max(1, boss["damage"]-player["armor"])
        if player["hp"]<=0:
            print ("boss wins")
            return -1

        return 0

    

    

    #pprint (player)
    #pprint (boss)

        

    player = {"who":"player", "hp":8, "damage":5, "armor":5}
    boss = {"who":"boss", "hp":12, "damage":7, "armor":2}


    # we deal max(p.dam - b.armor, 1) damage per turn, meaning that we take down the boss in b.hp / max(p.dam - b.armor, 1) turns
    # likewise, the boss takes us down in p.hp/max(b.dam - p.armor,1) turns -> we need to have higher score than the boss

    pwinsin = boss["hp"]/max(player["damage"]-boss["armor"],1)
    bwinsin = player["hp"]/max(boss["damage"]-player["armor"],1)

    pprint (player)
    pprint (boss)
    print("---")
    
    if pwinsin <= bwinsin:
        print ("player will win in",pwinsin,"turns")
    else:
        print ("boss will win in",bwinsin,"turns")
    
    while not fight(player,boss):
        pprint (player)
        pprint (boss)
        print("---")

    pprint (player)
    pprint (boss)

    
    
