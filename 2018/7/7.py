import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

#with open ("shortinput.txt") as fd:
with open ("input.txt") as fd:

    for  line in fd:
        x = line.split(" ")
        before = x[1]
        after = x[7]
        G.add_edge(before, after, weight=ord(after)-64)

nx.draw(G,  with_labels=True)
plt.savefig("maze.png")
helalistan=list(nx.lexicographical_topological_sort(G))
print("7A :"+"".join(helalistan))

# ---------------------

#ACHOQRXSEKUGMYIWDZLNBFTJVP

time=0
workers = [0,0,0,0,0,0,0,0,0,0]
doing = [None, None,None,None,None,None,None,None,None]


while list(G.nodes()) != []:

    for i in range(0,6):

        if workers[i] <= 0:
            # finish what was done, then pull something
            if doing[i]:
#                print ("Worker "+str(i)+" is done with "+doing[i])
                G.remove_node(doing[i])
                doing[i] = None
                
            for j in helalistan:
                #print ("Trying to pull node "+j)
                if not j in doing:
                    #print ("Nobody is working on "+j)
                    if G.has_node(j) and list(G.predecessors(j)) == []:
 #                       print ("Worker "+str(i)+" pulls node "+j)
                        doing[i] = j
                        workers[i] = 60+ord(j)-65
                        break
            
        else:
            workers[i] = workers[i] - 1

  #  print("Tick: "+str(time) + " working on "+str(doing))
    time=time+1


print("Total time for assembly: "+str(time-1))

    
    
    
    
    
