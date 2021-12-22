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

def combinex(a,b):

    if a.state != b.state:
        return None
    
    if a.y1==b.y1 and a.y2==b.y2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.x2==b.x1:
                return Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])
            
    else:
        return None

def combiney(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.y2==b.y1:
                return Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])
            
    else:
        return None

def combinez(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.y1==b.y1 and a.y2==b.y2:
            if a.z2==b.z1:
                return Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])
            
    else:
        return None

# cube completely overlaps c
def coverlap( cube, c):
        
    return c.x1>=cube.x1 and c.x2<=cube.x2 and c.y1>=cube.y1 and c.y2<=cube.y2 and c.z1>=cube.z1 and c.z2<=cube.z2

    
def checkforoverlap(c, cube):
    
    L = []
    
    if c.state=="off":
        return L
    
    # find the cuts between the cubes
    
    #if cube.state=="off":
    #    print (str(cube) + " intersects " + str(c))
    
    # regardless of how we do this, we remove "cube" from "c", then we either add cube or not, depending on if it is on or off
    
    layer1 = True
    layer2 = True
    layer3 = True
    
    if layer1:
        # layer 1
        TB=(Box(["on",c.x1,cube.x1, c.y1,cube.y1, cube.z2,c.z2, "1A"])) # A
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z2,c.z2, "1B"])) # B
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z2,c.z2, "1C"])) # C
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z2,c.z2, "1D"])) # D
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, cube.z2,c.z2, "1E"])) # E
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z2,c.z2, "1F"])) # F
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",c.x1,cube.x1,cube.y2,c.y2, cube.z2,c.z2, "1G"])) # G
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1, cube.x2, cube.y2,c.y2, cube.z2,c.z2, "1H"])) # H
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2, c.x2, cube.y2,c.y2, cube.z2,c.z2, "1I"])) # I
        if not coverlap(cube, TB):
            L.append(TB)
                
    if layer2:
        # layer 2
        TB=(Box(["on",c.x1,cube.x1,c.y1,cube.y1, cube.z1,cube.z2])) # A
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z1,cube.z2])) # B
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z1,cube.z2])) # C
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z1,cube.z2])) # D
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z1,cube.z2])) # F
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",c.x1,cube.x1,cube.y2, c.y2, cube.z1,cube.z2])) # G
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, cube.z1,cube.z2])) # H
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2,c.x2, cube.y2,c.y2, cube.z1,cube.z2])) # I
        if not coverlap(cube, TB):
            L.append(TB)
                
    if layer3:
        # layer 3
        TB=(Box(["on",c.x1,cube.x1, c.y1,cube.y1, c.z1,cube.z1])) # A
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1,cube.x2, c.y1,cube.y1, c.z1,cube.z1])) # B
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2,c.x2, c.y1,cube.y1, c.z1,cube.z1])) # C
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",c.x1,cube.x1, cube.y1,cube.y2, c.z1,cube.z1])) # D 
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, c.z1,cube.z1])) # E
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2,c.x2, cube.y1,cube.y2, c.z1,cube.z1])) # F
        if not coverlap(cube, TB):
            L.append(TB)            
        TB=(Box(["on",c.x1,cube.x1, cube.y2,c.y2, c.z1,cube.z1])) # G 
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, c.z1,cube.z1])) #
        if not coverlap(cube, TB):
            L.append(TB)
        TB=(Box(["on",cube.x2,c.x2, cube.y2,c.y2, c.z1,cube.z1])) # I
        if not coverlap(cube, TB):
            L.append(TB)
                
        #print("Remaining of ",str(c)," is ",sum(S)," blocks")
        X = list(filter(lambda x:x.size()>0,L))
        #if cube.state=="off":
        #    print(X,len(X))

        #    print ([(x,x.size()) for x in X])
        
        #P = list(filter(lambda x:x.size()<=0,L))
        #print(P,len(P))

        return X
    
def ai(L, c):

    T = []
    for i in L:
        X = checkforoverlap(i, c)
        T=T+X

    return T
    

    
    
class Reactor:
    def __init__(self):
        self.reactor=[]
        self.realcubes=[]
        self.thesize = 0

            
    def size(self):
        return self.thesize

    def __add__(self, cube):
        # b0rked
        #self.updaterealcubes(cube)
        rl = len(self.reactor)
        
        for i in range(rl-1,-1,-1):
            # if a _previous cube_ is completely covered by the _new_ cube, it can be removed
            # regardless of if it is set or not set
            if coverlap(cube, self.reactor[i]):
                #print ("kill ",self.reactor[i])                                
                self.reactor.pop(i)
                continue
                       
            x = combinex(cube,self.reactor[i])
            if x is not None:
                #print ("xkill ",self.reactor[i])
                self.reactor.pop(i)

                cube = x
                continue
            
            y = combiney(cube,self.reactor[i])
            if y is not None:
                #print ("ykill ",self.reactor[i])
                self.reactor.pop(i)

                cube = y
                continue
            
            z = combinez(cube,self.reactor[i])
            if z is not None:
                #print ("zkill ",self.reactor[i])
                self.reactor.pop(i)
                cube = z

                continue

        if cube.state!="off":
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
        X = ai(RR.reactor, b)
        for x in X:
            RR = RR + x
        RR = RR + b
        print(l)
        

        
    return RR
        
        
RR = readinaTOR()

s=0
for r in RR.reactor:
    s+=r.size()

print(s)
