import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache
#from shapely.geometry.polygon import Polygon
#from shapely import contains

arr = readarray("input",split=" ",convert=lambda x:x.strip(":"))
#lines = readlines("input.short")
#print(arr)

G=nx.DiGraph()

for l in arr:
    a=l[0]
    [G.add_edge(a,x) for x in l[1:]]

try:
    print("part 1:",len(list(nx.all_simple_paths(G,"you","out"))))
except:
    pass

# simple nx solution does not work for part 2 (it kills itself)

#nx.draw(G)
#solution idea: find all paths from svr to fft, then fft to dec, then dac to out
#start pruning the graph


# there are no paths from dac to fft in the graph.
it=nx.all_simple_paths(G,"dac", "out")
c=sum(1 for dummy in it)
print(c,"...")


pd = nx.ancestors(G,"dac")
ds = nx.descendants(G,"fft")
print(pd,ds)

v = pd.intersection(ds)
v.add("dac")
v.add("fft")

Y = nx.subgraph(G,list(v))
print(Y)

it=nx.all_simple_paths(Y,"fft", "dac")
b=sum(1 for dummy in it)
print(b,"...")


pd = nx.ancestors(G,"fft")
ds = nx.descendants(G,"svr")
print(pd,ds)

v = pd.intersection(ds)
v.add("svr")
v.add("fft")

Y = nx.subgraph(G,list(v))


it=nx.all_simple_paths(Y,"svr", "fft")
a=sum(1 for dummy in it)
print(a,"...")



s=a*b*c
print("part 2:",s)

assert(s>86719961286)

