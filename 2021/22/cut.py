from box import Box
from reactor import Reactor

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
        #print ("split",c2,"in the x axis")
        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # check if c2 is completely inside c1 on the y axis
    if c1.y2<c2.y2 and c1.y1>c2.y1:
        # split c2 in two parts before doing the cuts
        newy = (c2.y2-c2.y1)//2+c2.y1
        c2a = Box([c2.state,c2.x1,c2.x2, c2.y1,newy, c2.z1,c2.z2])
        c2b = Box([c2.state,c2.x1,c2.x2, newy+1,c2.y2, c2.z1,c2.z2])
        #print ("split",c2,"in the y axis")
        return dothecut(c1,c2a)+dothecut(c1,c2b)

    # check if c2 is completely inside c1 on the z axis
    if c1.z2<c2.z2 and c1.z1>c2.z1:
        # split c2 in two parts before doing the cuts
        newz = (c2.z2-c2.z1)//2+c2.z1
        c2a = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, c2.z1,newz])
        c2b = Box([c2.state,c2.x1,c2.x2, c2.y1,c2.y2, newz+1,c2.z2])
        #print ("split",c2,"in the z axis")
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
                if a.id != None and b.id != None:
                    c = Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2,a.id+"+"+b.id])
                else:
                    c = Box([a.state,a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])
                #print("x merge",a,b,c)
                                
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
                if a.id != None and b.id != None:
                    c = Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2,a.id+"+"+b.id])
                else:
                    c = Box([a.state,a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])
                #print("y merge",a,b,c)
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
                if a.id != None and b.id != None:
                    c = Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2,a.id+"+"+b.id])
                else:
                    c = Box([a.state,a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])
                #print("z merge",a,b,c)
                return [c]
            
    else:
        return None

def cutapart(c, cube):
    

    cx1 = c.x1
    cx2 = c.x2
    cy1 = c.y1
    cy2 = c.y2
    cz1 = c.z1
    cz2 = c.z2
    
    if c.id is None:
        c.id=""

        
    #if c.state=="off":
    #    return L
    
    # find the cuts between the cubes
    
    #if cube.state=="off":
    #    print (str(cube) + " intersects " + str(c))
    
    # regardless of how we do this, we remove "cube" from "c", then we either add cube or not, depending on if it is on or off
    # if "cube" is fully covered by c in any dimension, we split c in whatevs parts first
    

    # when we get here, the cubes have been split to overlap in one of the corners
    # this means that we need to retain the three slabs of "c" that are outside "cube"

    # slab covering the x side of cube
    if cx1 < cube.x1:
        xb = (Box([c.state,cx1,cube.x1,cy1,c.y2,cz1,cz2,c.id+" XLOW"]))
        cx1 = cube.x1
    else:
        xb = (Box([c.state,cube.x2,cx2,cy1,c.y2,cz1,cz2,c.id+" XHIGH"]))
        cx2 = cube.x2
        
    # slab covering the y side of cube. we have an overlap between X and this, that is known
    # hence, we need to remove the X value
    if cy1 < cube.y1:
        yb = (Box([c.state,cx1,cx2,cy1,cube.y1,cz1,cz2,"YLOW"]))
        cy1 = cube.y1
    else:
        yb = (Box([c.state,cx1,cx2,cube.y2,cy2,cz1,cz2,"YHIGH"]))
        cy2 = cube.y2

    # slab covering the z side of cube. again, overlap with previous, etc
    if cz1 < cube.z1:
        zb = (Box([c.state,cx1,cx2,cy1,cy2,cz1,cube.z1,"ZLOW"]))
    else:
        # b0rked
        zb = (Box([c.state,cx1,cx2,cy1,cy2,cube.z2,cz2,"ZHIGH"]))
        
    L = [xb,yb,zb]
       
    X = list(filter(lambda x:x.size()>0,L))
    if len(X)!=len(L):
        print("filtered cuts",X,[x.id for x in X])
    else:
        print("all cuts",L,[x.id for x in X])

    sss=0
    #for i in X:
    #    sss+=i.size()
    #    print(sss)
    
    return L


