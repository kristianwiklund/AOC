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

def push(ss,pad):
    prev="A"

    dacc=[]
    
    for s in ss:
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
        dacc+=acc
    return acc


su=0
for i in lines:
    t=push(push(push([i],numpad),dirpad),dirpad)
    t=list(set(t))
    t = min([len(x) for x in t])
    print(t)
    su+=t*ints(i)[0]
print(su)
assert(su<226342)
