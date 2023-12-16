import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
#lines = readlines("input.short")

p=[(-1,0,1)]
e=set([(-1,0,1)])

dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}


def tick(arr, p, e):

    np=[]
    
    for i in p:
        (xx,yy,d) = i

        (dx,dy)=dirs[d]
        x=xx+dx
        y=yy+dy

        if (x,y,d) in e:
            continue

        if checkpos(arr, x, y, lambda z:True, outofbounds=False):
            e.add((x,y,d))
        
            match arr[y][x]:
                case ".":
                    np.append((x,y,d))
                case "|":
                    if d==1 or d==3:
                        np.append((x,y,0))
                        np.append((x,y,2))
                    else:
                        np.append((x,y,d))

                case "-":
                    if d==0 or d==2:
                        np.append((x,y,1))
                        np.append((x,y,3))
                    else:
                        np.append((x,y,d))

                case "/":
                    match d:
                        case 0:
                            np.append((x,y,1))
                        case 1:
                            np.append((x,y,0))
                        case 2:
                            np.append((x,y,3))
                        case 3:
                            np.append((x,y,2))

                case "\\":
                    match d:
                        case 0:
                            np.append((x,y,3))
                        case 1:
                            np.append((x,y,2))
                        case 2:
                            np.append((x,y,1))
                        case 3:
                            np.append((x,y,0))
#        print((xx,yy), p,np,e,arr[y][x])
        
    return(np,e)

c=0
while len(p):
#    print("----------")
    (p,e)=tick(arr,p,e)
#    print(c,p,e)
#    printpath(p, background=arr)
    c+=1
    
#print(len(e),e)
v = set([(x,y) for (x,y,z) in e])
#printpath(list(v),background=arr)
v.remove((-1,0))
#print(len(v))
#print(v)

a1=len(v)

def doit(arr, xs, ys, d):
    p=[(xs,ys,d)]
    e=set([(xs,ys,d)])

    while(len(p)):
        (p,e)=tick(arr,p,e)
        v = set([(x,y) for (x,y,z) in e])
        v.remove((xs,ys))
    return(len(v))

a2=doit(arr,-1,0,1)

assert(a1==a2)
print("Part 1:",a1)

acc=[]
d=2
y=-1
for x in range(len(arr[0])):
    acc.append((x,y,doit(arr, x,y,d)))

d=0
y=len(arr)
for x in range(len(arr[0])):
    acc.append((x,y,doit(arr, x,y,d)))
               

d=1
x=-1
for y in range(len(arr)):
    acc.append((x,y,doit(arr, x,y,d)))

d=3
x=len(arr[0])
for y in range(len(arr)):
    acc.append((x,y,doit(arr, x,y,d)))

acc=sorted(acc,key=lambda x:-x[2])
print("Part 2:",acc[0][2])
