from curses import wrapper
import curses
import time
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

# 6483 too high
# 867 too low
def readmaze(fn):

    maze = dict()
    x = 0
    y = 0
    
    with open(fn,"r") as fd:

        for line in fd:
            x=0
            for i in line:

                if i == "." or i.isalpha() or i == "@":

                    maze[(x,y)] = i
                x=x+1

            y=y+1
        

    return (maze)

#----------------------------------------------

def setup():
    global stdscr
    
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    
    
#----------------------------------------------



def printmaze(maze):
    if not stdscr:
        return
    
    for (x,y) in maze.keys():
        stdscr.addstr(y+2,x+1,str(maze[x,y]))
    pass

#----------------------------------------------

def n(x,y):
    return (x,y-1)

def e(x,y):
    return (x+1,y)

def s(x,y):
    return (x,y+1)

def w(x,y):
    return (x-1,y)


# check that the location has not been visited before and that the maze is clear
def uno(maze, locs, key):
    if key in locs.keys():
        return False

    if key in maze.keys():
        if maze[key]==".":
            return True

    return False

# if the position corresponds to an isalpha, add it to the global list of thingies
def checknadd(maze,pos, depth, start):
    global G
    if pos in maze.keys():
        if (len(maze[pos])>1 or maze[pos] == "@") and (maze[pos] != start):
           G.add_edge(start, maze[pos], weight=depth) 

# breadth first helper for the maze router
def bfs(maze, locs, depth, start):
    
    newDict = { key:value for (key,value) in locs.items() if value == depth}
    if len(newDict)==0:
        with open('config.dictionary', 'w') as config_dictionary_file:
            config_dictionary_file.write(str(locs))

        return
    
    #print(newDict)

    # we have a number of locations to start expanding from.
    # we will only expand until we reach a position that is not "." - which is either the start or a letter
    # check the positions around the location

    for (x,y) in newDict.keys():

        if stdscr:
            stdscr.addstr(1,0, "Probing ("+str(x)+","+str(y)+") - depth "+str(depth)+" - "+str(len(newDict)) + " locs")

            #stdscr.addstr(y+2,x+1,"X")
            stdscr.addstr(2,20,str(n(x,y))+" "+str(e(x,y))+" "+str(s(x,y))+" "+str(w(x,y)))
        
        if uno(maze,locs,n(x,y)):
            locs[n(x,y)]=depth+1
        else:
            checknadd(maze,n(x,y),depth+1,start)
            
        if uno(maze,locs,e(x,y)):
            locs[e(x,y)]=depth+1
        else:
            checknadd(maze,e(x,y),depth+1,start)
                
        if uno(maze,locs,w(x,y)):
            locs[w(x,y)]=depth+1
        else:
            checknadd(maze,w(x,y),depth+1,start)
            
        if uno(maze,locs,s(x,y)):
            locs[s(x,y)]=depth+1
        else:
            checknadd(maze,s(x,y),depth+1,start)

    if stdscr:
        stdscr.refresh()

    #time.sleep(3)
    bfs(maze, locs, depth+1, start)
    

def findroutes(maze, where):
    global G

    print(where)
    (start,(x,y)) = where
    start = str(start)
    print (start)
    # find the distance from symbol start to all other symbols
    # through a breadth first search

    if start not in maze.values():
        print(str(start)+" not found")
        return
    
    (x,y) = (list(maze.keys())[list(maze.values()).index(start)])
    
    if stdscr:
        stdscr.addstr(0,0, "Starting search at "+start+"=("+str(x)+","+str(y)+")")
        stdscr.refresh()

    locs = dict() # empty tracker of locations
    locs[(x,y)]=0 # seed with starting point -     EnQueue( m.StartNode )


    bfs(maze, locs, 0, start)
    #    time.sleep(10)
    #time.sleep(1)

#----------------------------------------------

def nearbydot(maze, where):

    (x,y)=where
    
    if n(x,y) in maze:
        if maze[n(x,y)]==".":
            return n(x,y)
    if e(x,y) in maze:
        if maze[e(x,y)]==".":
            return e(x,y)
    if s(x,y) in maze:
        if maze[s(x,y)]==".":
            return s(x,y)
    if w(x,y) in maze:
        if maze[w(x,y)]==".":
            return w(x,y)
    return None


def nearbyalpha(maze, where):

    (x,y)=where
    
    if n(x,y) in maze:
        if maze[n(x,y)].isupper():
            return n(x,y)
    if e(x,y) in maze:
        if maze[e(x,y)].isupper():
            return e(x,y)
    if s(x,y) in maze:
        if maze[s(x,y)].isupper():
            return s(x,y)
    if w(x,y) in maze:
        if maze[w(x,y)].isupper():
            return w(x,y)
    return None


def exitfinder(maze):
    #what we search for:
    # isupper() next to an empty space and also next to another isupper()
    exits=[]
    #print(maze)
    helalistan=[]
    
    for key in maze.keys():
        value = maze[key]

        if value.isupper():
            dot =  nearbydot(maze, key)
            if dot:
                let = nearbyalpha(maze, key)
                if let:
                    # found it!
                    name=value+maze[let]

                    if name in helalistan:
                        name = "".join(reversed(name))
                                       
                    exits.append((name,key))
                    maze[dot] = name
                    maze[key] = " "
                    maze[let] = " "
                    helalistan.append(name)
    return(exits)
            
