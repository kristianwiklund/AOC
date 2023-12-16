import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split=";",convert=lambda x:x)
#lines = readlines("input.short")

c=dict()
for l in arr:
    v = l[0].split(" ")[1]
    r = ints(l[0])[0]

    t = [x.strip() for x in l[1].replace("tunnels lead to valves ","").replace("tunnel leads to valve ","").split(",")]
    c[v]=(r,t)

pprint(c)

p = "AA"
t = 1

@cache
def doit(p, t, v, ra,re):
    global c
    if t==30:
#        print (t,": (end) :",v,ra,re,pt)
        return (t, ra, re,v)

    if t>31:
        return (t, ra, 0,v)
    
#    print(t," - standing at",p,"selecting from",c[p][1], "releasing",ra, "released",re,"from",v)





    acc = []


    # it is only fruitful to open if it isn't already open and the flow rate is not zero
    # if so, open, test the paths we have
    if c[p][0]>0 and not p in v:
        
        for i in c[p][1]:
            r = doit(i,t+2,v+","+p+"("+str(t)+")="+str(c[p][0]),ra+c[p][0],re+ra+ra)
            acc.append(r)

    # do not open the valve, then test the paths we have
    for i in c[p][1]:
        r = doit(i,t+1,v,ra,re+ra)
        acc.append(r)
            
#    print(acc)
    acc = sorted(acc, key=lambda x:-x[2])
    return acc[0]
    
print(doit(p,t,"",0,0))

    

