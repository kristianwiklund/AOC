#!/usr/bin/python3

import networkx as nx
from copy import deepcopy
import sys
import random
import multiprocessing as mp

print (mp.cpu_count(),"processors")
#themin = sys.maxsize
tries=0
cache = dict()

#import matplotlib.pyplot as plt

#23100 too high
#18386 too high

planA = [
    "#############",
    "#...........#",
    "###C#C#A#B###",
    "###D#D#B#A###",
    "#############"]


plan12521 = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "###A#D#C#A###",
    "#############"]

plan44169 = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "###D#C#B#A###",
    "###D#B#A#C###",    
    "###A#D#C#A###",
    "#############"]

plant = [
    "#############",
    "#CC.......DD#",
    "###.#.#A#B###",
    "###.#.#B#A###",
    "#############"]




planB = [
    "#############",
    "#...........#",
    "###C#C#A#B###",
    "###D#C#B#A###",
    "###D#B#A#C###",
    "###D#D#B#A###",
    "#############"]

plantBt = [
    "#############",
    "#AA...B.B.BD#",
    "###B#.#.#.###",
    "###D#.#C#.###",
    "###D#.#C#C###",
    "###A#D#C#A###",
    "#############"]



plan = plantBt



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

    def __lt__(self, other):

        if self.t < other.t:
            return self.t<other.t

        if self.y < other.y:
            return self.y < other.y

        return self.x < other.x

        
    
    def __init__(self,t,x,y):
        self.t = t
        self.x = x
        self.y = y

    def findmoves(self, otherbagg, G):

        stoplist = []


        if self.t=="NONE":
            print("checking",self,"to see if we are at home or not")
                  
        if (self.x == self.home[self.t]):
            # if we are home, and in the bottom, stop moving
            if self.y==len(plan)-2:
                return None

            # if we are home, and not in the bottom, and the rest of the things are the correct ones, stop moving
            if self.y>=2: # check all levels
                if (self.t=="NONE"):
                    print("we are deeper than the corridor, check if we are good")
                    
                X = sorted(list(filter(lambda x:x is not self and x.t==self.t and x.x==self.home[self.t], otherbagg)), key=lambda b:b.y)
                l = len(plan)-4
                if (self.t=="NONE"):
                    print("bagg in home for",self,"of type",self.t," are :",X)

                # if all items in the list are home, and stacked starting from the bottom of the possible burrow, we are good

                bcnt=0
                #print (range(l,0,-1))
                GOGG=[str(x.x)+","+str(x.y) for x in X]
                for ll in range(len(plan)-2,0,-1):
                    if self.t=="NONE":
                        print ("checking position",str(self.home[self.t])+","+str(ll),"in",GOGG)
                        
                    if str(self.home[self.t])+","+str(ll) in GOGG:
                        if self.t=="NONE":
                            print ("Found a lower bagg - good")
                        bcnt+=1
                    else:
                        break
                    
                if bcnt==len(X) and len(X)!=0:
                    #print ("bagg",self,"is at home due to",GOGG)
                    return None
                            
                        
                # this is borked
                # if len(X) == l:
                #     return None
                # if l>2:
                #     if len(X) == 2:
                #         if X[0].y==4 and X[1]==5:
                #             return None
                #         elif len(X) == 3:
                #             if X[0].y==3 and X[1]==4 and X[2]==5:
                #                 return None
                            
        if self.t=="NONE":
            print("done checking if we are at home or not (we were not at home)")
                  
        # list of _potential_ moves
        P = set(G.nodes())
        X = list(filter(lambda x:x is not self, otherbagg))
        
        for i in X:
            P.remove(str(i.x)+","+str(i.y))

        if self.t=="NONE":
            print(P)

        # this is the list of all unoccupied spaces in the graph
        # filter it for what we actually are able to do



            # don't move to a burrow if the burrow contains a bagg of another kind
        # that bagg has to move outside first
        # we are not allowed to move to a burrow if there is a bagg of another type in it
        # fix this for part 2
        for i in [3,5,7,9]:
            for t in filter(lambda x: x.x==i and x.y>2 and x.t != self.t, otherbagg):
                P.discard(str(t.x)+",2")
                P.discard(str(t.x)+",3")
                P.discard(str(t.x)+",4")
                P.discard(str(t.x)+",5")
                if self.t=="NONE":
                    print("occ",t,P)

            
        # move to the lowest block in a burrow if we are allowed to move to a burrow
        
        for i in [3,5,7,9]:
            if str(i)+",3" in P:
                P.discard(str(i)+",2")
            if len(plan)>5:
                if str(i)+",4" in P:
                    P.discard(str(i)+",2")
                    P.discard(str(i)+",3")
                if str(i)+",5" in P:
                    P.discard(str(i)+",2")
                    P.discard(str(i)+",3")
                    P.discard(str(i)+",4")

        # don't move to a burrow if we are not supposed to be in that burrow
        for i in self.home:
            if i!=self.t:
                P.discard(str(self.home[i])+",2")
                P.discard(str(self.home[i])+",3")
                P.discard(str(self.home[i])+",4")
                P.discard(str(self.home[i])+",5")
                    

        if self.t=="NONE":
            print(P)
            
        if self.t=="NONE":
            print("wrong homes !=",self.home[self.t],"removed",P)
                            

        if self.t=="NONE":
            print("removed occupied burrows",P)
                

        # do not move in the corridor, if we already are in the corridor
        if self.y==1:
            for i in range(12):
                P.discard(str(i)+",1")

        if self.t=="NONE":
            print(P)
                            
        # find all possible paths from where we are to unoccupied spaces
        V=[]
        for i in P:
            t = nx.shortest_path(G,str(self.x)+","+str(self.y),i,weight="weight")
            V.append((path_weight(G,t,"weight")*self.e[self.t], nx.shortest_path(G,str(self.x)+","+str(self.y),i,weight="weight")))

        # then remove paths that collide with occupied spaces

        for i in list(X): # these are the occupied spaces
            for t in range(len(V)-1,-1,-1):
                if str(i.x)+","+str(i.y) in V[t][1] or len(V[t][1])==1:
                    V.pop(t)

        #print (V)
        # if our home is at the end of a possible path, go for it and nothing else
        for x in V:
            if str(self.home[self.t])+",2" in x[1] or str(self.home[self.t])+",3" in x[1]:
                if self.t=="NONE":
                    print("going home", [x])
                return [x]
                    
        if len(V)>0:
            if self.t=="NONE":
                print("final possible remaining moves", V)
                #            random.shuffle(V)
            V=sorted(V,reverse=True,key=lambda x:x[0])
            return (V)
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

