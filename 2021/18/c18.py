#!/usr/bin/python3

from anytree import Node, RenderTree, NodeMixin, AsciiStyle, PreOrderIter, LevelOrderIter, PostOrderIter
from anytree.exporter import DotExporter
from anytree.util import leftsibling,rightsibling

class SF(NodeMixin):

    def __init__(self,X,empty=False):
        super(SF, self).__init__()

        if empty:
            return
        
        if type(X) == list:
            lf = SF(X[0])
            lf.parent = self
            rf = SF(X[1])
            rf.parent = self
            self.value=None
            self.name="_"
        else:
            self.value=int(X)
            self.name="_"
            
    def __add__(self, other):
        x = SF(0,empty=True)
        self.parent = x
        other.parent = x
        x.name="+"
        return x

    def __eq__(self,other):
        if len(self.children)!=len(other.children):
            return False

        if len(self.children)==0:
            return self.value==other.value
        
        bop = True
        
        for i in range(len(self.children)):
            bop = bop and (self.children[i] == other.children[i])

        return bop

    def depth(self):
        if self.parent:
            return 1+self.parent.depth()
        else:
            return 0
    
    def __repr__(self):

        L = []
        if len(self.children)==2:

            return "["+str(self.children[0])+","+str(self.children[1])+" ("+str(self.depth())+") "+ "]"
        
        return str(self.value)

    def boom(self):
        if self.depth()<4 or len(self.children)==0:
            return None
        else:
            # do the boom
            left = leftsibling(self)
            right = rightsibling(self)
            print("left: "+str(left)+", right: "+str(right))

            if not left: # go up
                pass
            else:
                for i in PreOrderIter(left):
                    if type(i.value)==int:
                        i.value = i.value + self.children[0].value
                        break
            if not right: # go up
                pass
            else:
                for i in PostOrderIter(right):
                    if type(i.value)==int:
                        i.value = i.value + self.children[1].value
                        break
            
            return True
            
        

# --
def p(X):
    for line in DotExporter(X):
        print (line)
# -- 

assert(SF([1,2])+SF([[3,4],5])==SF([[1,2],[[3,4],5]]))

d = SF([[[[4,3],4],4],[7,[[8,4],9]]]) + SF([1,1])
assert(d==SF([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]))

e = SF([1,1])+SF([2,2])+SF([3,3])+SF([4,4])+SF([5,5])

print(e)

f = SF([[[[[9,8],1],2],3],4])
g = SF([[1,1],[2,2]])
print(RenderTree(f, style=AsciiStyle()))
for i in PreOrderIter(f):
    x = i.boom()
    if x:
        break

print(RenderTree(f, style=AsciiStyle()))
