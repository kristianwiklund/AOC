import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split=" ",convert=lambda x:int(x))
#lines = readlines("input.short")

def doit(arr):
    pred = []
    for i in arr:
        t = []
        t.append(i)

        while sum([x==0 for x in i])!=len(i):
            a = []
            for p in range(len(i)-1):
                a.append(i[p+1]-i[p])
                
            t.append(a)
            i=a
        pred.append(t)
    
    for i in range(len(pred)):
        for j in range(len(pred[i])-1,0,-1):
            a = pred[i][j][-1]
            if a==0:
                pred[i][j].append(0)
                
            b = pred[i][j-1][-1]
            pred[i][j-1].append(a+b)

    s=0
    for i in pred:
        s+=i[0][-1]

    print(s)


doit(arr)
        
    

