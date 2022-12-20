import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.txt",split=" ",convert=lambda x:int(float(x)))
arr=[x[0] for x in arr]
seq=deepcopy(arr)

def mix(seq,nr):

    pos = seq.index(nr)
    del seq[pos]

    pos+=nr

    pos=pos%len(seq)

    if pos<0:
        pos+=(len(seq))

    if pos==0:
        pos=len(seq)
        
    a = seq[:pos]
    b = seq[pos:]
  
    if a!=[] and b!=[]:
        seq=seq[:pos]+[nr]+seq[pos:]
    elif a!=[]:
        seq=seq[:pos]+[nr]
    else:
        seq=[nr]+seq[pos:]
    return seq

# sq=deepcopy(seq)
# print(seq)
# seq=mix(seq,1)
# print(seq)
# assert(seq==[2,1,-3,3,-2,0,4])

# seq=mix(seq,2)
# assert(seq==[1,-3,2,3,-2,0,4])

# seq=mix(seq,-3)
# assert(seq==[1,2,3,-2,-3,0,4])

# seq=mix(seq,3)
# assert(seq==[1,2,-2,-3,0,3,4])

# seq=mix(seq,-2)
# assert(seq==[1,2,-3,0,3,4,-2])

# seq=mix(seq,0)
# assert(seq==[1,2,-3,0,3,4,-2])

# seq=mix(seq,4)
# assert(seq==[1,2,-3,4,0,3,-2])

# print("---")
# seq=sq
for i in arr:
    seq=mix(seq,i)

#print(seq)
p=seq.index(0)
#print(p)
print(seq[(1000+p)%len(seq)],seq[(2000+p)%len(seq)],(seq[(3000+p)%len(seq)]))
print (seq[(1000+p)%len(seq)]+seq[(2000+p)%len(seq)]+seq[(3000+p)%len(seq)])
