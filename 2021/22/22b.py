#!/usr/bin/python3

import sys


class Box:
    def __init__(self, l):

        def splitinaTOR(s):
            x = s.split("=")[1].split("..")
            return (int (x[0]), int(x[1]))

        if type(l)==str:
            x = l.split()
            
            state = x[0]
            y = x[1].split(",")
        
            self.state = state
        
            (l,r)=splitinaTOR(y[0])
            self.x1 = min(l,r)
            self.x2 = max(l,r)+1
        
            (l,r)=splitinaTOR(y[1])
            self.y1 = min(l,r)
            self.y2 = max(l,r)+1
            
            (l,r)=splitinaTOR(y[2])
            self.z1 = min(l,r)
            self.z2 = max(l,r)+1
            
            self.id=None

        elif type(l)==list:

            self.state = l[0]
            self.x1 = l[1]
            self.x2 = l[2]
            self.y1 = l[3]
            self.y2 = l[4]
            self.z1 = l[5]
            self.z2 = l[6]
            if len(l)==8:
                self.id = l[7]
            else:
                self.id=None
    def __repr__(self):
        s= self.state+" x="+str(self.x1)+".."+str(self.x2-1)+",y="+str(self.y1)+".."+str(self.y2-1)+",z="+str(self.z1)+".."+str(self.z2-1)
        if self.id:
            s = s + " = "+str(self.size())
            s = s + " ("+self.id+")"
        return s

    def size(self):
        xs = (self.x2-self.x1)
        ys = (self.y2-self.y1)
        zs = (self.z2-self.z1)

        s = abs(zs*ys*xs) * (-1 if (zs<0 or ys<0 or xs <0) else 1)
        
        return s

class Reactor:
    def __init__(self):
        self.reactor=[]
        self.realcubes=[]
        self.thesize = 0

    # cube completely overlaps c
    def coverlap(self, cube, c):
        
        return c.x1>=cube.x1 and c.x2<=cube.x2 and c.y1>=cube.y1 and c.y2<=cube.y2 and c.z1>=cube.z1 and c.z2<=cube.z2
        
        
        
    def updaterealcubes(self, cube):

        nrc = []

        nein=False
        
        for c in self.reactor:
            print ("------------------------------\nchecking "+str(c)+" vs "+str(cube))
            # find if the cube kills or splits any existing cubes

            # if the cubes do not interact at all, do nothing
            if c.x2<cube.x1 or c.x1>cube.x2 or c.y2<cube.y1 or c.y1>cube.y2 or c.z2<cube.z1 or c.z1>cube.z2:
                #print (str(cube) + " does not overlap " + str(c))
                if c.state=="on":
                    nrc.append(c)
                continue

            # existing cube c is fully overlapped by new cube cube, remove existing cube c (regardless of if the new is on or off)
            if self.coverlap(c, cube):
                print (str(cube)+ " kills "+str(c) + " completely")
                continue

            # existing cube c fully overlaps the new cube cube. If the new cube is on, dump the new cube, it isn't needed
            if cube.state=="on" and (cube.x1>=c.x1 and cube.x2<=c.x2 and cube.y1>=c.y1 and cube.y2<=c.y2 and cube.z1>=c.z1 and cube.z2<=c.z2):
                #print (str(cube) + " is completely overlapped by "+str(c))

                if c.state=="on":
                    nein=True
                    nrc.append(c)
                break
            
            #print ("Checking for overlap between "+str(cube)+" and "+str(c))
            L = self.checkforintersection(c, cube)
            if not L is None:
                nrc = nrc + L

        #print("I got here for some reason: "+str(len(self.realcubes)))

        # all cubes in realcubes are "on"
        if cube.state == "on" and not nein:
            nrc.append(cube)
        #else:
        #    print ("Dropped "+str(cube)+" due to complete overlap or being an off cube")
        self.realcubes = nrc
        self.thesize = 0
        for i in nrc:
            self.thesize+=i.size()

        #print ("\n")
            
    def size(self):
        return self.thesize
                
    def __add__(self, cube):
        # b0rked
        #self.updaterealcubes(cube)

        for i in range(len(self.reactor)-1,-1,-1):
            # if a cube is completely covered, it can be removed
            # regardless of if it is set or not set
            if self.coverlap(cube, self.reactor[i]):
                self.reactor.pop(i)
        
        self.reactor.append(cube)
        
        return self
    
    def __repr__(self):

        return str(self.reactor)
    
# ---

def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:

        l = l.strip()

        b = Box(l)
        RR = RR + b

    return RR
        
        
RR = readinaTOR()

import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#R = Reactor()
#R = R + Box("on x=1..3,y=1..3,z=1..3")
#R = R + Box("off x=3..3,y=1..1,z=3..3")



# c=0
# ax = plt.figure().add_subplot(projection='3d')

# for i in R.realcubes:
#     c+=1
#     print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1)
#     n_voxels = np.zeros((15,15,15), dtype=bool)
#     for x in range(i.x1, i.x2):
#         for y in range(i.y1, i.y2):
#             for z in range(i.z1, i.z2):
#                 n_voxels[x,y,z]=True
#     ax.voxels(n_voxels)
#     plt.savefig("reactor"+str(c)+".png")

                    
# # #facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
# # #edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')



#ax = plt.figure().add_subplot(projection='3d')

n_voxels = np.zeros((110,110,110), dtype=bool)
print ("(master)")
c=0
for i in RR.reactor:
    c+=1
    print(i," - ",i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1, i.state=="on")
    for x in range(max(-50,i.x1), min(51,i.x2)):
        for y in range(max(-50,i.y1), min(51,i.y2)):
            for z in range(max(-50,i.z1), min(51,i.z2)):
                   if i.state=="on":
                       n_voxels[x+50,y+50,z+50]=True
                   else:
                       n_voxels[x+50,y+50,z+50]=False

#print("borkaborka")
#ax.voxels(n_voxels)
#plt.savefig("reactorMaster"+str(c)+".png")


print(sum(sum(sum(n_voxels))))