#----------------------------------------------

# AA=start
# ZZ= end

def main(ko):
    global stdscr
    global G
    stdscr=ko
    G = nx.Graph()
    
    maze = readmaze("input.txt")
    printmaze(maze)
    if stdscr:
        stdscr.refresh()

    # function to properly identify the two-literal exits/teleports
    exits=exitfinder(maze)
    print(exits)
    print(maze)

    # we have the maze. Now extract the nodes and edges. Put them
    # in a weighted graph

    # the tricky part here is to explore _all_ relevant paths
    # let's try the dumb way first

    for i in exits:
        printmaze(maze)
        if stdscr:
            stdscr.refresh()
        findroutes(maze, i)

    # G now contains all (we hope :-)) paths between X and Y
    # now add one weight edges for the exits

    for i in exits:
        (name,X) = i
        if name != "".join(reversed(name)): # don't join the exit to the exit
            G.add_edge(name, "".join(reversed(name)), weight=1)
    
def popaway(GG, what):

    GGG = GG
    import copy
    GGG = copy.deepcopy(GG)
    GGG.remove_node(what)
    
    # remove what from GG, keep connections to neighbors

    nb = GG[what]

    # connect all in nb to all in nb with the sum of a and b

    l = list(nb.keys())

    
    i = l.pop(0)
    while(len(l)):

        for j in l:
            #totweight=nx.subgraph(GG,[i,what,j]).size(weight="weight")

            #print (totweight)
            if not GGG.has_edge(i,j):
                totweight=nb[i]["weight"]+nb[j]["weight"]            
                GGG.add_edge(i,j,weight=totweight)

                #print("edge "+i+" to "+j)
                #print("PRE :"+str(nx.shortest_path(GG,i,j))+" "+str(nx.subgraph(GG,nx.shortest_path(GG,i,j)).size(weight="weight")))
                #print("POST:"+str(nx.shortest_path(GGG,i,j))+" "+str(nx.subgraph(GGG,nx.shortest_path(GGG,i,j)).size(weight="weight")))

                #time.sleep(1)
            
        i = l.pop(0)


    wgh=0


    #    print(GG.edges(data=True))
    return (GGG)
    

# this function starts at G, explores the neighbors of G, and finds the cheapest path out
def opt(GG, whereami, distance,visited,havekeys, depth,best):
    global cache
    global cnt
#    print(whereami,end="")
#    print("Arriving at "+whereami+"\n")
    neighbors=GG[whereami]

    #if distance>=best:
    #    return(distance,whereami)
    
    if not neighbors:
#        print (str(cnt)+": all visited \n"+str(best))
        return(0,whereami)

    if not whereami:
        return(0, "")

    bestdist=66666666666
    bestpath=[]

    b=GG.nodes()
    alln="".join(b)

    
    if ((whereami+alln) in cache.keys()):
        #cnt=cnt+1
        #        
       # if (cnt % 10000) == 0:
#            print (str(cnt)+" "+str(depth))
#            print ("cache hit: "+str(cnt)+" "+whereami+alln+" "+str(cache[whereami+alln])+"\n")
        #    print ("Standing at "+whereami+" rem: "+alln + "dist "+str(distance)+"\n")
        return cache[whereami+alln]

    
    import copy 

    GGG = popaway(GG, whereami)

    





    #cnt=cnt+1


    #keylist=[a for (a,b) in sorted(GG[whereami].items(), key=lambda edge: edge[1]['weight'])]
    #    print(keylist)

    keylist=GG.neighbors(whereami)
    for i in keylist:

        
        # don't go in circles (yet) - this doesnt work, we need to collapse the nodes...



        # if we don't have the key, we don't go there
        if i.isupper():
            if not (i.lower() in havekeys):
                continue
            else:
                pass


        if i.islower(): # key
            temphavekeys=havekeys+i
            if GGG.has_node(i.upper()):
                PGG = copy.deepcopy(GGG)
                PGG = popaway(PGG, i.upper())
                #print ("Unlocked door by removing "+i.upper()) # should possibly be replaced by a node removal...
            else:
                temphavekeys=havekeys
                PGG = GGG
        else:
            temphavekeys=havekeys
            PGG = GGG
        
        # remove the node we are at, and only keep the nodes that we are not at

            
        (newdist, newpath) = opt(PGG, i, distance+neighbors[i]["weight"], visited+whereami,temphavekeys,depth+1,min(best,bestdist))
        if (newdist+neighbors[i]["weight"]) < bestdist:
            bestpath = whereami+newpath
            bestdist = newdist+neighbors[i]["weight"]

    if distance==0:
        print (str(bestpath)+" = "+str(bestdist))
        totweight=nx.subgraph(GG,bestpath).size(weight="weight")
            
    cache[whereami+alln] = (bestdist, bestpath)
    return (bestdist, bestpath)
            
    
    
main(None)

#wrapper(main)
print(G.edges(data=True))
#print(G.nodes)
nx.draw(G,  with_labels=True)
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=labels)
plt.savefig("maze.png")
cnt=0
cache=dict()

# to here, it is the same as for exercise 18, basic

print("Path  : "+str(nx.shortest_path(G,"AA","ZZ",weight="weight")))
print("Length: "+str(nx.shortest_path_length(G,"AA","ZZ",weight="weight")))


#pprint(opt(G, "@", 0, "","",0,666666666666))



