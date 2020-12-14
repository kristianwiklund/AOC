import sys

class Mem(dict):
    ormask=0
    andmask=0b111111111111111111111111111111111111
    
    def setmask(self, mask):
        self.ormask = int(mask.replace("X","0"),2)
        self.andmask = int(mask.replace("X","1"),2)
        
    
    def __setitem__(self, key,value):
        value = value & self.andmask
        value = value | self.ormask
        
        return super(Mem, self).__setitem__(key, value)


class Mem2(dict):
    thekeepmask=0b111111111111111111111111111111111111
    thesetmask = 0
    thewildcardmask = ""

    def setmask(self, mask):
        
        #        print(mask)
        b = int(mask.replace("X","1"),2)
        self.thekeepmask =   (~b) + 0b111111111111111111111111111111111111
        self.thesetmask = int(mask.replace("X","0"),2)
        #        self.tsmask=mask
        self.themask = mask
        #print(self.thewildcardmask)

    def recurse(self, s):

        if len(s) == 0:
            return [""]            
        else:
            p = self.recurse(s[1:])
        l = list()

        for i in p:
            if s[0] == 'X':
                l.append("0"+i)
                l.append("1"+i)
            else:
                l.append(s[0]+i)

        return (l)
        
    def __setitem__(self, key, value):
        # wildcard match what already is in the memory
        # replace (fold) those into a single line
        
        #fkey = key & self.thekeepmask
        #fkey = fkey | self.thesetmask

        bopp = str(bin(key))[2:].zfill(36)
        #print("bopp:" +bopp)
        k=list()
        for i in range(0,36):
            if self.themask[i] == 'X' or self.themask[i] == '1':
                k.append(self.themask[i])
            else:
                k.append(bopp[i])
        

        k= str("".join(k))
        #print(k)
        lists=self.recurse(k)
        
        for i in lists:
            super(Mem2, self).__setitem__(i, value)

def sumzor(mem):

    return (sum(mem.values()))
