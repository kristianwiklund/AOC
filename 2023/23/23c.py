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

arr = readarray("input.short",split="",convert=lambda x:x if x not in "><^v" else ".")
#lines = readlines("input.short")

#print(arr)

start=[x for x in range(len(arr[0])) if arr[0][x]=="."][0]
stop=list(reversed([x for x in range(len(arr[len(arr)-1])) if arr[len(arr)-1][x]=="."]))[0]
print(start,stop)

G=nx.Graph()

for y in range(len(arr)):
    for x in range(len(arr[0])):

        match arr[y][x]:
            case "#":
                continue
            case ">":
                if checkpos(arr, x+dirs[1][0],y+dirs[1][1],lambda x:x!="#",outofbounds=False):
                    G.add_edge((x,y), (x+dirs[1][0],y+dirs[1][1]))
            case "<":
                if checkpos(arr, x+dirs[3][0],y+dirs[3][1],lambda x:x!="#",outofbounds=False):
                    G.add_edge((x,y), (x+dirs[3][0],y+dirs[3][1]))
            case "v":
                if checkpos(arr, x+dirs[2][0],y+dirs[2][1],lambda x:x!="#",outofbounds=False):
                    G.add_edge((x,y), (x+dirs[2][0],y+dirs[2][1]))
            case "^":
                if checkpos(arr, x+dirs[0][0],y+dirs[0][1],lambda x:x!="#",outofbounds=False):
                    G.add_edge((x,y), (x+dirs[0][0],y+dirs[0][1]))
                    print((x,y),"->",(x+dirs[0][0],y+dirs[0][1]))                
            case ".":
                z=checkallpos(arr,x,y,lambda x:x!="#",outofbounds=False)
                ch="^>v<"
                for i in range(4):
                    if z[i]:
                        if (arr[y+dirs[i][1]][x+dirs[i][0]]==ch[i]) or (arr[y+dirs[i][1]][x+dirs[i][0]]=="."):
                            G.add_edge((x,y),(x+dirs[i][0],y+dirs[i][1]),weight=1)

#pos = nx.spring_layout(G)
#nx.draw(G,pos=pos)
#plt.savefig("maze_nwx.png")

from simplifygraph import simplifygraph

R=simplifygraph(G,lambda x:len(G.edges(x))==2)

v=list(nx.all_simple_paths(R,(start,0),(stop,len(arr)-1)))
#print(v)

l = [nx.path_weight(R,x,"weight") for x in v]
l= sorted(l,key=lambda x:-x)
v=sorted(list(v),key=lambda x:-nx.path_weight(R,x,"weight"))

printpath(v[0],background=arr)
print(l[0]-1)
