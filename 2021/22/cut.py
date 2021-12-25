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

    return [c2]

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
                return [Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])]
            
    else:
        print ("combinex failed:",a,b)
        return None

# merge two cubes that are connected on the Y side and return a new cube
    
def combiney(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.z1==b.z1 and a.z2==b.z2:
            if a.y2==b.y1:
                return [Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])]
            
    else:
        print ("combiney failed:",a,b)
        return None

# merge two cubes that are connected on the Z side and return a new cube
    
def combinez(a,b):

    if a.state != b.state:
        return None
    
    if a.x1==b.x1 and a.x2==b.x2:
        if a.y1==b.y1 and a.y2==b.y2:
            if a.z2==b.z1:
                return [Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])]
            
    else:
        print ("combinez failed:",a,b)
        return None



    
    
        
