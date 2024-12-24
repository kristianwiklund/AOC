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
from pyeda.inter import *

with open("input","r") as fd:
    input = readblock(fd,convert=lambda x:tuple(x.replace(" ","").split(":")))
    logic = readblock(fd,convert=lambda x:[y.strip() for y in x.split("->")])

G = nx.DiGraph()



import operator
lolol={"XOR":Xor, "AND":And, "OR":Or}

#print(input)

xin = [t for t in input if t[0].startswith("x")]
yin = [t for t in input if t[0].startswith("y")]
#print(logic)
zout = [t[1] for t in logic if t[1].startswith("z")]
#print("z",zout)

thex = exprvars("x",len(xin))
they = exprvars("y",len(yin))
thez = exprvars("y",len(zout))

for i,l in enumerate(input):
#    print("i",i,l)
    a,v=l
    if a.startswith("x"):
        nl = (a,v,thex[ints(a)[0]])
    else:
        nl = (a,v,they[ints(a)[0]])
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
        if s:
            return nx.get_node_attributes(G,"inp")[n]
        else:
            if n.startswith("x"):
                return thex[ints(n)[0]]
            else:
                return they[ints(n)[0]]
            
    
    ie = list(ie)
  #  print("ie",ie)
    op = nx.get_node_attributes(G,"op")[n]
    
    return op(pappagrappa(ie[0][0], s=s),pappagrappa(ie[1][0], s=s), simplify=s)

def calculon(G,minimize=True):
    
    outs={}
    for o in (node for node, out_degree in G.out_degree() if out_degree == 0):
        # print("o",o)
        outs[o] = pappagrappa(o,s=minimize)

    if not minimize:
        return (None, None, outs)
    
    s=""
    for i in sorted(outs.keys(),key=lambda x:-ints(x)[0]):
        print(i,outs[i])
        s+=str(outs[i])
    print("")

    ans=int(s,2)

    return(s,ans, outs)

# ---------------
s,ans,_=calculon(G)

print("A:",ans)
# ---------------

sx=""
for x in sorted(xin,key=lambda v:-ints(v[0])[0]):
    sx+=x[1]

xval = int(sx,2)
print("x=",xval)

sy=""
for y in sorted(yin,key=lambda v:-ints(v[0])[0]):
    sy+=y[1]

yval = int(sy,2)
print("y=",yval)

print("x+y=",xval+yval)

sval = "{0:b}".format(xval+yval)

print("{:>40}".format(sval))
print("{:>40}".format(s))

print(thex,they)

_,_,outs = calculon(G,minimize=False)
print(outs)
import graphviz
import pathlib

gvsrc=expr2bdd(outs["z00"]).to_dot()
fp=pathlib.Path("ap.gv")
fp.write_text(gvsrc,encoding="ascii")

# ---------------------------

print("-----")

H = G.reverse()
for z in zout:
    print(z,list(nx.ancestors(G,z)))

