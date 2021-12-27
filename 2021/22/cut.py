from box import Box

# return true if c1 and c2 are touching
def collision(c1, c2):

    if c1.x2 < c2.x1:
        return False

    if c1.x1 > c2.x2:
        return False


    if c1.y2 < c2.y1:
        return False

    if c1.y1 > c2.y2:
        return False

    if c1.z2 < c2.z1:
        return False

    if c1.z1 > c2.z2:
        return False

    return True

# remove the overlapping parts between c1 and c2 from c2
def dothecut(c1, c2):
    # c1 is the new cube
    
    # check if c2 is completely inside c1 on the x axis
    if c1.x2<c2.x2 and c1.x1>c2.x1:
        # split c2 in two parts before doing the cuts
        newx = (c2.x2-c2.x1)//2+c2.x1
        c2a = Box([c2.state,c2.x1,newx, c2.y1,c2.y2, c2.z1,c2.z2])
        c2b = Box([c2.state,newx+1,c2.x2, c2.y1,c2.y2, c2.z1,c2.z2])

        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # check if c2 is completely inside c1 on the y axis
    if c1.y2<c2.y2 and c1.y1>c2.y1:
        # split c2 in two parts before doing the cuts
        newy = (c2.y2-c2.y1)//2+c2.y1
        c2a = Box([c2.state,c2.x1,c2.x2, c2.y1,newy, c2.z1,c2.z2])
        c2b = Box([c2.state,c2.x1,c2.x2, newy+1,c2.y2, c2.z1,c2.z2])

        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # check if c2 is completely inside c1 on the z axis
    if c1.z2<c2.z2 and c1.z1>c2.z1:
        # split c2 in two parts before doing the cuts
        newz = (c2.z2-c2.z1)//2+c2.z1
        c2a = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, c2.z1,newz])
        c2b = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, newz+1,c2.z2])

        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # find the cut between the boxes and remove it from c2

    # food plz

    #print("remove",c1,"from",c2)
    c2 = cutapart(c2,c1)
    #print("result",c2)
    return c2

# check if cube c1 completely overlaps cube c2
def coverlap( c1, c2):
    return c2.x1>=c1.x1 and c2.x2<=c1.x2 and c2.y1>=c1.y1 and c2.y2<=c1.y2 and c2.z1>=c1.z1 and c2.z2<=c1.z2


# merge two cubes that are connected on the X side and return a new cube
    
def combinex(a,b):

    if a.state != b.state:
        return None
    
    if a.y1==b.y1 and a.y2==b.y2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.x2==b.x1:
                c = Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])
#                print("x merge",a,b,c)
                                
                return [c]
            
    else:
        return None

# merge two cubes that are connected on the Y side and return a new cube
    
def combiney(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.y2==b.y1:
                c = Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])
#                print("y merge",a,b,c)
                return [c]
            
    else:
        return None

# merge two cubes that are connected on the Z side and return a new cube
    
def combinez(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.y1==b.y1 and a.y2==b.y2:
            if a.z2==b.z1:
#                print("z merge",a,b)
                return [Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])]
            
    else:
        return None

def cutapart(c, cube):
    
    L = []
    
    #if c.state=="off":
    #    return L
    
    # find the cuts between the cubes
    
    #if cube.state=="off":
    #    print (str(cube) + " intersects " + str(c))
    
    # regardless of how we do this, we remove "cube" from "c", then we either add cube or not, depending on if it is on or off
    # if "cube" is fully covered by c in any dimension, we split c in whatevs parts first
    
    
    layer1 = True
    layer2 = True
    layer3 = True
    
    if layer1:
        # layer 1
        L.append(Box(["on",c.x1,cube.x1, c.y1,cube.y1, cube.z2,c.z2, "1A"])) # A
        L.append(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z2,c.z2, "1B"])) # B
        L.append(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z2,c.z2, "1C"])) # C
        L.append(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z2,c.z2, "1D"])) # D
        L.append(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, cube.z2,c.z2, "1E"])) # E
        L.append(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z2,c.z2, "1F"])) # F
        L.append(Box(["on",c.x1,cube.x1,cube.y2,c.y2, cube.z2,c.z2, "1G"])) # G
        L.append(Box(["on",cube.x1, cube.x2, cube.y2,c.y2, cube.z2,c.z2, "1H"])) # H
        L.append(Box(["on",cube.x2, c.x2, cube.y2,c.y2, cube.z2,c.z2, "1I"])) # I
                
    if layer2:
        # layer 2
        L.append(Box(["on",c.x1,cube.x1,c.y1,cube.y1, cube.z1,cube.z2])) # A
        L.append(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z1,cube.z2])) # B
        L.append(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z1,cube.z2])) # C
        L.append(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z1,cube.z2])) # D
        L.append(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z1,cube.z2])) # F
        L.append(Box(["on",c.x1,cube.x1,cube.y2, c.y2, cube.z1,cube.z2])) # G
        L.append(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, cube.z1,cube.z2])) # H
        L.append(Box(["on",cube.x2,c.x2, cube.y2,c.y2, cube.z1,cube.z2])) # I
                
    if layer3:
        # layer 3
        L.append(Box(["on",c.x1,cube.x1, c.y1,cube.y1, c.z1,cube.z1])) # A
        L.append(Box(["on",cube.x1,cube.x2, c.y1,cube.y1, c.z1,cube.z1])) # B
        L.append(Box(["on",cube.x2,c.x2, c.y1,cube.y1, c.z1,cube.z1])) # C
        L.append(Box(["on",c.x1,cube.x1, cube.y1,cube.y2, c.z1,cube.z1])) # D 
        L.append(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, c.z1,cube.z1])) # E
        L.append(Box(["on",cube.x2,c.x2, cube.y1,cube.y2, c.z1,cube.z1])) # F
        L.append(Box(["on",c.x1,cube.x1, cube.y2,c.y2, c.z1,cube.z1])) # G 
        L.append(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, c.z1,cube.z1])) #
        L.append(Box(["on",cube.x2,c.x2, cube.y2,c.y2, c.z1,cube.z1])) # I

    #print("all cuts",L)
    X = list(filter(lambda x:x.size()>0,L))
    #print("filtered cuts",X)
    #sss=0
    #for i in X:
    #    sss+=i.size()
    #print(sss)
    return X


