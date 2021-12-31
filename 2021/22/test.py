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

def first():
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


    print (colored("Testcase 10x-x: Remove a smaller part of the blob","red"))
    R = Reactor()
    R+= Box("on x=1..4,y=1..1,z=1..1")
    R+= Box("off x=2..3,y=1..1,z=1..1")
    check(R.size()==2,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

    print (colored("Testcase 10y-y: Remove a smaller part of the blob","red"))
    R = Reactor()
    R+= Box("on x=1..1,y=1..4,z=1..1")
    R+= Box("off x=1..1,y=2..3,z=1..1")
    check(R.size()==2,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())


    print (colored("Testcase 10z-z: Remove a smaller part of the blob","red"))
    R = Reactor()
    R+= Box("on x=1..1,y=1..1,z=1..4")
    R+= Box("off x=1..1,y=1..1,z=2..3")
    check(R.size()==2,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

    # -----------------

    print (colored("Testcase 10xyz: Remove a part of a blob","red"))
    # off x=9..11,y=9..11,z=9..11 from on x=10..10,y=10..12,z=10..12
    R = Reactor()
    R+=Box("on x=10..10,y=10..12,z=10..12")
    R+=Box("off x=9..11,y=9..11,z=9..11")
    check(R.size()==5,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())

    # -----------------

def second():
    # tests for complete overlap on 2 axes
    # test Z
    a = Box("on x=2..4,y=2..4,z=2..4")
    b = Box("off x=1..4,y=1..4,z=-12..2")
    v = a-b
    assert (v[0] == Box("on x=2..4,y=2..4,z=3..4"))
    
    a = Box("on x=1..4,y=1..4,z=1..4")
    b = Box("off x=1..4,y=1..4,z=3..4")
    v = a-b
    assert (v[0] == Box("on x=1..4,y=1..4,z=1..2"))
    
    # test X
    a = Box("on x=1..4,y=1..4,z=1..4")
    b = Box("off x=-12..2,y=1..4,z=1..4")
    v = a-b
    assert (v[0] == Box("on x=3..4,y=1..4,z=1..4"))
    
    a = Box("on x=1..4,y=1..4,z=1..4")
    b = Box("off x=3..12,y=1..4,z=1..4")
    v = a-b
    assert (v[0] == Box("on x=1..2,y=1..4,z=1..4"))
    
    # test y
    
    a = Box("on x=1..4,y=1..4,z=1..4")
    b = Box("off x=1..4,y=-12..2,z=1..4")
    v = a-b
    assert (v[0] == Box("on x=1..4,y=3..4,z=1..4"))
    
    a = Box("on x=1..4,y=1..4,z=1..4")
    b = Box("off x=1..4,y=3..12,z=1..4")
    v = a-b
    assert (v[0] == Box("on x=1..4,y=1..2,z=1..4"))

    a = Box("on x=-20..26,y=-36..17,z=-47..7")
    b = Box("on x=-20..33,y=-21..23,z=-26..28") # = [on x=-20..26,y=-36..17,z=-47..-27, on x=-20..26,y=-36..-22,z=-26..7]
    v = a-b
    assert(sum([x.size() for x in v+[b]])==210918)

    print ("= selftest 2 passed")
    

def third():
    
    R=Reactor()
    a=Box("on x=10..12,y=10..12,z=10..12")
    a.id="Box1"
    R+=a
    assert(R.size()==27)
    b = Box("on x=11..13,y=11..13,z=11..13")
    b.id = "Box2"
    R+=b

    check(R.size()==27+19,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig())
    
    c = Box("off x=9..11,y=9..11,z=9..11")
    c.id = "Box3"
    R+=c

    check(R.size()==27+19-8,[R.size(),R.realcubes,[i.size() for i in R.realcubes]],f=lambda : R.savefig(colliding=True))
    

    R+=Box("on x=10..10,y=10..10,z=10..10")
    assert(R.size()==39)

    print ("= selftest 3 passed")
        
def fourth():

    R = Reactor()
    R.debug=True
            
    R+=Box("on x=1..4,y=1..4,z=1..4")
    R+=Box("on x=2..3,y=1..4,z=1..4")
    R.savefig()
    R.consistencycheck()
    
    R = Reactor()
    

    # this screws up things... what happens here?
    R+=Box('on x=-27..23,y=-28..26,z=-21..29')
    R+=Box("on x=-22..26,y=-27..20,z=-29..19")
    # vi tappar bort flaket som ligger mellan y=-28..-27
    # nya kuben är mindre än gamla i en av dimensionerna
    # check the on set vs the all set
    R.savefig()
    R.consistencycheck()
    R.debug=False

    
    R = Reactor()
    R+=Box("on x=-20..26,y=-36..17,z=-47..7")
    R+=Box("on x=-20..33,y=-21..23,z=-26..28")
    R+=Box("on x=-22..28,y=-29..23,z=-38..16")
    R+=Box("on x=-46..7,y=-6..46,z=-50..-1")
    R+=Box("on x=-49..1,y=-3..46,z=-24..28")
    R+=Box("on x=2..47,y=-22..22,z=-23..27")
    R+=Box("on x=-27..23,y=-28..26,z=-21..29")
    R+=Box("on x=-39..5,y=-6..47,z=-3..44")
    R+=Box("on x=-30..21,y=-8..43,z=-13..34")
    # check the on set vs the all set
    R.consistencycheck()
    R.debug=True
    # this screws up things... what happens here?
    R+=Box("on x=-22..26,y=-27..20,z=-29..19")
    # check the on set vs the all set
    R.consistencycheck()
    
    R+=Box("off x=-48..-32,y=26..41,z=-47..-37")
    R+=Box("on x=-12..35,y=6..50,z=-50..-2")
    R+=Box("off x=-48..-32,y=-32..-16,z=-15..-5")
    R+=Box("on x=-18..26,y=-33..15,z=-7..46")
    R+=Box("off x=-40..-22,y=-38..-28,z=23..41")
    R+=Box("on x=-16..35,y=-41..10,z=-47..6")
    R+=Box("off x=-32..-23,y=11..30,z=-14..3")
    R+=Box("on x=-49..-5,y=-3..45,z=-29..18")
    R+=Box("off x=18..30,y=-20..-8,z=-3..13")
    R+=Box("on x=-41..9,y=-7..43,z=-33..15")

    # check for the correct size of things
    nx = R.drawallblobs()
    
    assert(sum(sum(sum(nx))) == R.size())
    
    assert(R.size()==590784)
    print("= selftest 4 passed")
    return R


