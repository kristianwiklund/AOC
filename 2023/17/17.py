import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
from copy import copy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache
from clear_screen import clear

arr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

B = (0,0)
E = (len(arr[0])-1,len(arr)-1)

barr = [[2**64]*len(x) for x in arr]
front = SortedSet(key=lambda x:barr[x[0][1]][x[0][0]])

def bfs(arr, B, E):
    global front

    while len(front):
        
        (x,y),d,c = front.pop();

        p = checkallpos(arr,x,y,lambda x:True,outofbounds=False)

        for i,v in enumerate(p):
            if v:
                if abs(i-d)==2:
                    continue

                nx=x+dirs[i][0]
                ny=y+dirs[i][1]
                cost = barr[y][x]+arr[ny][nx]
                
                if i==d:
                    c+=1
                    if c<4:
                        if barr[ny][nx]>cost:
                            barr[ny][nx]=cost
                            front.add(((nx,ny),i,c))
                else:
                    if barr[ny][nx]>cost:
                        barr[ny][nx]=cost
                        front.add(((nx,ny),i,0))                    
                    
    return barr


front.add((B,1,0))
barr[B[1]][B[0]]=arr[B[1]][B[0]]
barr = bfs(arr,B,E)
pprint(barr)
printpath(droute(arr,barr,B,E,f=lambda x:True), background=arr)
