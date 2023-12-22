import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

q=[]

arr = readarray("input",split="->",convert=lambda x:x.strip())
arr = [(x[0][1:],x[0][0],[i.strip() for i in x[1].split(",")]) for x in arr]
barr = {x[0]:x[1] for x in arr}

G=nx.DiGraph()
for x in arr:
    G.add_node(x[0],type=x[1])

for x in arr:
    for i in x[2]:
        G.add_edge(x[0],i)

for x in G.nodes():
    v=[]
    for y in G.in_edges(x):
        v.append(y[0])

    try:
        if barr[x]=="&" and len(v)==1:
            print (x,"= not",v[0])
        elif barr[x]=="&":
            print (x,"= not ("," and ".join(v),")")
        else:
            if len(v)>1:
                print (x,"= ronk",v)
            else:
                print (x,"= ",barr[x],v)
    except:
        if x=="rx":
            print(x,"=",v[0])
