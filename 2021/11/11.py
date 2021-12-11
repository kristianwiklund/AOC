#!/usr/bin/python3

import sys,numpy

f = [t.strip() for t in sys.stdin]
M=[]
for i in f:
    M.append([int(x) for x in i])

M = numpy.array(M)
N = M

#print(M)

def mset(M,F,x,y):
    if x<0 or y<0:
        return
    if x>len(M)-1:
        return
    if y>len(M[x])-1:
        return
    if F[x][y]:
        return
    
    M[x][y]+=1
    
def c(M):
    F = M<-1000
    
    M = M + 1

    T = M > 9
    cnt=0
    all=False
    while T.any():
        cnt+=sum(sum(T))

        for x in range(len(M)):
            for y in range(len(M[x])):
                if T[x][y] and not F[x][y]:
                    F[x][y]=True
                    M[x][y]=0
                    mset(M,F,x-1,y-1)
                    mset(M,F,x-1,y)
                    mset(M,F,x-1,y+1)
                    mset(M,F,x,y-1)
                    mset(M,F,x,y+1)
                    mset(M,F,x+1,y-1)
                    mset(M,F,x+1,y)
                    mset(M,F,x+1,y+1)
        T = M > 9
    return(M,cnt,F.all())

flashes=0
all=-1
for i in range(100):
    (M,f,a)=c(M)
    flashes+=f
    if a:
        all=i
    
print("Answer 1:",flashes)

if not a:
    while True:
        (M,f,a)=c(M)
        flashes+=f
        if a:
            all=i
            break
        i+=1

print("Answer 2:",all+2)

