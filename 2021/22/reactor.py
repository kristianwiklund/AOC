import cut
from box import Box
from copy import copy

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
            fl = glob.glob("realcube*png")
            for fp in fl:
                try:
                    os.remove(fp)
                except:
                    pass
        except:
            pass
        c=0

        
        ax = plt.figure().add_subplot(projection='3d')
        print("plotting on-set")
        for i in self.realcubes:
            c+=1
            print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1,i.id if i.id!=None else "")
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
        n_voxels = np.zeros((15,15,15), dtype=bool)
        print("plotting all")
        for i in self.cubes:
            c+=1
            print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1)

            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[x,y,z]=(i.state=="on")
        ax.voxels(n_voxels)
        plt.savefig("cube"+str(c)+".png")
        
    
    
    
    # add a cube to the reactor and calculate what actually happened
    def __add__(self, newcube):
        
        # we have two lists of cubes. One is "realcubes" - the ones that are physically present
        # the other is the list of added cubes

        # when adding a cube, we check the impact on "realcubes"

        newrealcubes = []

        #print ("iterating over",self.realcubes)
        
        for c in self.realcubes:
            from termcolor import colored
            #print (colored("checking","green"),newcube,"vs",c,"for overlap")
            # if the new cube completely overlaps or is identical to an existing cube, we remove the existing cube
            if cut.coverlap(newcube, c):
                #print(newcube,"completely covers",c,"remove",c)
                continue # that is, don't add anything and continue with the next turn in the loop

            #print (colored("checking","green"),newcube,"vs",c,"for collision")
            # if the cubes do not collide, keep c in the realcubes list and continue with the next turn in the loop
            if not cut.collision(newcube, c):
                #print(newcube,"does not conflict with",c,"keep",c)
                newrealcubes.append(c)
                continue

            #print (colored(str(newcube),"green"),"collides with",c)
            
            # if we get here, we have some kind of collision
            L = cut.dothecut(newcube, c)
#            print("We cut something and got something",L)
            #print ("nrc",newrealcubes)
            newrealcubes = newrealcubes + L
            #print ("nrc 2",newrealcubes)
        # once we have filtered the realcubes, we add the new cube, if it is an "on" cube

        #print ("done iterating over realcubes")
        if newcube.state == "on":
            #print("adding",newcube,"to realcubes")
            newrealcubes.append(newcube)

        # we always add it to the list of cubes in the reactor (but not the realcubes)
        #print ("append",newcube,"to the completeset, updating realcubes")
        self.cubes.append(newcube)
        self.realcubes = newrealcubes

        if len(self.realcubes)<2:
            self.thesize=0
            for i in self.realcubes:
                self.thesize+=i.size()
            return self

        # try to merge the existing newrealcubes into smaller ones


        #s=0
        #for i in self.realcubes:
        #    s+=i.size()
        #print("pre merge",self.realcubes,s)
        # try to merge the realcubes

        tmpX = copy(self.realcubes)
        restart=True
        while restart:

            restart = False

            try:
                for i in range(len(self.realcubes)-1):
                    for j in range(i+1,len(self.realcubes)):
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

 #       print(colored("pre-merge on-set was","yellow"),tmpX)        
 #       print(colored("post-merge on-set is","yellow"),colored(str(self.realcubes),"red"))
                
        # go through the on-set and kill cubes that completely overlap each other

        tmpX = copy(self.realcubes)
        cnt=0
        restart=True
        while restart:

            restart = False
            #print("merge loop #",cnt)
            cnt+=1
            try:
                for i in range(len(self.realcubes)-1):
                    for j in range(i+1,len(self.realcubes)):
                        
                        #print(self.realcubes[i],self.realcubes[j])
                        # if an "older" cube completely overlaps a newer cube, we remove the newer cube. this works because realcubes only contain the "on" set
                        #print(colored("checking","green"),self.realcubes[i],"vs",self.realcubes[j])
                        if cut.coverlap(self.realcubes[i],self.realcubes[j]):
                            #print(self.realcubes)
                            #print(i,j,cut.coverlap(self.realcubes[i],self.realcubes[j]),self.realcubes[i],colored("removes","yellow"),self.realcubes[j],"due to 100% overlap")
                            self.realcubes.pop(j)
                            #print(self.realcubes)
                            X=[]
                            raise Done
                        if cut.coverlap(self.realcubes[j],self.realcubes[i]):
                            #print(self.realcubes)
                            #print(i,j,cut.coverlap(self.realcubes[j],self.realcubes[i]),self.realcubes[j],colored("removes","yellow"),self.realcubes[i],"due to 100% overlap")
                            self.realcubes.pop(i)
                            #print(self.realcubes)
                            X=[]
                            raise Done
                        
                        
                        
            except Done:                
                self.realcubes+=X
                restart = True
            except:
                import traceback
                print(traceback.format_exc())
                print(sys.exc_info()[2])
                sys.exit()


#        print(colored("pre-overlap on-set was","yellow"),tmpX)        
#        print(colored("post-overlap on-set is","yellow"),colored(str(self.realcubes),"red"))
        
        s=0
        for i in self.realcubes:
            s+=i.size()
#            print("post merge",i,s)
            self.thesize=s
        # and return the result of the addition
        return self
        

    # pretty print
    def __repr__(self):
        return str(self.cubes)
