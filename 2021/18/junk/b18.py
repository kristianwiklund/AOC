#!/usr/bin/python3

lq = []
rq = []

class SF:

    lf=None
    rf=None

    # add X to this
    def __add__(self,X):
        # trivial add:
        l = self.lf
        r = self.rf

        P = SF([None,None])
        P.lf = self
        P.rf = X
        P.ud(0)
        return P
    
    def __init__(self, X):
        if type(X) == list:
            if type(X[0]) != list:
                self.lf = X[0]
            else:
                self.lf = SF(X[0])
            if type(X[1]) != list:
                self.rf = X[1]
            else:
                self.rf = SF(X[1])
            self.ud(0)
            
    def __eq__(self, other):
        return (self.lf == other.lf) and (self.rf == other.rf)
    
    def __repr__(self):
        return "("+str(self.lf)+","+str(self.rf)+")["+str(self.depth)+"/"+str(self.maxd)+"]"

    def ud(self,d):
        self.depth=d
        self.ld=0
        self.rd=0
        
        if self.lf and type(self.lf)!=int:
            self.ld = self.lf.ud(d+1)
            
        if self.rf and type(self.rf)!=int:
            self.rd = self.rf.ud(d+1)

        self.maxd=max(self.ld,self.rd)
        return self.maxd+1

    def boom(self):

        #        print("boom", str(self), self.depth)
        
        if self.depth < 3:
            if type(self.lf) != int:
                self.lf.boom()
            if type(self.rf) != int:
                self.rf.boom()
        else:
            if type(self.lf) != int and type(self.rf) == int:
                self.rf = self.rf + self.lf.rf
                lq.append(self.lf.lf)
                self.lf = 0

            if type(self.rf) != int and type(self.lf) == int:
                self.lf = self.lf + self.rf.lf
                rq.append(self.rf.rf)
                self.rf = 0

a = SF([1,2])
b = SF([[3,4],5])

assert((a+b)==SF([[1,2],[[3,4],5]]))
print(a+b)

c = SF([[[[[9,8],1],2],3],4])
print(c)
c.boom()
print(c)

assert(c==SF([[[[0,9],2],3],4]))

d = SF([7,[6,[5,[4,[3,2]]]]])
d.boom()

assert(d==SF([7,[6,[5,[7,0]]]]))
