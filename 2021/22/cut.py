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
        c2b = Box([c2.state,c2.x1,c2.x2, newy,c2.y2, c2.z1,c2.z2])

        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # check if c2 is completely inside c1 on the z axis
    if c1.z2<c2.z2 and c1.z1>c2.z1:
        # split c2 in two parts before doing the cuts
        newz = (c2.z2-c2.z1)//2+c2.z1
        c2a = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, c2.z1,newz])
        c2b = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, newx,c2.z2])

        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # find the cut between the boxes and remove it from c2

    return c2
    

    
    
        
