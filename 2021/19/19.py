#!/usr/bin/python3

import sys
import scipy, numpy, scipy.spatial
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

ipp = {}
for i in sys.stdin:
    t = i.split()
    j = i.split(",")
    if "---" in i:
        scanner=int(t[2])
        print("Loading data from scanner "+str(scanner))
        ipp[scanner]=[]
    elif len(j)==3:
        ipp[scanner].append(numpy.array([int(x) for x in j]))

for i in ipp:
    ipp[i] = numpy.array(ipp[i])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in ipp:
    for j in ipp[i]:
        ax.scatter(j[0], j[1], j[2], marker=i)

plt.savefig("points.png")

def klubba(A,B):

    bop = []
    gop = {}
    for i in A:
        for j in B:
            G = i-j
            if (int(G[0])==68):
                s = (int(G[0]),int(G[1]),int(G[2]))
                if s in gop:
                    gop[s]+=1
                else:
                    gop[s]=1
    return gop
            

for i in range(len(ipp)-1):
    A = ipp[i]
    for j in range(i+1,len(ipp)):
        B = ipp[j]
        #        for k = range(24):
        r = R.from_euler('y', 180, degrees=True)
        V=r.apply(B)        
        print(klubba(A,V))

#r = R.from_euler('y', 180, degrees=True)
#B=numpy.matrix([[686,422,578]])
#print(B)
#print(r.apply(B))
