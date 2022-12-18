import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
#from box import Box
#from reactor import Reactor


class Box():

    def __init__(self,l):

        self.x1=l[0]
        self.y1=l[1]
        self.z1=l[2]
        if len(l)>3:
            self.x2=l[3]
            self.y2=l[4]
            self.z2=l[5]
        else:
            self.x2=self.x1+1
            self.y2=self.y1+1
            self.z2=self.z1+1

        # merge two cubes that are connected on the X side and return a new cube

    def __repr__(self):
        return("Box(["+str(self.x1)+","+str(self.y1)+","+str(self.z1)+","+str(self.x2)+","+str(self.y2)+","+str(self.z2)+"])")
        
    def combinex(a,b):

        if a.y1==b.y1 and a.y2==b.y2:
            if a.z1==b.z1 and a.z2==b.z2:
                if a.x2==b.x1:
#                    c = Box([a.x1,b.x2,a.y1,a.y2,a.z1,a.z2])
                    c = Box([a.x1,a.y1,a.z1,b.x2,a.y2,a.z2])
                    #print("x merge",a,b,c)            
                    return [c]
            
        else:
            return None

    # merge two cubes that are connected on the Y side and return a new cube

    def combiney(a,b):

        if a.x1==b.x1 and a.x2==b.x2:
            if a.z1==b.z1 and a.z2==b.z2:
                if a.y2==b.y1:
#                    c = Box([a.x1,a.x2,a.y1,b.y2,a.z1,a.z2])
                    c = Box([a.x1,a.y1,a.z1,a.x2,b.y2,a.z2])
                    #print("y merge",a,b,c)
                    return [c]
            
        else:
            return None

    # merge two cubes that are connected on the Z side and return a new cube
    
    def combinez(a,b):

        if a.x1==b.x1 and a.x2==b.x2:
            if a.y1==b.y1 and a.y2==b.y2:
                if a.z2==b.z1:
#                    c = Box([a.x1,a.x2,a.y1,a.y2,a.z1,b.z2])
                    c = Box([a.x1,a.y1,a.z1,a.z2,a.y2,b.z2])
                    #print("z merge",a,b,c)
                    return [c]
                    
        else:
            return None
        
            
    def merge(self, other):
        
        xx = self.combinex(other)
        yy = self.combiney(other)
        zz = self.combinez(other)

        if xx:
            return xx
        if yy:
            return yy
        if zz:
            return zz

    def __eq__(self, other):
        return self.x1==other.x1 and self.y1==other.y1 and self.z1==other.z1 and self.x2==other.x2 and self.y2==other.y2 and self.z2==other.z2

    def size(self):
        a = 0
        # top and bottom
        a += (self.y2-self.y1)*(self.x2-self.x1)
        # left and right
        a += (self.z2-self.z1)*(self.x2-self.x1)
        # far and near
        a += (self.z2-self.z1)*(self.y2-self.y1)
        a*=2
        return a
    
# ---

a = Box([1,1,1])
b = Box([2,1,1])

assert(a==a)
assert(a.merge(b)[0]==Box([1,1,1,3,2,2]))

print(a.merge(b)[0])
print(a.merge(b)[0].size())
arr = [Box(x) for x in readarray("input.short",split=",",convert=lambda x:int(x))]


def merge(arr):

    # box for box, check if something in arr touches something else

    narr = []
    kset = set()
    
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if str(arr[j]) in kset:
                continue
            t = arr[i].merge(arr[j])
            if t:
                print("Merge",arr[i],arr[j],"=",t)
                narr.append(t[0])
                kset.add(str(arr[i]))
                kset.add(str(arr[j]))
    
    for v in arr:
        if not str(v) in kset:
            narr.append(v)
    
    return (narr)
                

parr = []
while len(parr)!=len(arr):
    parr = arr
    arr = merge(arr)
    print(arr)

x = [x.size() for x in arr]
print (sum(x))
    
        
