#!/usr/bin/python3

import sys

class Box:
    def __init__(self, l):

        def splitinaTOR(s):
            x = s.split("=")[1].split("..")
            return (int (x[0]), int(x[1]))
        
        x = l.split()

        state = x[0]
        y = x[1].split(",")
        
        self.state = state
        
        (l,r)=splitinaTOR(y[0])
        self.x1 = l
        self.x2 = r
        
        (l,r)=splitinaTOR(y[0])
        self.y1 = l
        self.y2 = r
        
        (l,r)=splitinaTOR(y[0])
        self.z1 = l
        self.z2 = r

    def __repr__(self):
        return self.state+" x="+str(self.x1)+".."+str(self.x2)+",y="+str(self.y1)+".."+str(self.y2)+",z="+str(self.z1)+".."+str(self.z2)

    def size(self):
        return (self.x2-self.x1+1)*(self.y2-self.y1+1)*(self.z2-self.z1+1)

class Reactor:
    def __init__(self):
        self.reactor=[]
        self.realcubes=[]
        self.thesize = 0

    def checkforintersection(self, c, cube):

        # find the cuts between the cubes

        print (str(cube) + " is intersecting " + str(c))

        # cases

        if 
        
        
        
    def updaterealcubes(self, cube):

        nrc = []

        # all cubes in realcubes are "on"
        
        for c in self.realcubes:
            # find if the cube kills or splits any existing cubes

            # if the cubes do not interact at all, do nothing
            if c.x2 < cube.x1 or c.x1 > cube.x2 or c.y2 < cube.y1 or c.y1 > cube.y2 or c.z2 < cube.z1 or c.z2 > cube.z2:
                print (str(cube) + " does not overlap " + str(c))
                continue

            # existing cube c is fully overlapped by new cube cube, remove existing cube c (regardless of if the new is on or off)
            if c.x1>=cube.x1 and c.x2<=cube.x2 and c.y1>=cube.y1 and c.y2<=cube.y2 and c.z1>=cube.z1 and c.z2<=cube.z2:
                print (str(cube)+ " kills "+str(c) + " completely")
                continue

            # existing cube c fully overlaps the new cube cube. If the new cube is on, dump the new cube, it isn't needed
            if cube.state=="on" and (cube.x1>=c.x1 and cube.x2<=c.x2 and cube.y1>=c.y1 and cube.y2<=c.y2 and cube.z1>=c.z1 and cube.z2<=c.z2):
                cube.state="off"
                nrc.append(c)
                break
                
            else:
                L = self.checkforintersection(c, cube)
                if not L is None:
                    nrc = nrc + L

        if cube.state == "on":
            nrc.append(cube)

        self.realcubes = nrc
        self.thesize = 0
        for i in nrc:
            self.thesize+=i.size()

    def size(self):
        return self.thesize
                
    def __add__(self, cube):
        
        self.reactor.append(cube)
        self.updaterealcubes(cube)
        
        return self
    
    def __repr__(self):

        return str(self.reactor)
    
# ---

def readinaTOR():

    L = []
    
    for l in sys.stdin:

        l = l.strip()

        b = Box(l)
        L.append(b)
        
        
readinaTOR()

# Tests

assert(str(Box("on x=10..12,y=10..12,z=10..12"))=="on x=10..12,y=10..12,z=10..12")
assert(Box("on x=10..12,y=10..12,z=10..12").size()==27)

R = Reactor()

R = R + Box("on x=10..12,y=10..12,z=10..12")

assert(R.realcubes.__repr__()=="[on x=10..12,y=10..12,z=10..12]")
assert(R.size()==27)

# test case 1: add a cube that is the exact size as the existing cube in the reactor
R = R + Box("on x=10..12,y=10..12,z=10..12")
assert(R.size()==27)

# test case 2: add a cube that is smaller on one side compared to the existing cube in the reactor
R = R + Box("on x=11..12,y=10..12,z=10..12")

assert(R.size()==27)



R = R + Box("on x=11..13,y=11..13,z=11..13")
assert(R.size()==19+27)

R = R + Box("off x=9..11,y=9..11,z=9..11")
assert(R.size()==19+27-8)

R = R + Box("on x=10..10,y=10..10,z=10..10")
assert(R.size()==39)
print(R)

