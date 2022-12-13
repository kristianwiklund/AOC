# import sys
# sys.path.append("../..")
# from utilities import *

def comp(ls,rs):

    print("-- c",ls,rs)

    if isinstance(ls,int) and isinstance(ls,int):
        return ls<rs

    try:
        l=ls.pop(0)
    except:
        # run out of left first, order good
        return True

    try:
        r=rs.pop(0)
    except:
        # run out of right first, order bad
        return (False)

    if isinstance(l,int) and isinstance(r,int):
        if l>r:
 #           print(">")
            return (False)
        if l<r:
 #           print("<")
            return True
    
    if isinstance(r,list) and isinstance(l,int):
#        print("pa",l,ls,r,rs)
                
        l=[l]
        l.append(ls)
        r.append(rs)
#        print("a",l,r)
        return comp(l,r)

    if isinstance(l,list) and isinstance(r,int):
 #       print("pa",l,ls,r,rs)
        r=[r]
        l.append(ls)
        r.append(rs)
#        print("a",l,r)        
        return comp(l,r)

    # both items are lists
    if isinstance(l,int) and isinstance(r,int):
        if l==r:
            return(comp(ls,rs))
    if comp(l,r):
        return comp(ls,rs)
    else:
        return False
        

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
        try:
            if comp(l,r):
                score+=cnt
        except:
            print("crash")
            print(left)
            print(right)
            import sys
            sys.exit()
            
print("Part 1:",score)
            

        
    
