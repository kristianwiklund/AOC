# various utility functions that could be reusable
# -*-  coding: utf-8 -*-

# usage
# import sys
# sys.path.append("../..")
# from utilities import *
from functools import cache, wraps
import regex as re
import re
import math
import sys

# transpose matrix. from python docs
def transpose (matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
#https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "("+str(args)+","+str(kwargs)+")")
        return func(*args, **kwargs)
    return with_logging


# print call trace
from colorama import Fore
from inspect import signature

def calltrace(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(Fore.RED+function.__name__+"("+str(args)+") = "+str(result)+Fore.RESET)
        print(Fore.GREEN+"--",signature(function).parameters,Fore.RESET)
        return result
    return wrapper

def flatten(matrix):
    return [item for row in matrix for item in row]

# from copy import deepcopy

# def flippeflopp(a,b):

#     if isinstance(a,list) and isinstance(b,list):
#         print(a,b)
#         c = [x+y for x in a for y in b]
#     else:
#         print(a,b)
#         if isinstance(b,list):
#             c = [x+y for x in [a] for y in b]
#         else:
#             c = [x+y for x in a for y in [b]]

#     return c
    
    
# # consume a list of lists and create a flat list that have all bifurcations flattened
# @calltrace
# def fwb(l,pl,r):

#     print(r,"fwb",l,pl)
#     # trivial case, we have run out of tokens
#     if l==[]:
#         print(r,"no more tokens, return what we have")
#         return pl

# #    if len(l)==1 and isinstance(l[0],list):
# #        l=l[0]
    
#     # trivial case, completely flat list
#     nested = any(isinstance(i, list) for i in l)
#     if pl==[] and not nested:
#         print(r,"not nested returning l (ell)")
#         return [l]
    
#     # combine the previously collected items with the first item in the list
#     # treat the first item in the list recursively, in case it is a nested list

#     l=deepcopy(l)
#     print("-------------", l)
#     thirst = deepcopy(l.pop(0))
#     print(r,"calling fwb with",thirst,"to flatten if needed")
#     first = fwb(thirst,[],r+1)[0]
#     print(r,"we have flattened",thirst,"to",first)
# #    first=first[0]
    
#     # now first contains a cleaned (flat) list of items
#     # l contains the list of not yet processed items
#     # pl contains the list of items we have processed earlier

#     # combine first and pl into new items
#     if len(pl):
#         print(r,"combining",pl, "and", first)
#         print(type(pl).__name__,type(first).__name__)

#         print("----_---",pl,first)

#         c = flippeflopp(pl, first)

#         print(r,"|||||||||||||||| c=",c)
#  #       sys.exit()
#     else:
#         print(r,"pl is empty",pl,"using first for c",first)
#         c = first

    
#     print(r,"mupp","pl:",pl,"l:",l,"c:",c)

#     print(r,"calling again to continue flattening...")
#     return fwb(l, c, r+1)
    
# from sortedcontainers import SortedSet
        
# def flattenwithbranches(l, pl=[]):
#     m=fwb(l,pl,0)
#     return m
    


# #print(flattenwithbranches(["a"]))
# assert(flattenwithbranches(["a"])==[["a"]])
# assert(flattenwithbranches(["a","b"])==[["a","b"]])
# assert(flattenwithbranches(["a","b","c"])==[["a","b","c"]])
# #print(Fore.RED+"skogen"+Fore.RESET,flattenwithbranches(["a",["b","c"]]))
# print("----------------------------------------------------")
# assert(flattenwithbranches(["a",["b","c"]])==["ab"],["ac"])
# #print("skogen",flattenwithbranches(["a",["b","c"],"d"]))
# assert(flattenwithbranches(["a",["b","c"],"d"])==["abd","acd"])


# get the manhattan distance between two points
def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

# find one (default) or all (if flag) items in an array matching
def findinarray(arr,what,all=False):

#    barr=[(arr.index(row),row.index(what)) for row in arr if what in row]

    barr=[]
    for i,r in enumerate(arr):
        for j,w in enumerate(r):
          if w==what:
              barr.append((j,i))
    
    if not all:
        if not len(barr):
            return False
        else:
            return barr[0]
        
    return barr

# sign of a number
def sign(i):
    if i<0:
        return -1
    elif i>0:
        return 1
    else:
        return 0
    
import regex
# count all matches in a string, even overlapping
def countall(s,p):
    return len(re.findall(p, s, overlapped=True))
    
# reverse zip
def unzip(l):
    return list(zip(*l))

assert(unzip(zip([1,2,3],["a","b","c"]))==[(1,2,3),("a","b","c")])

# Custom Decorator function, for use with functools caches
def list_to_tuple(function):
    def wrapper(*args):
        args = [tuple(x) if isinstance(x, list) else x for x in args]
        result = function(*args)
        result = tuple(result) if isinstance(result, list) else result
        return result
    return wrapper


#return y as function of x given P
def fxl(P,x):
    # ax+by+c=0
    # by = 0-c-ax
    #y = -c/b - ax/b

    return ((-P[2]-P[0]*x)/P[1])
    
# calculate the line equation from two positions
# returns  ax+by+c=0
def p2l(P):
    
    P1 = P[0]
    P2 = P[1]#[P[0][0]+P[1][0],P[0][1]+P[1][1]]

    x1 = P1[0]
    y1 = P1[1]

    x2 = P2[0]
    y2 = P2[1]

    A = y2-y1
    B = x1-x2
    C = y1*(x2-x1)-(y2-y1)*x1

    dd=math.gcd(A,B,C)

#    print("x",[A/dd,B/dd,C/dd],P)
    return ([A/dd,B/dd,C/dd])

assert(p2l(((1,1),(2,2)))==[1.0,-1.0,0])

def printleq(P):
    print(P,"{}x{}{}y{}{} = 0".format(P[0],"+" if P[1]>-1 else "", P[1],"+" if P[2]>0 else "", P[2] ))

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


# https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(p1,p2):
#    print(p1,p2)
    A,B=p1
    C,D=p2
    
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)



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
import cProfile, pstats

def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        value = func(*args, **kwargs)
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumtime')
        stats.print_stats()
        return value
    return wrapper

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
    if not n:
        return None
    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sfactors(n):
    x = factors(n)
    return sorted(list(x))

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
    

from colorama import Fore

# print a path (list of tuples) on an array
def printpath(p,nonum=True, background=None,bgin=None,end="",thex=None,highlight=None):

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
                        if highlight!=background[y][x]:
                            print(Fore.RED+syms[(x,y)]+Fore.RESET,end="")
                        else:
                            print(Fore.BLUE+syms[(x,y)]+Fore.RESET,end="")
                    else:
                        if highlight!=background[y][x]:
                            print(Fore.RED+"#"+Fore.RESET,end="")
                        else:
                            print(Fore.BLUE+"#"+Fore.RESET,end="")                            
                else:
                    print ("{i: <{width}}|".format(i=path.index((x,y)), width=l),end="")
            else:
                if nonum:
                    if background==None:
                        print(".",end="")
                    else:                        
                        if bgin and background[y][x] in bgin:
                            if highlight!=background[y][x]:
                                print(background[y][x],end="")
                            else:
                                print(Fore.YELLOW+background[y][x]+Fore.RESET,end="")
                        else:
                            try:
                                if highlight!=background[y][x]:
                                    print(background[y][x],end="")
                                else:
                                    print(Fore.YELLOW+background[y][x]+Fore.RESET,end="")
                            except:
                                pass
                            #                            print(".",end="")
                else:
                    print (format("","<"+str(l))+"|",end="")

        print(Fore.RESET+""+end)
        
# --
from collections import defaultdict
# https://stackoverflow.com/questions/12720151/simple-way-to-group-items-into-buckets
def partition(seq, key):
    d = defaultdict(list)
    for x in seq:
        d[key(x)].append(x)
    return d

# --

def sparse2arr(spa,value="#",bg=".",dim=None):

    if dim:
        mx,my=dim
    else:
        mx=max([x for x,_ in spa])+1
        my=max([y for _,y in spa])+1

    arr = [[bg]*mx for _ in range(my)]

    for x,y in spa:
        if not value and isinstance(spa, collections.Mapping):
            arr[y][x]=spa[(x,y)]
        else:
            arr[y][x]=value
           # print(y,x)
            
    return arr
        
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




# north, east, south, west
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
# used by dijkstra function below
def droute(arr, barr, start, stop, f=lambda x:x==".",all=False):

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
#            printpath(r,background=arr)
            return None

        (x,y) = i[0]
        r.append((x,y))
        if (x,y)==start:
            break
    return list(reversed(r))



# dijksta on a matrix
# default follows "."
def dijkstra(arr, start, f=lambda x:x==".", stop=None, barr=None, mr=droute,maxlen=None):

    (startx, starty) = start

    if not f(arr[starty][startx]):
        return None

    if stop and not f(arr[stop[1]][stop[0]]):
        return None
    
    n = sum([len(x) for x in arr])**10

    if not barr:
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
        p = mr(arr, barr, start, stop, f)
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
