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

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

px = arr[0].index("S")
arr[1][px]="|"
barr = createidenticalarray(arr,0)
barr[1][px]=1




s=0
for y in range(1,len(arr)-1):
    for x in range(len(arr[y])):
        if arr[y][x]=="|":
            if arr[y+1][x]=="." or arr[y+1][x]=="|":
                arr[y+1][x]="|"
                barr[y+1][x]+=barr[y][x]
            elif arr[y+1][x]=="^":
                arr[y+1][x-1]="|"
                arr[y+1][x+1]="|"
                barr[y+1][x-1]+=barr[y][x]
                barr[y+1][x+1]+=barr[y][x]
                s+=1


n = [1 for x in arr[-1] if x=="|"]
print("part 1:",s)

#pprint(barr)

print("part 2:",sum(barr[-1]))




                    

