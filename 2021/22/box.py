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
            self.x1 = min(l[1],l[2])
            self.x2 = max(l[1],l[2])
            self.y1 = min(l[3],l[4])
            self.y2 = max(l[3],l[4])
            self.z1 = min(l[5],l[6])
            self.z2 = max(l[5],l[6])

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
