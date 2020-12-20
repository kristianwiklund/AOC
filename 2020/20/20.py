#!/usr/bin/python3

# solution:
# dump everything into a graph
# plot it
# look at the corners. done

import copy
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

from pprint import pprint

def readone(f):
    # parse one tile

    h = f.readline()
    h = h.strip('\n\r:')
    myid = int(h.split()[1])

    A = list()
    # then read the 10 lines
    for i in range(0,10):
        A.append(f.readline().strip('\n\r').replace("#","1").replace(".","0"))


    # process a signature for each tile

    ll = "".join([x[9] for x in A])
    lr = "".join([x[0] for x in A]) 
    
    top = int(A[0],2)
    bottom = int(A[9],2)
    left = int(ll,2)
    right = int(lr,2)

    rtop = int(A[0][::-1],2)
    rbottom = int(A[9][::-1],2)
    rleft = int(ll[::-1],2)
    rright = int(lr[::-1],2)
    
    # and discard final empty line
    f.readline()
    
    return (myid, (myid, top,bottom,left,right,rtop,rbottom,rleft,rright))

def getpix(fname):
    with open(fname,"r") as fd:
        pics = dict()
        
        try:
            while True:
                t = readone(fd)
                #pprint(t)
                pics[t[0]] = t[1]
        except:
            pass

        return pics

pics = getpix("input")
print (pics)

for i in pics:
    for j in pics[i]:
        G.add_edge("N"+str(i)+"N","E"+str(j)+"E")
        #        print(str(i)+"--"+str(j)+":"+str(pics[i]))

pos = nx.kamada_kawai_layout(G)
nlist = [x for x in G.nodes() if "N" in x]
nx.draw_networkx(G, pos, node_size=30, font_size=3, with_labels=True, nodelist=nlist)
plt.savefig("pix.pdf")
    
