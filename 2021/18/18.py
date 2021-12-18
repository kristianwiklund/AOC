#!/usr/bin/python3
import sys


IN = [eval(x.strip()) for x in sys.stdin]


s=[[6,[5,[4,[3,2]]]],1]

def lowboom(X):

    if type(X[0])==list and type(X[1])!=list:
        return ([0,X[1]+X[0][1]],X[0][0],None) # combine list, carry the leftmost value
    if type(X[1])==list and type(X[0])!=list:
        return ([X[0]+X[1][0], 0], None, X[1][1]) # combine list, carry the rightmost valu

    if type(X[0]) != list and type (X[1])!=list:
        return (X,None,None)

    print("lowboom",X)
    # these are two pairs
    # the left one explodes, and is added to the pair to the right which replaces both pairs
    LP = X[0]
    RP = X[1]
    
    return ([RP[0]+LP[1],0], LP[0], RP[1])

assert(lowboom([1,[2,3]])==([3,0],None, 3))
assert(lowboom([[1,2],3])==([0,5],1,None))
print(lowboom([[1,1],[2,2]]))
print(lowboom([0, [5, 8]]))
def notrightboom(X, nu):

    print("NRB",X,nu)
    if type(X) != list:
        return X

    if type(X[0]) !=list:
        return [X[0]+nu,X[1]]

    if type(X[1]) != list:
        return [X[0],X[1]+nu]

    print("----- dragons")
    print (X[0])
    return [notrightboom(X[0],nu),X[1]]

def boom(X,level):
    if type(X) != list: # should never end up here, but anyway...
        print("wtf")
        return None

    print(level, X)
    if level==3:
        R=lowboom(X)
        print("lowboom",R)
        return R
    
    if type(X[0]) == list and type(X[1])!=list:

        (NewL, vl, vr) = boom(X[0],level+1)
        if vr:
            NewR=X[1]+vr
            print("MR2",NewL, NewR)
            return ([NewL, NewR], vl, None)
        else:
            print("MR3",NewL, X[1])
            return ([NewL,X[1]], vl, vr)

    if type(X[0]) != list and type(X[1])==list:

        V = boom(X[1],level+1)
        print(V)
        (NewR, vl, vr) = V
        print(NewR)
        if vl:
            return ([X[0]+vl, NewR], None, vr)
        else:
            return ([X[0], NewR], vl, vr)

    if type(X[0]) != list and type(X[1])!= list:
        return (X, None, None)

    # out of the easy cases. if we get here, we may have to carry over the 
    # boom to the other side
    (NewLL,vll, vrl) = boom(X[0],level+1)
    if vrl:
        NewLR = notrightboom(X[1],vrl)
        print("nrb:",NewLR)
        return ([NewLL,NewLR],None,None)
    
    (NewLR,vlr, vrr) = boom(X[1],level+1)
        
    if vlr:
        print ("right boom carry over")

    return ([NewLL, NewLR], vll, vrr)

# ----- test code -----

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
(L,vl,vr)=boom([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],0)
assert(L==[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
(L,vl,vr)=boom([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],0)
assert(L==[[3,[2,[8,0]]],[9,[5,[7,0]]]])

(L, vl, vr)=boom([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]],0)
#print(L)
# all booms boom
assert(L==[[[[0,7],4],[15,[0,13]]],[1,1]])
#assert(L==[[[[0,7],4],[7,[[8,4],9]]],[1,1]])

(L, vl, vr)=boom([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]], 0)
assert(L==[[[[0,7],4],[[7,8],[6,0]]],[8,1]])

# ------ these were the explodes. now for the splits...

def split(X,splitted=False):

#    if not X:
#        print( X)
#        return (X,False)
    
    if type(X)!=list:
        if X>9 and not splitted:
            return ([X//2,X-X//2], True)
        else:
            return (X, splitted)

    (NL,splitted)=split(X[0],splitted)
    (NR,splitted)=split(X[1],splitted)
    return([NL,NR],splitted)

# ---- test code

(L, s) = split([[[[0,7],4],[15,[0,13]]],[1,1]])
#print(L)       
assert(L==[[[[0,7],4],[[7,8],[0,13]]],[1,1]])
(L, s) = split(L)
assert(L==[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])

def add(a,b):
    return [a,b]

# -- first test case for reducing a thing
L=add([[[[4,3],4],4],[7,[[8,4],9]]],[1,1])
(L,nl,nr)=boom(L,0)
(L,s)=split(L)
(L,s)=split(L)
(L,nl,nr)=boom(L,0)
assert(L==[[[[0,7],4],[[7,8],[6,0]]],[8,1]])

# end first tc

def dothething(L):

    ap=True

    while ap:
        print("boom", L)
        (L,nl,nr)=boom(L,0)
        print("split", L)
        (L,ap)=split(L)
    return L

L=add([[[[4,3],4],4],[7,[[8,4],9]]],[1,1])
L=dothething(L)
assert(L==[[[[0,7],4],[[7,8],[6,0]]],[8,1]])

V=add([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
L=dothething(V)
print(V)
print(L)
assert(L==[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
