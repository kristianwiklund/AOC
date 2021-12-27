import cut
from box import Box

class Done(Exception):
    pass
    
# the reactor
class Reactor:

    # constructor
    def __init__(self):
        self.cubes=[]
        self.realcubes=[]
        self.thesize = 0

    # return the size of the reactor. Updated during "add"
    def size(self):
        return self.thesize

    def savefig(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import os
        import glob

        try:
            fl = glob.glob("realcubes*png")
            for fp in fl:
                try:
                    os.remove(fp)
                except:
                    pass
        except:
            pass
        c=0

        
        ax = plt.figure().add_subplot(projection='3d')
        
        for i in self.realcubes:
            c+=1
            print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1)
            n_voxels = np.zeros((15,15,15), dtype=bool)
            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[x,y,z]=True
            ax.voxels(n_voxels)
            plt.savefig("realcube"+str(c)+".png")

        try:
            fl = glob.glob("cube*png")
            for fp in fl:
                try:
                    os.remove(fp)
                except:
                    pass
        except:
            pass
        c=0

        
        ax = plt.figure().add_subplot(projection='3d')
        
        for i in self.cubes:
            c+=1
            print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1)
            n_voxels = np.zeros((15,15,15), dtype=bool)
            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[x,y,z]=True
            ax.voxels(n_voxels)
            plt.savefig("cube"+str(c)+".png")
        
    
    
    
    # add a cube to the reactor and calculate what actually happened
    def __add__(self, newcube):
        
        # we have two lists of cubes. One is "realcubes" - the ones that are physically present
        # the other is the list of added cubes

        # when adding a cube, we check the impact on "realcubes"

        newrealcubes = []

        #print ("pre",self.realcubes)
        for c in self.realcubes:

            # if the new cube completely overlaps or is identical to an existing cube, we remove the existing cube
            if cut.coverlap(newcube, c):
                continue # that is, don't add anything and continue with the next turn in the loop
            
            # if the cubes do not collide, keep c in the realcubes list and continue with the next turn in the loop
            if not cut.collision(newcube, c):
                newrealcubes.append(c)
                continue

            # if we get here, we have some kind of collision
            L = cut.dothecut(newcube, c)
            #print("We cut something and got something",L)
            #print ("nrc",newrealcubes)
            newrealcubes = newrealcubes + L
            #print ("nrc 2",newrealcubes)
        # once we have filtered the realcubes, we add the new cube, if it is an "on" cube
        if newcube.state == "on":
            newrealcubes.append(newcube)

        # we always add it to the list of cubes in the reactor (but not the realcubes)
        self.cubes.append(newcube)
        self.realcubes = newrealcubes

        if len(self.realcubes)<2:
            self.thesize=0
            for i in self.realcubes:
                self.thesize+=i.size()
            return self

        # try to merge the existing newrealcubes into smaller ones


#        s=0
#        for i in self.realcubes:
#            s+=i.size()
#        print("pre merge",self.realcubes,s)
        # try to merge the realcubes
    
        restart=True
        while restart:
            restart = False

            try:
                for i in range(len(self.realcubes)-1):
                    for j in range(i+1,len(self.realcubes)):
                        #print(self.realcubes[i],self.realcubes[j])
                        # if an "older" cube completely overlaps a newer cube, we remove the newer cube. this works because realcubes only contain the "on" set
                        if cut.coverlap(self.realcubes[i],self.realcubes[j]):
                            #print(i,j,cut.coverlap(self.realcubes[i],self.realcubes[j]),self.realcubes[i],"removes",self.realcubes[j],"due to 100% overlap")
                            #self.realcubes.pop(j)
                            X=[]
                            raise Done

                        X = cut.combinex(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combiney(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combinez(self.realcubes[i], self.realcubes[j])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done

                        X = cut.combinex(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combiney(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done
                        X = cut.combinez(self.realcubes[j], self.realcubes[i])
                        if X is not None:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            raise Done                        

            except Done:

                self.realcubes+=X
                restart = True

            except:
                import traceback
                print(traceback.format_exc())
                print(sys.exc_info()[2])
                sys.exit()

        s=0
        for i in self.realcubes:
            s+=i.size()
#        print("post merge",self.realcubes,s)
        self.thesize=s
        # and return the result of the addition
        return self
        

    # pretty print
    def __repr__(self):
        return str(self.cubes)
