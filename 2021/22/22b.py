#!/usr/bin/python3

import sys
from box import Box,OverlapError
from reactor import Reactor
from termcolor import colored

# run the tests

#import test


#import networkx as nx
#import matplotlib.pyplot as plt

#G = R.interactions()

#nx.draw(G,  with_labels=True)
#plt.savefig("graph.png")


import test
test.second()
test.third()
R=test.fourth()
#R.savefig()
print(R.size())

sys.exit()
# - finally, read input from stdin and solve the problem

R = Reactor()

def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:
        l = l.strip()

        b = Box(l)
        RR = RR + b
        
    return RR

R = readinaTOR()

R.optimize()

for i in range(len(R.realcubes)-1,-1,-1):
    if R.realcubes[i].x2 < -50 or R.realcubes[i].z2 < -50 or R.realcubes[i].y2 < -50:
        R.realcubes.pop(i)
    elif R.realcubes[i].x1 > 51 or R.realcubes[i].z1 > 51 or R.realcubes[i].y1 > 51:
        R.realcubes.pop(i)
    else:
        R.realcubes[i].x1 = max(-50,R.realcubes[i].x1)
        R.realcubes[i].y1 = max(-50,R.realcubes[i].y1)
        R.realcubes[i].z1 = max(-50,R.realcubes[i].z1)

        R.realcubes[i].x2 = min(51,R.realcubes[i].x2)
        R.realcubes[i].y2 = min(51,R.realcubes[i].y2)
        R.realcubes[i].z2 = min(51,R.realcubes[i].z2)



s = sum([x.size() for x in R.realcubes])
print(s)
#print(R.realcubes)
#R.savefig()

# 1013549392644644 is too low

