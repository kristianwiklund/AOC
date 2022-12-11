# various utility functions that could be reusable

# usage
# import sys
# sys.path.append("../..")
# from utilities import *

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

# reads a file to an array
def readarray(fn, split=" ", convert=lambda x:x):

    arr = []
    
    with open(fn, "r") as fd:
        lines = fd.readlines()

        for line in lines:
            line = line.strip()

            la = [convert(x) for x in line.split(split)]
            arr.append(la)

        return arr

    return None

# factorization
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

