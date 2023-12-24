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


#lines = readlines("input.short")
#print(arr)


def p2l(P):
    
    P1 = P[0]
    P2 = [P[0][0]+P[1][0],P[0][1]+P[1][1]]

    x1 = P1[0]
    y1 = P1[1]

    x2 = P2[0]
    y2 = P2[1]

    A = y2-y1
    B = x1-x2
    C = y1*(x2-x1)-(y2-y1)*x1

#    print("x",A,B,C,P)
    return ([A,B,C])
    

arr = readarray("input",split="@",convert=lambda x:ints(x)[0:2])
barr = [p2l(x) for x in arr]    
#print(barr)
if len(arr)>50:
    limits = (200000000000000, 400000000000000)
else:
    limits = (7,27)


#@logged
def isx(L1,L2):

#    print(L1,L2)
    X = cross(L1,L2)
#    X = (X/X[2])[0:2]

    return X


c=0
cc=0
d=0
dd=0

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):

        v = isx(barr[i],barr[j])
        print(v)
        if v[2]!=0:
            p = (limits[0]*v[2] <= v[0]) and (v[0] <= limits[1]*v[2]) and  (limits[0]*v[2] <= v[1]) and (v[1] <= limits[1]*v[2])
            q1 = (v[0]>=arr[j][0][0]*v[2]) if arr[j][1][0]>=0 else (v[0]<=arr[j][0][0]*v[2])
            q2 = (v[0]>=arr[i][0][0]*v[2]) if arr[i][1][0]>=0 else (v[0]<=arr[i][0][0]*v[2])

            cc+=1
            if p:
                if q1 and q2:
                    #                print ("---")
                    #                print(arr[i],arr[j],v,arr[j][0],arr[j][1],q1, q2,p)
                    #                print (v,limits[0]*v[2],limits[1]*v[2])
                    #A                import sys
                    #                sys.exit()
                    c+=1
                else:
                    d+=1
        else:
            dd+=1

#print(arr[-1])
            
print("Answer 1:",c, "(checked",cc,"pairs)",d,"were in the past for a total of ",d+c,"intersections")
print("         ",dd, "were outside the area")
assert(c>16518) 
