#!/usr/bin/python3

import sys

#^
#|
#Y X->

#0   1   2   3   4   5   6  
#  1   2   3   4   5   6  
#1   2   3   4   5   6   7
#  2   3   4   5   6   7
#2   3   4   5   6   7   8
#  3   4   5   6   7   8
#3   4   5   6   7   8   9

# (dx,dy)
M = {"e":(1,0),
     "w":(-1,0),
     "se":(1,-1),
     "sw":(0,-1),
     "ne":(0,1),
     "nw":(-1,1)
     }


def movezor(x,y,grid, line):

    ll = list(line)

    while ll != []:
        i = ll.pop(0)
        if i!='e' and i!='w':
            ii = ll.pop(0)
            i=i+ii
            
        (dx,dy) = M[i]
        x=x+dx
        y=y+dy

    if (x,y) in grid:
        grid.pop((x,y))
    else:
        grid[(x,y)] = "black"

# find all black surrounding (x,y)
def bctb(x, y, grid):

    black = list()
    white = list()
    
    for (dx,dy) in M.values():
        if (dx+x,dy+y) in grid:
            black.append((dx+x,dy+y))
        else:
            white.append((dx+x,dy+y))

    return (black,white)
        
    

def flipzor(grid):

    new = dict()
    cnt = dict()
    
    for (x,y) in grid:
        (black,white) = bctb(x,y, grid)

        # keep as black
        if len(black)==1 or len(black)==2:
            new[x,y]="black"
            
        for i in white:
            if i in cnt:
                cnt[i]=cnt[i]+1
            else:
                cnt[i]=1
                
    for i in cnt:
        if cnt[i]==2:
            new[i]="bläck"

    return (new)
        
    
        
# ---- "main" ----
grid = dict()

fd = open(sys.argv[1],"r")
lines = fd.readlines()

for line in lines:
    line = line.strip("\n\r")
    movezor(0,0,grid, line)

print("Answer to part 1: "+str(len(grid)))

# --- part 2 ---

new = grid
for i in range(0,100):
    new=flipzor(new)

print("Answer to part 2: "+str(len(new)))




