import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

from rules import *

lines = readlines("input")
#lines=["5"]


def push(ss,pad):
    prev="A"

    dacc=[]
    
    for s in ss:
        #print(s)
        acc=[""]
        for i in s:
            if prev==i:
                hopp=["A"]
            else:
                hopp = pad[prev,i]
        
            mcc=[]
            #print(hopp,len(hopp))
            for v in acc:
                for t in hopp:
                   # print("vt",v,t)
                    mcc.append(v+t)
            prev=i                
            acc=mcc
            #print(acc)
        dacc+=acc
    return sorted(dacc,key=kolf2)


su=0
for i in lines:
    print(i)
    n=push([i], numpad)
    print("..")
    o=push(n, dirpad)
    print("--")
    p=push(o, dirpad)
    #print("n",n)
    #print("o",o)
    #print("p",p)
    t=list(set(p))
    #print(t)
    #print([len(x) for x in t])
    #print([kolf2(x) for x in t])
    t = min([len(x) for x in t])
    #print(t)
    su+=t*ints(i)[0]
print(su)

#print("x",push(["^^<A"],dirpad))
#print("y",push(['<^^A'],dirpad))
#print("z",push(['^<^A'],dirpad))
assert(su<226342)
assert(su!=27235)
assert(su!=225748)
assert(su!=218300)
