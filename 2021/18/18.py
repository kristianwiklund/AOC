#!/usr/bin/python3
import sys


L = [eval(x.strip()) for x in sys.stdin]

def a(x,y):
    return [x,y]

def split(x):
    if type(x) == list:
        return [split(x[0]),split(x[1])]
                
    if x>9:
        return [x//2,x-x//2]
    else:
        return x
    
def dotheboom(x):

    if type(x) != list:
        return

    if type(x[0]) == list and type (x[1]) != list:
        nl = [0,x[0][1]+x[1]]
    elif type(x[0]) != list and type (x[1]) == list:
        nl = [x[1][0]+x[0],0]
    else:
        nl = None

    return nl

assert(a([1,2],[[3,4],5])==[[1,2],[[3,4],5]])
assert(split([[9,8],1])==[[9,8],1])
assert(split([[[[0,7],4],[15,[0,13]]],[1,1]])==[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
                
assert(dotheboom([[9,8],1])==[0,9])
assert(dotheboom([4,[3,2]])==[7,0])

#assert(ex([[[[[9,8],1],2],3],4],0)==[[[[0,9],2],3],4])
#assert(ex([7,[6,[5,[4,[3,2]]]]],0)==[7,[6,[5,[7,0]]]])
#assert(ex([[6,[5,[4,[3,2]]]],0])==[[6,[5,[7,0]]],3])
#assert(ex([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],0)==[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
#assert(ex([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],0)==[[3,[2,[8,0]]],[9,[5,[7,0]]]])

