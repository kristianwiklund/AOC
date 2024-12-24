import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
import matplotlib.pyplot as plt
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

from pyeda.boolalg.expr import *

with open("input","r") as fd:
    input = readblock(fd,convert=lambda x:tuple(x.replace(" ","").split(":")))
    logic = readblock(fd,convert=lambda x:[y.strip() for y in x.split("->")])

G = nx.DiGraph()



import operator
lolol={"XOR":Xor, "AND":And, "OR":Or}

#print(input)
for i,l in enumerate(input):
#    print("i",i,l)
    a,v=l
    nl = [a,v,exprvar(a)]
#    input[i] = nl
    G.add_node(a,inp=int(v))#nl[2])

#print (input)
    

for x in logic:
#    print(x)
    a,g,b=x[0].split()
    c=x[1]
    G.add_node(c,op=lolol[g])
    G.add_edge(a,c)
    G.add_edge(b,c)

    
try:
    cycle = nx.find_cycle(G)
    print("The network is cyclic")
except nx.exception.NetworkXNoCycle:
    print("The network is not cyclic")

for x in G:
    if len(list(G.predecessors(x)))>2:
        print(x,"has more than two inputs")
    
#nx.draw(G, with_labels=True)
#plt.show()

def pappagrappa(n,s=False):

 #   print("enn",n)
    ie = G.in_edges(n)
    
    if not ie:
        return nx.get_node_attributes(G,"inp")[n]

    ie = list(ie)
  #  print("ie",ie)
    op = nx.get_node_attributes(G,"op")[n]
    
    return op(pappagrappa(ie[0][0]),pappagrappa(ie[1][0]), simplify=s)

    

outs={}
for o in (node for node, out_degree in G.out_degree() if out_degree == 0):
   # print("o",o)
    outs[o] = pappagrappa(o,s=True)

s=""
for i in sorted(outs.keys(),key=lambda x:-ints(x)[0]):
    print(i,outs[i])
    s+=str(outs[i])
print("")


print(s,"=",int(s,2))

assert(int(s,2)>31688159490575)

