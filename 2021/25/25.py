#!/usr/bin/python3

import sys

# ------ input

M={}

y=0
for l in sys.stdin:

    x=0
    for t in l.strip():
        if t in [">","v"]:
            M[(x,y)]=t
        x+=1
    y+=1

maxx=x
maxy=y

# ------ print

def pr(M,maxx,maxy):
    for y in range(maxy):
        print (str(y)+": ",end="")
        for x in range(maxx):
            if (x,y) in M:
                print(M[(x,y)],end="")
            else:
                print(".",end="")
        print("")

# ------ movement code

def move(M, maxx, maxy, c, dx, dy):

    canmove={}

    L = sorted(M, key=lambda x:x[0], reverse=True)

    for (x,y) in L:
        if M[(x,y)] == c:
            nx = (x+dx)%maxx
            ny = (y+dy)%maxy
        
            if not (nx, ny) in M:
                canmove[(x,y)]=(nx,ny)


    for i in canmove.keys():
        t = M[i]
        M.pop(i)

        M[canmove[i]]=t

    return (M, len(canmove))
    
    

def step(M,maxx,maxy):

    (M, movesx)  = move(M,maxx,maxy,">",1,0)
    (M, movesy)  = move(M,maxx,maxy,"v",0,1)
    
    return (M, movesx+movesy)

# ------ test code using the short test from AOC

MT = {(0, 0): 'v', (4, 0): '>', (5, 0): '>', (7, 0): 'v', (8, 0): 'v', (9, 0): '>', (1, 1): 'v', (2, 1): 'v', (3, 1): '>', (4, 1): '>', (6, 1): 'v', (7, 1): 'v', (0, 2): '>', (1, 2): '>', (3, 2): '>', (4, 2): 'v', (5, 2): '>', (9, 2): 'v', (0, 3): '>', (1, 3): '>', (2, 3): 'v', (3, 3): '>', (4, 3): '>', (6, 3): '>', (8, 3): 'v', (0, 4): 'v', (1, 4): '>', (2, 4): 'v', (4, 4): 'v', (5, 4): 'v', (7, 4): 'v', (0, 5): '>', (2, 5): '>', (3, 5): '>', (6, 5): 'v', (1, 6): 'v', (2, 6): 'v', (5, 6): '>', (7, 6): '>', (8, 6): 'v', (0, 7): 'v', (2, 7): 'v', (5, 7): '>', (6, 7): '>', (7, 7): 'v', (9, 7): 'v', (4, 8): 'v', (7, 8): 'v', (9, 8): '>'}

for i in range(58):
    (MT,_) = step(MT,10,9)

assert (MT=={(2, 0): '>', (3, 0): '>', (4, 0): 'v', (5, 0): '>', (6, 0): 'v', (7, 0): 'v', (2, 1): 'v', (4, 1): '>', (5, 1): '>', (6, 1): 'v', (7, 1): 'v', (2, 2): '>', (3, 2): '>', (4, 2): 'v', (5, 2): '>', (6, 2): '>', (7, 2): 'v', (8, 2): 'v', (2, 3): '>', (3, 3): '>', (4, 3): '>', (5, 3): '>', (6, 3): '>', (7, 3): 'v', (8, 3): 'v', (0, 4): 'v', (7, 4): '>', (8, 4): 'v', (9, 4): 'v', (0, 5): 'v', (1, 5): '>', (2, 5): 'v', (7, 5): '>', (8, 5): '>', (9, 5): 'v', (0, 6): 'v', (1, 6): 'v', (2, 6): 'v', (8, 6): '>', (9, 6): '>', (0, 7): '>', (1, 7): 'v', (2, 7): 'v', (9, 7): '>', (1, 8): '>', (2, 8): 'v', (4, 8): 'v', (5, 8): 'v', (7, 8): 'v'})
    
# ------ end test code

n = 1
c=0
while n>0:
    (M,n) = step(M,maxx,maxy)
    c+=1

print ("Answer 1:",c)
