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

barr = readarray("input",split=",",convert=lambda x:int(x))
#lines = readlines("input.short")

if len(barr)<30:
    MX=6
    MY=6
    L=12
else:
    MX=70
    MY=70
    L=1024

x,y=0,0
arr=sparse2arr(barr[:L], dim=(MX+1,MY+1))
(_,p) = dijkstra(arr, (x,y),stop=(MX,MY))
printpath(p, background=arr)
print("A:",len(p)-1)

for x,y in barr[L:]:
    arr[y][x]="#"
c=len(barr)    
for x,y in barr[L:][::-1]:
    arr[y][x]="."
    print(c,"/",len(barr))
    c-=1
    (_,p) = dijkstra(arr, (0,0),stop=(MX,MY))
    if p:
        print("B:",(x,y))
        break
