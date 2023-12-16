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

arr = readarray("input.txt",split=";",convert=lambda x:x)
#lines = readlines("input.short")



c=dict()
for l in arr:
    v = l[0].split(" ")[1]
    r = ints(l[0])[0]

    t = [x.strip() for x in l[1].replace("tunnels lead to valves ","").replace("tunnel leads to valve ","").split(",")]
    c[v]=[r,t]

pprint(c)

p = "AA"
t = 0

for l in c:
#    print(c[l])
    c[l][1]=sorted(c[l][1],key=lambda x:-c[x][0])
#    print(c[l])

@cache
def bound(v,t):
    global c
    v = v.split(",")[1:]
    r = 30-t
    n = {x:c[x] for x in c if c[x][0]!=0 and x not in v}
    return sum([n[x][0] for x in n])*r
    
    
@cache
def doit(p, t, v, ra,re):
    global c
    global mx
    
    if t==30:
#        print (t,": (end) :",v,ra,re,pt)
#        print(bound(v,t))
        return (t, ra, re,v)

    if t>31:
        return (t, ra, 0,v)

    # the absolute max we can get is the remaining time times the remaining possible flow rates plus the accumulated ratio right now
    if (bound(v,t)+(30-t)*ra+re)<mx:
#        print (t,ra,0,v,mx,bound(v,t)+ra)
        return (t,ra,0,v,mx,bound(v,t)+ra)

    
#    print(t," - standing at",p,"selecting from",c[p][1], "releasing",ra, "released",re,"from",v)

    acc = [(0,0,0)]


    # it is only fruitful to open if it isn't already open and the flow rate is not zero
    # if so, open, test the paths we have

    if c[p][0]>0 and not p in v and t<=28:        
        for i in c[p][1]:
            # we have released re
            # when we start opening the valve, we have release ratio ra. This takes one minute, during which we increase re to re=re+ra
            # we open the valve, then we have release ratio ra=ra+valve. We then move to the new node, which takes one minute, during which we increase re to re=re+ra, or in original terms, re=re+ra+ra+valve
            # time increases with 2 during this move
            r = doit(i,t+2,v+","+p,ra+c[p][0],re+ra+ra+c[p][0])
            
            if r[2]>mx:
                acc=[r]
                mx=r[2]
                print(mx)
    # do not open the valve, then test the paths we have

    for i in c[p][1]:
        r = doit(i,t+1,v,ra,re+ra)
        if r[2]>mx:
            acc = [r]
            mx=r[2]
            print(mx)
            
#    print(acc)
    acc = sorted(acc, key=lambda x:-x[2])
    return acc[0]

mx=0
print(doit(p,t,"",0,0))

    

