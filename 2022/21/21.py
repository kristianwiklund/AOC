import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

def readG():
    arr = readarray("input.txt",split=":",convert=lambda x:x.strip())

    G = nx.DiGraph()
    
    for i in arr:
        try:
            v = int(i[1])
            G.add_node(i[0],value=v)
        except:
            G.add_node(i[0],expr=i[1])
            G.add_edge(i[0],i[1].split(" ")[0])
            G.add_edge(i[0],i[1].split(" ")[2])

    return G

def calc(G, node):
#    print (node,G.nodes[node])
    
    if "value" in G.nodes[node]:
        return G.nodes[node]["value"]

    e = G.nodes[node]["expr"]
    for i in G.successors(node):
        e=e.replace(i,str(calc(G,i)))
#    print(node,e)
    v = eval(e)
    G.nodes[node]["value"]=v
    return v

G=readG()
print("Part 1:",int(calc(G,"root")))

#--

        
def bal(G, node):
    #print (node,G.nodes[node])
    
    if "value" in G.nodes[node]:
        return G.nodes[node]["value"]

    e = G.nodes[node]["expr"]

    for i in G.successors(node):
        e=e.replace(i,"("+str(bal(G,i))+")")
    try:
        v = eval(e)
    except:
        v=e
    
#    print(node,e,v)
#    v = eval(e)
    G.nodes[node]["value"]=v
    return v

G=readG()
G.nodes["humn"]["expr"]="HUMN"
del G.nodes["humn"]["value"]
G.nodes["root"]["expr"]=G.nodes["root"]["expr"].replace("+","=")
print(bal(G,"root")) 

v=list()
for i in G.successors("root"):
     v.append(G.nodes[i]["value"])

pprint (v)

ex = str(v[0])+"-"+str(v[1])

from sympy import *

HUMN=symbols("HUMN")
print("Part 2:",solve(eval(ex),HUMN))
