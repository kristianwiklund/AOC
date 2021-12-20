#!/usr/bin/python3

import sys

M=[]
for l in sys.stdin:

    l=l.strip()

    if len(l)==512:
        print("Got IRS")
        irs=l
    elif len(l)>0:
        M.append([1 if x =='#' else '0' for x in l])

O=M
#print(M)

def gp(M,y,x,step2):

    if x<0 or x>=len(M[0]):
        return 1 if step2 else 0

    if y<0 or y>=len(M):
        return 1 if step2 else 0

    return M[y][x]

    
    
def gv(M,x,y,step2):
    s=""
    s+=str(gp(M,y-1,x-1,step2))
    s+=str(gp(M,y-1,x,step2))
    s+=str(gp(M,y-1,x+1,step2))
    s+=str(gp(M,y,x-1,step2))
    s+=str(gp(M,y,x,step2))
    s+=str(gp(M,y,x+1,step2))
    s+=str(gp(M,y+1,x-1,step2))
    s+=str(gp(M,y+1,x,step2))
    s+=str(gp(M,y+1,x+1,step2))

    return (int(s,2))

def lookup(irs,v):
    return 1 if irs[v]=="#" else 0

def enhance(M,step2=False):

    NM=[]
    for y in range(-5,len(M)+5):
        s=[]
        for x in range(-5,len(M[0])+5):
            s.append(lookup(irs,gv(M,x,y,step2)))
        NM.append(s)
    return NM

def pr(M):
    for y in M:
        for x in y:
            if x:
                print("#",end="")
            else:
                print(".",end="")
        print("")
        

if len(M)==5: # test code
    assert(gv(M,2,2,False)==34)
    print("test 1  passed")

    assert(gv(M,-10,-10,False)==0)
    print("test 2 passed")

    assert(gv(M,-10,-10,True)==0b111111111)
    print("test 3 passed")

    testing=True
else:
    testing=False

M=enhance(M,step2=False)

M=enhance(M,step2=(True if not testing else False))

s1=0
for y in M:
   s+=sum(y)


# 5395
M=O

for i in range(50):
    M = enhance(M,step2=((i%2!=0) if not testing else False))
    print (i)
    
s=0
for y in M:
   s+=sum(y)

print("Answer 1:",s1)
print("Answer 2:",s)
