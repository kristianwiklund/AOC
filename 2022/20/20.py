import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

def toright(seq,nr):
    i = seq.index(nr)
    del seq[i]
    if i==len(seq)-1:
        seq.insert(0,nr)
    else:
        seq.insert(i+1,nr)
        
    return seq

def toleft(seq,nr):
    i = seq.index(nr)
    del seq[i]
    i=i-1
    if i<=0:
        seq.append(nr)
    else:
        
        seq.insert(i,nr)
    return seq

def  qmix(seq,nr):

    if nr==0:
        return seq
    
    # find nr
    pos = seq.index(nr)

    # calculate new position
    np = pos+nr
    while np<0:
        np+=(len(seq)-1)
        
    np = np%(len(seq)-1)

    # remove nr from list
    del seq[pos]


    # three cases, we are in the middle, at the bottom, or at the top

    if np==0:
        print(">>>")
        return (seq+[nr])
    
    if np==(len(seq)):
        print("<<<")
        return ([nr]+seq)

    return seq[:np]+[nr]+seq[np:]
    
def mix(seq,nr):

    print("mixing",nr)
    if nr<0:
        for i in range(-nr):
            seq=toleft(seq,nr)
#            print("<",seq)
        return seq
    if nr>0:
        for i in range(nr):
            seq=toright(seq,nr)
#            print(">",seq)
        return seq
    return seq

    
arr = readarray("input.short",split=" ",convert=lambda x:int(float(x)))
arr=[x[0] for x in arr]
seq=deepcopy(arr)
seq2=deepcopy(arr)

seq=mix(seq,1)
seq2=qmix(seq2,1)
assert(seq==[2,1,-3,3,-2,0,4])
assert(seq==seq2)

seq=mix(seq,2)
assert(seq==[1,-3,2,3,-2,0,4])
seq=mix(seq,-3)

assert(seq==[1,2,3,-2,-3,0,4])


seq=mix(seq,3)
assert(seq==[1,2,-2,-3,0,3,4])

seq=mix(seq,-2)
assert(seq==[1,2,-3,0,3,4,-2])

seq=mix(seq,0)
assert(seq==[1,2,-3,0,3,4,-2])

print(seq)
seq=mix(seq,4)
print(seq)

assert(seq==[1,2,-3,4,0,3,-2])

## -

arr = readarray("input.txt",split=" ",convert=lambda x:int(float(x)))
arr=[x[0] for x in arr]
seq=deepcopy(arr)
seq2=deepcopy(arr)

print("---")

for i in arr:
    seq=mix(seq,i)
    seq2==qmix(seq2,i)
    assert(seq==seq2)
    
print("---")
p=seq.index(0)

#v = seq[(1000+p)%len(seq)]+seq[(2000+p)%len(seq)]+seq[(3000+p)%len(seq)]
#assert(v!=1306)
#assert(v!=10022)
#assert(v!=15540)
#assert(v!=2655)

print (seq[(1000+p)%len(seq)])
print (seq[(2000+p)%len(seq)])
print (seq[(3000+p)%len(seq)])

print("<",seq[(1000+p)%len(seq)]+seq[(2000+p)%len(seq)]+seq[(3000+p)%len(seq)])

from itertools import cycle

cnt=0
pp=0
found=False
for i in cycle(seq):

    if i==0 and not found:
        found=True
        print("pp",pp,"p",p)
        continue

    p+=1

    if found:
        cnt+=1
        if cnt==1000:
            print (i)
            a=i

        if cnt==2000:
            print (i)
            b=i

        if cnt==3000:
            print (i)
            print(">",a+b+i)
            break

    if p>len(seq)*2:
        print("ebreak")
        break

print("trest",p,len(seq),seq.index(8767))
