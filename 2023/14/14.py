import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache

arr = readarray("input",split="",convert=lambda x:x)
barr = deepcopy(arr)

#lines = readlines("input.short")

dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

def tiltn(arr):
    global dirs

    a = arr
    b = deepcopy(a)
    d = 0
    
#    print(b)
    (dx,dy) = dirs[d]

    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x]=='O':
                if checkpos(b, x+dx, y+dy, lambda x:x=='.', outofbounds=False):
                    b[y+dy][x+dx]='O'
                    b[y][x]='.'

    return b

while True:
    a = tiltn(arr)
    if a==arr:
        break
    arr = a

#pprint(a)

v = [len(a)-y if a[y][x]=='O' else 0 for y in range (len(a)) for x in range(len(a[0]))]
#print(v)
print("Part 1:",sum(v))

tarr = deepcopy(arr)

arr = barr

#print(p)

def tilt(arr, d):

    a = deepcopy(arr)
    
    (dx, dy)=dirs[d]

    p = [(x,y) for x in range(len(a[0])) for y in range(len(a)) if a[y][x]=='O']

    
    # sort p according to tilt direction
    match d:
        case 0:
            p = sorted(p, key=lambda x:x[1])
        case 1:
            p = sorted(p, key=lambda x:-x[0])
        case 2:
            p = sorted(p, key=lambda x:-x[1])
        case 3:
            p = sorted(p, key=lambda x:x[0])
    
    for i in p:
        x,y = i
    
        if checkpos(a, x+dx, y+dy, lambda x:x==".", outofbounds=False):
            a[y+dy][x+dx] = 'O'
            a[y][x]='.'

    return a


#pprint(arr)


@cache
def spin(s, n):

    arr = [list(s[i:i+n]) for i in range(0, len(s), n)]
    
#    print("spin me round")
    while True:
        a = tilt(arr, 0)
        if a==arr:
            break
        
        arr=a
    
#    print("N:")
    #pprint(arr)
    # check that north went the same way as the previous
    #assert(a==tarr)

    arr=a
    while True:
        a = tilt(arr,  3)
        if a==arr:
            break
        arr=a

 #   print("W:")
    #pprint(a)
    
    arr=a
    while True:
        a = tilt(arr,  2)
        if a==arr:
            break
        arr=a

  #  print("S:")
    #pprint(a)
    
    while True:
        a = tilt(arr,  1)
        if a==arr:
            break
        arr=a
        # print("E:")
        #    pprint(["".join(x) for x in a])

    a = "".join(["".join(x) for x in a])
    return a

def score(a):
    v = [len(a)-y if a[y][x]=='O' else 0 for y in range (len(a)) for x in range(len(a[0]))]    
    return(sum(v))

#pprint(arr)
s=arr
n = len(arr[0])
arr = "".join(["".join(x) for x in arr])
#pprint([list(arr[i:i+n]) for i in range(0, len(arr), n)])

#print(arr)

for x in range(1000000000):
    knarr = arr
    arr = spin(arr, n)
    if arr==knarr:
        #pprint(["".join(x) for x in arr])
        break

#    if not x % 1000000:
#       print(x)


print("Part 2:",score([list(arr[i:i+n]) for i in range(0, len(arr), n)]))
    
