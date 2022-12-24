import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.short",split="",convert=lambda x:x)
b=arr2sparse(arr,ignore="#.")
#print(b)
bliz=dict()
c=0
for i in b:
    bliz[c]=(i,b[i])
    c+=1

#print(bliz)
    
bm = {
    ">":(1,0),
    "^":(0,-1),
    "v":(0,1),
    "<":(-1,0)
    }

# moves the things
def tick(b):

    b = deepcopy(bliz)
    
    for ii in bliz:
        #        print("moving",ii,bliz[ii])
        i,dd = bliz[ii]
        d = bm[dd]
        x,y =i
        
        nx=x+d[0]
        ny=y+d[1]
        # check wrap
        if nx>=len(arr[0]):
            nx=1
        if ny>=len(arr):
            ny=1
        if nx<=0:
            nx=0
        if ny<=0:
            ny=0
            #        print("new bliz pos:",(nx,ny))
#        arr[y][x]="."
#        arr[ny][nx]=dd
        bliz[ii]=((nx,ny),dd)
    
    return bliz

# start and stop points

x=arr[0].index(".")
y=0

stopx=arr[-1].index(".")
stopy=len(arr)-1

def checkbang(x,y,bliz):
    b = [x for x,d in bliz.values()]
    return (x,y) in b

assert(checkbang(1,1,{1:((1,1),">")}))
assert(not checkbang(1,0,{1:((1,1),">")}))

def solve(x,y,bliz):
    global stopx
    global stopy
    
    b = list(zip([1,0,-1,0],[0,-1,0,1]))
    
    if checkbang(x,y,bliz):
        return False

    if x==stopx and y==stopy:
        print("Win")
        import sys
        sys.exit()
    
    
    b2 = tick(bliz)
    for dx,dy in b:
        solve(x+dx,y+dy,b2)

solve(x,y,bliz)
