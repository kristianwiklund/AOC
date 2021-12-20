1#!/usr/bin/python3

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

print("all scanners loaded")
sq={}
sq[0]=ipp[0]
ipp[0]=None

scanners=[]
scanners.append((0,0,0))

def klubba(A,B,mykt=False):

    bop = []
    gop = {}

    for i in A:
        for j in B:
            G = i-j

            s = (int(G[0]),int(G[1]),int(G[2]))
            
            if s in gop:
                gop[s]+=1
            else:
                gop[s]=1

    if mykt:
        from pprint import pprint
        pprint(gop)
    for t in gop:
        if gop[t]>=6:
            return t
            
    return None
            
def rotate(A,m):
    return (numpy.dot(A,m))

def align(cnt,ipp,cpp):
    
    for i in sq.keys():
        A = sq[i]

        A=numpy.array(A)
        
        for j in range(len(ipp)):
            if (i,j) in cpp or i==j:
                continue
            
            B = ipp[j]
            if B is None:
                continue
            
            B = numpy.array(B)
#            print ("trying "+str(i)+" vs "+str(j))

            for x in [0,90,180,270]:
                for y in [0,90,180,270]:
                    for z in [0,90,180,270]:
                        V=B
                        
                        if x!=0:
                            rx = R.from_euler("X", x, degrees=True)
                            mx = rx.as_matrix()
                            mx = mx*((abs(mx)>0.5))
                            mx = mx.astype(int)
                            V=rotate(V,mx)
                            
                        if y!=0:
                            ry = R.from_euler("Y", y, degrees=True)
                            my = ry.as_matrix()
                            my = my*((abs(my)>0.5))
                            my = my.astype(int)
                            V=rotate(V,my)

                        if z!=0:
                            rz = R.from_euler("Z", z, degrees=True)
                            mz = rz.as_matrix()
                            mz = mz*((abs(mz)>0.5))
                            mz = mz.astype(int)
                            V=rotate(V,mz)                        



                        t = klubba(A,V)

                        if t:
                            print ("Match between "+str(i)+" and "+str(j)+ " for ("+str(x)+","+str(y)+","+str(z)+")")
                            U=[]
                            for tt in V:
                                U.append(tt+t)
                            scanners.append(t)
                            print("Realign "+str(j))

                            sq[j]=U
                        
                            ipp[j]=None
                            cpp[(i,j)]="aligned"
                            return i

    return False

cpp={}

bop=True
cnt=0
while(bop):
    cnt = align(cnt,ipp,cpp)
    if cnt is False:
        bop=False
    pass

print("post align align summary")
p = set()
for i in sq:
    for j in sq[i]:
        p.add((j[0],j[1],j[2]))
print("Answer 1:",len(p))

m = 0

for i in range(len(scanners)-1):
    for j in range(i,len(scanners)):

        m = max(m, abs(scanners[i][0]-scanners[j][0])+abs(scanners[i][1]-scanners[j][1])+abs(scanners[i][2]-scanners[j][2]))

print("Answer 2:",m)
