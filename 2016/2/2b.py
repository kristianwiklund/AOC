import sys

a = [[0,0,1,0,0],
     [0,2,3,4,0],
     [5,6,7,8,9],
     [0,'A','B','C',0],
     [0,0,'D',0,0]]

x=0
y=2

print("Answer 2: ",end='')

for l in sys.stdin:
    
    for t in l:
        ox=x
        oy=y
        if t=="U":
            y=max(0,y-1)
            if a[y][x]==0:
                y=oy
        if t=="D":
            y=min(4,y+1)
            if a[y][x]==0:
                y=oy
        if t=="L":
            x=max(0,x-1)
            if a[y][x]==0:
                x=ox
        if t=="R":
            x=min(4,x+1)
            if a[y][x]==0:
                x=ox
        
                
    print(a[y][x],end="")

print("")
