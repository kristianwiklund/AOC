# various utility functions that could be reusable

# usage
# import sys
# sys.path.append("../..")
# from utilities import *

# reads a block of lines separated with empty lines from a file
def readblock(fd,convert=lambda x:x,strip=True):
    elf = list()
    if strip:
        x = fd.readline().strip()
    else:
        x= fd.readline()
        
    while x:
        if x.strip()=="":
            return elf
        elf.append(convert(x))

        if strip:
            x = fd.readline().strip()
        else:
            x = fd.readline()

    return elf

# reads a file to an array
def readarray(fn, split=" ", convert=lambda x:x):

    arr = []
    
    with open(fn, "r") as fd:
        lines = fd.readlines()

        for line in lines:
            line = line.strip()

            if not split or split=="":
                la = [convert(x) for x in line]
            else:
                la = [convert(x) for x in line.split(split)]
            arr.append(la)

        return arr

    return None

# factorization
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# Returns the longest repeating non-overlapping
# substring in str
# from https://www.geeksforgeeks.org/longest-repeating-and-non-overlapping-substring/

def lrs(str):
 
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + str[i - 1]
 
    return res
 

# print a path (list of tuples) on an array

def printpath(path,nonum=True, background=None,bgin=None,end=""):

    if background:
        mx = len(background[0])
    else:
        mx = max([x for x,y in path])
            
    if background:
        my = len(background)
    else:
        my = max([y for x,y in path])


    l = len(path)
    l = 2+1 #hack


    # preprocess the path to figure out which symbol to use
    # - the item before and the item after are all on the same line
    # | the item before and the item after are all in the same column

    #
    #    ┏━┓
    #    ┃ ┃
    #    ┗━┛
    #

    draw = {
        (0,1,0,-1):"┃",
        (0,-1,0,1):"┃",
        (1,0,-1,0):"━",
        (-1,0,1,0):"━",
        (0,1,1,0):"┏",
        (1,0,0,1):"┏",
        (0,-1,-1,0):"┛",
        (-1,0,0,-1):"┛",
        (0,-1,1,0):"┗",
        (1,0,0,-1):"┗",
        (0,1,-1,0):"┓",
        (-1,0,0,1):"┓",
        }
    
    if nonum:
        syms = dict()
        # do all steps except the first and last one
        for i in range(1, len(path)-1):
            x = path[i][0]
            y = path[i][1]

            indx = (path[i-1][0]-x,path[i-1][1]-y,path[i+1][0]-x,path[i+1][1]-y)

            if indx in draw:
                s = draw[indx]
            else:
                s= "x"
            syms[path[i]] = s

            syms[path[0]]="B"
            syms[path[-1]]="E"
    
    for y in range(my):
        for x in range(mx):
            if (x,y) in path:
                if nonum:
                    if (x,y) in syms:
                        print(syms[(x,y)],end="")
                    else:
                        print("#",end="")
                else:
                    print ("{i: <{width}}|".format(i=path.index((x,y)), width=l),end="")
            else:
                if nonum:
                    if background==None:
                        print(".",end="")
                    else:
                        if bgin and background[y][x] in bgin:
                            print(background[y][x],end="")
                        else:
                            print(".",end="")
                else:
                    print (format("","<"+str(l))+"|",end="")

        print(""+end)
        
# --
from collections import defaultdict
# https://stackoverflow.com/questions/12720151/simple-way-to-group-items-into-buckets
def partition(seq, key):
    d = defaultdict(list)
    for x in seq:
        d[key(x)].append(x)
    return d

# --

# convert an array into a sparse array dict
def arr2sparse(arr,ignore=""):
    s = dict()

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] not in ignore:
                s[(x,y)] = arr[y][x]
    return (s)

# add a and b, which are tuples, item for item
def addtuples(a,b):
    return tuple([sum(x) for x in zip (a,b)])

assert(addtuples((1,0),(0,1))==(1,1))
assert(addtuples((-1,0),(1,0))==(0,0))
assert(addtuples((0,0),(0,0))==(0,0))
