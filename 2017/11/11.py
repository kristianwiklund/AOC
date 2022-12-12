# everything one need to know about hextiles. https://www.redblobgames.com/grids/hexagons/

# we use flat top tiles arranged as double height
# assume that we represent the hextiles with cubes

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

class C():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,o):
        kotte=C(self.x,self.y)
        kotte.x+=o.x
        kotte.y+=o.y
        return kotte

    def __repr__(self):
        return "C"+str((self.x,self.y))
    
# that makes the moves like this
moves = {
    "nw":C(-1,0),
    "n":C(0,-1),
    "ne":C(1,-1),
    "e":C(2,0),
    "se":C(1,0),
    "s":C(0,1),
    "sw":C(-1,1),
    "w":C(-2,0)
    }


def axial_distance(o1, o2):
    return int((abs(o1.x - o2.x)
                + abs(o1.x + o1.y - o2.x - o2.y)
                + abs(o1.y - o2.y)) / 2)
        

def move(c,l):
    l = l.split(",")

    for i in l:
        c+=moves[i]
    return c


x1 = C(0,0)
x2 =x1+moves["ne"]+moves["ne"]+moves["ne"]



x2 = x1+moves["ne"]+moves["ne"]+moves["sw"]+moves["sw"]
assert((axial_distance(x1,x2))==0)

x2=move(x1,"ne,ne")
x2=move(x1,"s,s")
assert(axial_distance(x1,x2)==2)

with open("input.txt","r") as fd:
    arr = fd.readline().strip()

    x2 = move(x1,arr)
    print(x2)
    print(axial_distance(x1,x2))
