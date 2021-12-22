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

    def __add__(self, cube):

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

# code originally used to draw a picture
import numpy as np
n_voxels = np.zeros((110,110,110), dtype=bool)

for i in RR.reactor:

#    print(i," - ",i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1, i.state=="on")
    for x in range(max(-50,i.x1), min(51,i.x2)):
        for y in range(max(-50,i.y1), min(51,i.y2)):
            for z in range(max(-50,i.z1), min(51,i.z2)):
                   if i.state=="on":
                       n_voxels[x+50,y+50,z+50]=True
                   else:
                       n_voxels[x+50,y+50,z+50]=False

print(sum(sum(sum(n_voxels))))
