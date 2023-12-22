import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache, wraps
from cachetools import cached
from cachetools.keys import hashkey
import sys
sys.setrecursionlimit(10000)

arr = readarray("input.short",split="",convert=lambda x:int(x))
#lines = readlines("input.short")

#dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

#print(arr)

barr=arr
arr=np.array(arr)
#barr=np.zeros_like(arr)

mini=150

#@cache
#
#@logged

#@logged
@cache
def walk(p, x, y, d,acc):
    global E
    global arr
    global mini
    global barr

    
    if not checkpos(arr, x,y, lambda x:True, outofbounds=False):
        return None
    
    if mini and (acc+abs(x-len(arr[0]))+abs(y-len(arr)))>=mini:

 #       print("\033c\033[3J", end='')
        #       print(p)
 #       printpath(eval("["+p+"]")
 #                 +[(x,y)],
 #                 background=barr)
        
  #      print("(",acc,")")
        return None

    #    print("walk", (x,y)==E, x,y,p)
    if (x,y)==E:
        print("\033c\033[3J", end='')
        #       print(p)
        printpath(eval("["+p+"]")
                  +[(x,y)],
                  background=None)
#        print(p)
        
        if mini==None or acc<mini:
            print(acc)                   
            mini=acc
        return acc
    if str((x,y)) in p:
        #        print("\033c\033[3J", end='')
        #       print(p)
        #        printpath(eval("["+p+"]")
        #                  +[(x,y)],
        #                  background=barr)
        return None


    if (x,y)==B:
        pp=[2,1]
    else:
        pp = [[3,1],[0,2],[1,3],[2,0]][d]
    
    mi=[]
    bo=[]
    
#    print((x,y),B,"--",d,pp)
    for dd in pp:
 #       print(d,dd)
        dx = dirs[dd][0]
        dy = dirs[dd][1]

        p1 = checkpos(arr, x+dx,y+dy, lambda x:True, outofbounds=False)
        p2 = p1 and checkpos(arr, x+2*dx,y+2*dy, lambda x:True, outofbounds=False)
        p3 = p2 and checkpos(arr, x+3*dx,y+3*dy, lambda x:True, outofbounds=False)

        if p3:
#            bo.append((p+","+str((x,y))+","+str((x+2*dx,y+2*dy))+","+str((x+dx,y+dy)), arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx]+arr[y+3*dy][x+3*dx],x+3*dx,y+3*dy,dd))
            bo.append((p+","+str((x,y)), arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx]+arr[y+3*dy][x+3*dx],x+3*dx,y+3*dy,dd))            

        if p2:
            bo.append((p+","+str((x,y)), arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx],x+2*dx,y+2*dy,dd))
#            bo.append((p+","+str((x,y))+","+str((x+dx,y+dy)), arr[y+dy][x+dx]+arr[y+2*dy][x+2*dx],x+2*dx,y+2*dy,dd))
            
        if p1:
            bo.append((p+","+str((x,y)),arr[y+dy][x+dx],x+dx,y+dy,dd))
            
    bo = sorted(bo,key=lambda x:x[1]/3)

#     walk(p+str((x,y,d)),x+dx,y+dy,dd,acc+arr[y+dy][x+dx])
    for b in bo:
#        print("b=",b)
        mi.append( walk(b[0],b[2],b[3],b[4],acc+b[1]))

        
    mi =[i for i in mi if i!=None]
    #print (mi)
    mi = min(mi) if len(mi) else None
    
    if mi:    
        return mi
    else:
        return None

B=(0,0)
E=(len(arr[0])-1,len(arr)-1)

print(walk(str((-1,-1)), B[0], B[1], 1,0))



