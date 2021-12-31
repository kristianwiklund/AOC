#!/usr/bin/python3

import sys
from box import Box,OverlapError
from reactor import Reactor
from termcolor import colored

# run the tests

#import test

# - finally, read input from stdin and solve the problem

R = Reactor()

def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:
        l = l.strip()

        b = Box(l)
        RR = RR + b
        
    return RR

#R = readinaTOR()
#print(len(R.cubes))
#R.optimize()
#print(len(R.cubes))

#import networkx as nx
#import matplotlib.pyplot as plt

#G = R.interactions()

#nx.draw(G,  with_labels=True)
#plt.savefig("graph.png")

# tests for complete overlap on 2 axes
# test Z
a = Box("on x=2..4,y=2..4,z=2..4")
b = Box("off x=1..4,y=1..4,z=-12..2")
v = a-b
print(v)
assert (v[0] == Box("on x=2..4,y=2..4,z=3..4"))

a = Box("on x=1..4,y=1..4,z=1..4")
b = Box("off x=1..4,y=1..4,z=3..4")
v = a-b
assert (v[0] == Box("on x=1..4,y=1..4,z=1..2"))

# test X
a = Box("on x=1..4,y=1..4,z=1..4")
b = Box("off x=-12..2,y=1..4,z=1..4")
v = a-b
assert (v[0] == Box("on x=3..4,y=1..4,z=1..4"))

a = Box("on x=1..4,y=1..4,z=1..4")
b = Box("off x=3..12,y=1..4,z=1..4")
v = a-b
assert (v[0] == Box("on x=1..2,y=1..4,z=1..4"))

# test y

a = Box("on x=1..4,y=1..4,z=1..4")
b = Box("off x=1..4,y=-12..2,z=1..4")
v = a-b
assert (v[0] == Box("on x=1..4,y=3..4,z=1..4"))

a = Box("on x=1..4,y=1..4,z=1..4")
b = Box("off x=1..4,y=3..12,z=1..4")
v = a-b
assert (v[0] == Box("on x=1..4,y=1..2,z=1..4"))

# trivial cases of cutting in half seems to work.
# now for the cases where we cut a corner off a
