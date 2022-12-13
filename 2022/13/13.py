# import sys
# sys.path.append("../..")
# from utilities import *

def comp(ls,rs, d=False):

    if d:
        print("<<>> c",ls,"<<>>",rs,"<<>>")


        
    if isinstance(ls,int) and isinstance(ls,int):
        if d:
            print("i-i comp",ls,rs)
        return ls<rs

    try:
        l=ls.pop(0)
    except:
        if d:
            print("--- l short")
        # run out of left first, order good
        return True

    try:
        r=rs.pop(0)
    except:
        if d:
            print("--- r short")
        # run out of right first, order bad
        return (False)

    if isinstance(l,int) and isinstance(r,int):
        if l>r:
            if d:
                print("--- int >")
            return (False)
        if l<r:
            if d:
                print("--- int <")
            return True
    
    if isinstance(r,list) and isinstance(l,int):
        l=[l]
        l.append(ls)
        r.append(rs)
        if d:
            print("--- a",l,r)
        return comp(l,r)

    if isinstance(l,list) and isinstance(r,int):
        r=[r]
        l.append(ls)
        r.append(rs)
        if d:
            print("--- a",l,r)        
        return comp(l,r)

    if isinstance(l,int) and isinstance(r,int):
        if l==r:
            if d:
                print("--- i=i retry",l,r,"-->",ls,rs)
            return(comp(ls,rs))

    if d:
        print("list,list=",isinstance(ls,list),isinstance(rs,list))
            
    if comp(l,r,d):
        return comp(ls,rs,d)
    else:
        return False
    


    return False

assert(comp([1,1,3,1,1], [1,1,5,1,1]))
assert(comp([[1],[2,3,4]], [[1],4]))
assert(not comp([9],[[8,7,6]]))
assert(comp([[4,4],4,4],[[4,4],4,4,4]))
assert(not comp([7,7,7,7],[7,7,7]))
assert(comp([],[3]))
assert(not comp([[[]]],[[]]))
assert(not comp([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]))

with open("input.debug") as fd:

    lines = [x.strip() for x in fd.readlines()]

    score=0
    cnt=0
    for i in range(0,len(lines),3):
        cnt+=1
        left = eval(lines[i])
        l=left
        right = eval(lines[i+1])
        r=right

        # chomp = i+2
        print("================================")
        try:
            if comp(l,r, d=True):
                score+=cnt
        except:
            print("crash")
            print(left)
            print(right)
            import sys
            sys.exit()
            
print("Part 1:",score)
            

        
    
