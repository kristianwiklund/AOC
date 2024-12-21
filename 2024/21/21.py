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


lines = readlines("input.short")

numpad={}

arr = readarray("numpad",split="",convert=lambda x:x)

for i in [str(x) for x in range(0,10)]+["A"]:
    for j in [str(x) for x in range(0,10)]+["A"]:
        x1,y1 = findinarray(arr,i)
        x2,y2 = findinarray(arr,j)
        
        dx = (x2-x1)//4
        dy = (y2-y1)//2

        if sign(dx)<0:
            sx=("<"*-dx)
        elif sign(dx)>0:
            sx=(">"*dx)
        else:
            sx=""

        if sign(dy)<0:
            sy=("^"*-dy)
        elif sign(dy)>0:
            sy=("v"*dy)
        else:
            sy=""

        if y1!=7 and y2!=7:
            s = sx+sy
        else:
            s = sy+sx
            
        
        numpad[i,j] = s

numprev = "A"
        
def numpush(s):
    global numpad
    global numprev
    m=""
    
    for i in s:
        m+=numpad[numprev,i]+"A"
        numprev=i
        
    return m

s=numpush("029A")
assert(s=="<A^A^^>AvvvA")

numpad={}

arr = readarray("numpad",split="",convert=lambda x:x)

for i in [str(x) for x in range(0,10)]+["A"]:
    for j in [str(x) for x in range(0,10)]+["A"]:
        x1,y1 = findinarray(arr,i)
        x2,y2 = findinarray(arr,j)
        
        dx = (x2-x1)//4
        dy = (y2-y1)//2

        if sign(dx)<0:
            sx=("<"*-dx)
        elif sign(dx)>0:
            sx=(">"*dx)
        else:
            sx=""

        if sign(dy)<0:
            sy=("^"*-dy)
        elif sign(dy)>0:
            sy=("v"*dy)
        else:
            sy=""

        if y1!=7 and y2!=7:
            s = sx+sy
        else:
            s = sy+sx
            
        
        numpad[i,j] = s

numprev = "A"
        
def numpush(s):
    global numpad
    global numprev
    m=""
    
    for i in s:
        m+=numpad[numprev,i]+"A"
        numprev=i
        
    return m
    
            
        
