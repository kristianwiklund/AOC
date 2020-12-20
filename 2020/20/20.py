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
    myid = str(h.split()[1])

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
    
    return (myid, (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A))

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

pics = getpix("input.short")
#print (pics)

for i in pics:
    for j in pics[i]:
        G.add_edge(str(i),"E"+str(j)+"E")
        #        print(str(i)+"--"+str(j)+":"+str(pics[i]))

pos = nx.kamada_kawai_layout(G)
#nlist = [x for x in G.nodes() if "N" in x]
#nx.draw_networkx(G, pos, node_size=30, font_size=3, with_labels=True, nodelist=nlist)
#plt.savefig("pix.pdf")

# the corners of the plotted graph contains the nodes of interest.
# now, what properties do they have?!
# -> they are the only nodes for which only two adjacent edges are connected.

# hence, start by removing all "E" nodes.

elist = [x for x in G.nodes() if "E" in x]
#pprint(elist)

H = copy.copy(G)

for i in elist:
    p = H.neighbors(i)
    p = list(p)
    # dump everything not connected to at least one node
    if(len(p)<2):
        H.remove_node(i)
        # else reconnect and remove
    else:
        #        print(i,p)

        for j in p:
            for k in p:
                #       print(j)
                #print(k)
                if k!=j:
                    H.add_edge(k,j)
        H.remove_node(i)

nx.draw_networkx(H, pos, node_size=30, font_size=3, with_labels=True)
plt.savefig("pix.pdf")

corners = [x for x in H.nodes() if len(list(H.neighbors(x)))==2]
print("Corners:"+str(corners))

# part 2 - find the sea monsters...
# there are no diagonals in the graph.
# do a chomp line by line to draw the area

# first find an edge between two corners

corners2 = copy.copy(corners)
corners2.remove(corners[0])

edges = [x for x in corners2 if len(list(nx.shortest_path(H,corners[0],x)))==int(math.sqrt(len(pics)))]

edge = list(nx.shortest_path(H,corners[0],edges[0]))

#print(corners[0],edge,edges[0])

# this edge is by definition horizontal and on the top, and starts at 0,0 and this is where we anchor everything

# now we can find the bottom edge by using the second node in "edges", and the node NOT included in (edges+corners[0])
corners3=copy.copy(corners)
corners3.remove(corners[0])
corners3.remove(edges[0])
#print(corners3)
edge2 = list(nx.shortest_path(H,corners3[0],corners3[1]))
#print(corners3[0],edge2,corners3[1])

# now we have two opposing edges. We need to order them to make sure that we do not get it the wrong way.
# this we do by checking the distance between the two first nodes in each edge

#print(edge,edge2)

if (len(list(nx.shortest_path(H,edge[0],edge2[0])))!=int(math.sqrt(len(pics)))):
    edge2.reverse()

# finally, move from top to bottom and draw the matrix

paper = list()

for i in range(0, len(edge)):

    p = list(nx.shortest_path(H,edge[i],edge2[i]))
    paper.append(p)

pprint(paper)

# the next problem is to find out if we are oriented correct.
# this we do by moving line by line in paper and rotating to match
# we have this information in G

def draw(paper):
    for i in range(0, len(paper)):
        for x in range(0,10):
            for j in range(0, len(paper[i])):
                print (pics[paper[i][j]][9][x],end='')
            print("")

draw(paper)
