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

for i in ipp:
    ipp[i] = numpy.array(ipp[i])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in ipp:
    for j in ipp[i]:
        ax.scatter(j[0], j[1], j[2], marker=i)

plt.savefig("points.png")

def klubba(A,B,mykt=False):

    bop = []
    gop = {}
    for i in A:
        for j in B:
            G = i-j

            s = (int(G[0]),int(G[1]),int(G[2]))
            if mykt:
                print (s)
            if s in gop:
                gop[s]+=1
            else:
                gop[s]=1


    for t in gop:

        if gop[t]==12:
            return t
            
    return None
            

def align(ipp,cpp):
    
    for i in range(0,len(ipp)-1):
        A = ipp[i]
        for j in range(i+1,len(ipp)):
            if (i,j) in cpp:
                continue

            print ("trying "+str(i)+" vs "+str(j))
            B = ipp[j]


            for a in ["x","y","z"]:
                for d in [0,90,180,270]:
                    r = R.from_euler(a, d, degrees=True)
                    m = r.as_matrix()
                    m = m*((abs(m)>0.5))
                    r = R.from_matrix(m)
                    V=r.apply(B)
                    mykt = (i==1) and (j==4)
                    if mykt:
                        print ("Trying "+str(i)+" and "+str(j)+" "+str(a)+"="+str(d))
                        print(V-A)
                    t = klubba(A,V,False)
                    if t:
                        print ("Match between "+str(i)+" and "+str(j)+" "+str(a)+"="+str(d))
                        U=[]
                        for tt in V:
                            U.append(tt+t)
                        ipp[j]=U
                        cpp[(i,j)]="aligned"
                        return True
    return False

cpp={}
while(align(ipp,cpp)):
    print("bopp")


#r = R.from_euler('y', 180, degrees=True)
#B=numpy.matrix([[686,422,578]])
#print(B)
#print(r.apply(B))
