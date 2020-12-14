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
    tsmask=0
    ormask=0
    andmask=0b111111111111111111111111111111111111
    
    def setmask(self, mask):
        self.ormask = int(mask.replace("X","0"),2)
        self.andmask = int(mask.replace("X","0"),2)
        self.tsmask=mask

        
    def __setitem__(self, key,value):
        l = len(self.tsmask)
        key = key & self.andmask
        key = (key | self.ormask)
        key = str(bin(key))[2:].zfill(l)
        key = list(key)
        for i in range(0,len(self.tsmask)):
            if self.tsmask[i] == 'X':
                key[i] = 'X'
                                    
        key = "".join(key)

        return super(Mem2, self).__setitem__(key, value)

