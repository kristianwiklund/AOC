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
import numpy as np
#import scipy
#from functools import cache

#Earr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")


c=0
s=[]
ss=[]

def idiotsolve(a,b,c):

    A = np.array([[a[0],b[0]],[a[1],b[1]]])
    B = np.array(c)

    y = np.linalg.solve(A,B)
    
    T = [int(round(y[0],0)),int(round(y[1],0))]
    I = [int(y[0]),int(y[1])]

    if np.array_equal(np.dot(A,T),B):
        return T[0]*3+T[1]
    else:
        return None
    
while True:

    if not "Button A: X" in lines[c]:
        raise Exception("Button A")
    if not "Button B: X" in lines[c+1]:
        raise Exception("Button B")
    if not "Prize: X" in lines[c+2]:
        raise Exception("Prize")
    
    a1=ints(lines[c])
    b1=ints(lines[c+1])
    e1=ints(lines[c+2])
    e1[0]+=10000000000000
    e1[1]+=10000000000000
    
    r = idiotsolve(a1,b1,e1)
    if r:
        ss.append(r)

    c+=4
    if c>=len(lines):
        break


print("---")
print("ss:", ss)
print("SS:",sum(ss),"tokens")
assert(sum(ss)>20271)
assert(sum(ss)>27760)
assert(sum(ss)!=133248)
print(c,"lines")
print(len(ss),"wins")

