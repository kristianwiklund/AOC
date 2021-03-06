#!/usr/bin/python3

# solution:
# dump everything into a graph
# plot it
# look at the corners. done

# part 2: todo:
# order the nodes. Then look at the edges again, don't use the numbers

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
    A.reverse()

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

pics = getpix(sys.argv[1])

#print (pics)

for i in pics:

    for j in pics[i]:
        if not type(j) is list:
            G.add_edge(str(i),"E"+str(j)+"E")
            #            print(str(i)+"--"+str(j)+":"+str(pics[i]))

pos = nx.kamada_kawai_layout(G)
#nlist = [x for x in G.nodes() if "N" in x]
#nx.draw_networkx(G, pos, node_size=30, font_size=3, with_labels=True, nodelist=nlist)
#plt.savefig("pix2.pdf")

# the corners of the plotted graph contains the nodes of interest.
# now, what properties do they have?!
# -> they are the only nodes for which only two adjacent edges are connected.

# hence, start by removing all "E" nodes.

elist = [x for x in G.nodes() if "E" in x]
#pprint(elist)

H = copy.deepcopy(G)

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

nx.draw_networkx(G, pos, node_size=30, font_size=3, with_labels=True)
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


def draw2(paper):
    for i in range(0, len(paper)):
        for x in range(1,9):
            for j in range(0, len(paper[i])):
                print (pics[paper[i][j]][9][x][1:9],end='')
            print("")
    

def draw(paper, merge=False):

    if merge:
        draw2(paper)
        return
    
    for i in range(0, len(paper)):
        for x in range(0,len(paper[i])):
            print("{node:^10}".format(node=paper[i][x]),end=' ')
        print("")
        for x in range(0,10):
            for j in range(0, len(paper[i])):
                print (pics[paper[i][j]][9][x],end=' ')
            print("")
        print("")
        
#draw(paper)


# the next problem is to find out if we are oriented correct.

# start by orienting the first line (edge) in the correct direction (top to bottom)
# what we need is to move the first one to align with the node behind it
# then we zip up the rest

# so, what points to the bottom?
# the first edge does, that's what points to the bottom

def rpic90(A):

    NA=list()
#    print("---------")
#    pprint(A)
    
    for y in range(0,len(A)):
        s = ""
        for x in range(0,len(A)):
            s=s+A[x][y]
        NA.append(s[::-1])

        #    pprint(NA)
        #    print("---------")
    return(NA)


def rot90(node):
    #    print("rot90")
    #    return (myid, (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A))
    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A) = node
    #    print(A)
    A = rpic90(A)
    return (myid, left ,right,bottom,top,rleft, rright, rbottom, rtop,A)

def rot180(n):
    #    print("rot180:")
    return rot90(rot90(n))

    
def rot270(n):
    #    print("rot270:")
    return rot90(rot90(rot90(n)))

#draw(paper)

p = list(nx.shortest_path(G,edge[0],edge[1]))[1]
p = int(p.replace("E",""))
print (str(edge[0])+"-"+str(edge[1])+" Aligning to "+str(p))

def norot(n):
    #print("norot")
    return n

print ("(myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A)")
print(pics[edge[0]])

def vflip(node):
    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A) = node
    #    print(A)
    A.reverse()
    return (myid, rbottom,rtop,left,right,top,bottom,rleft,rright,A)

def hflip(node):
    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A) =  node
    #    print(A)
    B = list()
    for i in A:
        B.append(i[::-1])
    return (myid, rbottom,rtop,left,right,top,bottom,rleft,rright,B)


# line up the first tile
success=False
for i in [lambda x:norot(x), lambda x:rot90(x), lambda x:rot180(x), lambda x:rot270(x), lambda x:vflip(x), lambda x:hflip(x)]:
#    return (myid, (myid, top,bottom,left,right,rtop,rbottom,rleft,rright,A))
    ap = i(pics[edge[0]])
    if ap[2] == p or ap[6] == p:
        success=True
        pics[edge[0]]=ap
                
        break

if not success:
    print("bad error fail")



def fingerprint(A):

    ll = "".join([x[9] for x in A])
    lr = "".join([x[0] for x in A]) 
    
    top = A[0]
    bottom = A[9]
    right = ll
    left = lr

    return (top,right,bottom,left)


def fpmatch(paper, pics, what, who):

    fp = fingerprint(pics[who][9])
    
    if what in fp:
        i = fp.index(what)
        ri=None
    elif what[::-1] in fp:
        ri = fp.index(what[::-1])
        i=None
    else:
        #draw(paper)
        #print (who, what, fp)
        raise RuntimeError # meaning that we didn't find any match at all, which we should since the tiles are basic ordered

    return(i,ri)

def matchup(paper, pics, parent, child):

    # get the bottom of the parent
    what = fingerprint(pics[parent][9])[2]

    (i,ri) = fpmatch(paper, pics, what, child)
    if i==0:
        return # already matched    


    if i is not None:
        if i==1:
            pics[child] = rot270(pics[child])
        elif i==3:
            pics[child] = hflip(rot90(pics[child]))
        elif i==2:
            pics[child] = vflip(pics[child])
        else:
            draw(paper)
            print("Matching top",parent,child)
            print (i,ri)
            sys.exit()

        
    if ri is not None:
        if ri == 2:
            pics[child] = rot180(pics[child])
        elif ri==0:
            pics[child] = hflip(pics[child])
        elif ri==1:
            pics[child] = hflip(rot270(pics[child]))
        elif ri==3:
            pics[child] = rot90(pics[child])
        else:
            draw(paper)
            print("Matching top",parent,child)
            print (i,ri)
            sys.exit()
            
    
def matchleft(paper, pics, parent, child):

    # get the right side of the parent
    what = fingerprint(pics[parent][9])[1]
    
    (i,ri) = fpmatch(paper, pics, what, child)

    if i==3:
        return # already matched
    
    if i is not None:
        if i == 0:
            pics[child] = rot270(pics[child])
        elif i==2:
            pics[child] = rot90(pics[child])
        elif i == 3:
            pics[child] = rot180(pics[child])
        elif i==1:
            pics[child] = hflip(pics[child])
        else:
            draw(paper)
            print("Matching side",parent,child)
            print (i,ri)
            sys.exit()
            
    if ri is not None:
        if ri == 3:
            pics[child] = vflip(pics[child])
        elif ri ==1:
            pics[child] = rot180(pics[child])
        elif ri == 0:
            pics[child] = rot270(pics[child])
        elif ri == 2:
            pics[child] = vflip(rot90(pics[child]))
        else:
            draw(paper)
            print("Matching side",parent,child)
            print (i,ri)
            sys.exit()

def alignzor(paper, pics, x,y):
    # investigate alignment in two directions: up and to the right

    if y-1 > -1:
        abovetile=paper[y-1][x]
        matchup(paper, pics, abovetile, paper[y][x])


    if x-1>-1:
        lefttile=paper[y][x-1]
        matchleft(paper, pics, lefttile, paper[y][x])

# first try the first tile
try:
    alignzor(paper,pics,1,0)
except:
    print("flipping first tile")
    pics[paper[0][0]] = hflip(pics[paper[0][0]])
    
for y in range(0,len(paper)):
    for x in range(0,len(paper)):
        alignzor(paper,pics,x,y)

print("--- sea ---")
draw(paper,merge=True)

        
#alignzor(paper,pics, 2,0)
#draw(paper)
#alignzor(paper,pics, 2,1)
#draw(paper)
#draw(paper,merge=True)





