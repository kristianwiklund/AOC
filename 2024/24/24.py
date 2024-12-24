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

with open("input.short","r") as fd:
    input = readblock(fd,convert=lambda x:x.replace(" ","").split(":"))
    logic = readblock(fd,convert=lambda x:[y.strip() for y in x.split("->")])

G = nx.DiGraph()

import operator
lolol={"XOR":operator.xor, "AND":operator.__and__, "OR":operator.__or__}

for x in logic:
    print(x)
    a,g,b=x[0].split()
    c=x[1]
    G.add_node(a+b+c,fun=lolol[g])
    G.add_edge(a,a+b+c)
    G.add_edge(b,a+b+c)
    G.add_edge(a+b+c,c)

nx.draw(G, with_labels=True)
plt.show()

