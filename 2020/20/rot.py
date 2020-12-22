#!/usr/bin/python
import sys

def rpic90(A):

    NA=list()
#    print("---------")
#    pprint(A)

    for y in range(0,len(A)):
        s = ""
        for x in range(0,len(A)):
            s=s+A[x][y]
        NA.append(s[::-1])

        #    pprint(NA)
        #    print("---------")
    return(NA)

A=list()
for line in sys.stdin:
    A.append(line.strip("\n\r"))


A=rpic90(A)

for y in range(0,len(A)):
    print(A[y])
