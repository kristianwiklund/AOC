
class Rope():

    def __init__(self,l):
        self.listan = list(range(l))
        self.cp = 0
        self.ll = l
        self.skip = 0

        
    def twist(self, length):
        l=[]
        
        for i in range(length):
            l.append(self.listan[(self.cp+i)%self.ll])
        l.reverse()

        for i in range(length):
            self.listan[(self.cp+i)%self.ll] = l[i]
            
        self.cp = (self.cp+length+self.skip) % self.ll
        self.skip+=1
        

    def __str__(self):
        return str(self.listan)
    
    def __eq__(self,l):
        return self.listan==l

    def result(self):
        return self.listan[0]*self.listan[1]
    
# tests

rope = Rope(5)
assert(rope==[0,1,2,3,4])

rope.twist(3)
assert(rope==[2,1,0,3,4])

rope.twist(4)
assert(rope==[4,3,0,1,2])

rope.twist(1)
assert(rope==[4,3,0,1,2])

rope.twist(5)
assert(rope==[3,4,2,1,0])

assert(rope.result()==12)

# kodden

rope = Rope(256)
lengths=[83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]

for i in lengths:
    rope.twist(i)

print("Part 1:",rope.result())
