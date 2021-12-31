import cut
from box import Box
from copy import copy
from termcolor import colored
import networkx as nx
import sys
        
class Done(Exception):
    pass
    
# the reactor
class Reactor:

    # constructor
    def __init__(self):
        self.cubes=[]
        self.realcubes=[]
        self.thesize = 0
        self.debug = False
        
    # consistency check

    def consistencycheck(self):

        import numpy as np
        
        nx = self.drawallblobs()
        ny = self.getonset()
        fail = (ny-nx)!=0

        try:
            assert(sum(sum(sum(fail)))==0)
        except:
            print ("consistency check failed")
            print ("last added box:",self.cubes[-1])
            where = set()
            for x in range(len(fail)):
                for y in range(len(fail[x])):
                    for z in range(len(fail[x][y])):
                        if fail[x][y][z]:
                            where.add((x,y,z))

            what = set()
            for (x,y,z) in where:
                for i in self.cubes:
                    if i.intersects(x,y,z):
                        what.add(str(i))
            print(what)
            sys.exit()

        
    # return the size of the reactor. Updated during "add"
    def size(self):
        return self.thesize

    def getonset(self):


        import numpy as np
        
        mix=0
        miy=0
        mxx=0
        mxy=0
        miz=0
        mxz=0
        
        for i in self.cubes:
            mix = min(mix,i.x1)
            miy = min(miy,i.y1)
            miz = min(miz,i.z1)
            mxx = max(mxx,i.x2)
            mxy = max(mxy,i.y2)
            mxz = max(mxz,i.z2)

        c=0
        
        n_voxels = np.zeros((mxx-mix+1,mxy-miy+1,mxz-miz+1))


        if self.debug:
            print("calculating on-set",len(self.realcubes),"cubes")
        
        for i in self.realcubes:
            c+=1
            if self.debug:
                print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1,i.id if i.id!=None else "")

            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[(x-mix),(y-miy),z-miz]+=1


        return n_voxels
                
    
    def drawallblobs(self):
        import numpy as np

        mix=0
        miy=0
        mxx=0
        mxy=0
        miz=0
        mxz=0
        
        for i in self.cubes:
            mix = min(mix,i.x1)
            miy = min(miy,i.y1)
            miz = min(miz,i.z1)
            mxx = max(mxx,i.x2)
            mxy = max(mxy,i.y2)
            mxz = max(mxz,i.z2)

        c=0
            
        n_voxels = np.zeros((mxx-mix+1,mxy-miy+1,mxz-miz+1), dtype=bool)

        if self.debug:
            print("calculating all",len(self.cubes),"cubes")
            
        for i in self.cubes:
            c+=1

            if self.debug:
                print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1)

            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[(x-mix),(y-miy),z-miz]=(i.state=="on")

        return n_voxels
                        
    def savefig(self,colliding=False):
        import numpy as np
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        import os
        import glob

        mix=0
        miy=0
        mxx=0
        mxy=0
        miz=0
        mxz=0
        
        for i in self.cubes:
            mix = min(mix,i.x1)
            miy = min(miy,i.y1)
            miz = min(miz,i.z1)
            mxx = max(mxx,i.x2)
            mxy = max(mxy,i.y2)
            mxz = max(mxz,i.z2)


        #ax.set_xlim3d(0, mxx-mix)
        #ax.set_ylim3d(0, mxy-miy)
        #ax.set_zlim3d(0, mxz-miz)

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
        plt.xlabel("x")
        plt.ylabel("y")
        #        plt.zlabel("x")
        
        print("plotting on-set",len(self.realcubes),"cubes")
        for i in self.realcubes:
            c+=1
            if colliding and c in cx:
                print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1,i.id if i.id!=None else "",colored("does not overlap","yellow"))
                continue
            print(c," - ",i," - ", i.x1,i.x2-1,i.y1,i.y2-1,i.z1,i.z2-1,i.id if i.id!=None else "")

            n_voxels = np.zeros((mxx-mix+1,mxy-miy+1,mxz-miz+1), dtype=bool)

            for x in range(i.x1, i.x2):
                for y in range(i.y1, i.y2):
                    for z in range(i.z1, i.z2):
                        n_voxels[(x-mix),(y-miy),z-miz]=True
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

        n_voxels = self.drawallblobs()
        
        ax.voxels(n_voxels)
        plt.savefig("cube"+str(c)+".png")

        nx = self.drawallblobs()
        ny = self.getonset()
        fail = (ny-nx)!=0
#        np.set_printoptions(threshold=sys.maxsize)
#        print(fail)
        ax = plt.figure().add_subplot(projection='3d')
                
        ax.voxels(fail)
        plt.savefig("diff.png")
        
        
    def __add__(self, newcube):
        #       print ("add",len(self.realcubes))
        self.cubes.append(newcube)
        self.realcubes.append(newcube)
        self.optimize()
        
        L = []
        for i in range(len(self.realcubes)-1):
            nc = self.realcubes[i]-newcube
            #            print(self.realcubes[i],"-",newcube,"=",nc )
            L += nc
            #          print(L)
            
            
            #        print("new realcubes",L)
        self.realcubes = L
        
        if newcube.state=="on":
            self.realcubes.append(newcube)

        self.optimize()

        self.thesize=sum([max(0,x.size()) for x in self.realcubes])
        
        return self
    
    # pretty print
    def __repr__(self):
        return str(self.cubes)

    # -------------
    
    def optimize(self):

        # optimization starts from the back
        # any cube that iscompletely covered by a later cube is removed

        poplist = set()
        
        for i in range(len(self.realcubes)-1,-1,-1):
            for j in range(0,i):
        
                if self.realcubes[i].covers(self.realcubes[j]):
                    poplist.add(j)

        for i in sorted(list(poplist),reverse=True):
            self.realcubes.pop(i)

        # then check if we can combine cubes

        done=False
        
        while not done:
            done = True
            try:
                for i in range(len(self.realcubes)-1):
                    for j in range(i+1,len(self.realcubes)):
                        V = cut.combinex(self.realcubes[i],self.realcubes[j])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done

                        V = cut.combiney(self.realcubes[i],self.realcubes[j])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done

                        V = cut.combinez(self.realcubes[i],self.realcubes[j])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done

                        V = cut.combinex(self.realcubes[j],self.realcubes[i])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done

                        V = cut.combiney(self.realcubes[j],self.realcubes[i])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done

                        V = cut.combinez(self.realcubes[j],self.realcubes[i])
                        if V:
                            self.realcubes.pop(j)
                            self.realcubes.pop(i)
                            self.realcubes += V
                            raise Done
            except Done:
                done = False

        
                        

            
            
    # produce an interaction graph between the different boxes to find out which are touching
    
    def interactions(self):

        G = nx.DiGraph()
        
        for i in range(len(self.cubes)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if self.cubes[i].touches(self.cubes[j]):
                    G.add_edge(str(i),str(j))

        return G
    
                
        
        
