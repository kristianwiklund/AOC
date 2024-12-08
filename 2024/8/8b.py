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

t = sorted(list(set("".join([i for i in ["".join(i).replace(".","") for i in arr] if i]))))
#print (t)

def fan(arr,a):
    p = findinarray(arr,a,all=True)
    # only one antenna
    if len(p)<2:
        return set()
    
  #  print(a,p)

    n = []
    
    # for all nodes, compare with all other nodes

    for i in range(len(p)-1):

        for j in range(i+1, len(p)):
            leq = p2l((p[i],p[j]))
            m = []

            start = min(p[i][0],p[j][0])%abs(p[i][0]-p[j][0])
            
            #print("stepping from", start, "to", len(arr[0]), "in steps of", abs(p[i][0]-p[j][0]))
            for x in range(start, len(arr[0]) ,abs(p[i][0]-p[j][0])):
                y = int(fxl(leq,x))
                #print("step:",x,"y=",y)

                if checkpos(arr,x,y,lambda x:True):
                    m.append((x,y))

 #           print(p[i],p[j],abs(p[i][0]-p[j][0]),abs(p[i][1]-p[j][1]),m)                               
            if not (p[i][0],p[i][1]) in m or not (p[j][0],p[j][1]) in m:
                print("b0rked", m, leq)
                print(a,"+",p[i],p[j],end=" | ")
                printleq(leq)
                for x in range(len(arr)):
                    for y in range(len(arr[0])):
                        if arr[y][x]!=a:
                            arr[y][x]="."
                printpath([p[i]]+m+[p[j]],background=arr,highlight=a)
                sys.exit()
                
            n+=m
            
    #pprint(arr)
    return set(n)

@timer
def doit():
    s = set()
    for x in t:
        #print(x)
        ss = fan(arr,x)
        #print(x,ss)
        s|=ss

    return s

s=doit()
print(len(s))

#printpath(s,background=arr)

assert(len(s)>966)
