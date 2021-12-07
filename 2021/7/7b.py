#!/usr/bin/python3
import sys,numpy

f = [t.split(",") for t in sys.stdin]
f = [int(x) for x in f[0]]
F = numpy.array(f)

t = list()
for i in range(0,max(f)+1):
    #if i == 2:
        #print(F)
        #print(numpy.abs(F-i))
    T = numpy.abs(F-i)
    g = []
    for j in T:
        g.append(sum(range(j+1)))
    t.append(sum(g))
    
#print(t)
print(min(t))

# 258542 too low
