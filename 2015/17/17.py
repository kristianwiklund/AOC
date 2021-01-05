#!/usr/bin/python3

import itertools


#input
r = [43,
     3,
     4,
     10,
     21,
     44,
     4,
     6,
     47,
     41,
     34,
     17,
     17,
     44,
     36,
     31,
     46,
     9,
     27,
     38]
vol=150

#testcase
#r = [5,5,10,15,20]
#vol=25


x = list()

for i in range(1,len(r)+1):
    x+=list(itertools.combinations(r, i))

y = [x for x in x if sum(x)==vol]
    
print("Answer to a: ",len(y))

for i in range(1,len(r)+1):
    x = list(itertools.combinations(r, i))
    y  = [x for x in x if sum(x)==vol]
    if y:
        break

print ("Answer to b:",len(y))
