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
    

# ---- "main" ----
grid = dict()

fd = open(sys.argv[1],"r")
lines = fd.readlines()

for line in lines:
    line = line.strip("\n\r")

    # eat the line

    movezor(0,0,grid, line)

print(len(grid))
