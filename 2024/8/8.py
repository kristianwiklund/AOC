import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

t = set("".join([i for i in ["".join(i).replace(".","") for i in arr] if i]))
print (t)

def fan(arr,a):
    p = findinarray(arr,a,all=True)
  #  print(a,p)

    n = []
    
    # for all nodes, compare with all other nodes

    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            # this can result in four antinodes
            # the distance between the antennas need to be at least 1 (meaning 3 manhattan distance)
            d = distance(p[i],p[j]) - 1

            # step
            dx=p[i][0]-p[j][0]
            dy=p[i][1]-p[j][1]

            # there are four cases
            l=[]            
            l.append((p[i][0]+2*dx,p[i][1]+2*dy))
            l.append((p[j][0]+2*dx,p[j][1]+2*dy))
            l.append((p[i][0]-2*dx,p[i][1]-2*dy))
            l.append((p[j][0]-2*dx,p[j][1]-2*dy))
            #print(a,i,j,"--",l)
            l = [v for v in l if distance(p[i],v)==2*distance(p[j],v) or 2*distance(p[i],v)==distance(p[j],v)]
            
            
            # check if these are good
            lll = [i for i in l if checkpos(arr,i[0],i[1],lambda y:y!=a)]
            #print(a,i,j,"--",lll)
            n+=lll
            #break
            #    print("nodes",set(n))
    #pprint(arr)
    return set(n)

s = set()
for x in t:
    print(x)
    ss = fan(arr,x)
    #print(x,ss)
    s|=ss

print(s,len(s))

printpath(s,background=arr)
