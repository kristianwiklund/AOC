#!/usr/bin/python3

import sys
import cut
from box import Box
from reactor import Reactor
from termcolor import colored

# -- assert helper
def check(what,output,f=None):
    try:
        assert(what)
    except:
        print("Assert failed, debug output: ",end="")
        print(output)
        if f is not None:
            f()
        sys.exit()

# -- end assert helper

# --- test cases

print (colored("Testcase 1: adding two identical boxes results in only one box","red"))
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")

print (colored("Testcase 2: adding various boxes that overlap but are on the edge with the first, also result in only one box","red"))
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")

print (colored("        2a: check that adding sliver on x doesn't cause more boxes","yellow"))
R += Box("on x=1..1,y=1..3,z=1..3")
check(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]",[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

print (colored("        2c: check that adding sliver on z doesn't cause more boxes ","yellow"))
R += Box("on x=1..3,y=1..3,z=1..1")
check(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]",[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

print (colored("        2b: check that adding sliver on y doesn't cause more boxes","yellow"))
R += Box("on x=1..3,y=1..1,z=1..3")
check(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]",[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())




print (colored("Testcase 3: merge on X edge"),"red")
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

print ("Testcase 7: merge on (reverse) Y edge")
R += Box("on x=1..3,y=1..1,z=2..3")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=2..3]")

print ("Testcase 8: merge on (reverse) Z edge")
R += Box("on x=1..3,y=1..3,z=1..1")
assert(R.realcubes.__repr__()=="[on x=1..3,y=1..3,z=1..3]")

print (colored("Testcase 9a: Remove a 1x1x1 cube from a 3x3x3 cube","red"))
        
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.size()==27)
R += Box("off x=1..1,y=1..1,z=1..1")
check(R.size()==26,[R.size(),R.realcubes],f=lambda : R.savefig())

print (colored("Testcase 9b: Remove a 1x1x1 cube from a 3x3x3 cube","red"))
        
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.size()==27)
R += Box("off x=3..3,y=3..3,z=3..3")
check(R.size()==26,[R.size(),R.realcubes],f=lambda : R.savefig())


print (colored("Testcase 9c: Remove a 1x1x1 cube from a 3x3x3 cube","red"))
        
R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.size()==27)
R += Box("off x=2..2,y=2..2,z=2..2")
check(R.size()==26,[R.size(),R.realcubes],f=lambda : R.savefig())

print (colored("Testcase 10x: Remove a slab from the upper end of a slab","red"))

R = Reactor()
R += Box("on x=1..3,y=1..1,z=1..1")
assert(R.size()==3)
R += Box("off x=3..3,y=1..1,z=1..1")
check(R.size()==2,[R.size(),R.realcubes],f=lambda : R.savefig())


print (colored("Testcase 10y: Remove a slab from the upper end of a slab","red"))

R = Reactor()
R += Box("on x=1..1,y=1..3,z=1..1")
assert(R.size()==3)
R += Box("off x=1..1,y=3..3,z=1..1")
check(R.size()==2,[R.size(),R.realcubes],f=lambda : R.savefig())


print (colored("Testcase 10z: Remove a slab from the upper end of a slab","red"))

R = Reactor()
R += Box("on x=1..1,y=1..1,z=1..3")
assert(R.size()==3)
R += Box("off x=1..1,y=1..1,z=3..3")
check(R.size()==2,[R.size(),R.realcubes],f=lambda : R.savefig())

print (colored("Testcase 10xy: Remove a corner from the upper end of a slab","red"))

R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..1")
assert(R.size()==9)
R += Box("off x=3..3,y=3..3,z=1..1")
check(R.size()==8,[R.size(),R.realcubes],f=lambda : R.savefig())

print (colored("Testcase 10xy: Remove a corner from the upper end of a cube","red"))

R = Reactor()
R += Box("on x=1..3,y=1..3,z=1..3")
assert(R.size()==27)
R += Box("off x=3..3,y=3..3,z=3..3")
check(R.size()==26,[R.size(),R.realcubes],f=lambda : R.savefig())


print(colored("Testcase 11, deconstructed","green"))
R = Reactor()
# steps 11a and 11b results in these cubes
a=Box("on x=10..10,y=10..12,z=10..12")
a.id="[1]"
#b=Box("on x=11..12,y=10..10,z=10..12")
#b.id="[2]"
#c=Box("on x=11..12,y=11..12,z=10..10")
#c.id="[3]"
#d=Box("on x=11..13,y=11..13,z=11..13")
#d.id="[4]"
R+=a
#R+=b
#R+=c
#R+=d
# steps 11c removes a cube
e=Box("off x=9..11,y=9..11,z=9..11")
e.id="[5]"
R+=e
R.savefig()
sys.exit()


print (colored("Testcase 11 : First example from AOC","red"))

R=Reactor()
print ("         11a: Check that first cube is size 27")
a=Box("on x=10..12,y=10..12,z=10..12")
a.id="Box1"
R+=a
assert(R.size()==27)
b = Box("on x=11..13,y=11..13,z=11..13")
b.id = "Box2"
R+=b
print ("         11b: Check that merging two cubes result in the correct size ("+str(27+19)+")")
check(R.size()==27+19,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

c = Box("off x=9..11,y=9..11,z=9..11")
c.id = "Box3"
R+=c
print ("         11c: Check that removing a cube result in the correct size ("+str(27+19-8)+")")
check(R.size()==27+19-8,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

print ("         11d: Check that adding a cube result in the correct size ("+str(39)+")")
R+=Box("on x=10..10,y=10..10,z=10..10")
assert(R.size()==39)

sys.exit()

# - finally, read input from stdin and solve the problem

R = Reactor()

def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:
        l = l.strip()

        b = Box(l)
        RR = RR + b
        
    return RR
        
        

