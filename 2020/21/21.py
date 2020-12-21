#!/usr/bin/python3

import sys
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

foods = dict()

G = nx.DiGraph()

def readone(G,line,foods):

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
        foods[i].append(set(b))
        for j in b:
            #           print(str(i)+"->"+str(j))
            G.add_edge(i,j)
    return foods

# -- "main" --

line=sys.stdin.readline()
while line:

    foods=readone(G,line,foods)
    line=sys.stdin.readline()

#print("-")
#pprint(foods)
#print("-")

# we now have a list of foods with associated potential allergies.
# find the easy ones first

def findfood(foods, nr):
    bop = dict()
    bap = dict()

    for i in foods:
        u= [x for x in foods[i] if len(x)==nr]
        if len(u):
            bop[i]=u

            p= set()
            for x in u:
                p|=x
                bap[i]=p

                #    return(bap)
    return({x:bap[x] for x in bap if len(bap[x])==nr})

print(findfood(foods,1))
#print(G.nodes())
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos, node_size=30, font_size=3, with_labels=True)
plt.savefig("pix.pdf")
