#!/usr/bin/python3

import sys
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

foods = dict()
allergens=dict()
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
        if not i in foods:
            foods[i] = list()
        foods[i].append(set(b)) # all potential allergenes for this food
    
        for j in b:
            #           print(str(i)+"->"+str(j))
            G.add_edge(i,j)

    for i in b:
        if not b in allergens:
            allergens[i] = list()
        allergens.append(set(a))
        
    return (foods,allergens)

# -- "main" --

line=sys.stdin.readline()
while line:

    (foods,allergens)=readone(G,line,foods,allergens)
    line=sys.stdin.readline()

print (foods)
print allergens()

# find foods that are present in all lines for a specific allergene and nowhere else

al = set()

for i in foods:
    print(i)
    for j in foods[i]:
        al|=j

print(al)
print(list(foods.keys()))

uses = dict()
for i in foods:
    uses[i] = dict()
    for k in al:
        #        print(k, i, foods[i])
        uses[i][k]= len(list(filter(lambda x:k in x, foods[i])))
        
        #uses[i][k] = [len(x) for x in foods[i] if k in foods[i]]

print (uses)

aluses=dict()
                 
for i in al:
    s=0
    #print("\n"+str(i))
    for j in uses:
        #print(uses[j])
        if i in uses[j]:
            #print(j, i, uses[j][i])
            s=s+uses[j][i]
    aluses[i] = s
        
print(aluses)