if(len(plan)==7):
    G.add_edge("3,3","3,4",weight=1)
    G.add_edge("3,4","3,5",weight=1)

    G.add_edge("5,3","5,4",weight=1)
    G.add_edge("5,4","5,5",weight=1)

    G.add_edge("7,3","7,4",weight=1)
    G.add_edge("7,4","7,5",weight=1)

    G.add_edge("9,3","9,4",weight=1)
    G.add_edge("9,4","9,5",weight=1)


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
    
def pr(rec, board, bagg, cost):

    bs = []
    for y in range(len(board)):
        s=""
        for x in range(len(board[0])):
            for b in bagg:
                if b.x==x and b.y==y:
                    s+=b.t
                    break
            if len(s)<=x:
                s+=board[y][x]

        bs.append(s)
    return bs

def moveprint(p):

    #print (p)
    if p==[]:
        return

    for i in range(max(0,len(p)-17),len(p)):
        print (str(i).ljust(len(p[0][0])+1," "),end="")
    print("")
    for i in range(len(p[0])):
        for j in range(max(0,len(p)-17),len(p)):
            print(p[j][i]+" ",end="")
        print("")


def descend(bagg, G, board, x, mv, i, rec=0, cost=0,path=[],themin=sys.maxsize,queue=None):

    #print ("moving bagg",i)
    #moveprint(path)
    
    for z in x[i]:
        if (cost+z[0])<mv:
            
            if bagg[i].t=="NONE":
                print ("x=",x,"x[i]=",x[i])            
                print("Moving bagg",i,bagg[i],"from",z[1][0],"to",z[1][-1])
                
            b = deepcopy(bagg)                
            t = (z[1])[-1].split(",")
                
            nx = int(t[0])
            ny = int(t[1])
            b[i].x=nx
            b[i].y=ny
            
            #proppen = "".join(pr(rec, board, b, cost))
            
            v = movebagg(b,G,plan, rec+1, cost+z[0],path+[pr(rec, board, b, cost)],mv,queue=queue)    
            mv = min(v,mv)
            #print(proppen,v)                    
            #cache[proppen] = v
            
            #print(b.__repr__())

    return mv

results=[]

def movebagg(bagg, G, board, rec=0, cost=0,path=[],themin=sys.maxsize,queue=None):

    global tries
    global cache
    
    tries+=1
    
#    if cost>themin:
#        return themin+1
    #pr(rec, board,bagg, cost)

    #proppen = "".join(pr(rec, board, bagg, cost))
    #if proppen in cache:
    #    return cache[proppen]
    
    x = dict()

    c=0
    for i in bagg:
        if i.x==i.home[i.t] and i.y>1:
            c+=1
    #print("home: ",c)
    if c==len(bagg):
        if themin is None or cost < themin:
            print ("all home",cost)
            #pr(rec, board, bagg, cost)
            moveprint(path)
            themin = cost
            if queue is not None:
                #print("sending result to queue")
                queue.put(themin)
        return cost

    if rec==0:
        m = mp.Manager()
        queue=m.Queue()
    

 

    if rec==0:
        pool = mp.Pool(max(len(bagg),mp.cpu_count()))
        print("Created pool with",max(len(bagg),mp.cpu_count()),"threads")
        
    mv=themin                       
    koko=0       
    for i in range(len(bagg)):
        x[i] = bagg[i].findmoves(bagg, G)

        if x[i]:
            koko+=len(x[i])
            if rec==0:
                res = pool.apply_async(descend, (bagg, G, board,x,mv,i),{"rec":rec, "cost":cost,"path":path,"themin":themin,"queue":queue})
                results.append(res)
            else:
                mv = descend(bagg, G, board,x,mv,i,rec, cost,path,themin,queue)
#        else:
#            print("found no moves for bagg",bagg[i])
#            moveprint(path)
    if koko==0:
        #print("deadlock",cost)
        if queue is not None:
            #print("sending result to queue")
            queue.put(sys.maxsize)
        return sys.maxsize

    if rec==0:
        mscnt=0
        while True:
            try:
                v = [res.get(timeout=1) for res in results]
                print (v)
                return (min(v))
            except:
                try:
                    while True:
                        w = queue.get(False)
                        if w != sys.maxsize:
                            print ("got potential minvalue",w,"old minvalue is",mv)
                        else:
                            mscnt+=1
                            if mscnt%1000==0:
                                print(mscnt,"dead ends")
                        if w < mv:
                            print ("new minvalue",w)
                            mv = w
                            break
                except: # queue empty exception
                    pass

    #cache[proppen]=mv        
    return mv    
    
themin=movebagg(bagg,G,plan)
    
print("Answer 1:",themin)           

