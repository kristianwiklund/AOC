#!/usr/bin/python3

import networkx as nx
from copy import deepcopy

#import matplotlib.pyplot as plt

plan = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "###A#D#C#A###",
    "#############"]

def path_weight(G,path, weight):
    
    multigraph = G.is_multigraph()
    cost = 0

    for node, nbr in nx.utils.pairwise(path):
        if multigraph:
            cost += min([v[weight] for v in G[node][nbr].values()])
        else:
            cost += G[node][nbr][weight]
    return cost


class Bagg:

    e = {"A":1, "B":10, "C":100, "D":1000}
    home = {"A":3, "B":5, "C":7, "D":9}
    
    def __init__(self,t,x,y):
        self.t = t
        self.x = x
        self.y = y

    def findmoves(self, otherbagg, G):

        stoplist = []

        if (self.x == self.home[self.t]):
            # if we are home, and in the bottom, stop moving
            if self.y==3:
                return None

            # if we are home, and not in the bottom, but the bottom thing is the correct one, stop moving
            if self.y==2:
                X = list(filter(lambda x:x is not self and x.t==self.t,otherbagg))
                if X[0].y==3 and X[0].x==self.home[self.t]:
                    return None
        
        
        # list of _potential_ moves
        P = set(G.nodes())
        X = list(filter(lambda x:x is not self, otherbagg))

        for i in X:
            P.remove(str(i.x)+","+str(i.y))

        # this is the list of all unoccupied spaces in the graph
        # filter it for what we actually are able to do

        # don't move to the first block in the burrow if the burrow is empty
        for i in [3,5,7,9]:
            if str(i)+",3" in P:
                P.discard(str(i)+",2")

        # don't move to a burrow if we are not supposed to be in that burrow
        for i in self.home:
            if i!=self.t:
                P.discard(str(self.home[i])+",2")
                P.discard(str(self.home[i])+",3")

        # don't move to a burrow if the burrow contains a bagg of another kind
        # that bagg has to move outside first
        
        for i in [3,5,7,9]:
            if filter(lambda x: x.x==i and x.y==3 and x.t != self.t, otherbagg):
                P.discard(str(i)+",2")
                P.discard(str(i)+",3")

        # do not move in the corridor, if we already are in the corridor
        if self.y==1:
            for i in [1,2,4,6,8,10,11]:
                P.discard(str(i)+",1")

        # find all possible paths from where we are to unoccupied spaces
        V=[]
        for i in P:
            V.append( nx.shortest_path(G,str(self.x)+","+str(self.y),i,weight="weight"))

        # then remove paths that collide with occupied spaces

        for i in list(X): # these are the occupied spaces
            for t in range(len(V)-1,-1,-1):
                if str(i.x)+","+str(i.y) in V[t] or len(V[t])==1:
                    V.pop(t)
        
                    
        if len(V)>0:
            return (path_weight(G,V[0],"weight")*self.e[self.t],V[0])
        else:
            return None

    def __repr__(self):
        return "["+self.t+":"+str(self.x)+","+str(self.y)+"]"
            
bagg = []
        
G = nx.Graph()

# corridor
G.add_edge("1,1","2,1",weight=1)
G.add_edge("2,1","4,1",weight=2)
G.add_edge("4,1","6,1",weight=2)
G.add_edge("6,1","8,1",weight=2)
G.add_edge("8,1","10,1",weight=2)
G.add_edge("10,1","11,1",weight=1)

# burrows

G.add_edge("2,1","3,2",weight=2)
G.add_edge("4,1","3,2",weight=2)
G.add_edge("3,2","3,3",weight=1)

G.add_edge("4,1","5,2",weight=2)
G.add_edge("6,1","5,2",weight=2)
G.add_edge("5,2","5,3",weight=1)

G.add_edge("6,1","7,2",weight=2)
G.add_edge("8,1","7,2",weight=2)
G.add_edge("7,2","7,3",weight=1)

G.add_edge("8,1","9,2",weight=2)
G.add_edge("10,1","9,2",weight=2)
G.add_edge("9,2","9,3",weight=1)

#nx.draw(G,  with_labels=True)
#plt.savefig("maze.png")

for y in range(len(plan)):
    s=""
    for x in range(len(plan[0])):
        
        if plan[y][x] in "ABCD":
            bagg.append(Bagg(plan[y][x],x,y))
            s+="."
        else:
            s+=plan[y][x]
    plan[y]=s
    
def pr(rec, board, bagg):

    print("-- "+str(rec)+" --")
    for y in range(len(board)):
        s=""
        for x in range(len(board[0])):
            for b in bagg:
                if b.x==x and b.y==y:
                    s+=b.t
                    break
            if len(s)<=x:
                s+=board[y][x]

        print(s)
    print("------")
            
def movebagg(bagg, G, board, rec=0):

    pr(rec, board,bagg)
    
    x = dict()
    mc=None
    vc=None
    for i in range(len(bagg)):
        x[i] = bagg[i].findmoves(bagg, G)
        if x[i]:
            print("Moving ",bagg[i],"from",x[i][1][0],"to",x[i][1][-1])
            b = deepcopy(bagg)
            t = (x[i][1])[-1].split(",")

            nx = int(t[0])
            ny = int(t[1])
            b[i].x=nx
            b[i].y=ny
            
            return min(sys.maxsize, x[i][0] + movebagg(b,G,plan, rec+1))
            
    return sys.maxsize
    
    
    
movebagg(bagg,G,plan)
            


