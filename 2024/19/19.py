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

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")
#from multiprocessing import Pool

pat = sorted(lines[0].replace(" ","").split(","), key=len)
#print(pat)
lines = lines[2:]
#print(lines)

@cache
def match(line):
    global pat
    fr=[]
    for i in pat:
        if line.startswith(i):
            fr.append((i, line[len(i):]))

    return fr

#tp = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']

def make(pile):
    global pat
    o,c,l = pile

    v = match(c)
    if not len(v):
        return([],[])

    newp = [(o,y,l+[x]) for x,y in v if len(y)]
    nawp = [(o,y,l+[x]) for x,y in v if not len(y)]
    return (newp, nawp)

X=[]
poss = set()

for l in lines:
#    X.append(("brwrr","brwrr",[]))

    print("Testing line",l)
    X=[(l,l,[])]
    
    ppo = 0

    vis = set()

    #pool = Pool()

    class byebye(Exception):
        pass

    cnt=0
    try:
        while len(X):
            if not cnt%100:
                print(cnt,len(X))
            cnt+=1
                    
            #    p = X.pop()
            #print(len(X))
            
            #    (x,y) = make(pat,p)
        
#            print("LX:",len(X))
            #    res = pool.map(make, X)
#            res = map(make, X)
            #            print("res",list(res))
            NX=[]
            
            for Y in X:                
                R = make(Y)
                
#                print("in:",Y,"out:",R)
                (x,y)=R
#                print(x)
#                print(y)
                if len(y):
                    poss.add(l)                                        
                    print("Hit",len(poss),"/",len(lines), "y=",y)
                    raise byebye
#                print("x",x)
                for a,b,c in x:
                    if not (a,b,c) in NX:
                        NX.append((a,b,c))
                    #            print("NX",NX)
            print(poss, len(NX))
            X = NX
    except byebye:
        continue
    
print(poss)
print(len(poss))
    
