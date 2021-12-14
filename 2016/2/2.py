#!/usr/bin/python3

import sys

x=2
y=2

print("Answer 1: ",end="")

for i in sys.stdin:

    for t in i:
        if t=="U":
            y=max(1,y-1)
        if t=="D":
            y=min(3,y+1)
        if t=="L":
            x=max(1,x-1)
        if t=="R":
            x=min(3,x+1)
        
    print(x+(y-1)*3,end="")

print("")
