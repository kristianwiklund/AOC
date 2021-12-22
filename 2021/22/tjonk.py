    def checkforintersection(self, c, cube):

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
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z2,c.z2, "1B"])) # B
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z2,c.z2, "1C"])) # C
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z2,c.z2, "1D"])) # D
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, cube.z2,c.z2, "1E"])) # E
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z2,c.z2, "1F"])) # F
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",c.x1,cube.x1,cube.y2,c.y2, cube.z2,c.z2, "1G"])) # G
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1, cube.x2, cube.y2,c.y2, cube.z2,c.z2, "1H"])) # H
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2, c.x2, cube.y2,c.y2, cube.z2,c.z2, "1I"])) # I
            if not self.coverlap(cube, TB):
                L.append(TB)
                
        if layer2:
            # layer 2
            TB=(Box(["on",c.x1,cube.x1,c.y1,cube.y1, cube.z1,cube.z2])) # A
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1, cube.x2, c.y1,cube.y1, cube.z1,cube.z2])) # B
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2, c.x2, c.y1,cube.y1, cube.z1,cube.z2])) # C
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",c.x1,cube.x1,cube.y1,cube.y2, cube.z1,cube.z2])) # D
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",cube.x2,c.x2,cube.y1,cube.y2, cube.z1,cube.z2])) # F
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",c.x1,cube.x1,cube.y2, c.y2, cube.z1,cube.z2])) # G
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, cube.z1,cube.z2])) # H
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2,c.x2, cube.y2,c.y2, cube.z1,cube.z2])) # I
            if not self.coverlap(cube, TB):
                L.append(TB)
                
        if layer3:
            # layer 3
            TB=(Box(["on",c.x1,cube.x1, c.y1,cube.y1, c.z1,cube.z1])) # A
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1,cube.x2, c.y1,cube.y1, c.z1,cube.z1])) # B
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2,c.x2, c.y1,cube.y1, c.z1,cube.z1])) # C
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",c.x1,cube.x1, cube.y1,cube.y2, c.z1,cube.z1])) # D 
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1, cube.x2, cube.y1,cube.y2, c.z1,cube.z1])) # E
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2,c.x2, cube.y1,cube.y2, c.z1,cube.z1])) # F
            if not self.coverlap(cube, TB):
                L.append(TB)            
            TB=(Box(["on",c.x1,cube.x1, cube.y2,c.y2, c.z1,cube.z1])) # G 
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x1,cube.x2, cube.y2,c.y2, c.z1,cube.z1])) #
            if not self.coverlap(cube, TB):
                L.append(TB)
            TB=(Box(["on",cube.x2,c.x2, cube.y2,c.y2, c.z1,cube.z1])) # I
            if not self.coverlap(cube, TB):
                L.append(TB)
                
        #print("Remaining of ",str(c)," is ",sum(S)," blocks")
        X = list(filter(lambda x:x.size()>0,L))
        #if cube.state=="off":
        #    print(X,len(X))

        #    print ([(x,x.size()) for x in X])
        
        #P = list(filter(lambda x:x.size()<=0,L))
        #print(P,len(P))

        return X


        
            

            
            
        
