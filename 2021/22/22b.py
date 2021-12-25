#!/usr/bin/python3

import sys
import cut
from box import Box


# what this is doing, I don't know
def ai(L, c):
    T = []
    for i in L:
        X = checkforoverlap(i, c)
        T=T+X

    return T
    
class Done(Exception):
    pass
    
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

            # if the new cube completely overlaps or is identical to an existing cube, we remove the existing cube
            if cut.coverlap(newcube, c):
                continue # that is, don't add anything and continue with the next turn in the loop
            
            # if the cubes do not collide, keep c in the realcubes list and continue with the next turn in the loop
            if not cut.collision(newcube, c):
                newrealcubes.append(c)
                continue

            # if we get here, we have some kind of collision
            L = cut.dothecut(newcube, c)

            newrealcubes = newrealcubes + L
            
        # once we have filtered the realcubes, we add the new cube, if it is an "on" cube
        if newcube.state == "on":
            newrealcubes.append(newcube)

        # we always add it to the list of cubes in the reactor (but not the realcubes)
        self.cubes.append(newcube)
        self.realcubes = newrealcubes

        if len(self.realcubes)<2:
            return self

        # try to merge the existing newrealcubes into smaller ones

        restart=True
        while restart:
            restart = False

            try:
                for i in range(len(self.realcubes)-1):
                    for j in range(i+1,len(self.realcubes)):
                        # if an "older" cube completely overlaps a newer cube, we remove the newer cube. this works because realcubes only contain the "on" set
                        if cut.coverlap(self.realcubes[i],self.realcubes[j]):
                            #print(i,j,cut.coverlap(self.realcubes[i],self.realcubes[j]),self.realcubes[i],"removes",self.realcubes[j],"due to 100% overlap")
                            self.realcubes.pop(j)
                            X=[]
                            raise Done

                        X = cut.combinex(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combiney(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combinez(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done

                        X = cut.combinex(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combiney(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combinez(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done                        

            except Done:

                self.realcubes+=X
                restart = True

            except:
                import traceback
                print(traceback.format_exc())
                print(sys.exc_info()[2])
                sys.exit()

        # and return the result of the addition
        return self
        

    # pretty print
    def __repr__(self):
        return str(self.cubes)
    
# --- test cases

print ("Testcase 1: adding two identical boxes results in only one box")
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")

print ("Testcase 2: adding various boxes that overlap but are on the edge with the first, also result in only one box")
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
R += Box("on x=1..1,y=1..3,z=1..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")
R += Box("on x=1..3,y=1..1,z=1..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")
R += Box("on x=1..3,y=1..3,z=1..1")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")


print ("Testcase 3: merge on X edge")
R = Reactor()

R += Box("on x=1..1,y=1..1,z=1..1")
R += Box("on x=2..3,y=1..1,z=1..1")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..1,z=1..1]")

print ("Testcase 4: merge on Y edge")
R += Box("on x=1..3,y=2..3,z=1..1")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..1]")

print ("Testcase 5: merge on Z edge")
R += Box("on x=1..3,y=1..3,z=2..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")

print ("Testcase 6: merge on (reverse) X edge")
R = Reactor()

R += Box("on x=2..3,y=2..3,z=2..3")
R += Box("on x=1..1,y=2..3,z=2..3")

assert(R.realcubes.__repr__()=="[on x=1..3,y=2..3,z=2..3]")

print ("Testcase 4: merge on (reverse) Y edge")
R += Box("on x=1..3,y=1..1,z=2..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=2..3]")

print ("Testcase 5: merge on (reverse) Z edge")
R += Box("on x=1..3,y=1..3,z=1..1")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")

# #read from stdin, create a reactor
def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:

        l = l.strip()

        b = Box(l)

        RR = RR + b
        
    return RR
        
        
RR = readinaTOR()
print(len(RR.cubes),len(RR.realcubes))
