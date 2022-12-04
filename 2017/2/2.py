import sys
sys.path.append("../..")
from utilities import *

arr = readarray("input", split="\t", convert = lambda x:int(x))
score = 0

    
for a in arr:
    
    a = sorted(a)
    l = len(a)

    for i in range(l):
        for j in range(i+1,l):
            if not (a[j]%a[i]):
                score += a[j]//a[i]
                
print (score)
