import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")
#print(arr)

barr=deepcopy(arr)

c=0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x]=='@' and countallaround(arr,x,y,lambda x:x=='@')<4:
            c+=1

print("part 1:", c)

#---------

def bop(arr):
    c=0
    for y in range(len(arr)):
        
        for x in range(len(arr[0])):
            if checkpos(arr,x,y,lambda x:x=="."):
                continue
            
            if countallaround(arr,x,y,lambda x:x=='@')<4:
                c+=1
                arr[y][x]="."

        for x in range(len(arr[0])-1,0,-1):
            if checkpos(arr,x,y,lambda x:x=="."):
                continue
            
            if countallaround(arr,x,y,lambda x:x=='@')<4:
                c+=1
                arr[y][x]="."


    for x in range(len(arr[0])):

        for y in range(len(arr)):
            if checkpos(arr,x,y,lambda x:x=="."):
                continue
            
            if countallaround(arr,x,y,lambda x:x=='@')<4:
                c+=1
                arr[y][x]="."

        for y in range(len(arr)-1,0,-1):
            if checkpos(arr,x,y,lambda x:x=="."):
                continue
            
            if countallaround(arr,x,y,lambda x:x=='@')<4:
                c+=1
                arr[y][x]="."

                        
    return c

#pprint(arr)

s=0
while True:
    c=bop(arr)
    s+=c
    if not c:
        break
print(s)
#pprint(arr)
                
        


