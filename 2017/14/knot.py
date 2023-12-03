
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

    def hash(self):

        l = list()
        for i in range(16):
            h = 0
            for j in range(16):
                h = h^self.listan[i*16+j]
            l.append(h)

        x = ""
        for i in l:
            x+='{:02x}'.format(i)
        return str(x)
    
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


# -- part 
def convert(s):
    input = [ord(x) for x in s]
    return input+[17,31,73,47,23]

def megatwist(s,l=256):
    rope = Rope(l)
    lengths=convert(s)
    for i in range(64):
        for i in lengths:
            rope.twist(i)
    return rope.hash()

assert(convert("1,2,3") == [49,44,50,44,51,17,31,73,47,23])
assert(megatwist("")=="a2582a3a0e66e6e86e3812dcb672a272")
assert(megatwist("AoC 2017")=="33efeb34ea91902bb2f59c9920caa6cd")

    

