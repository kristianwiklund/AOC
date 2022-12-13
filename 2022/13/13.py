# import sys
# sys.path.append("../..")
# from utilities import *


def c2(l,r,d=False):
    # if both values are integer, the lower integer should come first

    if isinstance(l,int) and isinstance(r,int):
        if l<r:
            return True
        if l>r:
            return False

    # if exactly one value is an integer, convert the integer to a list
    if isinstance(l,int):
        l=[l]


    if isinstance(r,int):
        r=[r]
        

    # if both values are lists, compare the first value of the list, then the second value, and so on
    # if the left list runs out of values first, the inputs are in the right order
    # if the right list runs out of values first, the inputs are in the wrong order
    # if the lists are the same length, and no comparison makes a decision about the order, continue checking the next part of the input

    if isinstance(l,list) and isinstance(r,list):

        for i in range(len(l)):
            # right runs out of values first, wrong order
            if i>=len(r):
                return False

            if l[i]==r[i]:
                continue
            return c2(l[i],r[i])
        
    # left runs out of items first
    return True

assert(c2([1,1,3,1,1], [1,1,5,1,1]))
assert(c2([[1],[2,3,4]], [[1],4],d=True))
assert(not c2([9],[[8,7,6]]))
assert(c2([[4,4],4,4],[[4,4],4,4,4]))
assert(not c2([7,7,7,7],[7,7,7]))
assert(c2([],[3]))
assert(not c2([[[]]],[[]]))
assert(not c2([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9],d=True))

#import sys
#sys.exit()

with open("input.txt") as fd:

    lines = [x.strip() for x in fd.readlines()]
    klines = list()
    
    
    score=0
    cnt=0
    for i in range(0,len(lines),3):
        cnt+=1
        left = eval(lines[i])
        klines.append(left)
        l=left
        right = eval(lines[i+1])
        klines.append(right)
        r=right

        # chomp = i+2

        try:
            if c2(l,r, d=True):
                score+=cnt
        except:
            print("crash")
            print(left)
            print(right)
            import sys
            sys.exit()
            
print("Part 1:",score)

def c3(l,r):
    if l==r:
        return 0
    
    if c2(l,r):
        return -1
    else:
        return 1
from functools import cmp_to_key
from pprint import pprint

klines.append([[2]])
klines.append([[6]])

klines.sort(key=cmp_to_key(c3))

a = klines.index([[2]])
b = klines.index([[6]])
print("part 2:",(a+1)*(b+1))
