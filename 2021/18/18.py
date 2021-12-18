#!/usr/bin/python3
import sys


L = [x.strip() for x in sys.stdin]

#print (L)

s=[[6,[5,[4,[3,2]]]],1]

def lowboom(X):
#    print("lowboom",X)
    if type(X[0])==list and type(X[1])!=list:
        return ([0,X[1]+X[0][1]],X[0][0],None) # combine list, carry the leftmost value
    if type(X[1])==list and type(X[0])!=list:
        return ([X[0]+X[1][0], 0], None, X[1][1]) # combine list, carry the rightmost valu
    return X

assert(lowboom([1,[2,3]])==([3,0],None, 3))
assert(lowboom([[1,2],3])==([0,5],1,None))

def boom(X,level):
    if type(X) != list: # should never end up here, but anyway...
        return

    #print(level, X)
    if level==3:
        R=lowboom(X)
#        print("lowboom",R)
        return R
    
    if type(X[0]) == list and type(X[1])!=list:

        (NewL, vl, vr) = boom(X[0],level+1)
        if vr:
            return ([NewL, X[1]+vr], vl, None)
        else:
            return ([NewL,X[1]], vl, vr)

    if type(X[0]) != list and type(X[1])==list:

        (NewL, vl, vr) = boom(X[1],level+1)
        if vl:
            return ([X[0]+vl, NewL], None, vr)
        else:
            return ([X[0], NewL], vl, vr)

    if type(X[0]) != list and type(X[1])!= list:
        return (X, None, None)

    (NewLL,vll, vrl) = boom(X[0],level+1)
    (NewLR,vlr, vrr) = boom(X[1],level+1)

    return ([NewLL, NewLR], vll, vrr)
    
(L,vl,vr)=boom([[[[[9,8],1],2],3],4],0)
assert(L==[[[[0,9],2],3],4])

(L,vl,vr)=boom([7,[6,[5,[4,[3,2]]]]],0)
assert(L==[7,[6,[5,[7,0]]]])

(L, vl, vr)=boom([[6,[5,[4,[3,2]]]],1],0)
assert(L==[[6,[5,[7,0]]],3])

# b0rked, because we need to handle the left hand side first,
# then we need to carry the right, and add it to the first left number
# this goes the other way around as well...
# if (one side explodes first, then the other side inherits the number)
V=boom([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],0)
print(V)
assert(L==[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
