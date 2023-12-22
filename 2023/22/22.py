import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split="~",convert=lambda x:ints(x))
#lines = readlines("input.short")

print(arr)
# annotate and convert to python ranges
arr = [[arr[i][0],[x+1 for x in arr[i][1]],chr(ord('A')+i)] for i in range(len(arr))]
print(arr)

# check if a intersects b

def intersects(a,b):

    # two volumes intersect if all of the areas overlap somehow
    
    if overlaps(range(a[0][0],a[1][0]), range(b[0][0],b[1][0])):
        if overlaps(range(a[0][1],a[1][1]), range(b[0][1],b[1][1])):
            if overlaps(range(a[0][2],a[1][2]), range(b[0][2],b[1][2])):
                return True
             
    return False


#assert(not intersects([[0, 0, 2], [2, 0, 2], 'B'],[[1, 0, 1], [1, 2, 1], 'A']))       
#assert(intersects([[0, 0, 1], [2, 0, 1], 'B'],[[1, 0, 1], [1, 2, 1], 'A']))


# try to drop the bricks one step
def tick():
    c = 0
    
    global arr
    # start at the bottom
    arr = sorted(arr, key=lambda x:x[0][2])

    # iterate over array, check if we can drop the current brick one step
    for i in range(len(arr)):
        # lowest possible, do nothing
        if arr[i][0][2]==1:
            continue

        # create a shadow cube at "one step down", test it against all other bricks in the system
        sb = deepcopy(arr[i])
        sb[0][2]-=1
        sb[1][2]-=1
    #    print("sb:",arr[i],sb)
    #    print(arr," x ", arr[i])
        t = [intersects(x,sb) for x in arr]
        t[i]=False
    #    for ii in range(len(t)):
    #        print(t[ii],arr[ii],sb)
        t = sum(t)
        
        if not t:
            arr[i]=sb
#            print(sb[2],t)                    
#            print("Moving",arr[i],"down")
            c+=1

    return c

def blockzorprintzor(arr):
#    barr = sorted(arr, key=lambda x:-x[0][2])
    xm=max([x[1][0] for x in arr])
    ym=max([x[1][1] for x in arr])
    zm=max([x[1][2] for x in arr])

    print(xm,ym,zm)

    import numpy as np
    a = np.full((zm,ym)," ")

    for i in arr:
        for x in range(i[0][1],i[1][1]):
            for z in range(i[0][2],i[1][2]):
                a[zm-z][x]=i[2]

    print(a)
    

cc=0
while True:
    c=tick()
    cc+=1
    print(cc,c)
    if not c:
        break
    #blockzorprintzor(arr)

#print(arr)

# check items from the bottom
arr = sorted(arr,key=lambda x:x[1][2])
print(arr)

c=0
tbf=0
barr=deepcopy(arr)
for i in range(len(barr)):

    arr=deepcopy(barr)
    # remove i from arr
    arr.pop(i)
    ccc=tick()
    if not ccc:
        c+=1
    else:
        tbf+=ccc
    
print("Part 1:",c)
print("Part 2:",tbf)



        
    
    
    
    
