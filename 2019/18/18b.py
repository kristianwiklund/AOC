from curses import wrapper
import curses
import time
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

#redesign. We have four graphs. Extract those.
# then call the subgraph thing thingy when we go for a new step
# breadth first -> graphs -> breadth first

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

    if stdscr:
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
        if (maze[pos].isalpha() or maze[pos] == "@") and (maze[pos] != start):
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
            if stdscr:
                stdscr.addstr(2,0, "NF ")
            checknadd(maze,n(x,y),depth+1,start)
            
        if uno(maze,locs,e(x,y)):
            locs[e(x,y)]=depth+1
        else:
            if stdscr:
                stdscr.addstr(2,4, "EF ")
            checknadd(maze,e(x,y),depth+1,start)
                
        if uno(maze,locs,w(x,y)):
            locs[w(x,y)]=depth+1
        else:
            if stdscr:
                stdscr.addstr(2,8, "WF ")
            checknadd(maze,w(x,y),depth+1,start)
            
        if uno(maze,locs,s(x,y)):
            locs[s(x,y)]=depth+1
        else:
            if stdscr:
                stdscr.addstr(2,12, "SF ")
            checknadd(maze,s(x,y),depth+1,start)

    if stdscr:
        stdscr.refresh()

    #time.sleep(3)
    bfs(maze, locs, depth+1, start)
    

def findroutes(maze, start):
    global G
    
    # find the distance from symbol start to all other symbols
    # through a breadth first search

    if start not in maze.values():
        return
    
    (x,y) = (list(maze.keys())[list(maze.values()).index(start)])


    if stdscr:
        stdscr.addstr(0,0, "Starting search at "+start+"=("+str(x)+","+str(y)+")")
        stdscr.refresh()

    locs = dict() # empty tracker of locations
    locs[(x,y)]=0 # seed with starting point -     EnQueue( m.StartNode )


    bfs(maze, locs, 0, start)
    #    time.sleep(10)
    #    time.sleep(1)

    
#----------------------------------------------



def main(ko):
    global stdscr
    global G
    stdscr=ko
    G = nx.Graph()
    
    #maze = readmaze("smallinput4.txt")
    maze = readmaze("input2.txt")
    printmaze(maze)
    if stdscr:
        stdscr.refresh()

    # we have the maze. Now extract the nodes and edges. Put them
    # in a weighted graph

    # find the four starting points first
    spoints=list()
    cnt=0
    for pos in maze.keys():
        if maze[pos]=="@":
            spoints.append(pos)
            maze[pos]="@"+str(cnt)
            (x,y)=pos
            if stdscr:
                stdscr.addstr(y+2,x+1,str(cnt))
                stdscr.refresh()
            cnt=cnt+1
            
    time.sleep(10)
    

    # the tricky part here is to explore _all_ relevant paths
    # let's try the dumb way first

    for i in range(0,4):
        findroutes(maze, "@"+str(i))
        #time.sleep(5)
    
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        printmaze(maze)
        if stdscr:
            stdscr.refresh()
        findroutes(maze, i)



    return maze
    # G now contains all (we hope :-)) paths between X and Y

def popaway(GG, what):


    if not GG.has_node(what):
        return GG
    
    import copy
    GG = copy.deepcopy(GG)
    GGG = nx.Graph(GG)

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
    

# find the way out...

def findtheway(graphs, currentnodes):

    global cache
    
    # four graphs. find options

    ngb = [None,None,None,None]

    for i in range(0,4):
        ngb[i]=list(graphs[i].neighbors(currentnodes[i]))
        ngb[i] = list(filter(lambda x: x.islower(), ngb[i]))
        #        print(list(ngb[i]))

    if ngb == [[],[],[],[]]:
        return (0, "")

    flatten = lambda l: [item for sublist in l for item in sublist] # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    fingerprint = "".join(currentnodes)+"".join(flatten(ngb))

    if fingerprint in cache.keys():
        return cache[fingerprint]

    print(str(ngb))
    
    # these are the items that are next in line in each graph that we can move to
    # iterate over those items

    mcost = 666666666666666666
    mpath = []
    
    for i in range(0,4):
        for j in ngb[i]:
            print("trying "+currentnodes[i]+"->"+j)

            tmplist = list(graphs)
            tmplist[i] = popaway(tmplist[i],currentnodes[i])
            tmpcurrent = list(currentnodes)
            tmpcurrent[i] = j

            # here we have popped the lowercase one. We also need to pop any matching UPPERCASE ones
            # (unlocking the doors)

            for x in range(0,4):
                XG = tmplist[x]
                if XG.has_node(j.upper()):
                    tmplist[x] = popaway(tmplist[x], j.upper())
            

            (dist, path) = findtheway(tmplist, tmpcurrent)


            if dist+graphs[i][currentnodes[i]][j]["weight"] < mcost:
                mcost = dist+graphs[i][currentnodes[i]][j]["weight"]
                mpath = currentnodes[i] + path

    cache[fingerprint] = (mcost, mpath)
    return (mcost, mpath)
            
    
    
    
main(None)
#wrapper(main)
import pygraphviz
from networkx.drawing.nx_agraph import write_dot
#print(G.edges(data=True))
#print(G.nodes)

#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=labels)

cnt=0
cache=dict()
write_dot(G, "maze.dot")

nx.draw_spring(G,  with_labels=True)
plt.savefig("maze_nwx.png")

# cut the graph into the four distinct different graphs

graphs = list()
for i in range(0,4):
    graphs.append(nx.subgraph(G,nx.node_connected_component(G,"@"+str(i))))
    

cache = dict()
print(findtheway(graphs,["@0","@1","@2","@3"]))



