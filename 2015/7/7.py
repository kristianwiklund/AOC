import networkx as nx
import matplotlib.pyplot as plt
import sys
from pprint import pprint
G = nx.DiGraph()

with open("input.txt") as fd:

    for line in fd:
        line = line.rstrip()
        # format
        # expr -> target

        [expr, target] = line.split(" -> ")

        # expr can be either binary op, unary op (NOT), a variable, or a number

        sp = expr.split(" ")
        c = len(sp)

        if c == 3:
            G.add_node(target, op=sp[1])
            G.add_edge(sp[0],target)
            G.add_edge(sp[2],target)
                        
        elif c == 2:
            G.add_node(target, op=sp[0])
            G.add_edge(sp[1],target)
        else:
            G.add_node(target, op="NIL")
            G.add_edge(sp[0], target)


#pprint(G.nodes(data=True))

nx.draw(G, with_labels=True)
plt.savefig("maze.png")

#----
def calcvalue(G, node):

    # first, check if we already have a value for the node, if so, return it and do nothing

    values = nx.get_node_attributes(G, "value")
    if node in values:
        return values[node]

    # then, check if this is an integer node
    
    pred = list(G.predecessors(node))
    if pred == []:
        if node.isdigit():
            G.add_node(node, value = int(node))
            return int(node)
        else:
            raise ValueError

    ops = nx.get_node_attributes(G, "op")
    op = ops[node]


 #   print ("Node "+node+" have predecessors "+str(pred))
    cv = []
    for i in pred:
        cv.append(calcvalue(G, i))

#    print (cv)

    if op == "NOT":
        value = ~cv[0]
    elif op == "RSHIFT":
        value = cv[0] >> cv[1]
    elif op == "LSHIFT":
        value = cv[0] << cv[1]
    elif op == "AND":
        value = cv[0] & cv[1]
    elif op == "OR":
        value = cv[0] |  cv[1]
    else:
        value = cv[0]

    G.add_node(node, value = value)
        
    return value
    
    
#----

outputs = [x for x in G.nodes() if list( G.successors(x)) == [] ]
print(outputs)

for i in outputs:
    print(i+"= "+str(calcvalue(G, i)))

