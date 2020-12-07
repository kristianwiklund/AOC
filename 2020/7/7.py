#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain

G = nx.DiGraph()

def bagparse(G, line):

    #<light red> bags contain <<1> <bright white> bag>, <<2> <muted yellow> bags>.
    #<line> := <color> "bags contain" [<bagdef>, ..., <bagdef>]
    #<bagdef> := <color> bag|bags

    line = line.strip()
    line = line.replace(" bags contain no other bags.","")
    line = line.replace(" bags contain ",",")
    line = line.replace(" bag, ",",")
    line = line.replace(" bags, ",",")
    line = line.replace(" bags.", "")
    line = line.replace(" bag.", "")
    a = line.split(",")
    b = a.pop(0)

    for i in a:
        i = i.split(" ")
#        print(b+"->"+" ".join(i[1:]))
        G.add_edge(b, " ".join(i[1:]), weight=int(i[0]))

def bop(G, l):

    t = l
    s = set(t)
#    print(list(t))
    for i in l:
#        print(i)
#        print(i+"->"+str(list(G.predecessors(i))))
        x = bop(G,list(G.predecessors(i)))
 #       print(x)
        s=s.union(x)
           
    return (s)

def bap(G, n, l):

    t = l
    s = 0

    if len(l) == 0:
        return 1
    for i in l:
        w = G.edges[n, i]["weight"]

        x = bap(G,i, list(G.successors(i)))
#        print(n+"->"+str(w)+"->"+i+" = "+str(x))
        s=s+w*x
           
    return (s+1)
        
with open ("input") as fd:
    
    for  line in fd:
        bagparse(G, line)



    if "shiny gold" in G:

        n = bop(G, list(G.predecessors("shiny gold")))
        print("A="+str(len(n)))
        Y = G.subgraph(list(n)+["shiny gold"])
#        print(list(Y))
        nx.draw(Y,  with_labels=True)
        plt.savefig("bags.png")
        
        # -----

        m = bap(G, "shiny gold", list(G.successors("shiny gold")))
        print("B="+str(m-1))



