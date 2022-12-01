# various utility functions that could be reusable


# reads a block of lines separated with empty lines from a file
def readblock(fd):
    elf = list()
    x = fd.readline().strip()
    
    while x:
        if x=="":
            return elf
        elf.append(int(x))
        
        x = fd.readline().strip()

    return elf
