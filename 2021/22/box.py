class OverlapError(Exception):
    pass

class Box:

    # constructor can either create a cube from the string in the input, or from a list representing a cube
    
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
            self.x1 = l[1] #min(l[1],l[2])
            self.x2 = l[2] #max(l[1],l[2])
            self.y1 = l[3] #min(l[3],l[4])
            self.y2 = l[4] #max(l[3],l[4])
            self.z1 = l[5] #min(l[5],l[6])
            self.z2 = l[6] #max(l[5],l[6])

            if len(l)==8:
                self.id = l[7]
            else:
                self.id=None
                
            #print("Created",self)

    # to pretty print a cube
    
    def __repr__(self):
        s= self.state+" x="+str(self.x1)+".."+str(self.x2-1)+",y="+str(self.y1)+".."+str(self.y2-1)+",z="+str(self.z1)+".."+str(self.z2-1)
#        if self.id:
#            s = s + " = "+str(self.size())
#            s = s + " ("+self.id+")"
        return s

    # calculate the size of a cube

    def size(self):
        xs = (self.x2-self.x1)
        ys = (self.y2-self.y1)
        zs = (self.z2-self.z1)

        #        print((self.x2-self.x1),(self.y2-self.y1),(self.z2-self.z1))
        s = abs(zs*ys*xs) * (-1 if (zs<0 or ys<0 or xs <0) else 1)
        
        return s

    # returns true if this cube completely covers "other" cube
    def covers(self, other):

        if other.x1 >= self.x1 and other.x2 <= self.x2:
            if other.y1 >= self.y1 and other.y2 <= self.y2:
                if other.z1 >= self.z1 and other.z2 <= self.z2:
                    return True

        return False

    # true, if in the same range on x
    def inxrange(self, other):

        if self.x2 <= other.x1:
            return False

        if self.x1 >= other.x2:
            return False

        return True

    # true, if in the same range on y
    def inyrange(self, other):

        if self.y2 <= other.y1:
            return False

        if self.y1 >= other.y2:
            return False

        return True

    # true, if in the same range on z
    def inzrange(self, other):

        if self.z2 <= other.z1:
            return False

        if self.z1 >= other.z2:
            return False

        return True

    
    
    # return true if c1 and other are touching
    def touches(self, other):
        return self.inxrange(other) and self.inyrange(other) and self.inzrange(other)

    def __eq__(self,other):

        return self.state==other.state and self.x1 == other.x1 and self.x2 == other.x2 and self.y1==other.y1 and self.y2==other.y2 and self.z1==other.z1 and self.z2==other.z2

    def __add__(self,other):
        return [self,other]
    
    # remove other from self. Returns an unoptimized list of Box with the parts covered by other removed
    def __sub__(self, other):


        # if the boxes do not touch, return self
        if not self.touches(other):
            return [self]
        
        # assumption: self is always smaller than other

        #if self.covers(other):
        #    raise OverlapError

        # we completely cover self, return the empty list, nothing remains
        if other.covers(self):
            return []

        # when we get here, we have a number of possible scenarios

        # complete overlap on two sides, but skewed on one. this means that we cut off one single slab
        # partial overlap on all sides, this means that we cut out one single slab plus two on the sides

        completex = other.x1 <= self.x1 and other.x2 >= self.x2
        completey = other.y1 <= self.y1 and other.y2 >= self.y2
        completez = other.z1 <= self.z1 and other.z2 >= self.z2

        # we have complete overlap in xy, partial in z
        if completex and completey:
            # return either higher slab or lower slab
            if other.z1 <= self.z1:
                return [Box([self.state, self.x1, self.x2, self.y1, self.y2, other.z2, self.z2, "LowerZ"])]
            else:
                return [Box([self.state, self.x1, self.x2, self.y1, self.y2, self.z1, other.z1, "HigherZ"])]
            
        # we have complete overlap in xz, partial in y
        if completex and completez:
            # return either higher slab or lower slab
            if other.y1 <= self.y1:
                return [Box([self.state, self.x1, self.x2, other.y2, self.y2, self.z1, self.z2, "LowerY"])]
            else:
                return [Box([self.state, self.x1, self.x2, self.y1, other.y1, self.z1, self.z2, "HigherY"])]


        # we have complete overlap in yz, partial in x
        if completey and completez:
            # return either higher slab or lower slab
            if other.x1 <= self.x1:
                return [Box([self.state, other.x2, self.x2, self.y1, self.y2, self.z1, self.z2, "LowerX"])]
            else:
                return [Box([self.state, self.x1, other.x1, self.y1, self.y2, self.z1, self.z2, "HigherX"])]


        # now for the trickier parts. we need to cut a corner off self
        # this can be broken down in several steps


        L=[]

        # step one, cut the box in two parts z-wise. 
        
        new1 = Box([self.state, self.x1, self.x2, self.y1, self.y2, other.z2, self.z2, "LowerZ"]) #- other
        new2 = Box([self.state, self.x1, self.x2, self.y1, self.y2, self.z1, other.z1, "HigherZ"])# - other

        # one of these will have a zero size. that is the one where we collide
        # we keep the non-zero one, and subtract it from self to get the slab where we need to continue working
        # (that subtraction is trivial)
        if new1.size()<=0:
            L.append(new2)
            keep = (self-new2)[0]
        else:
            L.append(new1)
            keep = (self-new1)[0]

        # step 2, do the same thing with "keep" as with "self", but in the y axis
        
        new1 = Box([self.state, self.x1, self.x2, other.y2, self.y2, self.z1, self.z2, "LowerY"])
        new2 = Box([self.state, self.x1, self.x2, self.y1, other.y1, self.z1, self.z2, "HigherY"])

        # one of these will have a zero size. that is the one where we collide
        # we keep the non-zero one, and subtract it from self to get the slab where we need to continue working
        # (that subtraction is trivial)
        if new1.size()<=0:
            L.append(new2)
            keep = (self-new2)[0]
        else:
            L.append(new1)
            keep = (self-new1)[0]

        # test
        L.append(keep)
            
        return L
