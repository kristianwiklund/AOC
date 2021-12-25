#!/usr/bin/python3

import sys
from cut import collision,dothecut
from box import Box

# merge two cubes that are connected on the X side and return a new cube
    
def combinex(a,b):

    if a.state != b.state:
        return None
    
    if a.y1==b.y1 and a.y2==b.y2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.x2==b.x1:
                return Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])
            
    else:
        return None

# merge two cubes that are connected on the Y side and return a new cube
    
def combiney(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.y2==b.y1:
                return Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])
            
    else:
        return None

# merge two cubes that are connected on the Z side and return a new cube
    
def combinez(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.y1==b.y1 and a.y2==b.y2:
            if a.z2==b.z1:
                return Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])
            
    else:
        return None

# check if cube c1 completely overlaps cube c2
def coverlap( c1, c2):
        
    return c2.x1>=c1.x1 and c2.x2<=c1.x2 and c2.y1>=c1.y1 and c2.y2<=c1.y2 and c2.z1>=c1.z1 and c2.z2<=c1.z2

# what this is doing, I don't know
def ai(L, c):
    T = []
    for i in L:
        X = checkforoverlap(i, c)
        T=T+X

    return T
    

    
# the reactor
class Reactor:

    # constructor
    def __init__(self):
        self.cubes=[]
        self.realcubes=[]
        self.thesize = 0

    # return the size of the reactor. Updated during "add"
    def size(self):
        return self.thesize

    
    
    # add a cube to the reactor and calculate what actually happened
    def __add__(self, newcube):
        
        # we have two lists of cubes. One is "realcubes" - the ones that are physically present
        # the other is the list of added cubes

        # when adding a cube, we check the impact on "realcubes"

        newrealcubes = []
        
        for c in self.realcubes:

            # if the new cube completely overlaps an existing cube, we remove the existing cube
            if coverlap(newcube, c):
                continue # that is, don't add anything and continue with the next turn in the loop

            # if the cubes do not collide, keep c in the realcubes list and continue with the next turn in the loop
            if not collision(newcube, c):
                newrealcubes.append(c)
                self.thesize+=newcube.size()
                continue

            # if we get here, we have some kind of collision
            L = dothecut(newcube, c)

            for i in L:
                newrealcubes.append(i)
                self.thesize+=i.size()
            
        # once we have filtered the realcubes, we add the new cube, if it is an "on" cube
        if newcube.state == "on":
            newrealcubes.append(newcube)
            self.thesize+=newcube.size()

        # we always add it to the list of cubes in the reactor (but not the realcubes)
        self.cubes.append(newcube)
        self.realcubes = newrealcubes
        
        # and return the result of the addition
        return self
        

    # pretty print
    def __repr__(self):

        return str(self.reactor)
    
# ---

#read from stdin, create a reactor
def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:

        l = l.strip()

        b = Box(l)

        RR = RR + b
        print(l)
        
    return RR
        
        
RR = readinaTOR()
print(RR)
