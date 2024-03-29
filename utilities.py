# various utility functions that could be reusable

# usage
# import sys
# sys.path.append("../..")
# from utilities import *
from functools import cache, wraps
import re


# calculate the line equation from two positions
# returns  ax+bx+c=0
def p2l(P):
    
    P1 = P[0]
    P2 = [P[0][0]+P[1][0],P[0][1]+P[1][1]]

    x1 = P1[0]
    y1 = P1[1]

    x2 = P2[0]
    y2 = P2[1]

    A = y2-y1
    B = x1-x2
    C = y1*(x2-x1)-(y2-y1)*x1

#    print("x",A,B,C,P)
    return ([A,B,C])

# calculate the intersection point of two lines on line equation format
def isx(L1,L2):

#    print(L1,L2)
#    X = cross(L1,L2)
#    X = (X/X[2])[0:2]
#    return X
    
    a1 = L1[0]
    b1 = L1[1]
    c1 = L1[2]

    a2 = L2[0]
    b2 = L2[1]
    c2 = L2[2]
    
    x0 = (b1*c2-b2*c1)
    y0 = (c1*a2-c2*a1)
    k0 = (a1*b2-a2*b1)

    if not k0:
        return None
    
    #    return (x0,y0,k0)
    return (x0/k0,y0/k0,1)




# https://stackoverflow.com/questions/1984799/cross-product-of-two-vectors-in-python
def cross(a, b):
#    if len(a)==2:
#        c = a[0]*b[1]-b[0]*a[1]
    #el
    if len(a)==3:
        c = [a[1]*b[2] - a[2]*b[1],
             a[2]*b[0] - a[0]*b[2],
             a[0]*b[1] - a[1]*b[0]]
    else:
        raise ValueError("wrong dimension, need 3")
    
    return c

#https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "("+str(args)+","+str(kwargs)+")")
        return func(*args, **kwargs)
    return with_logging


# get all integers from a string
# if negative is True, also handles negative numbers
@cache
def ints(s, negative=True):
    if not negative:
        v = [int(x) for x in re.split(r'\D+',s) if x.isdigit()]
    else:
        pattern = r"[+-]?\d+"
        v = [int(x) for x in re.findall(pattern, s)]

    return v

assert(ints("5 lions ate 3 sheep")==[5,3])
assert(ints("it is usally -10 or -100 or 50 degrees outside")==[-10,-100,50])
assert(ints("banana 5 nabana 5")==[5,5])

assert(ints("5 lions ate 3 sheep",negative=False)==[5,3])
assert(ints("it is usally -10 or -100 or 50 degrees outside", negative=False)==[10,100,50])
assert(ints("banana 5 nabana 5", negative=False)==[5,5])

import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        run_time = end_time - start_time
        print("Finished {} in {} ms".format(repr(func.__name__), run_time/1000000))
        return value
    
    return wrapper

# deprecated:
# can be replaced by sortedcontainers
def sortdictbykey(d):
    return (sorted(d.items(), key=lambda kv: 
                 (kv[1], kv[0])))

# read lines and remove end linefeed

def readlines(fn):
    with open(fn) as fd:
        return [x.strip() for x in fd.readlines()]

# reads a block of lines separated with empty lines from a file
def readblock(fd,convert=lambda x:x,strip=True):
    
    elf = list()
    x = fd.readline()
    if x=="":
        return None    
    if strip:
        x = x.strip()
    else:
        x= x.strip("\n")
        
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
def readarray(fn, split=" ", convert=lambda x:x, strip=True):

    arr = []
    
    with open(fn, "r") as fd:
        lines = fd.readlines()

        for line in lines:
            if strip:
                line = line.strip()
            else:
                line = line.strip("\n")
                
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


# flood fill an array with v starting at x,y where elements are b
def floodfill(a,x,y,v,b=0):
   p = [(x,y)]

   while p:
      x,y=p.pop()
      a[y][x]=v
      for i in range(4):
         if checkpos(a, x+dirs[i][0], y+dirs[i][1], lambda i:i==b, outofbounds=False):
            p.append((x+dirs[i][0], y+dirs[i][1]))



# draw a line between two points in an array
#@logged
def drawline(ap, x1,y1,x2,y2,d):

    xx1 = min(x1,x2)
    yy1 = min(y1,y2)

    xx2 = max(x1,x2)
    yy2 = max(y1,y2)
    

    # doesn't work for diagonals
    for x in range(xx1,xx2+1):
        for y in range(yy1,yy2+1):
            ap[y][x]=d



# normalize a path to have its lower value at 0
def poff(path):
    x = [i[0] for i in path]
    y = [i[1] for i in path]

    dx = -min(0,min(x))
    dy = -min(0,min(y))

    return (dx,dy)
    
            
