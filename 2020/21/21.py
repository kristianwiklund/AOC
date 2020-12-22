#!/usr/bin/python3

import sys
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

foods = dict()
foodc=dict()
allergens=dict()
allerc=dict()

G = nx.DiGraph()

def readone(G,line,foods, allergens):

    line=line.strip("\n)")
    t=line.split("(")
    #    print(line)
    a=t[0]
    b=t[1].replace(",","")

    a=a.strip(" ").split(" ")

    b=b.split(" ")

    
    for i in a:
        if not i in foodc:
            foodc[i]=1
        else:
            foodc[i]+=1
            
        if not i in foods:
            foods[i] = list()

        foods[i].append(set(b)) # all potential allergenes for this food
    
        for j in b:
            #           print(str(i)+"->"+str(j))
            G.add_edge(i,j)

    for i in b:
        if not i in allerc:
            allerc[i]=1
        else:
            allerc[i]+=1
        
        if not i in allergens:
            allergens[i] = list()
        allergens[i].append(set(a))
        
    return (foods,allergens)

# -- "main" --

line=sys.stdin.readline()
while line:
    (foods,allergens)=readone(G,line,foods,allergens)
    line=sys.stdin.readline()

print (allergens)



