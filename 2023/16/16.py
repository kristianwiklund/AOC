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
op=set()

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
print(len(v))
#print(v)
    
