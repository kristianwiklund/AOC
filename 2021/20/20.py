#!/usr/bin/python3

import sys,numpy

M=[]
for l in sys.stdin:

    l=l.strip()

    if len(l)==512:
        print("Got IRS")
        irs=l
    elif len(l)>0:
        M.append([1 if x =='#' else '0' for x in l])

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
    for y in range(-200,len(M)+200):
        s=[]
        for x in range(-200,len(M[0])+200):
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
    assert(gv(M,2,2)==34)
    print("test 1  passed")

    assert(gv(M,-10,-10)==0)
    print("test 2 passed")

M=enhance(M,step2=False)
print("step 1:"+str(len(M)))

M=enhance(M,step2=True)
print("step 2:"+str(len(M)))
#print(M)

pr(M)
s=0
for y in M:
   s+=sum(y)
print(s)

# not 6816
# 10590 is too high
# 5504
