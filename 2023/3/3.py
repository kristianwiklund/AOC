import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
import scipy

arr = readarray("input.long",split="",convert=lambda x:0 if x=="." else ord(x)+10)
#lines = readlines("input.short")

arr = np.array(arr)

labels,  numl = scipy.ndimage.label(arr, structure=[[1,1,1],[1,1,1],[1,1,1]])
t=np.zeros_like(arr)
f = np.vectorize(lambda x:int(chr(x-10))+10 if (x>=ord('0')+10 and x<=ord('9')+10) else x)
        
arr = f(arr)

for i in range(numl+1):
    a = arr*(labels == i)
    v = a>19
    if sum(sum(v)):
        t+=a

t = t*(t<=19)

narr=[]
for i in t:
    i = [str(x-10) if x else " " for x in i]
    narr.append(ints("".join(i)))

print("Part 1:", sum([sum(x) for x in narr]))

sum=0
for i in range(numl+1):
    a = arr*(labels==i)
    if (a==(ord('*')+10)).any():
        a = f(a)
        # adjacent to _exactly two_ part numbers
        a = a*(a<=19)
        b = ""
        for i in a:
            b+="".join([str(x-10) if x else " " for x in i])
        
        nums = ints(b)
        if len(nums)==2:
            sum+=(nums[0]*nums[1])

print("Part 2:",sum)
