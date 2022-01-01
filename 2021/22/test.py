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

    print ("= selftest 3 started")
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

    print ("= selftest 4 started")
    R = Reactor()
            
    R+=Box("on x=1..4,y=1..4,z=1..4")
    R+=Box("off x=2..3,y=1..4,z=1..4")
    R.consistencycheck()

    R = Reactor()
    
    # this screws up things... what happens here?
    a=Box('on x=-27..23,y=-28..26,z=-21..29')
    b=Box("on x=-22..26,y=-27..20,z=-29..19")
    a.id="a"
    b.id="b"
    R+=a
    R+=b
    # vi tappar bort flaket som ligger mellan y=-28..-27
    # nya kuben är mindre än gamla i en av dimensionerna
    # check the on set vs the all set
    R.consistencycheck()

    
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
    R+=Box("on x=-22..26,y=-27..20,z=-29..19")
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

def example2():

    print ("= example 2 started")
    R = Reactor()
    
    R+=Box("on x=-5..47,y=-31..22,z=-19..33")
    R+=Box("on x=-44..5,y=-27..21,z=-14..35")
    R+=Box("on x=-49..-1,y=-11..42,z=-10..38")
    R+=Box("on x=-20..34,y=-40..6,z=-44..1")
    R+=Box("off x=26..39,y=40..50,z=-2..11")
    R+=Box("on x=-41..5,y=-41..6,z=-36..8")
    R+=Box("off x=-43..-33,y=-45..-28,z=7..25")
    R+=Box("on x=-33..15,y=-32..19,z=-34..11")
    R+=Box("off x=35..47,y=-46..-34,z=-11..5")
    R+=Box("on x=-14..36,y=-6..44,z=-16..29")
    R+=Box("on x=-57795..-6158,y=29564..72030,z=20435..90618")
    R+=Box("on x=36731..105352,y=-21140..28532,z=16094..90401")
    R+=Box("on x=30999..107136,y=-53464..15513,z=8553..71215")
    R+=Box("on x=13528..83982,y=-99403..-27377,z=-24141..23996")
    R+=Box("on x=-72682..-12347,y=18159..111354,z=7391..80950")
    R+=Box("on x=-1060..80757,y=-65301..-20884,z=-103788..-16709")
    R+=Box("on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856")
    R+=Box("on x=-52752..22273,y=-49450..9096,z=54442..119054")
    R+=Box("on x=-29982..40483,y=-108474..-28371,z=-24328..38471")
    R+=Box("on x=-4958..62750,y=40422..118853,z=-7672..65583")
    R+=Box("on x=55694..108686,y=-43367..46958,z=-26781..48729")
    R+=Box("on x=-98497..-18186,y=-63569..3412,z=1232..88485")
    R+=Box("on x=-726..56291,y=-62629..13224,z=18033..85226")
    R+=Box("on x=-110886..-34664,y=-81338..-8658,z=8914..63723")
    R+=Box("on x=-55829..24974,y=-16897..54165,z=-121762..-28058")
    R+=Box("on x=-65152..-11147,y=22489..91432,z=-58782..1780")
    R+=Box("on x=-120100..-32970,y=-46592..27473,z=-11695..61039")
    R+=Box("on x=-18631..37533,y=-124565..-50804,z=-35667..28308")
    R+=Box("on x=-57817..18248,y=49321..117703,z=5745..55881")
    R+=Box("on x=14781..98692,y=-1341..70827,z=15753..70151")
    R+=Box("on x=-34419..55919,y=-19626..40991,z=39015..114138")
    R+=Box("on x=-60785..11593,y=-56135..2999,z=-95368..-26915")
    R+=Box("on x=-32178..58085,y=17647..101866,z=-91405..-8878")
    R+=Box("on x=-53655..12091,y=50097..105568,z=-75335..-4862")
    R+=Box("on x=-111166..-40997,y=-71714..2688,z=5609..50954")
    R+=Box("on x=-16602..70118,y=-98693..-44401,z=5197..76897")
    R+=Box("on x=16383..101554,y=4615..83635,z=-44907..18747")
    R+=Box("off x=-95822..-15171,y=-19987..48940,z=10804..104439")
    R+=Box("on x=-89813..-14614,y=16069..88491,z=-3297..45228")
    R+=Box("on x=41075..99376,y=-20427..49978,z=-52012..13762")
    R+=Box("on x=-21330..50085,y=-17944..62733,z=-112280..-30197")
    R+=Box("on x=-16478..35915,y=36008..118594,z=-7885..47086")
    R+=Box("off x=-98156..-27851,y=-49952..43171,z=-99005..-8456")
    R+=Box("off x=2032..69770,y=-71013..4824,z=7471..94418")
    R+=Box("on x=43670..120875,y=-42068..12382,z=-24787..38892")
    R+=Box("off x=37514..111226,y=-45862..25743,z=-16714..54663")
    R+=Box("off x=25699..97951,y=-30668..59918,z=-15349..69697")
    R+=Box("off x=-44271..17935,y=-9516..60759,z=49131..112598")
    R+=Box("on x=-61695..-5813,y=40978..94975,z=8655..80240")
    R+=Box("off x=-101086..-9439,y=-7088..67543,z=33935..83858")
    R+=Box("off x=18020..114017,y=-48931..32606,z=21474..89843")
    R+=Box("off x=-77139..10506,y=-89994..-18797,z=-80..59318")
    R+=Box("off x=8476..79288,y=-75520..11602,z=-96624..-24783")
    R+=Box("on x=-47488..-1262,y=24338..100707,z=16292..72967")
    R+=Box("off x=-84341..13987,y=2429..92914,z=-90671..-1318")
    R+=Box("off x=-37810..49457,y=-71013..-7894,z=-105357..-13188")
    R+=Box("off x=-27365..46395,y=31009..98017,z=15428..76570")
    R+=Box("off x=-70369..-16548,y=22648..78696,z=-1892..86821")
    R+=Box("on x=-53470..21291,y=-120233..-33476,z=-44150..38147")
    R+=Box("off x=-93533..-4276,y=-16170..68771,z=-104985..-24507")

    s = sum([x.size() for x in R.realcubes])
    assert(s==2758514936282235)
    
    print ("= example 2 passed")
