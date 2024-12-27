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

lines = readlines("input.short")
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


n=push(["<"],dirpad)

@cache
def ndpush(s,l):
    global dirpad
    
    if l==25:
        return l

    l+=1
    print(l)
    c=0
    s="A"+s
    
    for i in range(1,len(s)):
#        print(dirpad[(s[i-1],s[i])])
        if s[i-1]==s[i]:
            c+=costzor[s[i-1],s[i]]
        else:
            c+=ndpush(dirpad[(s[i-1],s[i])][0],l)+costzor[s[i-1],s[i]]

    return c

for u in lines:
    b = push(u,numpad)[0]
    print("b=",b)
    n=ndpush(b,0)
    print(b,n)
