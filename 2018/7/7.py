import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

with open ("shortinput.txt") as fd:

    for  line in fd:
        x = line.split(" ")
        before = x[1]
        after = x[7]
        G.add_edge(before, after)

nx.draw(G,  with_labels=True)
plt.savefig("maze.png")
print("7A :"+"".join(list(nx.lexicographical_topological_sort(G))))

# ---------------------

#ACHOQRXSEKUGMYIWDZLNBFTJVP

def canwe (G, node, done):

    # try pulling the current node
    # to be able to do that, all predecessors to the node must be in the "done" set

    pre = G.predecessors(node)

    if set(pre) > set(done):
        print("cannot pull "+current+" due to preconditions")
        return False

    # do the work

    return True


def work(G):

    for i in G:


