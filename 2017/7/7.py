import networkx as nx
import sys
G = nx.DiGraph()

v = dict()
    
def sumsub(G, n):
    s = list()
    m = list()
    for i in G.successors(n):
        t = sumsub(G, i)
        v[i] = t
        s.append(t)

    if len(s)==0:
        return G.nodes[n]["weight"]

    if sum(s)//len(s) == s[0]:
        return sum(s)+G.nodes[n]["weight"]

    #tree = list(G.successors(n))[0]
    #print ("Unbalanced program is",tree,s,", ",end="")
    # find which subtree
    ma = max(s)
    mi = min(s)

    if s.count(ma)==1:
        i = s.index(ma)
        print (i,"is broken")
        w = mi-ma
    else:
        i = s.index(mi)
        print (i,"is broken")
        w = ma-mi
            
    bn = list(G.successors(n))[i]
    print ("Part 2:",s,"subprogram",bn,"with weight",G.nodes[bn]["weight"],"is broken, need to be weight",G.nodes[bn]["weight"]+w)
    sys.exit()
    

with open("input.txt","r") as fd:
    lines = [x.strip() for x in fd.readlines()]

    for line in lines:

        t = line.split(" ")
        G.add_node(t[0])
        G.nodes[t[0]]["weight"]=int(eval(t[1]))
        
        #print(t[0],G.nodes[t[0]])
        if len(t)>2:
            for i in range(3, len(t)):
                G.add_edge(t[0],t[i].strip(","))

    root = list(nx.topological_sort(G))[0]
    print("Answer 1:", root)

    sumsub(G, root)
    #print(v)


    #13363

    
