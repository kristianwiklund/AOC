import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

with open ("input.txt") as fd:

    for  line in fd:
        x = line.split(" ")
        before = x[1]
        after = x[7]
        G.add_edge(before, after)

nx.draw(G,  with_labels=True)
plt.savefig("maze.png")
print("".join(list(nx.lexicographical_topological_sort(G))))
