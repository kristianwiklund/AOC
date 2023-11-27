import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#import numpy as np

#arr = readarray("input.short",split="",convert=lambda x:x)


def decompress(sx,ack=""):

    S=sx.split("(",maxsplit=1)
    if len(S)==2:
        (s,sx)=S
        (c,sx)=sx.split(")",maxsplit=1)
        (cnt,rpt)=c.split("x")
        cnt=int(cnt)
        rpt=int(rpt)
        ack+=s
        it = sx[:cnt]
        sx = sx[cnt:]

        ack+=it*rpt
        return decompress(sx,ack=ack)
        
    else:
        return ack+sx
    
assert(decompress("ADVENT")=="ADVENT")
assert(decompress("A(1x5)BC")=="ABBBBBC")
assert(decompress("(3x3)XYZ")=="XYZXYZXYZ")
assert(decompress("A(2x2)BCD(2x2)EFG")=="ABCBCDEFEFG")
assert(decompress("X(8x2)(3x3)ABCY")=="X(3x3)ABC(3x3)ABCY")

lines = [len(decompress(x)) for x in readlines("input.long")]
print("Part 1:",sum(lines))

# unoptimized version
# this doesn't work, too much memory usage (as the task says) but it was useful to see if the decoder worked, then refactor into the correct solution

def decompress2(sx,ack=""):

    S=sx.split("(",maxsplit=1)
    if len(S)==2:
        (s,sx)=S
        (c,sx)=sx.split(")",maxsplit=1)
        (cnt,rpt)=c.split("x")
        cnt=int(cnt)
        rpt=int(rpt)
        ack+=s
        it = sx[:cnt]
        sx = sx[cnt:]

        ack+=decompress2(it)*rpt
        return decompress2(sx,ack=ack)
        
    else:
        return ack+sx


assert(decompress2("ADVENT")=="ADVENT")
assert(decompress2("A(1x5)BC")=="ABBBBBC")
assert(decompress2("(3x3)XYZ")=="XYZXYZXYZ")
assert(decompress2("A(2x2)BCD(2x2)EFG")=="ABCBCDEFEFG")
assert(decompress2("X(8x2)(3x3)ABCY")=="XABCABCABCABCABCABCY")
assert(sum([x=='A' for x in decompress2("(27x12)(20x12)(13x14)(7x10)(1x12)A")])==241920)
assert(len(decompress2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))==445)



def dc2lenh(sx,ack="0"):
    S=sx.split("(",maxsplit=1)
    if len(S)==2:
        (s,sx)=S
        (c,sx)=sx.split(")",maxsplit=1)
        (cnt,rpt)=c.split("x")
        cnt=int(cnt)
        rpt=int(rpt)
        ack+="+"+str(len(s))
        it = sx[:cnt]
        sx = sx[cnt:]

        ack+="+ ("+dc2lenh(it)+")*"+str(rpt)
        return dc2lenh(sx,ack=ack)
        
    else:
        return ack+"+"+str(len(sx))

def dc2len(s):
    return eval(dc2lenh(s))
    

assert(dc2len("ADVENT")==6)
assert(dc2len("A(1x5)BC")==7)
assert(dc2len("(3x3)XYZ")==9)
assert(dc2len("A(2x2)BCD(2x2)EFG")==11)
assert(dc2len("X(8x2)(3x3)ABCY")==20)
assert(dc2len("(27x12)(20x12)(13x14)(7x10)(1x12)A")==241920)
assert(dc2len("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")==445)

lines = [dc2len(x) for x in readlines("input.long")]
print("Part 2:",sum(lines))
