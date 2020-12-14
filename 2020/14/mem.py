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
    themask = "111111111111111111111111111111111111"

    def setmask(self, mask):
        self.themask = mask

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
        bopp = str(bin(key))[2:].zfill(36)

        k=list()
        for i in range(0,36):
            if self.themask[i] == 'X' or self.themask[i] == '1':
                k.append(self.themask[i])
            else:
                k.append(bopp[i])
        

        k= str("".join(k))

        lists=self.recurse(k)
        
        for i in lists:
            super(Mem2, self).__setitem__(i, value)

