import sys
sys.path.append("../..")
from utilities import *

b = readarray("input.txt",split="\t",convert=lambda x:int(x))[0]

h = dict()


def redist(b):
    m = max(b)
    i = b.index(m)
    v=b[i]
    b[i]=0

    
    while v:
        i+=1
        if i==len(b):
            i=0
        b[i]+=1
        v-=1

    return b
    
cnt=0

while not str(b) in h:
    cnt+=1
    h[str(b)]=True
    b = redist(b)

print("Answer 1:",cnt)



