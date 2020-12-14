import re

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
        #        print("  "+mask)
        #        print(bin(b).zfill(36))
        #        print(bin(self.keepmask).zfill(36))
        self.thesetmask = int(mask.replace("X","0"),2)
        #        self.tsmask=mask
        self.thewildcardmask = mask.replace("1"," ").replace("0"," ").replace("X",".")

        
    def __setitem__(self, key,value):
        # wildcard match what already is in the memory
        # replace (fold) those into a single line
        
        fkey = key & self.thekeepmask
        fkey = fkey | self.thesetmask

        bopp = str(bin(fkey))[2:].zfill(36)

        k=list()
        for i in range(0,36):
            if self.thewildcardmask[i] != ' ':
                k.append(self.thewildcardmask[i])
            else:
                k.append(bopp[i])


        k= str("".join(k))

        if k[35] == '.':
            lists = ["1","0"]
        else:
            lists = [k[i]]
        
        for i in range(34,0,-1):
            if k[i] == '.':
                what = ['1','0']
            else:
                what = [k[i]]

            lists = [[x+y for x in lists for y in what]]
            lists = sum(lists,[])
            
        for i in lists:
            super(Mem2, self).__setitem__(i[::-1], value)

def sumzor(mem):

    k =0
    for i in mem.keys():
        x = sum(map((lambda x:1 if x=='.' else 0), list(i)))
        k=k+((2**x)*mem[i])
    return (k)