# print a path (list of tuples) on an array
def printpath(p,nonum=True, background=None,bgin=None,end="",thex=None):

    path = [(i[0],i[1]) for i in p]
    
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

    # we may also turn back the same path, this is not covered by the table above

    draw[(1,0,1,0)] = "⮎" #⮎ ⮌ ⮏ ⮍
    draw[(-1,0,-1,0)] = "⮌"
    draw[(0,-1,0,-1)] = "⮍"
    draw[(0,1,0,1)] = "⮏"
    
    if nonum:
        syms = dict()
        # do all steps except the first and last one
        if len(path)>1:
            for i in range(1, len(path)-1):
                x = path[i][0]
                y = path[i][1]

                indx = (path[i-1][0]-x,path[i-1][1]-y,path[i+1][0]-x,path[i+1][1]-y)

                if indx in draw:
                    s = draw[indx]
                else:
                    #print(indx)
                        
                    if thex:
                        s = thex[i]

                    else:
                        s= "x"
                        
                syms[path[i]] = s
                
                syms[path[0]]="B"
                syms[path[-1]]="E"
        else:
            if len(path)==1:
                syms[path[0]]="B"
            
    
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
                            try:
                                print(background[y][x],end="")
                            except:
                                pass
                            #                            print(".",end="")
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

# def check a position in an array to see if it fulfills the lambda function
# outofbounds is the value used if we are out of the array

def checkpos(arr, x, y, fun, outofbounds=False):
    if x<0:
        return outofbounds

    if y<0:
        return outofbounds

    if x>=len(arr[0]):
        return outofbounds

    if y>=len(arr):
        return outofbounds

    return fun(arr[y][x])

dirs = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

def checkallpos(arr, x, y, fun, outofbounds=False):

    v= [checkpos(arr, x+dirs[i][0], y+dirs[i][1], fun, outofbounds) for i in range(4)]
    #    print("cap",x,y,v)
    return v
        

# check position around an item in an array to see if they fulfill the lambda function
def checkallaround(arr, x, y, fun, outofbounds=True):
    v = True
    v &= checkpos(arr,x-1,y-1,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x-1,y,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x-1,y+1,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x,y-1,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x,y+1,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x+1,y-1,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x+1,y,fun, outofbounds=outofbounds)
    v &= checkpos(arr,x+1,y+1,fun, outofbounds=outofbounds)

    return v

def checkanyaround(arr, x, y, fun, outofbounds=False):
    v = False
    v |= checkpos(arr,x-1,y-1,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x-1,y,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x-1,y+1,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x,y-1,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x,y+1,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x+1,y-1,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x+1,y,fun, outofbounds=outofbounds)
    v |= checkpos(arr,x+1,y+1,fun, outofbounds=outofbounds)

    return v    


___arr=[['4', '6', '7', '', '', '1', '1', '4', '', ''], ['', '', '', '*', '', '', '', '', '', ''], ['', '', '3', '5', '', '', '6', '3', '3', ''], ['', '', '', '', '', '', '#', '', '', ''], ['6', '1', '7', '*', '', '', '', '', '', ''], ['', '', '', '', '', '+', '', '5', '8', ''], ['', '', '5', '9', '2', '', '', '', '', ''], ['', '', '', '', '', '', '7', '5', '5', ''], ['', '', '', '$', '', '*', '', '', '', ''], ['', '6', '6', '4', '', '5', '9', '8', '', '']]

assert(checkanyaround(___arr, 0, 0, lambda x:x!=''))

# true if a overlaps b
# a and b are ranges
def overlaps(a, b):

    return a.stop > b.start and b.stop>a.start


# route through a cost matrix
def droute(arr, barr, start, stop, f=lambda x:x=="."):

    r = [stop]
    (x,y) = stop
    
    while True:
        v = checkallpos(arr,x,y,f,outofbounds=False)
        i = sorted([i for i in range(4) if v[i]], key=lambda t:barr[y+dirs[t][1]][x+dirs[t][0]])
        i = [(x+dirs[t][0],y+dirs[t][1]) for t in i]
        i = [t for t in i if t not in r]
        
        # check if unroutable (i.e. we will backtrack on ourselves)
        # this happens if we have fed the router a strange weighted matrix as in 2023 17
        if not len(i):
            printpath(r,background=arr)
            return None
        
        (x,y) = i[0]                
        r.append((x,y))
        if (x,y)==start:
            break
    return list(reversed(r))
    
# dijksta on a matrix
# default follows "."
def dijkstra(arr, start, f=lambda x:x==".", stop=None):

    (startx, starty) = start

    if not f(arr[starty][startx]):
        return None

    if stop and not f(arr[stop[1]][stop[0]]):
        return None
    
    n = sum([len(x) for x in arr])**10
    barr = [[n+1]*len(x) for x in arr]
    
    barr[starty][startx]=0

    p = [(x,y) for x in range(len(arr[0])) for y in range(len(arr)) if f(arr[y][x])]

    while len(p):
        p = sorted(p,key = lambda x:barr[x[1]][x[0]])
        (x,y) = p.pop(0)

        v = checkallpos(arr,x,y,f,outofbounds=False)
        for i in range(4):
            if v[i]:
                barr[y+dirs[i][1]][x+dirs[i][0]] = min(barr[y+dirs[i][1]][x+dirs[i][0]],barr[y][x]+1)

        if stop!=None and stop==(x,y):
            break


    if stop!=None:
        p = droute(arr, barr, start, stop, f)
        return(barr,p)
    else:
        return(barr,None)
                                                       

__arr=["@@@@@@@@@",
       "@.......@",
       "@.@@@@@.@",
       "@.....@.@",
       "@@@.@.@@@",
       "@...@...@",
       "@@@@@@@.@"]

(__barr,__p) = (dijkstra(__arr, (7,6), stop=(7,2)))
assert(__p==[(7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2)])
#print(__p)
#printpath(__p,background=__arr)
