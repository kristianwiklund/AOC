import cut
from box import Box
from copy import copy
from termcolor import colored

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

    def savefig(self,colliding=False):
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import os
        import glob

        # only plot colliding on-set items if specified
        cx = set(range(0,len(self.realcubes)))
        if colliding:

            for i in range(len(self.realcubes)-1):
                for j in range(i+1,len(self.realcubes)):
                    if cut.collision(self.realcubes[i],self.realcubes[j]):
                        print(i,"collides with",j)
                        cx.discard(i)
                        cx.discard(j)
                        

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
            if colliding and c in cx:
                print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1,i.id if i.id!=None else "",colored("does not overlap","yellow"))
                continue
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
        
        

    # pretty print
    def __repr__(self):
        return str(self.cubes)
