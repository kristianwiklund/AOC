import networkx as nx
import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

G = nx.DiGraph()

snumpad = ["789","456","123","X0A"]
sdirpad = ["X^A","<v>"]

bop="^>v<"

for y,l in enumerate(snumpad):
    for x,v in enumerate(l):
        if v=="X":
            continue
        
        a = checkallpos(snumpad,x,y,fun = lambda x:x!="X", outofbounds=False)
        for i,w in enumerate(a):
            if w:
                n = snumpad[y+dirs[i][1]][x+dirs[i][0]]
                if n!=v:
                    #print(v,"->",n)
                    G.add_edge(v, n, d=bop[i])
                
numpad={}        
for i in "".join(snumpad):
    for j in "".join(snumpad):
        if i=="X" or j=="X":
            continue
        if i==j:
            continue
        
        pths = list(nx.all_shortest_paths(G,i,j))
        #        print(i,"->",j,":",len(pths))
        numpad[i,j]=[]
        for pth in pths:                        
            eal = "".join([G[pth[i]][pth[i+1]]['d'] for i in range(len(pth[:-1]))])+"A"
            numpad[i,j].append(eal)
        numpad[i,j]=sorted(numpad[i,j],key=len)
        
#print(numpad)
G = nx.DiGraph()

for y,l in enumerate(sdirpad):
    for x,v in enumerate(l):
        if v=="X":
            continue
        
        a = checkallpos(sdirpad,x,y,fun = lambda x:x!="X", outofbounds=False)
        for i,w in enumerate(a):
            if w:
                n = sdirpad[y+dirs[i][1]][x+dirs[i][0]]
                if n!=v:
                    #print(v,"->",n)
                    G.add_edge(v, n, d=bop[i])
                
dirpad={}        
for i in "".join(sdirpad):
    for j in "".join(sdirpad):
        if i=="X" or j=="X":
            continue
        if i==j:
            continue
        
        pths = list(nx.all_shortest_paths(G,i,j))
        #        print(i,"->",j,":",len(pths))
        dirpad[i,j]=[]
        for pth in pths:                        
            eal = "".join([G[pth[i]][pth[i+1]]['d'] for i in range(len(pth[:-1]))])+"A"
            dirpad[i,j].append(eal)
        dirpad[i,j]=sorted(dirpad[i,j],key=len)
#------------------------------

rnumpad={}
# ('A', '4'): ['^^<<A', '^<^<A', '<^^<A', '^<<^A', '<^<^A'],

for i in numpad:
    fr = i[0]
    tto = i[1]
    mx = numpad[i]

    for j in mx:
        j=j[:-1]
        rnumpad[fr,j]=tto # remove separator "A"
    
#pprint(dirpad)


rdirpad={}

for i in dirpad:
    fr = i[0]
    tto = i[1]
    mx = dirpad[i]

    for j in mx:
        j=j[:-1]
        rdirpad[fr,j]=tto # remove separator "A"

#pprint(rdirpad)

def decodedir(st):
    
    st = st.split("A")[:-1]
    print(st)
#    print("st",st)
    pos="A"

    n=""
    for i in st:
        if i=="":
            x=pos
        else:
            x=rdirpad[pos,i]
        pos=x
        n+=x
    return (n)

def decodenum(st):
    
    st = st.split("A")[:-1]
    
    pos="A"

    n=""
    for i in st:
        try:
            x=rnumpad[pos,i]
        except:
            #pprint(rnumpad)
            #pprint(numpad)

            print(pos,i)
            print(st)
            sys.exit()
        pos=x
        n+=x
    return (n)


            
