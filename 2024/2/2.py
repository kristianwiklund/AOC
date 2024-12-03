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

arr = readarray("input",split=" ",convert=lambda x:int(x))
#lines = readlines("input.short")
#print(arr)


c=0
u=[]

def check(x):
    p = [x[i]-x[i+1] for i in range(len(x)-1)]
    y = [False if abs(j)>3 or abs(j)==0 else sign(j) for j in p]
    return not False in y and not abs(sum(y))!=len(y)
        
for i in range(len(arr)):
    x=arr[i]

    if check(x):
        c+=1
        continue
    else:
        u.append(i)
        continue

print("A:",c)

c2=0
for i in u:
    x = arr[i]
    s=False
    for y in range(len(x)):
        a = x[:y]+x[y+1:]
        s=check(a)
        if(s):
            break
    if s:
        c2+=1

print("B:",c+c2)
            
    

    

    
